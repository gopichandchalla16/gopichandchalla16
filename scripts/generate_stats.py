"""Build profile stat cards as SVG files, using the GitHub GraphQL API.

Runs inside GitHub Actions with the built in GITHUB_TOKEN, so it does not
depend on any third party card service. Needs only the Python standard library.
"""
import json
import os
import sys
import urllib.request
from collections import Counter
from html import escape

LOGIN = os.environ.get("LOGIN", "gopichandchalla16")
TOKEN = os.environ["GITHUB_TOKEN"]
OUT = os.environ.get("OUT_DIR", "assets")

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes { stargazerCount primaryLanguage { name color } }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
  }
}
"""

THEMES = {
    "light": dict(bg="#FFFFFF", border="#D0D7DE", title="#0D1626", text="#57606A", accent="#2243E6",
                  cells=["#EBEDF0", "#C6D2FA", "#8FA5F5", "#5471EE", "#2243E6"]),
    "dark": dict(bg="#0D1117", border="#30363D", title="#E6EDF3", text="#8B949E", accent="#7C93FF",
                 cells=["#161B22", "#1E2A5A", "#2F46A8", "#5470E6", "#8FA5FF"]),
}
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json",
                 "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if "errors" in data or not data.get("data", {}).get("user"):
        print(json.dumps(data)[:600], file=sys.stderr)
        sys.exit(1)
    return data["data"]["user"]


def card(w, h, t, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" font-family="{FONT}">'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>'
            f'{body}</svg>')


def stats_svg(u, t):
    repos = u["repositories"]["nodes"]
    cc = u["contributionsCollection"]
    stars = sum(r["stargazerCount"] for r in repos)
    rows = [
        ("Public repositories", u["repositories"]["totalCount"]),
        ("Stars received", stars),
        ("Followers", u["followers"]["totalCount"]),
        ("Commits, last 12 months", cc["totalCommitContributions"]),
        ("Pull requests, last 12 months", cc["totalPullRequestContributions"]),
    ]
    body = f'<text x="24" y="36" font-size="16" font-weight="600" fill="{t["title"]}">GitHub stats</text>'
    for i, (label, value) in enumerate(rows):
        y = 70 + i * 27
        body += (f'<text x="24" y="{y}" font-size="13" fill="{t["text"]}">{escape(label)}</text>'
                 f'<text x="371" y="{y}" font-size="14" font-weight="600" text-anchor="end" fill="{t["title"]}">{value}</text>')
    return card(395, 205, t, body)


def langs_svg(u, t):
    counts = Counter()
    colors = {}
    for r in u["repositories"]["nodes"]:
        pl = r["primaryLanguage"]
        if pl:
            counts[pl["name"]] += 1
            colors[pl["name"]] = pl["color"] or "#8B949E"
    top = counts.most_common(6)
    total = sum(counts.values()) or 1
    body = f'<text x="24" y="36" font-size="16" font-weight="600" fill="{t["title"]}">Languages by repository</text>'
    x = 24.0
    bar_w = 347.0
    body += f'<clipPath id="c"><rect x="24" y="48" width="{bar_w}" height="8" rx="4"/></clipPath><g clip-path="url(#c)">'
    for name, n in top:
        seg = bar_w * n / sum(c for _, c in top)
        body += f'<rect x="{x:.1f}" y="48" width="{seg:.1f}" height="8" fill="{colors[name]}"/>'
        x += seg
    body += "</g>"
    for i, (name, n) in enumerate(top):
        col, row = divmod(i, 3)
        cx, cy = 24 + col * 180, 84 + row * 26
        pct = 100 * n / total
        body += (f'<circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{colors[name]}"/>'
                 f'<text x="{cx+16}" y="{cy}" font-size="13" fill="{t["title"]}">{escape(name)}</text>'
                 f'<text x="{cx+160}" y="{cy}" font-size="12" text-anchor="end" fill="{t["text"]}">{pct:.0f}%</text>')
    return card(395, 170, t, body)


def heatmap_svg(u, t):
    cal = u["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    peak = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=0) or 1
    size, gap, left, top = 11, 3, 24, 52
    w = left * 2 + len(weeks) * (size + gap) - gap
    h = top + 7 * (size + gap) - gap + 30
    body = (f'<text x="24" y="32" font-size="16" font-weight="600" fill="{t["title"]}">Contributions, last 12 months</text>'
            f'<text x="{w-24}" y="32" font-size="13" text-anchor="end" fill="{t["text"]}">{cal["totalContributions"]} in total</text>')
    for i, wk in enumerate(weeks):
        for d in wk["contributionDays"]:
            n = d["contributionCount"]
            level = 0 if n == 0 else min(4, 1 + int(3 * (n - 1) / max(peak - 1, 1)))
            dow = __import__("datetime").date.fromisoformat(d["date"]).weekday()
            dow = (dow + 1) % 7  # Sunday first, like GitHub
            body += (f'<rect x="{left + i*(size+gap)}" y="{top + dow*(size+gap)}" width="{size}" height="{size}" rx="2" '
                     f'fill="{t["cells"][level]}"><title>{d["date"]}: {n}</title></rect>')
    return card(w, h, t, body)


def main():
    u = fetch()
    os.makedirs(OUT, exist_ok=True)
    for name, t in THEMES.items():
        for stem, fn in (("stats", stats_svg), ("languages", langs_svg), ("contributions", heatmap_svg)):
            with open(os.path.join(OUT, f"{stem}-{name}.svg"), "w", encoding="utf-8") as f:
                f.write(fn(u, t))
    print("written")


if __name__ == "__main__":
    main()

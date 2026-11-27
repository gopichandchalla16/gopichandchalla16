<div align="center">

# Gopichand Challa

### AI Engineer

LLM applications, multi agent systems and RAG pipelines in Python
<br/>
Guntur, India. Open to remote work and relocation.

<a href="mailto:gopichandchalla516@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/gopichandchalla"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://dev.to/gopichand_dev"><img src="https://img.shields.io/badge/DEV.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white"/></a>
<a href="https://x.com/GopichandAI"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white"/></a>

</div>

---

## At a glance

| | |
|---|---|
| **Role I am looking for** | AI Engineer, GenAI Engineer, LLM Application Developer |
| **What I do** | Build LLM apps, RAG pipelines and data services in Python |
| **Experience** | Two AI internships in 2025, ten AI projects with public code |
| **Education** | B.Tech, Computer Science and Engineering, 2024 |
| **Also learning** | Solana development with Rust and Anchor (Turbin3 Q3 2026 cohort, Solana Fall School) |
| **Reach me** | gopichandchalla516@gmail.com |

---

## About me

I am an AI engineer from Guntur, India. I graduated in 2024 with a B.Tech in Computer Science and Engineering, and in 2025 I completed two AI internships: Data Science with GenAI at Innomatics Research Labs, and AI at Infosys Springboard.

I like the part of AI work where a model has to fit inside a real service. That means structured outputs, a fallback for when an API call fails, authentication, and a deployment someone else can call. Most of my projects follow that pattern. Data comes in messy, an LLM or a model reads it, and the service returns a decision with a reason attached.

I learn by building and I keep my code public. Alongside the AI work, I am learning Solana development with Rust and Anchor. I was selected for Solana Fall School and I am part of the Turbin3 Q3 2026 Builders cohort. I am also working through 100 Days of Solana in public, at 78 of 100 days so far.

I am looking for an AI engineer role at an early stage company where I can build, ship and learn quickly. I can work remotely or relocate.

---

## Tech stack

<div align="center">

<img src="https://skillicons.dev/icons?i=py,fastapi,nextjs,ts,js,java,rust,mysql,postgres,mongodb,git,github,vercel&perline=13" alt="Tech stack icons"/>

</div>

| Area | Tools |
|---|---|
| **AI and ML** | Gemini API, OpenAI API, Whisper, LangChain, LangGraph, CrewAI, prompt engineering, embeddings, RAG, scikit-learn, Prophet, ARIMA |
| **Languages** | Python, SQL, TypeScript, JavaScript, Java, Rust |
| **Backend** | FastAPI, REST APIs, Pydantic, API key auth, Next.js, Streamlit |
| **Data** | Pandas, NumPy, Plotly, Matplotlib, PostgreSQL, MySQL, MongoDB, feedparser, yfinance |
| **Web3** | Solana, Anchor, Token-2022, PDAs, CPIs, LiteSVM |
| **Tools and hosting** | Git, GitHub, Jupyter, Google Colab, Vercel, Render |

---

## Featured AI projects

<table>
<tr>
<td width="50%" valign="top">

### StockSense AI
**Multi agent platform for Indian stocks**

A LangGraph workflow that coordinates eight agents: news sentiment, chart patterns, FII and DII flows, IPO analysis, opportunity signals, a morning briefing, market explanations and a portfolio chat. An LLM router calls Gemini and falls back to Hugging Face. Streamlit and Plotly front end. Built with a team for the ET GenAI Hackathon 2026.

`Python` `LangGraph` `Gemini` `Streamlit` `Plotly`

[Source](https://github.com/gopichandchalla16/StockSense-AI) | [Live demo](https://stocksense-neuralforge.streamlit.app/)

</td>
<td width="50%" valign="top">

### AI-Sentinel
**LLM risk analyzer for Solana**

Sends on-chain data from Helius to Gemini with structured prompts and parses the JSON risk verdict. Six API routes cover analysis, wallet profiling, program scan, threat feed, follow up chat and wallet history. A rule based fallback runs if the LLM call or parsing fails. Colosseum Frontier Hackathon 2026.

`Next.js` `TypeScript` `Gemini` `Vercel`

[Source](https://github.com/gopichandchalla16/AI-Sentinel) | [Live demo](https://ai-sentinel-three.vercel.app)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### NovaAI Nexus
**Scam detection honeypot API**

FastAPI service that checks messages for scams and phishing, keeps multi turn sessions, and returns JSON with signals, confidence and a reason. Detection is rule based. Regex pulls out UPI IDs, bank accounts and phishing links, and results post to the organiser's callback endpoint. India AI Impact Buildathon 2026.

`Python` `FastAPI` `Pydantic` `Render`

[Source](https://github.com/gopichandchalla16/novaai-nexus-honeypot) | [API docs](https://novaai-nexus-honeypot.onrender.com/docs)

</td>
<td width="50%" valign="top">

### Real-Time Industry Insight System
**Market sentiment and forecasting pipeline**

Built in a team of four during my Infosys Springboard internship. Pulls Google News RSS and Yahoo Finance data, scores sentiment with Gemini from -100 to +100, forecasts with Prophet, and produces a rule based BUY, SELL or HOLD signal. Plotly and Streamlit dashboard with Slack alerts.

`Python` `Gemini` `Prophet` `Streamlit`

[Source](https://github.com/gopichandchalla16/infosys-internship-real-time-industry-insight-system)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Project Samarth
**Q&A across climate and crop data**

A Streamlit app where Python data tools pull from IMD climate data and a crop production dataset, and Gemini writes a policy brief that must cite the source dataset for each claim. Built for the Build For Bharat fellowship task.

`Python` `Pandas` `Gemini` `Streamlit`

[Source](https://github.com/gopichandchalla16/Project_Samarth_Prototype) | [Live demo](https://samarth-data-insights.streamlit.app/)

</td>
<td width="50%" valign="top">

### Search My Subtitles
**Audio to subtitles with Whisper**

A Streamlit app that turns MP3, WAV and M4A files into SRT subtitles with OpenAI Whisper, then lets you search the text.

`Python` `Whisper` `Streamlit`

[Source](https://github.com/gopichandchalla16/Enhancing-Search-Engine-Relevance-for-Video-Subtitles) | [Live demo](https://searchmysubtitles.streamlit.app/)

</td>
</tr>
</table>

### More AI work

- [CognitoSync](https://github.com/gopichandchalla16/CardanoNovachain-Nexus): knowledge verification agent built with CrewAI, Masumi and Cardano at the Cardano Hackathon Asia 2025.
- [AI Medical Diagnosis System](https://github.com/gopichandchalla16/AI-Medical-Diagnosis-System): Streamlit app with trained machine learning models that predict health risks from input data. A demo, not medical advice. [Live demo](https://smarthealthstream.streamlit.app/)
- [AI Code Reviewer](https://github.com/gopichandchalla16/AI-Code-Reviewer): run Python and ask Gemini to explain or debug it. [Demo](https://syntax-surgeon.streamlit.app/)
- [AI Travel Planner](https://github.com/gopichandchalla16/AI-Travel-Planner): Gemini trip itineraries in Streamlit. [Demo](https://smartai-trip-planner.streamlit.app/)

---

## How my projects work

The Infosys system, as an example of how I build: take messy input, get a structured result, and keep working when a part fails.

```mermaid
flowchart LR
    A[Google News RSS<br/>Yahoo Finance] --> B[Python pipeline]
    B --> C{Gemini sentiment<br/>-100 to +100}
    C -->|API fails| D[Lexicon scorer]
    C --> E[Prophet forecast]
    D --> E
    E -->|model fails| F[ARIMA fallback]
    E --> G[Rule based signal<br/>BUY, SELL or HOLD]
    F --> G
    G --> H[Plotly and Streamlit dashboard<br/>Slack alerts]
```

---

## Experience

| When | Role | What I did |
|---|---|---|
| **Oct 2025 to Dec 2025** | **AI Intern, Infosys Springboard** | Worked on a Python market intelligence pipeline with a team of four. Built Gemini sentiment scoring with an automatic fallback, added Prophet forecasting with an ARIMA fallback, and delivered a Plotly and Streamlit dashboard with Slack alerts. |
| **Jan 2025 to Apr 2025** | **Data Science with GenAI Intern, Innomatics Research Labs** | Built LLM apps and chatbots with LangChain, OpenAI APIs and Streamlit. Used prompt engineering, embeddings and RAG, and trained and evaluated models with scikit-learn, Pandas and NumPy. |

---

## Solana and Web3

I build on Solana as a second track. The Rust and Anchor work comes from the Turbin3 cohort and Solana Fall School.

| Project | What it is |
|---|---|
| [Solana Escrow](https://github.com/gopichandchalla16/turbin3-escrow-q3-26) | Token swap program in Rust and Anchor with refunds, updates and expiry. Works with SPL Token and Token-2022. |
| [Transfer Hook](https://github.com/gopichandchalla16/solana-fall-transfer-hook) | Token-2022 transfer hook that rate limits transfers using PDA state and CPIs. |
| [100 Days of Solana](https://github.com/gopichandchalla16/100-days-of-solana) | Public build log, 78 of 100 days so far. |
| [PrivateCredit AI](https://github.com/gopichandchalla16/privatecredit-ai-midnight) | Prototype where AI scores credit data and a lender checks a threshold result without seeing the data. Uses Midnight and ZK. |
| [TipLink Live](https://github.com/gopichandchalla16/tiplink-live) | Creator tipping app in Next.js with Solana Actions routes and Gemini thank you messages. |

---

## Certifications

<div align="center">

<img src="https://img.shields.io/badge/Claude_Code_in_Action-Anthropic,_Mar_2026-D97757?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OCI_2025_Generative_AI_Professional-Oracle,_Aug_2025-C74634?style=for-the-badge&logo=oracle&logoColor=white"/>
<img src="https://img.shields.io/badge/Data_Analyst_Professional_Certificate-Meta,_Dec_2024-0866FF?style=for-the-badge&logo=meta&logoColor=white"/>

</div>

---

## GitHub activity

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=gopichandchalla16&show_icons=true&hide_border=true&theme=tokyonight&include_all_commits=true" height="170" alt="GitHub stats"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=gopichandchalla16&layout=compact&hide_border=true&theme=tokyonight&langs_count=8" height="170" alt="Top languages"/>

<img src="https://streak-stats.demolab.com?user=gopichandchalla16&theme=tokyonight&hide_border=true" alt="Contribution streak"/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=gopichandchalla16&theme=tokyo-night&hide_border=true&area=true" width="100%" alt="Contribution graph"/>

</div>

---

## Writing

- [CPI on Solana: The Mental Model I Wish I Had on Day 71](https://dev.to/gopichand_dev/cpi-on-solana-the-mental-model-i-wish-i-had-on-day-71-ceh)
- [What I Learned About PDAs in a Week of Building on Solana](https://dev.to/gopichand_dev/what-i-learned-about-pdas-in-a-week-of-building-on-solana-4n9b)

---

## Let's talk

If you are hiring for an AI engineer role, or building something with LLMs, I would like to hear about it. Email is the fastest way to reach me.

<div align="center">

<a href="mailto:gopichandchalla516@gmail.com"><img src="https://img.shields.io/badge/Email_me-gopichandchalla516@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/gopichandchalla"><img src="https://img.shields.io/badge/Message_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>


</div>

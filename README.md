<!--
  Profile README for github.com/Mokshitsharma
  GitHub username used by the live stats cards below: Mokshitsharma
  To change it, find and replace "Mokshitsharma" in this file (stats section and links only).
  Photo: replace assets/profile-photo-placeholder.svg. See README-ASSETS.md.
-->

<p align="center">
  <img src="assets/hero-banner.svg" width="100%" alt="Mokshit Sharma, AI/ML Engineer and Agentic AI Developer, Indore, India. Banner shows an agent graph: task, plan, retrieve and tools, a verify step, then act." />
</p>

<p align="center">
  <a href="https://mokshitsharma27.vercel.app/"><img src="assets/links/portfolio.svg" height="40" alt="Portfolio" /></a>&nbsp;
  <a href="https://www.linkedin.com/in/mokshit-sharma-75b5ab305"><img src="assets/links/linkedin.svg" height="40" alt="LinkedIn" /></a>&nbsp;
  <a href="https://github.com/Mokshitsharma"><img src="assets/links/github.svg" height="40" alt="GitHub" /></a>&nbsp;
  <a href="mailto:mokshitsharmalaptop@gmail.com"><img src="assets/links/email.svg" height="40" alt="Email" /></a>
</p>

<img src="assets/profile-photo-placeholder.svg" align="right" width="190" height="190" alt="Profile photo of Mokshit Sharma (placeholder)" />

## About

- Integrated B.Tech + M.Tech in **Artificial Intelligence & Data Science** at DAVV, Indore. CGPA 8.2, graduating 2028.
- **Founding Engineer (AI/ML) at Movigo**, a live B2B logistics marketplace in Indore. I built its core platform, an AI voice agent and the surge-pricing model.
- I build **LLM and agentic systems** that check their own work: cited RAG answers, guarded agent payouts, MCP servers tested against real APIs.
- I like the architecture under the model: how requests flow, where a system fails and how to make it recover.
- Goal: production AI systems people can trust with real work.

<br clear="right" />

## Current focus

<img src="assets/current-focus.svg" width="100%" alt="Current focus. Agents and LLMs: agentic AI, multi-agent architectures, LLM applications, RAG pipelines. ML and systems: machine learning, data science, AI engineering, system design." />

<img src="assets/dividers/divider.svg" width="100%" alt="" />

## Featured projects

<table>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/settleai"><img src="assets/project-thumbnails/settleai.svg" width="100%" alt="SettleAI flow: signed mandate, scoping agent, proof checks, Mandate Guard, PayPal payout, signed receipt" /></a>

### SettleAI
Escrow for real-world work that AI agents hire people to do. Built for the PayPal AI Hackathon 2026.

**Problem:** an agent paying a person needs proof the work was done and a clear answer on who is liable when it was not.

**Approach:** AI agents scope jobs and check photo proof; a deterministic Mandate Guard approves every payout; every step becomes a signed receipt that verifies offline.

**Stack:** TypeScript, Next.js, PostgreSQL (PGlite), PayPal, Groq models, MCP

**Results (offline eval):** 28/28 scenarios passed, 0 of 8 bad proofs paid, 49/49 receipt tampering attempts detected

[Repository](https://github.com/Mokshitsharma/settleai) · [Live demo](https://settleai-07ue.onrender.com) · [Screenshot](https://github.com/Mokshitsharma/settleai/blob/HEAD/docs/devpost/2-denied-before-money-moves.png)

</td>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/docIQ"><img src="assets/project-thumbnails/dociq.svg" width="100%" alt="docIQ RAG pipeline: upload, parse and chunk, embed, retrieve, grounded answer, citations" /></a>

### docIQ
RAG document intelligence: ask questions of contracts and invoices and get answers cited to the source.

**Problem:** key terms are buried in long documents, and an uncited AI answer can't be trusted.

**Approach:** parse, chunk and embed; vector or hybrid retrieval; grounded answers that refuse out-of-scope questions; automatic risk and clause extraction. Runs offline with no API keys.

**Stack:** Node.js, Express, MongoDB, Next.js, Chroma, BullMQ/Redis, Gemini/Groq

**Results:** 16/16 end-to-end checks pass

[Repository](https://github.com/Mokshitsharma/docIQ)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/ToolForge"><img src="assets/project-thumbnails/toolforge.svg" width="100%" alt="ToolForge LangGraph flow: OpenAPI spec, design, check plan, human review, generate and validate, live test, security audit, scorecard, with feedback loops to design" /></a>

### ToolForge
Agents that turn an OpenAPI spec into a tested, security-audited MCP server.

**Problem:** thousands of APIs have no MCP server, and writing one by hand is repetitive.

**Approach:** a LangGraph state machine: an LLM designs the tools, a human approves, a tester agent uses the server against the live API, and design problems loop back to the designer. Every build ends with a security audit and a scorecard.

**Stack:** Python, LangGraph, MCP, Groq / Gemini / Claude

**Results:** PokéAPI 8/8 live tests and 100/100 security; Petstore 6/8 after a redesign fixed 2 design bugs

[Repository](https://github.com/Mokshitsharma/ToolForge)

</td>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/naman-jarvis"><img src="assets/project-thumbnails/naman.svg" width="100%" alt="Naman voice assistant: wake word, speech to text, router, LangGraph agent, approval step, tools" /></a>

### Naman
A voice-controlled AI assistant for a Windows laptop and Telegram.

**Problem:** everyday laptop control, task tracking and job hunting take many small manual steps.

**Approach:** offline wake word, Groq speech to text, a router over skill packs and a LangGraph agent with memory. Risky actions wait for approval in their own graph step. Supports MCP servers.

**Stack:** Python, LangGraph, Groq, Whisper, MCP, Telegram

**Runs on:** free tiers

[Repository](https://github.com/Mokshitsharma/naman-jarvis)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/system-design-atlas"><img src="assets/project-thumbnails/system-design-atlas.svg" width="100%" alt="System Design Atlas: an interactive diagram where a request travels from rider app through gateway and services" /></a>

### System Design Atlas
Beginner-friendly system design tutorials: how apps like Uber, Netflix, IRCTC and Rapido could be designed.

**Problem:** most system design material assumes you already know the vocabulary.

**Approach:** nine-section tutorials with interactive workflow diagrams, failure views, capacity calculators and every claim labelled Public, Inferred or Assumption.

**Stack:** Next.js 16, React 19, TypeScript, Zod, custom SVG diagram engine, Vitest, Playwright

**Scope:** 6 tutorials, 121 platforms, 25 architecture patterns

[Repository](https://github.com/Mokshitsharma/system-design-atlas) · [Live site](https://sdatlas.vercel.app/)

</td>
<td width="50%" valign="top">

<a href="https://github.com/Mokshitsharma/Customer_Churn_using_XAI"><img src="assets/project-thumbnails/churn-xai.svg" width="100%" alt="Customer churn with explainable AI: telco data, XGBoost, SHAP, plain-language reasons, retention actions, Streamlit dashboard" /></a>

### Customer churn with explainable AI
Predicts which customers will churn, explains why and suggests what to do.

**Problem:** a churn score alone doesn't tell a retention team what to act on.

**Approach:** XGBoost for risk; SHAP TreeExplainer for per-customer reasons, turned into plain language and mapped to retention actions.

**Stack:** Python, XGBoost, SHAP, scikit-learn, Streamlit

**Data:** telecom dataset, ~7K customers, 19 features

[Repository](https://github.com/Mokshitsharma/Customer_Churn_using_XAI) · [Live demo](https://customer-churn-explanation.streamlit.app/)

</td>
</tr>
</table>

<img src="assets/dividers/divider.svg" width="100%" alt="" />

## Experience

### Movigo Innovations Pvt. Ltd.
**Founding Engineer (AI/ML)** · Apr 2026 – Present · Indore

A live B2B intra-city logistics marketplace. The codebase is private, so this is a high-level view only.

<img src="assets/architecture/movigo.svg" width="100%" alt="Movigo high-level architecture: retailer and driver apps feed a core platform of bookings, dispatch and an ML surge-pricing model; an AI voice agent resolves about 81% of support calls and escalates the rest." />

- Built the core platform from zero and designed the system architecture
- Built an AI voice agent that resolves ~81% of inbound support calls
- Built the surge-pricing model; improved driver availability and dispatch
- Review code written by 2 full-stack engineers and by AI coding tools

### Kangaroo Software
**Data Scientist Intern** · Dec 2025 – Feb 2026

Built chatbots and ML solutions for client projects.

### Evoastra Ventures
**Artificial Intelligence Intern** · Oct 2024 – Nov 2024

### Cognifyz Technologies
**Data Scientist Intern** · Sep 2024 – Oct 2024

<img src="assets/dividers/divider.svg" width="100%" alt="" />

## Technical skills

<table>
<tr><td width="190"><b>Languages</b></td><td><img src="https://skillicons.dev/icons?i=py,ts,js,java,r&theme=dark" height="40" alt="Python, TypeScript, JavaScript, Java, R" /><br/>SQL</td></tr>
<tr><td><b>AI / ML</b></td><td><img src="https://skillicons.dev/icons?i=sklearn,pytorch&theme=dark" height="40" alt="scikit-learn, PyTorch" /><br/>XGBoost, LightGBM, CatBoost, SHAP</td></tr>
<tr><td><b>GenAI / LLMs</b></td><td>RAG, embeddings, hybrid retrieval, Chroma, Groq, Gemini, Claude</td></tr>
<tr><td><b>Agentic AI</b></td><td>LangGraph, MCP, tool design, human-in-the-loop approval, agent evaluation</td></tr>
<tr><td><b>Data science</b></td><td>pandas, NumPy, Plotly, Streamlit, Power BI</td></tr>
<tr><td><b>Databases</b></td><td><img src="https://skillicons.dev/icons?i=postgres,mongodb,sqlite,redis&theme=dark" height="40" alt="PostgreSQL, MongoDB, SQLite, Redis" /></td></tr>
<tr><td><b>Cloud & infra</b></td><td><img src="https://skillicons.dev/icons?i=docker,vercel&theme=dark" height="40" alt="Docker, Vercel" /><br/>Render, Streamlit Community Cloud</td></tr>
<tr><td><b>Tools</b></td><td><img src="https://skillicons.dev/icons?i=git,github,vscode,nodejs&theme=dark" height="40" alt="Git, GitHub, VS Code, Node.js" /></td></tr>
</table>

<sub>Familiar with: AWS (studying for MLA-C02), Flask, Express, Next.js, Playwright, Vitest</sub>

## GitHub activity

<!-- Live cards. Public repos only. Username: Mokshitsharma -->
<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Mokshitsharma&theme=nord_dark" height="165" alt="GitHub stats for Mokshitsharma" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Mokshitsharma&theme=nord_dark" height="165" alt="Top languages by repository for Mokshitsharma" />
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=Mokshitsharma&background=0B1628&border=1E2D45&stroke=1E2D45&ring=2F81F7&fire=22D3EE&currStreakNum=E6EDF7&sideNums=E6EDF7&currStreakLabel=22D3EE&sideLabels=8A9BB5&dates=8A9BB5&disable_animations=true" height="165" alt="Contribution streak for Mokshitsharma" />
</p>
<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Mokshitsharma&theme=nord_dark" width="100%" alt="Contribution activity for Mokshitsharma" />
</p>

<img src="assets/dividers/divider.svg" width="100%" alt="" />

## Certifications and hackathons

<table>
<tr>
<td width="50%" valign="top">

**Certifications**

- [5-Day AI Agents Intensive](https://drive.google.com/file/d/1NmhjV9PXbdtnp09OdMNtMaizlODUNfke/view?usp=sharing) · Google and Kaggle · Dec 2025
- [Generative AI Foundations](https://drive.google.com/file/d/12LL5X1XFkZa-KYVSoCFUJZ7zyR9aB1wr/view?usp=sharing) · Skillsoft · Nov 2025
- [Generative AI Foundations: IT Integration with Generative AI](https://drive.google.com/file/d/1FGNt8vyrA4aseMvbjoMUgsXYuAgrszPy/view?usp=sharing) · Infosys Springboard · Nov 2024
- [Excel](https://drive.google.com/file/d/1C0E6VwPqfuZyaZkvkLYWOFl5JvfWJ48R/view?usp=sharing) · Infosys Springboard · Nov 2024

In progress: AWS Certified Machine Learning Engineer – Associate (MLA-C02)

</td>
<td width="50%" valign="top">

**Hackathons and competitions**

- **PayPal AI Hackathon 2026**: participant with [SettleAI](https://github.com/Mokshitsharma/settleai)
- **Kaggle Playground Series**: two [competition entries](https://github.com/Mokshitsharma/Kaggle-Competitions)

</td>
</tr>
</table>

## Currently learning and building

- Advanced AI engineering
- Multi-agent systems and LLM architecture
- Production AI systems, cloud and system design
- Preparing for AWS Certified Machine Learning Engineer – Associate

<img src="assets/dividers/divider.svg" width="100%" alt="" />

<p align="center">
  <b>Building AI agents, RAG or ML systems? Let's talk.</b><br/>
  <sub>Indore, India · IST (UTC+5:30)</sub>
</p>

<p align="center">
  <a href="https://mokshitsharma27.vercel.app/">mokshitsharma27.vercel.app</a> ·
  <a href="https://www.linkedin.com/in/mokshit-sharma-75b5ab305">LinkedIn</a> ·
  <a href="https://github.com/Mokshitsharma">GitHub</a> ·
  <a href="mailto:mokshitsharmalaptop@gmail.com">mokshitsharmalaptop@gmail.com</a>
</p>

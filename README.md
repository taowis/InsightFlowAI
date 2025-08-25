# InsightFlowAI

**InsightFlowAI** is a monorepo for **AI-powered client reporting and operations automation**, built for digital marketing agencies.  
It streamlines the reporting workflow, automates repetitive finance/ops tasks, and provides AI-generated insights with human-in-the-loop review.

---

## 🔧 Features
- **Automated client reporting**
  - Connect to Google Ads, GA4, Meta Ads, HubSpot (connectors in progress)
  - Standardized KPI calculations (CTR, CPC, CPA, ROAS)
  - Generate branded reports in PPTX/PDF or Google Slides
  - AI-generated narratives and recommendations
- **Multi-agent workflows**
  - Data Agent → Insight Agent → Validation Agent → Report Agent
- **Integrations**
  - Slack notifications, Google Drive export, HubSpot sync
- **Operational automations (planned)**
  - Invoicing automation (OCR + finance system integration)
  - Budget pacing alerts & anomaly detection
- **Human-in-the-loop**
  - Streamlit admin console for draft review and approvals
- **Cloud-ready**
  - Designed for Google Cloud Run + Cloud SQL / BigQuery
  - Workspace API integration for Slides/Docs/Drive

---

## 📂 Repository Structure
- **backend/** – FastAPI services: connectors, ETL, LLM insights, reporting, agents  
- **admin/** – Streamlit internal console (for AM/AE to generate/approve/export reports)  
- **packages/common-python/** – Shared Python utilities (KPI calculations, theming, prompt templates)  
- **db/** – Database schema (Postgres/SQLite)  
- **configs/** – Environment variable examples (`.env.example`)  
- **docs/** – User guide and cloud deployment notes  

---

## 🚀 Quickstart

```bash
# Backend
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload

# Admin (internal console)
pip install -r admin/requirements.txt
streamlit run admin/Home.py

# Optional: Postgres
docker compose up -d
```

---

## ☁️ Cloud Deployment (Google Cloud Run)

- Containerize backend and admin apps  
- Use **Cloud SQL (Postgres)** or **BigQuery** for data storage  
- Store exported reports in **Google Drive** or **Cloud Storage**  
- Authenticate via **Service Accounts / OAuth** for Workspace APIs  

👉 See **docs/CloudDeploy_GCP.md** for detailed deployment steps.

---

## 🤖 LLM Provider Switch (OpenAI vs Azure OpenAI)

InsightFlowAI supports both **OpenAI API** and **Azure OpenAI** with a simple environment switch:

```bash
# Default: OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini

# Azure OpenAI
LLM_PROVIDER=azure
AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com/
AZURE_OPENAI_KEY=...
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=gpt4o-mini
```

All chat completions are routed through `backend/llm/provider_router.py`, so business logic is provider-agnostic.

---

## 🗺️ Roadmap Highlights
- ✅ End-to-end reporting automation MVP  
- 🔄 Real Google Ads & GA4 connectors  
- 🔄 Multi-agent orchestration (CrewAI / AutoGen)  
- 🔄 Invoicing automation + budget pacing monitor  
- 🔄 Slack / Drive / HubSpot integrations  
- 🔄 Client-facing portal (Next.js + Looker Studio integration)  

---

## 📖 Documentation
- **docs/UserGuide.md** – Step-by-step user guide for AM/AE teams  
- **docs/CloudDeploy_GCP.md** – Cloud deployment guide (Google Cloud Run)  
- **docs/Providers.md** – LLM provider configuration (OpenAI vs Azure)  

---

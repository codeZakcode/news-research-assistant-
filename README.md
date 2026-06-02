# News Research Assistant
**Capstone Project 06** — RAG · MCP · Agents · Evals · 7-Day Plan · 3 Members

An agentic news research assistant that ingests articles from multiple sources, retrieves the most relevant content for any research question, and generates cited, multi-source summaries.

## Team
| Member | Responsibility |
|--------|---------------|
| Member A | RAG Pipeline (`ingestion/`) |
| Member B | Agent + MCP + UI (`agent/`, `ui/`) |
| Member C | Evals (`evals/`) |

## Project Structure
```
news-research-assistant/
├── ingestion/      # Member A — RSS fetch, clean, chunk, embed, store
├── agent/          # Member B — MCP tools, agent reasoning loop
├── evals/          # Member C — Retrieval, answer, citation, agent evals
├── ui/             # Member B — Streamlit frontend
├── data/           # Shared schemas, sample eval queries
├── .env.example    # API key template (copy to .env)
└── requirements.txt
```

## Setup
```bash
git clone https://github.com/subhanalisha/news-research-assistant.git
cd news-research-assistant
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # Add your API keys
```

## Branch Strategy
```
main      ← stable, demo-ready
dev       ← integration branch
feat/rag      ← Member A
feat/agent    ← Member B
feat/evals    ← Member C
```

## Tech Stack
- **Fetching:** feedparser, NewsAPI, newspaper3k
- **Vector DB:** ChromaDB (local)
- **Embeddings:** text-embedding-3-small or all-MiniLM-L6-v2
- **Agent LLM:** Claude Sonnet / GPT-4o-mini
- **UI:** Streamlit
- **Evals:** Custom Python harness

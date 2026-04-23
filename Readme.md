# 📚 Automated Book Publication Workflow

An end-to-end, modular pipeline that automates the scraping, AI-powered rewriting, human review, and versioning of online book chapters — with a reinforcement learning feedback loop baked in.

---

## 🧠 Overview

This project simulates a real-world book publication pipeline where AI agents and humans collaborate to produce polished content. A chapter is fetched from the web, rewritten by an LLM, reviewed by another AI agent, presented to a human editor for final approval, and then stored — with every accept/reject decision feeding back into a reward model.

```
Scrape Chapter → AI Rewrite → AI Review → Human Edit → Store Version → RL Feedback
```

---

## ✨ Features

- **Web Scraping with Screenshots** — Fetches chapter content from any URL using Playwright and BeautifulSoup
- **AI Writing Agent** — Rewrites (spins) raw scraped text using instruction-tuned LLMs via Hugging Face Transformers
- **AI Reviewing Agent** — A second LLM pass that critiques and refines the spun text before human review
- **Human-in-the-Loop Editing** — Presents the AI-generated content to a human editor who can accept, reject, or modify it
- **RL Reward Feedback** — Accept/reject decisions are passed to a reward model, simulating a reinforcement learning training loop
- **Content Versioning** — Finalized chapters are stored with version tags via ChromaDB for traceability and future semantic search
- **Agentic & Modular Architecture** — Each module is self-contained and can be extended into a standalone API or microservice

---

## 🗂️ Project Structure

```
Automated-Book-Publication-Workflow/
│
├── main.py                  # Entry point — orchestrates the full pipeline
├── requirements.txt
│
├── Scraping/
│   └── fetcher.py           # Playwright + BeautifulSoup web scraper
│
├── Ai_writer/
│   ├── writer.py            # LLM-based text rewriting (spinning)
│   └── reviewer.py          # LLM-based review and refinement
│
├── human_loop/
│   └── edit_interface.py    # CLI/UI for human editor to accept/reject/edit
│
├── chroma_search/
│   └── version_store.py     # ChromaDB-backed versioning and semantic search
│
├── rl/
│   ├── reward_model.py      # Computes reward from human feedback
│   └── trainer.py           # Updates policy based on reward signal
│
├── agent_api/               # (Extensible) FastAPI layer for agentic access
├── data/                    # Local data storage
└── utils/                   # Shared utilities
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/AliSayyed123/Automated-Book-Publication-Workflow.git
cd Automated-Book-Publication-Workflow
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**
```bash
playwright install
```

---

## 🚀 Usage

Run the full pipeline with:

```bash
python main.py
```

By default, the pipeline targets a sample chapter from Wikisource:
```
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
```

To process a different chapter, update the `URL` variable in `main.py`:
```python
URL = "https://your-target-chapter-url.com"
```

### Pipeline Flow

1. `fetch_chapter(URL)` — Scrapes and extracts raw chapter text
2. `spin_text(raw_text)` — AI rewrites the content
3. `review_text(spun)` — AI reviews and refines the rewrite
4. `present_for_editing(reviewed)` — Human editor accepts, edits, or rejects
5. `store_version(final, version_tag)` — Stores the approved chapter in ChromaDB
6. `compute_reward(...)` + `update_policy(reward)` — RL feedback loop updates the model

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Web Scraping | [Playwright](https://playwright.dev/python/), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) |
| AI Writing & Review | [Hugging Face Transformers](https://huggingface.co/docs/transformers/), PyTorch |
| Vector Storage | [ChromaDB](https://www.trychroma.com/), Sentence Transformers |
| API Layer | [FastAPI](https://fastapi.tiangolo.com/), Uvicorn |
| Language | Python 3.10+ |

---

## 🔮 Roadmap

- [ ] Swap stub RL trainer with a real RLHF training loop
- [ ] Add a web-based human editing interface (FastAPI + frontend)
- [ ] Expand ChromaDB integration for full semantic chapter search
- [ ] Support batch processing of multiple chapters
- [ ] Add export to EPUB / PDF format

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Add a `LICENSE` file to specify terms.

---

## 👤 Author

**Ali Sayyed** — [@AliSayyed123](https://github.com/AliSayyed123)

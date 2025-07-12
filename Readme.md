# Automated Book Publication Workflow

This project implements a modular pipeline to automate the scraping, rewriting, and review of online book chapters with human-in-the-loop collaboration. It integrates AI writing and reviewing agents, human feedback loops, reinforcement-based decision logic, and support for versioning and future semantic search.

## Features

- **Web scraping with screenshots**: Extracts chapter content from a given URL using Playwright and BeautifulSoup.
- **AI Writing and Reviewing**: Uses instruction-tuned large language models (LLMs) to rewrite ("spin") chapters and optionally refine them.
- **Human-in-the-loop editing**: Enables users to accept, reject, or edit AI-generated content before finalizing.
- **Reward-based decision loop**: Accept/reject actions are passed to a reward model for feedback, simulating reinforcement learning inference.
- **Versioning support**: Saves chapter versions for traceability and future comparison.
- **Agentic flow**: Each functional step is isolated and can be expanded into callable APIs or microservices.

## Technologies Used

- Python 3.10+
- [Playwright](https://playwright.dev/python/) for web scraping and screenshots
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for LLM-based rewriting
- [ChromaDB](https://www.trychroma.com/) (planned or stubbed) for vector-based content versioning and semantic search
- Custom reward logic simulating an RL feedback loop




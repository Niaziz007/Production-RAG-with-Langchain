# Production RAG Masterclass

**Build, debug, optimize, and scale Retrieval-Augmented Generation systems for production.**

> *"You followed a RAG tutorial. It worked on 10 documents. Then you tried 10,000 — and everything broke."*

Most RAG tutorials stop at the happy path. This course covers what they skip: **why the majority of RAG projects fail in production, and how to fix them.**

---

## Table of Contents

- [What You'll Learn](#what-youll-learn)
- [The 5 RAG Failure Modes](#the-5-rag-failure-modes)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Course Structure](#course-structure)
- [Part 6: Advanced RAG 2026](#part-6-advanced-rag-2026)
- [Prerequisites](#prerequisites)
- [Free Resources](#free-resources)
- [Community](#community)
- [About the Instructor](#about-the-instructor)
- [FAQ](#faq)
- [License](#license)
- [Support](#support)

---

## What You'll Learn

| Part | Topic | What You'll Build |
|------|-------|-------------------|
| **1** | Build the Foundation | A complete RAG pipeline from scratch |
| **2** | Debug RAG Failures | Fixes for the 5 failure modes that break most RAG systems |
| **3** | Optimize for Quality | Semantic chunking, reranking, multi-query retrieval |
| **4** | Scale for Production | Caching, monitoring, production vector databases |
| **5** | Production Project | A full, production-ready RAG application |
| **6** | Advanced RAG 2026 | Agentic RAG, GraphRAG, Contextual Retrieval, Multimodal |

---

## The 5 RAG Failure Modes

Most RAG projects fail for the same five reasons. This course teaches you to diagnose and fix each one.

| # | Failure Mode | What Happens | The Fix |
|---|--------------|--------------|---------|
| 1 | **Bad Chunking** | Wrong context retrieved; chunks split mid-sentence | Semantic chunking, smart overlap |
| 2 | **Embedding Mismatch** | User says *"cancel"*, docs say *"termination policy"* | Query rewriting, hybrid search |
| 3 | **Retrieval Noise** | 10 docs retrieved, only 2 are relevant | Reranking, filtering |
| 4 | **Context Overflow** | Too much stuffed into the prompt; the LLM ignores half | Smart truncation, map-reduce |
| 5 | **Hallucination** | The answer is in context, but the LLM makes things up | Constrained prompts, citations |

---

## Tech Stack

| Component | Choice |
|-----------|--------|
| Language | Python 3.10+ |
| Framework | LangChain 1.x (2026 stable release) |
| Agents | LangGraph 1.x (Agentic RAG) |
| Vector Store | ChromaDB (local development) |
| Embeddings & LLMs | OpenAI |
| UI | Streamlit |

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/pdichone/production-rag-course.git
cd production-rag-course
```

### 2. Set up your environment

```bash
cd code/part1-foundation
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Or with [uv](https://github.com/astral-sh/uv) (faster):

```bash
uv venv && uv pip install -r requirements.txt
```

### 3. Configure your API keys

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 4. Run the first example

```bash
python 01_document_loading.py
```

---

## Course Structure

```
production-rag-course/
└── code/
    ├── part1-foundation/
    ├── part2-debugging/
    ├── part3-optimization/
    ├── part4-scaling/
    ├── part5-production-project/
    └── part6-advanced/              # 2026 cutting-edge
        ├── 01_long_context_vs_rag.py
        ├── 02_contextual_retrieval.py
        ├── 03_late_chunking.py
        ├── 04_agentic_rag.py
        ├── 05_graphrag_intro.py
        └── 06_multimodal_rag.py
```

---

## Part 6: Advanced RAG 2026

The cutting-edge techniques that separate production RAG from tutorials:

| Technique | What It Solves | Improvement |
|-----------|----------------|-------------|
| **Long Context vs RAG** | When to use 1M-token windows vs retrieval | Cost optimization |
| **Contextual Retrieval** | Chunks losing document context | Up to 67% fewer retrieval failures |
| **Late Chunking** | Cross-chunk context lost in embeddings | 10–12% accuracy boost |
| **Agentic RAG** | One-shot retrieval missing information | Self-correcting loops |
| **GraphRAG** | Multi-hop reasoning failures | Relationship traversal |
| **Multimodal RAG** | Tables and charts destroyed by text extraction | Vision-based retrieval |

---

## Prerequisites

| Requirement | Level |
|-------------|-------|
| Python | Comfortable with functions, classes, and pip |
| APIs | Basic understanding of REST APIs |
| LLMs | Helpful, but not required |
| ML / AI | Not required — we explain everything |

---

## Free Resources

**Production AI Checklist** — a free checklist for deploying AI applications to production. Covers testing, monitoring, security, and scaling.

→ [Download the Production AI Checklist](#)

---

## Community

**AI Guild** — join thousands of AI engineers building production AI systems:

- Live weekly sessions on AI development
- Code reviews and architecture feedback
- A private community of practitioners
- Early access to new courses and content

→ [Join the AI Guild](#)

---

## About the Instructor

**Paulo Dichone** — AI Engineer & Educator

- 350,000+ students taught across platforms
- 70+ courses on AI, Python, and mobile development
- Building AI systems in production since 2015
- Creator of the *AI Developer Masterclass* and *Vector Databases Masterclass*

---

## FAQ

**Is this different from other RAG tutorials?**
Yes. Most tutorials show you *how* to build RAG. This course shows you *why* RAG breaks and how to fix it. The "5 Failure Modes" framework comes from teaching 300K+ students and seeing the same problems repeatedly.

**Do I need a GPU?**
No. All code runs on CPU. Part 6's Multimodal RAG section mentions a GPU for ColPali, but it's optional.

**Which vector database should I use?**
We use ChromaDB for simplicity. The patterns apply equally to Pinecone, Weaviate, Supabase, or any vector store.

**Is the code up to date?**
Yes. All code uses LangChain 1.x (2026 stable release) with current best practices.

---

## License

This course code is available under the [MIT License](LICENSE).

---

## Support

- **Issues** — open a GitHub issue for bugs or questions
- **Community** — join the AI Guild for direct support
- **Updates** — star this repo to get notified of new releases

---

*Ready to build RAG that actually works in production? Let's go.*

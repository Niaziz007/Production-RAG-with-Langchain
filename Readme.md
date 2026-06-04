# Production RAG with LangChain

**A Retrieval-Augmented Generation system built to survive production — not just the happy path.**

> *A RAG pipeline that works on 10 documents is easy. One that holds up at 10,000 — accurate, fast, and observable — is a different problem entirely.*

This project is my take on building RAG the way it actually needs to work in production: diagnosing why retrieval quality degrades at scale, and engineering around the failure modes that break most naive pipelines.

---

## Table of Contents

- [Overview](#overview)
- [The 5 RAG Failure Modes](#the-5-rag-failure-modes)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Layout](#project-layout)
- [Roadmap](#roadmap)
- [Advanced Techniques](#advanced-techniques)
- [License](#license)

---

## Overview

The goal of this project is a RAG stack that is correct, fast, and observable under real load. It covers the full pipeline:

| Stage | Focus |
|-------|-------|
| **Foundation** | A complete RAG pipeline — loading, chunking, embedding, retrieval, generation |
| **Reliability** | Hardening against the failure modes that break naive pipelines |
| **Quality** | Semantic chunking, reranking, multi-query retrieval |
| **Scale** | Caching, monitoring, production vector databases |
| **Advanced** | Agentic RAG, GraphRAG, contextual retrieval, multimodal |

---

## The 5 RAG Failure Modes

Most RAG systems fail for the same handful of reasons. This project is engineered to diagnose and fix each one.

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
| Language | Python 3.13+ |
| Framework | LangChain 1.x |
| Agents | LangGraph 1.x (Agentic RAG) |
| Vector Store | ChromaDB (local development) |
| Embeddings & LLMs | OpenAI, Anthropic |
| Package Manager | uv |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/haseebkhan/production-rag-with-langchain.git
cd production-rag-with-langchain
```

### 2. Set up the environment

This project uses [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

### 3. Configure API keys

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY and ANTHROPIC_API_KEY
```

### 4. Verify the setup

```bash
uv run python main.py
```

---

## Project Layout

```
production-rag-with-langchain/
├── main.py               # Environment + model connectivity check
├── document_loader.py    # Document ingestion utilities
├── pyproject.toml        # Dependencies (managed with uv)
└── Readme.md
```

---

## Roadmap

- [x] Project scaffolding and model connectivity
- [x] Document loading utilities
- [ ] Chunking strategies (recursive, semantic)
- [ ] Embedding + vector store integration (ChromaDB)
- [ ] Retrieval + generation pipeline
- [ ] Reranking and hybrid search
- [ ] Caching, monitoring, and evaluation
- [ ] Agentic RAG with LangGraph

---

## Advanced Techniques

The techniques that separate production RAG from a tutorial:

| Technique | What It Solves | Improvement |
|-----------|----------------|-------------|
| **Long Context vs RAG** | When to use large context windows vs retrieval | Cost optimization |
| **Contextual Retrieval** | Chunks losing document context | Up to 67% fewer retrieval failures |
| **Late Chunking** | Cross-chunk context lost in embeddings | 10–12% accuracy boost |
| **Agentic RAG** | One-shot retrieval missing information | Self-correcting loops |
| **GraphRAG** | Multi-hop reasoning failures | Relationship traversal |
| **Multimodal RAG** | Tables and charts destroyed by text extraction | Vision-based retrieval |

---

## License

Released under the [MIT License](LICENSE).

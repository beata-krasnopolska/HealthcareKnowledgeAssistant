# Healthcare Knowledge Assistant

A product-style AI project focused on healthcare knowledge retrieval using LangChain, LangGraph, RAG, tools, citations, and end-to-end tests.

## Project goal

The goal of this project is to build a healthcare-related knowledge assistant that can:

- answer questions based on trusted healthcare documents,
- retrieve relevant context using RAG,
- route requests using LangGraph,
- use local tools when appropriate,
- provide grounded answers with citations,
- include automated tests.

## Tech stack

- Python
- LangChain
- LangGraph
- OpenAI
- Chroma
- Streamlit
- Pytest
- Pydantic Settings

## Sample knowledge base

The project includes a small healthcare-oriented knowledge base with sample documents covering:
- patient visit preparation,
- privacy and data protection,
- appointments and referrals,
- clinic FAQ.

These documents will be used in the next steps to build the RAG pipeline.

## Current status

Commit 1:
- initial project structure
- environment configuration
- settings management
- basic logging
- application entrypoint
- smoke test

## Planned next steps

- add LLM integration
- add healthcare sample documents
- implement ingestion and chunking
- add vector store and retrieval
- build RAG flow
- add citations
- add healthcare tools
- implement LangGraph router
- add guardrails
- add Streamlit UI
- add e2e tests
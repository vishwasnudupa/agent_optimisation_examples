# Reranking Layers

Add a reranking step after broad retrieval so the most relevant chunks reach the
model first.

Use this for enterprise search, RAG, documentation QA, and knowledge base
assistants.

This example sorts retrieved chunks by overlap with query terms.

```powershell
python .\techniques\reranking_layers\agent_example.py
```

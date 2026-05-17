# Incremental Retrieval / Progressive RAG

Retrieve a small amount of context first, then fetch more only if the current
evidence is insufficient. This avoids paying for large retrievals on every task.

Use this for massive knowledge bases, manuals, legal corpora, and enterprise
search.

This example increases retrieval depth until a useful document appears.

```powershell
python .\techniques\incremental_retrieval_progressive_rag\agent_example.py
```

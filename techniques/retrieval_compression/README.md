# Retrieval Compression

Compress retrieved documents before injecting them into context. This keeps
large RAG workflows cheaper and reduces irrelevant detail.

Use this when retrieved context repeatedly exceeds several thousand tokens.

This example keeps only the first useful sentences from a simulated log
document.

```powershell
python .\techniques\retrieval_compression\agent_example.py
```

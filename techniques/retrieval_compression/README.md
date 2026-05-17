# Retrieval Compression

Compress retrieved documents before injecting them into context. This keeps
large RAG workflows cheaper and reduces irrelevant detail.

Use this when retrieved context repeatedly exceeds several thousand tokens.

This example keeps only the first useful sentences from a simulated log
document.

```powershell
python .\techniques\retrieval_compression\agent_example.py
```

## Realistic Scenarios

In RAG over long incident reports, the model may only need symptoms, timeline,
root cause, and remediation. Compression removes chatty background and duplicate
logs before context injection.

In firmware debugging, a 20,000-line UART capture can be compressed into boot
phases, faults, counters, and last-known-good events.

Use this when retrieved documents are long but only a small part is relevant.
Compression should preserve citations or source references when answers need to
be auditable.

## Pipeline Stage

Use this during **context preparation**, after retrieval/reranking and before
the final prompt is assembled.

```mermaid
flowchart LR
    A["Long retrieved docs"] --> B["Extract key facts"]
    B --> C["Compressed context"]
    C --> D["Prompt assembly"]
    D --> E["Model answer"]
```

# Reranking Layers

Add a reranking step after broad retrieval so the most relevant chunks reach the
model first.

Use this for enterprise search, RAG, documentation QA, and knowledge base
assistants.

This example sorts retrieved chunks by overlap with query terms.

```powershell
python .\techniques\reranking_layers\agent_example.py
```

## Realistic Scenarios

Enterprise search often retrieves broad matches from a vector database. A
reranker can then compare the query against each candidate and push the best
chunks to the top before the model sees them.

In legal or policy QA, reranking helps avoid answering from a loosely related
document when a more precise clause exists lower in the initial results.

Use this when retrieval returns plausible but noisy chunks. Better ordering can
improve accuracy without increasing context size.

## Pipeline Stage

Use this between **initial retrieval and context injection**. It chooses which
chunks deserve the model's limited attention.

```mermaid
flowchart LR
    A["Query"] --> B["Vector search"]
    B --> C["Candidate chunks"]
    C --> D["Reranker"]
    D --> E["Top relevant chunks"]
    E --> F["Model prompt"]
```

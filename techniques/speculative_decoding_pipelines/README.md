# Speculative Decoding Pipelines

Use a small fast model to draft tokens while a larger model verifies or corrects
the draft. In real serving stacks, this reduces generation latency.

Use this for high-throughput chat, inference servers, and GPU-bound model
serving.

This example simulates draft generation followed by large-model verification.

```powershell
python .\techniques\speculative_decoding_pipelines\agent_example.py
```

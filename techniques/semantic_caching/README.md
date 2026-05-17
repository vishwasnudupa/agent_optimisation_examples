# Semantic Caching

Cache responses for prompts that are semantically similar, not just identical.
This can greatly reduce latency and cost for repeated support-style requests.

Use this for FAQs, customer support, internal helpdesk bots, and high-volume
query systems.

This example creates a normalized semantic key for similar password-reset
questions.

```powershell
python .\techniques\semantic_caching\agent_example.py
```

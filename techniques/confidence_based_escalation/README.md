# Confidence-Based Escalation

Start with a cheap or fast model, then escalate only when confidence is low.
This reduces cost while preserving quality for uncertain tasks.

Use this in high-volume SaaS workflows, support bots, routers, and production
agent systems with mixed difficulty.

This example assigns a confidence score and chooses whether to use a stronger
model.

```powershell
python .\techniques\confidence_based_escalation\agent_example.py
```

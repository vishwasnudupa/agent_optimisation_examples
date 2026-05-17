# Adaptive Context Injection

Dynamically inject only the memory, documentation, or state that is relevant to
the current task. This keeps prompts focused and avoids distracting the model
with unrelated history.

Use this when assistants have large memory stores, big documentation sets, or
long-running conversations.

This example filters a small memory dictionary and injects only entries that
match the task.

```powershell
python .\techniques\adaptive_context_injection\agent_example.py
```

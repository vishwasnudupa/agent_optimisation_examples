# Reflection Loops

Let an agent critique and repair its own output in bounded iterations. The loop
should have clear stopping conditions and external validation when possible.

Use this for code generation, planning, summarization quality checks, and tasks
with known failure modes.

This example generates code, detects a missing guard, and repairs it.

```powershell
python .\techniques\reflection_loops\agent_example.py
```

# Tool Selection Routers

Use a lightweight router to select the right tool before invoking expensive or
state-changing operations.

Use this when agents have many tools, call the wrong tool often, or waste time
probing unnecessary systems.

This example routes compile-like tasks to a shell diagnostic and other tasks to
search.

```powershell
python .\techniques\tool_selection_routers\agent_example.py
```

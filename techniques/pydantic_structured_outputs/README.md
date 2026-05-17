# Pydantic Structured Outputs

Force model output into a known schema before using it in routers, tools, state
updates, or configuration generation.

Use this when regex parsing fails, JSON is malformed, or branching becomes
unstable.

This example parses JSON into a typed route decision object and validates
required fields.

```powershell
python .\techniques\pydantic_structured_outputs\agent_example.py
```

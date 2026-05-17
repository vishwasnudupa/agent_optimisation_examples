# Prompt Caching Layouts

Put stable, repeated context at the beginning of prompts so providers or local
caches can reuse it across calls.

Use this for API specs, register maps, protocol documents, coding standards, and
repeated workflows with identical prefixes.

This example caches answers using a stable static-context prefix key.

```powershell
python .\techniques\prompt_caching_layouts\agent_example.py
```

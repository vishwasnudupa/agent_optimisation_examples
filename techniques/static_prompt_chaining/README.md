# Static Prompt Chaining

Use a fixed linear pipeline when the workflow does not need dynamic branching.
This is faster and easier to reason about than autonomous planning.

Use this for speech-to-summary-to-lookup flows, extraction pipelines, and other
predictable transformations.

This example chains transcribe, summarize, and lookup agents.

```powershell
python .\techniques\static_prompt_chaining\agent_example.py
```

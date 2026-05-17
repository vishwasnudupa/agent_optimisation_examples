# Static Prompt Chaining

Use a fixed linear pipeline when the workflow does not need dynamic branching.
This is faster and easier to reason about than autonomous planning.

Use this for speech-to-summary-to-lookup flows, extraction pipelines, and other
predictable transformations.

This example chains transcribe, summarize, and lookup agents.

```powershell
python .\techniques\static_prompt_chaining\agent_example.py
```

## Realistic Scenarios

For predictable workflows like transcript to summary to CRM update, a fixed
chain is simpler and faster than an autonomous planner. Each step has a known
input and output.

In document processing, a static chain might extract fields, normalize names,
validate schema, and write to a database.

Use this when branching is unnecessary. Static chains are easier to test,
monitor, and reason about than open-ended agent autonomy.

## Pipeline Stage

Use this as the **main workflow design** for predictable transformations where
every request follows the same path.

```mermaid
flowchart LR
    A["Input"] --> B["Step 1"]
    B --> C["Step 2"]
    C --> D["Step 3"]
    D --> E["Validated output"]
```

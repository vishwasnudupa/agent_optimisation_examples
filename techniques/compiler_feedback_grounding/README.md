# Compiler Feedback Grounding

Feed exact compiler or runtime errors back into the repair step instead of
asking the model to guess what happened. Deterministic error text gives the
agent a concrete target.

Use this for code generation, firmware development, generated scripts, and
automated repair loops.

This example repairs a tiny source snippet using a simulated compiler error.

```powershell
python .\techniques\compiler_feedback_grounding\agent_example.py
```

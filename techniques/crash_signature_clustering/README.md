# Crash Signature Clustering

Group repeated crashes by stable signatures such as exception type, fault code,
or top stack frame. Clustering helps agents focus on recurring root causes.

Use this for firmware crash logs, backend incidents, mobile crash reporting, and
fleet diagnostics.

This example clusters crash strings by their prefix.

```powershell
python .\techniques\crash_signature_clustering\agent_example.py
```

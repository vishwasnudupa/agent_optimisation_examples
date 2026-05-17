# Build Artifact Fingerprinting

Create stable hashes for build inputs such as source files, flags, board
configuration, and dependency versions. The fingerprint tells the workflow when
an artifact is already current and when it must be rebuilt.

Use this in firmware, CI, code generation, and compile-test loops.

This example hashes a simulated firmware build configuration.

```powershell
python .\techniques\build_artifact_fingerprinting\agent_example.py
```

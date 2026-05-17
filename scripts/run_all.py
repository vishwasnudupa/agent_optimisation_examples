from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    examples = sorted(ROOT.glob("techniques/*/agent_example.py"))
    failures: list[str] = []
    for example in examples:
        relative = example.relative_to(ROOT)
        result = subprocess.run(
            [sys.executable, str(example)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        status = "ok" if result.returncode == 0 else "failed"
        print(f"{status:6} {relative}")
        if result.returncode != 0:
            failures.append(f"{relative}\n{result.stderr}")
    if failures:
        print("\nFailures:\n" + "\n".join(failures))
        return 1
    print(f"\nRan {len(examples)} technique examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import json
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PLUGIN_ROOT / "runtime"))

from optimized_workflow import OptimizedAgentWorkflow
from provider_adapters import MockProvider


def main() -> None:
    workflow = OptimizedAgentWorkflow(provider=MockProvider())

    tasks = [
        "Debug UART RX overflow in staging firmware",
        "Debug UART RX overflow in staging firmware",
        "Prepare production firmware flash plan",
    ]

    for task in tasks:
        result = workflow.run(task)
        print(json.dumps({"task": task, "result": result}, indent=2))


if __name__ == "__main__":
    main()

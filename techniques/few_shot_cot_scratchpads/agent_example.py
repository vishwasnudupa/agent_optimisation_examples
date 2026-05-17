import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

EXAMPLES = [
    "Example: if ping fails, check link, route, then DNS.",
    "Example: if compile fails, inspect the exact compiler error first.",
]


def main() -> None:
    agent = Agent(
        "scratchpad-planning-agent",
        "small",
        lambda task: "\n".join(EXAMPLES + [f"Task: {task}", "Reasoning:"]),
    )
    result = agent.run("debug intermittent network timeout")
    print(demo_result("Few-Shot CoT Scratchpads", "Provide reasoning examples before task", result))


if __name__ == "__main__":
    main()

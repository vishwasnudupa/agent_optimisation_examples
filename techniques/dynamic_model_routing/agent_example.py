import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, route_by_complexity


def main() -> None:
    agent = Agent(
        "model-routing-agent",
        "small",
        lambda tasks: [{"task": task, "model": route_by_complexity(task)} for task in tasks],
    )
    result = agent.run(["format json", "debug race condition in RTOS scheduler"])
    print(demo_result("Dynamic Model Routing", "Route by task complexity", result))


if __name__ == "__main__":
    main()

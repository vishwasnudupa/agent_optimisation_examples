import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def score(plan: str) -> int:
    return plan.count("validate") + plan.count("test")


def main() -> None:
    agent = Agent("tree-of-thought-agent", "large", lambda plans: max(plans, key=score))
    result = agent.run(
        ["patch then deploy", "reproduce validate patch test deploy", "restart service"]
    )
    print(demo_result("Tree-of-Thought Execution", "Explore and score multiple plans", result))


if __name__ == "__main__":
    main()

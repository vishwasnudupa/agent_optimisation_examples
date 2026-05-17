import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, run_pipeline


def main() -> None:
    planner = Agent("planner", "small", lambda task: f"steps for {task}")
    coder = Agent("coder", "large", lambda plan: f"implementation based on {plan}")
    tester = Agent("tester", "small", lambda code: f"smoke-tested {code}")
    result = run_pipeline("generate firmware update flow", [planner, coder, tester])
    print(demo_result("Micro-Agent Splitting", "Specialized staged agents", result))


if __name__ == "__main__":
    main()

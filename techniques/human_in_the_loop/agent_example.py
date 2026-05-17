import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def requires_approval(action: str) -> bool:
    return any(term in action for term in ["flash", "delete", "deploy", "payment"])


def main() -> None:
    def approval_gate(action: str) -> dict[str, str]:
        if requires_approval(action):
            return {"status": "paused", "reason": "human approval required", "action": action}
        return {"status": "executed", "action": action}

    agent = Agent("approval-gate-agent", "small", approval_gate)
    result = agent.run("flash production firmware")
    print(demo_result("Human-in-the-Loop", "Pause risky actions for approval", result))


if __name__ == "__main__":
    main()

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

BLOCKED_TERMS = {"delete production", "exfiltrate", "disable audit"}


def guardrail(prompt: str) -> None:
    if any(term in prompt.lower() for term in BLOCKED_TERMS):
        raise PermissionError("blocked by policy")


def main() -> None:
    def guarded_execute(prompt: str) -> dict[str, str]:
        guardrail(prompt)
        return {"status": "allowed", "prompt": prompt}

    agent = Agent("guardrail-agent", "small", guarded_execute)
    result = agent.run("deploy staging config")
    print(demo_result("Guardrail Validation Layers", "Policy check before execution", result))


if __name__ == "__main__":
    main()

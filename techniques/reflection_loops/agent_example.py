import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def generate() -> str:
    return "return user.name.upper()"


def critique(code: str) -> str:
    return "missing None guard" if "user.name" in code else "ok"


def repair(code: str, issue: str) -> str:
    return "return user.name.upper() if user and user.name else ''" if issue != "ok" else code


def main() -> None:
    def reflect_and_repair(_: str) -> dict[str, str]:
        code = generate()
        issue = critique(code)
        return {"issue": issue, "repaired_code": repair(code, issue)}

    agent = Agent("reflection-repair-agent", "medium", reflect_and_repair)
    result = agent.run("generate safe username formatter")
    print(demo_result("Reflection Loops", "Critique then repair output", result))


if __name__ == "__main__":
    main()

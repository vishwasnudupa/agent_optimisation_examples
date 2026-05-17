import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def repair_from_compiler_error(source: str, error: str) -> str:
    if "missing semicolon" in error:
        return source.rstrip() + ";"
    return source


def main() -> None:
    agent = Agent(
        "compiler-repair-agent",
        "small",
        lambda task: repair_from_compiler_error(task["source"], task["error"]),
    )
    result = agent.run({"source": "int x = 1", "error": "error: missing semicolon"})
    print(demo_result("Compiler Feedback Grounding", "Repair from exact compiler error", result))


if __name__ == "__main__":
    main()

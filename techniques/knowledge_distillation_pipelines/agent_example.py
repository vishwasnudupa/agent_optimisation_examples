import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def teacher(task: str) -> str:
    return f"Detailed expert solution for {task}: classify, validate, answer."


def distill(teacher_output: str) -> str:
    return teacher_output.replace("Detailed expert solution", "Small-model rule")


def main() -> None:
    agent = Agent("distillation-agent", "small", lambda task: distill(teacher(task)))
    result = agent.run("support triage")
    print(demo_result("Knowledge Distillation Pipelines", "Compress teacher output", result))


if __name__ == "__main__":
    main()

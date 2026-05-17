import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def small_model_draft(prompt: str) -> str:
    return f"draft answer for {prompt}"


def large_model_verify(draft: str) -> str:
    return draft.replace("draft", "verified")


def main() -> None:
    agent = Agent(
        "speculative-decoding-agent",
        "small+large",
        lambda prompt: large_model_verify(small_model_draft(prompt)),
    )
    result = agent.run("support question")
    print(demo_result("Speculative Decoding Pipelines", "Small draft with large verification", result))


if __name__ == "__main__":
    main()

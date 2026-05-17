import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, SimpleCache, demo_result, semantic_key


def main() -> None:
    cache = SimpleCache()
    agent = Agent(
        "semantic-cache-agent",
        "small",
        lambda prompt: cache.get_or_set(semantic_key(prompt), lambda: "password reset answer"),
    )
    outputs = []
    for prompt in ["How do I reset my password?", "reset password help"]:
        value, hit = agent.run(prompt)["output"]
        outputs.append({"prompt": prompt, "hit": hit, "value": value})
    print(demo_result("Semantic Caching", "Similarity-keyed answer reuse", outputs))


if __name__ == "__main__":
    main()

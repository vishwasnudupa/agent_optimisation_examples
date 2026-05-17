import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, SimpleCache, demo_result, stable_hash


STATIC_CONTEXT = "register map v1; protocol spec v2; coding rules"


def main() -> None:
    cache = SimpleCache()
    prefix_key = stable_hash(STATIC_CONTEXT)
    agent = Agent(
        "prompt-cache-agent",
        "small",
        lambda task: cache.get_or_set(prefix_key + ":" + task, lambda: f"answer for {task}"),
    )
    outputs = []
    for task in ["decode uart fault", "decode uart fault"]:
        value, hit = agent.run(task)["output"]
        outputs.append({"cache_hit": hit, "value": value})
    print(demo_result("Prompt Caching Layouts", "Stable prefix cache reuse", outputs))


if __name__ == "__main__":
    main()

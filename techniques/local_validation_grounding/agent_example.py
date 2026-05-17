import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def deterministic_validator(raw: str) -> dict[str, str]:
    payload = json.loads(raw)
    if payload["status"] != "compiled":
        raise ValueError("build did not compile")
    return payload


def main() -> None:
    agent = Agent("local-validator-agent", "small", deterministic_validator)
    result = agent.run('{"status": "compiled", "artifact": "firmware.bin"}')
    print(demo_result("Local Validation Grounding", "Deterministic validation outside model", result))


if __name__ == "__main__":
    main()

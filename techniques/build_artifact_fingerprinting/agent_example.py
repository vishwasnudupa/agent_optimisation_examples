import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, stable_hash


def main() -> None:
    agent = Agent(
        "artifact-cache-agent",
        "small",
        lambda source_flags: {
            "artifact": "firmware.bin",
            "fingerprint": stable_hash(source_flags),
            "rebuild_needed": False,
        },
    )
    result = agent.run("main.c|net.c|-O2|board=v1")
    print(demo_result("Build Artifact Fingerprinting", "Stable build input hashing", result))


if __name__ == "__main__":
    main()

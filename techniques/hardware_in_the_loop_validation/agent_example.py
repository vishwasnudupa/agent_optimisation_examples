import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def hil_check(command: str) -> dict[str, str]:
    simulated_board_reply = "OK led=on voltage=3.3"
    return {"command": command, "board_reply": simulated_board_reply, "status": "passed"}


def main() -> None:
    agent = Agent("hil-validation-agent", "medium", hil_check)
    result = agent.run("flash firmware.bin && run smoke test")
    print(demo_result("Hardware-in-the-Loop Validation", "Verify behavior on board", result))


if __name__ == "__main__":
    main()

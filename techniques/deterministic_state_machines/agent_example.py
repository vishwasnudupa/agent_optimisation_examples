from enum import Enum
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


class State(str, Enum):
    PLAN = "plan"
    VALIDATE = "validate"
    EXECUTE = "execute"
    DONE = "done"


TRANSITIONS = {
    State.PLAN: State.VALIDATE,
    State.VALIDATE: State.EXECUTE,
    State.EXECUTE: State.DONE,
}


def main() -> None:
    def execute_state_machine(start: State) -> list[str]:
        state = start
        trace = [state.value]
        while state != State.DONE:
            state = TRANSITIONS[state]
            trace.append(state.value)
        return trace

    agent = Agent("state-machine-agent", "small", execute_state_machine)
    result = agent.run(State.PLAN)
    print(demo_result("Deterministic State Machines", "Explicit graph transitions", result))


if __name__ == "__main__":
    main()

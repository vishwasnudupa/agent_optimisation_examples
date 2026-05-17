import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, event_queue


def main() -> None:
    def handle_events(items: list[str]) -> list[dict[str, str]]:
        events = event_queue(items)
        handled = []
        while not events.empty():
            handled.append({"handled_event": events.get()})
        return handled

    agent = Agent("event-worker-agent", "small", handle_events)
    result = agent.run(["build_finished", "test_failed", "ticket_created"])
    print(demo_result("Event-Driven Agent Architecture", "Queue-triggered execution", result))


if __name__ == "__main__":
    main()

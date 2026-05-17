import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, Telemetry, demo_result


def main() -> None:
    telemetry = Telemetry()

    def measured_work(calls: int) -> dict[str, float | int]:
        for _ in range(calls):
            started = time.perf_counter()
            time.sleep(0.001)
            telemetry.record_latency((time.perf_counter() - started) * 1000)
        return telemetry.summary()

    agent = Agent("telemetry-feedback-agent", "small", measured_work)
    result = agent.run(3)
    print(demo_result("Runtime Telemetry Feedback", "Metrics-driven orchestration", result))


if __name__ == "__main__":
    main()

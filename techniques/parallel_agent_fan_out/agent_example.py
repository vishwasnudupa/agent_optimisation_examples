from concurrent.futures import ThreadPoolExecutor
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def analyze_file(path: str) -> str:
    return f"{path}: no issue"


def main() -> None:
    def fan_out(paths: list[str]) -> list[str]:
        with ThreadPoolExecutor(max_workers=3) as pool:
            return list(pool.map(analyze_file, paths))

    agent = Agent("parallel-analysis-agent", "medium", fan_out)
    result = agent.run(["api.py", "db.py", "ui.py"])
    print(demo_result("Parallel Agent Fan-Out", "Concurrent independent analysis", result))


if __name__ == "__main__":
    main()

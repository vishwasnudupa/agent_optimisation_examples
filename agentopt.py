from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TECHNIQUES = ROOT / "techniques"


def technique_dirs() -> list[Path]:
    return sorted(path for path in TECHNIQUES.iterdir() if path.is_dir())


def list_techniques(_: argparse.Namespace) -> int:
    for path in technique_dirs():
        print(path.name)
    return 0


def run_technique(args: argparse.Namespace) -> int:
    example = TECHNIQUES / args.technique / "agent_example.py"
    if not example.exists():
        print(f"Unknown technique: {args.technique}", file=sys.stderr)
        return 2
    return subprocess.run([sys.executable, str(example)], cwd=ROOT, check=False).returncode


def run_all(_: argparse.Namespace) -> int:
    script = ROOT / "scripts" / "run_all.py"
    return subprocess.run([sys.executable, str(script)], cwd=ROOT, check=False).returncode


def explain(args: argparse.Namespace) -> int:
    readme = TECHNIQUES / args.technique / "README.md"
    if not readme.exists():
        print(f"Unknown technique: {args.technique}", file=sys.stderr)
        return 2
    print(readme.read_text(encoding="utf-8"))
    return 0


def plugin_demo(_: argparse.Namespace) -> int:
    demo = ROOT / "plugins" / "agent-optimization-runtime" / "examples" / "realistic_workflow_demo.py"
    return subprocess.run([sys.executable, str(demo)], cwd=ROOT, check=False).returncode


def generate_index(_: argparse.Namespace) -> int:
    script = ROOT / "scripts" / "generate_technique_index.py"
    return subprocess.run([sys.executable, str(script)], cwd=ROOT, check=False).returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agent optimization example toolkit")
    sub = parser.add_subparsers(required=True)

    list_cmd = sub.add_parser("list", help="List available techniques")
    list_cmd.set_defaults(func=list_techniques)

    run_cmd = sub.add_parser("run", help="Run one technique example")
    run_cmd.add_argument("technique")
    run_cmd.set_defaults(func=run_technique)

    run_all_cmd = sub.add_parser("run-all", help="Run all technique examples")
    run_all_cmd.set_defaults(func=run_all)

    explain_cmd = sub.add_parser("explain", help="Print a technique README")
    explain_cmd.add_argument("technique")
    explain_cmd.set_defaults(func=explain)

    plugin_cmd = sub.add_parser("plugin-demo", help="Run the realistic plugin workflow demo")
    plugin_cmd.set_defaults(func=plugin_demo)

    index_cmd = sub.add_parser("generate-index", help="Generate TECHNIQUE_INDEX.md")
    index_cmd.set_defaults(func=generate_index)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

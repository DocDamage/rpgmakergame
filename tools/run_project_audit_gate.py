#!/usr/bin/env python3
"""
Run project cohesion/integrity/syntax audit gates in one command.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run canonical project audit gates."
    )
    parser.add_argument(
        "--scope",
        choices=("core", "all"),
        default="core",
        help="Quest scope for story/content checks (default: core).",
    )
    parser.add_argument(
        "--skip-js-syntax",
        action="store_true",
        help="Skip JavaScript parser checks (`node --check`).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Run validators in strict mode where supported.",
    )
    return parser.parse_args()


def run_cmd(cmd: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        capture_output=True,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, output.strip()


def main() -> int:
    args = parse_args()
    content_cmd = [
        "python3",
        "tools/validate_content_integrity.py",
        "--scope",
        args.scope,
        "--strict-map-npc-anchors",
    ]
    if args.strict:
        content_cmd.append("--strict-mainline")

    story_cmd = ["python3", "tools/audit_story_cohesion.py", "--scope", args.scope]
    if args.strict:
        story_cmd.extend(["--strict-act-gating", "--strict-npc-anchors"])

    route_cmd = ["python3", "tools/audit_quest_route_pacing.py", "--scope", args.scope]
    if args.strict:
        route_cmd.append("--strict")

    runtime_bridge_cmd = ["python3", "tools/validate_runtime_map_bridge.py"]
    if args.strict:
        runtime_bridge_cmd.append("--strict")

    transfer_contract_cmd = ["python3", "tools/validate_runtime_transfer_contract.py"]
    if args.strict:
        transfer_contract_cmd.append("--strict")

    runtime_world_dress_cmd = ["python3", "tools/validate_runtime_world_dressing.py"]
    if args.strict:
        runtime_world_dress_cmd.extend(["--warn-surplus", "--strict"])

    world_cmd = ["python3", "tools/validate_world_integrity.py"]
    if args.strict:
        world_cmd.append("--strict-gates")

    steps: list[tuple[str, list[str]]] = [
        (
            "party_sprite_coverage",
            [
                "python3",
                "tools/validate_party_sprite_coverage.py",
                *(["--strict"] if args.strict else []),
            ],
        ),
        (
            "runtime_audio_references",
            [
                "python3",
                "tools/validate_runtime_audio_references.py",
                *(["--strict"] if args.strict else []),
            ],
        ),
        (
            "runtime_image_references",
            [
                "python3",
                "tools/validate_runtime_image_references.py",
                *(["--strict", "--strict-effects"] if args.strict else []),
            ],
        ),
        ("content_integrity", content_cmd),
        ("story_cohesion", story_cmd),
        ("quest_route_pacing", route_cmd),
        ("runtime_map_bridge", runtime_bridge_cmd),
        ("runtime_transfer_contract", transfer_contract_cmd),
        ("runtime_world_dressing", runtime_world_dress_cmd),
        ("world_integrity", world_cmd),
        (
            "environment_sprite_coverage",
            [
                "python3",
                "tools/audit_environment_sprite_coverage.py",
                "--strict-candidates",
                "--strict-world-dressing",
            ],
        ),
    ]

    if not args.skip_js_syntax:
        node_path = shutil.which("node")
        if node_path is None:
            print("node not found in PATH; JS syntax checks cannot run.")
            return 1
        js_files = sorted((ROOT / "js").rglob("*.js"))
        for path in js_files:
            rel = path.relative_to(ROOT).as_posix()
            steps.append((f"js_syntax:{rel}", ["node", "--check", rel]))

    failed: list[tuple[str, str]] = []
    passed: list[str] = []

    print("=" * 72)
    print("PROJECT AUDIT GATE")
    print("=" * 72)
    print(f"Scope: {args.scope}")
    print(f"Strict mode: {'enabled' if args.strict else 'disabled'}")
    print(f"JS syntax checks: {'disabled' if args.skip_js_syntax else 'enabled'}")
    print("-" * 72)

    for name, cmd in steps:
        code, out = run_cmd(cmd, ROOT)
        if code == 0:
            passed.append(name)
            print(f"[PASS] {name}")
            continue
        failed.append((name, out))
        print(f"[FAIL] {name}")

    print("-" * 72)
    print(f"Passed: {len(passed)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFAILED DETAILS")
        print("-" * 72)
        for name, out in failed:
            print(f"[{name}]")
            if out:
                print(out)
            else:
                print("(no output)")
            print("-" * 72)
        return 1

    print("\nAll audit gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

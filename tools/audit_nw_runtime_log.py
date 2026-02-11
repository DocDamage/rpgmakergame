#!/usr/bin/env python3
"""
Audit NW runtime smoke log for actionable runtime failures.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    line_no: int
    line: str


FATAL_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("console_error", re.compile(r"INFO:CONSOLE:.*(TypeError|ReferenceError|SyntaxError|Uncaught|Error:)", re.I)),
    ("missing_resource", re.compile(r"(ERR_FILE_NOT_FOUND|Failed to load resource|ENOENT)", re.I)),
    ("webgl_fatal", re.compile(r"Your browser does not support WebGL", re.I)),
    ("gpu_fatal", re.compile(r"ContextResult::kFatalFailure", re.I)),
)

WARNING_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("dbus", re.compile(r"ERROR:dbus/object_proxy\.cc", re.I)),
    ("gpu_init", re.compile(r"gl::init::InitializeStaticGLBindingsOneOff failed", re.I)),
    ("vaapi", re.compile(r"vaapi|libva\.so", re.I)),
)

IGNORE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"org\.freedesktop\.UPower", re.I),
    re.compile(r"Widevine enabled but no library found", re.I),
    re.compile(r"Desktop Identity Consistency", re.I),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit NW runtime log for JS/resource/runtime failures."
    )
    parser.add_argument("log_path", help="Path to runtime log file.")
    parser.add_argument(
        "--max-lines",
        type=int,
        default=25,
        help="Max finding lines to print per severity (default: 25).",
    )
    return parser.parse_args()


def should_ignore(line: str) -> bool:
    return any(p.search(line) for p in IGNORE_PATTERNS)


def classify_line(line: str) -> tuple[str, str] | None:
    for category, pat in FATAL_PATTERNS:
        if pat.search(line):
            return ("error", category)
    for category, pat in WARNING_PATTERNS:
        if pat.search(line):
            return ("warning", category)
    return None


def run_audit(log_path: Path) -> tuple[list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    if not log_path.exists():
        errors.append(
            Finding(
                severity="error",
                category="inputs",
                line_no=0,
                line=f"Log file not found: {log_path}",
            )
        )
        return errors, warnings

    with log_path.open("r", encoding="utf-8", errors="replace") as fh:
        for idx, raw in enumerate(fh, start=1):
            line = raw.rstrip("\n")
            if not line:
                continue
            if should_ignore(line):
                continue
            match = classify_line(line)
            if match is None:
                continue
            severity, category = match
            finding = Finding(severity=severity, category=category, line_no=idx, line=line)
            if severity == "error":
                errors.append(finding)
            else:
                warnings.append(finding)
    return errors, warnings


def main() -> int:
    args = parse_args()
    log_path = Path(args.log_path)
    errors, warnings = run_audit(log_path)

    print("=" * 68)
    print("NW RUNTIME LOG AUDIT")
    print("=" * 68)
    print(f"Log: {log_path}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("-" * 68)
        print("ERROR FINDINGS")
        for finding in errors[: args.max_lines]:
            print(f"[{finding.category}] line {finding.line_no}: {finding.line}")

    if warnings:
        print("-" * 68)
        print("WARNING FINDINGS")
        for finding in warnings[: args.max_lines]:
            print(f"[{finding.category}] line {finding.line_no}: {finding.line}")

    if not errors and not warnings:
        print("\nNo actionable runtime findings detected.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

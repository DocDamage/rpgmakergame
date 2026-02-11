#!/usr/bin/env python3
"""
Provision missing runtime audio tokens in audio/bgm|bgs|me|se.

Strategy:
- Scan runtime references from project database/map/common-event/troop data.
- For each missing token, copy a silence source file into the required folder.
- Prefer `assets/audio/_placeholder_silence.ogg` when present.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from validate_runtime_audio_references import AUDIO_DIR, ROOT, collect_refs


PLACEHOLDER_CANDIDATES = (
    ROOT / "assets" / "audio" / "_placeholder_silence.ogg",
    ROOT / "assets" / "audio" / "_placeholder_silence.wav",
)


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Provision missing runtime audio files with placeholder copies."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned writes without creating files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing runtime token files.",
    )
    parser.add_argument(
        "--ext",
        default=".ogg",
        choices=(".ogg", ".wav"),
        help="Output extension for created runtime files (default: .ogg).",
    )
    return parser.parse_args()


def resolve_placeholder(ext: str) -> Path | None:
    preferred = ROOT / "assets" / "audio" / f"_placeholder_silence{ext}"
    if preferred.exists():
        return preferred
    for candidate in PLACEHOLDER_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def token_exists(kind: str, token: str) -> bool:
    folder = AUDIO_DIR / kind
    for ext in (".ogg", ".m4a", ".wav", ".mp3"):
        if (folder / f"{token}{ext}").exists():
            return True
    return False


def main() -> int:
    args = parse_args()
    placeholder = resolve_placeholder(args.ext)
    issues: list[Issue] = []
    if placeholder is None:
        issues.append(
            Issue(
                "error",
                "inputs",
                "No placeholder source found. Expected assets/audio/_placeholder_silence.ogg or .wav",
            )
        )
        for issue in issues:
            print(f"[{issue.severity.upper()}] {issue.category}: {issue.detail}")
        return 1

    refs = collect_refs()
    unique = sorted({(ref.kind, ref.token) for ref in refs})

    created = 0
    overwritten = 0
    skipped = 0
    folders_created = 0

    print("=" * 72)
    print("PROVISION RUNTIME AUDIO PLACEHOLDERS")
    print("=" * 72)
    print(f"References scanned: {len(refs)}")
    print(f"Unique tokens: {len(unique)}")
    print(f"Placeholder source: {placeholder.relative_to(ROOT)}")
    print(f"Write extension: {args.ext}")
    print(f"Mode: {'dry-run' if args.dry_run else ('overwrite' if args.overwrite else 'create-missing')}")
    print("-" * 72)

    # Ensure canonical runtime folders exist even when no token currently targets one kind.
    for kind in ("bgm", "bgs", "me", "se"):
        folder = AUDIO_DIR / kind
        if not folder.exists() and not args.dry_run:
            folder.mkdir(parents=True, exist_ok=True)
            folders_created += 1

    for kind, token in unique:
        folder = AUDIO_DIR / kind

        # Keep existing token if any supported extension already resolves.
        if token_exists(kind, token) and not args.overwrite:
            skipped += 1
            continue

        out_path = folder / f"{token}{args.ext}"
        exists = out_path.exists()
        if args.dry_run:
            if exists:
                overwritten += 1
            else:
                created += 1
            continue

        shutil.copy2(placeholder, out_path)
        if exists:
            overwritten += 1
        else:
            created += 1

    print(f"Folders created: {folders_created}")
    print(f"Created files: {created}")
    print(f"Overwritten files: {overwritten}")
    print(f"Skipped tokens: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

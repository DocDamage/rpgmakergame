#!/usr/bin/env python3
"""
Slice off-grid sprite imports, then pad each slice to a 16px grid.

Workflow:
1) Scan PNG files in assets/sprites/*/_imports.
2) Slice by known sheet layouts when filename hints match.
3) Otherwise auto-slice by connected components (alpha first, background-color key fallback).
4) Pad each slice to the next multiple of 16 using transparent canvas.
5) Write audit reports to docs/reports.

Original import files are never modified.
"""

from __future__ import annotations

import argparse
import csv
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from PIL import Image


LAYOUT_HINTS_12X8 = (
    "2k8chars",
    "runechars",
    "down_npc",
    "oldnpcs",
    "bigsheet",
    "8_chars",
)
LAYOUT_HINTS_3X4 = (
    "singlesheet",
    "minecart_char",
    "npcactions",
)


@dataclass
class Result:
    source: Path
    category: str
    width: int
    height: int
    off_grid: bool
    strategy: str
    slices_written: int
    padded_slices: int
    manual_review: bool
    notes: str
    output_dir: Path | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Slice sprite imports and pad slices to a target grid."
    )
    parser.add_argument(
        "--sprites-root",
        default="assets/sprites",
        help="Root folder containing category folders with _imports subfolders.",
    )
    parser.add_argument(
        "--report-prefix",
        default="docs/reports/sprite_slice_pad_audit",
        help=(
            "Report path prefix. Script writes '<prefix>.csv' and '<prefix>.md'. "
            "Date suffix is appended automatically."
        ),
    )
    parser.add_argument(
        "--pad-grid",
        type=int,
        default=16,
        help="Pad each exported slice to nearest multiple of this value.",
    )
    parser.add_argument(
        "--off-grid-only",
        action="store_true",
        help="Process only imports whose dimensions are not multiples of pad-grid.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Delete and regenerate existing per-source output directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze and report without writing image outputs.",
    )
    parser.add_argument(
        "--alpha-threshold",
        type=int,
        default=1,
        help="Alpha > threshold is treated as solid for component extraction.",
    )
    parser.add_argument(
        "--background-tolerance",
        type=int,
        default=8,
        help="Per-channel tolerance for background color keying fallback.",
    )
    parser.add_argument(
        "--bg-dilate-iters",
        type=int,
        default=2,
        help=(
            "4-neighbor dilation iterations applied to background-key masks "
            "before component extraction."
        ),
    )
    parser.add_argument(
        "--min-component-area",
        type=int,
        default=32,
        help="Ignore tiny connected components below this pixel area.",
    )
    parser.add_argument(
        "--max-components",
        type=int,
        default=400,
        help="Abort auto-slicing on files with more than this many components.",
    )
    return parser.parse_args()


def iter_import_pngs(sprites_root: Path) -> Iterable[Path]:
    if not sprites_root.exists():
        return []
    for category_dir in sorted(p for p in sprites_root.iterdir() if p.is_dir()):
        imports_dir = category_dir / "_imports"
        if not imports_dir.is_dir():
            continue
        for file_path in sorted(imports_dir.glob("*.png")):
            yield file_path


def infer_named_layout(stem: str, width: int, height: int) -> tuple[str, int, int] | None:
    lowered = stem.lower()

    if any(token in lowered for token in LAYOUT_HINTS_12X8):
        if width % 12 == 0 and height % 8 == 0:
            return ("grid_12x8", 12, 8)

    if any(token in lowered for token in LAYOUT_HINTS_3X4):
        if width % 3 == 0 and height % 4 == 0:
            return ("grid_3x4", 3, 4)

    return None


def slice_grid(img: Image.Image, cols: int, rows: int) -> list[tuple[Image.Image, int, int]]:
    cell_w = img.width // cols
    cell_h = img.height // rows
    slices: list[tuple[Image.Image, int, int]] = []

    for row in range(rows):
        y0 = row * cell_h
        y1 = y0 + cell_h
        for col in range(cols):
            x0 = col * cell_w
            x1 = x0 + cell_w
            slices.append((img.crop((x0, y0, x1, y1)), row + 1, col + 1))

    return slices


def alpha_mask(img: Image.Image, alpha_threshold: int) -> tuple[bytearray, float]:
    alpha = img.getchannel("A")
    raw = alpha.tobytes()
    mask = bytearray(1 if px > alpha_threshold else 0 for px in raw)
    solid = sum(mask)
    coverage = solid / (img.width * img.height)
    return mask, coverage


def dominant_border_color(img: Image.Image) -> tuple[tuple[int, int, int], float]:
    rgb = img.convert("RGB")
    pix = rgb.load()
    width, height = rgb.size
    border_pixels = []

    for x in range(width):
        border_pixels.append(pix[x, 0])
        border_pixels.append(pix[x, height - 1])
    for y in range(height):
        border_pixels.append(pix[0, y])
        border_pixels.append(pix[width - 1, y])

    color, count = Counter(border_pixels).most_common(1)[0]
    ratio = count / len(border_pixels)
    return color, ratio


def background_key_mask(
    img: Image.Image, bg_color: tuple[int, int, int], tolerance: int
) -> bytearray:
    rgb = img.convert("RGB")
    raw = rgb.tobytes()
    mask = bytearray(len(raw) // 3)
    br, bg, bb = bg_color
    out_idx = 0

    for in_idx in range(0, len(raw), 3):
        r = raw[in_idx]
        g = raw[in_idx + 1]
        b = raw[in_idx + 2]
        if (
            abs(r - br) <= tolerance
            and abs(g - bg) <= tolerance
            and abs(b - bb) <= tolerance
        ):
            mask[out_idx] = 0
        else:
            mask[out_idx] = 1
        out_idx += 1

    return mask


def dilate_mask(mask: bytearray, width: int, height: int, iterations: int) -> bytearray:
    if iterations <= 0:
        return mask

    current = mask
    total = width * height
    for _ in range(iterations):
        nxt = bytearray(current)
        for idx in range(total):
            if current[idx] == 0:
                continue
            y, x = divmod(idx, width)
            if x > 0:
                nxt[idx - 1] = 1
            if x + 1 < width:
                nxt[idx + 1] = 1
            if y > 0:
                nxt[idx - width] = 1
            if y + 1 < height:
                nxt[idx + width] = 1
        current = nxt
    return current


def connected_components(
    mask: bytearray,
    width: int,
    height: int,
    min_area: int,
    max_components: int,
) -> tuple[list[tuple[int, int, int, int]], str | None]:
    total = width * height
    visited = bytearray(total)
    boxes: list[tuple[int, int, int, int]] = []

    for idx in range(total):
        if mask[idx] == 0 or visited[idx] == 1:
            continue

        stack = [idx]
        visited[idx] = 1

        area = 0
        min_x = width
        min_y = height
        max_x = -1
        max_y = -1

        while stack:
            cur = stack.pop()
            y, x = divmod(cur, width)
            area += 1

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            if x > 0:
                left = cur - 1
                if mask[left] == 1 and visited[left] == 0:
                    visited[left] = 1
                    stack.append(left)

            if x + 1 < width:
                right = cur + 1
                if mask[right] == 1 and visited[right] == 0:
                    visited[right] = 1
                    stack.append(right)

            if y > 0:
                up = cur - width
                if mask[up] == 1 and visited[up] == 0:
                    visited[up] = 1
                    stack.append(up)

            if y + 1 < height:
                down = cur + width
                if mask[down] == 1 and visited[down] == 0:
                    visited[down] = 1
                    stack.append(down)

        if area >= min_area:
            boxes.append((min_x, min_y, max_x + 1, max_y + 1))
            if len(boxes) > max_components:
                return [], f"component_count_exceeds_limit({max_components})"

    boxes.sort(key=lambda b: (b[1], b[0]))
    return boxes, None


def pad_to_grid(frame: Image.Image, grid: int) -> tuple[Image.Image, bool]:
    width, height = frame.size
    padded_w = ((width + grid - 1) // grid) * grid
    padded_h = ((height + grid - 1) // grid) * grid

    if padded_w == width and padded_h == height:
        return frame, False

    out = Image.new("RGBA", (padded_w, padded_h), (0, 0, 0, 0))
    offset_x = (padded_w - width) // 2
    offset_y = (padded_h - height) // 2
    out.paste(frame, (offset_x, offset_y))
    return out, True


def export_slices(
    source: Path,
    slices: list[tuple[str, Image.Image]],
    output_dir: Path,
    pad_grid: int,
    dry_run: bool,
) -> tuple[int, int]:
    written = 0
    padded = 0

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    for filename, frame in slices:
        padded_frame, did_pad = pad_to_grid(frame, pad_grid)
        if did_pad:
            padded += 1
        written += 1

        if not dry_run:
            out_path = output_dir / filename
            padded_frame.save(out_path)

    return written, padded


def process_source(file_path: Path, args: argparse.Namespace) -> Result:
    category = file_path.parent.parent.name
    output_dir = file_path.parent.parent / "_slices" / file_path.stem

    with Image.open(file_path) as raw_img:
        img = raw_img.convert("RGBA")

    width, height = img.size
    off_grid = (width % args.pad_grid != 0) or (height % args.pad_grid != 0)

    if args.off_grid_only and not off_grid:
        return Result(
            source=file_path,
            category=category,
            width=width,
            height=height,
            off_grid=off_grid,
            strategy="skipped_on_grid",
            slices_written=0,
            padded_slices=0,
            manual_review=False,
            notes="already aligned to pad grid",
            output_dir=None,
        )

    if output_dir.exists() and args.overwrite and not args.dry_run:
        shutil.rmtree(output_dir)

    layout = infer_named_layout(file_path.stem, width, height)
    if layout is not None:
        strategy, cols, rows = layout
        raw_slices = slice_grid(img, cols, rows)
        slices = [
            (
                f"{file_path.stem}_r{row:02d}_c{col:02d}.png",
                frame,
            )
            for frame, row, col in raw_slices
        ]
        written, padded = export_slices(
            source=file_path,
            slices=slices,
            output_dir=output_dir,
            pad_grid=args.pad_grid,
            dry_run=args.dry_run,
        )
        note = f"{cols}x{rows} grid from filename hint"
        return Result(
            source=file_path,
            category=category,
            width=width,
            height=height,
            off_grid=off_grid,
            strategy=strategy,
            slices_written=written,
            padded_slices=padded,
            manual_review=False,
            notes=note,
            output_dir=output_dir,
        )

    mask, alpha_coverage = alpha_mask(img, args.alpha_threshold)
    mask_method = "alpha"

    # If image is effectively opaque, fallback to background color keying.
    if alpha_coverage >= 0.98:
        bg_color, bg_ratio = dominant_border_color(img)
        if bg_ratio < 0.45:
            return Result(
                source=file_path,
                category=category,
                width=width,
                height=height,
                off_grid=off_grid,
                strategy="manual_review",
                slices_written=0,
                padded_slices=0,
                manual_review=True,
                notes="opaque image with no dominant border color",
                output_dir=None,
            )
        mask = background_key_mask(img, bg_color, args.background_tolerance)
        if args.bg_dilate_iters > 0:
            mask = dilate_mask(mask, width, height, args.bg_dilate_iters)
        mask_method = (
            f"bg_key({bg_color[0]},{bg_color[1]},{bg_color[2]})"
            f"+dilate{args.bg_dilate_iters}"
        )

    solid = sum(mask)
    if solid == 0:
        return Result(
            source=file_path,
            category=category,
            width=width,
            height=height,
            off_grid=off_grid,
            strategy="manual_review",
            slices_written=0,
            padded_slices=0,
            manual_review=True,
            notes=f"no extractable foreground with {mask_method}",
            output_dir=None,
        )

    boxes, error = connected_components(
        mask=mask,
        width=width,
        height=height,
        min_area=args.min_component_area,
        max_components=args.max_components,
    )
    if error is not None:
        return Result(
            source=file_path,
            category=category,
            width=width,
            height=height,
            off_grid=off_grid,
            strategy="manual_review",
            slices_written=0,
            padded_slices=0,
            manual_review=True,
            notes=f"{mask_method} extraction failed: {error}",
            output_dir=None,
        )

    if not boxes:
        return Result(
            source=file_path,
            category=category,
            width=width,
            height=height,
            off_grid=off_grid,
            strategy="manual_review",
            slices_written=0,
            padded_slices=0,
            manual_review=True,
            notes=f"no components above area threshold using {mask_method}",
            output_dir=None,
        )

    slices = []
    for idx, box in enumerate(boxes, start=1):
        frame = img.crop(box)
        slices.append((f"{file_path.stem}_obj{idx:03d}.png", frame))

    written, padded = export_slices(
        source=file_path,
        slices=slices,
        output_dir=output_dir,
        pad_grid=args.pad_grid,
        dry_run=args.dry_run,
    )

    return Result(
        source=file_path,
        category=category,
        width=width,
        height=height,
        off_grid=off_grid,
        strategy=f"components_{mask_method}",
        slices_written=written,
        padded_slices=padded,
        manual_review=False,
        notes=f"component_count={len(boxes)}",
        output_dir=output_dir,
    )


def write_csv_report(results: list[Result], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "source",
                "category",
                "width",
                "height",
                "off_grid",
                "strategy",
                "slices_written",
                "padded_slices",
                "manual_review",
                "notes",
                "output_dir",
            ]
        )
        for row in results:
            writer.writerow(
                [
                    row.source.as_posix(),
                    row.category,
                    row.width,
                    row.height,
                    "yes" if row.off_grid else "no",
                    row.strategy,
                    row.slices_written,
                    row.padded_slices,
                    "yes" if row.manual_review else "no",
                    row.notes,
                    row.output_dir.as_posix() if row.output_dir else "",
                ]
            )


def write_markdown_report(results: list[Result], md_path: Path, args: argparse.Namespace) -> None:
    md_path.parent.mkdir(parents=True, exist_ok=True)

    total = len(results)
    processed = [r for r in results if r.strategy != "skipped_on_grid"]
    manual = [r for r in results if r.manual_review]
    slice_total = sum(r.slices_written for r in results)
    padded_total = sum(r.padded_slices for r in results)

    strategy_counts = defaultdict(int)
    for row in results:
        strategy_counts[row.strategy] += 1

    with md_path.open("w", encoding="utf-8") as fh:
        fh.write("# Sprite Slice + Pad Audit\n\n")
        fh.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        fh.write("## Summary\n\n")
        fh.write(f"- Imports scanned: **{total}**\n")
        fh.write(f"- Imports processed: **{len(processed)}**\n")
        fh.write(f"- Manual review required: **{len(manual)}**\n")
        fh.write(f"- Slices written: **{slice_total}**\n")
        fh.write(f"- Padded slices: **{padded_total}**\n")
        fh.write(f"- Pad grid: **{args.pad_grid}px**\n")
        fh.write("\n")

        fh.write("## Strategy Counts\n\n")
        for strategy in sorted(strategy_counts):
            fh.write(f"- `{strategy}`: {strategy_counts[strategy]}\n")
        fh.write("\n")

        fh.write("## Manual Review List\n\n")
        if not manual:
            fh.write("- None\n")
        else:
            for row in manual:
                fh.write(f"- `{row.source.as_posix()}`: {row.notes}\n")
        fh.write("\n")

        fh.write("## Notes\n\n")
        fh.write("- Original files under `_imports` were not modified.\n")
        fh.write("- Slice outputs were written under sibling `_slices/<source_stem>/` folders.\n")
        fh.write("- Per-file details are in the CSV report.\n")


def main() -> int:
    args = parse_args()
    sprites_root = Path(args.sprites_root)
    if not sprites_root.exists():
        print(f"Error: sprites root not found: {sprites_root}")
        return 1

    sources = list(iter_import_pngs(sprites_root))
    if not sources:
        print(f"No PNG files found under {sprites_root}/**/_imports")
        return 1

    results: list[Result] = []
    for source in sources:
        result = process_source(source, args)
        results.append(result)
        print(
            f"{result.strategy:28} | {result.slices_written:4d} slices | "
            f"{result.source.as_posix()}"
        )

    date_suffix = datetime.now().strftime("%Y-%m-%d")
    report_prefix = Path(args.report_prefix)
    csv_path = report_prefix.parent / f"{report_prefix.name}_{date_suffix}.csv"
    md_path = report_prefix.parent / f"{report_prefix.name}_{date_suffix}.md"

    write_csv_report(results, csv_path)
    write_markdown_report(results, md_path, args)

    manual_count = sum(1 for r in results if r.manual_review)
    print("\nDone.")
    print(f"- CSV report: {csv_path.as_posix()}")
    print(f"- Markdown report: {md_path.as_posix()}")
    print(f"- Manual review items: {manual_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

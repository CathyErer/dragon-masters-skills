#!/usr/bin/env python3
"""Install or validate the shared Dragon Keep theme in a lesson-plan folder."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


CSS_NAME = "dragon-keep-theme.css"
JS_NAME = "dragon-keep-theme.js"
CSS_TAG = f'<link rel="stylesheet" href="{CSS_NAME}">'
JS_TAG = f'<script src="{JS_NAME}"></script>'
CONFLICT_RE = re.compile(r"^(?:<<<<<<<|>>>>>>>|=======)$", re.MULTILINE)
PAGE_GLOBS = ("DM*_Day*_Lesson_Plan.html", "DM*_Ch*_Lesson_Plan.html")


def page_day(text: str) -> int | None:
    match = re.search(r"<title>[^<]*\b(?:Day|Ch(?:apter)?)\s*(\d+)\b", text, re.I)
    return int(match.group(1)) if match else None


def selected_day(text: str) -> int | None:
    match = re.search(
        r'<option\b(?=[^>]*\bselected\b)(?=[^>]*\bvalue="")[^>]*>\s*(?:Day|Ch(?:apter)?)\s*(\d+)\b',
        text,
        re.I,
    )
    return int(match.group(1)) if match else None


def validate_page(
    path: Path,
    text: str,
    require_theme: bool,
    configured_days: set[int],
) -> list[str]:
    errors: list[str] = []
    day = page_day(text)
    selected = selected_day(text)
    tab_count = len(
        re.findall(
            r'<button\s+class="tab(?:\s+on)?"\s+data-p="p[1-4]"',
            text,
        )
    )

    if day is None:
        errors.append("missing Day number in <title>")
    elif day not in configured_days:
        errors.append(f"Day {day} missing from theme chapter configuration")
    if selected is not None and day != selected:
        errors.append(f"title Day {day} does not match selected Day {selected}")
    if tab_count != 4:
        errors.append(f"expected 4 tabs, found {tab_count}")
    if len(re.findall(r'id="p[1-4]"', text)) != 4:
        errors.append("expected panels #p1–#p4 exactly once")
    if '<div id="doc">' not in text:
        errors.append("missing #doc container")
    if '<header class="ed' not in text:
        errors.append("missing editable lesson header")
    if CONFLICT_RE.search(text):
        errors.append("contains merge-conflict markers")
    if require_theme:
        if text.count(CSS_TAG) != 1:
            errors.append(f"expected one {CSS_NAME} link")
        if text.count(JS_TAG) != 1:
            errors.append(f"expected one {JS_NAME} script")
    return errors


def patch_page(text: str) -> str:
    if CSS_TAG not in text:
        if "</head>" not in text:
            raise ValueError("missing </head>")
        text = text.replace("</head>", f"{CSS_TAG}\n</head>", 1)
    if JS_TAG not in text:
        if "</body>" not in text:
            raise ValueError("missing </body>")
        text = text.replace("</body>", f"{JS_TAG}\n</body>", 1)
    return text


def check_relative_navigation(folder: Path, page: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in set(re.findall(r'href="(DM\d+_Day[^"#]+\.html)"', text)):
        if not (folder / target).is_file():
            errors.append(f"broken navigation target: {target}")
    return errors


def validate_shared_assets(folder: Path) -> tuple[list[str], set[int]]:
    errors: list[str] = []
    css_path = folder / CSS_NAME
    js_path = folder / JS_NAME
    if not css_path.is_file():
        errors.append(f"missing shared asset: {CSS_NAME}")
    if not js_path.is_file():
        errors.append(f"missing shared asset: {JS_NAME}")
    if errors:
        return errors, set()

    css = css_path.read_text(encoding="utf-8")
    js = js_path.read_text(encoding="utf-8")
    if css.count("{") != css.count("}"):
        errors.append("unbalanced braces in shared CSS")
    if CONFLICT_RE.search(css) or CONFLICT_RE.search(js):
        errors.append("shared assets contain merge-conflict markers")

    node = shutil.which("node")
    if node:
        result = subprocess.run(
            [node, "--check", str(js_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            detail = (result.stderr or result.stdout).strip().splitlines()[-1]
            errors.append(f"shared JavaScript syntax error: {detail}")

    configured_days = {
        int(value) for value in re.findall(r"^\s*(\d+)\s*:\s*\{", js, re.MULTILINE)
    }
    if not configured_days:
        errors.append("no Day entries found in theme chapter configuration")

    # Hero art is optional: only validate configured images when ART_BASE is set.
    base_match = re.search(r"ART_BASE\s*=\s*['\"]([^'\"]*)['\"]", js)
    art_base = base_match.group(1) if base_match else ""
    if art_base:
        hero_dir = (folder / art_base).resolve()
        for asset in set(re.findall(r"\bart\s*:\s*['\"]([^'\"]+)['\"]", js)):
            if not (hero_dir / asset).is_file():
                errors.append(f"missing configured hero image: {asset}")
    return errors, configured_days


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lesson_dir", type=Path)
    parser.add_argument("--check", action="store_true", help="validate only; write nothing")
    parser.add_argument("--dry-run", action="store_true", help="show intended writes")
    args = parser.parse_args()

    folder = args.lesson_dir.expanduser().resolve()
    if not folder.is_dir():
        print(f"ERROR: lesson directory not found: {folder}", file=sys.stderr)
        return 2

    skill_dir = Path(__file__).resolve().parent.parent
    asset_dir = skill_dir / "assets"
    source_assets = [asset_dir / CSS_NAME, asset_dir / JS_NAME]
    for asset in source_assets:
        if not asset.is_file():
            print(f"ERROR: bundled asset missing: {asset}", file=sys.stderr)
            return 2

    pages = sorted({p for g in PAGE_GLOBS for p in folder.glob(g)})
    if not pages:
        print(f"ERROR: no Dragon Masters daily lesson-plan HTML files in {folder}", file=sys.stderr)
        return 2

    configured_days: set[int] = set()
    if args.check:
        asset_errors, configured_days = validate_shared_assets(folder)
        if asset_errors:
            for error in asset_errors:
                print(f"FAIL shared assets: {error}")
            print("FAILED: shared asset validation", file=sys.stderr)
            return 1
    else:
        bundled_js = (asset_dir / JS_NAME).read_text(encoding="utf-8")
        configured_days = {
            int(value)
            for value in re.findall(r"^\s*(\d+)\s*:\s*\{", bundled_js, re.MULTILINE)
        }

    failures = 0
    for page in pages:
        original = page.read_text(encoding="utf-8")
        errors = validate_page(page, original, require_theme=args.check, configured_days=configured_days)
        errors.extend(check_relative_navigation(folder, page, original))
        if errors:
            failures += 1
            print(f"FAIL {page.name}: {'; '.join(errors)}")
            continue

        if not args.check:
            try:
                updated = patch_page(original)
            except ValueError as exc:
                failures += 1
                print(f"FAIL {page.name}: {exc}")
                continue
            if updated != original:
                print(f"{'WOULD UPDATE' if args.dry_run else 'UPDATED'} {page.name}")
                if not args.dry_run:
                    page.write_text(updated, encoding="utf-8")
            else:
                print(f"UNCHANGED {page.name}")
        else:
            print(f"OK {page.name}")

    if not args.check and not args.dry_run and not failures:
        for source in source_assets:
            destination = folder / source.name
            if source.resolve() != destination.resolve():
                shutil.copy2(source, destination)
                print(f"COPIED {source.name}")

    if failures:
        print(f"FAILED: {failures} page(s)", file=sys.stderr)
        return 1
    print(f"PASS: {len(pages)} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

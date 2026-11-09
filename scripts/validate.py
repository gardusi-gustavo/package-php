#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    composer = root / "composer.json"
    if not composer.is_file():
        print("missing composer.json", file=sys.stderr); return 1
    data = json.loads(composer.read_text())
    if data.get("name") != "gardusi-gustavo/package-php":
        print("unexpected package name", file=sys.stderr); return 1
    php = sorted((root / "src").rglob("*.php")) + sorted((root / "tests").rglob("*.php"))
    if not php:
        print("no PHP sources", file=sys.stderr); return 1
    for p in php:
        text = p.read_text(encoding="utf-8")
        if not text.startswith("<?php"):
            print(f"{p}: missing <?php", file=sys.stderr); return 1
        if "namespace " not in text:
            print(f"{p}: missing namespace", file=sys.stderr); return 1
        if text.count("{") != text.count("}"):
            print(f"{p}: unbalanced braces", file=sys.stderr); return 1
    print(f"php validation ok ({len(php)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

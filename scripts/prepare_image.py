#!/usr/bin/env python3
"""Normalize one raster image to 16:9 without stretching."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageColor


def normalize(src: Path, dst: Path, mode: str, focus: str, width: int, background: str) -> None:
    with Image.open(src) as opened:
        image = opened.convert("RGB")
        out_w, out_h = width, round(width * 9 / 16)
        if mode == "contain":
            image.thumbnail((out_w, out_h), Image.Resampling.LANCZOS)
            result = Image.new("RGB", (out_w, out_h), ImageColor.getrgb(background))
            result.paste(image, ((out_w - image.width) // 2, (out_h - image.height) // 2))
        else:
            scale = max(out_w / image.width, out_h / image.height)
            resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
            left = max(0, (resized.width - out_w) // 2)
            top = 0 if focus == "top" else max(0, resized.height - out_h) if focus == "bottom" else max(0, (resized.height - out_h) // 2)
            result = resized.crop((left, top, left + out_w, top + out_h))
        dst.parent.mkdir(parents=True, exist_ok=True)
        result.save(dst, **({"quality": 94} if dst.suffix.lower() in {".jpg", ".jpeg"} else {}))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("cover", "contain"), default="cover")
    parser.add_argument("--focus", choices=("center", "top", "bottom"), default="center")
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--background", default="#FFFFFF")
    args = parser.parse_args()
    if args.width < 160:
        parser.error("--width must be at least 160 pixels")
    normalize(args.input, args.output, args.mode, args.focus, args.width, args.background)


if __name__ == "__main__":
    main()

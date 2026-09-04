"""Run headless YOLO inference and save annotations to disk."""
from __future__ import annotations
import argparse
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--weights", required=True, type=Path); source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--image", type=Path); source.add_argument("--image-dir", type=Path)
    p.add_argument("--conf", type=float, default=None); p.add_argument("--output-dir", type=Path, default=Path("outputs/inference"))
    p.add_argument("--display", action="store_true"); p.add_argument("--device", default=None, help="Optional device; omit for auto-selection")
    a = p.parse_args()
    if not a.weights.is_file(): raise FileNotFoundError(f"Weights not found: {a.weights}")
    input_path = a.image or a.image_dir
    if not input_path.exists(): raise FileNotFoundError(f"Input not found: {input_path}")
    from ultralytics import YOLO
    kw = {"source": str(input_path), "save": True, "project": str(a.output_dir.parent), "name": a.output_dir.name, "exist_ok": True, "show": a.display}
    if a.conf is not None: kw["conf"] = a.conf
    if a.device is not None: kw["device"] = a.device
    YOLO(str(a.weights)).predict(**kw)
if __name__ == "__main__": main()

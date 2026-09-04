"""Evaluate YOLO weights on a selected split of a dataset YAML."""
from __future__ import annotations
import argparse
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--weights", required=True, type=Path); p.add_argument("--data", required=True, type=Path)
    p.add_argument("--split", choices=("train", "val", "test"), default="test"); p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--device", default=None, help="Optional device; omit for auto-selection")
    a = p.parse_args()
    for label, path in (("weights", a.weights), ("dataset YAML", a.data)):
        if not path.is_file(): raise FileNotFoundError(f"{label.capitalize()} not found: {path}")
    from ultralytics import YOLO
    kw = {"data": str(a.data), "split": a.split, "imgsz": a.imgsz}
    if a.device is not None: kw["device"] = a.device
    YOLO(str(a.weights)).val(**kw)
if __name__ == "__main__": main()

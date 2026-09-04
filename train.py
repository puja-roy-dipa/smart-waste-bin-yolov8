"""Train an Ultralytics YOLO detector without machine-specific paths."""
from __future__ import annotations
import argparse
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", required=True, type=Path); p.add_argument("--model", default="yolov8s.pt")
    p.add_argument("--epochs", type=int, default=50); p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=8); p.add_argument("--patience", type=int, default=10)
    p.add_argument("--project", type=Path, default=Path("outputs")); p.add_argument("--name", default="yolov8s")
    p.add_argument("--device", default=None, help="Optional device; omit for auto-selection")
    a = p.parse_args()
    if not a.data.is_file(): raise FileNotFoundError(f"Dataset YAML not found: {a.data}")
    from ultralytics import YOLO
    kw = dict(data=str(a.data), epochs=a.epochs, imgsz=a.imgsz, batch=a.batch, patience=a.patience, project=str(a.project), name=a.name)
    if a.device is not None: kw["device"] = a.device
    YOLO(a.model).train(**kw)
if __name__ == "__main__": main()

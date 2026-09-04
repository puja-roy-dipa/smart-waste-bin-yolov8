# Reproducibility notes

The IEEE paper is the source of truth for published claims and official metrics. The supplied development notebook is a historical record of available code, configuration, environment, and run output.

For YOLOv8s, the notebook records a training invocation approximately using `yolov8s.pt`, `epochs=100`, `imgsz=640`, `batch=8`, `patience=10`, `lr0=0.001`, and `lrf=0.001`. Its saved output appears to stop/complete at 58 epochs and records approximately precision 0.889, recall 0.866, mAP@50 0.937, and mAP@50–95 0.909.

The publication reports YOLOv8s precision 0.889, recall 0.866, F1 0.877, and mAP@50 0.927, and states 50 training epochs. Neither source has been altered to make the values agree. The development notebook appears to contain experiment/run artifacts that are not necessarily identical to the final paper-reported run.

Published metrics should be cited from the paper. Notebook outputs are historical experiment records. Exact reconstruction of the final paper run requires confirmation of the exact final checkpoint, dataset revision, configuration, and execution conditions.

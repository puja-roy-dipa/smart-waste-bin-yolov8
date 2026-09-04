# Environment and installation

## Recorded original experiment environment

The supplied notebook records an environment approximately comprising Python 3.9.18, Ultralytics YOLO 8.1.14, PyTorch 1.12.1+cu116, and a CUDA-enabled NVIDIA GeForce RTX 3090. These are historical experiment records, not requirements for modern installations.

## Recommended installation

Create an isolated Python environment and install the project requirements:

```bash
python -m venv .venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install a PyTorch build appropriate for the intended OS/CUDA environment following PyTorch’s official guidance. `requirements.txt` leaves `torch` unpinned to avoid forcing an incompatible CUDA wheel.

## Reproduction caution

Exact numerical reproduction can vary with Ultralytics, PyTorch, CUDA, driver versions, hardware, data preprocessing, and non-recorded stochastic settings. Do not treat a current installation as an exact reconstruction of the final paper run.

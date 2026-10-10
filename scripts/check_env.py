#!/usr/bin/env python3
"""Check the ML environment and record it in ENVIRONMENT.md.

Also measures matrix-multiply speed and memory bandwidth on this machine.
Those two numbers are the first points on your Stage 8 roofline.

Run with:  uv run python scripts/check_env.py
"""
import datetime as dt
import importlib
import os
import platform
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows, notes, problems = [], [], []


def sysctl(key):
    try:
        return subprocess.run(["sysctl", "-n", key], capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def version(mod):
    try:
        return importlib.import_module(mod).__version__
    except Exception:
        return None


# ---------- machine ----------
chip = sysctl("machdep.cpu.brand_string") or platform.processor() or platform.machine()
mem = sysctl("hw.memsize")
mem_gb = f"{int(mem) / 2**30:.0f} GB" if mem.isdigit() else "unknown"
mac = platform.mac_ver()[0]
rows += [("Machine", chip), ("Unified memory", mem_gb),
         ("OS", f"macOS {mac}" if mac else platform.platform()), ("Python", sys.version.split()[0])]
for mod in ["numpy", "torch", "torchvision", "mlx", "sklearn", "jupyterlab"]:
    v = version(mod if mod != "mlx" else "mlx.core") or (version("mlx") if mod == "mlx" else None)
    rows.append((mod, v or "not installed"))


# ---------- PyTorch on the Mac GPU (MPS) ----------
def bench_torch():
    import torch
    if not torch.backends.mps.is_available():
        problems.append("PyTorch can't see the Mac GPU (MPS). Check that you're on Apple Silicon and macOS 14 or later.")
        return
    dev = torch.device("mps")
    sync = torch.mps.synchronize
    for dtype, name in [(torch.float32, "fp32"), (torch.float16, "fp16")]:
        best = 0.0
        for n in (2048, 4096):
            a = torch.randn(n, n, device=dev, dtype=dtype)
            b = torch.randn(n, n, device=dev, dtype=dtype)
            for _ in range(3):
                a @ b
            sync()
            reps = 10
            t = time.perf_counter()
            for _ in range(reps):
                a @ b
            sync()
            best = max(best, 2 * n**3 * reps / (time.perf_counter() - t) / 1e12)
        rows.append((f"PyTorch MPS matmul {name}", f"{best:.1f} TFLOP/s"))
        if name == "fp16":
            notes.append(("peak_fp16", best))
    # Bandwidth: copy 1 GiB (reads 1 GiB, writes 1 GiB)
    x = torch.empty(2**28, device=dev, dtype=torch.float32)
    y = torch.empty_like(x)
    for _ in range(3):
        y.copy_(x)
    sync()
    reps = 10
    t = time.perf_counter()
    for _ in range(reps):
        y.copy_(x)
    sync()
    gbs = 2 * x.numel() * 4 * reps / (time.perf_counter() - t) / 1e9
    rows.append(("PyTorch MPS copy bandwidth", f"{gbs:.0f} GB/s"))
    notes.append(("bw", gbs))


def bench_mlx():
    import mlx.core as mx
    rows.append(("MLX default device", str(mx.default_device())))
    n, reps = 4096, 10
    a = mx.random.normal((n, n)).astype(mx.float16)
    b = mx.random.normal((n, n)).astype(mx.float16)
    for _ in range(3):
        mx.eval(a @ b)
    t = time.perf_counter()
    for _ in range(reps):
        mx.eval(a @ b)
    rows.append(("MLX matmul fp16", f"{2 * n**3 * reps / (time.perf_counter() - t) / 1e12:.1f} TFLOP/s"))


for fn, label in [(bench_torch, "PyTorch"), (bench_mlx, "MLX")]:
    try:
        fn()
    except ImportError:
        problems.append(f"{label} isn't installed. Run: uv sync")
    except Exception as e:  # keep going so the report still gets written
        problems.append(f"{label} check failed: {e}")

d = dict(notes)
if "peak_fp16" in d and "bw" in d:
    ridge = d["peak_fp16"] * 1e12 / (d["bw"] * 1e9)
    rows.append(("Measured ridge point (fp16)", f"about {ridge:.0f} FLOPs per byte"))

# ---------- report ----------
lines = ["# My ML environment", "",
         f"Recorded {dt.date.today().isoformat()} by `scripts/check_env.py`.", "",
         "| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rows]
lines += ["", "The matmul speed and copy bandwidth are your first measured points for the Stage 8 roofline. "
          "Ops whose arithmetic intensity is below the ridge point are limited by memory bandwidth, not by compute.", ""]
if problems:
    lines += ["## Problems", ""] + [f"- {p}" for p in problems] + [""]
with open(os.path.join(ROOT, "ENVIRONMENT.md"), "w") as f:
    f.write("\n".join(lines))

width = max(len(k) for k, _ in rows)
for k, v in rows:
    print(f"{k:<{width}}  {v}")
print("\nSaved to ENVIRONMENT.md")
if problems:
    print("\nProblems:\n- " + "\n- ".join(problems))
    sys.exit(1)

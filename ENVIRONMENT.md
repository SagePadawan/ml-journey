# My ML environment

Recorded 2026-10-10 by `scripts/check_env.py`.

| | |
|---|---|
| Machine | Apple M5 Max |
| Unified memory | 48 GB |
| OS | macOS 26.6.2 |
| Python | 3.12.15 |
| numpy | 2.5.3 |
| torch | 2.14.1 |
| torchvision | 0.29.1 |
| mlx | 0.32.3 |
| sklearn | 1.9.1 |
| jupyterlab | 4.6.4 |
| PyTorch MPS matmul fp32 | 15.0 TFLOP/s |
| PyTorch MPS matmul fp16 | 63.6 TFLOP/s |
| PyTorch MPS copy bandwidth | 543 GB/s |
| MLX default device | Device(gpu, 0) |
| MLX matmul fp16 | 51.2 TFLOP/s |
| Measured ridge point (fp16) | about 117 FLOPs per byte |

The matmul speed and copy bandwidth are your first measured points for the Stage 8 roofline. Ops whose arithmetic intensity is below the ridge point are limited by memory bandwidth, not by compute.

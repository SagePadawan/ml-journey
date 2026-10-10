# Stage 8 · IO-aware kernels

Weeks 40–41 · Compute: Mac for the Metal path, or a rented NVIDIA GPU for the Triton path

**Why it’s here:** The FlashAttention beat lands better now: you can already see memory traffic in a trace, and here you write the fused kernel that removes it.

**Test it:** Test every kernel against the PyTorch version for correctness before you time it.

## The idea

**What holds up.** Softmax, LayerNorm, elementwise ops and long-sequence attention are memory-bound. FlashAttention wins by cutting reads and writes to HBM, while doing slightly more FLOPs.

**Where it breaks.** Large training matmuls are compute-bound. “FLOPs don’t matter” is only true to the left of the roofline’s ridge point, and the roofline tells you which side you are on.

**Concepts:** Memory hierarchy, Arithmetic intensity, Roofline model, Kernel fusion, Tiling, Online softmax, Coalescing

## Project: Roofline your GPU, then write the kernel

Build a roofline for your hardware, place measured ops on it, and implement online softmax. Then write one fused kernel: Triton on a rented NVIDIA GPU, or Metal through MLX on your Mac. A fused color-grade kernel is the Metal option, and it is directly useful for the video editor. Runs at measure-and-reason depth: two weeks, one kernel.

Each milestone below is a GitHub issue in the milestone **Stage 8 · IO-aware kernels**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Compute peak FLOP/s, memory bandwidth and ridge point for your GPU or Mac
2. Benchmark matmuls at several sizes plus softmax and LayerNorm; plot achieved throughput on the roofline
3. Implement online softmax in NumPy and match naive softmax to 1e-6
4. Time naive attention vs F.scaled_dot_product_attention at sequence lengths 512 to 8k, recording time and peak memory
5. Write one fused kernel: a Triton row-softmax on a rented NVIDIA GPU, or a fused color-grade kernel in Metal through MLX on your Mac
6. Plot your fused kernel on your roofline next to the unfused version

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/08-io-aware-kernels/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Which of your measured ops will land left of the ridge point?

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain why FlashAttention does more FLOPs and still runs faster.

300 words, or a link to a 3-minute recording:


## Revisit

> Was your Stage 6 CNN compute-bound or memory-bound? Then place one denoising step from Track A on your roofline.



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [FlashAttention](https://arxiv.org/abs/2205.14135) — Dao et al., 2022 **(core)**
- [ ] [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — OpenAI / Triton, 2021 **(core)**
- [ ] [Roofline: An Insightful Visual Performance Model](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.html) — Williams, Waterman, Patterson, 2009
- [ ] [Online softmax](https://arxiv.org/abs/1805.02867) — Milakov & Gimelshein, 2018
- [ ] [FlashAttention-2](https://arxiv.org/abs/2307.08691) — Tri Dao, 2023
- [ ] [FlashAttention-3](https://arxiv.org/abs/2407.08608) — Shah et al., 2024
- [ ] [Triton](https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf) — Tillet, Kung, Cox, 2019

## On the job

**Roles that use this:** GPU kernel engineer, ML compiler engineer (Triton, XLA, MLIR), Performance engineer at a chip company

**At enterprise scale:**

- Writing fused attention kernels for a new GPU generation
- Optimizing on-device models for Apple Silicon or mobile chips with Metal

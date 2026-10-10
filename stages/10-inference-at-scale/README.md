# Stage 10 · Inference at scale

Weeks 44–47 · Compute: Rented NVIDIA GPUs for serving tests; Mac for your own GPT

**Why it’s here:** The capstone pulls everything together: bandwidth floors (Stage 8), launch overhead (7), active parameters (9) and quality checks (2). The same latency model prices serving for the video editor and the storyboard app.

**Test it:** Load-test the endpoint at rising request rates and alert on latency, errors and output drift.

**Safety and security:** Serving endpoints need authentication, rate limits and spending caps, or a leaked key becomes a large bill.

## The idea

**What holds up.** CUDA graphs record a sequence of kernel launches and replay it as one, removing per-launch CPU overhead. At batch 1 with thousands of small kernels, that overhead is real.

**Where it breaks.** CUDA graphs remove overhead above a floor. The floor is bytes moved per token divided by memory bandwidth, set by size, precision, sharding, batch and whether the model is MoE. At bf16, 400B parameters is 800 GB of weights, more than eight 80 GB H100s hold.

**Concepts:** CUDA graphs, Decode is bandwidth-bound, KV cache, Batching, Tensor parallelism, Quantization, Speculative decoding, Monitoring & safe rollout

## Project: Capstone: the comeback

Write a one-page latency model for decoding a 400B model, then validate the method on your own GPT by measuring each optimization separately.

Each milestone below is a GitHub issue in the milestone **Stage 10 · Inference at scale**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Latency model: weight bytes, KV-cache bytes, communication, launch overhead, bandwidth floor
2. Measure your GPT decoding: eager vs torch.compile(mode="reduce-overhead")
3. Add batching and report tokens/s vs batch size
4. Add int8 weight quantization and re-measure
5. Publish a waterfall chart of where each millisecond went, with your answer to the last line
6. Check the quantized model on your held-out eval so speed doesn’t hide a quality loss
7. Load-test your endpoint at rising request rates, then set alerts for latency, error rate and output drift

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/10-inference-at-scale/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict the speedup from CUDA graphs alone at batch 1 and at batch 64.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Give the full answer to the last line of the monologue in under 2 minutes.

300 words, or a link to a 3-minute recording:


## Revisit

> Re-read the whole monologue. Mark which regime makes each line true, and which questions it never asked.



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — Pope et al., 2022 **(core)**
- [ ] [Getting Started with CUDA Graphs](https://developer.nvidia.com/blog/cuda-graphs/) — NVIDIA, 2019 **(core)**
- [ ] [PagedAttention (vLLM)](https://arxiv.org/abs/2309.06180) — Kwon et al., 2023 **(core)**
- [ ] [Accelerating PyTorch with CUDA Graphs](https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/) — PyTorch team, 2021
- [ ] [Megatron-LM](https://arxiv.org/abs/1909.08053) — Shoeybi et al., 2019
- [ ] [Speculative decoding](https://arxiv.org/abs/2211.17192) — Leviathan, Kalman, Matias, 2022
- [ ] [GPTQ](https://arxiv.org/abs/2210.17323) — Frantar et al., 2022

## On the job

**Roles that use this:** Inference engineer, ML platform engineer, AI capacity and FinOps analyst, TPM for model serving, Solutions architect

**At enterprise scale:**

- Cutting serving cost per million tokens with batching, quantization and speculative decoding
- Planning GPU capacity for a launch against latency targets
- Helping enterprise customers size and budget a self-hosted deployment

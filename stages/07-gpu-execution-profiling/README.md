# Stage 7 · GPU execution & profiling

Weeks 38–39 · Compute: Mac (Instruments) plus a few hours on a rented NVIDIA GPU for Nsight

**Why it’s here:** Moved ahead of IO-aware kernels. You need to read a trace and understand async launches before a roofline means anything.

**Test it:** Add a benchmark test that fails if a training step gets more than 10% slower.

**Safety and security:** Rented GPU machines are on the internet. Never expose Jupyter without a password, and keep API keys out of notebooks.

## The idea

**What holds up.** CUDA launches are asynchronous. When kernels are large, Python races ahead and its cost is hidden.

**Where it breaks.** When kernels are tiny, as in small-batch decode, or when code hits a sync point like .item(), the GPU sits idle waiting for Python. The gaps are visible in an Nsight trace.

**Concepts:** GPU execution model, Async launches, Sync points, Launch overhead, Profiling, Input pipeline

## Project: Read the trace

Profile your own training and decoding loops until you can point at every gap in the timeline and say what caused it. Do the first pass on your Mac with Instruments, then rent an NVIDIA GPU for a few hours to see the same loop in Nsight.

Each milestone below is a GitHub issue in the milestone **Stage 7 · GPU execution & profiling**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Profile a training step with torch.profiler, then with Nsight Systems on a rented NVIDIA GPU (or Instruments’ Metal System Trace on your Mac); label compute vs idle
2. Insert a .item() inside the loop and find the stall it causes in the trace
3. Profile batch-1 decoding of your GPT and measure GPU idle percentage
4. Add DataLoader workers and pinned memory; show the input-pipeline gap close

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/07-gpu-execution-profiling/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict GPU idle percentage during batch-1 decoding before profiling.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain, with your trace screenshot, when Python is and is not the bottleneck.

300 words, or a link to a 3-minute recording:


## Revisit

> Profile your Stage 6 CNN training step. Is the GPU waiting on data loading?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Making Deep Learning Go Brrrr](https://horace.io/brrr_intro.html) — Horace He, 2022 **(core)**
- [ ] [PyTorch CUDA semantics](https://docs.pytorch.org/docs/stable/notes/cuda.html) — PyTorch docs, 2024 **(core)**
- [ ] [PyTorch Profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) — PyTorch docs, 2024
- [ ] [Nsight Systems guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html) — NVIDIA, 2024
- [ ] [GPU MODE lectures](https://github.com/gpu-mode/lectures) — GPU MODE community, 2024

## On the job

**Roles that use this:** ML performance engineer, ML infrastructure engineer, TPM for training infrastructure, GPU developer advocate

**At enterprise scale:**

- Finding why a training cluster runs at 35% utilization and raising it
- Profiling a slow inference service before a major launch and removing sync stalls

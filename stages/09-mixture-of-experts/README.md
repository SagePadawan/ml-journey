# Stage 9 · Mixture of experts

Weeks 42–43 · Compute: Mac; keep the model tiny

**Why it’s here:** Needs your GPT, your roofline and your evaluation habits. MoE claims are about loss per FLOP and bytes moved, and both need honest measurement.

**Test it:** Test that the router sends each token to exactly k experts and that the balancing loss stays finite.

## The idea

**What holds up.** MoE separates total parameters from FLOPs per token. DeepSeek-V3 reported a competitive model at a training compute budget far below comparable dense models.

**Where it breaks.** Every expert still has to be stored and moved. MoE adds memory cost, all-to-all communication and load-balancing problems, and at large decode batches nearly every expert gets touched.

**Concepts:** Router / gating, Top-k routing, Load balancing, Active vs total params, Expert parallelism, All-to-all comm, Conditional memory (Engram)

## Project: MoE-ify your GPT

Replace the MLP in your Stage 3 model with a top-2-of-8 expert layer and study how routing behaves. Keep the model tiny so it trains on your Mac. Runs at measure-and-reason depth: the full dense comparisons are Deep path.

Each milestone below is a GitHub issue in the milestone **Stage 9 · Mixture of experts**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Router with top-2 gating and a load-balancing auxiliary loss
2. Log tokens per expert per step and plot the histogram over training
3. Ablate the balancing loss and document router collapse
4. Deep path: compare loss vs FLOPs for MoE, dense-active and dense-total
5. Count bytes of weights touched per decode step at batch 1 and batch 256
6. Deep path: compare MoE vs dense-active on held-out loss across 3 seeds with confidence intervals

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/09-mixture-of-experts/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict how many experts get at least one token in a batch of 256 tokens.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain why active parameters set the FLOPs but total parameters set the GPU count.

300 words, or a link to a 3-minute recording:


## Revisit

> Put an MoE layer on your Stage 8 roofline. Is the expert matmul compute-bound at batch 1? What does that mean for an API price quoted per million tokens?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Outrageously Large Neural Networks](https://arxiv.org/abs/1701.06538) — Shazeer et al., 2017 **(core)**
- [ ] [Switch Transformer](https://arxiv.org/abs/2101.03961) — Fedus, Zoph, Shazeer, 2021 **(core)**
- [ ] [DeepSeek-V3 report](https://arxiv.org/abs/2412.19437) — DeepSeek-AI, 2024 **(core)**
- [ ] [Engram: Conditional Memory via Scalable Lookup](https://arxiv.org/abs/2601.07372) — Cheng et al., DeepSeek, 2026 **(core)**
- [ ] [GShard](https://arxiv.org/abs/2006.16668) — Lepikhin et al., 2020
- [ ] [Mixtral of Experts](https://arxiv.org/abs/2401.04088) — Jiang et al., 2024
- [ ] [DeepSeekMoE](https://arxiv.org/abs/2401.06066) — Dai et al., 2024

## On the job

**Roles that use this:** Distributed training engineer, Inference infrastructure engineer, Research engineer (model architecture)

**At enterprise scale:**

- Laying out experts across GPU nodes to match the network topology
- Pricing an MoE model’s API from its active parameters and memory footprint

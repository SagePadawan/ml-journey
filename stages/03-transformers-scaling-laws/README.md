# Stage 3 · Transformers & scaling laws

Weeks 12–14 · Compute: Mac (PyTorch on MPS, or MLX)

**Why it’s here:** You now have the math to derive attention and the evaluation habits to trust your own scaling fit.

**Test it:** Test the causal mask (no token can see the future) and that loss on one tiny batch drops near zero.

**Safety and security:** Language models memorize rare training text, so anything private in your training data can come back out.

## The idea

**What holds up.** Attention plus scale explains most recent language-model progress. Loss falls as a smooth power law in parameters, data and compute.

**Where it breaks.** Kaplan’s compute allocation was revised by Chinchilla, which found tokens matter about as much as parameters. Scaling laws count FLOPs and say nothing about how long a FLOP takes on real hardware.

**Concepts:** Tokenization, Self-attention, Multi-head attention, Positional encoding, Residuals & LayerNorm, Scaling laws, Compute-optimal training

## Project: Tiny GPT and a scaling sweep

Write a decoder-only transformer without nn.Transformer, train it on a small text corpus, then train five sizes and fit a power law to final loss.

Each milestone below is a GitHub issue in the milestone **Stage 3 · Transformers & scaling laws**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Single-head causal self-attention with a visible mask test
2. Multi-head attention, MLP, residuals and LayerNorm assembled into blocks
3. Train to a validation loss that beats a bigram baseline by a wide margin
4. Train 5 model sizes on the same token budget and log FLOPs with 6·N·D
5. Fit loss vs parameters on a log-log plot and report the exponent

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/03-transformers-scaling-laws/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Guess the fitted exponent and the size where your curve flattens before you fit anything.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain scaled dot-product attention, including the √dₖ, to someone who knows matrix multiplication.

300 words, or a link to a 3-minute recording:


## Revisit

> Report your validation loss across three seeds with a bootstrap interval. Is the gap over the bigram baseline real?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017 **(core)**
- [ ] [Let’s build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Andrej Karpathy, 2023 **(core)**
- [ ] [Scaling Laws for Neural LMs](https://arxiv.org/abs/2001.08361) — Kaplan et al., 2020 **(core)**
- [ ] [Chinchilla](https://arxiv.org/abs/2203.15556) — Hoffmann et al., 2022 **(core)**
- [ ] [nanochat (successor to nanoGPT)](https://github.com/karpathy/nanochat) — Andrej Karpathy, 2025
- [ ] [GPT-3](https://arxiv.org/abs/2005.14165) — Brown et al., 2020
- [ ] [RoFormer (RoPE)](https://arxiv.org/abs/2104.09864) — Su et al., 2021
- [ ] [Neural MT of Rare Words with Subword Units (BPE)](https://arxiv.org/abs/1508.07909) — Sennrich, Haddow, Birch, 2015
- [ ] [Stanford CS336 (Spring 2026)](https://cs336.stanford.edu/) — Liang & Hashimoto, 2026

## On the job

**Roles that use this:** Research engineer (pretraining), LLM engineer, Research scientist, AI compute capacity planner

**At enterprise scale:**

- Running small scaling-law sweeps that decide how big the next flagship model should be
- Forecasting how many GPUs and weeks a training run needs, months in advance
- Pretraining a domain model on a bank’s or hospital’s own text

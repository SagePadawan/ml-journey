# Stage 4 · Training dynamics

Weeks 15–16 · Compute: Mac

**Why it’s here:** Follows the transformer because you now have a real model whose training you can break and fix.

**Test it:** Run the same short training twice with the same seed and assert the losses match. Unrepeatable runs hide real bugs.

**Safety and security:** A few bad training examples can plant a hidden trigger. Know where every training file came from.

## The idea

**What holds up.** Most training failures are recipe problems, not architecture problems. Learning rate, warmup, initialization, batch size and numeric precision decide whether a good model trains at all.

**Where it breaks.** Rules of thumb don’t transfer across scale. The best learning rate shifts as models grow, loss spikes show up mostly in big runs, and a run that looks fine on training loss can be quietly overfitting.

**Concepts:** Learning rate & schedules, Warmup, Initialization, Batch size, Gradient clipping, Mixed precision, Regularization, Loss spikes & instability, μP (hyperparameter transfer)

## Project: Break it, then fix it

Take your Stage 3 GPT and break training five ways. Diagnose each failure from the loss curve and gradient statistics alone, then fix it. End with a learning-rate sweep at two model widths.

Each milestone below is a GitHub issue in the milestone **Stage 4 · Training dynamics**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Log loss, gradient norm, learning rate and weight norms every step to a dashboard such as TensorBoard
2. Break it five ways: learning rate 10× too high, no warmup, bad initialization, no gradient clipping, fp16 without loss scaling; screenshot each failure
3. Fix each one and write a one-line diagnosis rule per failure
4. Overfit one tiny batch to prove the model can learn, then add weight decay or dropout and show the train–validation gap shrink
5. Sweep the learning rate at two model widths and plot how the best value moves

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/04-training-dynamics/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict whether the best learning rate goes up or down when you double model width.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain warmup to someone who has never trained a model.

300 words, or a link to a 3-minute recording:


## Revisit

> Do your Stage 3 scaling fits change when each size gets its own tuned learning rate?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/) — Andrej Karpathy, 2019 **(core)**
- [ ] [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook) — Godbole et al., Google, 2023 **(core)**
- [ ] [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — Micikevicius et al., 2017 **(core)**
- [ ] [Decoupled Weight Decay (AdamW)](https://arxiv.org/abs/1711.05101) — Loshchilov & Hutter, 2017
- [ ] [Accurate, Large Minibatch SGD](https://arxiv.org/abs/1706.02677) — Goyal et al., 2017
- [ ] [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852) — He et al., 2015
- [ ] [Tensor Programs V (μP)](https://arxiv.org/abs/2203.03466) — Yang et al., 2022
- [ ] [Dropout](https://jmlr.org/papers/v15/srivastava14a.html) — Srivastava et al., 2014

## On the job

**Roles that use this:** Research engineer, ML infrastructure engineer, Training reliability engineer

**At enterprise scale:**

- Monitoring a multi-week run on thousands of GPUs and rewinding to a checkpoint after a loss spike
- Tuning hyperparameters on small proxy models so settings transfer to the full-size run
- Building the dashboards and alerts that catch divergence before it wastes a week of compute

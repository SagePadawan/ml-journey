# Stage 5 · Post-training

Weeks 17–19 · Compute: Mac with MLX for LoRA; a rented GPU makes DPO much faster

**Why it’s here:** Needs a pretrained model, training-dynamics instincts and evaluation discipline, which Stages 2 to 4 just gave you.

**Test it:** Keep a fixed set of prompts and check every new checkpoint against it before you keep it.

**Safety and security:** Preference tuning shapes safety behavior. Measure refusals and harmful outputs before and after tuning, not just helpfulness.

## The idea

**What holds up.** A pretrained model knows a lot but doesn’t follow instructions. Supervised fine-tuning teaches the format, and preference tuning (RLHF or DPO) pushes it toward answers people prefer, using a small fraction of pretraining compute.

**Where it breaks.** Preference tuning optimizes a stand-in for what people want. Push too hard and the model learns to please the reward model (reward hacking), drifts from its base knowledge, or gets wordier without getting better. Catching that takes Stage 2 discipline.

**Concepts:** Supervised fine-tuning, LoRA, Reward model, RLHF, DPO, KL penalty, Reward hacking, LLM-as-a-judge, RL with verifiable rewards, RL environments & GRPO, Interpretability

## Project: Instruct-tune a small model

Fine-tune a small open model (about 0.5 to 1B parameters) with LoRA on an instruction dataset, then run DPO on a preference dataset. Evaluate each step against the base model on held-out prompts.

Each milestone below is a GitHub issue in the milestone **Stage 5 · Post-training**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Run the base model on 50 held-out prompts and save the outputs as your baseline
2. Supervised fine-tune with LoRA on an instruction dataset; plot training and validation loss
3. Run DPO on a preference dataset, starting from your fine-tuned checkpoint
4. Compare base, SFT and DPO by win rate (LLM-as-a-judge with answer order swapped) and one exact-match task, with bootstrap intervals
5. Find a reward-hacking or length-bias symptom in your DPO outputs and document it
6. Deep path: write a verifiable RL environment (for example, a checker that scores storyboard shot lists against a script) and run a small GRPO loop with TRL on a rented GPU

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/05-post-training/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict the DPO-vs-SFT win rate and how much average answer length will change.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain the difference between RLHF and DPO in three sentences, without equations.

300 words, or a link to a 3-minute recording:


## Revisit

> Put your Stage 4 dashboard on the fine-tuning run. Which training failure is most likely at this scale?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [InstructGPT](https://arxiv.org/abs/2203.02155) — Ouyang et al., 2022 **(core)**
- [ ] [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — Rafailov et al., 2023 **(core)**
- [ ] [LoRA](https://arxiv.org/abs/2106.09685) — Hu et al., 2021 **(core)**
- [ ] [Proximal Policy Optimization](https://arxiv.org/abs/1707.06347) — Schulman et al., 2017
- [ ] [Constitutional AI](https://arxiv.org/abs/2212.08073) — Bai et al., 2022
- [ ] [Judging LLM-as-a-Judge (MT-Bench)](https://arxiv.org/abs/2306.05685) — Zheng et al., 2023
- [ ] [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760) — Gao, Schulman, Hilton, 2022
- [ ] [Tülu 3](https://arxiv.org/abs/2411.15124) — Lambert et al., 2024
- [ ] [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — DeepSeek-AI, 2025
- [ ] [TRL library docs](https://huggingface.co/docs/trl) — Hugging Face, 2024
- [ ] [DeepSeekMath (introduces GRPO)](https://arxiv.org/abs/2402.03300) — Shao et al., 2024
- [ ] [Toy Models of Superposition](https://arxiv.org/abs/2209.10652) — Elhage et al., 2022
- [ ] [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — Lindsey et al., Anthropic, 2025
- [ ] [circuit-tracer](https://github.com/decoderesearch/circuit-tracer) — Open-source tool, 2025

## On the job

**Roles that use this:** Post-training research engineer, Alignment researcher, Human-data operations lead, Model behavior PM

**At enterprise scale:**

- Running preference-data programs with thousands of annotators and quality checks
- Fine-tuning a customer-support model to follow one company’s policies and tone
- Training reasoning models with verifiable rewards on code and math

# Stage 2 · Data & evaluation

Weeks 6–7 · Compute: Mac

**Why it’s here:** Comes before any big model, so every number you report from here on has an honest split, a baseline and an error bar.

**Test it:** Write tests that fail if any example appears in two splits, if the schema changes, or if label balance shifts sharply.

**Safety and security:** Data leakage has a privacy twin: keep real people’s data out of public repos, and treat test sets that contain it as sensitive.

## The idea

**What holds up.** A model is only as good as its data and the test that measures it. A clean held-out split, a strong baseline and an honest metric catch most bad conclusions.

**Where it breaks.** Benchmarks leak into training data, test sets get reused until they are overfit, and small score differences are often noise. A number without an error bar and a contamination check is a rumor.

**Concepts:** Train / val / test splits, Data leakage, Benchmark contamination, Baselines, Overfitting & generalization, Metrics, Error bars & bootstrap, Benchmarks, Distribution shift, Testing ML systems

## Project: Leak hunt

Train a simple classifier on a real dataset, then deliberately add four kinds of leakage and measure how much each one inflates the score. Finish by comparing two models with bootstrap confidence intervals and checking a benchmark for contamination.

Each milestone below is a GitHub issue in the milestone **Stage 2 · Data & evaluation**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Make train, validation and test splits; write down what the test set is for and lock it away
2. Train baselines (majority class, then logistic regression) and record their scores
3. Add leakage four ways: duplicates across splits, a target-derived feature, preprocessing fit on all data, and a time-order violation; measure each inflation
4. Compute bootstrap 95% intervals for two models and decide whether the gap is real
5. Check a small public benchmark against a text corpus for 13-gram overlap and report the contamination rate
6. Write pytest tests for your data pipeline (no example in two splits, schema and label checks) and have them run automatically on every push

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/02-data-evaluation/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Guess which leak inflates accuracy the most before running any of them.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain to a non-engineer why a 0.5-point leaderboard gain may mean nothing.

300 words, or a link to a 3-minute recording:


## Revisit

> Re-run your Stage 1 MLP with a proper validation split. Was it overfitting?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Leakage and the Reproducibility Crisis in ML-based Science](https://arxiv.org/abs/2207.07048) — Kapoor & Narayanan, 2022 **(core)**
- [ ] [Do ImageNet Classifiers Generalize to ImageNet?](https://arxiv.org/abs/1902.10811) — Recht et al., 2019 **(core)**
- [ ] [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640) — Evan Miller, 2024 **(core)**
- [ ] [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118) — Ribeiro et al., 2020 **(core)**
- [ ] [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) — Gebru et al., 2018
- [ ] [HELM](https://arxiv.org/abs/2211.09110) — Liang et al., 2022
- [ ] [MMLU](https://arxiv.org/abs/2009.03300) — Hendrycks et al., 2020
- [ ] [Time Travel in LLMs: Tracing Data Contamination](https://arxiv.org/abs/2308.08493) — Golchin & Surdeanu, 2023
- [ ] [The ML Test Score](https://research.google/pubs/pub46555/) — Breck et al., Google, 2017
- [ ] [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — Sculley et al., Google, 2015

## On the job

**Roles that use this:** ML evaluation engineer, Data scientist, Data quality engineer, Responsible AI analyst, TPM for model launches

**At enterprise scale:**

- Owning the eval suite that must pass before any model release ships at an AI lab
- Auditing a fraud model that looked 99% accurate and finding target leakage
- Running contamination checks before a company publishes benchmark results
- Writing the launch criteria (metrics, error bars, regressions) a program review signs off on

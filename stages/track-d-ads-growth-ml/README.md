# Track D · Ads & growth ML

Weeks 8–11 · Compute: Mac · Builds toward: the ad marketplace, the agency CRM

**Why it’s here:** Needs only math and evaluation, so it starts right after Stage 2. It runs on tabular data, so your Mac is enough, and it gives the agency CRM a working lead-scoring model early.

**Test it:** Test feature code for leakage: assert that no feature uses information from after the moment of prediction.

**Safety and security:** Housing, job and credit ads have legal limits on targeting by protected traits and close stand-ins such as zip code. Check lookalike features for proxies.

## The idea

**What holds up.** Most business ML runs on tables, not text. Gradient-boosted trees on well-built features beat deep models on most tabular problems, and calibrated probabilities turn predictions into budget decisions.

**Where it breaks.** Prediction isn’t causation. A model that predicts who converts doesn’t tell you which ad caused the sale, and optimizing on observed clicks bakes in the platform’s own targeting. Proving that spend worked takes experiments or careful causal methods.

**Concepts:** Gradient-boosted trees, Feature engineering, Calibration, CTR & conversion prediction, Recommendation & matching, Bandits, A/B testing & power, Causal inference & uplift, Attribution & media mix, Entity resolution

## Project: Ad marketplace campaign brain

Using a public ad dataset plus your agency’s own records, predict conversion, allocate a simulated budget across channels with a bandit, and estimate the true lift of one campaign. The lead-scoring model feeds the agency CRM.

Each milestone below is a GitHub issue in the milestone **Track D · Ads & growth ML**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Train logistic regression and gradient-boosted trees on a public click-through dataset; compare log loss and AUC with bootstrap intervals
2. Calibrate the better model and plot a reliability diagram; write down why calibration matters for bidding
3. Score your own past leads for likelihood to book, then check feature importances for leakage
4. Simulate 5 channels with hidden conversion rates; compare a fixed split, epsilon-greedy and Thompson sampling on total conversions
5. Design an A/B test for one real campaign: power analysis, sample size, and the analysis plan written before you see results
6. Estimate lift on a public uplift dataset with a two-model approach, and compare it with the naive difference

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/track-d-ads-growth-ml/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict how many simulated days Thompson sampling needs to find the best channel.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain to a client why “people who saw the ad bought more” doesn’t prove the ad worked.

300 words, or a link to a 3-minute recording:


## Revisit

> Run your Stage 2 leakage checklist on the lead-scoring features. Which one would give away the outcome?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [XGBoost](https://arxiv.org/abs/1603.02754) — Chen & Guestrin, 2016 **(core)**
- [ ] [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — Grinsztajn, Oyallon, Varoquaux, 2022 **(core)**
- [ ] [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — Kohavi, Tang, Xu, 2020 **(core)**
- [ ] [A Tutorial on Thompson Sampling](https://arxiv.org/abs/1707.02038) — Russo et al., 2017 **(core)**
- [ ] [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — Guo et al., 2017
- [ ] [DLRM](https://arxiv.org/abs/1906.00091) — Naumov et al., 2019
- [ ] [Causal Inference: The Mixtape (online edition, now The Remix)](https://mixtape.scunning.com/) — Scott Cunningham, 2021
- [ ] [Causal Inference and Uplift Modeling: A Review](http://proceedings.mlr.press/v67/gutierrez17a.html) — Gutierrez & Gérardy, 2017

## On the job

**Roles that use this:** Ads ranking ML engineer, Marketing data scientist, Experimentation platform engineer, Growth analyst, Ads measurement PM

**At enterprise scale:**

- Click-through-rate models that score billions of ad auctions a day at an ad platform
- Geo-lift and holdout studies that prove a campaign’s return to a large advertiser
- Marketing mix models that set a retailer’s quarterly budget across channels
- Lead-scoring models inside enterprise CRMs that route sales teams to the best accounts

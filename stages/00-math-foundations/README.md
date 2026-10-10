# Stage 0 · Math foundations

Weeks 1–3 · Compute: Mac

**Why it’s here:** Every later derivation, from attention to scaling-law fits to DPO’s loss, is built from these pieces.

**Test it:** Check every hand-derived gradient against finite differences in a test that runs automatically.

## The idea

**What holds up.** Most of ML is a few pieces of math used over and over: vectors and matrix multiplies, probability, derivatives, and lowering a loss by stepping downhill.

**Where it breaks.** Nothing breaks yet. Skipping this is what makes the attention and scaling-law derivations feel like magic later.

**Concepts:** Vectors & matrices, Matrix multiplication, Eigenvectors & PCA, Derivatives & chain rule, Gradient descent, Probability, Maximum likelihood, Entropy & cross-entropy, Softmax

## Project: Regression from scratch

Using only NumPy, fit linear regression three ways, then logistic regression with gradients you derived on paper. Finish with PCA from the eigenvectors of a covariance matrix.

Each milestone below is a GitHub issue in the milestone **Stage 0 · Math foundations**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Derive the gradient of mean squared error by hand and check it with finite differences
2. Fit linear regression with the normal equations and with gradient descent; confirm they agree
3. Logistic regression on a 2-class dataset using your hand-derived cross-entropy gradient
4. Sweep 5 learning rates and plot the loss curves; find where training diverges
5. PCA on a small dataset from the covariance matrix’s eigenvectors; plot the first two components

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/00-math-foundations/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Before the sweep, guess the largest learning rate that won’t diverge.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain why cross-entropy is the negative log-likelihood of the data, using a coin-flip example.

300 words, or a link to a 3-minute recording:


## Revisit

> Nothing to revisit yet. Start the error log here.



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — 3Blue1Brown (Grant Sanderson), 2016 **(core)**
- [ ] [Mathematics for Machine Learning](https://mml-book.github.io/) — Deisenroth, Faisal, Ong, 2020 **(core)**
- [ ] [The Matrix Calculus You Need for Deep Learning](https://arxiv.org/abs/1802.01528) — Parr & Howard, 2018 **(core)**
- [ ] [Seeing Theory](https://seeing-theory.brown.edu/) — Brown University, 2016
- [ ] [CS229 lecture notes](https://cs229.stanford.edu/main_notes.pdf) — Andrew Ng et al., Stanford, 2023

## On the job

**Roles that use this:** Data scientist, ML engineer, Research scientist, Quantitative analyst

**At enterprise scale:**

- Tracing why a recommendation model’s gradients explode after a new feature ships, and fixing the math
- Compressing millions of product embeddings with PCA before indexing them for search
- Explaining to leadership why a demand forecast’s uncertainty widened this quarter

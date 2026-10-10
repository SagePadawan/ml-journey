# Stage 6 · Convolution & inductive bias

Weeks 26–27 · Compute: Mac

**Why it’s here:** Placed here so the CNN-vs-ViT comparison uses proper evaluation, and because the CNN and ViT backbones are what Tracks B and A build on. It also sets up a question the systems stages answer: why is convolution so cheap?

**Test it:** Add behavioral tests: a flipped or slightly cropped image should get the same label.

**Safety and security:** Vision models can be fooled by tiny, invisible pixel changes, so never use one alone for a security decision.

## The idea

**What holds up.** Convolution builds in locality and weight sharing, so it needs less data, and each weight is reused at every position, which keeps arithmetic intensity high.

**Where it breaks.** ViT showed that weak priors win once data is large enough, and ConvNeXt showed much of the remaining gap was training recipe. Inductive bias is a trade against data, not a law.

**Concepts:** Convolution, Locality, Weight sharing, Patch embedding, Inductive bias

## Project: CNN vs ViT on a data diet

Train a small ResNet-style CNN and a tiny ViT with matched parameter counts on CIFAR-10 at 10%, 30% and 100% of the training set. Count FLOPs per image for both.

Each milestone below is a GitHub issue in the milestone **Stage 6 · Convolution & inductive bias**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Small CNN baseline with augmentation and a cosine schedule
2. Tiny ViT with patch embedding, reusing your Stage 3 attention block
3. Run both at three data fractions with the same budget
4. Plot accuracy vs data fraction and annotate FLOPs per image

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/06-convolution-inductive-bias/` instead. That folder is a separate private repo and never appears here.

## Predict first

> At which data fraction does the gap close, if it closes at all at this scale?

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain “inductive bias” using your plot, not a definition.

300 words, or a link to a 3-minute recording:


## Revisit

> Use your Stage 2 bootstrap intervals. At which data fractions is the CNN–ViT gap real?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [ResNet](https://arxiv.org/abs/1512.03385) — He et al., 2015 **(core)**
- [ ] [Vision Transformer (ViT)](https://arxiv.org/abs/2010.11929) — Dosovitskiy et al., 2020 **(core)**
- [ ] [ConvNeXt](https://arxiv.org/abs/2201.03545) — Liu et al., 2022 **(core)**
- [ ] [LeNet: Gradient-Based Learning Applied to Document Recognition](https://doi.org/10.1109/5.726791) — LeCun et al., 1998
- [ ] [AlexNet](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) — Krizhevsky, Sutskever, Hinton, 2012
- [ ] [CS231n conv notes](https://cs231n.github.io/convolutional-networks/) — Stanford, 2016

## On the job

**Roles that use this:** Computer vision engineer, Perception engineer (robotics, autonomous vehicles), Edge ML engineer

**At enterprise scale:**

- Defect detection on factory cameras with models small enough to run on the line
- Choosing a CNN or transformer backbone for a phone camera feature under a strict latency budget

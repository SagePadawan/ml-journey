# Stage 1 · Neural nets & autograd

Weeks 4–5 · Compute: Mac

**Why it’s here:** Autograd is the chain rule from Stage 0 turned into code, and every project after this trains something.

**Test it:** Test shapes, gradients and a one-batch overfit. These three checks catch most model bugs.

**Safety and security:** Saved PyTorch .pt files are pickles that can run code when loaded. Load downloaded weights with weights_only=True, or use safetensors.

## The idea

**What holds up.** A neural network is a differentiable program. Stack simple functions, measure the loss, and autograd gives you the gradient of everything.

**Where it breaks.** Autograd gives you gradients, not good training. Whether a model learns anything useful is a data and training-dynamics question, covered in Stages 2 and 4.

**Concepts:** Tensors & shapes, MLP & activations, Autograd, Next-token loss, Optimizers

## Project: Micrograd replay

Rebuild a scalar autograd engine from memory, then use it to train a small MLP. Check every gradient against PyTorch.

Each milestone below is a GitHub issue in the milestone **Stage 1 · Neural nets & autograd**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Value class with +, *, tanh and a backward() that walks a topological sort
2. Gradient check: match PyTorch to 1e-6 on a random expression
3. Train a 2-layer MLP on a toy 2D dataset to >95% accuracy
4. Rewrite the training loop in PyTorch and confirm identical loss curves

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/01-neural-nets-autograd/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Before running backward(), compute one weight’s gradient by hand and write it down.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain why gradients are summed when a value feeds two operations.

300 words, or a link to a 3-minute recording:


## Revisit

> Redo your Stage 0 logistic regression as a one-neuron network in your engine. Do the gradients match your hand derivation?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Intro to backprop (micrograd)](https://www.youtube.com/watch?v=VMj-3S1tku0) — Andrej Karpathy, 2022 **(core)**
- [ ] [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — Andrej Karpathy, 2023
- [ ] [Adam](https://arxiv.org/abs/1412.6980) — Kingma & Ba, 2014
- [ ] [Deep Learning (book)](https://www.deeplearningbook.org/) — Goodfellow, Bengio, Courville, 2016

## On the job

**Roles that use this:** ML engineer, Applied scientist, Framework engineer (PyTorch, JAX, MLX teams)

**At enterprise scale:**

- Writing a custom layer and its gradient for a ranking model, then proving it matches a reference implementation
- Porting a production model between frameworks and showing outputs match to 1e-6
- Building shared training pipelines that dozens of internal teams reuse

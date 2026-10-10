# ML Journey

A one-year, project-first path from math foundations to frontier ML systems, with applied tracks that build working pieces of four products: an ad marketplace, a script-to-storyboard app, an AI video editor and an agency CRM.

**Progress:** see [PROGRESS.md](PROGRESS.md), which updates itself whenever an issue is closed or a reading is ticked.

## How each stage works

1. **Predict.** Write a number in the stage README before running anything.
2. **Build.** Code goes in the stage’s `code/` folder, plots and tables in `results/`.
3. **Measure.** Fill in the Results table and log any big miss in [ERRORS.md](ERRORS.md).
4. **Test.** Add `test_*.py` files next to your code. GitHub runs them on every push and marks the commit red if anything fails.
5. **Explain.** Write the explain-back section without notes.
6. **Revisit.** Answer the revisit prompt, then close the stage’s issues.

Each week, add one row to [LOG.md](LOG.md).

## Study order

| # | Stage | Weeks | Project |
|---|---|---|---|
| Stage 0 | [Math foundations](stages/00-math-foundations/) | 1–3 | Regression from scratch |
| Stage 1 | [Neural nets & autograd](stages/01-neural-nets-autograd/) | 4–5 | Micrograd replay |
| Stage 2 | [Data & evaluation](stages/02-data-evaluation/) | 6–7 | Leak hunt |
| Track D | [Ads & growth ML](stages/track-d-ads-growth-ml/) | 8–11 | Ad marketplace campaign brain |
| Stage 3 | [Transformers & scaling laws](stages/03-transformers-scaling-laws/) | 12–14 | Tiny GPT and a scaling sweep |
| Stage 4 | [Training dynamics](stages/04-training-dynamics/) | 15–16 | Break it, then fix it |
| Stage 5 | [Post-training](stages/05-post-training/) | 17–19 | Instruct-tune a small model |
| Track C | [LLM applications](stages/track-c-llm-applications/) | 20–23 | Agency CRM proposal agent |
| Track S | [Security, privacy & safety](stages/track-s-security-privacy-safety/) | 24–25 | Red-team your own agent |
| Stage 6 | [Convolution & inductive bias](stages/06-convolution-inductive-bias/) | 26–27 | CNN vs ViT on a data diet |
| Track B | [Video & audio understanding](stages/track-b-video-audio-understanding/) | 28–31 | Video editor assistant |
| Track A | [Generative vision](stages/track-a-generative-vision/) | 32–37 | Storyboard engine |
| Stage 7 | [GPU execution & profiling](stages/07-gpu-execution-profiling/) | 38–39 | Read the trace |
| Stage 8 | [IO-aware kernels](stages/08-io-aware-kernels/) | 40–41 | Roofline your GPU, then write the kernel |
| Stage 9 | [Mixture of experts](stages/09-mixture-of-experts/) | 42–43 | MoE-ify your GPT |
| Stage 10 | [Inference at scale](stages/10-inference-at-scale/) | 44–47 | Capstone: the comeback |

Weeks 48–52 are buffer for catching up and shipping product slices.

## Set up your Mac

On an Apple Silicon Mac, paste this into Terminal. It installs Homebrew, Git, the GitHub CLI, uv, VS Code and GitHub Desktop, clones this repo to `~/ml-journey`, builds the Python environment (Python 3.12, PyTorch, MLX, Jupyter), and records your machine in [ENVIRONMENT.md](ENVIRONMENT.md):

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SagePadawan/ml-journey/main/scripts/bootstrap-mac.sh)"
```

The Python packages are pinned in `uv.lock`, so the environment can be rebuilt exactly. Add tools when a stage needs them:

| Command | When |
|---|---|
| `uv sync --group tabular` | Track D (XGBoost, LightGBM) |
| `uv sync --group llm` | Stage 5 and Track C (Transformers, TRL, PEFT, MLX-LM) |
| `uv sync --group vision` | Stage 6 and Tracks A and B (Diffusers, OpenCV, OpenCLIP) |
| `uv sync --group audio` | Track B (librosa, MLX Whisper) |

## Public and private

This repo is public. A second, private repo lives in the `private/` folder (it is ignored here and pushed to `ml-journey-private`). Use it for client data, real leads and proposals, pricing, footage, transcripts and anything you would not post publicly. Commit the method and results summaries here, and the sensitive inputs there.

A pre-commit check blocks commits that contain API keys or files over 20 MB. Keys belong in `.env`, which git ignores.

## Repo conventions

- One folder per stage under `stages/`. Each has a README, `code/` and `results/`.
- Every project milestone is a GitHub issue grouped under a GitHub milestone with a due date.
- Commit messages that include `Closes #12` close issue 12 automatically.
- Datasets, model weights and raw footage stay out of git (see `.gitignore`). Keep them on your external drive and note where they live in the stage README.

# Track A · Generative vision

Weeks 32–37 · Compute: Cloud NVIDIA GPU for video models; Mac for image work · Builds toward: the storyboard app, the video editor

**Why it’s here:** Comes after Track B, so you already have the masks, depth maps and poses that control generation, and after Stage 5, so LoRA and preference tuning carry over.

**Test it:** Generate with fixed seeds and reference images so you can see when a change alters identity or style.

**Safety and security:** Generated media can deceive. Label it, keep provenance metadata (C2PA), and never generate real people without permission.

## The idea

**What holds up.** Diffusion and flow-matching models make images by learning to undo noise step by step. Working in a compressed latent space makes this affordable, and conditioning signals such as text, pose, depth and reference images give you control.

**Where it breaks.** Control is the hard part. Text prompts don’t pin down identity, camera or layout; characters drift between shots; video models flicker; and every denoising step is a full model pass, so speed and consistency trade against each other.

**Concepts:** Diffusion models, Samplers & steps, Flow matching, Latent diffusion & VAEs, Classifier-free guidance, Conditioning & control, Character consistency, Inpainting & editing, Video generation, Camera & 3D, Diffusion language models

## Project: Storyboard engine

Turn a three-scene script into a consistent storyboard: one character with a fixed identity, controlled poses and framing, and a short animated shot. Start with a tiny diffusion model you write yourself, then move to an open latent diffusion model.

Each milestone below is a GitHub issue in the milestone **Track A · Generative vision**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Train a tiny DDPM on 32×32 images from scratch; save sample grids every few epochs
2. Swap the objective for flow matching and compare sample quality at 10, 25 and 50 steps
3. With an open latent diffusion model, generate one shot three ways: text only, with depth and pose conditioning, and with a reference image
4. Train a character LoRA on 15–30 images; measure identity consistency across 20 shots with face-embedding similarity
5. Generate a 3-second clip with an open video model from a storyboard frame; measure flicker with optical-flow warping error
6. Build script → shot list → frames end to end and run a blind preference test against plain text-to-image
7. Deep path: run an open text-diffusion model such as DiffusionGemma on a rented GPU and compare tokens per second and quality with its autoregressive twin on a caption-editing task

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/track-a-generative-vision/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict how many denoising steps you can cut before you notice quality loss.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain classifier-free guidance, and why turning it up too high makes images worse.

300 words, or a link to a 3-minute recording:


## Revisit

> Compare your character LoRA with the language LoRA from Stage 5. What is the same, and what is different?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — Lilian Weng, 2021 **(core)**
- [ ] [DDPM](https://arxiv.org/abs/2006.11239) — Ho, Jain, Abbeel, 2020 **(core)**
- [ ] [Latent Diffusion (Stable Diffusion)](https://arxiv.org/abs/2112.10752) — Rombach et al., 2021 **(core)**
- [ ] [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — Ho & Salimans, 2022 **(core)**
- [ ] [ControlNet](https://arxiv.org/abs/2302.05543) — Zhang, Rao, Agrawala, 2023 **(core)**
- [ ] [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) — Lipman et al., 2022
- [ ] [DiT: Scalable Diffusion with Transformers](https://arxiv.org/abs/2212.09748) — Peebles & Xie, 2022
- [ ] [DreamBooth](https://arxiv.org/abs/2208.12242) — Ruiz et al., 2022
- [ ] [IP-Adapter](https://arxiv.org/abs/2308.06721) — Ye et al., 2023
- [ ] [Stable Video Diffusion](https://arxiv.org/abs/2311.15127) — Blattmann et al., 2023
- [ ] [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) — Kerbl et al., 2023
- [ ] [Diffusers library docs](https://huggingface.co/docs/diffusers) — Hugging Face, 2024
- [ ] [The Flexibility Trap](https://arxiv.org/abs/2601.15165) — Ni et al., 2026
- [ ] [DiffusionGemma 26B-A4B](https://huggingface.co/google/diffusiongemma-26B-A4B-it) — Google DeepMind, 2026

## On the job

**Roles that use this:** Generative media research engineer, Creative tools ML engineer, ML engineer at a VFX or animation studio, Applied scientist for ad creative

**At enterprise scale:**

- Generative fill and video extension features inside creative software suites
- Consistent product imagery for thousands of ad variants from one brand kit
- Previsualization pipelines that turn scripts into animatics for film and game studios

# Track B · Video & audio understanding

Weeks 28–31 · Compute: Mac; a cloud GPU speeds up long clips · Builds toward: the video editor, the storyboard app

**Why it’s here:** Follows Stage 6 because these models are built on CNN and ViT backbones, and it comes before Track A because masks, depth and pose are what you use to control generation.

**Test it:** Keep hand-labeled clips from your own footage as a fixed test set, and never tune on them.

**Safety and security:** Face and voice data counts as biometric data in many places, with consent and retention rules. Get written consent and keep it in your private repo.

## The idea

**What holds up.** Pretrained models now handle most perception tasks out of the box: segment and track an object, estimate depth and motion, embed frames for search, and transcribe speech with word timings.

**Where it breaks.** Real footage breaks them at the edges: motion blur, low light, fast cuts, overlapping speakers, music under dialogue. Errors also build up over time, so a mask that drifts two pixels a frame is useless after ten seconds.

**Concepts:** Shot detection, CLIP & vision-language models, Segmentation, Tracking & optical flow, Depth & pose estimation, Quality assessment, Speech recognition, Source separation, Speech synthesis, Self-supervised learning & JEPA

## Project: Video editor assistant

Point a pipeline at a folder of your own footage. It should find shots, score and cull them, tag them for search, caption the dialogue, and produce a tracked mask for one subject through a full clip.

Each milestone below is a GitHub issue in the milestone **Track B · Video & audio understanding**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Detect shot boundaries in 30 minutes of footage; measure precision and recall against cuts you mark by hand
2. Score each shot for blur, exposure, face visibility and motion; compare its top picks with yours
3. Embed frames with a CLIP-style model and build text search such as “wide shot, golden hour, two people”; measure recall@10
4. Transcribe with a Whisper-class model, add speaker labels and export word-timed captions; measure word error rate on 5 minutes you correct by hand
5. Segment and track one subject through a 20-second clip with a SAM 2–class model; measure how far the mask drifts
6. Separate dialogue from music, then normalize loudness to a broadcast target
7. Compare CLIP features with self-supervised video features (a V-JEPA-class model) for finding visually similar shots; report recall@10 for each

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/track-b-video-audio-understanding/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict where in your clip the tracked mask will fail first.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain the difference between detecting, segmenting and tracking an object, using one of your clips.

300 words, or a link to a 3-minute recording:


## Revisit

> Use Stage 2 discipline: build a small hand-labeled test set from your own footage before trusting any of these models.



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [CLIP](https://arxiv.org/abs/2103.00020) — Radford et al., 2021 **(core)**
- [ ] [SAM 2](https://arxiv.org/abs/2408.00714) — Ravi et al., 2024 **(core)**
- [ ] [Whisper](https://arxiv.org/abs/2212.04356) — Radford et al., 2022 **(core)**
- [ ] [V-JEPA](https://arxiv.org/abs/2404.08471) — Bardes et al., 2024 **(core)**
- [ ] [Segment Anything](https://arxiv.org/abs/2304.02643) — Kirillov et al., 2023
- [ ] [RAFT](https://arxiv.org/abs/2003.12039) — Teed & Deng, 2020
- [ ] [Depth Anything](https://arxiv.org/abs/2401.10891) — Yang et al., 2024
- [ ] [TransNet V2](https://arxiv.org/abs/2008.04838) — Souček & Lokoč, 2020
- [ ] [Hybrid Transformers for Music Source Separation](https://arxiv.org/abs/2211.08553) — Rouard, Massa, Défossez, 2022
- [ ] [pyannote.audio](https://github.com/pyannote/pyannote-audio) — Bredin et al., 2023
- [ ] [VALL-E](https://arxiv.org/abs/2301.02111) — Wang et al., 2023
- [ ] [I-JEPA](https://arxiv.org/abs/2301.08243) — Assran et al., 2023
- [ ] [Masked Autoencoders](https://arxiv.org/abs/2111.06377) — He et al., 2021
- [ ] [DINOv2](https://arxiv.org/abs/2304.07193) — Oquab et al., 2023

## On the job

**Roles that use this:** Computer vision engineer, Video ML engineer (streaming, creative tools), Speech and audio ML engineer, Trust and safety ML engineer

**At enterprise scale:**

- Auto-captioning and translating a streaming service’s whole catalog
- Moderation systems that scan uploaded video for policy violations
- Smart search, auto-reframe and transcript-based editing in professional editing software

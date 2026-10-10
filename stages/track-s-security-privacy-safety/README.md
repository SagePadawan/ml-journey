# Track S · Security, privacy & safety

Weeks 24–25 · Compute: Mac · Builds toward: the ad marketplace, the storyboard app, the video editor, the agency CRM

**Why it’s here:** Comes right after Track C, the first time you ship something that reads untrusted input and takes actions, and before the tracks that handle client footage, faces and voices.

**Test it:** Keep your 30 attacks as an automated test suite and rerun it on every change to the agent.

## The idea

**What holds up.** Most ML security failures are ordinary security failures in a new place: untrusted input, permissions that are too broad, leaked secrets and unvetted dependencies. Threat modeling, least privilege and red-teaming your own system catch most of them.

**Where it breaks.** ML adds attacks ordinary security tools don’t see: instructions hidden in data, poisoned training sets, model files that run code when loaded, and models that leak what they were trained on. Safety failures, such as discriminatory ad targeting or deceptive generated media, cause harm even when nothing is breached.

**Concepts:** Threat modeling & least privilege, Red-teaming, Adversarial examples & jailbreaks, Data poisoning & backdoors, Model supply chain, Privacy attacks & differential privacy, Content provenance & labeling, Fairness in targeting & scoring

## Project: Red-team your own agent

Threat-model the proposal agent from Track C, attack it the way an adversary would, fix what you find, and write the one-page security and privacy review an enterprise customer’s security team would ask for.

Each milestone below is a GitHub issue in the milestone **Track S · Security, privacy & safety**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Threat-model the agent against the OWASP Top 10 for LLM Applications (2026): list its assets, entry points, tools and exactly what each tool may do
2. Red-team it with 30 attacks, including instructions hidden in a lead’s website, data exfiltration through tool calls, and attempts to make it quote unapproved prices; record the success rate
3. Fix the top three problems (least-privilege tools, approval gates, output checks) and re-run the same 30 attacks to measure the improvement
4. Secure the supply chain: load models only as safetensors, pin dependency versions, scan for secrets, and show with a harmless demo why loading an untrusted pickle file runs code
5. Run a membership-inference test on a small model fine-tuned on private text, then retrain with deduplication or differential privacy and compare
6. Write a one-page security, privacy and responsible-use review: data handled, retention, consent for faces and voices, ad-targeting rules, and how generated media is labeled

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/track-s-security-privacy-safety/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict what share of your 30 attacks will succeed before you run them.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain indirect prompt injection to a non-technical client, and why a better prompt can’t fully fix it.

300 words, or a link to a 3-minute recording:


## Revisit

> Go back to your Stage 2 leakage checklist. Which of those leaks would also be a privacy breach if the data were about real people?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [OWASP Top 10 for LLM Applications (2026)](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — OWASP GenAI Security Project, 2026 **(core)**
- [ ] [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) — Carlini et al., 2020 **(core)**
- [ ] [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/) — OWASP GenAI Security Project, 2026
- [ ] [MITRE ATLAS](https://atlas.mitre.org/) — MITRE, 2024
- [ ] [NIST AI RMF: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) — NIST, 2024
- [ ] [Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572) — Goodfellow, Shlens, Szegedy, 2014
- [ ] [Universal and Transferable Adversarial Attacks on Aligned LMs](https://arxiv.org/abs/2307.15043) — Zou et al., 2023
- [ ] [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) — Carlini et al., 2023
- [ ] [Membership Inference Attacks](https://arxiv.org/abs/1610.05820) — Shokri et al., 2016
- [ ] [Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133) — Abadi et al., 2016
- [ ] [safetensors docs](https://huggingface.co/docs/safetensors) — Hugging Face, 2024
- [ ] [C2PA content credentials](https://c2pa.org/) — Coalition for Content Provenance and Authenticity, 2024
- [ ] [Fairness and Machine Learning](https://fairmlbook.org/) — Barocas, Hardt, Narayanan, 2023

## On the job

**Roles that use this:** AI security engineer, AI red-team engineer, Privacy engineer, Trust and safety lead, AI governance program manager, Security TPM

**At enterprise scale:**

- Red-teaming a new model or agent before launch and tracking every finding to a fix
- Running the AI risk review that every customer-facing AI feature must pass, mapped to NIST AI RMF
- Answering enterprise customers’ security questionnaires about how their data is used in AI features
- Detecting and removing deepfake and scam ads on an ad platform

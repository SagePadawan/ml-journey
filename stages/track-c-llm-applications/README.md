# Track C · LLM applications

Weeks 20–23 · Compute: Mac plus API credits; a small cloud server to deploy · Builds toward: the agency CRM, the storyboard app, the video editor

**Why it’s here:** Follows Stage 5 because you now know what fine-tuning and judges can and can’t do, so you can choose between prompting, retrieval and tuning.

**Test it:** Every prompt or model change reruns the eval set. Block the change if scores drop beyond the error bars.

**Safety and security:** Agents that read the web can be hijacked by hidden instructions. Give tools the least access they need and require approval for anything irreversible. Track S goes deeper.

## The idea

**What holds up.** Most of an LLM product’s value comes from the system around the model: structured outputs your code can trust, retrieval that grounds answers in your own data, tools the model can call, and evals that catch regressions.

**Where it breaks.** LLM apps fail quietly. Retrieval misses the right document, agents loop or take the wrong action, and outputs shift when the model changes. Without an eval set and logged traces, you can’t tell whether a prompt change helped. In production, an agent that can act also needs limits on what it may do and spend.

**Concepts:** Prompting & context, Structured output, Retrieval-augmented generation, Vector & hybrid search, Tool use & agents, Prompt injection & guardrails, App evals & tracing, Deploying agents, MCP & tool servers, Decision models (System 1), Long-horizon agent evals, Continual learning & memory

## Project: Agency CRM proposal agent

Build an agent that reads a lead’s website, extracts structured facts, retrieves your most relevant past projects, and drafts a proposal and landing-page copy. An eval set scores every version, and the finished agent is deployed with limits, approvals and monitoring.

Each milestone below is a GitHub issue in the milestone **Track C · LLM applications**. When you finish one, commit your work with a message that includes `Closes #<issue number>`.

1. Extract company name, industry, size signals and contact page into a validated JSON schema from 50 real websites; measure field accuracy
2. Index your past proposals and project notes; build retrieval with embeddings plus keyword search; measure recall@5 on 30 queries you write
3. Draft proposals grounded in the retrieved projects, citing which past project each claim came from
4. Add tools (a pricing calculator, calendar availability) and log a full trace of every run
5. Build a 40-case eval set with rubric-based LLM judging, spot-check it against your own grades, and compare two prompt versions with bootstrap intervals
6. Add guardrails against inventing clients or prices, and test them with adversarial inputs, including instructions hidden in a lead’s website
7. Package your tools as an MCP server and connect the agent to it, so the storyboard app and the video editor can reuse them
8. Deploy the agent behind an API with per-run cost and time limits, retries, human approval before anything is sent to a lead, and a dashboard of traces and eval scores
9. Decision-layer bake-off: qualify 300 leads three ways (a small fine-tuned classifier, a frontier LLM with structured output, and a System One decision model, either TypeSafe’s hosted Jev or an open-weight one such as Amazon’s Strands Decider 2B running on your Mac); compare accuracy with bootstrap intervals, calibration (Brier score and a reliability diagram), p95 latency and cost per 1,000 decisions

Put code in `code/` (tests as `test_*.py`, which run automatically on every push) and plots, tables and screenshots in `results/`. Anything with client or business data (leads, proposals, pricing, footage, transcripts, screenshots that show them) goes in `private/stages/track-c-llm-applications/` instead. That folder is a separate private repo and never appears here.

## Predict first

> Predict your retrieval recall@5 before you measure it.

My prediction, written before running anything:

- 

## Results

| Milestone | Predicted | Measured | Notes |
|---|---|---|---|
|  |  |  |  |

## Explain back

> Explain when to fine-tune, when to retrieve and when to just rewrite the prompt.

300 words, or a link to a 3-minute recording:


## Revisit

> Apply Stage 5’s judge-bias fixes to your eval. Does swapping answer order change the result?



## Readings

Tick a box when you finish a reading. Core readings get all three passes.

- [ ] [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) — Lewis et al., 2020 **(core)**
- [ ] [ReAct](https://arxiv.org/abs/2210.03629) — Yao et al., 2022 **(core)**
- [ ] [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic, 2024 **(core)**
- [ ] [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — Hamel Husain, 2024 **(core)**
- [ ] [Sentence-BERT](https://arxiv.org/abs/1908.10084) — Reimers & Gurevych, 2019
- [ ] [Lost in the Middle](https://arxiv.org/abs/2307.03172) — Liu et al., 2023
- [ ] [Toolformer](https://arxiv.org/abs/2302.04761) — Schick et al., 2023
- [ ] [Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — Greshake et al., 2023
- [ ] [Model Context Protocol docs](https://modelcontextprotocol.io) — MCP project, 2024
- [ ] [ModernBERT](https://arxiv.org/abs/2412.13663) — Warner et al., 2024
- [ ] [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) — Kwa et al., METR, 2025
- [ ] [Why We Need Continual Learning](https://a16z.com/why-we-need-continual-learning/) — Aubakirova & Bornstein, a16z, 2026

## On the job

**Roles that use this:** AI engineer, Forward-deployed engineer, Solutions engineer, AI product manager, Customer program manager for AI deployments

**At enterprise scale:**

- Deploying an internal knowledge assistant over company documents, with access controls per team
- Building agents that triage support tickets and draft replies, with a human approving each send
- Running evals and red-teaming before an enterprise customer goes live
- Leading a customer’s rollout program: success metrics, pilot groups, risk reviews and adoption reporting

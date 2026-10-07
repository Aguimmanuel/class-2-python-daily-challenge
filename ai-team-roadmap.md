# 🧭 AI Engineering Team Roadmap — 7 Pillars, Daily Teach-Backs

**Team:** 7 Junior AI Engineers
**Model:** Each person owns one pillar of the AI stack, dives deep, and teaches the group daily. Everyone becomes **T-shaped**: deep in one lane, conversant in all.
**Default duration:** 12 weeks (adjustable — see "Tuning the timeline" at the bottom)
**Output at the end:** one production-grade team product built from all 7 pillars, plus 7 specialists who can each teach their lane.

---

## 1. The Core Idea: 7 Pillars of an AI Product

Every real AI product is held up by the same seven pillars. If one collapses, the product collapses. Your job as a team is to make sure **no pillar is held by only one fragile pair of hands** — hence: one owner per pillar, daily teaching, everyone buttresses everyone.

```
                 ┌─────────────────────────────┐
                 │   ⑦ EVALUATION, SAFETY &    │  ← measures & protects everything
                 │      OBSERVABILITY          │
                 └──────────────┬──────────────┘
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   ┌─────────┐          ┌─────────┐           ┌─────────┐
   │ ⑤ AGENTS│          │ ⑥ INFERENCE│       │ ③ RAG & │
   │ & TOOLS │          │ DEPLOYMENT │       │  SEARCH │
   └────┬────┘          └────┬────┘           └────┬────┘
        └──────────┬───────────┘                     │
                   ▼                                 ▼
        ┌────────────────────┐            ┌────────────────────┐
        │ ④ FINE-TUNING &    │◄───────────│ ② DATA ENGINEERING │
        │    ALIGNMENT       │  (datasets)│   & PIPELINES      │
        └─────────┬──────────┘            └────────────────────┘
                  │ feeds
                  ▼
        ┌────────────────────┐
        │ ① LLM FOUNDATIONS & │  ← the bedrock everyone stands on
        │  PROMPTING         │
        └────────────────────┘
```

**The buttressing rule:** every pillar feeds at least two others. When you learn something in your lane, ask: *"Who else on this team needs this?"* That question is answered in the daily teach-back.

---

## 2. Role Assignments

Assign one person per pillar. If two people gravitate toward the same pillar, split it (e.g., split ⑥ into "serving/quantization" and "MLOps/CI-CD/monitoring").

| # | Pillar | Owner owns… | Owner teaches the group… | Feeds (buttresses) |
|---|--------|-------------|--------------------------|--------------------|
| ① | **LLM Foundations & Prompting** | How LLMs actually work: tokens, attention, context windows, decoding, prompting & context engineering | "Why the model said that" — the mental model everyone debugs with | All pillars (shared vocabulary) |
| ② | **Data Engineering & Pipelines** | ETL, data cleaning, dedup, annotation workflows, dataset versioning, the data flywheel | "Garbage in, garbage out" — how to build datasets that survive production | ③ RAG, ④ Fine-tuning, ⑦ Eval |
| ③ | **RAG & Search** | Embeddings, chunking strategies, vector DBs, hybrid search, reranking, retrieval evaluation | "How to give the model a memory" | ⑤ Agents, ⑦ Eval, ① prompting |
| ④ | **Fine-Tuning & Alignment** | LoRA/QLoRA, PEFT, dataset prep for tuning, RLHF/DPO basics, when NOT to fine-tune | "When prompting stops being enough" | ⑥ Deployment, ② Data, ⑦ Eval |
| ⑤ | **Agents & Orchestration** | Tool use, planning, memory, multi-agent patterns, frameworks (LangGraph, CrewAI, etc.), agent loops & failure modes | "From chatbots to coworkers" | ③ RAG, ⑥ Serving, ⑦ Eval |
| ⑥ | **Inference, Deployment & MLOps** | Serving (vLLM/TGI), quantization, batching, latency/cost optimization, CI/CD for ML, monitoring & rollback | "Getting it to production and keeping it there" | ⑤ Agents, ④ Models, ⑦ Observability |
| ⑦ | **Evaluation, Safety & Observability** | Evals (benchmarks, LLM-as-judge, human eval), red-teaming, guardrails, tracing (LangSmith/Phoenix), regression suites | "How do we know it works — and keeps working?" | Everything (the safety net) |

---

## 3. The Daily Ritual (the engine of the whole plan)

### 3.1 Daily Teach-Back Standup — 30 min, every morning

One person teaches per day, rotating so **each person teaches ~once per week**. Format, strictly timed:

| Time | Segment | What happens |
|------|---------|--------------|
| 0:00–0:05 | **Hook** | Teacher states the one idea from yesterday's deep dive: *"Yesterday I learned X. Here's the 30-second version."* |
| 0:05–0:15 | **Teach** | Teacher explains it at the whiteboard/screen using the **Feynman technique**: no jargon without definition, one diagram, one code snippet. |
| 0:15–0:20 | **Live demo** | Teacher shows it running (a notebook cell, a curl command, a trace screenshot). |
| 0:20–0:27 | **Q&A** | Group grills the teacher. If the teacher can't answer, it goes on the "parking lot" list — they research it and answer tomorrow. |
| 0:27–0:30 | **Buttress link** | Teacher states explicitly: *"This matters to [Pillar Y] because…"* — one sentence connecting their lane to someone else's. |

**Rules:**
- The teacher prepares the night before (30 min prep max — teaching forces clarity).
- Everyone else takes notes in their personal **"Buttress Log"** (see §5).
- No laptops open during the teach — full attention. Notes are handwritten or in a shared doc.
- If the teacher is absent/sick, the next person in rotation goes; never skip a day.

### 3.2 Daily Cross-Lane Sync — 15 min, end of day (or async in your team channel)

Each person answers three prompts, one line each:
1. **Built:** What did I finish in my lane today?
2. **Blocked:** What do I need from another lane?
3. **Buttress:** What did I learn today that another lane should know?

This is where pillars connect. Example: *"RAG person chunked the docs differently than Data person expected → flagged in sync → fixed same day."*

### 3.3 Weekly Rhythm

| Day | Ritual |
|-----|--------|
| Mon–Thu | Teach-back standup + deep work + cross-lane sync |
| **Friday** | **Demo Day (60–90 min):** each person shows 5 min of what they built this week in their lane. Group gives feedback. |
| Friday (last 30 min) | **Retro:** What did we learn? What's stuck? Adjust next week's plan. Update the shared roadmap doc. |

---

## 4. The 12-Week Phase Plan

### Phase 0 — Week 0: Shared Bedrock (everyone together)

**Goal:** Everyone speaks the same base language before specializing. No one dives into their pillar yet.

- All 7 build **one small app together**: a FastAPI + Streamlit chat app calling an LLM API (any provider).
- Crash course (self-paced, ~2 days): Python refresher, HTTP APIs, Git workflow, how to read a model card.
- Everyone reads: *Attention Is All You Need* (abstract + skim), the Lil'Log posts "Prompt Engineering" and "LLM Powered Autonomous Agents" (Eugene Yan / Lilian Weng).
- **Exit criteria:** everyone has deployed the shared app locally, can explain tokens/context window/temperature to a non-engineer.

### Phase 1 — Weeks 1–4: Foundations in Your Lane

**Goal:** Each pillar owner becomes *conversant-to-solid* in their lane and can teach it.

Each person, in their lane:
1. **Learn** (60% of time): follow the curriculum in §6 for their pillar, weeks 1–4.
2. **Build** (30%): one small hands-on project in their lane (listed in §6). Must run end-to-end, however ugly.
3. **Teach** (10%): prepare daily teach-backs; start writing their **Pillar Playbook** (see §5).

The team also starts the **capstone project** (§7): pick the product, write the one-page spec. No building yet — just design, with each pillar owner contributing their lane's requirements.

**Exit criteria (per person):** can pass the "Proficiency Ladder" rungs 1–3 for their pillar (§8).

### Phase 2 — Weeks 5–8: Depth + First Integration

**Goal:** Production-grade skills in the lane; pillars start connecting into the capstone.

- Each person builds their **Phase 2 project** (§6) — bigger, with tests, docs, and a demo.
- Capstone build begins: each pillar owner builds their component **against a shared interface contract** (API schemas agreed in week 4). Example: Data person delivers a versioned dataset → RAG person indexes it → Agent person consumes retrieval → Eval person scores the pipeline → Infra person serves it.
- Introduce **pair rotations**: each week, two pillar owners pair for one day on the seam between their lanes (e.g., RAG + Eval one day; Fine-tuning + Data another). This is where buttressing becomes muscle memory.
- **Exit criteria:** rungs 1–4 of the proficiency ladder; capstone has a working end-to-end demo (even if rough).

### Phase 3 — Weeks 9–12: Hardening, Integration & Ownership

**Goal:** The capstone becomes a real, deployed, evaluated product; each pillar owner is the team's go-to expert.

- Capstone goes to **production**: deployed, monitored, cost-tracked, with an eval suite and guardrails.
- Each pillar owner writes the **final Pillar Playbook** and records a **30-min "pillar masterclass"** video for the team (their teach-backs, condensed).
- **Chaos & failure drills** (run by ⑦ with help from ⑥): kill the vector DB, corrupt the index, push a bad model version — can the team detect and recover? (This is where ⑦ and ⑥ shine.)
- Final Demo Day: capstone presented as if to users/investors; each person presents their pillar's contribution and answers hard questions.
- **Exit criteria:** rung 5 of the proficiency ladder for each owner; capstone live with dashboards; every team member can teach a 15-min session on **any** pillar (not just their own).

---

## 5. The Artifacts That Make It Stick

Create a shared repo (GitHub/GitLab) with this structure:

```
ai-team-hub/
├── capstone/                  # the team product (everyone contributes)
├── pillar-playbooks/          # one folder per pillar
│   ├── 01-foundations/        # owner: Pillar ① person
│   ├── 02-data/
│   ├── 03-rag/
│   ├── 04-fine-tuning/
│   ├── 05-agents/
│   ├── 06-inference-mlops/
│   └── 07-eval-safety/
├── buttress-logs/             # one file per person, updated DAILY
│   ├── person-a.md
│   └── ...
├── teach-backs/               # slides/notes from every daily teach-back
├── parking-lot/               # unanswered questions, with owner + due date
└── weekly-retros/             # Friday retro notes
```

### The Pillar Playbook (each owner's living document)
Each pillar owner maintains a playbook that grows all 12 weeks:
1. **Concept map** — the 20 concepts of the pillar, one diagram.
2. **Cheat sheet** — commands, configs, gotchas (the stuff you always Google).
3. **Cookbook** — 5–10 copy-paste recipes ("How to chunk a PDF corpus," "How to LoRA a 7B model on one GPU").
4. **Failure gallery** — every bug you hit and the fix. This is the most valuable section.
5. **Teach-back archive** — your daily teaching notes.

### The Buttress Log (each person's daily file)
Every team member, every day, appends 3–5 bullet points:

```markdown
## 2026-10-08
- Learned: [one concept, in my own words]
- Built: [what I made/changed today]
- Buttress: [who else needs this, and why — name the pillar]
- Question for tomorrow's standup: [if any]
```

> The Buttress Log is the habit that turns 7 individual learners into one team. Review logs in the Friday retro — skim each other's.

---

## 6. Per-Pillar Curriculum & Projects

Each pillar: **Weeks 1–4 (learn + small project)** → **Weeks 5–8 (deepen + production project)** → **Weeks 9–12 (integrate into capstone + masterclass)**.

---

### ① LLM Foundations & Prompting
**Weeks 1–4 — Learn:** tokenization (tiktoken, BPE), context windows & KV cache, attention (intuition first, math second), decoding strategies (temperature, top-p, top-k, repetition penalty), system/user/assistant roles, prompt patterns (few-shot, chain-of-thought, structured output/JSON mode), context engineering (what to put in the window and why), common failure modes (hallucination, prompt injection, lost-in-the-middle).
**Project:** Build a "prompt lab" — a notebook comparing 5 prompt strategies on the same task, with a scoring rubric. Publish results.
**Weeks 5–8 — Learn:** function/tool calling internals, long-context techniques (RAG vs. long context tradeoffs — coordinate with ③), model comparison methodology, cost-per-token math, latency anatomy.
**Project:** Build a **model router**: given a task, automatically pick the cheapest model that passes a quality bar (mini-eval harness). This becomes a capstone component.
**Capstone role:** owns prompt templates, context assembly, and the model-routing layer.
**Resources:** Lil'Log (Lilian Weng) blog; "Prompt Engineering" guides from Anthropic/OpenAI; Chip Huyen's *AI Engineering* (ch. 1–3); tiktoken playground.

---

### ② Data Engineering & Pipelines
**Weeks 1–4 — Learn:** data sourcing & licensing, cleaning (dedup, PII scrubbing, quality filters), text normalization, train/val/test splits done right, dataset versioning (DVC/Hugging Face datasets), annotation basics (guidelines, inter-annotator agreement), synthetic data generation & its risks.
**Project:** Take one messy public dataset, clean it, version it, and write a data card documenting every decision.
**Weeks 5–8 — Learn:** ETL orchestration (Airflow/Prefect/Dagster — pick one), streaming vs. batch, building a **data flywheel** (production data → cleaned → retraining data), data contracts between teams, feature/data stores for AI (when you need more than a CSV).
**Project:** Build an automated pipeline: new raw data lands → cleaned → validated → versioned → notification. Runs on a schedule.
**Capstone role:** owns all capstone data: ingestion, cleaning, versioning, and the flywheel that improves the product from usage.
**Resources:** Chip Huyen's *Designing Machine Learning Systems* (data chapter); DVC docs; Hugging Face datasets course; "Data-centric AI" materials (Andrew Ng).

---

### ③ RAG & Search
**Weeks 1–4 — Learn:** embedding models (how they work, choosing one, dimensions vs. quality), vector DBs (index types: HNSW, IVF; when you don't need one), chunking strategies (fixed, semantic, recursive, parent-child), hybrid search (BM25 + vector), reranking (cross-encoders), retrieval metrics (recall@k, MRR, nDCG).
**Project:** Build a "chat with your docs" app over a real corpus (e.g., your team's own docs or a Wikipedia subset). Measure retrieval quality with 20 hand-labeled queries.
**Weeks 5–8 — Learn:** query transformation (HyDE, multi-query, decomposition), agentic/self-querying retrieval, GraphRAG (when structure matters), caching & cost control, multimodal retrieval (images + text — coordinate with ①), keeping indexes fresh (coordinate with ②).
**Project:** Production RAG service: versioned index, incremental updates, query analytics, latency < 500ms p95. Plug into the capstone.
**Capstone role:** owns the retrieval layer the agent (⑤) and the app talk to.
**Resources:** Pinecone/Weaviate/Qdrant learning centers; LangChain/LlamaIndex docs (concepts, not just API); "RAG" chapters of Chip Huyen's *AI Engineering*; BERGEN/eval papers as stretch reading.

---

### ④ Fine-Tuning & Alignment
**Weeks 1–4 — Learn:** when to fine-tune vs. prompt vs. RAG (the decision tree — teach this, it's gold), supervised fine-tuning (SFT) mechanics, LoRA/QLoRA/PEFT (rank, alpha, target modules — intuition), dataset formatting (instruction formats, chat templates), overfitting & early stopping, base vs. instruct models.
**Project:** Fine-tune a small open model (7–8B, QLoRA on a free GPU — Colab/Kaggle) to do one task well (e.g., extract structured data, or speak in your company's tone). Compare against a prompt-only baseline.
**Weeks 5–8 — Learn:** evaluation-driven tuning (build the eval first — coordinate with ⑦), DPO/RLHF at a conceptual depth (what alignment is, why it's hard, what "preference data" is), merging adapters, multi-task tuning, quantization-aware tuning, cost math (when fine-tuning beats paying per token).
**Project:** Tune a model for the capstone's core task; run a head-to-head: base vs. prompted vs. fine-tuned, scored by ⑦'s eval suite. Write the decision memo.
**Capstone role:** owns the custom model (if the team fine-tunes) and the base-vs-tuned decision.
**Resources:** Hugging Face PEFT/TRL docs; LoRA paper (Hu et al.); fast.ai; Sebastian Raschka's writings; Axolotl/Unsloth for easy tuning.

---

### ⑤ Agents & Orchestration
**Weeks 1–4 — Learn:** what an agent is (LLM + loop + tools + memory), tool calling patterns, ReAct (reason + act), planning (CoT planning, task decomposition), memory (short-term, long-term, episodic), reflection/self-critique, when NOT to use agents (teach this too).
**Project:** Build a single agent with 3 tools that completes a multi-step task (e.g., "research a topic and produce a cited report"). Log every step.
**Weeks 5–8 — Learn:** orchestration frameworks (LangGraph state machines, CrewAI roles — pick one deeply, know the other), multi-agent patterns (supervisor, swarm, hierarchical) and their failure modes, human-in-the-loop checkpoints, agent memory architectures (coordinate with ③), tool design (good tools are narrow, well-described, idempotent), guardrails for agent loops (coordinate with ⑦), cost/latency budgeting for agent loops.
**Project:** Multi-agent system for the capstone (e.g., researcher → writer → critic), with a LangGraph-style state machine, full trace logging, and a hard step/cost budget.
**Capstone role:** owns the agent layer that orchestrates tools, retrieval (③), and the model (①/④).
**Resources:** Lilian Weng's "LLM Powered Autonomous Agents"; LangGraph docs/tutorials; Anthropic's "Building Effective Agents"; ReAct and Reflexion papers.

---

### ⑥ Inference, Deployment & MLOps
**Weeks 1–4 — Learn:** serving fundamentals (batching, streaming, concurrency), open-model serving engines (vLLM, TGI, Ollama — deep dive one), quantization (GPTQ, AWQ, GGUF — quality vs. speed), GPU memory math (KV cache, model weights, activations), latency vs. throughput, cost modeling (tokens/sec/$, $/1M tokens), containerizing an AI app (Docker), API design for AI services.
**Project:** Serve an open model locally with vLLM; benchmark 3 quantization levels; write up latency/cost/quality tradeoffs.
**Weeks 5–8 — Learn:** production deployment (managed endpoints vs. self-hosted; when to use what), autoscaling & load testing, CI/CD for ML (test data, test prompts, canary deploys, rollback), monitoring (latency, error rates, token usage, drift — coordinate with ⑦), cost observability & budgets, caching strategies (semantic caching — coordinate with ③), A/B testing model versions.
**Project:** Deploy the capstone backend: containerized, autoscaled, monitored, with canary deploy and one-click rollback. Dashboard for latency/cost/errors.
**Capstone role:** owns everything between "code works on my laptop" and "users can hit it reliably."
**Resources:** vLLM docs & blog; Chip Huyen's *AI Engineering* (deployment chapters); "Machine Learning Systems" (CMU course, free); AWS/GCP/Azure ML deployment docs (pick your cloud).

---

### ⑦ Evaluation, Safety & Observability
**Weeks 1–4 — Learn:** why evals are the hardest part of AI (teach this early — it reframes the whole team), eval types (unit, integration, human, LLM-as-judge, benchmarks), building a golden dataset, eval metrics for generation (BLEU/ROUGE when they're OK, and when they're not), regression evals in CI, tracing & observability (LangSmith, Phoenix, Helicone — pick one), logging the right things.
**Project:** Build an eval suite for the Phase 0 shared chat app: 50 test cases, automated scoring, a simple report. Run it on every change.
**Weeks 5–8 — Learn:** red-teaming & safety (prompt injection, jailbreaks, PII leakage, bias — attack your own capstone), guardrails (input/output filters, constitutional approaches), eval design for agents (did it use the right tool? did it finish? — coordinate with ⑤), data flywheel for evals (production failures → new test cases — coordinate with ②), observability dashboards, alerting (when does a human get paged?).
**Project:** Full eval + safety harness for the capstone: automated eval gate in CI, tracing on every request, a red-team report with fixes, and a live dashboard.
**Capstone role:** owns the trust layer: the eval gate that blocks bad deploys, the safety guardrails, and the dashboards everyone watches.
**Resources:** Hamel Husain's "Your AI Product Needs Evals" (blog/course); LangSmith/Phoenix docs; OWASP Top 10 for LLMs; Chip Huyen's *AI Engineering* (eval chapters); Anthropic's red-teaming write-ups.

---

## 7. The Capstone: One Product, Seven Pillars

Pick **one real product** in Week 0. It should be small enough to finish in 12 weeks but real enough to matter. Strong candidates:

- **An internal AI assistant for a real workflow** (e.g., "answer questions from our company's documents, draft documents, and file tickets") — exercises every pillar.
- **A domain-specific research agent** (e.g., for legal/medical/agritech — relevant to Port Harcourt: oil & gas, logistics, finance docs) — RAG + agents + eval heavy.
- **A fine-tuned specialist model + API** (e.g., a model that speaks Nigerian Pidgin/English customer-support style) — fine-tuning + serving + eval heavy.

**Why the capstone matters:** the pillars are not abstract. The capstone is where buttressing becomes visible — when ③'s retrieval feeds ⑤'s agent which is scored by ⑦'s evals which is served by ⑥'s infra which is trained on ②'s data using ④'s model with ①'s prompts. If one pillar is weak, the product shows it. That pressure is the point.

**Interface contracts (agree these in Week 4):**
- ② → ③/④: dataset schema + versioning contract
- ③ → ⑤: retrieval API (query in, ranked chunks out)
- ⑤ → ①/④: model call contract (prompt format, model version, budget)
- ①/④/⑤ → ⑥: service API + latency/cost SLOs
- everything → ⑦: eval gate contract (what must pass before deploy)

---

## 8. Proficiency Ladder (how you know someone "owns" a pillar)

Each person self-assesses weekly and the group calibrates in Friday retro. **A pillar owner is "proficient" at rung 5.**

| Rung | Level | Evidence |
|------|-------|----------|
| 1 | **Can explain** | Teaches one concept from their lane clearly in the daily standup |
| 2 | **Can build** | Ships their weekly project, working end-to-end |
| 3 | **Can debug** | Fixes a broken thing in their lane without hand-holding (logs the fix in the Failure Gallery) |
| 4 | **Can integrate** | Their component works inside the capstone with the agreed contract |
| 5 | **Can lead** | Owns a capstone subsystem, answers the team's hardest questions in their lane, delivers their 30-min masterclass |

**Bonus rung for everyone (all 12 weeks):** *Can teach any pillar at rung 1.* The daily teach-backs and buttress logs are designed to get the whole team here — that's what makes you a team of 7 specialists instead of 7 people who each know one thing.

---

## 9. Operating Rules (print these, pin them)

1. **No skipped teach-backs.** The rotation is sacred. If you can't teach, you prep extra hard.
2. **Teach to be understood, not to impress.** If the group is lost, the teacher failed, not the group. Re-teach differently.
3. **Every claim in a teach-back gets a demo or a source.** No hand-waving.
4. **The Buttress Log is written daily.** Five minutes, non-negotiable.
5. **Parking-lot questions get owners and deadlines.** Unanswered questions are debt.
6. **Cross-lane seams are everyone's job.** The person on each side of a seam owns it jointly.
7. **Measure everything in the capstone.** If ⑦ can't measure it, it doesn't count as done.
8. **Failure Gallery entries are celebrated in retro.** The best retro moment is "here's what broke and what we learned."
9. **One tool per lane, mastered.** Don't adopt a new framework mid-phase. Depth beats novelty.
10. **Rest is part of the plan.** Sustainable pace over 12 weeks beats a heroic 3 weeks and burnout.

---

## 10. Suggested Weekly Time Budget (per person)

| Activity | Hours/week |
|----------|-----------|
| Deep work in own lane (learn + build) | 20–24 |
| Daily teach-back (attend) + prep (own day) | 3–4 |
| Cross-lane sync + pair rotation | 2–3 |
| Buttress log + playbook writing | 1–2 |
| Friday demo + retro | 2 |
| **Total** | **~30–35 hrs** |

---

## 11. Tuning the Timeline

- **6-week sprint version:** cut Phase 2 projects in half; capstone is a demo, not production; drop pair rotations to biweekly.
- **6-month version:** add a second capstone; add interview prep / portfolio polish in months 4–6; each person gives an external talk or writes a public blog post on their pillar; consider contributing to an open-source AI tool in your lane.
- **If someone leaves / team changes:** their Pillar Playbook is the handover document. That's why it exists. A new member reads the playbook + buttress logs + teach-back archive and is productive in days, not months.

---

## 12. Week 0 & Week 1 — Start Here

**This week (Week 0):**
1. Hold a 90-min kickoff: assign pillars (let people pick; resolve conflicts by consensus or coin flip).
2. Set up the `ai-team-hub` repo with the folder structure in §5.
3. Everyone starts the Phase 0 shared app (chat app over an LLM API).
4. Schedule the teach-back rotation for the next 4 weeks (write it down — same time daily).
5. Pick the capstone product and write the one-page spec.

**Week 1, day 1:** First teach-back. Pillar ① owner teaches "how a token becomes a prediction" in 10 minutes. The habit starts now.

---

## 13. Quick Reference: One-Line Summary for Each Pillar

> Teach these to each other until they're boring:

1. **① Foundations:** "A model predicts tokens; everything else is engineering around that."
2. **② Data:** "The model is only as good as the data flywheel feeding it."
3. **③ RAG:** "Retrieval is how you give a small context window a big memory."
4. **④ Fine-tuning:** "Teach the model the shape of your task; prompt it for everything else."
5. **⑤ Agents:** "An agent is a loop: think, act, observe — until done or out of budget."
6. **⑥ Inference/MLOps:** "Production is a latency, cost, and reliability problem."
7. **⑦ Eval/Safety:** "If you can't measure it and can't break it, you don't have a product."

---

*Good luck, team. Twelve weeks from now you won't be 7 juniors — you'll be 7 specialists who can each stand under the whole roof.*

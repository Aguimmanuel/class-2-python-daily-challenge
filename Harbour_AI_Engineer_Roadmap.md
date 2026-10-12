# HARBOUR: Project-Driven Roadmap to Job-Ready AI Engineers

**Team:** 10 junior AI engineers
**Format:** Build one real system, component by component. Each component is a subtopic. Each subtopic is split into 10 chunks, one per member. Members teach their chunk, the team integrates it, and then the project moves on.
**Capstone:** **HARBOUR**, an AI operations copilot for a small business in Port Harcourt (a distributor, pharmacy chain, school, or clinic). It answers customers from the business's own documents, looks up orders and stock, drafts replies, escalates to humans, and runs in production with evals, guardrails, and monitoring.

> The Port Harcourt SME is a working example. If you already have a partner organisation or a domain you prefer, the phases stay the same and only the data changes.

---

## 1. How the Team Works

### 1.1 The learning cycle (every subtopic)

Each subtopic runs in two meeting days:

| Step | Meeting day | What happens | Output |
|---|---|---|---|
| **1. Chunk prep** | Self-study between meetings | Each member masters their own chunk from the brief, using the listed resources and a small experiment | Chunk brief + runnable demo |
| **2. Teach-back** | Day A (morning block) | Each member teaches their chunk: 15 min talk, 5 min Q&A, 5 min "trap question" from a peer | 10 teach-backs per subtopic |
| **3. Integrate & build** | Day B (build block) | Pairs wire the 10 chunks into the project component, then run a cold-call drill | Working component merged to `main` |
| **4. Interview-proof** | Day B (end of day) | Random members explain any chunk, including ones they did not teach | Pass / revisit list |

**Principle:** you are the deepest person on your chunk, and you are still expected to explain the others. Interviewers test depth and breadth.

### 1.2 Chunk ownership and rotation

- Every subtopic has **exactly 10 chunks**, and each member owns **exactly one** per subtopic.
- Assign chunks by lot at the start of each subtopic.
- Do not give the same member the same kind of chunk twice in a row. Everyone should eventually own every kind of work (data, code, evaluation, UI, writing).
- **Pair buddies:** each chunk owner is paired with the member whose work depends on theirs (e.g., the chunking owner pairs with the embedding owner).

### 1.3 Chunk brief (what each member submits)

Every member writes a one-page brief for their chunk containing:

1. **The concept in one paragraph**, plain language, no jargon the audience has not met.
2. **The core trade-off** and when you would not use it.
3. **A runnable demo** (notebook or script) that shows the concept on the Harbour corpus.
4. **Three interview questions** on your chunk, with model answers.
5. **One failure mode** you observed and how you would detect it in production.

### 1.4 Meeting-day template (9 hours, Mon / Wed / Fri)

| Time | Block | Purpose |
|---|---|---|
| 09:00–09:30 | **Computational thinking warm-up** | One problem in pairs, then a 5-min debrief |
| 09:30–10:00 | Stand-up and chunk briefs | Blockers, what was learned since the last session |
| 10:00–12:30 | **Teach-back block** (Day A) or **Deep build** (Day B) | Core learning |
| 12:30–13:30 | Lunch | |
| 13:30–16:00 | **Integrate & build** (pairs on the project) | Wire chunks together, merge code, run tests |
| 16:00–16:30 | **Cold-call drill** | Random members explain others' chunks, 3 min each |
| 16:30–17:30 | **From-scratch lab** | Rebuild a core concept without a framework (see §5) |
| 17:30–18:00 | Retro and learning log | Each member writes three lines: what I learned, what confused me, what I'll explain differently |

### 1.5 Self-study expectations

Because the team meets three days a week, each member should expect roughly **3–4 hours of self-study per week** for chunk prep and reading. The chunk brief tells you exactly what to do, so nobody has to guess.

### 1.6 Phase gate (Definition of Done)

A phase is complete only when all of the following are true:

- [ ] The project component runs end-to-end on a fresh clone (one command to start it).
- [ ] Tests and CI are green. Evals are included where the phase has them.
- [ ] Every member passes a **20-minute solo cold-call** on their own chunk.
- [ ] Every member completes the **from-scratch challenge** for that phase.
- [ ] An **Architecture Decision Record (ADR)** is written for each major choice (chunk size, index type, model choice, etc.).
- [ ] A **live demo** is given to the whole team, with one question each from a non-owner.

### 1.7 Roles on the capstone

The original roadmap's capstone ownership is kept, but each role is now shared by a squad of 2–3 members:

| Capstone layer | Squad | Owns |
|---|---|---|
| Model & prompts | 2–3 members | Prompt templates, context assembly, model-routing layer |
| Data | 2 members | Ingestion, cleaning, versioning, the data flywheel |
| Retrieval (RAG) | 2–3 members | Retrieval layer that the agent and app call |
| Agents | 2 members | Orchestration, tools, memory, budgets |
| Custom model | 1–2 members | Fine-tuned model and the base-vs-tuned memo |
| Platform & trust | 2 members | Eval gate, guardrails, deployment, dashboards |
| Frontend | 1–2 members | Chat UI and agent trace viewer |

Squads rotate between phases so that everyone eventually owns a layer end-to-end.

---

## 2. Roadmap at a Glance

Durations are in **meeting days** (3 per week, Mon/Wed/Fri). Calendar weeks are approximate. The first week has only **2 meeting days (Wed 14 and Fri 16 October 2026)**, and those count toward Phase 0.

| Phase | Name | Project | Meeting days | Cumulative | ≈ Weeks |
|---|---|---|---|---|---|
| **0** | Engineering Foundations & Computational Thinking | Harbour Core API | 12 | 1–12 | 4 |
| **1** | LLM Foundations, Prompting & Model Routing | Prompt Lab & Model Router | 12 | 13–24 | 4 |
| **2** | Data Engineering & Pipelines | Harbour Data Factory | 12 | 25–36 | 4 |
| **3** | RAG & Search | Harbour Knowledge (RAG service) | 15 | 37–51 | 5 |
| **4** | Agents, Tools & Orchestration | Harbour Agent Crew + chat UI | 15 | 52–66 | 5 |
| **5** | Evaluation, Safety & Observability | Harbour Trust Layer | 12 | 67–78 | 4 |
| **6** | Fine-Tuning & Alignment | Harbour Tuned Extractor | 12 | 79–90 | 4 |
| **7** | Inference, Deployment & Distributed Systems | Harbour in Production | 12 | 91–102 | 4 |
| **8** | Interview & Job-Readiness Sprint | Harbour Launch + portfolio | 9 | 103–111 | 3 |

**Total:** 111 meeting days, about 37 weeks. Phases can extend by 3 days (one week) if the team needs it. Extensions are decided at the phase gate, not mid-phase.

**Why this order?**
- **Engineering first** (Phase 0): the capstone is a backend service. You cannot build AI on top of a system you cannot test, containerise, or query.
- **LLM before data** (Phase 1 → 2): you need to know what the model needs before you design what the data should look like.
- **Data before RAG** (Phase 2 → 3): RAG is only as good as its corpus, and the pipeline produces the corpus.
- **RAG before agents** (Phase 3 → 4): the agent's most important tool is retrieval.
- **Trust layer before fine-tuning** (Phase 5 → 6): you cannot tell if a fine-tune helped without an eval suite.
- **Deployment last** (Phase 7): by then there is something worth deploying.

---

## 3. Stack Coverage Matrix

Every item on the team stack is taught inside a project, not in isolation.

| # | Stack item | Primary phase | Reinforced in |
|---|---|---|---|
| 1 | Python problem solving | **P0** (algorithms, idioms) | Daily warm-ups, P8 (DSA drills) |
| 2 | SQL / PostgreSQL | **P0** (schema, queries, indexes) | P2 (metadata, lineage), P3 (pgvector), P4 (agent checkpoints), P7 |
| 3 | FastAPI / backend | **P0** (APIs, auth, layering) | P1 (router service), P3 (RAG API), P4 (agent API), P7 |
| 4 | LLM APIs + structured outputs | **P1** (schemas, tool calling) | P4 (tools), P5 (judges), P6 (training data) |
| 5 | RAG / retrieval | **P3** (embeddings, chunking, hybrid search) | P4 (retrieval tool), P5 (retrieval evals) |
| 6 | Testing + evaluation | **P0** (pytest), **P1** (mini-eval) | P3 (retrieval metrics), P5 (eval suite and CI gate), P6 (head-to-head) |
| 7 | Docker | **P0** (Compose, images) | P4 (multi-service), P7 (production images) |
| 8 | CI/CD | **P0** (GitHub Actions) | P5 (eval gate), P7 (canary, rollback) |
| 9 | Observability | **P1** (logs, cost, traces) | P4 (agent traces), P5 (dashboards, alerts), P7 (SLOs) |
| 10 | TypeScript / React | **P4** (chat UI, trace viewer) | P5 (eval dashboard) |
| 11 | Agents / LangGraph | **P4** (state machines, multi-agent) | P5 (agent evals), P8 (system design) |
| 12 | Kubernetes / distributed systems | **P7** (K8s, queues, retries) | P2 (queues, orchestration), P3 (index serving), P8 (system design) |

---

## 4. Computational Thinking Track

Computational thinking (CT) is trained every morning and assessed in every phase. It has four pillars. Each phase focuses on one pillar, and the warm-up problems follow the same focus.

| Pillar | What it means | Where it's trained |
|---|---|---|
| **Decomposition** | Break a messy problem into parts that can be solved independently | P0 (API layers), P3 (RAG pipeline stages), P4 (agent graph) |
| **Pattern recognition** | Spot the same problem shape in different clothes (two-pointer, BFS, retrieval ranking) | P0 (algorithms), P2 (duplicate detection), P8 (DSA patterns) |
| **Abstraction** | Hide detail behind a stable interface (provider adapter, retriever interface, tool schema) | P1 (provider layer), P3 (retriever interface), P7 (service boundaries) |
| **Algorithm design** | State the steps precisely, reason about correctness and cost (Big-O, latency budgets, token budgets) | P0 (complexity), P3 (ANN trade-offs), P7 (capacity planning) |

**Daily warm-up rules:**
- One problem per day, solved in pairs, with a written plan before any code.
- Each person states the **invariant**, the **complexity**, and **one edge case** before they run the code.
- Fridays: a 30-minute "explain the solution to a non-programmer" round.

**Assessment:** every phase gate includes one CT question that must be solved on a whiteboard or in a shared doc, with no IDE.

---

# 5. Phases in Detail

Each phase lists its project, the stack items it covers, the CT focus, its subtopics (each split into 10 chunks), the from-scratch challenge, interview translations, and resources.

---

## PHASE 0: Engineering Foundations & Computational Thinking
**Meeting days:** 12 (days 1–12). **Starts:** Wed 14 Oct 2026 (this week).
**Project: Harbour Core API.** A production-style FastAPI and PostgreSQL service for orders and support tickets: authenticated, migrated, tested, containerised, and built by CI on every push. This is the backend the rest of the capstone will plug into.
**Stack covered:** 1, 2, 3, 6 (basics), 7 (basics), 8 (basics).
**CT focus:** Decomposition and algorithm design.
**Capstone role:** Core backend, database schema, CI skeleton.

### Subtopic 0.1 — Python Problem Solving & Complexity
1. **Hashing and frequency counting:** two-sum, anagram grouping, `Counter` and `defaultdict`.
2. **Two pointers:** sorted arrays, palindromes, container-with-most-water logic.
3. **Sliding window:** longest substring with constraints; fixed vs variable windows.
4. **Binary search on sorted space:** search-in-rotated, first/last occurrence, "binary search on the answer."
5. **Stacks, queues, monotonic structures:** valid parentheses, next-greater element, sliding-window max.
6. **Recursion, trees, and traversal:** DFS, BFS, depth and level-order problems.
7. **Heaps and top-k:** `heapq`, top-k frequent, merging k sorted lists.
8. **Dynamic programming:** 1D and 2D tables, memoisation vs tabulation, coin change.
9. **Graphs:** adjacency lists, BFS shortest path, topological sort, cycle detection.
10. **Big-O in practice:** measuring with `timeit` and `cProfile`; when constants matter.

### Subtopic 0.2 — SQL & PostgreSQL
1. **SELECT fundamentals:** filtering, sorting, `NULL` semantics, `COALESCE`.
2. **JOINs:** inner, left, anti-join, self-join on a real Harbour schema.
3. **Aggregation and windows:** `GROUP BY`, `HAVING`, `ROW_NUMBER`, running totals.
4. **Schema design:** primary and foreign keys, normalisation, `CHECK` and `UNIQUE` constraints.
5. **Indexes:** B-tree basics, `EXPLAIN ANALYZE`, when an index hurts writes.
6. **Transactions and isolation:** ACID, `BEGIN`/`COMMIT`, lost updates, row locks.
7. **JSONB and full-text basics:** storing semi-structured payloads, `tsvector` intro.
8. **Migrations with Alembic:** versioned schema changes, rollback, zero-downtime habits.
9. **Connection pooling and the N+1 problem:** why a loop of queries kills latency.
10. **Recursive CTEs:** org charts and category trees; reading a query plan line by line.

### Subtopic 0.3 — FastAPI & Backend Engineering
1. **HTTP and REST:** methods, status codes, idempotency, safe vs unsafe verbs.
2. **Pydantic models:** request and response schemas, validation errors, `model_config`.
3. **Layering:** router → service → repository; dependency injection with `Depends`.
4. **Async vs sync:** the event loop, `async def` pitfalls, when to use threads.
5. **SQLAlchemy 2.0 ORM:** sessions, unit of work, lazy vs eager loading.
6. **Authentication:** API keys, OAuth2 password flow, JWT lifecycle, password hashing.
7. **Pagination, filtering, and rate limiting basics:** cursor vs offset pagination.
8. **Background tasks and idempotency keys:** safe retries for `POST` endpoints.
9. **Configuration and logging:** 12-factor config, environment separation, structured logs.
10. **API contracts:** OpenAPI generation, versioning strategy, breaking-change rules.

### Subtopic 0.4 — Testing, Docker & CI Basics
1. **Unit tests with pytest:** fixtures, `parametrize`, arranging test data.
2. **Integration tests against real Postgres:** `testcontainers` or a Compose test service.
3. **Mocking boundaries:** fakes vs mocks; where to draw the line.
4. **Meaningful coverage:** what to measure, what not to chase.
5. **Docker images:** layers, caching, multi-stage builds, slim base images.
6. **Docker Compose:** app + database, health checks, named volumes.
7. **Git workflow:** branches, pull requests, review checklist, conventional commits.
8. **GitHub Actions:** lint → type-check → test → build pipeline on every push.
9. **Linting and typing:** `ruff`, `mypy` or `pyright`, what strict typing buys you.
10. **Dependencies and packaging:** `pyproject.toml`, `uv`, lockfiles, reproducible installs.

**From-scratch challenge:** Implement a generic LRU cache with O(1) get and put using a dict and a doubly linked list. Then write its tests.

**Interview translation:** "Reverse a linked list" is a warm-up, but the real question is "what is the complexity of your solution, and what breaks at 10 million rows?"

**Resources:** Python docs and "Python Data Structures" (official), *PostgreSQL Exercises*, FastAPI docs (tutorial and advanced user guide), SQLAlchemy 2.0 tutorial, pytest docs, Docker "Getting started," GitHub Actions quickstart.

---

## PHASE 1: LLM Foundations, Prompting & Model Routing
**Meeting days:** 12 (days 13–24).
**Project: Prompt Lab & Model Router.** Compare five prompt strategies on the same Harbour task (classify a customer message and draft a reply), with a written scoring rubric and a published report. Then build a **model router** that picks the cheapest model passing a quality bar on each task, backed by a mini-eval harness. This becomes the routing layer of the capstone.
**Stack covered:** 4 (LLM APIs, structured outputs), 6 (mini-eval), 9 (logs, cost, traces), 3 (router API).
**CT focus:** Abstraction. A prompt is a function with inputs, a contract, and a failure mode.
**Capstone role:** Prompt templates, context assembly, routing layer.

### Subtopic 1.1 — How LLMs Work (Under the Hood)
1. **Tokenization:** BPE from scratch on a toy corpus; `tiktoken` playground; why counting tokens matters.
2. **Context windows and token budgeting:** system + history + retrieved context + output reserve.
3. **Attention intuition:** queries, keys, and values; a NumPy toy with four tokens.
4. **KV cache:** why generation is memory-bound; how long context costs grow.
5. **Decoding strategies:** temperature, top-k, top-p, repetition penalty; implement a sampler.
6. **Roles and chat templates:** system, user, assistant, tool; what the template does to your prompt.
7. **Latency anatomy:** time to first token, tokens per second, streaming, network overhead.
8. **Cost math:** price per million input and output tokens, cached-input discounts, batch pricing.
9. **Base vs instruct models:** what instruction tuning changed, conceptually.
10. **Model selection methodology:** capability, cost, latency, context size, and data-residency and privacy constraints.

### Subtopic 1.2 — Prompting Patterns & Context Engineering
1. **Zero-shot vs few-shot:** how to choose and order examples; example leakage.
2. **Chain-of-thought:** when reasoning helps, when it adds cost without accuracy.
3. **Instruction hierarchy:** system prompt design, constraints vs preferences.
4. **Context engineering:** what goes into the window, in what order; lost-in-the-middle effects.
5. **Prompt templates as code:** versioned files, variables, rendering, and tests.
6. **Self-consistency and verification prompts:** sampling several answers and voting; a checker pass.
7. **Compression and memory:** summarising conversation history without losing facts.
8. **Prompt injection:** direct and indirect injection; a demo, then two defences.
9. **Hallucination:** detection signals, grounding instructions, designing for "I don't know."
10. **Controlled prompt comparisons:** same inputs, same seeds where possible, one variable at a time.

### Subtopic 1.3 — Structured Outputs, Tool Calling & the API Layer
1. **JSON mode vs schema-constrained decoding:** what each guarantees and what it does not.
2. **Pydantic as the contract:** schema design, validation errors, retry-with-feedback loops.
3. **Function and tool calling:** schema definition, model proposes arguments, your code executes.
4. **Parallel tool calls and error results:** returning errors the model can act on.
5. **Streaming structured output:** handling partial JSON safely in the client.
6. **Provider abstraction:** one internal interface over two providers, plus an open model via Ollama.
7. **Timeouts, retries, and backoff:** which errors are retryable; jitter; idempotency.
8. **Response caching:** exact-match cache keyed on model, prompt version, and input hash.
9. **Token and cost logging:** a middleware that records tokens, latency, and cost per call.
10. **Secrets and testing:** keeping keys out of code; recorded LLM responses for deterministic tests.

### Subtopic 1.4 — Model Router & Mini-Eval
1. **Task taxonomy:** classify requests by difficulty and risk (simple lookup, drafting, policy-sensitive).
2. **Golden dataset for routing:** 50 labelled cases with difficulty tags and expected outputs.
3. **Scoring rubric:** exact match, rubric-based scoring, and when a human must score.
4. **LLM-as-judge basics:** bias types (verbosity, position), and a calibration check against humans.
5. **Quality bar selection:** choosing a threshold from the data, not from intuition.
6. **Cascade routing:** try the cheap model first, escalate on low confidence or failed validation.
7. **Router classifier:** heuristic rules vs a logistic-regression router on simple features.
8. **Cost-quality frontier:** plotting Pareto points and picking the operating point.
9. **Statistical confidence:** bootstrap confidence intervals on pass rates; "is this difference real?"
10. **Router as a service:** FastAPI endpoint, tests, and per-request decision logs.

**From-scratch challenge:** Implement BPE merge training and a top-p sampler in pure Python, with no libraries.

**Interview translation:** "Design an LLM pipeline that cuts cost by 60% without losing quality." The answer is routing plus a measured quality bar.

**Resources:** Lilian Weng's blog (Lil'Log), Anthropic and OpenAI prompt engineering guides, Chip Huyen's *AI Engineering* (chapters 1–3), `tiktoken` documentation, Karpathy's "Let's build the GPT Tokenizer" video.

---

## PHASE 2: Data Engineering & Pipelines
**Meeting days:** 12 (days 25–36).
**Project: Harbour Data Factory.** An automated, scheduled pipeline. New raw data lands (policy PDFs, product sheets, ticket exports, and a messy public customer-support dataset) → it is cleaned → validated → versioned → and the team is notified. A data card documents every decision. The pipeline also captures production feedback into a review queue, which is the start of the **data flywheel**.
**Stack covered:** 2 (metadata and lineage in Postgres), 12 (queues and orchestration), 6 (data tests), 8 (data CI).
**CT focus:** Pattern recognition. Duplicates, label noise, leakage, and drift are all patterns that can be detected automatically.
**Capstone role:** Ingestion, cleaning, versioning, and the flywheel.

### Subtopic 2.1 — Sourcing, Licensing & Annotation
1. **Dataset licensing:** open licences, commercial-use terms, attribution, and what "public" does not mean.
2. **Privacy and personal data:** the Nigeria Data Protection Act 2023, PII categories, and consent basics.
3. **Annotation guidelines:** writing rules with examples and edge cases.
4. **Inter-annotator agreement:** Cohen's kappa; what a low score tells you.
5. **Labelling workflow:** gold items, adjudication, and reviewer assignment.
6. **Sampling and class balance:** stratified sampling; over- and under-sampling trade-offs.
7. **Synthetic data generation:** using an LLM to create examples; prompts for diversity.
8. **Synthetic data risks and checks:** leakage from the generator, duplicates, model collapse, and checking against real data.
9. **Data cards and datasheets:** what a reader must know to reuse the dataset safely.
10. **Bias audit of a dataset:** coverage across languages, dialects (including Nigerian Pidgin), names, and regions.

### Subtopic 2.2 — Cleaning & Quality
1. **Text normalisation:** Unicode NFKC, whitespace, casing, and handling mixed English and Pidgin text.
2. **Exact deduplication:** content hashing and what counts as "the same" document.
3. **Near-duplicate detection:** MinHash and LSH; choosing the Jaccard threshold.
4. **PII detection and scrubbing:** regex rules vs Microsoft Presidio; false positives and negatives.
5. **Language detection and filtering:** identifying the language of each record and handling mixed records.
6. **Quality heuristics:** length bounds, repetition, boilerplate and navigation-text removal.
7. **Parsing documents:** PDF, HTML, and DOCX to clean text; tables and headers.
8. **Outliers and label noise:** finding suspicious labels with disagreement and confidence signals.
9. **Cleaning as tested code:** deterministic transforms, property tests, and golden files.
10. **Before-and-after metrics:** a cleaning report showing counts removed and why.

### Subtopic 2.3 — Splits, Versioning & Reproducibility
1. **Splits:** random, stratified, group-based, and time-based; picking the right one.
2. **Leakage:** duplicates across splits, and future information leaking into training.
3. **DVC:** tracking data, remotes, and pipeline stages in `dvc.yaml`.
4. **Hugging Face Datasets:** versioned datasets, dataset cards, and loading by revision.
5. **Lineage:** content hashes, provenance records, and "which data trained this model?"
6. **Schema evolution:** adding and renaming fields without breaking consumers.
7. **Data contracts:** producer and consumer agreements, SLAs, breaking-change notice.
8. **Data validation:** Pandera or Great Expectations suites that fail the run on bad data.
9. **Reproducibility:** seeds, locked environments, deterministic output ordering.
10. **When a CSV is not enough:** feature and data stores, and where pgvector fits later.

### Subtopic 2.4 — Orchestration, Streaming & the Flywheel
1. **Orchestration concepts:** DAGs, assets, and tasks; Dagster (chosen) vs Airflow (know for interviews).
2. **Scheduling and triggers:** cron schedules, sensors that fire when a file lands.
3. **Idempotent, retryable tasks:** running twice must not duplicate data; backfills.
4. **Batch vs streaming:** latency, cost, and complexity; a Kafka or Redpanda overview.
5. **Queue-based ingestion:** a Postgres-backed job queue (`SKIP LOCKED`) for the team's scale.
6. **Notifications:** Slack or email on success and failure, with run links.
7. **Pipeline observability:** run durations, row counts, failure rates.
8. **The data flywheel:** production logs → review queue → curated training and eval data.
9. **Human feedback capture:** thumbs up and down, corrections, and consent-aware storage.
10. **Testing pipelines:** fixtures, golden outputs, and CI jobs that run on sample data.

**From-scratch challenge:** Implement MinHash and LSH deduplication in pure Python. Then write a tiny DAG runner that executes tasks in topological order and retries failures.

**Interview translation:** "Deduplicate 100 million rows" and "your nightly job ran twice, what happens?" Both are idempotency and pattern questions.

**Resources:** Chip Huyen's *Designing Machine Learning Systems* (data chapters), DVC documentation, Hugging Face Datasets course, Andrew Ng's data-centric AI materials, Dagster tutorials, Microsoft Presidio documentation.

---

## PHASE 3: RAG & Search
**Meeting days:** 15 (days 37–51). Six subtopics, so this is the largest phase.
**Project: Harbour Knowledge.** A production RAG service over the Harbour corpus (policies, product sheets, FAQs, and a Wikipedia subset for scale tests). Requirements:
- Versioned index in **pgvector**, with incremental updates and blue/green index swaps.
- Hybrid search (BM25 + vector) with a cross-encoder reranker.
- Query analytics and ACL-aware retrieval (users see only the documents they are allowed to see).
- **p95 retrieval latency under 500 ms**, measured with a load test.
- Evaluated on **100 hand-labelled queries** (start with 20, then expand).
- *Stretch:* multimodal retrieval over product images.

**Stack covered:** 5 (RAG), 2 (pgvector), 3 (RAG API), 6 (retrieval metrics), 9 (retrieval traces).
**CT focus:** Algorithm design. Recall, latency, and memory trade-offs of approximate nearest-neighbour search.
**Capstone role:** The retrieval layer that the agent and the app talk to.

### Subtopic 3.1 — Embeddings & Vector Search Fundamentals
1. **How embedding models are trained:** contrastive learning, positive and negative pairs.
2. **Choosing an embedding model:** public leaderboards (MTEB), dimensions vs quality, cost and latency.
3. **Similarity metrics:** cosine, dot product, L2; when normalisation makes them equivalent.
4. **Exact (brute-force) search:** O(n·d) cost and when it is good enough.
5. **HNSW:** the layered graph intuition; `M`, `efConstruction`, and `efSearch` trade-offs.
6. **IVF and product quantisation:** clustering, `nprobe`, and memory savings.
7. **pgvector in practice:** `ivfflat` vs `hnsw` indexes, distance operators, query planning.
8. **Dedicated vector databases:** Qdrant, Weaviate, Pinecone; when the extra service pays for itself.
9. **When you do not need a vector database:** SQL full-text search, BM25, or a small in-memory index.
10. **Benchmarking ANN:** recall-vs-latency curves; never trust one number.

### Subtopic 3.2 — Chunking & Document Processing
1. **Fixed-size chunking:** token-accurate windows with overlap; the boundary-loss problem.
2. **Recursive splitting:** separators in order (headings, paragraphs, sentences).
3. **Structure-aware chunking:** headings, HTML sections, DOCX styles.
4. **Semantic chunking:** breakpoints where embedding similarity drops.
5. **Parent-child (small-to-big) retrieval:** index small chunks, return their parent section.
6. **Tables and lists:** keeping rows intact; row-to-text conversion for embedding.
7. **Contextual headers:** prefixing each chunk with document title and section path.
8. **Contextual retrieval:** LLM-written context for each chunk, and its cost at scale.
9. **Chunk-size sweeps:** a grid of sizes with boundary-loss and retrieval metrics.
10. **Chunk metadata schema:** `doc_id`, version, source URL, ACL group, timestamps, content hash.

### Subtopic 3.3 — Retrieval Quality: Hybrid Search & Reranking
1. **BM25 from scratch:** term frequency, inverse document frequency, length normalisation.
2. **Postgres full-text search:** `tsvector`, `ts_rank`, and how it compares to BM25.
3. **Hybrid fusion:** score normalisation vs Reciprocal Rank Fusion (RRF).
4. **Bi-encoder vs cross-encoder:** why reranking is slower and more accurate.
5. **Reranking in practice:** a cross-encoder reranker, the top-k budget, and the latency cost.
6. **Metadata filtering:** pre-filter vs post-filter and the recall they cost.
7. **Multilingual retrieval:** English, Nigerian Pidgin, and mixed-language queries.
8. **Query normalisation:** spelling tolerance, abbreviations, and stop-words in business text.
9. **Retrieval metrics:** recall@k, MRR, and nDCG, implemented from scratch.
10. **Failure analysis:** a taxonomy of retrieval misses (chunk split, wrong doc, filter error, no answer exists).

### Subtopic 3.4 — Query Transformation & Advanced Retrieval
1. **Query rewriting:** making a vague question searchable; asking a clarifying question.
2. **HyDE:** embedding a hypothetical answer instead of the question.
3. **Multi-query and RAG-Fusion:** several rewrites, fused results.
4. **Query decomposition:** breaking a multi-hop question into sub-questions.
5. **Self-querying:** the LLM converts a question into structured metadata filters.
6. **Agentic retrieval:** deciding when to re-retrieve; the bridge to Phase 4.
7. **GraphRAG:** entity and relation graphs; when structure matters and when it is overkill.
8. **Multimodal retrieval:** CLIP-style joint embeddings for images and text.
9. **Citations and attribution:** linking each claim to a source span.
10. **Faithfulness checks:** NLI or LLM-judge checks that the answer follows from the sources.

### Subtopic 3.5 — Index Operations, Caching & Cost
1. **Versioned indexes:** build a new index, validate it, then swap the alias.
2. **Incremental updates:** content-hash diffing, upserts, tombstones for deleted documents.
3. **Rebuild cost and scheduling:** when to rebuild fully, and how the Phase 2 DAG triggers it.
4. **Embedding cache:** deduplicating embedding calls by content hash.
5. **Semantic caching:** similarity thresholds and the risk of wrong cache hits.
6. **Query analytics:** zero-result rate, reformulation rate, click-through as a quality signal.
7. **Latency budgets:** profiling p50, p95, and p99; where the time actually goes.
8. **Async database access:** connection pooling and async drivers for the retrieval service.
9. **Cost model:** embeddings + storage + reranking + LLM tokens per answered query.
10. **Load testing:** `k6` or `locust` profiles that reproduce real traffic; the p95 gate.

### Subtopic 3.6 — The RAG Service & Its Evaluation
1. **Retrieval evaluation:** building the 100-query golden set and its labelling rules.
2. **Generation evaluation:** groundedness and answer relevance (RAGAS-style metrics).
3. **Abstention testing:** does the system say "not in the documents" when it should?
4. **Eval harness in pytest:** metrics as tests with thresholds.
5. **Chunk-config A/B tests:** comparing two indexes on the same golden set.
6. **API design:** streaming responses, citation schema, error envelope.
7. **Fallbacks:** no hits, low confidence, and the escalation path.
8. **Tracing:** spans for retrieve → rerank → generate, with timings and scores.
9. **Security:** ACL filtering enforced in SQL, tested with cross-tenant attack cases.
10. **Architecture decision records:** chunk size, index type, embedding model, and why.

**From-scratch challenge:** Implement BM25, a brute-force cosine index, and Reciprocal Rank Fusion in pure Python. Measure recall@5 on the team's 20 labelled queries.

**Interview translation:** "Design RAG over 10 million documents," "why hybrid search?", "explain HNSW's trade-off in one minute." Every answer must include a metric.

**Resources:** Pinecone, Weaviate, and Qdrant learning centres; LangChain and LlamaIndex concept docs (not just the API); the RAG chapters of Chip Huyen's *AI Engineering*; the pgvector README; the BEIR and BERGEN papers as stretch reading; the RAGAS documentation.

---

## PHASE 4: Agents, Tools & Orchestration
**Meeting days:** 15 (days 52–66).
**Project: Harbour Agent Crew.** A multi-agent system that handles a customer case end to end:
- **Researcher** retrieves policy and product context (Phase 3 service) and reads order data through a **read-only SQL tool**.
- **Writer** drafts a reply with citations.
- **Critic** checks the draft against policy and groundedness, and can send it back.
- A **supervisor** routes work. Refunds and other writes need **human approval** through an interrupt.
- Built as a **LangGraph state machine** with checkpointing, full trace logging, and a **hard step and cost budget**.
- A **React + TypeScript chat UI** streams the answer and shows a live trace timeline of every step.

Before the crew, the team builds a **single agent with three tools** that writes a cited report, and logs every step. That warm-up is the first two subtopics.

**Stack covered:** 11 (LangGraph), 10 (TypeScript/React), 4 (tool calling), 9 (agent traces), 3 (agent API).
**CT focus:** Graph and state thinking. Every agent is a state machine with explicit transitions and termination conditions.
**Capstone role:** Orchestration, tools, memory, budgets, and the chat UI.

### Subtopic 4.1 — Single-Agent Fundamentals
1. **What an agent is:** LLM + loop + tools + memory; a 100-line agent with no framework.
2. **Tool-calling patterns:** read tools vs write tools; when the model should not call a tool.
3. **ReAct:** reason-act-observe traces, action parsing, and failure recovery.
4. **Planning:** plan-then-execute vs interleaved planning; task decomposition.
5. **Short-term memory:** message windows, summarisation, and what to keep verbatim.
6. **Long-term and episodic memory:** what to store, how to retrieve it, and the write policy.
7. **Reflection and self-critique:** Reflexion-style retries; when they help and when they loop.
8. **When not to use an agent:** the decision tree between a fixed workflow, a single LLM call, and an agent.
9. **Tool design:** narrow purpose, precise descriptions, typed errors, idempotent behaviour.
10. **Agent evaluation primitives:** steps taken, tool-call correctness, task completion.

### Subtopic 4.2 — LangGraph State Machines
1. **Graph concepts:** nodes, edges, typed state, and reducers that merge updates.
2. **Conditional edges:** routing on state; keeping routing logic in one place.
3. **Checkpointing:** Postgres-backed checkpoints; resuming a case after a crash.
4. **Cycles and loop guards:** maximum iterations and what happens when the guard fires.
5. **Interrupts and human-in-the-loop:** pausing for approval, resuming with a decision.
6. **Streaming:** node-level events and token streaming to the UI.
7. **Subgraphs:** composing graphs; when a team boundary becomes a subgraph.
8. **Tool nodes and error handling:** returning structured errors to the model.
9. **Replay and time travel:** rerunning from a checkpoint to debug a bad decision.
10. **Testing graphs:** stubbed LLM nodes, deterministic transitions, and golden traces.

### Subtopic 4.3 — Multi-Agent Patterns
1. **Supervisor pattern:** one router delegates to specialists; its failure modes.
2. **Swarm and handoffs:** agents pass control directly; when this is simpler.
3. **Hierarchical teams:** sub-supervisors and their budgets.
4. **The Harbour pipeline:** researcher → writer → critic, with exit conditions.
5. **Role prompts and shared-state contracts:** what each agent reads and writes.
6. **Failure modes:** infinite loops, role drift, and agents agreeing with each other by mistake.
7. **Debate and critique patterns:** when a second opinion pays for its cost.
8. **CrewAI concepts:** roles, tasks, and crews; how they map onto LangGraph.
9. **Inter-agent messages:** a typed message schema with validation at each hop.
10. **Choosing a pattern:** a decision matrix over latency, cost, reliability, and debuggability.

### Subtopic 4.4 — Tools, Integrations & Safe Actions
1. **SQL tool:** read-only database role, parameterised queries, table allow-list, row limits.
2. **Retrieval tool:** a thin wrapper around the Phase 3 RAG API with timeouts.
3. **HTTP tools:** timeouts, retries, and mapping vendor errors to tool errors.
4. **Write actions:** refunds and ticket creation behind approval gates.
5. **Idempotency keys for side effects:** the same refund request must never run twice.
6. **Least-privilege permissions:** a permission table per agent and per tool.
7. **Tool input and output validation:** schemas on both sides of the call.
8. **Sandboxed code execution:** for calculations and data analysis, with resource limits.
9. **Indirect prompt injection through tools:** a retrieved page tells the agent to do something bad.
10. **Audit trail:** every tool call logged with who, what, when, and the result.

### Subtopic 4.5 — Budgets, Traces & the Agent UI
1. **Step and cost budgets:** hard limits and graceful stops with a useful partial answer.
2. **Token accounting per node:** attributing cost to each step of the graph.
3. **Latency budgets:** parallel branches, critical paths, and timeouts per node.
4. **Trace schema:** OpenTelemetry spans for agent steps, tool calls, and LLM calls.
5. **Arize Phoenix instrumentation:** tracing a LangGraph run end to end.
6. **React streaming chat:** a client consuming server-sent events or WebSocket messages.
7. **TypeScript API client:** generated from OpenAPI, with types shared between endpoints.
8. **Trace timeline component:** rendering steps, durations, and tokens.
9. **Approval UI:** showing the proposed action, the evidence, and approve or reject controls.
10. **Frontend tests:** Vitest and React Testing Library for components; one Playwright smoke test.

**From-scratch challenge:** Build a ReAct loop with a fake LLM and three tools, with no framework. Then rebuild the same agent in LangGraph and compare the two line by line: where does each one hide its state?

**Interview translation:** "Design an agent that issues refunds safely," "how do you stop an agent from looping?," "draw the graph for this workflow." Answers should name the budget, the approval gate, and the trace.

**Resources:** Lilian Weng's "LLM Powered Autonomous Agents," LangGraph docs and tutorials, Anthropic's "Building Effective Agents," the ReAct and Reflexion papers, the CrewAI docs, the React docs, the TypeScript handbook, Playwright docs.

---

## PHASE 5: Evaluation, Safety & Observability
**Meeting days:** 12 (days 67–78).
**Project: Harbour Trust Layer.** The trust layer that everything else must pass through:
- An eval suite of **200+ cases** covering retrieval, the router, and the agent, with automated scoring and a readable report.
- A **CI eval gate** that blocks a merge when quality drops beyond the agreed tolerance.
- A **red-team report** on Harbour: prompt injection (direct and indirect), jailbreaks, PII leakage, bias, and excessive agency. Every finding has a severity and a fix.
- **Guardrails** on input and output, tested for false-positive rate.
- **Tracing on every request**, a **Grafana dashboard** (quality, cost, latency, errors), and **alerts** that page a human on defined conditions.

**Stack covered:** 6 (testing and evaluation, full), 8 (CI gate), 9 (observability, full), 4 (LLM judges), 11 (agent evals).
**CT focus:** Experimental design. Every claim about quality is a hypothesis that needs a controlled comparison and an interval.
**Capstone role:** The eval gate, guardrails, and dashboards that everyone watches.

### Subtopic 5.1 — Evaluation Design
1. **Why evals are the hardest part:** error analysis before metrics; the team's first 50 failures.
2. **Eval types:** unit, integration, human, LLM-as-judge, benchmark; when each is the right tool.
3. **Golden dataset design:** coverage, difficulty tiers, and versioning the dataset itself.
4. **Open coding and error taxonomy:** labelling failures, grouping them, counting them.
5. **BLEU and ROUGE:** where they are acceptable and where they mislead.
6. **LLM-as-judge design:** pairwise vs pointwise scoring; rubric anchors with examples.
7. **Judge validation:** agreement with human labels, and what to do when it is low.
8. **Statistical rigour:** confidence intervals, paired comparisons, sample-size estimates.
9. **Regression evals in CI:** baselines, tolerances, and updating a baseline on purpose.
10. **Agent evals:** tool correctness, task completion, and path efficiency.

### Subtopic 5.2 — Red-Teaming & Safety Testing
1. **Threat modelling for LLM apps:** assets, trust boundaries, and attacker goals.
2. **OWASP Top 10 for LLM Applications:** a walkthrough mapped onto Harbour.
3. **Direct prompt injection:** attacks against the system prompt and the policy rules.
4. **Indirect prompt injection:** malicious text inside documents, emails, or tool results.
5. **Jailbreaks and policy bypass:** role-play, encoding, and multi-turn attacks.
6. **PII leakage:** cross-tenant leakage through retrieval and through logs.
7. **Bias and fairness tests:** names, dialects, Pidgin inputs, and regional references.
8. **Excessive agency:** the agent taking actions it was never meant to take.
9. **Automated red-teaming:** an attacker model generates attacks; a judge scores success.
10. **Red-team report writing:** severity scale, reproduction steps, fix, and retest result.

### Subtopic 5.3 — Guardrails & Defences
1. **Input filters:** rules vs classifiers; the cost of each.
2. **Output filters:** PII redaction, policy checks, and blocking unsafe content.
3. **Critique passes:** a second model checks the first against written principles.
4. **Spotlighting untrusted content:** delimiters, labels, and "treat this as data" instructions.
5. **Enforcing least privilege:** verifying the Phase 4 permission table with tests.
6. **Rate limiting and abuse detection:** per-user limits and suspicious-pattern alerts.
7. **Refusal design:** helpful refusals that offer a next step and a human path.
8. **Guardrail cost and latency:** measuring what each check adds to a request.
9. **Guardrail testing:** false-positive and false-negative rates on labelled attacks and benign traffic.
10. **Escalation rules:** when the system hands over to a human, and who receives it.

### Subtopic 5.4 — Observability & Alerting
1. **Structured logging:** what to log, and what must never be logged (PII, secrets).
2. **Tracing with OpenTelemetry:** one trace from API → retrieval → LLM → tools.
3. **Metrics:** latency histograms, error rates, token usage, cache hit rate.
4. **Dashboards:** Grafana panels for quality, cost, latency, and errors.
5. **Online evals:** sampling production traffic for judge scores.
6. **Drift detection:** input distribution shift and quality drift over time.
7. **Alert design:** SLOs, error-budget burn rates, and paging thresholds.
8. **Incident runbooks:** what to check first, who to call, how to roll back.
9. **Feedback capture:** user corrections become eval cases (the flywheel from Phase 2).
10. **Cost observability:** cost per tenant and per feature, with budget alerts.

**From-scratch challenge:** Write a small eval harness that computes bootstrap confidence intervals for pass rates. Then build a simple prompt-injection detector and report its false-positive rate on 100 benign messages.

**Interview translation:** "How would you test an LLM feature before launch?" "Walk me through a prompt-injection attack on a RAG system." "What is your SLO for this endpoint, and when does it page?"

**Resources:** Hamel Husain's "Your AI Product Needs Evals" and related posts, Arize Phoenix and LangSmith docs, OWASP Top 10 for LLM Applications, Chip Huyen's *AI Engineering* (evaluation chapters), Anthropic's red-teaming write-ups, the OpenTelemetry documentation, the Google SRE book chapters on SLOs.

---

## PHASE 6: Fine-Tuning & Alignment
**Meeting days:** 12 (days 79–90).
**Project: Harbour Tuned Extractor.** Fine-tune a 7–8B open model with **QLoRA** (free GPU on Colab or Kaggle) to extract structured ticket fields from customer messages: order reference, issue type, urgency, and refund eligibility. Then:
- Compare **base vs prompted vs fine-tuned** using the Phase 5 eval suite.
- Run a small **DPO** experiment on preference pairs (chosen vs rejected replies).
- Merge the adapter, export a quantised artifact, and hand it to Phase 7 for serving.
- Write a **decision memo** that says whether the team should tune at all, and at what volume the answer changes.

**Stack covered:** 4 (structured outputs at training level), 6 (head-to-head evaluation), 9 (experiment tracking), 1 (training-data code).
**CT focus:** Cost and trade-off reasoning. Every choice has a break-even point, and the team computes it.
**Capstone role:** Custom model (if the team tunes) and the base-vs-tuned decision.

### Subtopic 6.1 — Decide: Fine-Tune, Prompt, or RAG?
1. **The decision tree:** knowledge problems → RAG; behaviour and format problems → prompts or tuning.
2. **Cost break-even:** fixed training cost vs per-token API cost, worked on real volumes.
3. **Data requirements:** how many examples, what quality, and how to know you have enough.
4. **Baseline discipline:** the strongest possible prompt must be beaten before tuning.
5. **Base vs instruct models:** choosing the starting point; chat templates for training.
6. **Catastrophic forgetting:** capability loss after narrow tuning, and how to measure it.
7. **Licences:** base model licence, adapter ownership, and commercial-use limits.
8. **Hardware reality:** VRAM budget for 7–8B QLoRA; what fits on a free GPU.
9. **Experiment tracking:** MLflow or Weights & Biases; logging config, data hash, and metrics.
10. **The decision memo template:** question, options, numbers, recommendation, and risks.

### Subtopic 6.2 — SFT & LoRA/QLoRA Mechanics
1. **Full fine-tuning vs PEFT:** what gets updated and why it matters for cost.
2. **LoRA maths:** the low-rank update W + BA, and why it is cheap.
3. **Rank and alpha:** what they control, and quick experiments to see the effect.
4. **Target modules:** attention projections vs MLP projections; the trade-off.
5. **QLoRA:** 4-bit NF4 base weights, double quantisation, paged optimisers.
6. **Dataset formatting:** chat templates, system prompts, and loss masking on the prompt.
7. **Training with TRL's SFTTrainer:** learning rate, batch size, gradient accumulation.
8. **Overfitting and early stopping:** reading validation curves; picking the checkpoint.
9. **Learning-rate schedules:** warm-up, cosine decay, and their effect on stability.
10. **Unsloth vs Axolotl:** when each saves time and when it hides detail.

### Subtopic 6.3 — Preference Alignment: DPO & RLHF (Concepts & Experiment)
1. **What alignment means:** helpfulness, harmlessness, and the trade-off between them.
2. **Preference data:** chosen vs rejected pairs, annotation rules, and their noise.
3. **Reward models:** the Bradley–Terry intuition for pairwise preferences.
4. **RLHF pipeline:** SFT → reward model → policy optimisation (conceptual, with a diagram).
5. **DPO:** the loss intuition, the reference model, and why it avoids a separate reward model.
6. **Why alignment is hard:** reward hacking, sycophancy, and over-refusal.
7. **Synthetic preferences:** LLM-judge labels and the biases they carry.
8. **Running a small DPO experiment:** TRL's DPOTrainer on a few hundred pairs.
9. **Evaluating alignment:** win-rate against the baseline, judged blind.
10. **Safety regressions:** checking that alignment tuning did not weaken refusals or PII handling.

### Subtopic 6.4 — Merging, Quantisation & the Head-to-Head
1. **Merging adapters:** `merge_and_unload` and checking outputs match before and after.
2. **Multi-task and swappable adapters:** one base model, several adapters, switched per request.
3. **Quantisation formats:** GPTQ, AWQ, GGUF; an introduction (benchmarked in Phase 7).
4. **Quantisation-aware vs post-training quantisation:** what each costs and what it protects.
5. **Head-to-head evaluation:** base vs prompted vs tuned on the Phase 5 suite.
6. **Statistical comparison:** paired tests and confidence intervals on the same cases.
7. **Self-hosted vs API economics:** latency, cost per request, and operational burden.
8. **Model registry:** versioned artifacts, metadata, and promotion rules.
9. **Reproducibility:** config files, seeds, dataset hash, and environment lock.
10. **Defending the memo:** a five-minute presentation and five minutes of hostile questions.

**From-scratch challenge:** Implement a LoRA layer in plain PyTorch (`W + BA` with a scaling factor), verify it matches a reference on random inputs, and count the trainable parameters against full fine-tuning.

**Interview translation:** "When would you fine-tune instead of using RAG?" "What does LoRA rank control?" "How do you know the tuned model is better and not just different?"

**Resources:** Hugging Face PEFT and TRL docs, the LoRA paper (Hu et al.), the QLoRA paper, the DPO paper (Rafailov et al.), fast.ai course materials, Sebastian Raschka's writing on LLM training, Unsloth and Axolotl documentation.

---

## PHASE 7: Inference, Deployment & Distributed Systems
**Meeting days:** 12 (days 91–102).
**Project: Harbour in Production.** Take every service to production:
- Containerise the API, retrieval, router, agent, and worker services, and run them on **local Kubernetes (kind)**, then on a managed cluster.
- Serve the Phase 6 model with **vLLM**, and benchmark three quantisation levels on latency, cost, and quality.
- **Horizontal autoscaling** driven by CPU and by queue depth, proven with a load test.
- A **CI/CD pipeline** with the eval gate, a **canary deploy** with traffic splitting, and a **one-click rollback**.
- Caching, rate limits, and graceful degradation (fall back to a smaller model when the primary is slow or down).
- A dashboard of latency, cost, and errors, with SLOs.

**Stack covered:** 12 (Kubernetes, distributed systems), 7 (Docker, full), 8 (CI/CD, full), 9 (SLOs and monitoring), 3 (production APIs).
**CT focus:** Systems thinking. Capacity, failure, and recovery are designed as a set of numbers, not as hope.
**Capstone role:** Everything between "it works on my laptop" and "users can hit it reliably."

### Subtopic 7.1 — Serving Open Models
1. **Batching and continuous batching:** why throughput rises and latency tails grow.
2. **vLLM deep dive:** PagedAttention and how KV-cache memory is managed.
3. **Streaming and concurrency:** limits per GPU, per request, and per user.
4. **Serving engine choice:** Ollama vs TGI vs vLLM; a decision matrix.
5. **GPU memory maths:** weights, KV cache, and activations, with a worked example.
6. **Quantised serving:** AWQ, GPTQ, GGUF benchmarks at three levels.
7. **Throughput vs latency:** tail latency (p99) under load.
8. **Cost per million tokens:** utilisation, idle GPU cost, and break-even against an API.
9. **Autoscaling GPU workloads:** why GPUs scale differently from CPUs.
10. **Benchmark design:** realistic prompt-length distributions and reproducible load profiles.

### Subtopic 7.2 — Containers & Kubernetes
1. **Docker recap:** images, registries, tags, multi-stage builds.
2. **Kubernetes objects:** Pod, Deployment, Service, and how they relate.
3. **Ingress and routing:** exposing services, path-based routing, TLS basics.
4. **ConfigMaps and Secrets:** configuration separated from images.
5. **Health probes:** liveness vs readiness, and why confusing them causes outages.
6. **Horizontal Pod Autoscaler:** CPU vs custom metrics such as queue depth.
7. **Stateful components:** Postgres on Kubernetes vs a managed database; the trade-offs.
8. **Helm basics:** charts, values files, and per-environment overrides.
9. **Local clusters with kind:** creating, loading images, and debugging with `kubectl`.
10. **Resource requests and limits:** OOM kills and CPU throttling, and how to diagnose them.

### Subtopic 7.3 — Distributed Systems Essentials for AI Services
1. **Latency budgets:** network hops, serialisation, and where milliseconds disappear.
2. **Consistency and idempotency:** duplicate messages and at-least-once delivery.
3. **Queues and async jobs:** Redis or Postgres-backed queues; workers and acknowledgements.
4. **Retries, timeouts, circuit breakers:** how they interact and how they cause retry storms.
5. **Load balancing and streaming:** sticky routing for streamed responses.
6. **Caching layers:** invalidation, TTLs, and semantic cache risk.
7. **CAP and partitions:** the intuition, and where Harbour makes deliberate trade-offs.
8. **Rate limiting at scale:** token-bucket and sliding-window designs.
9. **Backpressure and degradation:** shedding load and falling back to a smaller model.
10. **Failure injection:** killing pods and adding latency on purpose; what recovers and what does not.

### Subtopic 7.4 — CI/CD, Canary, Monitoring & MLOps
1. **Pipeline stages:** build → unit and integration tests → eval gate → push image.
2. **Environment promotion:** dev, staging, production; what changes between them.
3. **Canary deploys:** traffic splitting, the metrics that decide promotion or rollback.
4. **Blue/green and one-click rollback:** rollback drills, not just rollback scripts.
5. **Versioning models and prompts:** rolling back a prompt change is a deploy.
6. **Monitoring and SLOs:** the SLOs agreed in Phase 5, enforced in production.
7. **Cost observability:** budget alerts per service and per model.
8. **Semantic caching in production:** A/B testing it and guarding against bad hits.
9. **A/B testing model versions:** success metrics defined before the test starts.
10. **Runbooks and an on-call drill:** the team practises a real incident end to end.

**From-scratch challenge:** Implement a token-bucket rate limiter, then a worker that pulls jobs from a queue with retries, exponential backoff, and idempotency keys. Test it with injected failures.

**Interview translation:** "Design a chat LLM service for 10,000 concurrent users." "A pod keeps restarting, what do you check?" "How do you roll back a bad prompt change without downtime?"

**Resources:** vLLM documentation and blog, Chip Huyen's *AI Engineering* (deployment chapters), CMU's "Machine Learning Systems" course (free), the Kubernetes documentation (concepts and tasks), the Google SRE book, AWS, GCP, or Azure ML deployment docs (pick one cloud).

---

## PHASE 8: Interview & Job-Readiness Sprint
**Meeting days:** 9 (days 103–111).
**Project: Harbour Launch.** Ship the final release and the portfolio:
- A **public repository** with a README, ADRs, a one-command setup, and a demo video.
- A **technical write-up** from each member on their own chunk. This is the proof of depth.
- A **final showcase** to an invited audience (non-engineers included), with live Q&A.
- Each member's **interview pack**: a resume, a two-minute project pitch, and three stories written with STAR.

**Stack covered:** 1 (DSA, full), all stack items through mock interviews.
**CT focus:** Interview reasoning. State assumptions, decompose, estimate, choose, justify, and stress-test.
**Capstone role:** Final release, documentation, and the handover.

### Subtopic 8.1 — DSA Pattern Drills
1. **Hashing and frequency counting:** the first pattern to recognise.
2. **Two pointers:** sorted input and in-place updates.
3. **Sliding window:** variable and fixed windows over strings and arrays.
4. **Prefix sums and intervals:** range queries and merge-interval problems.
5. **Binary search on the answer:** monotonic predicates and feasibility checks.
6. **BFS and DFS on graphs and grids:** shortest path and connected components.
7. **Dynamic programming:** state definition is the hard part; practise defining it aloud.
8. **Heaps and top-k:** streaming data and bounded memory.
9. **Tries:** prefix search and autocomplete.
10. **Backtracking and bit manipulation:** subsets, permutations, and XOR tricks.

### Subtopic 8.2 — System Design for AI Systems
1. **Clarifying requirements:** users, scale, latency, cost, and what "good" means.
2. **Designing RAG at scale:** ingestion, index, retrieval, and the evaluation loop.
3. **Designing an agent platform:** budgets, approvals, traces, and tool permissions.
4. **Designing an eval pipeline and CI gate:** datasets, judges, and blocking rules.
5. **Designing a data flywheel:** capture, labelling, retraining, and re-deployment.
6. **Designing for cost:** caching, routing, batching, and quantisation.
7. **Designing for reliability:** fallbacks, SLOs, and graceful degradation.
8. **Designing multi-tenant security:** ACL-aware retrieval and isolation.
9. **Designing a streaming chat backend:** connections, backpressure, and reconnects.
10. **Back-of-envelope estimates:** tokens per second, storage per million chunks, cost per day.

### Subtopic 8.3 — Logical & Behavioural Interviews
1. **Logic puzzles under constraints:** reasoning aloud, checking edge cases.
2. **Fermi estimation:** structured guesses with stated assumptions.
3. **Debugging scenario:** a broken pipeline; the questions to ask before touching code.
4. **Code review scenario:** finding the bug in a pull request, and phrasing feedback kindly.
5. **Ambiguous requirements:** negotiating scope with a non-technical stakeholder.
6. **Explaining trade-offs:** the same decision explained to a manager, a designer, and an engineer.
7. **STAR stories from the project:** situation, task, action, result, each tied to a metric.
8. **Disagreement in a team:** a real example from the ten-person build and how it was resolved.
9. **Owning a mistake:** a short, honest post-mortem story.
10. **Portfolio narrative:** the two-minute pitch and the "why this project" answer.

### Subtopic 8.4 — Mock Interviews, Portfolio & Job Search
1. **Mock technical screen:** 45-minute live coding with a timer and a peer observer.
2. **Mock system design:** 60 minutes, whiteboard or shared doc, graded on the rubric.
3. **Rapid-fire ML and LLM concepts:** 20 questions, 60 seconds each.
4. **Take-home practice:** a 4-hour assignment scored against a checklist.
5. **Resume and GitHub review:** keywords for AI engineer roles, clear project impact lines.
6. **Public write-up:** each member's chunk published as a short technical article.
7. **Demo video and README polish:** a three-minute walkthrough anyone can follow.
8. **Peer interview rounds:** each member interviews two others and gives written feedback.
9. **Job search pipeline:** target companies in Nigeria and remote roles, a tracking sheet, and outreach templates.
10. **Final showcase:** a 10-minute group presentation followed by 10 minutes of hostile questions.

**From-scratch challenge:** Solve three problems from memory in 30 minutes each, with no notes, then explain the complexity and one alternative approach.

**Interview translation:** every item above is an interview. The final gate is a mock loop: a technical screen, a system design, a logic round, and a behavioural round, each run by a different member.

**Resources:** *Cracking the Coding Interview* (patterns chapters), NeetCode and LeetCode (pattern lists), *Designing Data-Intensive Applications* (Kleppmann), the "System Design Primer" repository, your own project repository and logs.

---

# 6. This Week: Wednesday 14 & Friday 16 October 2026

### Wednesday 14 October — Kickoff (Day 1)
| Time | Activity |
|---|---|
| 09:00–09:30 | Computational thinking warm-up: the "bus stop" problem (decompose a route into steps, then estimate the time) |
| 09:30–10:30 | Introduce HARBOUR, the four CT pillars, and the 1.1 learning cycle. Walk through this roadmap. |
| 10:30–12:30 | **Team setup:** Git repository, branch rules, code owners, environment setup, Python 3.12+ installed, `uv` configured, Postgres via Docker Compose. Everyone runs a "hello, Harbour" test. |
| 13:30–15:00 | **Member roster and chunk draw** for Subtopic 0.1 and 0.2. Each member writes a one-line goal for their chunk. |
| 15:00–16:30 | Pair work: first SQL schema for the Harbour Core API (customers, orders, tickets). |
| 16:30–17:30 | From-scratch lab: LRU cache (Phase 0 challenge). |
| 17:30–18:00 | Retro and learning log. |

### Friday 16 October — Foundations Start (Day 2)
| Time | Activity |
|---|---|
| 09:00–09:30 | CT warm-up: two pointers vs hashing on the same problem; which is faster and why |
| 09:30–10:00 | Stand-up. Confirm everyone can run the environment. |
| 10:00–12:30 | **Teach-back block, Subtopic 0.1 (Python problem solving):** each member teaches their chunk (15 min each). |
| 13:30–16:00 | Build block: first FastAPI skeleton with a health endpoint and a `GET /orders` route, plus its first test. |
| 16:00–16:30 | Cold-call drill on Subtopic 0.1. |
| 16:30–17:30 | Lab: implement the Phase 0 CT question on a whiteboard, with no IDE. |
| 17:30–18:00 | Retro. Confirm the Monday 19 October plan. |

**Note:** Subtopic 0.1 teach-backs start on Friday. Members who are not yet ready to present will teach on Monday 19 October and be added to the cold-call rotation on the same day.

---

# 7. Definition of "Job-Ready" (Team Checklist)

Each member should be able to do all of the following without help, by the end of Phase 8.

**Engineering**
- [ ] Write and explain an O(n log n) or O(n) solution to a medium-difficulty problem in 25 minutes.
- [ ] Design a PostgreSQL schema, write a JOIN with a window function, and read an `EXPLAIN ANALYZE` plan.
- [ ] Build a FastAPI service with auth, validation, tests, and a Dockerfile, and run it in Compose.
- [ ] Ship a change through CI with lint, types, tests, and an eval gate.

**AI engineering**
- [ ] Explain tokenization, the KV cache, and sampling parameters to a non-engineer.
- [ ] Build a structured-output extraction with validation and retries.
- [ ] Build a RAG pipeline and defend the choice of chunking, index, and reranker with metrics.
- [ ] Build a LangGraph agent with a budget, a checkpoint, an approval gate, and a trace.
- [ ] Design and run an eval suite, including the statistics behind a claim.
- [ ] Decide, with numbers, whether to fine-tune; run QLoRA and a head-to-head.
- [ ] Explain a deployment, a canary, a rollback, and an SLO in one minute each.

**Computational thinking and interviews**
- [ ] Decompose an unfamiliar problem and state assumptions before solving it.
- [ ] Estimate numbers (tokens, storage, cost, latency) for a system within an order of magnitude.
- [ ] Explain a project's trade-offs in two minutes, and answer a hostile follow-up.

---

# 8. Resource Index (Quick Reference)

| Area | Resource |
|---|---|
| LLM foundations | Lil'Log (Lilian Weng), Karpathy's tokenizer video, `tiktoken` |
| Prompting | Anthropic and OpenAI prompt engineering guides |
| Book (throughout) | Chip Huyen, *AI Engineering*; *Designing Machine Learning Systems* (data and deployment chapters) |
| Data | DVC docs, Hugging Face Datasets course, Andrew Ng's data-centric AI, Microsoft Presidio |
| RAG | Pinecone, Weaviate, Qdrant learning centres; pgvector README; RAGAS docs; BEIR paper |
| Agents | Anthropic's "Building Effective Agents," LangGraph docs, ReAct and Reflexion papers |
| Fine-tuning | Hugging Face PEFT and TRL docs, LoRA/QLoRA/DPO papers, fast.ai, Raschka, Unsloth, Axolotl |
| Evals and safety | Hamel Husain's evals posts, Arize Phoenix, OWASP Top 10 for LLM Applications |
| Deployment | vLLM docs, Kubernetes docs, Google SRE book, CMU "Machine Learning Systems" (free) |
| Interviews | *Cracking the Coding Interview*, NeetCode, *Designing Data-Intensive Applications*, the System Design Primer |

---

**Open items for the team to decide in Week 1:**
1. Confirm the capstone domain (Port Harcourt SME operations copilot as default).
2. Confirm the hosted LLM provider budget and the open-model host (local Ollama or a rented GPU).
3. Confirm the exact calendar mapping for meeting days, including public holidays.
4. Confirm the cloud for Phase 7 (AWS, GCP, or Azure), or stay on local Kubernetes only.

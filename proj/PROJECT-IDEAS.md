# Kaustubh Sonawane — Project Ideas for S-tier Gaps

Twenty project ideas that each close at least three of the six S-tier gaps in `GAPS.md`: **S1** LLM evaluation, **S2** agent frameworks and multi-agent orchestration, **S3** MCP, **S4** agent harness and context engineering, **S5** LLM observability and tracing, **S6** hybrid retrieval and RAG depth. Gap codes refer to rows in `GAPS.md`.

- **One project can close all six.** The gaps fit together as one system: a retrieval index (S6), served as tools through an MCP server (S3), used by a LangGraph multi-agent workflow (S2), with long-running memory and compaction (S4), traced end to end (S5), and scored by an eval suite gated in CI (S1).
- Ideas 1–16 and 19–20 cover all six. Ideas 17–18 cover four, but close A-tier gaps (fine-tuning, PyTorch, serving) instead.
- **Honesty:** nothing here goes into `EXPERIENCE.md` or a CV until the project exists.

## The common spine

What every 6/6 project needs at a minimum before a gap can be claimed:

| Gap | Minimum to build |
|---|---|
| S6 | BM25 + dense vector + hybrid (RRF) + cross-encoder reranker; recall@k / MRR measured on a labelled query set; answers carry citations to the source chunk |
| S3 | The retrieval and domain tools ship as a standalone **MCP server**; the agent uses them through an MCP client; one write-up comparing MCP tools with plain function calling |
| S2 | **LangGraph** (or Google ADK) graph with planner, retriever/worker and verifier subagents; durable checkpointing so a run survives a restart |
| S4 | Session + long-term memory store (Postgres/Redis) with reconciliation and forgetting; context compaction with a measured quality cost; Pydantic structured outputs; retries and model fallback |
| S5 | **Langfuse** or Arize Phoenix tracing of every node and tool call; a dashboard of per-request cost, latency and failure modes |
| S1 | Gold dataset (50–200 items), regression suite, LLM-as-judge **calibrated against your own human labels**, error analysis write-up, GitHub Actions gate that fails on regression |

## 20 project ideas

Effort is solo, full-time: **M** ≈ 3–4 weeks, **L** ≈ 5–6 weeks (MVP of the spine first, extras after).

| # | Project | What it does | S gaps | Extra gaps closed | Public data | Best-fit JDs / roles | Effort |
|---|---|---|---|---|---|---|---|
| 1 | **FundLens**: mutual-fund research agent | Answers fund questions by combining SQL tools over a fund DB with hybrid search over factsheets and regulator circulars; abstains on investment advice | S1–S6 (6/6) | A5, A6, B3, B8, B11, D7 | AMFI NAV data, SEBI circulars, AMC factsheet PDFs | Fintech, BSC, Capsa, Apexon, India roles; direct sequel to HDFC work | M |
| 2 | **CiteScout**: scientific-literature agent | Multi-hop questions over PubMed / Europe PMC with citation-grounded answers and a gene/cell-line knowledge graph; extends CellLineSelector | S1–S6 (6/6) | B1, B4, A5 | Europe PMC OA, PubMed abstracts, DepMap/HPA | Elsevier, Tank, Viridien, Callosum, DS roles | L |
| 3 | **RuleCheck**: UK financial-regulation copilot | Clause-level Q&A over the FCA Handbook / PRA Rulebook, plus an agent that checks a policy doc against rules and flags gaps | S1–S6 (6/6) | A5, B4, D5 | FCA Handbook, PRA Rulebook (public) | Pay.UK, Compare the Market, Lendable, Apexon | M |
| 4 | **TriageGuide**: clinical / veterinary guideline assistant | Symptom intake → retrieve guidance → structured triage with confidence and an abstain/escalate path; hallucination eval is the headline | S1–S6 (6/6) | A5, D5, (B2 if images added) | NICE guidelines, open vet formularies | Paloma Health, Vet-AI | M |
| 5 | **DealDesk**: PE / M&A filings analyst | Reads 10-K/8-K filings, extracts metrics, runs calcs in a code sandbox, drafts a cited investment memo into docx/xlsx | S1–S6 (6/6) | B19, B20, B4, A6 | SEC EDGAR (free API) | Capsa, BSC, finance AI roles | L |
| 6 | **ClaimPilot**: insurance claims copilot | Matches a claim to policy wording with citations, calls a fraud-score tool, routes to approve/deny/escalate with human approval | S1–S6 (6/6) | A5, B7, B20 | Public UK policy wordings, Kaggle insurance-fraud data | Prima, Compare the Market, Lendable | L |
| 7 | **RepoPilot**: developer-productivity agent | MCP server over a repo's docs, issues and CI logs; hybrid code search; PR-review and test-generation subagents on the Claude Agent SDK, plus a Claude Code skill | S1–S6 (6/6) | B21, C6, B11, C8, D6 | Any large OSS repo (e.g. FastAPI) + its issues | Anthropic FDE / DNB, Intelstack, Linux Recruit, Gazelle Global | M |
| 8 | **DeskMate**: customer-support agent | Classify ticket → retrieve help-centre articles → resolve or hand off; replayed A/B of two prompt/model variants | S1–S6 (6/6) | A5, A7, B4, B6 | Bitext support dataset, a public help centre | Lendable, Currys, Ten, Moonpig | M |
| 9 | **InboxBrain**: Outlook + calendar assistant | Personal memory with source refs and corrections over your mail; OAuth, webhook sync, queue, idempotent writes, approval before any action | S1–S6 (6/6) | B15, C3, C4, D7 | Your own Microsoft 365 dev tenant (free) | Byte, UBE, Microsoft-heavy roles | L |
| 10 | **GiftGenie**: conversational shopping advisor | Hybrid product search + a recommender tool + preference memory; offline A/B with uplift metrics | S1–S6 (6/6) | B5, B6, A7 | Amazon Reviews (McAuley) dataset | Moonpig, Currys, Compare the Market | L |
| 11 | **Tenant**: multi-tenant enterprise knowledge agent | Per-tenant isolated indexes and memory, OAuth + secrets manager, connectors (GitHub, Drive, Notion) as MCP servers, cost-aware model router; HDFC's siloed departmental RAG, rebuilt properly | S1–S6 (6/6) | C3, B3, B8, A5, A6 | Demo tenants: fund docs (#1) + papers (#2) | Gazelle Global, Linux Recruit, CATCHES, BSC, most AI Engineer JDs | L |
| 12 | **OpsSleuth**: incident-investigation agent | Classify alert → retrieve runbooks and past incidents → query logs/metrics via MCP → reason → validate → propose action with human approval | S1–S6 (6/6) | C5, A5, D1 | OpenTelemetry demo app + synthetic incidents | Apexon (matches its workflow wording), Viridien, Ten | L |
| 13 | **WellLog**: geoscience report agent | VLM OCR over scanned well/survey reports, hybrid retrieval, entity graph of wells/fields, cited answers | S1–S6 (6/6) | B20, B1, B4 | NSTA National Data Repository, BGS reports | Viridien, energy/engineering AI roles | L |
| 14 | **StatuteScope**: UK legislation agent | Section-level Q&A over legislation.gov.uk with amendment timelines (point-in-time retrieval) and Hansard context | S1–S6 (6/6) | B1, B4 | legislation.gov.uk API, Hansard API | CGI, consultancies (Saragossa-type), GovTech | M |
| 15 | **TutorLoop**: course tutor agent | Grounded tutoring over open textbooks, student-progress memory with forgetting, quiz generation, accessibility audit on the UI | S1–S6 (6/6) | F (WCAG), optional B12 Copilot Studio port | OpenStax textbooks, MIT OCW | UBE, EdTech | M |
| 16 | **Concierge**: voice lifestyle agent | STT → LangGraph → TTS booking assistant with preference memory and hybrid venue search; latency budget per turn | S1–S6 (6/6) | B9, A6, D7 | Yelp Open Dataset | Ten Lifestyle, Lendable, CATCHES | L |
| 17 | **SmallBrain**: fine-tuned SLM as the agent's router/tool-caller | QLoRA a small open model to do tool selection inside a LangGraph agent; serve with vLLM behind LiteLLM; compare with a frontier model on quality/cost/latency | S1, S2, S4, S5 (4/6) | A1, A2, A3, A6, B3, B13, C9 | Synthetic tool-call traces + Gorilla/BFCL | Elsevier, CGI, Tank, Callosum, Byte, MLE roles | L |
| 18 | **RetrievalLab**: retrieval benchmark + fine-tuned embedder | Benchmarks BM25 / dense / hybrid / reranked across pgvector, OpenSearch and Qdrant; fine-tunes an embedder in PyTorch; ships the winner as an MCP search server | S1, S3, S5, S6 (4/6) | A1, A2, B18 | BEIR datasets (SciFact, FiQA) | Capsa, Elsevier, Callosum | M |
| 19 | **DocFlow**: document-to-data ingestion agent | VLM OCR of scanned letters/invoices → Pydantic extraction → retrieve similar past docs as few-shot → verify against DB via MCP; field-accuracy eval (mirrors the HDFC image-email story) | S1–S6 (6/6) | B20, B8, B4 | FUNSD, CORD, SROIE datasets | Capsa, Apexon, data-engineer roles | M |
| 20 | **AskTheWarehouse**: text-to-SQL analyst agent | Hybrid retrieval over schema + dbt docs as a semantic layer, SQL via MCP, sandboxed Python for charts, memory of metric definitions; eval on a BIRD-style gold set | S1–S6 (6/6) | B16, B19, C1, B17 | BIRD / Spider, NYC Taxi in DuckDB/Athena | Lafosse, Compare the Market, Saragossa, DS/DE roles | M |

## Recommendation

Build **#11 Tenant** first, with **#1 FundLens** as its first demo tenant.

- It closes all six S gaps plus C3, B3, B8, A5 and A6, the most coverage of any idea.
- It matches the "enterprise AI platform" wording in Gazelle Global, Linux Recruit, CATCHES and BSC.
- It turns the strongest HDFC story (department-siloed RAG with a cost-aware Llama-3/Azure split) into a "here's how I'd build it now" repo, which is easy to talk through in interviews.
- The fund tenant gives it real data and domain depth, and a papers tenant (#2) can be added later without new architecture.

For the Anthropic / Intelstack track, build **#7 RepoPilot** first instead. It is smaller and also closes B21, C8 and D6.

# Kaustubh Sonawane — Project Gaps

Topics and tech that the jobs applied for ask for, and that `EXPERIENCE.md` cannot back with a real project. Build a project for each, then add it to `EXPERIENCE.md` and the CV.

- **Source:** the 13 JDs in `jobs/*/JD.txt` (BSC, CATCHES, CGI, Currys, Elsevier, Lendable, Moon Commerce, Moonpig, Paloma Health, Prima, Tank/Data Scientist GenAI, TowardsChange, Vet-AI). Milltech has no JD saved, so it is not counted.
- **Count (x/13):** how many JDs ask for it, from a manual read. Required and nice-to-have are both counted, so treat it as approximate. Most of the 13 are AI Engineer roles, so Data Scientist and ML items are under-counted.
- **Tiers:** S = build first. A = high value. B = middle. C = lower. D = only if cheap. F = skip, a bullet or a line in Skills is enough.
- **Ordering rule:** AI/ML tech sits in S and A, data work in the middle tiers, MLOps, cloud and extra languages in the low tiers. Within that, ties are broken by how many JDs ask and how firmly, then by how cheap the project is.
- **Honesty:** nothing here is claimed until the project exists and is in `EXPERIENCE.md`. Per the guardrails, HDFC had no formal evals, no fine-tuning and no MCP.

## Build these first (flagship projects)

Five projects close most of S and A. Build them as the open-source repos a recruiter can click.

| # | Project | Closes |
|---|---|---|
| 1 | **Agent harness**: a long-running agent with MCP tools, durable state and memory, context compaction, retries and fallbacks, model/tool routing, guardrails and subagents. Use LangGraph or Google ADK, plus one custom loop for comparison. Add per-user isolation, OAuth and a secrets manager. | S2, S3, S4, A5, A6 (cost), B3, B8, C3 |
| 2 | **Eval and observability rig**: gold dataset, regression suite, LLM-as-judge calibrated against human labels, error analysis, Langfuse or Phoenix tracing, a cost dashboard, a prompt-versioning gate in CI, and an offline simulator with a replayed A/B comparison. Run it against project 1 or Wingman. | S1, S5, A6 (cost), A7, B11 |
| 3 | **SLM fine-tune**: LoRA/QLoRA on a small open model for a narrow task, written in PyTorch and Hugging Face. Train it, then evaluate it against a prompted frontier model and a baseline, and report cost and latency. Add drift detection and a retrain trigger. | A1, A2, A3, C2 |
| 4 | **Scientific-literature retrieval project**: BM25, vector and hybrid retrieval with a reranker, measured on recall@k and answer faithfulness, with evidence-grounded answers and citations. Add a knowledge graph and entity extraction on top. Extend the AstraZeneca/CellLineSelector work. | S6, B1, B4 |
| 5 | **Wingman vision validation (cheap)**: Wingman already scores photos with a vision model. Validate those scores against a labelled set, report accuracy and failure cases, and add an abstain path. Upgrade to a full multimodal triage app only if you target Vet-AI-style roles. | B2 |

Also deploy one of the flagships on Vertex AI (Cloud Run + Vertex) to close B10 at low cost.

## S tier

| # | Topic | Asked by | Gap today | Project to build |
|---|---|---|---|---|
| S1 | **LLM evaluation**: gold/regression datasets, LLM-as-judge, synthetic eval data, error analysis, evaluating where there is no clean ground truth, offline-to-online correlation | 9/13: Paloma, Vet-AI, CATCHES, Lendable, Moon, BSC, TowardsChange, Currys, Tank | No formal evals at HDFC or in Wingman. Paloma and Vet-AI make this their core requirement. | Flagship 2. Report the baseline plainly, including where a change did not beat it. |
| S2 | **Agent frameworks and orchestration**: LangGraph, Google ADK, multi-agent systems, subagents, durable workflows, managed agents | 10/13: Vet-AI, Paloma, CATCHES, Currys, CGI, Tank, TowardsChange, Lendable, Moon, BSC | Only hand-rolled tool calling and LlamaIndex. No framework, multi-agent or durable workflow project. | Flagship 1. Build the same agent on LangGraph, on ADK and with a custom loop, and write up the trade-offs. |
| S3 | **MCP**: building servers and clients, evaluating connectors, tool gateways | 3/13: Paloma, CATCHES, BSC | No project. Claude Code is only a tool in Skills. Ranked S for high signal and low effort (a few days), not for frequency. | Flagship 1. Publish an MCP server over a real data source plus a client, and compare MCP tools against plain function calling. |
| S4 | **Agent harness and context engineering**: context management, structured outputs, compaction, long-running sessions, state, memory schemas, forgetting, retries and fallbacks | 3/13: CATCHES, BSC, Vet-AI | Wingman has validate/repair/retry/cache and SSE streaming, but no memory, compaction or long-running sessions. | Flagship 1. Add a memory store with reconciliation and forgetting, and measure what compaction costs in quality. |
| S5 | **LLM observability and tracing**: Langfuse, LangSmith, Braintrust, Arize Phoenix, debugging non-deterministic systems, production monitoring, rollback | 5/13: Paloma, CATCHES, Lendable, Currys, Vet-AI | None. Prompts were versioned in Git only. | Flagship 2. Trace every agent step and build a dashboard of failure modes and per-request cost. |
| S6 | **Hybrid retrieval and RAG depth**: keyword plus vector search, reranking, FAISS/Pinecone/Chroma, retrieval metrics, evidence-grounded generation | 6/13 asked by name: CATCHES, Elsevier, Tank, Moon, CGI, Paloma. RAG appears in most of the other JDs too, and Vet-AI lists RAG depth as essential. | pgvector only, with no hybrid retrieval, reranking or retrieval metrics. Moved up from A because retrieval is the most common theme across the JDs. | Flagship 4. Compare BM25, vector and hybrid with a reranker on recall@k and faithfulness, and try a second vector store. |

## A tier

| # | Topic | Asked by | Gap today | Project to build |
|---|---|---|---|---|
| A1 | **Fine-tuning LLMs and SLMs**: LoRA, QLoRA, domain adaptation, comparison against prompting | 4/13: Elsevier, Tank, CGI, BSC (familiarity) | HDFC explicitly had no fine-tuning. Required at Elsevier and CGI, desirable elsewhere. Matters most for ML and DS roles. Moves to S if you target those. | Flagship 3. Fine-tune a small model for a narrow task, then compare it with prompting and RAG on quality, cost and latency. |
| A2 | **Deep learning frameworks**: PyTorch, TensorFlow, Hugging Face Transformers, with training loops | 4/13: Elsevier, Prima, CGI, Tank | Only a CNN in the B.Tech project and the VisionCaptioner team study, and the personal split of that study is not recorded. | Flagship 3, written in PyTorch and Hugging Face. Add a solo transformer or classifier fine-tune with a full training loop. |
| A3 | **Training and adapting models**: domain data prep, adaptation of foundation models, training pipelines | 3/13: CGI, Tank, Elsevier | None as a personal project. | Part of flagship 3. Include a dataset-building and cleaning pipeline. |
| A4 | **Prompt engineering as a product**: prompt/skill libraries, versioning, evaluation, prompt optimisation research | 3/13: BSC, Vet-AI, Paloma | Versioning in Git only, no systematic optimisation. | A prompt library with versions and eval scores, plus automated prompt optimisation (DSPy or similar) with a before/after report. |
| A5 | **Guardrails, safety and decision control**: guardrails, calibrated decision models, bias mitigation, abstention | 4/13: CATCHES, BSC, Tank, Vet-AI | System prompts only. | Flagship 1. Add input/output guardrails, a calibrated confidence score and an abstain/escalate path. |
| A6 | **Cost and latency modelling** for LLM systems | 5/13: BSC, CATCHES, Currys, Tank, TowardsChange | Llama-3 vs Azure was decided on cost, but not modelled. Moved up from B: 5/13, BSC and Tank ask explicitly, and it falls out of flagships 1 and 2. | Parts of flagships 1 and 2. A cost model per request and per workflow, and a latency budget. |
| A7 | **Evaluation platform depth**: A/B testing of LLM variants, simulation environments, offline-vs-live correlation | 2/13: Vet-AI, Moonpig | None. | Extend flagship 2 with an offline simulator and a replayed A/B comparison. |

## B tier

| # | Topic | Asked by | Gap today | Project to build |
|---|---|---|---|---|
| B1 | **Knowledge graphs, ontologies and taxonomies** for retrieval and grounding | 1/13: Elsevier (graphs, ontologies, citations) | No project. Moved down from A: only one JD asks. Still worth building because flagship 4 covers it. | Part of flagship 4. A graph over the DepMap/GEO/HPA data or a paper corpus, with graph plus vector retrieval (GraphRAG-style). |
| B2 | **Multimodal and computer vision in production**: frontier VLMs with evaluation and guardrails, custom vision models | 3/13: Vet-AI, Prima, CATCHES | Wingman scores photos, but those scores are LLM-judged and unvalidated. VisionCaptioner is academic. Moved down from A: essential only at Vet-AI. | Flagship 5 (the cheap route). Validate against labelled data and report accuracy and failure cases. |
| B3 | **Model and tool routing**: routing between models and tools by task, cost and confidence | 2/13: CATCHES, TowardsChange | HDFC did manual per-department model allocation, with no routing logic. Moved down from A: 2/13 and cheap to fold into flagship 1. | Flagship 1. A router with a cost/quality benchmark. |
| B4 | **NLP tasks**: entity extraction, classification, summarisation, QA, ranking over large text corpora | 3/13: Elsevier, Tank, Lendable | Document extraction at HDFC, with no measured NLP models. | Part of flagship 4. Entity extraction and classification with precision/recall against a labelled set. |
| B5 | **Recommendation and personalisation systems**, customer modelling (propensity, uplift, CLV) | 1/13: Moonpig | None. Apriori only. | A recommender on a public dataset with offline metrics and a simple uplift or CLV model. |
| B6 | **Experiment design and A/B testing** statistics: metrics, power, interpretation | 2/13: Moonpig, Vet-AI | None. | A written-up A/B analysis on a public dataset with sample-size and metric choices explained. |
| B7 | **Classical ML on tabular data**: feature engineering, validation, model selection, overfitting | 4/13: Moonpig, Prima, Elsevier, Tank | Only the datathon fraud entry and the MSc. Would rise if you apply to more DS and ML roles. | A tabular project with proper validation and a model card. A claims-style or fraud dataset fits Prima. |
| B8 | **Data pipelines for AI**: ingestion, verification, preparing context for agents, feature engineering | 4/13: BSC, Currys, CGI, CATCHES | HDFC pipelines exist, but not tied to LLM context. | Part of flagship 1. An ingestion and verification pipeline that feeds the agent's context. |
| B9 | **Voice AI** and multimodal inputs (messaging, voice) | 2/13: Lendable, CATCHES | None. | A small voice agent (speech-to-text, LLM, text-to-speech) with a latency measurement. |
| B10 | **Managed cloud AI platforms**: Vertex AI/Gemini, Azure AI services, Bedrock | 6/13: Paloma, Vet-AI, Currys, TowardsChange, BSC, CGI | Azure OpenAI at HDFC, and AWS. No Vertex AI or GCP. Moved up from C: 6/13, and GCP with Vertex AI is essential at Vet-AI. | Deploy one flagship on Vertex AI (Cloud Run + Vertex), and call Azure AI. Low effort on top of a flagship. |
| B11 | **CI/CD for ML and LLM systems** (eval gates in pipelines) | 3/13: CGI, Moonpig, Paloma | Jenkins/GitLab deploys at HDFC, with no eval gates. Moved up from C because it is part of flagship 2. | Part of flagship 2. GitHub Actions that block a merge on an eval regression. |

## C tier

| # | Topic | Asked by | Gap today | Project to build |
|---|---|---|---|---|
| C1 | **Spark / Databricks and the wider data platforms**: Databricks, Fabric, BigQuery, dbt | 4/13: Currys, BSC, Vet-AI, Moonpig | None. | A small Databricks or Spark pipeline, plus a dbt model layer. Fabric and BigQuery are lower value. |
| C2 | **Model monitoring, drift detection, automated retraining** | 3/13: Elsevier, Moonpig, CGI | None. | Add drift detection and a retrain trigger to flagship 3 or B7. |
| C3 | **Multi-user isolation, permissions and secrets management** | 3/13: CATCHES, BSC, Tank | RBAC and LDAP at HDFC. No SSO, OAuth or secrets-manager work. | Add OAuth, per-user isolation and a secrets manager to flagship 1. |
| C4 | **Microsoft ecosystem**: Graph API, SharePoint, Power Automate | 1/13: BSC | None. | An agent that reads SharePoint via Graph API. Only worth it for Microsoft-heavy roles. |

## D tier

| # | Topic | Asked by | Gap today | Project to build |
|---|---|---|---|---|
| D1 | **Kubernetes and container orchestration**, GPU or on-prem AI environments | 1/13: CGI (needs clearance and is on-site) | Docker only, and a GPU EC2 instance for Llama-3. | Deploy flagship 3 on a local k8s cluster (kind or k3s) if time allows. |
| D2 | **Automation tools**: n8n, Zapier, Make | 1/13: Moon Commerce | None. | A short n8n workflow wrapping an LLM call. Skills line only is fine. |
| D3 | **Golang** | 1/13: Vet-AI (nice to have) | None. | A small Go service wrapping an LLM call. |
| D4 | **Pub/Sub, event-driven messaging, BigQuery dashboards** | 1/13: Vet-AI | None. | Add Pub/Sub to the GCP deployment (B10). |
| D5 | **Healthcare or regulated-domain documentation** (regulatory documentation, information governance, model risk) | 3/13: Paloma, Vet-AI, Tank | HDFC Compliance review only. | Write a model card and risk assessment for a flagship. |
| D6 | **Anthropic product familiarity** (Claude Cowork, Managed Agents) | 1/13: BSC | Claude Code is already in Skills. | Covered by S2 and S3. A one-line mention is enough. |

## F tier

Skip these: they show up once, are cheap to learn on the job, and do not justify a project.

| Topic | Asked by | Note |
|---|---|---|
| Streamlit / Flask | Tank | FastAPI already covers the API requirement. |
| Elixir / Rust | Prima (nice to have) | Not worth a project. |
| Cursor / Codex as tools | Currys | Claude Code is already listed in Skills. |

## Gaps that a project cannot close

Mention these in applications where relevant, but do not spend time on them.

- **UK right to work:** several JDs (BSC, Moon Commerce, Tank) require existing right to work and no sponsorship. Current status is Student Visa, eligible for the Graduate Visa.
- **Security clearance:** CGI needs UK clearance or eligibility.
- **Domain experience:** impact investing (BSC), insurance claims (Prima), healthcare or veterinary (Paloma, Vet-AI), e-commerce (Moonpig). HDFC covers financial services only.
- **Seniority:** Vet-AI asks for 4+ years of AI/ML engineering. The CV shows about 3 years.
- **Degree result:** the MSc is awaiting result and must not be claimed.

## Already covered (no project needed)

RAG with pgvector, LlamaIndex and Azure OpenAI; agentic tool calling (hand-rolled); FastAPI and React full-stack delivery; AWS deployment; Docker and Jenkins/GitLab CI/CD; PostgreSQL schema design and ingestion; document and email extraction; Power BI and Pandas analysis; RBAC with LDAP; Wingman as an LLM app with output validation; MSc data work with AstraZeneca; stakeholder delivery and team leadership.

# Aventum: AI Engineer (VN583), Round 1 Interview Strategy

## 1. Snapshot

| | |
|---|---|
| Role | AI Engineer, Technology department, reports to the Head of AI. No management duties. |
| Entity | Aventum Group Management Services Ltd (group brands: Rokstone underwriting/MGA, Consilium broking). Specialty (re)insurance, Lloyd's/London market. |
| Pay / place | Up to £80,000. Monument Building, 11 Monument Street, EC3R 8AF. Hybrid, 3 days a week in the office, 8:30am to 5pm. |
| Contact | Lucy Orpwood, Talent Attraction Partner (lucy.orpwood@aventumgroup.com, +44 7514 315 402). |
| When | **Friday 23 Oct 2026, afternoon. Exact time NOT confirmed yet.** Your last mail said "any time in the afternoon works". |
| Format | Unknown. Their recruitment journey says an **Outlook invite with "everything you need to prepare"** follows once the time is agreed. Usually **2 interview stages**, sometimes a **3rd case study or technical exercise**; the whole process runs at most 3 weeks. If you don't progress after round 1 you get a written update. |

### Open actions (do today/tomorrow)
- [ ] Chase the time if no invite by Wednesday midday: one line to Lucy ("Happy with any afternoon slot on Friday, could you confirm the time and whether it's on Teams or at the office?").
- [ ] When the Outlook invite arrives, read it for **who** is interviewing (Talent, the Head of AI, an engineer?) and **format** (video or in person). Adjust section 9 accordingly. If in person, plan Bristol to London travel (aim to arrive 30 min early).
- [ ] Have these answers ready, because the recruitment journey says they will ask for **remuneration and notice period**:
  - **Salary expectation:** `[YOU: figure]`. The band tops out at £80k. A range in the upper-middle of the band is defensible on 3 years of production AI delivery, but your cover letter openly listed several gaps against this JD, so don't open at the ceiling. Give a range, say it's flexible for the right role, and mention the CSOP and bonus count in the total.
  - **Notice period / availability:** you are not employed (left HDFC Jul 2025, MSc ended Sep 2026), so it is effectively immediate. `[YOU: confirm, subject to Graduate Visa status]`.
  - **Right to work:** Student Visa, eligible for the Graduate Visa (2 years full working rights). `[YOU: has the Graduate Visa been applied for or granted? Have the exact status and dates ready.]` Right-to-work evidence is checked at offer stage.
  - **Location:** based in Bristol; `[YOU: relocating to London, or commuting 3 days a week?]` Have a one-sentence, confident answer.

## 2. Timeline

| Day | Focus | Output |
|---|---|---|
| **Tue 20 (evening)** | Read this file end to end. Re-read your submitted CV and cover letter (`KaustubhSonawaneAIEngineer.docx`, `...CoverLetter.docx`). They will interview off those. | Know every line of both. |
| **Wed 21** | (a) Core HDFC stories, written as STAR bullets and said out loud (section 4). These also serve BSC on Monday. (b) Concept crash course, sections 5.1 to 5.3 (sequence/behavioural, decision processes, causal). | 6 stories timed at ≤2 min each; one-page concept notes in your own words. |
| **Thu 22** | (a) Morning: the mini-build (section 7), max 4 hours. (b) Afternoon: sections 5.4 to 5.6, the domain scenarios (section 6), gap scripts (section 8). (c) Evening: mock Q&A out loud against section 9, ideally recorded. | A notebook you can honestly say you worked through; answers to every question in section 9. |
| **Fri 23 (morning)** | No new material. Re-read sections 3, 4 and 8. Do one out-loud run of the intro and the "how would you build it" answer (section 6.1). Logistics check. | Calm, rehearsed. |

## 3. Positioning (the one idea they should leave with)

> "A production engineer who has already shipped AI into regulated financial-services workflows end to end (APIs, microservices, event-driven pipelines, CI/CD, security review), who has the ML and sequence-modelling foundations from the MSc, and who is closing the behavioural and causal modelling gap quickly."

Why this framing:
- The JD stresses **production**, saying "not just experimentation or notebooks" twice. Production delivery is your real strength, so lead with it.
- Your cover letter **already stated plainly** that you have not built behavioural models, used causal tooling, run A/B, shadow or replay validation, or shipped a PyTorch/TensorFlow model to production. **Stay consistent with that letter.** They invited you anyway, so they have priced it in; they now want to see (a) whether the production story is real and deep, and (b) whether you can reason about the modelling side and learn fast. Don't backtrack on the honesty and don't over-claim.

**90-second intro (draft, adapt in your own words):**
1. 3 years at HDFC Asset Management, a regulated mutual-fund house, as an AI Solutions / Forward Deployed Engineer. Designed and built the first GenAI systems end to end, initially just my manager and me.
2. What shipped: department-specific RAG applications and tool-calling agents (ReactJS, FastAPI microservices in Docker on AWS, LlamaIndex, Azure OpenAI and self-hosted Llama-3, pgvector), and an event-driven pipeline that turns 300+ rating-agency emails a day into structured data, saving 60 analyst hours a month.
3. Production discipline: Jenkins/GitLab CI/CD, RBAC against LDAP, working with the security team until the apps passed VAPT, and Compliance reviewing every release.
4. Then an MSc in Data Science at Bristol: LSTM and attention sequence decoders in a multi-architecture study, and a ranking tool with AstraZeneca.
5. Why here: this role takes models into live decisioning, which is exactly the bridge I've been working on, and it pushes me into behavioural and causal modelling, where I want to grow.

## 4. Evidence map: JD accountability → your story

Use these as your answer bank. Numbers allowed: **300+ emails/day, 60 analyst hours/month, 10 hours/week, 3 years**. Nothing else.

| JD asks for | Your evidence | Story hook |
|---|---|---|
| Deploy AI models into production, not notebooks | GenAI apps in production for Compliance, Client Service, Investment; FastAPI microservices (uvicorn) in Docker on AWS EC2/ECR | "Prototype → real users → iterate on feedback" |
| End-to-end AI pipelines: ingestion, features, inference, monitoring | Rating-email pipeline: shared inbox → parse (Textract first, then Azure OpenAI) → fuzzy-match company names to tracked list → daily summary + Excel in S3. Morningstar ingestion into a normalised PostgreSQL schema (fortnightly fixed income, monthly equity) | **Failure story:** an agency started sending emails as images, the Textract parser broke, you moved to Azure OpenAI, which fixed it and was more accurate. |
| Event-driven architectures | EventBridge rule at 9 AM → Lambda → SageMaker pipeline | Know this precisely; SageMaker was used **only** for this pipeline. |
| APIs and microservices integration | FastAPI microservices serving the React frontend; agents call Python functions as tools that run SQL-backed fund comparisons and generate PDF reports | "Agentic decision engine" ≈ tool-calling agent over business logic; don't oversell. |
| Agentic systems | Tool-calling agents, system-prompt guardrails, prompts versioned in Git, Compliance review | Honest: no agent framework, no formal evals. |
| CI/CD, versioning, lifecycle | One-click Jenkins + GitLab deploy to dev/prod; frontend and backend in separate repos, each with dev/prod branches and own container; prompts versioned in Git | It was **button-triggered**, two environments. Don't say "fully automated CD". |
| Security, reliability | RBAC via Python auth function against LDAP (3 tiers), department-siloed vector DBs, Security Groups limited to company private IPs, Nginx reverse proxy as one of the fixes that got the apps through VAPT | Maps well to FCA conduct rules ("due skill, care and diligence"). |
| Commercial delivery vs research | Self-hosted Llama-3 on GPU EC2 for the largest department (cost), Azure OpenAI for decision makers (quality), models switchable | Your best "balancing innovation with delivery" story. |
| Partner with product / business | Worked directly with Client Service, Compliance, Investment; Power BI migration (10 hours/week); recreated dashboards in React when Power BI licensing was too costly to scale | Also a build-vs-buy story. |
| Sequence models (LSTM, Transformers) | MSc VisionCaptioner (team project): CNN/ViT/ResNet encoders, symbolic, SBERT retrieval and LSTM decoders with/without Bahdanau attention, 5 seeds, SBERT cosine/BLEU/ROUGE-L, benchmarked against BLIP/SigLIP/commercial VLMs | Say "team project". Know how an LSTM decoder and attention work (5.1). Caveat: the VLM comparison used different protocols, so don't claim you "beat" them. `[YOU: which framework did the team use? Only name it if you're sure.]` |
| Ranking / decision scoring | CellLineSelector (co-built): per-gene desirability scores over six evidence layers, correlation weighting, exclusion veto, calibration, confidence tiers; your focus was preprocessing, scoring and the RAG layer; validated with AstraZeneca scientists | No metrics, never "led". |
| Leadership / collaboration | De facto team lead for up to 4 interns in year 3; Best Team Project 2024 (email automation) and 2025 (department RAG chatbot), internal | |

### The 6 core STAR stories (shared with BSC; prepare once on Wednesday)
1. **Department RAG apps:** built end to end, context siloed per department, model choice per department, released to real users.
2. **Rating-email pipeline + image-email failure:** event-driven production pipeline, robustness, measurable value (60 h/month).
3. **Llama-3 vs Azure OpenAI:** cost/quality trade-off, commercial judgement.
4. **Security and VAPT:** repeatedly failing, then passing; coordination with the security team; RBAC/LDAP.
5. **Stakeholders:** turning Compliance/Investment/Client Service requirements into tools; Power BI → React recreation for scale at lower cost.
6. **Leading interns / team growth:** from 2 people to two leads in the GenAI team.

## 5. Concept crash course (discussion level, mapped to insurance)

Goal: you can **reason fluently** about each item, say how you would apply it, and say plainly you haven't shipped it. Write a one-paragraph explanation of each in your own words.

### 5.1 Sequence and intent modelling
- **Markov chain baseline:** P(next state | current state) estimated from counts. Order-k chains condition on the last k events. Cheap, interpretable, a strong baseline to beat. *Insurance:* the submission lifecycle (received → triaged → referred → quoted → bound / not taken up / declined) or broker-portal event streams.
- **Hidden Markov Models:** a latent "intent" state emits observed events, e.g. a broker is "shopping around" vs "ready to bind".
- **RNN/LSTM/GRU:** process sequences step by step with gated memory (input, forget and output gates fight vanishing gradients). Input shape (batch, seq_len, features). Use the last hidden state for classification (intent) or every step for next-event prediction.
- **Attention / Transformers:** each position attends to all others (Q, K, V; scaled dot product; positional encoding; causal mask for next-event prediction). Better long-range dependencies and parallel training. SASRec-style next-item transformers are the standard for behaviour sequences. Your MSc team study used Bahdanau (additive) attention in the LSTM decoder, so be ready to explain how that differs from Transformer self-attention.
- **Intent prediction:** classify the goal or outcome from a *partial* sequence (e.g. P(bind) after 3 interactions). Metrics: accuracy@k / recall@k for next event, AUC and **calibration** for outcome probabilities (decisions need calibrated probabilities).
- **Gotchas:** leakage from future events, time-based train/test splits (never random), variable-length padding and masking, cold start for new brokers.

### 5.2 Behavioural modelling and decision processes
- **Behavioural cloning (BC):** supervised learning of a policy π(action | state) from logged expert (state, action) pairs. *Insurance:* learn how underwriters act on submissions (quote / decline / refer, price loading, terms) from historical decisions. That is effectively an **underwriter Digital Twin**.
- **BC failure mode:** covariate shift / compounding errors. The learner visits states the expert never did, so errors snowball. **DAgger** fixes this by having the expert label the states the learner actually visits.
- **Inverse RL / GAIL:** infer the *reward* the expert is optimising rather than copying actions. More robust when the environment changes.
- **Big caveats in insurance:** cloning reproduces historical **bias** (fairness and FCA Consumer Duty, "deliver good outcomes for retail customers" is one of the conduct rules in the JD pack). There is also **selective labels**: you only observe losses on risks that were bound, so outcome-based learning is biased toward past acceptance policy.
- **MDP:** states, actions, transition dynamics, rewards, discount, policy. **Offline RL** (e.g. conservative Q-learning) learns from logs without live exploration, which suits regulated settings.
- **Contextual bandits:** one-step decisions with context (which risks to prioritise, which recommendation to show). Exploration vs exploitation (ε-greedy, Thompson sampling, LinUCB). Log **propensities** so you can evaluate off-policy later.
- **"RL-inspired methods" in the JD** most likely means bandits/offline RL for decisioning, not game-playing RL.

### 5.3 Causal inference (the gap they named most clearly)
- **Why:** "Did the AI recommendation *cause* higher bind rates or better loss ratios, or did underwriters just use it on easier risks?" Correlation is confounded by who uses the tool and when.
- **Potential outcomes:** Y(1), Y(0); ATE = E[Y(1) − Y(0)]; CATE = effect for a segment (heterogeneous effects). You never see both outcomes for one unit.
- **Assumptions:** unconfoundedness (no hidden confounders given X), **positivity/overlap** (every type of unit could get either treatment), SUTVA (no interference).
- **DAGs and the backdoor criterion:** draw the graph, adjust for confounders, **never adjust for mediators or colliders**.
- **Estimators:** regression adjustment; propensity score matching / **IPW**; **doubly robust (AIPW)**, which is consistent if either the outcome model or the propensity model is right; **Double ML** (EconML `LinearDML`, `CausalForestDML`) uses ML nuisance models with cross-fitting; **meta-learners** S/T/X (CausalML) for uplift / CATE.
- **Quasi-experiments when you can't randomise:** difference-in-differences (staggered rollout by team or line of business), regression discontinuity (score thresholds), instrumental variables, synthetic control.
- **DoWhy's 4 steps:** **model** (causal graph) → **identify** (estimand via backdoor/IV/frontdoor) → **estimate** → **refute** (placebo treatment, random common cause, data-subset, unobserved-confounder sensitivity).
- **One-liner to say:** "If I can randomise, I'd A/B test. Causal inference is for when I can't, or to understand heterogeneity after the test."

### 5.4 Validating deployed models (JD: offline replay, A/B, shadow, simulation)
- **Offline replay:** run the new model/policy over historical logged events and compare its decisions with what happened. For policies, use **off-policy evaluation** (replay method, IPS, doubly robust), which needs logged propensities.
- **Shadow deployment:** the model runs on live traffic and its outputs are logged but not acted on. You get real-world latency, errors and agreement with humans at zero business risk. Your natural first production step.
- **A/B test:** randomise units (brokers, underwriters, submissions; watch for interference), pre-register the primary metric, a power/sample-size calculation, guardrail metrics (loss ratio, complaint rate, latency), and run time. **Canary** = small rollout percentage with automatic rollback.
- **Simulation:** use the Digital Twin as a sandbox to test policy changes before they touch real customers.
- **Sequence to propose:** offline replay → shadow → canary / A/B → full rollout with monitoring. Say this unprompted when asked how you'd ship a model.

### 5.5 Digital Twins
- A virtual model of a real entity or process (an underwriter, a broker, a portfolio, the submission pipeline), kept in sync with real data and used to **simulate "what if"** scenarios: new appetite rules, pricing changes, auto-decline thresholds, workload routing.
- Built from the pieces above: state models (5.1), behavioural policies (5.2), causal structure (5.3) so interventions are simulated correctly, and validated by replay against history (5.4).
- Ask them what *their* twin represents (section 10).

### 5.6 Production ML / MLOps vocabulary to have ready
- Model registry and versioning (MLflow), data + model + prompt versions together, reproducible training.
- Serving: FastAPI/Docker (your experience), batch vs real-time, latency budgets.
- Monitoring: data drift (PSI, KS test), prediction drift, performance once labels arrive (delayed labels are normal in insurance), alerting, retraining triggers.
- Explainability for regulated decisions: SHAP / feature attribution, reason codes for underwriters, audit trails. Human-in-the-loop for consequential decisions.
- **PyTorch basics** (in case of a light technical question): `Dataset`/`DataLoader`, `nn.Module`, forward → loss → `loss.backward()` → `optimizer.step()` → `optimizer.zero_grad()`; `model.eval()` + `torch.no_grad()` at inference; `nn.LSTM(input_size, hidden_size, batch_first=True)`.

## 6. Domain scenarios (practise out loud)

Aventum is a specialty (re)insurance group: MGAs underwrite on behalf of capacity providers, and brokers bring them submissions. Likely ground for "behavioural intelligence": **underwriter decision support, submission triage, broker behaviour, pricing/appetite, claims**. These are hypotheses, so frame them as questions in the interview.

### 6.1 Worked answer: "How would you build a model that predicts which submissions an underwriter will quote, and put it into production?"
1. **Clarify:** the decision it supports (prioritise the queue? suggest quote/decline?), the user (underwriters), the success metric (time to quote, hit ratio, loss ratio), constraints (explainability, FCA, latency).
2. **Data:** submission fields, broker, line of business, history of underwriter actions (the event sequence), outcomes. Time-based split. Watch leakage (fields filled in after the decision).
3. **Baselines first:** rules/appetite, then gradient boosting on tabular features, then a sequence model (Markov → LSTM/Transformer) if the interaction history adds lift. Calibrate the probabilities.
4. **Behavioural framing:** this is behavioural cloning of underwriter decisions, so discuss bias, selective labels and covariate shift (5.2).
5. **Serve:** a FastAPI microservice in Docker behind the submission workflow, triggered by a "submission received" event (your EventBridge→Lambda pattern), with reasons/SHAP returned.
6. **Validate:** offline replay → shadow alongside underwriters (measure agreement) → A/B on queue prioritisation → causal read-out of the effect on time-to-quote and bind rate (5.3, 5.4).
7. **Operate:** CI/CD, model registry, drift and performance monitoring with delayed labels, human override always, an audit log.

### 6.2 Other prompts to rehearse (2 minutes each)
- "The business rolled out an AI triage tool to half the underwriting teams last quarter. How do you tell whether it worked?" → diff-in-diff / DoWhy, confounders, refutation (5.3).
- "How would you build a Digital Twin of a broker?" → event sequences, intent HMM/LSTM, simulator, replay validation.
- "Your model looks great offline but underwriters ignore it." → shadow/agreement analysis, explainability, user research. Your HDFC "release to real users and iterate" story fits here.
- "An agent makes decisions in a workflow. How do you keep it safe?" → tool permissions, human approval for consequential actions, logging, guardrails, your Compliance-review experience.

## 7. Mini-build (Thursday morning, at most 4 hours, optional but high value)

Purpose: turn "I've read about it" into "I worked through it this week", **which you must frame exactly that way.** It is not experience; it shows you learn quickly.

1. **Causal (2 hours):** in a notebook, use DoWhy on the Lalonde job-training data (ships with DoWhy / `causaldata`). Build the graph → identify → estimate with propensity weighting and EconML `LinearDML` → run two refuters. Compare with the naive difference in means and explain the gap.
2. **Sequence (1.5 hours):** on any public event/session dataset (or a small synthetic submission-lifecycle generator), fit a first-order Markov next-event baseline and a small PyTorch LSTM, and compare accuracy@3 on a time-based split.
3. Push it to GitHub (an `aventum-prep` or `causal-sequence-notes` repo). Mention it only if the conversation reaches the gaps, e.g. "Since applying I've been working through DoWhy and EconML on the Lalonde data. What struck me was how much the naive estimate differed..."

Do **not** add these to the CV or `EXPERIENCE.md` as experience. Afterwards, consider whether to log them as partial progress against GAPS A10/A11.

## 8. Gap-handling scripts

Structure: **acknowledge plainly → nearest real evidence → what I've done since → how I'd ramp in the role.** Keep each under 45 seconds and never apologise twice.

- **Causal inference:** "I haven't applied DoWhy or EconML to real business data. My nearest work is measuring impact the practical way, e.g. the 60 analyst hours a month from the email pipeline, which is a before/after, not a causal estimate. This week I worked through DoWhy and DML on a public dataset, and I understand the confounding problem you'd have measuring an AI tool's effect on underwriting. In the role I'd pair with whoever owns experimentation and start on a rollout we can analyse as a diff-in-diff."
- **Behavioural modelling / imitation learning / RL:** "Not in production. I understand behavioural cloning as supervised learning of a policy from logged decisions, and its compounding-error and bias problems. My sequence-modelling base is the LSTM and attention work from the MSc. Where I'm strong is the part that usually breaks these projects: getting the model into the workflow, behind an API, safely."
- **PyTorch/TensorFlow in production:** "My production work was Python services and GenAI. My deep learning is from my degrees. The gap is the training-pipeline side, not the serving or deployment side, which I've done many times."
- **A/B, shadow, replay:** "At HDFC quality came from user feedback, Compliance review and system-prompt guardrails, not controlled experiments. I'd introduce shadow mode as the first step for any model here, because it's zero-risk and gives real evidence."
- **Insurance domain:** "No insurance experience, but regulated financial services: an asset manager, a Compliance department reviewing every release, credit-rating data. The disciplines carry over."

## 9. Likely questions (prepare answer skeletons)

**If it's a talent/screening-style conversation (possible for round 1):**
- Walk me through your CV / why the MSc / why leave HDFC? (Planned move to study; left Jul 2025.)
- Why Aventum? Why insurance? → production AI with real decisions attached; a group that has grown fast (about 10,000% in a decade per their CSOP booklet) and is investing in Digital Twins and agentic systems; "Dare to Discover" fits a role that's partly new ground for you.
- Salary, notice, right to work, location (section 1). Hybrid 3 days and 8:30 to 5.
- What do you know about us? → specialty (re)insurance group, Rokstone underwriting and Consilium broking, London market, mission "the most inspiring specialty (re)insurance group in the world", 93% say they can be themselves at work, CSOP for all eligible staff.

**Technical / hiring manager:**
- Biggest production system you built, and what you'd do differently. (RAG apps: today you'd add an eval set, tracing and permission-aware retrieval as standard.)
- Tell me about a time something broke in production. (Image emails → Textract parser broke.)
- How do you take a model from notebook to production? (Section 6.1, steps 5 to 7.)
- How would you monitor a model where labels arrive months later?
- Explain LSTM vs Transformer for sequence prediction. Explain attention.
- What is behavioural cloning and when does it fail?
- How would you measure the impact of an AI decision tool without an A/B test?
- Trade-off between innovation and delivery. (Llama-3 vs Azure.)
- Working with non-technical stakeholders; disagreement with a stakeholder. `[YOU: pick a real example from Compliance or Investment.]`
- Leading the interns: how you delegated, reviewed and unblocked.

**Behavioural (Aventum values: challenge the status quo, continuous improvement, collaboration):**
- A time you challenged the way something was done. (Power BI licensing → React recreation; Textract → Azure OpenAI.)
- A time you learned something fast. (Early GenAI at HDFC as one of two people; MSc; this week's causal work.)
- A time you got feedback and changed course. (Releasing to users and iterating.)

## 10. Questions to ask (pick 3 or 4)
1. What does the Digital Twin represent today: underwriters, brokers, portfolios, or the submission workflow? How far along is it?
2. Which decisions are the agentic decision engines meant to make or support first, and where does a human stay in the loop?
3. What data is available for behavioural modelling: event logs from the digital suite, underwriting decisions, claims?
4. How is the AI team structured (ML engineers, software engineers, product) and how does it work with the underwriting businesses?
5. How do you currently validate models: is there shadow or experimentation infrastructure, or would this role help build it?
6. What would a successful first 6 months look like?
7. What does stage 2 look like (case study or technical exercise)?
- *Hold until offer stage unless they raise it:* visa sponsorship after the Graduate Visa. (Rokstone Group Ltd is on the Home Office sponsor register; the hiring entity, Aventum Group Management Services Ltd, did not appear in the copy in `LiscensedSponsors.csv`.)

## 11. Day-of checklist
- [ ] Outlook invite accepted; know the interviewer names and look them up on LinkedIn.
- [ ] Video: camera, mic, Teams tested, quiet room, CV and cover letter open, this file's sections 3, 4 and 8 on a second screen. In person: printed CV, travel buffer.
- [ ] Water, pen and paper for diagrams (draw the 6.1 pipeline if asked to whiteboard).
- [ ] Keep answers to 2 minutes, then offer to go deeper ("Happy to go into the architecture if useful").
- [ ] Close with a one-line summary of why you fit plus one sincere question.
- [ ] Afterwards: a short thank-you to Lucy the same day. Note the questions asked in `interview/aventum/notes.md` (useful for stage 2 and for BSC on Monday).

## Honesty guardrails (from `cv/EXPERIENCE.md`)
- No formal evals, LLM-as-judge or golden datasets at HDFC. No fine-tuning. No MCP. No SSO/OAuth (it was **LDAP**).
- SageMaker = the email pipeline only. S3 = that pipeline's Excel output only. CloudFormation = used security-team templates, never authored.
- CI/CD = one-click Jenkins button, dev and prod only. ExpressJS = development phase only.
- "De facto team lead", "up to 4 interns". Never a formal title.
- Don't quote "below 1%" security figures, user/document counts, or CellLineSelector metrics. Both MSc projects are team projects.
- Llama-3 served Client Service only; the rest used Azure OpenAI. Each department had its own vector DB.

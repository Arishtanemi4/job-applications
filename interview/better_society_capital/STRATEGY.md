# Better Society Capital: AI Full Stack Engineer, Round 1 Interview Strategy

## 1. Snapshot

| | |
|---|---|
| Role | AI Full Stack Engineer, Investment department, reports to the Head of AI. The AI team is **two people** (Head of AI + you), sitting between Investment and a Transformation team of about 10 FTEs. |
| Pay / place | £50,400 to £65,800. Hybrid, Old Street (EC1Y), 40 to 60% in the office. |
| Interviewer | **Nicholas (Nick) Andreou, Head of AI** (NAndreou@bettersocietycapital.com). An internal hire from the investment team: strong on BSC and investment, "intermediate" on technical foundations, statistics, GenAI and agents. He wants a technical partner who complements him. |
| When | **Monday 26 Oct 2026. 30 minutes, online.** (He wants all round-1s done by Fri 30 Oct.) |
| Format | (1) **CV deep-dive**, then (2) a **live problem statement** "to think through together how we might approach it as an AI team". He says there's nothing to prepare in advance, which means he is testing how you think, not what you memorised. |
| Next rounds | R2 virtual (w/c 16 Nov), R3 **in person** (w/c 23 Nov), per the JD. |

### Open actions
- [ ] **Confirm the slot is booked** through his booking link for Monday, and that the calendar invite has a video link. Note the exact time here: `[YOU: time]`.
- [ ] Find and read the **Stanford paper** linked in the JD ("Creating our prompt and skill library with a particular focus on impact assessment (you can read about one of our experiments in this paper published by Stanford)"). Open the JD link on the Applied posting or search "Better Society Capital Stanford impact assessment LLM". Referring to it specifically is the single best signal that you did your homework.
- [ ] Skim bettersocietycapital.com: mission, asset classes (property, debt, venture, outcome contracts), recent news, anything on their AI work. Look up Nick on LinkedIn.
- [ ] **Right to work:** the JD needs existing right to work and says BSC cannot sponsor. Your answer: Student Visa now, eligible for the Graduate Visa (2 years full working rights). `[YOU: status of the Graduate Visa application.]` Don't raise sponsorship in R1. (FYI: Better Society Capital Ltd *is* on the Home Office sponsor register in `LiscensedSponsors.csv`, which may matter for a conversation much later, not now.)

## 2. Timeline (after Aventum on Friday)

| Day | Focus | Output |
|---|---|---|
| **Wed 21 / Thu 22** | The 6 core HDFC STAR stories you're preparing for Aventum (see `interview/aventum/STRATEGY.md` §4) serve both interviews. Only the framing differs (section 4 below). | Nothing BSC-specific yet. |
| **Fri 23 (evening)** | Decompress from Aventum, then 1 hour: Stanford paper, BSC website, re-read the BSC JD, CV and cover letter (`KaustubhSonawaneAIFullStackEngineer.docx`, `...CoverLetter.docx`). | Notes on 3 things you'll reference. |
| **Sat 24** | **Weekend build** (section 6), about 5 to 6 hours. | A small public repo you can honestly talk about. |
| **Sun 25** | Morning: re-frame the stories for BSC and time them (section 4). Afternoon: **problem-solving dry runs** (section 5); do all 5 JD projects out loud, 5 to 7 minutes each, ideally with someone playing Nick. Evening: landscape refresh (section 7). | Can run the framework on any prompt without notes. |
| **Mon 26** | Light warm-up only: intro out loud twice, framework card, questions for Nick. | |

## 3. What Nick is scoring (from the essential criteria)

| Essential criterion | What to show in 30 minutes |
|---|---|
| Technical and leadership experience; significant technical decisions; ownership of complex work | Architecture choices at HDFC (siloed vector DBs, model allocation, RBAC), leading interns |
| Shipped technical products users depend on, some AI/agentic | Department RAG apps and tool-calling agents in daily use; the rating-email pipeline |
| Technical advisor / thinking partner on build vs buy, vendors, architecture | Llama-3 vs Azure OpenAI; Power BI licensing → React recreation; Textract → Azure OpenAI |
| Appetite for learning, staying current | Building with LLMs since the early GPT-3.5 tooling, the MSc, Claude Code, **this weekend's MCP build** |
| Commitment to improving lives in the UK | Swindon fuel-poverty hack + your genuine reason (section 9) |

Also implicit, because it's a "Swiss army knife" role in a team of two: **pragmatism** (right level of rigour for the problem), **communicating with non-technical people**, and **comfort working solo**.

## 4. CV deep-dive (about 12 to 15 minutes)

### 90-second intro (adapt in your own words)
1. Three years at HDFC Asset Management, a mutual fund house, as an AI Solutions / Forward Deployed Engineer: the person who takes an AI tool from a business team's problem to something they use every day.
2. Year 1 it was my manager and me. I designed and built the first GenAI applications end to end: React frontend, FastAPI microservices, RAG with LlamaIndex over Azure OpenAI and a self-hosted Llama-3, pgvector, tool-calling agents for fund comparisons. By year 3 I was the de facto lead for up to four interns.
3. Alongside that, AI-assisted data pipelines, e.g. turning 300+ rating-agency emails a day into structured updates for analysts, saving 60 analyst hours a month.
4. Then an MSc in Data Science at Bristol, with a dissertation tool built with AstraZeneca.
5. Why this role: a small AI team embedding AI across an organisation is exactly the forward-deployed work I enjoy, and I want it to serve social impact in the UK.

### Stories, re-framed for BSC (≤2 minutes each; have 5, expect to use 3)
| Story | BSC framing / criterion |
|---|---|
| **Department RAG apps** | *Context engineering:* each department had its own documents and access rules, so each got its own pgvector database, scoping what the assistant could see. GPT-3.5 and Llama-3 also struggled to separate similar content across departments. **Reflection to offer:** "Today I'd look at a single store with permission-aware metadata filtering plus an eval set to prove retrieval quality. Back then siloing was the pragmatic, safe choice." |
| **Llama-3 vs Azure OpenAI** | *Cost modelling and vendor choice:* self-hosted Llama-3 on a GPU EC2 instance for Client Service (the largest department) to control cost; Azure OpenAI's stronger outputs kept for decision makers; models switchable. Be honest that it was a reasoned decision, not a formal cost model. |
| **Power BI → React recreation** | *Build vs buy:* Power BI licences were too costly to scale to the nationwide client-service team, so the dashboards were recreated in the React app, opening the data to the wider organisation at lower cost. (No user numbers or savings figures.) |
| **Rating-email pipeline** | *AI in data pipelines (ingestion, verification):* parse → fuzzy-match against tracked companies → daily summary. **Iteration:** an agency switched to image emails, the Textract parser broke, you moved to Azure OpenAI, which was robust and more accurate. Maps directly to "working on data pipelines with AI with our data team". |
| **Security / IT interface** | *Working with IT on permissions, auth, security:* RBAC via a Python auth function against LDAP (3 tiers), Security Groups limited to private IPs, coordinating with the security team on port whitelisting, an Nginx reverse proxy as one of the fixes that got the apps through VAPT, Compliance review of every release. |
| **Stakeholders + interns** | *Non-technical stakeholders, leadership:* gathering requirements from Compliance, Investment, Client Service; demoing; turning feedback into releases; leading up to 4 interns. |
| **CellLineSelector** (if asked about the MSc) | Co-built with the team; your focus was preprocessing, the scoring algorithm and the RAG layer (which you designed); refined with AstraZeneca scientists' feedback. A domain-expert-in-the-loop story, similar to working with BSC's impact team. |

Prompts and skills as products: say how you treated prompts at HDFC: system-prompt guardrails, **every prompt change versioned in Git**, Compliance review before release, iteration on user feedback. Then the honest bit: "no formal eval datasets or LLM-as-judge; building that rigour into your prompt and skill library is what I'd want to own" (consistent with your cover letter).

## 5. Live problem-solving (about 15 minutes): the core of the interview

### How to behave
- It's "**think through together as an AI team**", so treat Nick as a colleague. **Ask 2 or 3 clarifying questions first**, think out loud, check in ("Does that match how the team works today?"), and build on his answers.
- Explain technical choices in plain language (he's intermediate technically). Offer the trade-off, then a recommendation.
- Start small: **v0 in days with what they already have (Claude + Microsoft 365)**, then grow. In a team of two, pragmatism beats a grand architecture.
- Name risks without being asked: data access and permissions, hallucination on investment-relevant facts, bias, GDPR, cost.
- Watch the clock: aim to reach a concrete proposal and a "how we'd know it worked" by minute 12.

### The framework (memorise as 8 words: **Users, Workflow, Data, Build/Buy, v0, Evals, Safety and Cost, Adoption**)
1. **Users and outcome:** who uses it, what decision or task, what "good" looks like (time saved, better decisions, coverage)?
2. **Current workflow:** how is it done today, where is the pain, what volume?
3. **Data and context:** where does the information live (SharePoint, Fabric, CRM, email, external sources)? What does the model need to see to do the task (context engineering)? Permissions?
4. **Build vs buy ladder:** (a) a Claude project / skill / prompt in the existing Claude rollout → (b) an existing or new **MCP connector** to the data → (c) automated flow (Power Automate trigger, or a scheduled agent / Claude Managed Agents) → (d) a custom app or agent only if needed. Prefer the lowest rung that solves it.
5. **v0 in a week:** the smallest thing a real user can try; plan the next iteration from their feedback.
6. **Evals:** a golden set of 20 to 50 real past cases with expert labels; a scoring rubric; LLM-as-judge calibrated against human scores; regression tests whenever a prompt or model changes; track agreement with experts.
7. **Safety and cost:** human-in-the-loop for anything that influences investment or outreach; guardrails; SSO / least-privilege access; secrets in a vault, not in prompts; audit logs; data residency. Cost: tokens per item × items per month × price per token; caching and model tiering (cheap model for extraction, frontier model for judgement), like the Llama-3/Azure split.
8. **Adoption:** training through the AI Academy, a champion in the team, measure usage, iterate.

### Pre-worked sketches of the JD's live projects (likely sources of the problem statement)

**A. Automating screening in the venture pipeline**
- Clarify: inbound volume, what the screening criteria are, who decides, what a "miss" costs.
- v0: a Claude skill containing BSC's screening rubric (investment criteria + impact thesis) that reads a pitch deck/application from SharePoint and returns structured fields (sector, stage, ask, impact thesis, evidence) and a first-pass fit assessment **with citations to the deck**.
- v1: a Power Automate trigger on new submissions → extraction → a row in Fabric → summary posted to the team.
- Evals: back-test on past screening decisions (agreement rate; **false negatives matter most**, so don't auto-reject); inconsistency checks by running twice.
- Risks: bias against unconventional founders (anonymise, audit by segment), prompt injection inside uploaded decks, over-trust. Human decides.

**B. Evaluating/building MCP connectors for Claude**
- Evaluation criteria: first-party vs community connector, **auth model** (Entra ID / OAuth delegated permissions so it respects SharePoint access), read vs write scopes, audit logging, data residency, maintenance, **prompt-injection risk from tool outputs**, latency and token cost.
- Method: a task suite (10 to 20 real tasks per connector), success rate, failure analysis; start read-only.
- Build vs buy: use first-party remote connectors where they exist; build a small custom MCP server only for internal systems without one (e.g. a Fabric dataset or a CRM view), exposing a few narrow, well-described tools rather than raw SQL.
- Your hook: the weekend build (section 6) and HDFC's agents calling Python functions as tools, the same pattern MCP standardises.

**C. Agentic flow to discover new investors and tailor outreach (engagement team)**
- Clarify: what a good-fit investor is (type, ticket size, impact themes), the CRM, the volume, who sends.
- Flow: source candidates (Companies House, Charity Commission, 360Giving grant data, public reports/news) → entity resolution and de-duplication against the CRM (your fuzzy-matching experience) → fit scoring with reasons → draft outreach grounded in cited facts → **human review and send**.
- Risks: GDPR for individuals' data (lawful basis, legitimate-interest assessment, no scraping that breaks terms of service), hallucinated facts in emails (require citations, a check step), tone.
- Evals: the engagement team rates lead quality; track reply rates later.

**D. Prompt and skill library for impact assessment**
- Treat each skill as a product: owner, purpose, inputs/outputs, version (Git), changelog, test set, eval scores, status (draft / approved / deprecated).
- Impact assessment specifics: align rubrics with frameworks BSC uses (e.g. the five dimensions of impact: what, who, how much, contribution, risk; confirm what BSC actually uses); calibrate against expert assessors; measure LLM–human agreement as you would inter-rater agreement; watch for confident but unsupported claims; require evidence citations.
- Connect to the Stanford paper's findings (read it first).
- Distribution: organisation-wide Claude skills; feedback loop from users; AI Academy sessions on using them.

**E. AI in data pipelines with the data team (Fabric)**
- Example: ingesting portfolio/fund-manager reports (PDF/Excel) into Fabric.
- Flow: extract to a defined schema → validation rules (types, ranges, totals reconcile) + LLM verification + confidence score → **exceptions queue for humans** → load to the lakehouse → lineage/audit.
- Your direct analogue: the rating-email pipeline (unstructured → structured, matched to a reference list, daily delivery, and the switch from Textract to an LLM when the input format changed). Be honest that you haven't used Fabric; your pipelines were PostgreSQL / AWS.

### Curveballs to have a 1-minute answer for
- **"Staff are pasting sensitive data into consumer ChatGPT. What do we do?"** → an approved enterprise tool (they have Claude), a clear data policy, training via the AI Academy, make the approved path easier than the workaround.
- **"What memory system should our agents use?"** (it's in the JD) → start simple: retrieval over curated notes / per-project memory files with provenance and timestamps; then structured memory with explicit write rules, corrections, forgetting (GDPR) and permissions; avoid an opaque vector-store dump; evaluate whether memory actually improves task success.
- **"Build or buy an AI tool for X?"** → buy/configure when it's commodity and the vendor meets the security bar; build when it's core to BSC's edge (impact assessment) or the data is unique; think about lock-in, cost at scale, exit path.
- **"How would you estimate monthly cost?"** → worked example out loud: e.g. 200 documents × 20k tokens in + 1k out × price per million tokens; add retries and evals; levers: prompt caching, batching, model tiering.
- **"How do you decide what to automate first?"** → value × feasibility × risk; quick wins that build trust; pick a workflow with a willing champion.

## 6. Weekend build (Saturday, about 5 to 6 hours, high ROI)

Your cover letter said you haven't built MCP connectors or formal evals. Closing a small version of both before Monday gives you a true, specific answer, and it demonstrates the "appetite for learning" essential criterion.

1. **MCP server (about 3 hours):** using the official Python MCP SDK, expose 2 or 3 narrow tools over a **public UK social-impact dataset**: e.g. 360Giving GrantNav (UK grant data) or the Companies House API (free key). Example tools: `search_grants(theme, region)`, `get_organisation(company_number)`. Connect it to Claude Desktop or Claude Code and run some real queries. Note what was hard (tool descriptions, auth, response size, errors).
2. **One Claude skill (about 1 hour):** e.g. "first-pass impact screen", with a short rubric and output format, used together with the MCP tools.
3. **Tiny eval (about 1.5 hours):** 15 to 20 hand-labelled examples; a script that runs the skill and scores it with exact-match fields + an LLM-as-judge on the rubric; compare the judge with your own labels; change the prompt once and show the before/after.
4. Push to GitHub with a short README (what it does, what you learned, what you'd do next).

How to mention it: "After applying I wanted hands-on MCP experience, so this weekend I built a small MCP server over 360Giving data and a skill with a basic eval. What I learned was..." **Frame it as a weekend learning build**, never as production experience. Don't add it to the CV or `EXPERIENCE.md` unless you decide to later (it would partially close GAPS S3 and S1).

If Saturday runs short, cut the eval to 10 examples. Don't cut the MCP server; it's the one Nick's team uses.

## 7. Landscape refresh (Sunday evening, for confident conversation)

The JD wants someone who can "make confident decisions", so be able to discuss each of these in 30 seconds:
- **How transformers work:** tokens, embeddings, self-attention, next-token prediction, context window. (Your MSc team study used Bahdanau attention in its LSTM decoders.)
- **RAG vs long context vs fine-tuning:** when each wins (fresh/private data → RAG/connectors; stable style/format/narrow task → fine-tuning; small corpora → long context). You haven't fine-tuned; say so if asked.
- **Embeddings and retrieval:** chunking, hybrid keyword + vector search, reranking, retrieval evals.
- **Interpreting benchmarks:** contamination, the gap between benchmark and your task, why your own eval set matters most.
- **Current model landscape and pricing:** check the current frontier models from Anthropic, OpenAI and Google plus leading open-weight models, and their per-million-token prices, the week before. Know rough tiers (frontier / mid / small) and when to use each.
- **Anthropic products:** Claude apps (projects, skills, connectors), **Claude Code** (you use it), **Claude Cowork**, **Managed Agents**, MCP. Spend 30 minutes on the Anthropic docs/news for Cowork and Managed Agents so you can say what each is for.
- **Microsoft side:** Graph API (one API over M365 data, Entra ID auth, delegated vs application permissions), SharePoint, Power Automate (triggers + connectors), Fabric (lakehouse/OneLake, data pipelines). Read a one-page overview of each; you have no hands-on experience, so say so.
- **Guardrails:** input/output filtering, structured outputs with validation (your Wingman project validates LLM JSON with Pydantic, repairs and caches it, which is a good example), human approval steps.

## 8. Gap-handling scripts (≤40 seconds each)
- **MCP:** "I hadn't built one when I applied. My HDFC agents called Python functions as tools, which is the pattern MCP standardises, and this weekend I built a small MCP server over [dataset]."
- **Formal evals:** "At HDFC evaluation was user feedback, Compliance review and versioned prompts, with no golden datasets. I'd put that in from day one here; I've just built a small LLM-as-judge eval to get hands-on."
- **Microsoft Fabric / Graph / SharePoint / Power Automate:** "My cloud work was AWS and Azure OpenAI. I've worked closely with IT and security teams on permissions and access before, and I'd learn the Microsoft stack with your IT team. It's the same concepts: identity, scopes, connectors."
- **Impact investing domain:** "My finance experience is a mutual fund house, working with investment analysts and credit-rating data. I'd lean on the investment team the way I leaned on analysts at HDFC, and the impact-assessment work is the part I'm most keen to learn."

## 9. "Why BSC?" and commitment to the UK

This is an **essential criterion**, and BSC's application guidance says authentic, personal answers score best. Write your own in your own words:
- `[YOU: the genuine reason social impact in the UK matters to you; a specific moment, community or experience. 3 or 4 sentences.]`
- Evidence: the **Swindon Borough Council Fuel-Poverty Hack** (a household and neighbourhood fuel-poverty analysis tool); hackathon habit (Rolls-Royce Derby 4th, Encode 2nd, Lloyds-sponsored Datathon 3rd), which also shows you could help **run BSC's hackathons** for the AI Academy.
- Why this role: an organisation-wide AI transformation from the ground up, in a two-person team with real ownership, close to investment decisions that affect people's lives.
- **Citizenship activity:** pick one you'd genuinely do (e.g. help organise a social, or run an AI hackathon).

## 10. Questions for Nick (pick 2; there will be little time)
1. What's the most important decision the Technical Design Authority has in front of it right now?
2. How are prompts and skills evaluated today, and what would you want the eval setup to look like in 6 months?
3. Of the Innovation Lab projects, which is most urgent, and what's blocked it?
4. How mature is the Fabric setup, and how do the AI and data teams split the pipeline work?
5. What does success look like for this hire at 6 months?
6. What did the Stanford experiment teach you about using LLMs for impact assessment? (Only if you've read it, and refer to something specific.)

## 11. Day-of checklist
- [ ] Video link tested, camera/mic, quiet room. CV, cover letter, this file's sections 4 and 5 (framework card) open on a second screen.
- [ ] Pen and paper. In the problem section, sketch the flow as you speak, and offer to share your screen with a quick diagram if useful.
- [ ] **Timebox:** intro 90 seconds; answers ≤2 minutes; leave about 3 minutes for your questions. If he's running long, say "Conscious of time, the short version is..."
- [ ] Ask clarifying questions before solving. Summarise the proposal in 3 sentences at the end of the problem section.
- [ ] Afterwards: a brief thank-you email to Nick the same day, referencing one point from the problem discussion. Log the problem statement and your approach in `interview/better_society_capital/notes.md` for round 2.

## Honesty guardrails (from `cv/EXPERIENCE.md`)
- No formal evals, LLM-as-judge or golden datasets at HDFC. No fine-tuning. No MCP at HDFC. Authentication was **LDAP**, never SSO or OAuth.
- Each department had its own vector DB. Llama-3 served Client Service only; the rest used **Azure OpenAI**.
- CI/CD = a one-click Jenkins deploy, dev and prod only. CloudFormation = used security-team templates only. S3 = that pipeline's Excel output only.
- "De facto team lead", "up to 4 interns". Best Team Project = an internal recognition (2024 email automation, 2025 RAG chatbot).
- Numbers allowed: 300+ emails/day, 60 analyst hours/month, 10 hours/week, 3 years. No user, document or cost-saving figures.
- Wingman's login is demo-grade and its photo scores are LLM-judged, so use it only for the Pydantic validation / rate-limit design points.
- Both MSc projects are team projects; CellLineSelector is "co-built", never "led".

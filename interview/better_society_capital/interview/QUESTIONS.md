# Likely technical questions: BSC AI Full Stack Engineer R1

How to use: say the **30-second answer** out loud first, then go deeper only if Nick asks. He is "intermediate" technically, so lead with plain language, then name the technique. Every answer has a **Your hook** line: the honest link to your experience. Honesty limits (from `cv/EXPERIENCE.md`): no formal evals or LLM-as-judge at HDFC, no fine-tuning, no MCP at HDFC, LDAP not SSO/OAuth, no Fabric or Microsoft stack. The weekend build is a learning build (15 cases, 4 labels yours and 11 Claude's).

Contents: A Hallucinations · B RAG evaluation · C Improving RAG · D LLM fundamentals · E Evals, prompts and skills · F Agents, MCP, memory · G Security and governance · H Cost and build-vs-buy · I Adoption and stakeholders · J Behavioural · K Questions about Nick's article

---

## A. Hallucinations

### A1. How do we control AI hallucinations?
**30 seconds.** You can't remove them, so you design so that a wrong answer is rare, visible and cheap. Four layers: (1) **ground** the model in the real source (retrieval, or paste the document in); (2) **constrain** it (instructions to say "not stated", fixed output formats, citations); (3) **verify** (check quotes against the source, a second model or a rule checks claims); (4) **put a human on anything that matters**, and measure the hallucination rate so it isn't a feeling.

**Deeper.**
- *Why they happen:* the model predicts plausible text, not true text. It has no built-in "I don't know". Gaps in what it was trained on, vague questions and poor retrieved context all make it worse.
- *Two kinds:* **intrinsic** (contradicts the source you gave it) and **extrinsic** (adds something not in the source, which may or may not be true). The second is harder to catch.
- *Ground it:* RAG or direct document input; low temperature for factual tasks; put the source before the question.
- *Constrain it:* "answer only from the document; if it is not there, say 'not stated'"; structured JSON with required fields; require a **quote per claim**.
- *Verify it:* (a) deterministic check that every quote appears in the source, (b) claim-level checking: split the answer into claims and ask a second model whether the source supports each one (NLI-style or LLM judge), (c) tools for arithmetic and lookups instead of "mental maths", (d) self-consistency: run twice and flag disagreement.
- *Process:* human review for anything influencing investment or outreach, an exceptions queue, logging, and a golden set to track the rate over time.
- *What doesn't work:* "do not hallucinate" in the prompt on its own; trusting a confident tone; asking the model "are you sure?" (it often flips or doubles down).

**Your hook.** At HDFC: system-prompt guardrails, answers from the department's own documents, every prompt versioned in Git, Compliance review. No formal measurement. In the weekend build: verbatim-quote check (100% of quotes were in the record), a judge model that caught 4 of 4 planted fabrications, and v2's "intended, not achieved" rule after the judge flagged outcome wording that overclaimed.
**Tie to Nick's article.** They estimated 10 to 20% of AI assessments had hallucinations and it sometimes took 2 to 3 follow-ups before the AI admitted a mistake. Good line: "That's why I'd want the hallucination rate measured, not estimated."

### A2. How would you measure a hallucination rate?
Take a golden set of real cases, run the system, and have an expert (or a calibrated judge checked against an expert) mark each output as supported or not **claim by claim**. Report the rate with the sample size. Slice it by case type (the article found worse results for early-stage companies with little public data). Re-run on every prompt or model change.
**Your hook.** Planted-error test in the build: insert a known fabrication and check the judge flags it, which tests the judge before you trust it.

### A3. The model sounds confident but is wrong. What do you do?
Confidence in the text is not evidence. Make evidence explicit (citations, quotes), show the source next to the claim so a reviewer can check in seconds, and calibrate: if the model's own confidence score is used, check it against outcomes first. For high-stakes fields, use extraction with validation rules (totals reconcile, dates in range) instead of free text.

### A4. When is a hallucination acceptable?
When the cost of a wrong answer is low and a human is going to look anyway (brainstorming outreach angles, summarising a long report to decide whether to read it). Not when it feeds an investment view or an email to an external party without review. It's a risk-tiering question: low, medium, high impact, with controls for each tier.

---

## B. Evaluating RAG systems

### B1. How do we evaluate a RAG system?
**30 seconds.** Split it in two and measure each part, then the whole. **Retrieval:** did we fetch the right passages? **Generation:** given those passages, was the answer faithful and useful? Then **end to end:** does it give the right answer on real questions? You need a **golden set** of real questions with expert-approved answers and the passages that support them.

**Deeper.**
- **Retrieval metrics** (need to know which passages are relevant for each question): **recall@k** (is the right passage in the top k?), **precision@k**, **MRR** (how high is the first right result?), **nDCG** (rewards putting the best ones first). Recall@k is the one to watch first: if the right passage isn't retrieved, nothing downstream can fix it.
- **Generation metrics:** **faithfulness / groundedness** (every claim supported by the retrieved context), **answer relevance** (does it answer what was asked), **completeness**, **citation accuracy** (do the cited passages actually support the claim).
- **The "RAG triad"** (TruLens) and **Ragas** metrics are the common frameworks: context relevance / context precision and recall, faithfulness, answer relevance. Use them as ideas; the labels still have to be right for your domain.
- **End to end:** answer correctness against expert answers; **abstention** (does it say "not found" when the answer isn't in the data?); **latency and cost per query**.
- **Building the golden set:** 30 to 100 real questions from users, with expert answers and source passages; add the hard ones (ambiguous, multi-document, not-in-corpus). Keep a held-out part you don't tune on.
- **LLM-as-judge for scale:** useful, but it has biases (prefers longer answers, its own style, the first option shown). Calibrate it against human labels (agreement, Cohen's kappa) and test it with planted errors before trusting it.
- **Online:** thumbs up/down, "show sources" clicks, escalation rate, and sampled human review of live traffic.
- **Regression testing:** rerun the golden set on every change to chunking, embeddings, prompt or model; don't ship if recall@k or faithfulness drops.

**Your hook.** The weekend build is an eval for a skill, not RAG, but it has the same shape: labelled cases, field-level matches, a judge model separate from the generator, a planted-error check of the judge, results saved per version. At HDFC the RAG apps were evaluated by user feedback and Compliance review, not formal metrics. Say so, and say that's what you'd put in from day one.

### B2. Retrieval looks fine but answers are still wrong. Why?
Check in order: (1) is the right passage retrieved but **buried** in the context (models can miss material in the middle of long contexts)? (2) is the passage **cut off** or missing context because of chunking? (3) are there **conflicting** passages from different versions of a document? (4) is the prompt letting the model **fill gaps from memory** instead of saying "not found"? (5) is the **question ambiguous**? Debug by logging the retrieved chunks next to every answer.

### B3. How do you evaluate with no labelled data on day one?
Start small: sit with 3 to 5 users, collect 30 real questions, answer them yourself with an expert, and treat that as v0 of the set. Generate synthetic questions from documents to widen coverage, but have a human review them, because synthetic sets are easier than real ones. Grow the set from real failures.

### B4. How do you know the eval itself is good?
Check the label quality (two raters, measure agreement; if experts disagree a lot, the model can't be expected to match), check the set covers the real mix of cases, keep a held-out slice, and read the failures by hand. A model that matches your labels is only as good as the labels. **Your hook:** my build's labels are 4 mine and 11 Claude's; the honest next step is a second human rater.

---

## C. Improving RAG systems: strategies and algorithms

### C1. What would you do to improve a RAG system?
**30 seconds.** First **measure where it fails** (retrieval or generation), then fix that part. Retrieval fixes: better chunking, **hybrid search** (keyword plus vector), **reranking**, metadata filters, better queries. Generation fixes: a tighter prompt, forcing citations, a stronger model, and an "I don't know" path. Change one thing at a time and re-run the golden set.

**The toolbox, with what each is for:**

| Problem | Technique | Plain-language idea |
|---|---|---|
| Right passage not retrieved | **Hybrid search** (BM25 keyword + dense vectors, merged with **Reciprocal Rank Fusion**) | Keywords catch exact terms and codes; vectors catch meaning. Together beat either. |
| Right passage retrieved but ranked low | **Reranking** with a **cross-encoder** (retrieve 50, rerank to 5) | A slower model reads the question and each passage together and scores the fit. |
| Chunks lose context ("it", "the company") | **Contextual retrieval** (prepend a short summary of where the chunk sits, before embedding), **parent-document / small-to-big** (search small chunks, return the larger section) | Make each chunk understandable on its own. |
| Chunks split mid-idea | Structure-aware chunking (by headings, tables, sentences), some overlap; **semantic chunking** | Cut at natural boundaries, not every 500 tokens. |
| User question is vague or short | **Query rewriting**, **multi-query** (several paraphrases), **HyDE** (embed a hypothetical answer instead of the question), **step-back** prompting | Turn the question into something that matches how documents are written. |
| Wrong documents for this user | **Metadata filtering** (department, date, document type, permissions) | Filter before searching. Also the right place to enforce access control. |
| Results all say the same thing | **MMR** (maximal marginal relevance) | Trade relevance against duplication. |
| Needs facts spread across many documents or relationships | **GraphRAG** / knowledge graph, multi-hop retrieval | Link entities so the system can follow connections. Heavy; use only if the questions really need it. |
| Query is sometimes answerable without retrieval, sometimes needs several rounds | **Agentic RAG** (the model decides what to search and when), **Self-RAG / Corrective RAG** (grade retrieved passages, retry or fall back) | The model checks its own retrieval. Adds cost and latency. |
| Domain jargon embeds badly | **Fine-tune the embedding model** on your own query-passage pairs; try a better off-the-shelf embedding first | Teach the vectors your domain's language. |
| Too slow or expensive | Caching (semantic cache, prompt caching), smaller models for easy steps, fewer retrieved chunks | |
| Answer ignores the context | Stronger instruction to quote; put the context close to the question; shrink the context | |
| Whole corpus is small | **Skip RAG**: put it all in the context window | Simplest thing that works. |

**Order I'd try (cheapest first):** fix chunking and metadata → add hybrid search → add a reranker → query rewriting → only then agentic or graph approaches or fine-tuning embeddings.

**Your hook.** At HDFC: LlamaIndex RAG over pgvector, a separate vector DB per department because retrieval struggled to separate similar content (and for access scoping). The reflection to offer: today I'd test one store with permission-aware metadata filters plus a reranker, and prove it with a retrieval eval.

### C2. RAG vs long context vs fine-tuning?
- **RAG** when the data is large, changes often or is private, and you need citations.
- **Long context** when the corpus is small enough to fit and the task needs the whole document (a single report). Simple, but costs more per query and models can miss details in the middle.
- **Fine-tuning** teaches **style, format or a narrow skill**, not fresh facts. Try prompting and examples first. You haven't fine-tuned: say so.
- They combine: fine-tuned model + RAG for facts.

### C3. How do you choose chunk size?
There's no universal number. Start around a few hundred tokens with some overlap, align to document structure, then **test on your own golden set** with recall@k at several sizes. Small chunks retrieve precisely but lose context; large chunks carry context but dilute the match. Small-to-big gets both.

### C4. What is an embedding, and how do you choose a model?
A vector of numbers that places text in a space where similar meaning is close together. Choose by: performance on **your** retrieval eval (leaderboards like MTEB are a start), language and domain, dimension size and cost, whether it can run inside your data boundary. Re-embedding everything when you change model is a real cost.

### C5. How do you handle tables, PDFs and scanned documents in RAG?
Parse structure first (layout-aware parsers, or a vision-capable model for complex pages), keep tables as tables (Markdown or JSON) with their caption and headers in the chunk, store page numbers for citations, and test on the ugly documents specifically. **Your hook:** the rating-agency emails turned into images, the Textract parser broke, and a vision-capable Azure OpenAI model was more robust.

### C6. How would you keep a RAG index fresh and permission-correct?
Incremental re-indexing on change events (not nightly full rebuilds), store document version and source ID in metadata, and apply the **user's permissions at query time** by filtering on access metadata or by querying through the source system's own permissions (e.g. delegated Microsoft Graph access), so the AI never shows anything the user couldn't open themselves.

---

## D. LLM fundamentals

### D1. How do transformers work?
Text is split into **tokens** and each token becomes a vector (**embedding**). Layers of **self-attention** let every token look at the others and weigh which matter for it, so "it" can pick up what it refers to. Stacking many layers builds up meaning. The model's output is a probability for the **next token**; it samples one, appends it, and repeats. Training teaches those probabilities on huge text, then instruction tuning and human or AI feedback make it follow instructions. **Your hook:** the MSc team study used Bahdanau attention in LSTM decoders, which is the earlier form of the same idea.

### D2. What is the context window, and what are its limits?
The maximum tokens the model can read and write in one call. Bigger windows cost more, are slower, and accuracy on details can drop when the key fact sits in the middle of a long context ("lost in the middle"). Context is the working memory: nothing persists between calls unless you send it again.

### D3. What does temperature do?
Controls randomness when picking the next token. Low = more consistent, better for extraction and classification; higher = more varied, for drafting and ideas. Even at 0, outputs can vary slightly between runs, so don't assume exact reproducibility. (My build used 0 and v1 still moved by a case or two between runs.)

### D4. How do you read a benchmark?
Ask what it measures, whether the test data may have leaked into training (**contamination**), whether the tasks resemble yours, and whether the margin is bigger than run-to-run noise. Treat leaderboards as a shortlist, then run your own 30 to 50 cases. Your own eval set matters more than any public score.

### D5. What's the difference between prompt engineering, context engineering and fine-tuning?
**Prompt engineering** = how you phrase the instruction. **Context engineering** = deciding what information goes into the model's window and how: the right documents, tools, examples, history, in a compact form, plus the pipeline that fetches them. **Fine-tuning** = changing the model's weights. For the BSC role, context engineering is the main lever.

### D6. Reasoning models vs standard models?
Reasoning models spend extra tokens "thinking" before answering, which helps on multi-step problems and costs more and runs slower. Use them for hard judgement and planning; use cheaper, faster models for extraction and routing. **Your hook:** the HDFC split of Llama-3 for volume and Azure OpenAI for decision-makers is the same tiering idea.

### D7. What is structured output and why does it matter?
Forcing the model to return valid JSON against a schema (via the API's structured-output mode, function calling, or validation with retries). It makes outputs usable by code and checkable. **Your hook:** Wingman validates LLM JSON with Pydantic and repairs it; in the eval, my runner validates and retries, and reports retries (one case still never produced valid JSON on v2).

### D8. What is quantisation / what are open-weight models for?
Open-weight models can be self-hosted for data control or cost; quantisation compresses the weights (e.g. to 4-bit) so they fit smaller GPUs, with some quality loss. **Your hook:** Llama-3 self-hosted on a GPU instance for Client Service.

---

## E. Evals, prompts and skills

### E1. How do you treat prompts and skills as products?
Each has an **owner, purpose, inputs and outputs, version in Git, changelog, a test set with scores, and a status** (draft / approved / deprecated). Changes go through the eval before release, like code review plus tests. Feedback from users is logged. **Your hook:** every HDFC prompt change was versioned in Git with Compliance review; the build's skill has a v1 and v2 with a changelog and scored results. Honest gap: no formal eval sets at HDFC. **Tie to the article:** their prompt grew from about 10 to 200+ lines over dozens of iterations, with each element tested on 5 cases.

### E2. How do you build and run an eval for an LLM feature?
1. Define "good" with the people who use the output. 2. Collect 30 to 100 real cases, including edge cases. 3. Get expert labels (two raters if you can). 4. Score what's checkable by rule (exact fields, schema, quote presence) and use a judge only for what needs judgement. 5. Calibrate any judge against humans and test it with planted errors. 6. Version the set and results; run on every change; look at failures by hand. 7. Keep a held-out slice.

### E3. What are the weaknesses of LLM-as-judge?
Prefers longer or more fluent answers, prefers its own model family's style, sensitive to the order options are shown, can be inconsistent, and has the same hallucination risk. Mitigate: use a different model from the one being judged, a narrow rubric, binary or small-scale scores, calibration against human labels, planted-error tests, and spot checks.

### E4. How do you measure agreement between an LLM and human experts?
Percent agreement is a start; **Cohen's kappa** corrects for chance agreement; for ordinal scores (1 to 5) use within-one agreement or weighted kappa. Compare against **human-human agreement** as the ceiling. **Tie to the article:** AI matched the final scores 81% of the time vs deal leads 64%, but the final was set by the same team after seeing the AI's output, so how the benchmark is built matters.

### E5. How do you handle non-determinism in testing?
Run each case several times and look at consistency, use temperature 0 for evals, evaluate on enough cases that noise doesn't decide the result, and don't accept a change on a one-case difference. **Your hook:** my n = 15 build can't separate v1 from v2 reliably, and the README says so.

### E6. A prompt change fixed one case and broke two others. What now?
That's what the regression set is for. Run the whole set on every change, compare per-case, and only ship if the aggregate improves without breaking the cases that matter most. If a rule keeps conflicting, split into two steps or add examples.

### E7. How would you build the impact-assessment skill library at BSC?
Start from the framework BSC already uses (the article mentions Impact Frontiers: who is affected, depth of impact, contribution; confirm what the team uses now). Define terms precisely, since the AI applies definitions literally. Write the rubric with the impact team, label a set of past assessments together, build the skill, test against their final scores, and track agreement. Output with **evidence citations** and a "human decides" line. Version it, and review disagreements with the team because they expose framework gaps (the article found this too: affordability, indirect beneficiaries).

---

## F. Agents, MCP and memory

### F1. What is an agent, and when do you not need one?
A model in a loop that can call tools and decide the next step. You don't need one when a fixed workflow does the job: a defined sequence of steps with an LLM call inside is cheaper, faster and easier to test. Use an agent when the path really depends on what it finds. Start with the simplest design that works.

### F2. What is MCP and why does it matter?
Model Context Protocol: an open standard for exposing tools and data to AI apps, so one connector works across clients (Claude, IDEs) instead of a custom integration for each. A server lists tools with descriptions and schemas; the client lets the model call them. **Your hook:** HDFC agents called Python functions as tools (the pattern MCP standardises); this weekend I built a small MCP server with three read-only tools.

### F3. What did you learn building an MCP server?
- **Tool descriptions are the interface**: the model chooses tools from the text, so vague descriptions mean wrong calls.
- **Few, narrow tools** beat exposing raw SQL.
- **Cap the output** so one call can't flood the context window.
- **Read-only first.**
- **Tool output is untrusted input**: grant descriptions are written by third parties and could contain instructions (prompt injection), so truncate and treat as data.
- Practical: version differences between SDKs (v2 renamed `FastMCP`; I pinned v1), and blocked data sources (the registry moved).

### F4. How do you evaluate or choose an MCP connector?
First-party vs community; **auth model** (Entra ID / OAuth delegated so it respects existing permissions); read vs write scopes; audit logs; data residency; maintenance; prompt-injection exposure; latency and token cost. Then a task suite of 10 to 20 real tasks per connector with success rate and failure analysis; start read-only.

### F5. What memory system should the agents use?
Start simple: curated notes or per-project files the agent reads, with source and timestamp. Add structured memory only when needed, with explicit write rules (what gets saved, who can correct it), a way to forget (GDPR, stale facts) and permissions per user/team. Avoid dumping everything into a vector store. Measure whether memory improves task success, otherwise skip it.

### F6. How do you make agents reliable?
Narrow scope, tools with clear schemas, step limits and timeouts, validation on every tool call, human approval before any external action (send, write, delete), logging each step so you can replay failures, and evals on whole tasks (did it finish correctly?), not only on single answers.

### F7. What is prompt injection and how do you defend against it?
When text the model reads (a web page, a pitch deck, an email, a tool result) contains instructions that hijack it. **Direct** = the user types it; **indirect** = it's hidden in content the agent fetches. No complete fix. Layers: treat external content as data, least-privilege tools, no autonomous writes or sends, human approval for side effects, output filtering, separate the part that reads untrusted text from the part that holds secrets or powers. For BSC: decks and outreach research are the exposure points.

### F8. How would you let Claude read SharePoint safely?
A connector using **delegated** permissions through Entra ID, so Claude can only see what that user already can; least-privilege scopes; audit logging; no write access at first; test with a restricted user; agree the design with IT. You have no hands-on Microsoft experience: say you'd work it out with their IT team and know the concepts (identity, scopes, consent).

---

## G. Security, privacy and governance

### G1. Staff are pasting sensitive data into consumer ChatGPT. What do you do?
Don't just ban it. Provide an **approved enterprise tool** that's easier to use (BSC already has Claude), a short clear data policy (what can and can't go in), training through the AI Academy, and visibility and logging. If the approved path is easier, the workaround fades.

### G2. What are the GDPR / UK data issues with AI at BSC?
UK GDPR: lawful basis and purpose for personal data, data minimisation, retention, rights (access, deletion), a DPIA for higher-risk uses, and contracts and data-processing terms with vendors. Check where data is processed and whether it's used for training (enterprise terms normally say no). For outreach to individuals: legitimate-interest assessment and no scraping that breaks terms of service. Say you'd work with BSC's data protection lead rather than claiming legal expertise.

### G3. How would you set guardrails?
Input checks (PII, injection patterns), restricted tools, structured outputs with validation, output checks (citations present, banned content), confidence or exceptions routing to a human, and monitoring in production. Pick controls by impact tier.

### G4. How do you manage secrets and API keys for AI tools?
In a secrets manager (Key Vault in Azure), never in prompts, code or notebooks; short-lived tokens where possible; rotation; separate keys per environment; usage limits and alerts. **Your hook:** worked with the security team at HDFC on IP allow-listing and reverse-proxy fixes for VAPT. Authentication there was LDAP, not SSO/OAuth.

### G5. What AI regulation should we know about?
UK takes a principles-based, regulator-led approach (no single AI law yet; check current position). The EU AI Act applies if you serve the EU, with risk tiers. For an investor, the practical points are data protection, explainability of decisions that affect people, and record-keeping. Keep this short and say you'd confirm current rules with compliance.

### G6. How do you audit and monitor AI in production?
Log prompt version, model, inputs (with PII care), retrieved sources, outputs and tool calls; sample for human review; dashboards for cost, latency, error and feedback rates; alerts on drift or sudden changes; a rollback path for prompts and models.

---

## H. Cost and build-vs-buy

### H1. How do you estimate the monthly cost of an AI workflow?
Tokens in × items × price + tokens out × items × price, plus retries, eval runs and a margin. Example (prices are third-party figures from Oct 2026, **verify**): 200 documents × 20k tokens in and 1k out on a mid-tier model at about $2 / $10 per million = (4M × $2) + (0.2M × $10) = $10 a run. Levers: **prompt caching** (cached input is much cheaper), **batch** (about 50% off for non-urgent work), **model tiering** (small model to extract, larger to judge), shorter context, and fewer retries. Set budgets and alerts.

### H2. Build or buy?
Buy or configure when it's a commodity and the vendor meets your security bar. Build when it's core to your edge (impact assessment) or the data is unique. Also weigh: lock-in, cost at scale, exit path, maintenance burden for a two-person team. **Use the ladder:** a Claude project or skill → an MCP connector → a scheduled or automated flow (Power Automate, scheduled agent) → a custom app only if needed. **Your hook:** Llama-3 vs Azure OpenAI; Power BI licences too costly to scale, so dashboards rebuilt in React.

### H3. Which model would you use for X?
Pick by task and risk, not by name: small and cheap for extraction and routing, mid-tier for most drafting and analysis, frontier or reasoning model for hard judgement. Test two or three on your own set and compare quality, latency and cost. Models change fast, so keep the model swappable behind one interface. **Your hook:** models switchable at HDFC.

### H4. How do you decide what to automate first?
Value × feasibility × risk. Pick a frequent, painful, well-defined task with a willing champion, where errors are cheap or reviewable. Quick wins build trust for harder projects.

### H5. How do you show an AI project is worth it?
Baseline first (time per task, error rate, volume), then compare after: time saved, quality against experts, adoption. **Your hook:** 300+ rating emails a day → about 60 analyst hours a month saved. Don't invent numbers for projects where you don't have them.

---

## I. Adoption, stakeholders and the AI Academy

### I1. How do you explain a technical risk to a non-technical colleague?
Use an example from their work, not jargon: "it can sound sure and still be wrong, like a confident new analyst who didn't read the file; so we show where each claim came from." Then say what you've done about it and what they need to do (check the quote).

### I2. A senior colleague wants AI to make a decision for them. What do you say?
Show what it's good at (first pass, consistency, speed) and where it isn't (unsupported claims, bias), propose AI-assisted not AI-decided, and agree what evidence would earn more trust. The article's own warning is over-reliance on fluent output.

### I3. How would you run an AI hackathon or training?
Start with real tasks from teams, pair non-technical staff with a builder, give a safe sandbox and approved tools, time-box to a day, end with demos and a shortlist of ideas to take forward, and follow up in a month on what stuck. **Your hook:** hackathon record (Rolls-Royce Derby 4th, Encode 2nd, Lloyds-sponsored Datathon 3rd) and the Swindon fuel-poverty hack.

### I4. How do you get people to actually use what you build?
Build with a champion in the team, demo early, make the first version fit their current workflow (inside tools they already use), collect feedback, track usage, and retire what isn't used. **Your hook:** HDFC departments used the apps daily; requirements gathered from Compliance, Investment and Client Service; feedback turned into releases.

### I5. How do you work with IT and the data team?
Bring them in early, ask what constraints exist (identity, network, data location), agree who owns what, and follow their security process rather than routing around it. **Your hook:** coordinated with the security team on port allow-listing, private-IP Security Groups, and an Nginx reverse proxy to pass VAPT.

---

## J. Behavioural (have a 90-second STAR for each)

- **Tell me about a significant technical decision you made.** Siloed vector DBs per department; Llama-3 vs Azure OpenAI split; Textract → Azure OpenAI. State the options, the choice, the trade-off, and what you'd do differently.
- **A time something you shipped failed or was wrong.** The Textract parser broke when an agency switched to image emails; you diagnosed it and moved to Azure OpenAI. Say what you changed so it would be noticed sooner.
- **A disagreement with a stakeholder.** Choose a real one (e.g. a Compliance request that slowed a release). Say what you understood about their concern.
- **Leading others.** De facto lead for up to four interns: how you split work, reviewed code, unblocked them.
- **Learning something fast.** This weekend's MCP and eval build; earlier, building with LLMs since the early GPT-3.5 tooling.
- **What would you do in your first 90 days?** Listen first: the team's real workflows, what's already built, where Claude is used. Get one small win live. Set up the eval and versioning basics for the prompt/skill library. Agree priorities with Nick.
- **Biggest weakness for this role.** No impact-investing background and no hands-on Microsoft stack; plan: learn from the investment and IT teams, and read the framework and article.
- **Why BSC / why the UK?** Your own words (still blank in `STRATEGY.md` §9).

---

## K. Questions about Nick's article (he wrote it; expect him to enjoy this)

Read the article in full first. Facts to check against it: 45 ventures; 3 Impact Frontiers dimensions on a 1 to 4 scale; Perplexity Deep Research with a 200+ line prompt; AI matched the final scores 81% vs deal leads 64%; hallucinations estimated at 10 to 20%.

**K1. What did you take from our article?**
"That the prompt is a product (10 to 200+ lines over dozens of iterations), the AI's disagreements exposed gaps in your own framework, and the main limit is that the final benchmark was set after seeing the AI's output."

**K2. What would you do differently to test it more rigorously?** Fix the labels first, from independent assessors who haven't seen the AI output; use more companies and several runs per company; measure hallucinations claim by claim instead of estimating them; report human-human agreement as the ceiling; split by company stage.

**K3. How would you get the hallucination rate down from 10 to 20%?** Retrieve and cache company evidence in a first step so claims can be checked against it; require a citation and a quote per claim; a verifier pass that checks each claim; a "not enough public information" outcome for early-stage firms instead of a guess; then re-measure.

**K4. What would you add to the data sources (LinkedIn, reviews, Crunchbase)?** Each source has terms, accuracy and bias: a company's own marketing is not independent evidence, reviews skew, and some sources can't be used under their terms. Track source and reliability per claim.

**K5. What's the risk of staff over-relying on AI scores?** Fluent output gets trusted; juniors stop forming their own view; errors repeat consistently. Controls: show evidence with every score, ask reviewers to score first on a sample, track disagreements, keep a named human owner.

**K6. How would you move from a one-off experiment to a standing process?** Version the prompt and rubric, keep a labelled set from each review cycle, run regression tests when the prompt or model changes, assign an owner, log outputs and final decisions, and review the agreement numbers each cycle.

**K7. Link to your build in one sentence:** "My weekend build did a small version of this loop: a versioned skill, labelled cases, a separate judge, a planted-error check, and a README that says how little 15 cases can prove."

---

## Curveballs and quick answers
- **"What's the biggest risk of AI at BSC?"** Over-trust: fluent output treated as verified. Second: data leaving the boundary.
- **"What would you not use AI for?"** Final investment decisions, anything where you can't check the output cheaply, and decisions about individuals without a clear human owner.
- **"A model update changes your outputs overnight."** Pin versions, run the regression set on new versions before switching, keep the previous model available.
- **"How do you stay current?"** Be specific: the docs and release notes for the tools you use, hands-on builds like this weekend's, and reading primary sources (the article, papers) instead of summaries.
- **"What don't you know?"** Fabric, Graph/SharePoint/Power Automate in practice, impact-investing frameworks, fine-tuning. Say how you'd close each gap.

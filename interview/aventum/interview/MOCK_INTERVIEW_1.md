# Aventum Round 1: Mock Interview (Head of AI)

Questions the Head of AI is likely to ask, each with an answer in your voice. Built from `../STRATEGY.md` (§4 evidence, §5 concepts, §6 scenarios, §8 gap scripts, §9 questions), your CV and cover letter, and the JD. The introduction is in `INTRODUCTION-CLAUDE.md`.

How to use it:
- Say each answer out loud, in your own words. Aim for **90 seconds or less** per answer, then offer to go deeper.
- `[YOU: ...]` marks facts I don't have. Fill them in or use the fallback given. Don't invent them.
- **Answer-shape:** claim, one concrete example, what you'd do differently now. For gaps: acknowledge plainly, nearest real evidence, what you've done since, how you'd ramp.
- Honesty rules (`STRATEGY.md`, "Honesty guardrails"): only the figures 3 years, 300+ emails a day, 60 analyst hours a month, 10 hours a week, up to 4 interns. "De facto team lead". Both MSc projects are team projects. No formal evals or fine-tuning at HDFC. CI/CD was a one-click Jenkins/GitLab deploy to dev and prod. Auth was LDAP.

Contents: 1 Opening and motivation, 2 HDFC deep dive, 3 Sequence and behavioural modelling, 4 Causal inference and validation, 5 Design and scenario questions, 6 Behavioural questions, 7 Logistics, 8 Your questions, 9 Weak spots to drill.

---

## 1. Opening and motivation

### Q1. Why did you leave HDFC and do an MSc?
> It was a planned move. I'd spent three years building GenAI applications, mostly self-taught on the job, and I wanted a formal grounding in the machine learning and statistics underneath: sequence models, evaluation, and how to be rigorous about whether a model is actually good. I left in July 2025, started at Bristol in September, and the MSc ended this September, so I'm available now.

### Q2. Why this role, and why insurance?
> Two reasons. First, the role is about models that sit inside live decisions: pipelines, inference services, monitoring, validation. That's the work I've been doing, in a different domain. Second, it pushes me into behavioural and causal modelling, which I haven't done in production and want to. Insurance appeals because it's regulated and decision-heavy, like asset management, and your Digital Twin and agentic work sounds like it's still being defined, so there's room to contribute rather than just follow a playbook.

*Watch-out:* don't claim insurance knowledge you don't have. If asked, see Q41.

### Q3. What do you know about Aventum?
> It's a specialty (re)insurance group in the London market. Rokstone is the underwriting and MGA side and Consilium is the broking side. Their CSOP booklet describes very fast growth over the last decade, and the mission is to be the most inspiring specialty (re)insurance group. I've read the recruitment material, and I understand this role sits in Technology under the Head of AI and builds behavioural intelligence into the digital products. I'd like to hear from you how far along the Digital Twin is.

### Q4. Your CV is strong on production but light on what the JD asks for: behavioural models, causal inference, PyTorch in production. Why should we see you?
> You're right, and my cover letter said the same. I haven't built behavioural models, used DoWhy or EconML on real data, or shipped a PyTorch model. What I have is the part that usually decides whether those projects succeed: getting a model behind an API, into a workflow, with security review, CI/CD and users giving feedback. I also have the sequence-modelling foundations from the MSc. Since applying I've worked through behavioural cloning, DoWhy and EconML on public data, so I know where the traps are. I'd expect the production side to be fast for me and the modelling side to be where I need a partner and a first scoped project.

---

## 2. HDFC deep dive

### Q5. What's the biggest production system you built? Walk me through the architecture.
> The department RAG applications for Compliance, Client Service and Investment. A ReactJS frontend talking to FastAPI microservices run with uvicorn in Docker on AWS (EC2, ECR). Retrieval used LlamaIndex with Azure OpenAI embeddings and a separate pgvector database per department, so each team only searched its own documents. Generation was Azure OpenAI GPT-3.5 for most users and a self-hosted Llama-3 on a GPU EC2 instance for Client Service, the largest department. Agents called Python functions as tools to run SQL-backed fund comparisons and generate PDF reports. Access went through RBAC with a Python auth function against LDAP, and everything sat behind Nginx with Security Groups limited to company private IPs.

*Follow-up to expect:* "What would you do differently?" See Q6.

### Q6. What would you do differently today?
> Evaluation, mainly. We relied on user feedback, Compliance review of each release and versioned prompts, but we had no golden question set and no tracing. Today I'd build a small evaluation set per department with Compliance, run it on every prompt or model change, and add tracing so we could see retrieval and generation failures. I'd also look at one store with permission-aware filtering instead of one database per department, though the per-department split was a deliberate, simple answer to the access-control requirement at the time.

### Q7. Why a separate vector database per department rather than metadata filtering?
> Access control was department-based, and the separate databases made that boundary obvious and easy to audit. We also found GPT-3.5 and Llama-3 mixed up similar content across departments when everything was in one place. The cost is operational overhead and no cross-department search. Today I'd weigh permission-aware filtering in one store, with retrieval evals to check it doesn't leak.

### Q8. How did you know the RAG answers were good?
> Honestly, not with a formal evaluation set. Quality came from users telling us when answers were wrong, Compliance reviewing every release, system-prompt guardrails, and versioning prompts in Git so we could roll back. It worked for internal tools, but it's the first thing I'd change, and it's directly relevant here, because validating a model before it affects decisions is what this role is about.

### Q9. Tell me about something that broke in production.
> The rating-email pipeline. It parsed 300+ emails a day from credit-rating agencies, first with AWS Textract. One agency started sending its emails as images, and the Textract parser broke on those. `[YOU: say how you noticed.]` I switched the extraction step to Azure OpenAI, which handled the image emails and was more accurate on the rest. What I took from it: formats you don't control will change, so the pipeline needs a check that tells you when an expected source is missing. I'd add that alert now.

*Watch-out:* how the failure was detected isn't recorded in your notes, so the answer leaves it for you to fill in. Don't guess.

### Q10. Describe the email pipeline end to end.
> A shared inbox feeds a parser. Each email is parsed into structured fields, first with Textract and later with Azure OpenAI. Company names are fuzzy-matched against the list the analysts track. Then a daily summary and an Excel file are produced and stored in S3. It runs as a SageMaker batch job, started by an EventBridge rule at 9 AM that triggers a Lambda function, separate from the user-facing services. It saved about 60 analyst hours a month.

*Know precisely:* SageMaker was used only for this pipeline.

### Q11. How did you stop the fuzzy matching producing false matches?
> `[YOU: recall the threshold and any manual-review step. If you can't, use this:]` I can't give you the exact threshold from memory. The approach I'd use, and would use now, is thresholds tuned on labelled pairs, with a manual-review band between "clearly matches" and "clearly doesn't" so ambiguous names go to an analyst instead of being auto-assigned.

### Q12. You used Llama-3 for one department and Azure OpenAI for the rest. Why, and what did it cost?
> Client Service was the largest department, and self-hosting Llama-3 on a GPU EC2 instance was the cost-driven choice there. Decision makers got Azure OpenAI because the outputs were stronger. The models were switchable. It was a reasoned trade-off, not a formal cost model, so I can't quote figures. It's my best example of balancing quality and commercial delivery.

*Watch-out:* don't invent cost or serving-stack details.

### Q13. How did CI/CD work?
> Frontend and backend were separate repos, each with dev and prod branches and its own container. A one-click Jenkins and GitLab pipeline deployed to dev or prod. I'd call it button-triggered rather than fully automated continuous delivery, and there were only two environments. What I'd add for a model lifecycle is automated tests and evaluation gates in the pipeline, and model and prompt versioning alongside the code.

### Q14. How did you get through the security review?
> We failed VAPT several times before passing. I worked with the security team on the findings. The fixes I own: RBAC through a Python auth function against LDAP in three tiers, Security Groups limited to company private IPs, and an Nginx reverse proxy. We used the security team's CloudFormation templates and didn't author our own. The lesson was to involve security early rather than at the end.

### Q15. Tell me about the agents. Did you use an agent framework?
> No framework. The agents were tool-calling: the model chose from Python functions that ran SQL-backed fund comparisons or generated PDF reports, and results went back through the FastAPI services. I guided behaviour with system prompts, versioned every change in Git, and had Compliance review each release. For anything consequential I'd now add human approval, tool permissions and full logging. I haven't built formal agent evaluations.

---

## 3. Sequence and behavioural modelling

### Q16. Explain an LSTM, and why use one over a plain RNN?
> An RNN processes a sequence one step at a time, carrying a hidden state. In long sequences the gradients vanish, so it forgets early steps. An LSTM adds a cell state and three gates, input, forget and output, that decide what to write, keep and expose, which lets it hold information over longer spans. Input is (batch, sequence length, features). For intent classification I'd use the last hidden state, and for next-event prediction I'd use every step.

### Q17. Explain attention, and how it differs from Transformer self-attention.
> Attention lets the model weight which input positions matter for each output. In my MSc team project the LSTM decoder used Bahdanau (additive) attention: at each decoding step it scores the encoder states against the decoder state and takes a weighted sum. Transformer self-attention does it between all positions of the same sequence, using queries, keys and values with a scaled dot product, plus positional encodings, and it trains in parallel instead of step by step. For next-event prediction you add a causal mask so a position can't see the future.

### Q18. LSTM vs Transformer for predicting a user's next action?
> For short sequences and small data, an LSTM or even a first-order Markov baseline is cheap and often competitive. Transformers, like SASRec-style models, tend to win with longer histories and more data because they capture long-range dependencies and parallelise. I'd start with a Markov baseline, then gradient boosting on tabular features, then a sequence model only if it adds measurable lift. A time-based split matters more than the architecture.

### Q19. What did you actually build with sequence models?
> In the MSc VisionCaptioner team project we compared CNN, ViT and ResNet encoders with symbolic, SBERT-retrieval and LSTM decoders, with and without Bahdanau attention, trained with Adam over five seeds. It was a comparison study, so it's academic experience, and I'm not claiming a production sequence model. I also wouldn't claim we beat the commercial models we benchmarked against, because those comparisons weren't run under the same protocol. `[YOU: only name the framework (PyTorch?) if you're sure what the team used.]`

### Q20. What is behavioural cloning, and when does it fail?
> It's supervised learning of a policy, the action given the state, from logged expert decisions. For underwriting that would be learning how underwriters quote, decline or refer from historical submissions, which is effectively a model of the underwriter. It fails through covariate shift: the model visits states the expert never did, errors compound, and it has no idea what to do. DAgger addresses that by having the expert label the states the learner actually visits. In insurance there are two further problems: it copies historical bias, which matters for fairness and Consumer Duty, and selective labels, since you only see outcomes for risks that were bound.

### Q21. What would imitation learning or inverse RL add beyond cloning?
> Inverse RL infers the reward the expert is optimising instead of copying the actions, so the policy can stay sensible when conditions change, such as new appetite rules. It's harder to fit and validate, so for a first version I'd keep cloning plus strong baselines and monitoring, and consider IRL if the environment shifts a lot.

### Q22. What does "RL-inspired" mean here? Would you use RL?
> I read it as bandits and offline RL for decisioning, not game-playing RL. For one-step decisions like which submissions to prioritise, a contextual bandit with logged propensities fits and lets us evaluate off-policy later. For multi-step workflows, offline RL such as conservative Q-learning learns from logs without live exploration, which suits a regulated setting. In both cases I'd want shadow evaluation before anything acts on its own.

### Q23. Have you built any of this?
> Not in production, and I'd rather say that plainly. I understand the concepts and since applying I've worked through Markov and LSTM baselines, behavioural cloning with DAgger, and bandits on synthetic and public data. Where I'm strong is the part that usually breaks these projects: getting the model into the workflow, behind an API, safely.

*Watch-out:* "worked through", never "built" or "experience".

---

## 4. Causal inference and validation

### Q24. How would you measure whether an AI tool actually improved underwriting outcomes?
> First choice is to randomise, an A/B test or a staged rollout with a control group, so the comparison isn't confounded by who chooses to use the tool. If we can't randomise, say it was rolled out to half the teams last quarter, I'd use difference-in-differences against the teams that didn't get it, check parallel pre-trends, and adjust for confounders such as line of business and broker mix. DoWhy's model, identify, estimate, refute steps are a good structure, and refuters like a placebo treatment tell you how fragile the estimate is. Outcomes need guardrails too, such as loss ratio and complaints, and may arrive late.

### Q25. Have you used DoWhy or EconML?
> Not on real business data. This week I worked through DoWhy and EconML on the Lalonde job-training dataset: build the graph, identify the estimand, estimate with propensity weighting and Double ML, then run refuters. What struck me was how far the naive difference in means was from the adjusted estimate, which is exactly the confounding problem you'd have measuring an AI tool's effect. In the role I'd pair with whoever owns experimentation and start with a rollout we can analyse as a diff-in-diff.

*Watch-out:* only say this if you did notebook 05. If not, drop the "this week" sentence.

### Q26. What are the assumptions behind causal estimates from observational data?
> Unconfoundedness, meaning no unmeasured confounders given the covariates. Positivity or overlap, meaning every kind of unit could have received either treatment. And SUTVA, no interference between units. Beyond those, a DAG tells you what to adjust for: confounders yes, mediators and colliders no. Doubly robust estimators like AIPW are consistent if either the outcome model or the propensity model is right, which is why I'd prefer them to one model alone.

### Q27. A/B test, shadow deployment, offline replay: when would you use each?
> Offline replay first: run the new model over historical logged events and compare its decisions with what happened, using off-policy evaluation if it's a policy, which needs logged propensities. Then shadow: the model runs on live traffic, outputs are logged but not acted on, so you get real latency, errors and agreement with humans at no business risk. Then a canary or A/B test on a small slice with guardrail metrics and automatic rollback. Then full rollout with monitoring. If asked how I'd ship a model, that's the sequence.

### Q28. How would you monitor a model when labels arrive months later?
> In three layers. Immediately: input data drift (PSI or KS tests), prediction drift, latency and error rates. Soon: proxy signals such as agreement with human decisions and override rates. Later: true performance once labels arrive, using cohorts by decision date. Add alerting, and retraining triggers that are reviewed rather than automatic. Delayed labels are normal in insurance, so the monitoring has to be designed around them.

### Q29. Your model looks great offline but underwriters ignore it. What do you do?
> I'd treat it as a product problem, not only a model one. Run it in shadow and measure agreement with underwriters, then look at where it disagrees and why. Check whether the outputs are explainable enough to act on: reason codes or SHAP, not a bare score. Talk to the underwriters. I've done a version of this at HDFC: we released prototypes to real users and changed the applications based on their feedback.

---

## 5. Design and scenario questions

### Q30. How would you build a model that predicts which submissions an underwriter will quote, and put it into production?
> I'd start by clarifying: what decision does it support, prioritising the queue or suggesting quote or decline, who uses it, and the success metric, such as time to quote, hit ratio or loss ratio, and constraints like explainability, FCA rules and latency. Data: submission fields, broker, line of business, the history of underwriter actions, and outcomes, with a time-based split and care around leakage from fields filled in after the decision. Baselines first: rules, then gradient boosting, then a sequence model if the interaction history adds lift, with calibrated probabilities. I'd recognise it as behavioural cloning of underwriter decisions, so bias and selective labels are explicit risks.
>
> To serve it: a FastAPI microservice in Docker behind the submission workflow, triggered by a submission-received event, which is the EventBridge and Lambda pattern I've used, returning reasons with the score. To validate: offline replay, shadow alongside underwriters, then an A/B on queue prioritisation, then a causal read-out of the effect on time-to-quote and bind rate. To operate: CI/CD, a model registry, drift and delayed-label monitoring, human override always, and an audit log.

*Tip:* draw this as a pipeline if there's a whiteboard or paper.

### Q31. How would you build a Digital Twin of a broker?
> I'd define what questions the twin must answer, for example "what happens to quote volume if we change this appetite rule". State comes from event sequences: submissions, responses, binds. An intent model, maybe an HMM or LSTM, estimates what the broker is likely to do next. A behavioural policy generates actions, and I'd add causal structure so interventions are simulated correctly rather than just correlated. Then validate by replay against history before trusting any what-if answer. I'd keep it small and honest about what it can't predict.

### Q32. An agent makes decisions inside a workflow. How do you keep it safe?
> Limit what it can do: tool permissions with least privilege. Require human approval for consequential actions. Log every tool call and decision for audit. Add guardrails in the prompt and checks on outputs, validating them as untrusted input. In my Wingman project I treated LLM output as untrusted, validated it with Pydantic and repaired or retried when it failed. At HDFC the guardrails were system prompts plus Compliance review. I'd add evaluation sets and shadow mode on top.

### Q33. If you joined, what would you build first?
> Shadow-mode infrastructure and an offline replay harness. Every behavioural model you build needs to be validated safely before it touches live decisions, and it connects my production strength directly to your validation accountabilities. It would also give the causal work something solid to run on.

### Q34. What would you need from me to ramp on causal and behavioural modelling?
> Access to logged decision data, a pairing partner who has done this before, and a first scoped project that I can ship. I learn fastest by building something real with fast feedback, which is how I picked up GenAI at HDFC.

---

## 6. Behavioural questions

### Q35. Tell me about a time you challenged how something was done.
> Power BI licensing. Financial analysts had moved from Excel to Power BI, which saved about 10 hours a week. Then licensing costs made it hard to scale to more users, so I recreated the dashboards in React. The other example is replacing Textract with Azure OpenAI when the image emails broke the parser.

### Q36. Tell me about working with a difficult stakeholder or a disagreement.
> `[YOU: pick a real example from Compliance, Investment or Client Service. Use this structure: what they wanted, why you disagreed, what evidence or demo you used, how it ended.]` If you need a fallback: Compliance wanted to review every release, which slowed us down at first. I made the review easier by versioning every prompt change in Git, so they could see exactly what had changed, and that turned the review into a quick step.

*Watch-out:* the fallback is a plausible framing of the facts in your CV (Compliance reviewed each release, prompts were versioned in Git). It is not recorded as an actual disagreement. Don't use it unless it's true.

### Q37. Tell me about a time you learned something quickly.
> Early GenAI at HDFC: it was my manager and me, with no playbook, so we learned the tooling as we built and released. More recently, the MSc, and working through the causal and behavioural material for this interview.

### Q38. How did you lead the interns?
> I acted as de facto team lead for up to four interns in my final year, not a formal title. I split work into pieces with clear outputs, reviewed their code, and unblocked them when they were stuck `[YOU: confirm this is how it actually worked]`. The team grew from two people to two leads in the GenAI team, and our work was recognised as Best Team Project in 2024 and 2025. `[YOU: add one specific delegation or review example.]`

### Q39. How do you balance research quality against delivery pressure?
> I ship the simplest thing that can be validated, then improve. The Llama-3 and Azure decision is a good example: cost where it mattered, quality where it mattered. For models I'd do the same: baseline first, shadow to get real evidence, then invest in complexity only where it measurably helps.

---

## 7. Logistics (usually Lucy, but have them ready)

### Q40. Salary expectations?
> `[YOU: figure.]` Suggested shape: "I'm looking for something in the upper-middle of the advertised band, and I'm flexible for the right role. I'd also look at the CSOP and bonus as part of the total." Don't open at the £80k ceiling, because your cover letter listed gaps.

### Q41. Do you have insurance experience?
> No, but I've worked in regulated financial services: an asset manager, a Compliance department reviewing every release, credit-rating data. The disciplines carry over, such as audit trails, explainability and conservative rollout. I'd expect to learn the London market quickly by sitting with underwriters.

### Q42. Notice period and right to work?
> I'm not currently employed, so I can start as soon as needed. I'm on a Student Visa and eligible for the Graduate Visa, which gives two years of full working rights. `[YOU: state whether the Graduate Visa is applied for or granted, with dates.]`

### Q43. Location and hours?
> `[YOU: relocating to London, or commuting three days a week?]` Give a one-sentence, confident answer. The role is hybrid, three days in the office, 8:30 to 5.

---

## 8. Your questions (pick 3 or 4)

1. What does the Digital Twin represent today: underwriters, brokers, portfolios or the submission workflow, and how far along is it?
2. Which decisions are the agentic decision engines meant to make or support first, and where does a human stay in the loop?
3. What data is available for behavioural modelling: event logs from the digital suite, underwriting decisions, claims?
4. How do you validate models today: is there shadow or experimentation infrastructure, or would this role help build it?
5. What would a successful first six months look like?
6. What does stage 2 look like: a case study or technical exercise?
7. How do you like to work with your engineers, and how do you support people growing into new areas such as causal modelling?

Close with: "Thanks, this has made me more interested in the role. I'm happy to do any follow-up exercise."

---

## 9. Weak spots to drill before Friday

| Weak spot | Why it is risky | Fix |
|---|---|---|
| Q9 (how the failure was noticed) | The story is in your notes but the detection detail isn't | Recall it and rewrite Q9 in your own words |
| Q12 (Llama-3 vs Azure) | No cost figures or serving details are recorded | Say it was a reasoned, cost-driven choice and don't invent numbers |
| Q29 (users ignoring the model) | Your only evidence is "released to users, changed on feedback" | Keep to that, or add a real example |
| Q38 (leading interns) | The delegation and review details are unconfirmed | Confirm them and add one real example |
| Q11 (fuzzy-match threshold) | Likely deep-dive follow-up | Recall it, or use the stated fallback |
| Q19 (MSc framework and your part) | They may ask what you personally coded | Decide what you did, and say "team" |
| Q25 (DoWhy this week) | Only true if you ran notebook 05 | Run it Thursday morning, or drop the claim |
| Q36 (real stakeholder disagreement) | A fabricated story will unravel on follow-up | Pick a real one |
| Q40 and Q42 (salary, visa status) | Likely asked at some stage | Decide the numbers and dates now |
| Q16 to Q18 (LSTM, attention, Transformer) | Likely quick technical probes | Say each in 60 seconds from memory, with no notes |

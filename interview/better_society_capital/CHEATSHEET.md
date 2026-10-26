# BSC R1 cheat sheet (written Sun 25 Oct 2026)

Facts marked **(verify)** come from web summaries, not primary sources. Check them before you quote a number.

## 1. Nick's own article (SSIR, 2025) (verify against the article)
https://ssir.org/articles/entry/ai-assessments-impact-investing — authors: Nicholas Andreou, Philipp Essl, Jeremy Rogers (all BSC). Nick is the author, so this is the experiment he means in the JD.
- 45 venture startups, each scored 1-4 on 3 Impact Frontiers dimensions (who is affected, depth of impact, contribution) = 135 scores.
- Humans: deal leads. AI: Perplexity Deep Research with a 200+ line prompt, public information only.
- Disagreements were re-examined; a "final" score was agreed by the Venture Impact Lead and deal leads. AI matched final **81%**, deal leads **64%**.
- Hallucinations estimated at **10-20%** of AI assessments; worse for early-stage companies with little public data.
- Their lessons: treat the prompt like a product (grew from ~10 to 200+ lines over dozens of iterations, each element tested on 5 cases); define terms precisely; keep a human in the loop.
- Limits the authors admit: one tool, small sample, the "final" benchmark was set by the same team after seeing the AI output, hallucination rate estimated not tracked, risk of over-trusting fluent output.
- Their next steps: AI first pass reviewed by the Venture Impact Lead; more sources (LinkedIn, reviews, Crunchbase); make data queryable by deal leads; checks against over-reliance.

**How it connects to your build.** Your weekend eval is a small version of the same loop: a versioned prompt, a labelled set, agreement with humans, groundedness checks. Two honest differences: your labels are 4 human + 11 Claude, and the model is Nemotron, not Perplexity.

**Good questions it gives you:** How did the 200-line prompt change as you added eval cases? Did the AI disagree with the "final" score in ways that exposed gaps in the framework (they said it did: affordability, indirect beneficiaries)? How would you stop the benchmark being set after seeing the AI's answer?

## 2. Anthropic products (verify details on anthropic.com / docs)
- **Claude Cowork:** agentic mode of Claude for knowledge work, with a GUI, aimed at non-technical staff. Works on folders you approve and connected apps (M365, Google Workspace, Slack), produces finished files, supports scheduled tasks and subagents. Launched Jan 2026, GA Apr 2026, on all paid plans. Right for BSC staff, not engineers.
- **Claude Managed Agents:** hosted agent service (public beta since 8 Apr 2026). Anthropic runs the agent loop and a sandbox container per session. Resources: Agents (versioned config: model, system prompt, tools, MCP servers, skills), Environments, Sessions (stateful, event stream). Right when you want a scheduled or long-running agent without running your own harness.
- **Claude Code:** terminal/IDE coding agent; you use it daily.
- **MCP:** open protocol for exposing tools/data to models. Your server is a small example.
- **Skills:** folders of instructions the model loads when relevant; treat them as products (owner, version, tests).

## 3. Prices, Oct 2026 (third-party trackers, **verify**)
Per million tokens, input / output: Opus 5.5 $4 / $20; Sonnet 5.5 $2 / $10; Haiku 5.5 $0.10 / $0.50; Fable 5.1 $10 / $50. Batch is 50% off; cache hits are roughly a tenth of input price.
Worked example for the cost question: 200 documents x 20k tokens in + 1k out on Sonnet 5.5 = 4M in x $2 + 0.2M out x $10 = $8 + $2 = **$10 per run**; with Haiku for extraction about $0.50; add retries and eval runs.

## 4. Microsoft side, 30 seconds each (you have no hands-on experience; say so)
- **Graph API:** one REST API over M365 data (mail, SharePoint, Teams); Entra ID auth; **delegated** permissions act as the signed-in user, **application** permissions act as the app (broader, needs admin consent). For an assistant, prefer delegated so it respects existing access.
- **SharePoint:** document store with permissions; the likely home of decks and reports.
- **Power Automate:** trigger + action flows with connectors; good for "new file arrives -> call AI -> write a row".
- **Fabric:** Microsoft's data platform: OneLake storage, lakehouse, data pipelines.

## 5. Your build in 30 seconds
"This weekend I built a small MCP server over 360Giving grant data, with three narrow read-only tools, and a first-pass impact-screen skill. I labelled a few cases, built an eval with a separate judge model, and changed the prompt once. The numbers are small and noisy, so I treat it as a learning build, but it showed me how much the prompt and the labels matter."
Then ONE honest limitation (pick one): labels are mostly mine/Claude's; n=15; the judge is a different small model.

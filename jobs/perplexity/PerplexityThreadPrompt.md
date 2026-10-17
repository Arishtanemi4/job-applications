# Perplexity "champion" thread

Portal field: a URL to a Perplexity thread explaining why you are a strong candidate. The portal has no cover-letter field, so this thread and the CV are all the reader sees. Run the three queries below in ONE thread (Turn 1, then 2, then 3), then use Share -> copy link. Check the link opens in a private window before pasting it into the portal.

Before sharing: do not attach the CV file and do not paste phone numbers or email. Everything the thread needs is in the Turn 1 text, and a shared thread is readable by anyone with the link.

## Turn 1 (paste as is)

I am applying for the Machine Learning Engineer role at Perplexity that improves search quality across the middle and later stages of ranking. The role wants a ranking generalist who owns ambiguous quality problems end to end (define the evaluation, find the bottleneck, build and ship the fix), trains and evaluates retrieval, ranking and classification models (neural and LLM-based), builds ranking infrastructure (feature computation, low-latency inference, multi-stage cascades, monitoring) and trades off quality, latency, reliability and cost.

Write an honest, evidence-based case for why I am a strong candidate. Search the web for Perplexity's public engineering and research writing on search, retrieval and ranking, and connect my background to what the team is working on. Cite sources for anything you take from the web. Use ONLY the facts about me below. Do not invent experience, and do not claim that I have owned a production search or ranking system, trained learning-to-rank models or neural rerankers, or run online ranking experiments.

About me (Kaustubh Sonawane, MSc Data Science, University of Bristol, awaiting result; about 3 years of industry experience):
- HDFC Asset Management (Jul 2022 - Jul 2025), AI Solutions Engineer. Designed and built production retrieval and GenAI applications end to end for Compliance, Client Service and Investment teams: ReactJS frontend, Python FastAPI microservices, RAG with LlamaIndex, Azure OpenAI embeddings and a separate pgvector database per department for semantic search.
- Traded quality against cost: self-hosted Llama-3 on a GPU EC2 instance for the largest department, kept Azure OpenAI for decision makers. Deployed with Docker on AWS through a one-click Jenkins and GitLab CI/CD pipeline; operated both real-time services and a daily batch pipeline on SageMaker.
- Built a pipeline parsing 300+ rating-agency emails a day with fuzzy matching of company names, saving 60 analyst hours a month; moved it from AWS Textract to Azure OpenAI when an agency began sending images.
- First GenAI systems were a two-person effort (my manager and me), so I owned them without task decomposition; later a de facto team lead for up to 4 interns. Best Team Project internally in 2024 and 2025.
- MSc dissertation with AstraZeneca: co-built CellLineSelector, which ranks cancer cell lines by target inclusion and exclusion genes. My focus: data preprocessing, the scoring and ranking algorithm (per-gene scores over six evidence layers, calibrated across lineages, confidence tiers) and the RAG layer. Refined with feedback from AstraZeneca scientists. Code: github.com/Arishtanemi4/az-team25
- MSc group project VisionCaptioner: compared CNN, ViT and ResNet encoders with symbolic, SBERT embedding-retrieval and LSTM decoders, scored with SBERT cosine, BLEU and ROUGE-L. Code: github.com/Arishtanemi4/ata-team30
- Wingman, a personal project: FastAPI and React app with 108 LLM personas where LLM output is treated as untrusted (validated with Pydantic, repaired, cached by input hash) and rate limits shaped the architecture. Code: github.com/Arishtanemi4/wingman
- Portfolio: kaustubh-sonawane-portfolio.vercel.app

Write in first person with a confident, factual tone. Do not include a gaps, recommendations or next-steps section, do not mention other roles or internships, and do not write "not met" or similar in any table cell: where my evidence is adjacent, say what it is and why it transfers, in one clause. Say "co-built" for CellLineSelector (my focus was preprocessing, the scoring and ranking algorithm and the RAG layer), "our team" for VisionCaptioner, and "internally recognised" for Best Team Project. Use Perplexity sources only for statements about Perplexity, never to support claims about me.

Structure the answer as:
1. A summary of exactly three sentences. State plainly that my ranking experience is adjacent (retrieval, and a scoring and ranking algorithm in a dissertation) rather than a production ranking system at scale, and say what the case rests on instead.
2. A table with three columns: each qualification in the role, my closest evidence, and why it transfers.
3. Why ownership, retrieval, quality-versus-cost trade-offs and shipping to real users are relevant to this role.

## Turn 2 (follow-up in the same thread)

Based on Perplexity's public writing on its answer engine, what are the hardest ranking-quality problems in the middle and later stages, such as citation quality, freshness, and query types where retrieval and ranking disagree? For two of them, design an offline evaluation: what to measure, how to build the judgment set, and how to tell whether an offline win will hold online. Cite sources.

## Turn 3 (follow-up in the same thread)

Using my CellLineSelector work, which combines per-gene scores across six evidence layers, calibrates them across lineages and groups results into confidence tiers, explain where the analogy to a multi-stage ranking cascade holds and where it breaks. Be specific about what would not transfer.

## Notes

- Turn 3 is where the thread acknowledges the limit of your ranking experience, so do not drop it.
- Skim the answer before sharing and regenerate if it overclaims anything (for example production ranking ownership). The thread is judged as your work.
- If an answer comes out wrong, edit the Turn 1 message and rerun it instead of adding a corrective follow-up, so the bad answer is not left in the thread.
- Check against the CV: CellLineSelector and VisionCaptioner are team projects ("co-built", "we"), Best Team Project was an internal recognition, and the summary should not say "designed" or "chose" for the whole scoring system.
- Use a normal search thread (`perplexity.ai/search/...`), not a `/computer/tasks/` link, which may not be shareable. Open the shared link in a private window while logged out to confirm the answer shows.
- A first run (agent-product thread) added a "gaps" section that suggested intern roles; the extra Turn 1 paragraph forbids that. Perplexity figures it quoted (Photon 68% cost cut, DCG 2.45 to 2.21, p99 800 ms to 65 ms) were checked against its blog and were accurate.
- If you do want the CV used, paste its text minus the contact line instead of uploading the file.

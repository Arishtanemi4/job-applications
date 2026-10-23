# Aventum: "Tell me about yourself" script

For Round 1 with the Head of AI (Fri 23 Oct 2026). Built from `STRATEGY.md` (§3 positioning, §4 evidence, Honesty guardrails), your submitted CV and cover letter, and the JD. Say it in your own words; the script is a skeleton to rehearse, not to recite.

Pace: about 140 words a minute, so 60 s is about 140 words and 120 s is about 280 words. Time yourself out loud; if the main script runs past 2 minutes, cut the MSc paragraph to one sentence.

## Main script (about 110 seconds, 269 words)

> Thanks for having me. I'm Kaustubh, an AI engineer, and for the last three years my work has been taking AI from prototype into production in regulated financial services.
>
> I was at HDFC Asset Management, where the first GenAI systems were a two-person effort between my manager and me. I built RAG applications and tool-calling agents for Compliance, Client Service and Investment, on FastAPI microservices in Docker on AWS, with Azure OpenAI and a self-hosted Llama-3. I also built an event-driven pipeline that turns over 300 rating-agency emails a day into structured data, saving about 60 analyst hours a month.
>
> I'm proudest of the production discipline: Jenkins and GitLab CI/CD, role-based access against LDAP, and working with the security team until the apps passed VAPT, with Compliance reviewing every release. In my last year I acted as de facto team lead for up to four interns.
>
> Then I moved to Bristol for an MSc in Data Science, which ended in September. That gave me the modelling foundations: LSTM and attention sequence decoders in a team study, and a dissertation with AstraZeneca on a scoring and ranking tool with a RAG assistant, refined with their scientists' feedback.
>
> What draws me to this role is that it sits where I'm strongest, getting models behind APIs and into live workflows, and it pushes me into behavioural and causal modelling, which is where I want to grow. I'm upfront that I haven't shipped those yet, but since applying I've been working through sequence models, behavioural cloning and DoWhy and EconML on public data, and I'd like to apply that to real decisions here.

## Short version (about 55 seconds, about 130 words)

Use this if they say "just a quick intro" or the call is running short.

> I'm Kaustubh, an AI engineer with three years of production experience in regulated financial services. At HDFC Asset Management I built RAG applications and tool-calling agents end to end for Compliance, Client Service and Investment: FastAPI microservices in Docker on AWS, with Jenkins and GitLab CI/CD, LDAP-based access control, and a security review we had to pass. I also built an event-driven pipeline that processes over 300 rating-agency emails a day and saves about 60 analyst hours a month.
>
> I then did an MSc in Data Science at Bristol, covering LSTM and attention sequence models and a dissertation with AstraZeneca.
>
> I'm drawn to this role because it's about getting models into live decisioning, which is my strength, and it takes me into behavioural and causal modelling, where I want to grow.

## Why it is built this way

| Choice | Reason |
|---|---|
| Opens with "production, regulated financial services" | It is the one idea from `STRATEGY.md` §3 you want them to keep. The JD says "not just experimentation or notebooks" twice. |
| HDFC takes about 60% of the time | The Head of AI will probe it first ("why that architecture? what broke?"). The intro should hand them hooks you know cold: RAG per department, the email pipeline, VAPT. |
| MSc is short and says "team" | The cover letter already said your sequence modelling is academic. Don't oversell it, and both MSc projects are team projects. |
| Gaps are named in one sentence | The cover letter listed them openly and they invited you anyway. Staying consistent reads as honest and lets you steer to the work you did since applying. |
| Ends on "apply that to real decisions here" | It points at their roadmap and sets up the Digital Twin / validation questions in `STRATEGY.md` §10. |

## Numbers and claims you may use

Only these figures: **three years, 300+ emails a day, 60 analyst hours a month, up to four interns**. Do not add others.

- "Team lead" is always "acted as de facto team lead" if asked. It was never a formal title.
- Say "CI/CD through Jenkins and GitLab", not "fully automated". It was a one-click deploy to dev and prod.
- Say "access against LDAP", not SSO or OAuth.
- Say "team architecture study" and "co-built dissertation". Don't say "I led", and don't claim you beat BLIP/SigLIP or quote CellLineSelector metrics.
- The last line ("since applying I've been working through...") is true only if you have done the notebooks. If you haven't finished them, swap it for: "...and I'd like to start applying that to real decisions here."

## Swaps for the context

- **If they open with "walk me through your CV":** this script is the answer. Stop after the HDFC and MSc paragraphs if they look keen to dig in, and finish with the "why this role" line.
- **If the interviewer is research-leaning:** move the MSc paragraph before the "production discipline" paragraph and add: "In the VisionCaptioner project I compared LSTM decoders with and without Bahdanau attention across five seeds."
- **If the interviewer is engineering-leaning:** drop the MSc paragraph to one sentence and spend the time on the Llama-3 vs Azure OpenAI trade-off ("self-hosted for the largest department for cost, Azure for decision makers for quality, models switchable").
- **Why leave HDFC (likely follow-up):** "A planned move to study. I left in July 2025 to do the MSc."

## Delivery

- Look at the camera at the start of each paragraph, not through it. Pause after "...into production" and after "...where I want to grow".
- End on the last sentence and stop. Then offer a thread to pull: "Happy to go deeper on the architecture or the email pipeline."
- Rehearse it three times out loud on Thursday and once on Friday morning (`STRATEGY.md` §2). Record one run and check it lands between 100 and 120 seconds.

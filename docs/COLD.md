# Cold Outreach Strategy

Written 2026-10-19. A plan for moving from portal-only applications to people-first outreach.

---

## 1. Where things stand

- `ApplicationTracker.xlsx`: **61 portal applications**, **9 rejected**, **51 awaiting reply**, **0 interviews logged**.
- Because there are no interviews yet, the problem is **getting past screening**, not interviewing. The CVs are tailored, but an ATS or a recruiter skimming 300 applications rarely gives a profile like mine (Indian experience, a new UK MSc, Graduate Visa) a second look.
- Outreach fixes this by putting a person between me and the ATS, someone who can say "look at this one".

---

## 2. The short answers

### Which of the three options?

**Do option 2 now, run a targeted version of option 1 alongside it, and drop option 3.**

| Option | Verdict | Why |
|---|---|---|
| 1. Cold-message random people on LinkedIn | **Change it to targeted cold** | Messages to random people have a near-zero reply rate and use up my weekly LinkedIn invite limit. Messages to the **hiring manager or an engineer on the team behind a live role** get replies. |
| 2. Start with my UK industry connections | **Start here, this week** | Warm contacts reply 3 to 5 times more often than cold ones, and they can forward me internally, which cold contacts almost never do. |
| 3. Hold the connections back until cold outreach fails | **Don't** | Explained below. |

**Why holding the connections back is a mistake:**

1. **Warm connections go cold.** A judge from Project Hack 27, an AstraZeneca scientist from the dissertation or a datathon sponsor remembers me *now*. Six months from now I am just a name. Their value falls every month I wait.
2. **Connections are not used up by asking for small things.** The worry behind option 3 is "I only get one ask per person". That holds only if the first ask is a big one. Use an **ask ladder** instead:
   1. **Advice:** "15 minutes on how your team hires for X?" Nearly everyone says yes.
   2. **Intro:** "Who should I talk to about the ML team?"
   3. **Referral:** only when they have a real role open and they offer, or the conversation has earned it.

   Most contacts only ever get rung 1, and that is fine. Rung 1 often turns into rung 3 without me asking.
3. **The visa clock is running.** The Graduate Visa gives a fixed window. Every month spent on low-yield cold outreach before using warm contacts is a month of that window gone.
4. **Cold outreach doesn't "fail" in a clean way.** It just trickles. There would never be a clear moment to switch, so the warm contacts would sit unused.

### Should I hold the referral until I have 3 or 4 interviews?

**No. Use it as soon as that company has a role that fits me well.**

- **Roles close and people move on.** The referrer could change team, leave, or lose context on me, and the role could be filled. A referral held back for months can disappear.
- **The bottleneck is getting interviews, and the referral is the strongest tool I have for that.** Waiting for 3 or 4 interviews before using it is backwards: the referral is how the *first* interview happens.
- **The practice worry is solved another way.** A referred application at a large company still takes 2 to 4 weeks to reach a first round. That gap is my practice window: do mock interviews (section 10) and take any outreach-generated calls.
- **What to do this week, before any formal ask:** message the referrer for a 15-minute call about the team, the interview loop and which open role fits me best. This costs nothing, keeps the connection warm and makes the eventual referral much stronger, because they can then refer me to a specific role with a specific reason.
- **The only reason to wait:** `<ReferralCompany>` has **no open role that fits me** right now. In that case keep in touch (one useful message a month) and set a job alert for that company's careers page.

---

## 3. Contact tiers

Each tier gets a different ask. Never use a Tier C template on a Tier A person.

### Tier A: warm (I have met them or worked with them)
Start here. Aim for 15 to 25 people.

| Source | Who to look for |
|---|---|
| MSc dissertation with AstraZeneca | The scientists who gave feedback on CellLineSelector, and the project supervisor(s) |
| Project Hack 27 (Rolls-Royce Derby, 4th place) | Judges, mentors, organisers (Projecting Success), Rolls-Royce people met there, other teams |
| Encode Vibe Coding Hackathon (codeplain track, 2nd place) | Codeplain team, judges, Encode organisers, sponsors |
| University of Bristol Datathon (Lloyds sponsored, 3rd place) | Lloyds people met there, organisers |
| Swindon Borough Council fuel-poverty hack | Council data team, organisers, mentors |
| University of Bristol | Lecturers, project supervisors, careers / employability team, industry guest speakers |
| Any UK meetups, conferences or events I attended | Speakers and attendees I spoke to |

**Ask:** reconnect, give a short update, then advice → intro.

### Tier B: lukewarm (a shared link, not met)
- University of Bristol alumni working in AI, ML or data roles (LinkedIn → University of Bristol page → Alumni → filter by company and "data" / "machine learning").
- Former HDFC AMC and NMIMS people now in the UK.
- People I share hackathon communities, Discords or Slack groups with.

**Ask:** "I'm a fellow Bristol MSc / ex-HDFC, could I ask you 2 questions about X team?"

### Tier C: targeted cold (no link, but a reason)
- The **hiring manager** for a live role (Head of ML, Engineering Manager, CTO at a startup).
- **An engineer on that team** (often more likely to reply than the manager).
- **Founders and CTOs at seed to Series B startups**, where there is often no portal at all.
- **Specialist recruiters** for AI / data / ML (Saragossa and Linux Recruit were already this kind; see the recruiter workflow memory).

**Ask:** one specific thing connected to one specific role.

---

## 4. Targeting: which companies

1. **Filter for sponsors.** Every target should appear in `LiscensedSponsors.csv` (Worker, Skilled Worker route), so I can move from the Graduate Visa to Skilled Worker later without changing jobs. Claude Code can check a list of names against the CSV.
2. **Build a list of 40 to 60 companies** across the core roles (AI / GenAI engineer, FDE, MLE, DS, SDE, DE, MLOps). For each one, record why I fit in one line.
3. **Split the list by approach:**

| Company type | Best channel | Why |
|---|---|---|
| Seed to Series B startups, AI consultancies | **Cold DM or email to the founder or CTO** | Small teams, founders read their own inbox, often no ATS |
| Scale-ups (200 to 2,000 people) | **Apply, then message the hiring manager** | A human message moves an application up the pile |
| Big tech, banks, large corporates | **Portal + referral + alumni** | Cold messages to big-company managers rarely work; referrals do |
| Recruiters (agency) | **Email with CV attached** | They are paid to place people, so they reply when the profile fits |

4. **Strongest fit to lead with:** companies where my HDFC story counts directly, i.e. **FDE and GenAI roles at fintech, asset management, insurance and financial-services AI firms** (end-to-end RAG for Compliance, Client Service and Investment teams; Morningstar data platform; rating-email automation), plus **biotech / health-data AI** for the AstraZeneca dissertation.

---

## 5. Finding the right person and their address

- **LinkedIn:** the company page → People → search "machine learning", "data", "AI", "engineering manager". The job post itself often shows "Meet the hiring team".
- **Company email format:** find one public address (blog, GitHub commits, conference talk), then use the same pattern (`first.last@`, `first@`). Free tiers of Hunter.io or Apollo check the pattern. Never guess more than two variants.
- **Who's talking publicly:** the engineering blog, conference talks, GitHub org, podcasts. These are also the best hook ("I read your post on X").
- **LinkedIn limits:** free accounts get roughly 100 to 200 invites a week, and notes on invites are limited. Spend them on Tier A, B and C targets, never on random people. Email is not capped, so use it for Tier C where I can find the address.

---

## 6. Message templates

Rules for every message:
- **One ask.** Never "any advice, roles or referrals?".
- **One proof link** that fits the role:
  - GenAI / AI engineering: Wingman, https://github.com/Arishtanemi4/wingman.git
  - Data science / bio / data work: the CellLineSelector demo, http://celllineselector-frontend-408937187029.s3-website.eu-west-2.amazonaws.com/
  - General: https://github.com/Arishtanemi4
- **Claims only from `cv/EXPERIENCE.md`.** The allowed numbers are 300+ emails a day, 60 analyst hours a month, 10 hours a week and 3 years. The MSc is "awaiting result". No "led" (use "de facto team lead" or "led a small team of interns"). Use "Azure OpenAI", not "OpenAI".
- **Visa line, always:** "I'm in Bristol and eligible for the Graduate Visa, so I have full UK work rights with no sponsorship needed to start." Hiring managers worry about visas, so remove the worry up front.
- **Short.** Connection notes up to 300 characters, DMs up to 100 words, emails up to 120 words.

### 6.1 Warm reconnect (Tier A)
> Hi `<Name>`, hope you're well! We met at `<event>` when my team `<what we did / placed>`. I've just finished my MSc Data Science at Bristol (awaiting result) and I'm now looking for AI / ML engineering roles in the UK. Before that I spent 3 years building GenAI and RAG apps end to end at HDFC Asset Management.
>
> Would you be up for a 15-minute chat about how `<their company / team>` hires for this kind of role? Totally fine if not.

### 6.2 LinkedIn connection note (Tier B and C, up to 300 characters)
> Hi `<Name>`, Bristol MSc Data Science grad, 3 yrs building GenAI/RAG apps end to end at HDFC AMC. Really interested in `<team / product>` at `<Company>`. Would love to connect and ask one quick question about the team.

### 6.3 Follow-up DM after they accept
> Thanks for connecting, `<Name>`! Quick context: at HDFC AMC I designed and built RAG applications for Compliance, Client Service and Investment teams (React, FastAPI, pgvector, Azure OpenAI and a self-hosted Llama-3 on AWS), and an email pipeline that saved analysts 60 hours a month.
>
> I saw the `<Role>` opening on your team. Is it the kind of role where hands-on GenAI delivery like this counts, or is it after something different? I'm on the Graduate Visa route, so no sponsorship is needed to start.

### 6.4 Cold email to a founder or hiring manager (Tier C)
**Subject:** `<Role>`: built production RAG for an asset manager's Compliance and Investment teams

> Hi `<Name>`,
>
> `<One line on why them: their post, product or launch>`.
>
> For 3 years at HDFC Asset Management I designed and built GenAI applications end to end: a React frontend, FastAPI microservices in Docker, department-siloed pgvector stores, and Azure OpenAI alongside a self-hosted Llama-3 on AWS, deployed through Jenkins and GitLab. The department RAG chatbot won an internal Best Team Project award in 2025. I've just finished an MSc Data Science at Bristol (awaiting result).
>
> I think this fits `<specific problem from the JD or product>`. Would a 15-minute call make sense? CV attached; example work: `<proof link>`.
>
> I'm eligible for the Graduate Visa, so no sponsorship is needed to start.
>
> Kaustubh

### 6.5 After applying: note to the hiring manager
> Hi `<Name>`, I've just applied for `<Role>` (`<job ID>`). The short version of why: `<one line that maps my strongest HDFC bullet to their top requirement>`. If it helps, I can send a 2-minute walkthrough of the RAG system I built. I'm on the Graduate Visa route, so no sponsorship is needed to start. Thanks either way!

### 6.6 Asking for the referral
Only after a conversation. Make it easy for them to say yes, or to say no without awkwardness:
> Thanks again for the chat, `<Name>`, it really helped. The `<Role>` (`<link / ID>`) looks like the strongest match. Would you be comfortable referring me? Completely fine if not. If it helps, here's a blurb you can paste:
>
> *"Kaustubh has 3 years building production GenAI and RAG applications end to end at HDFC Asset Management (React, FastAPI, pgvector, Azure OpenAI, AWS) and has just finished an MSc Data Science at Bristol. He's on the Graduate Visa route, so no sponsorship is needed to start."*

(Change the blurb to suit the role. For DS or DE roles, lead with the Morningstar data platform or the AstraZeneca dissertation instead.)

---

## 7. Cadence

| Activity | Per day | Per week |
|---|---|---|
| Tier A warm messages | 3–5 (until the list is done) | 15–25 |
| Tier B / C targeted messages | ~10 | ~50 |
| Portal applications (keep going, aim lower) | 1–3, the strongest fits only | 5–15 |
| Follow-ups | as they come due | — |

- **Follow up twice, then stop:** once on day 4 or 5 ("bumping this in case it got buried"), once on day 10 with something new (a project update, a relevant post). After that, stop. Mark it "No reply" and move on.
- **Time-box it:** about 90 minutes a day for outreach. Mornings work best; Tuesday to Thursday get the best replies.
- **Apply first, then message** for any company with a live posting, because a cold message without an application usually just gets "please apply through the portal".

---

## 8. Tracking

Add an **Outreach** sheet to `ApplicationTracker.xlsx` (or a separate workbook) when outreach starts. Suggested columns:

`Date | Contact | Title | Company | Tier (A/B/C) | Channel (LinkedIn / Email / Event) | Ask (Advice / Intro / Referral / Role) | Linked application (row / role) | Follow-up 1 | Follow-up 2 | Reply? | Outcome (Call / Referral / Interview / No / No reply) | Notes`

Keep one row per person. Link it to the application row when one exists.

---

## 9. Metrics and when to change course

Review every Friday.

| Metric | Healthy | If below |
|---|---|---|
| Tier A reply rate | 30–50% | The message reads as a favour request. Lead with the update and make the ask smaller. |
| Tier C reply rate | 10–20% | The hook is generic. Personalise the first line and tie it to one live role. |
| Replies → calls | ~30% | The ask is unclear or too big. Ask for 15 minutes, not "any opportunities". |
| Calls → referrals or interviews | ~25% | The story needs work. Practise the 60-second pitch (section 10). |

- **After 2 weeks:** if Tier C is under 10%, rewrite the templates before sending more.
- **After 4 weeks:** if Tier C is working better than portal applications, cut portal applications further. If not, change the targeting (company type or role family), not the effort.

---

## 10. Be ready for interviews (in parallel)

Outreach calls and the referral are worth nothing if I'm not ready to interview. Start now, not after the interviews arrive.

- **A 60-second pitch** that answers "tell me about yourself": HDFC end-to-end GenAI → the Bristol MSc → why this role.
- **A story bank (STAR)** from `cv/EXPERIENCE.md`:
  - siloed RAG per department
  - the cost-aware Llama-3 / Azure OpenAI split
  - Textract → Azure OpenAI when an agency switched to image emails
  - getting through VAPT
  - the React recreation of the Power BI dashboards
  - working with the AstraZeneca scientists
  - leading interns as de facto team lead
- **Technical prep for each role family:**
  - RAG system design, ML fundamentals and evaluation for GenAI / MLE roles
  - SQL and Python for DS / DE roles
  - LeetCode-style practice for SDE roles
- **Mock interviews:** the University of Bristol careers service (alumni access usually continues after graduation), peers from the MSc, Pramp-style platforms. Aim for 2 mocks a week until the first real interview.
- Close the S-tier gaps in `cv/GAPS.md`. Each one closed also gives a fresh, genuine reason to follow up ("I've just shipped X").

---

## 11. Workflow with Claude Code

- For each target company: give Claude Code the company, the person (name, title, any public post) and the role.
- Claude drafts the message in `jobs/{company}/`, the same pattern as the Saragossa and Linux Recruit recruiter workflows: a connection note, DM or email, plus a tailored CV if there is a live role.
- **I send every message myself. Claude does not send anything.**
- Log every outreach in the tracker (section 8).

---

## 12. 30-day plan

| Week | Focus | Targets |
|---|---|---|
| **1** | Warm first + referral | List every Tier A contact. Send all Tier A reconnects (15–25). Book the 15-minute call with the referrer and pick the target role at `<ReferralCompany>`. Build the 40–60 company list (sponsor-checked). Add the Outreach sheet. Write the 60-second pitch. |
| **2** | Referral in + targeted cold starts | Submit the referred application if a role fits. Start Tier B / C at ~10 a day. Follow up on week-1 messages. 2 mock interviews. |
| **3** | Volume + calls | Keep 50 targeted messages a week. Take every advice call and move up the ask ladder where it's earned. 2 mock interviews. First Friday metrics review. |
| **4** | Review and adjust | Compare reply rates against section 9 and rewrite templates or targeting. Decide how much portal time to keep. Second warm touch for Tier A people who replied (a useful update, not another ask). |

---

## 13. Visa timing note

- The CV says "Student Visa, eligible for Graduate Visa (2 years full working rights)".
- The Graduate Visa has to be applied for **from inside the UK, before the Student Visa runs out**, and the rules on its length have been under review. **Check gov.uk ("Graduate visa") for the current length and deadline.** If the window is shorter than 2 years, the case for using warm contacts and the referral *now* gets even stronger.
- Once the Graduate Visa is granted, the visa line in every template ("no sponsorship needed to start") is a real advantage. Lead with it.

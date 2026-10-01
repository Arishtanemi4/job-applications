# Kaustubh Sonawane — Experience Bank

## How to use this file

- Source of truth for tailoring resumes and cover letters. Pull the bullets relevant to the target role (see **Role → Evidence Map**) and lift them into the tailored CV.
- Bullets use the wording of `KaustubhSonawaneCVUK` so they can be pasted directly. Keep the bolded keywords.
- Only use the numbers listed here. Do not invent metrics. If a JD needs a skill not listed here, ask before claiming it.

## Profile Snapshot

- Based in Bristol, UK. UK Visa: Student Visa, eligible for Graduate Visa (2 years full working rights).
- ~3 years industry experience (GenAI, data, MLOps), plus an MSc in Data Science. Left HDFC in July 2025 to pursue the MSc.
- **University of Bristol — MSc Data Science** (Sep 2025 – Sep 2026, awaiting result). Do not claim a result or classification.
- **NMIMS — B.Tech Information Technology + MBA Technology Management** (dual degree, Jun 2017 – Apr 2022).

## Work Experience

### HDFC Asset Management Company Ltd. — AI Solutions Engineer / Forward Deployed Engineer
*July 2022 – July 2025*

#### Team & Leadership
- **Year 1:** just the candidate and their manager; the candidate designed and built the first GenAI systems.
- **Year 2:** a more senior engineer joined, who also led some resources, and a **dedicated frontend developer** joined.
- **Year 3:** **2 to 4 interns** (4 at the peak, 2 on average) worked under the candidate. The candidate acted as a **de facto team lead**, apart from the senior engineer. By the end there were **two leads in the GenAI team**, each leading a smaller team.
- Worked directly with the **Client Service, Compliance and Investment** departments, plus marketing (Apriori insights).
- **Recognition (internal):** **Best Team Project 2024** for the **rating-change email automation**, and **Best Team Project 2025** for the **department-specific RAG chatbot**. The awarding body is not specified.
- Left in July 2025 to study the MSc in Data Science at the University of Bristol.

#### RAG / GenAI Engineering
- **Designed and built the GenAI applications end to end:** the complete system, covering the **frontend**, **backend**, **GenAI / RAG logic**, **vector database** and **embeddings** pipeline, not just the model layer. Initially the sole engineer (with the manager); later led as the team grew (see Team & Leadership).
- **Architecture of the GenAI applications:** **ReactJS** frontend served by **Nginx** on one **AWS EC2** instance; **Python FastAPI** backend built as **microservices** on a separate **EC2** instance; frontend and backend deployed via a **Jenkins + GitLab CI/CD pipeline**.
- **Department-based RAG with siloed vector databases:** the RAG system served several departments (**Compliance, Client Service, Investment team**), each with its own documents. Access was department-based, so each department had its **own separate vector DB**, which siloed the embeddings. This was an early stage of RAG development, and GPT-3.5 and Llama-3 were not good at telling similar content apart across departments.
- **Cost-aware model allocation:** **Llama-3 self-hosted on a GPU EC2 instance** served the Client Service department (the largest, so this saved cost). The other departments used the **Azure OpenAI API**. Llama-3 was an economic decision with the capability to switch models and deploy at scale; the better Azure OpenAI outputs were kept for decision makers.
- **Containerization:** the FastAPI microservices were packaged as **Docker** containers running **uvicorn** on port 8000.
- **Release and iteration:** the apps were released to real users (department members) and changed based on what was found. **Prompts were versioned in Git commits.** No fine-tuning; behaviour was guardrailed through **system prompts**. The **Compliance** department always reviewed the applications. No formal golden datasets, LLM-as-judge or eval tooling were used, so don't claim them.
- **Agentic / tool-calling:** AI agents call **Python functions** as tools, implementing the math formulae a mutual fund house needs to compare two or more funds, and plot the comparison into a **PDF** on user request. The same comparisons are also available in the frontend directly, with no AI tool call.
- **ExpressJS (development phase only):** built **ExpressJS** APIs for the same project during development, to serve the fund-comparison calculations because the Python APIs were slower. The final backend was Python FastAPI.
- Developed **GenAI applications** using **LlamaIndex** and **Azure OpenAI GPT-3.5 & Llama-3** for internal company use to answer department-specific queries.
- Designed and maintained a **Vector Database** using **pgvector** and the **Azure OpenAI embeddings model** to enable efficient semantic search and retrieval across internal company documents.
- Developed a **Python** automation job utilizing **AWS Textract** to parse over **300 daily emails**, transforming unstructured data into a structured format and **saving 60 manual analyst hours a month**.
- **How the email pipeline works:** emails from credit rating agencies (**ICRA, India Ratings, CRISIL** and others) arrive in a **shared inbox**. The job runs on **AWS SageMaker**, triggered at 9 AM by EventBridge → Lambda. The agencies' emails list rating changes, but only for some of the companies and bonds do the analysts care. The pipeline parses them (first with AWS Textract, later with Azure OpenAI), uses **fuzzywuzzy** to fuzzy-match **company names** against the companies the analysts track, and drops the rest. It then sends the analyst a **daily consolidated email** with each tracked company's **previous and changed rating**, and stores an **Excel** file of the same in **S3**. Analysts no longer have to monitor the agencies by hand. This pipeline is the only use of SageMaker. **History:** the first version parsed the emails with **AWS Textract**. It was later upgraded: **Azure OpenAI replaced Textract**. The trigger was that one rating agency started sending its emails as an **image instead of text**, which broke the Textract-based parser; Azure OpenAI was the robust fix, and its performance/accuracy was also much better. The 300+ emails/day and 60 hours/month figures hold for both versions. For GenAI-flavoured roles, lead with the Azure OpenAI version and mention Textract as the first iteration; for data/cloud roles, either version works.

#### Data Analysis
- Analyzed customer data and drew insights using **Python Pandas**. Pandas was used in virtually every project: data jobs, backend APIs and RAG pipelines. It was integral to the day-to-day work.
- Developed **Power BI** dashboards for fortnightly credit report analysis, migrating financial analysts from **Excel to Power BI** and improving analyst efficiency by **10 hours a week**. The dashboards were built for the **investment team**.
- **Democratized the dashboards in React:** Power BI licensing was too costly to scale to the nationwide client service team (head office and branches), so the **ReactJS frontend** of the GenAI project includes a **complete recreation of the Power BI dashboards**. This gave the whole organization access to the data at lower cost, with the comparisons available directly in the UI without any AI tool call.
- Identified customer buying patterns using **Market Basket Analysis** by implementing the **Apriori Algorithm**. The results were analysed and handed to the **marketing team** as insights; how to act on them was entirely the marketing team's decision.

#### Data Engineering
- Designed the **entire database schema** (**Normalized SQL Schema**) for the internal analytics platform, executed by the candidate to the analysts' requirements and guidance.
- Ingested and processed incoming **Morningstar** data to the company's requirements, and **integrated it seamlessly with the legacy data** the company already maintained (previously held in analysts' Excel files). The new data was much richer than the old.
- **Ingestion:** wrote the **Python scripts** that call the enterprise-licensed **Morningstar API**, refreshing the data **fortnightly for fixed income funds** and **monthly for equity funds**. The data covered **every fund in the Indian mutual fund market** over 2023–2025. The database is **PostgreSQL**; the pgvector data sits on the same server in a separate schema.
- This is why the role is both **Forward Deployed Engineer** (built directly with the analysts, to their requirements) and **Data Engineer**.
- The GenAI application reuses this data: its **Python functions run SQL queries** to fetch it for fund-house comparison and fund-performance comparison.
- Developed **Optimized SQL** queries for data preprocessing.
- Developed **SQL Functions** and **Procedures** for efficient data insertion.

#### MLOps / Infrastructure
- Designed the infrastructure architecture for internal analytics platforms and GenAI applications on AWS utilizing core services such as **EC2, S3, ECR, and Lambda**.
- Scheduled the email-automation pipeline (hosted on **AWS SageMaker**): an **AWS EventBridge** rule fires at 9 AM and triggers an **AWS Lambda** function that runs the SageMaker pipeline.
- Provisioned new **EC2** instances using **CloudFormation** templates prebuilt by the security team (used the templates, did not author them).
- Configured **AWS Security Groups** so that only **company private IPs** could reach the internally deployed apps.
- Acted as the **coordinator with the security team**: worked out which ports needed whitelisting and which safeguards had to be maintained during development, following the security team's instructions.
- Implemented **RBAC (role-based access control)** for the GenAI apps, alongside the department-based access to documents. Wrote a **Python authentication function** that connects to the company **LDAP** server to authenticate users. There were **3 tiers**: department heads and managers (high), team leads (mid), executives (low).
- Deployed an **Nginx** reverse proxy, one of the security fixes that took the application from repeatedly failing to **passing the VAPT** (Vulnerability Assessment and Penetration Testing) by the security team. (The CV's "below 1%" figure is unverified, so don't quote it.)
- Built the deployment automation with **Jenkins** and **GitLab**: a **one-click deploy button in Jenkins** runs the deployment script for the chosen **dev** or **prod** branch. There were two environments (dev, prod), since these were internal apps, with provision made to add more. The frontend and backend lived in **separate repos**, each with its own **dev and prod branches** and its own **Docker container**, and the pipeline deployed both.
- Ran the main backend microservices from a single **Anaconda Python** environment packaged in **Docker**, with the email-automation job kept completely separate from it. (The CV's "multiple Anaconda environments" overstates this, so don't use that wording.)

## Additional Full-Stack & Cloud Experience

Skills the CV under-sells. All of them were used in the HDFC role (Jul 2022 – Jul 2025), mainly while building and deploying the end-to-end GenAI applications above. Use them when a role needs full-stack, backend or cloud depth. No metrics have been supplied for these, so don't add numbers.

- **Python backend development:** FastAPI, uvicorn.
- **Node.js:** ReactJS frontend (production); ExpressJS APIs (development phase only, see above).
- **Nginx:** deploying and serving the ReactJS frontend on EC2.
- **AWS:** EC2, ECR, Lambda, EventBridge; CloudFormation (used security-team templates to provision EC2, not authored).
- Overall: a proper **full-stack** profile (frontend, backend, GenAI/RAG, deployment, cloud), designed by the candidate and shipped first as the only engineer, later with a team they led.

Confirmed mapping for the GenAI applications: ReactJS frontend (Nginx, own EC2 instance), Python FastAPI microservices backend in Docker with uvicorn on port 8000 (own EC2 instance), Jenkins + GitLab CI/CD. Lambda + EventBridge belong to the 9 AM email-automation pipeline on SageMaker, not the GenAI apps.

## Projects

- **MSc Dissertation with AstraZeneca (Univ. of Bristol):** CellLineSelector, an algorithm to rank the best-suited cell lines based on target inclusion and exclusion genes. GitHub: https://github.com/Arishtanemi4/az-team25.git. Demo (frontend on S3): http://celllineselector-frontend-408937187029.s3-website.eu-west-2.amazonaws.com/
  - **Data sources (confirmed by candidate):** **DepMap**, **GEO** and **HPA**. (The earlier notes also list Cellosaurus and CCLE for identity bridging; CCLE data is distributed via DepMap.)
  - **Team project, co-built.** Commits were mostly joint, often from one laptop, with the team working together in the library, so "co-built" is accurate for the whole system. Personal focus: the **data preprocessing**, the **scoring algorithm** and the **RAG layer** (candidate designed it). Team size and other members not stated in the repo.
  - **Scientist feedback and validation (confirmed by candidate):** interacted directly with AstraZeneca scientists for feedback, and the ranking was validated. How it was validated (against what reference) and any results are not recorded, so don't describe the method or quote numbers.
  - **What it does:** a researcher supplies genes to include and exclude, and the tool returns a short ranked list of cancer cell lines with the evidence behind each pick. An AI assistant narrates results and answers methodology questions. About **2,100 cell lines** and six evidence layers (RNA expression, protein, dependency, copy number, mutation, fusion).
  - **Preprocessing (`preprocessing/`):** a pipeline that reads 17 raw and augmented inputs and builds **14 clean, joined tables** (CSV and Parquet). It covers identity resolution (bridging model and profile IDs and gene symbols across Cellosaurus, CCLE, HPA and GEO sources), duplicate handling, missingness (a detection floor for protein), scaling (log2 TPM, z-scores) and joins. It enforces integrity checks (every input read, no duplicate model/gene keys) and writes a `build_manifest.json` audit file.
  - **Scoring (`scoring/`):** per-gene **desirability scoring** across the evidence layers (weighted by layer, with the gene's inclusion/exclusion role deciding the direction), **correlation weighting** across genes, and a veto for exclusion genes. A **calibration** step keeps scores comparable across lineages. Cell lines are ranked by the final score and grouped into confidence tiers (High, Moderate, Low, Insufficient), with similar backup lines attached.
  - **System stack (team):** five FastAPI services (genes, scoring, RAG, data, research), a React + TypeScript frontend, Docker Compose, Git LFS, a RAG layer. The RAG layer is confirmed as candidate-designed; for the other parts say "co-built" with the team, and don't single them out as personally owned.
- **MSc Applied Data Science Group Project:** VisionCaptioner, a multi-phase architecture study comparing CNN/ViT/ResNet encoders and LSTM/attention/transformer decoders for generating natural-language image descriptions, benchmarked against BLIP/SigLIP and commercial VLMs. GitHub: https://github.com/Arishtanemi4/ata-team30.git
  - **Team project (5 authors).** Report: "Image Captioning of Synthetic Scenes: A Multi-Architecture Study". The report has no contribution statement and the repo doesn't say who did what. All team members discussed every part and understand each aspect in depth, so no personal split is recorded. Describe it as a team effort across the whole study.
  - **Setup:** three synthetic datasets (tic-tac-toe boards, multi-digit numbers, coloured shapes), 10,000 images each, 70/15/15 split. Encoders trained from scratch: SimpleCNN, DeeperCNN, ResNet-18, custom ViT. Decoders: symbolic, embedding (SBERT retrieval), LSTM sequence, with global pooling or Bahdanau attention. Adam, 30 epochs, five seeds. Metrics: SBERT cosine (primary), BLEU, ROUGE-L.
  - **Results:** best seed-mean validation SBERT cosine of 0.998 / 0.937 / 0.895 (tic-tac-toe / numbers / shapes). Benchmarked against six pre-trained VLMs: BLIP scored 0.000 / 0.000 / 0.120 on caption correctness, SigLIP did best on shapes (0.860, but as a retrieval task), and GPT-4o and Claude beat the team's models on numbers. The report says the protocols differ, so the cross-model numbers are not directly comparable.
  - Numbers above come from a web summary of the report. Check them against `report/team30.tex` before quoting.
- **B.Tech Final Year Project:** Udacity self-driving car simulator, a self-driving car trained using a **Convolutional Neural Network (CNN)** model.
- **Pauti:** expense tracking and payment splitting Android app, offline-only and privacy-first using a **CRDT** architecture. GitHub: https://github.com/Arishtanemi4/pauti.git
- **Swindon Borough Council Fuel-Poverty Hack:** household and neighborhood-based fuel poverty data analysis tool. GitHub: https://github.com/Arishtanemi4/fuel-poverty.git
- **Contact Reminder:** Android app that texts contacts on important dates (birthday, anniversary), with phone call and WhatsApp integration. GitHub: https://github.com/Arishtanemi4/contact-reminder.git

## Achievements

- **Project Hack 27:** Rolls-Royce Derby, 4th place. Human-centric data analytics tool to predict the competition winner from wellbeing and psychological temperament survey data. GitHub: https://github.com/Arishtanemi4/team-4b.git
- **Encode Vibe Coding Hackathon:** Codeplain.ai track, 2nd place. Wingman.ai, an AI-powered dating app simulation built with codeplain's spec-driven framework. GitHub: https://github.com/Arishtanemi4/wingman-codeplain.git
- **University of Bristol Datathon (sponsored by Lloyds Bank):** 3rd place. Kaggle credit card fraud detection problem.

## Skills Inventory

- **Tools:** Jupyter, Anaconda, AWS, Azure OpenAI, Power BI, Nginx, Git, Putty, Linux, LDAP (authentication/RBAC), VS Code, Docker, Jenkins, GitLab, Claude Code.
- **Languages:** Python (pandas, FastAPI, uvicorn, scikit-learn, fuzzywuzzy), R (dplyr, tidyverse, ggplot2), Node.js (Express, ReactJS), Shell.
- **Databases:** PostgreSQL (schema design, functions and procedures, pgvector), SQLite.
- **Data sources/APIs:** Morningstar API, rating-agency emails (ICRA, India Ratings, CRISIL).
- **Cloud:** AWS (EC2 incl. GPU EC2 hosting self-hosted Llama-3, S3, ECR, Lambda, EventBridge, SageMaker, Textract, Security Groups; CloudFormation as a user of prebuilt templates), Azure OpenAI.

## Role → Evidence Map

| Role | Lead with | Supporting |
|---|---|---|
| AI Solutions / GenAI / Agentic AI Engineer | End-to-end ownership of GenAI apps, RAG stream, Azure OpenAI, LlamaIndex, pgvector | Email-parsing automation (Textract → Azure OpenAI), Wingman.ai, FastAPI |
| Forward Deployed Engineer | HDFC title match, end-to-end delivery for internal stakeholders, Power BI migration | Full-stack + AWS deployment |
| Machine Learning Engineer | CNN, VisionCaptioner, MSc ML work | MLOps stream; SageMaker (email pipeline only, not model training) |
| Data Scientist | Bristol MSc, AstraZeneca dissertation, Apriori, Pandas | Hackathon wins |
| Software Development Engineer / Full Stack | End-to-end GenAI apps at HDFC (frontend + backend + deployment), React recreation of Power BI dashboards, Node/React/Express, FastAPI, Nginx, AWS | Pauti, Contact Reminder |
| Data Engineer | Morningstar ingestion + legacy data integration, full schema design, SQL functions/procedures, email-parsing pipeline (Textract → Azure OpenAI) | Lambda, EventBridge, S3, SageMaker |
| DevOps / MLOps / Infra Engineer | AWS stack (EC2, ECR, Lambda, EventBridge, SageMaker), Jenkins/GitLab CI/CD, Docker, Nginx, Security Groups | Linux, CloudFormation (template user only) |

## Guardrails

- Quantified claims allowed: 300+ daily emails, 60 analyst hours/month, 10 hours/week, 3 years experience.
- Do NOT quote "external security threat below 1%". It has no known measurement behind it. Use the VAPT outcome instead: the app was repeatedly failing VAPT, and the Nginx reverse proxy was one of the fixes that got it through. Don't claim Nginx alone did it, and don't name the security tooling (unknown).
- MSc result is pending. Say "awaiting result".
- The extra full-stack and cloud skills are HDFC skills, so they can sit under the HDFC role. They have no numbers, so don't add any.
- Projects: keep project entries at CV-bullet depth; the team all discussed every part and knew each aspect in depth. Both MSc projects were team projects. For CellLineSelector, "co-built" is accurate (joint commits, pair-programmed); name preprocessing, scoring and the RAG layer as the candidate's focus. Never say "led". For VisionCaptioner keep "team project" wording, as no personal split is recorded. Don't quote metrics for CellLineSelector (none in the repo). VisionCaptioner: the CV mentions "transformer decoders" but the report lists symbolic, embedding and LSTM decoders, so confirm before using that wording. The VLM comparison is not like-for-like, so don't say the team's models "beat" BLIP or SigLIP without that caveat.
- Data scale: say "every fund in the Indian mutual fund market (2023–2025)". Don't state fund, row or record counts (not remembered). Refresh cadence: fortnightly (fixed income), monthly (equity).
- Power BI / dashboards: don't state the number of dashboard users. Say the React recreation made the data available to the wider organization at lower cost, but don't invent a cost-saving figure.
- Apriori: insights were handed to the marketing team, who made the decisions. Don't claim revenue or campaign impact. (Which customers and items were analysed, and what the marketing team did with the insights, is not known, so don't describe them.)
- RAG: don't state user counts, document counts or query volumes (not supplied). Say "multiple departments (Compliance, Client Service, Investment)". Llama-3 served Client Service only; other departments used the Azure OpenAI API. Name it "Azure OpenAI", not plain "OpenAI", for the GenAI apps. Don't claim a single shared vector DB.
- Rating-email pipeline: the pipeline filters agency rating-change emails to the analysts' tracked companies via fuzzy name matching. It does not itself detect changes, because the agencies only send changed ratings. Don't claim change detection or rating prediction.
- Textract: only the first version of the email pipeline used it. The current/final version used Azure OpenAI. Don't present Textract as the final parsing method. The switch was triggered by a rating agency sending image emails (not purely for accuracy).
- SageMaker: used only to run the rating-email pipeline. Don't claim SageMaker for model training, general data pipelines or ML deployment.
- Security: the work was Security Groups restricted to company private IPs, the Nginx reverse proxy, RBAC, and coordinating with the security team on port whitelisting and development safeguards. Don't claim penetration-test remediation, TLS/encryption design, SSO or IAM design beyond that. Authentication was LDAP (say "LDAP", never "RDAP", and not SSO or OAuth). It is not specified what each of the 3 tiers could access, so don't describe tier permissions. The security team owned the standards and the VAPT.
- S3: only holds the Excel output of the rating-email pipeline. It was a stop-gap, because a database was not approved for that project at the time, and the move to a DB never happened. Don't present S3 as a data lake or a deliberate storage architecture.
- CI/CD: deployment was triggered by a button in Jenkins, not automatically on every commit. Two environments only (dev, prod). Say "CI/CD pipeline" or "one-click deployment", not "fully automated continuous deployment" or "multiple environments".
- Anaconda/Docker: one Anaconda environment for the backend microservices. Don't claim "multiple Anaconda environments".
- CloudFormation: say "provisioned EC2 using CloudFormation templates", never "wrote/authored CloudFormation templates". Don't call it IaC authorship.
- ExpressJS: development phase only, not in the final backend. Don't present Node/Express as the production backend.
- The GenAI applications were designed and built end to end by the candidate (frontend, backend, RAG logic, vector DB, embeddings), initially as the only engineer. A dedicated frontend developer joined in year 2 and interns in year 3, so don't say "alone" or "solely" for the whole three years, and don't claim every later React change personally.
- Leadership: say "de facto team lead" or "led interns/a small team", never a formal title like "Team Lead" or "Manager". Interns: 2 to 4 (4 at the peak, 2 on average), so say "up to 4 interns" or "2–4 interns". Don't quote team sizes beyond the above.
- Recognition: "Best Team Project" for two projects (rating-email automation, department RAG chatbot). Years: 2024 (rating-email automation), 2025 (RAG chatbot). It is an internal recognition; don't call it a company-wide or industry award.

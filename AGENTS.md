# Job Applications

## Application Tracker

- Keep ApplicationTracker.xlsx updated on every job application. 


## Application Tailoring

- Tailor my `KaustubhSonawaneCVUK.docx` or `KaustubhSonawaneCVUK.pdf` as per the job description supplied to you.
- Save the tailored cv is a seperate folder for the company applied in `jobs/{commpnayname}/KaustubhSonawane{JobRole}.docx`
- Use the MasterCV as is in terms of formatting. Change the words and roles as needed.
- **Keep the tailored CV to 2 pages (hard limit).** Never ship a CV that spills onto a 3rd page. Do NOT estimate the length from the word count or from the paragraph count: after generating the `.docx`, open it in Word and read the real page count (`Word.Application` -> `Documents.Open(path, $false, $true)` -> `ComputeStatistics(2)`; `0` returns the word count). If it comes back as 3 pages, cut wording and re-check, and keep re-checking after every trim rather than once at the end. Trim in this order: tighten existing bullet and project wording first, then drop the least relevant project entry, then drop the weakest work-experience bullet. Leave a few lines of slack at the bottom of page 2 so a small rendering difference cannot push it over. The cover letter stays on 1 page.
- The fromat of the cv must be as is in the `KaustubhSonawaneCVUK.docx` i.e. the structuing, layout and the endlines "---\n" that lead to a line covering the width.
- The exception to teh struction change is only in the Work Experience section. (It is siloed as per the multiple different responsibilities that I had. Incase they are not relevant to an application restructure them or remove them as you see fit in improving my chances to land the job.)
- If the Role is being read from `jobs-india/*` then the application is being targeted for an Indian position and thus would need an Indian CV format and a **TRUE** flag for India column in the excel sheet.


## Job Roles

- The applications will be targeted to the following core roles and roles that are similar to them. They might vbe named differently by each company:
    1. AI Solutions Engineer / Gnerative AI Engineer / Agentic AI Engineer
    2. Forward Deployed Engineer
    3. Machine Learning Engineer
    4. Data Scientist
    5. Software Development Engineer / Full Stack Developer
    6. Data Engineer
    7. DevOps Engineer / MLOps Engineer / Infra Engineer
- Based on the Job Role the proper tailoring must be done to the resume for whome the relevant work experience must be fetched from `cv/EXPERIENCE.md`


## Gaps

- If a JD contains any requirements that are not covered in my `EXPERIENCE.md` then add those requirements to `GAPS.md`.
- The file contains tiers and each GAP is appropriately classifed into each tiers based on how much ROI I can get by filling it.
- S tier gaps are the ones that need immediate attention.



## Functioning

- I shall be supplying Claude Code with the Job Description for each job I am to apply, once done You are supposed to:
    1. Draft the tailored Resume and Cover Letter.
    2. Save the created files the proper folder (Create the folder as well if not existing).
    3. Update the excel `ApplicationTracker.xlsx` sheet accordingly. (Put Apply date for the same date the cv is created.)
    4. Fill the `GAPS.md` file approprieately.
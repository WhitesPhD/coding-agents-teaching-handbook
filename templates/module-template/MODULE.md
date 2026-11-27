# ECN000 Module Title

Standing instructions for the agent. Keep this file to one or two pages.
Replace every [bracket], delete the examples that do not apply, and put
detail for a single task (a rubric, a marking scheme) in its own file.

## Module facts
- Level [6], [15] credits, about [120] students, taught in [term 1].
- Prerequisites: [ECN000 Econometrics I]. Co-requisites: [none].
- Teaching: [10] lectures of [100] minutes, [10] tutorials, [5] computer labs.
- Module leader: [name]. Teaching assistants: [names, or see admin/staff.md].

## Learning outcomes
As approved in the module specification. Do not reword them.
1. [Estimate a linear factor model and test its restrictions.]
2. [...]
Every lecture plan, problem set and assessment says which outcomes it serves.

## What students know
- Assume: [linear algebra to eigenvalues; OLS and its asymptotic theory;
  Python with pandas, numpy and matplotlib].
- Do not assume: [maximum likelihood; matrix calculus; R or Stata].
- Where students usually struggle: [moving from moment conditions to the GMM
  objective; reading a table with clustered standard errors].

## Notation
- Returns r_t, excess returns r^e_t; logs lower case, levels upper case.
- Vectors bold lower case, matrices bold upper case; estimators carry a hat.
- E_t[.] is the expectation conditional on information at time t.
- Where this list is silent, follow [textbook], chapters [x-y].

## Software
- Python [3.12]. Packages pinned in requirements.txt; use no others.
- Every notebook runs from top to bottom in a fresh kernel before release.
- Lecture notes use lectures/template.tex and compile with latexmk.

## Folders and file names
- lectures/weekNN/: plan.md, notes.tex, slides.tex, figures/ with the script
  that produces each figure.
- problem-sets/psN/: questions.tex, solutions.tex, solve.py, data/.
- sources/: read-only. sources/third-party/ holds licensed material.
- assessment/: outside version control. Never shared, synced or uploaded.

## House style
- British spelling.
- One lecture is [100] minutes: at most [25] slides and [two] worked examples.
- Full rules: the lecture-style skill in .claude/skills/lecture-style/.

## Rules
- Never edit anything in sources/.
- Never supply a reference, fact or number that is not in sources/ or in code
  output. If something is missing, stop and list it.
- Every number in a solution, table or figure comes from a script that has
  been run.
- Compile or run every file before reporting it finished.
- No student work, marks or personal data in this folder.
- Commit before and after each task, with a message saying what changed and
  why. Never commit anything in assessment/.
- Ask before deleting a file or changing more than one week's material in a
  single task.

## Related files
- Coursework rubric: [assessment/coursework-rubric.md]. Read it only when
  working on marking or on the assessment.
- Module outline and schedule: admin/outline.md.

## Decisions log
One dated line per decision, newest last, so that settled questions are not reopened.
- 2026-11-26  Dropped the Kalman filter lecture; replaced by a second GMM lab.
- [date]  [decision, and the reason for it]

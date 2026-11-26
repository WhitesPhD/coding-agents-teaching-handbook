---
name: assessment-loop
description: Iteratively tests and revises an assessment using a candidate and an examiner subagent.
disable-model-invocation: true
---

You are the setter for the assessment in $ARGUMENTS.

Settings (edit before running):
  stop when the candidate's total is below 50, or after 3 rounds,
  or when no revision satisfies the constraints.

Constraints on every revision:
  - every learning outcome in MODULE.md that the original assessed is still assessed
  - format, weighting, word limit and time allowance unchanged
  - a well-prepared student can complete it using only what the module taught
  - no trick wording and no reliance on information students cannot obtain

Each round:
  1. Copy the student-facing files to rounds/roundN/student/.
  2. Use the candidate subagent on that folder only.
  3. Use the examiner subagent on the submission and the rubric.
  4. Save the examiner's report to rounds/roundN/report.md.
  5. Check the stopping rule. If met, go to the final report.
  6. Identify the criteria passed most easily. Propose one or two revisions
     that satisfy every constraint. Record each in changes.md with the
     criterion it targets and the reason. Apply them to a new version.

Final report (report.md): original and final versions, the change log,
marks by criterion for every round, the final attempt in full, and which
constraints came under strain. State plainly if the format could not be
made robust.

Never edit the original assessment files. Work on copies.

---
name: assessment-loop
description: Tests an assessment by having a candidate subagent sit it and an examiner subagent mark it, and revises it until a stopping rule is met.
disable-model-invocation: true
argument-hint: "[assessment folder, e.g. assessment/coursework1]"
---

You are the setter for the assessment in $ARGUMENTS, and you run the loop.
In each round you call the candidate and examiner subagents yourself. The
lecturer starts you and approves the plan, and does not call the subagents.

Settings (edit before running):
  stop when the candidate's total is below 50, or after 3 rounds,
  or when no revision satisfies the constraints.

The assessment folder must contain:
  student/   exactly what a student receives: brief, data, reading list
  marking/   rubric.md, and any marking notes or model answers

Constraints on every revision:
  - every learning outcome in CLAUDE.md that the original assessed is still assessed
  - format, weighting, word limit and time allowance unchanged
  - a well-prepared student can complete it using only what the module taught
  - no trick wording and no reliance on information students cannot obtain

Before round 1:
  1. Check that student/ and marking/ exist and list their files. If either
     is missing or empty, stop and say what is needed.
  2. Check that .claude/agents/ contains candidate.md and examiner.md.
  3. Copy student/ and marking/ unchanged to versions/v0/.
  4. Show me the files, the settings and the constraints, and wait for my
     approval.

Round N, starting at 1, uses the latest version vK:
  1. Copy versions/vK/student/ to rounds/roundN/student/.
  2. Use the candidate subagent. Give it the full path of
     rounds/roundN/student/ and nothing else about the assessment. It saves
     its submission in that folder.
  3. Use the examiner subagent. Give it the full paths of the submission and
     of versions/vK/marking/rubric.md. Save its report to
     rounds/roundN/report.md.
  4. Add the marks by criterion for this round to rounds/summary.md.
  5. Check the stopping rule. If it is met, go to the final report.
  6. Identify the criteria the candidate passed most easily. Propose one or
     two revisions that satisfy every constraint, and record each in
     changes.md with the criterion it targets and the reason.
  7. Write the revised student/ and marking/ folders to the next version,
     versions/v(K+1)/, and start the next round.

Final report (report.md): the original and final versions side by side, the
change log, marks by criterion for every round, the final attempt in full,
and which constraints came under strain. State plainly if the format could
not be made robust.

Never edit student/ or marking/ in the assessment folder; work on copies.
Never give the candidate the marking files, the change log or earlier rounds.

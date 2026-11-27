---
name: notebook-release
description: Check that a solution notebook runs from top to bottom and produce the student version without the solution cells. Use before releasing any notebook to students.
disable-model-invocation: true
argument-hint: "[path to the solution notebook]"
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/release.py *)
---

Release the notebook $ARGUMENTS.

1. Check that the installed package versions match the pinned versions in
   the module (requirements.txt or its equivalent in CLAUDE.md). Report any
   difference and stop.
2. Run ${CLAUDE_SKILL_DIR}/scripts/release.py on the notebook. The script
   runs the notebook in a fresh kernel and stops at the first error. If it
   ran, it writes NAME-student.ipynb next to it, without the cells tagged
   "solution" and with all outputs cleared.
3. If the run fails, report the cell and the error. Do not edit the
   notebook to make it pass without telling me exactly what you changed.
4. Read the student version. Check that every question still makes sense
   without the removed cells, and that no answer survives in a markdown cell
   or a comment.
5. Report: whether the notebook ran and how long it took, which cells were
   removed, and anything in the student version that needs my attention.

Never release a student version from a notebook that did not run.

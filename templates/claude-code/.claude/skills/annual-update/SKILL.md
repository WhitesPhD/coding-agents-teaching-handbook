---
name: annual-update
description: Prepare the module for a new academic year. Finds dated material, reruns figure and solution scripts on current data, and reports every change against last year. Use once a year before teaching starts.
disable-model-invocation: true
argument-hint: "[academic year, e.g. 2027-28]"
---

Prepare the module for the academic year $ARGUMENTS.

1. Read CLAUDE.md, including the decisions log.
2. List everything that has dated, with file and location: data ending in
   an old year, superseded references, examples overtaken by events, dates
   and deadlines in admin/. Change nothing yet.
3. Wait for me to mark which items to update.
4. If the folder is under version control, commit its current state first.
5. Rerun every figure and solution script on current data. Record the
   download date of each dataset next to it.
6. Where a rerun changes a number in the notes, slides or solutions, take
   the new number from the output and list the change.
7. Make the other approved updates.
8. Compile or run every changed file and fix any errors.
9. Report: each change against last year's version, file by file; every
   number that changed, old and new; anything you could not update.

Never edit sources/. Do not change learning outcomes or assessment
weightings: list any that look out of date for me to raise at module review.

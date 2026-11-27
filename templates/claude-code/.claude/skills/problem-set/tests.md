# Test cases for the problem-set skill

Not read in normal use: SKILL.md does not point to this file. Run each case
in a fresh session after any edit to the skill and after each update to the
tool or model, and record the result below.

## Case 1: empirical questions with data
Input: /problem-set week05, with lecture notes for week 5 and a dataset in data/.
A correct output:
- every number in solutions.tex appears in the output of solve.py
- the checker ran, and its disagreements are listed (or it found none)
- the report lists the stretch questions
- no question reproduces or paraphrases an exercise from sources/

## Case 2: derivations only
Input: /problem-set week07, a week whose material is derivations with no data.
A correct output:
- each final expression is verified symbolically or numerically, and the
  report says how
- solve.py contains the verification, not an empty placeholder
- the checker and report items from case 1

## Case 3: missing input
Input: /problem-set week11, with no lecture notes for week 11.
A correct output:
- the skill stops and lists what is missing; no files are written

## Requests that should start the skill
- "Write next week's problem set"
- "I need exercises with solutions for week 6"

## Requests that should not
- "Mark these problem-set answers"
- "Fix the typo in question 3 of ps5"

## Results

| Date | Tool and model | Case 1 | Case 2 | Case 3 | Trigger | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

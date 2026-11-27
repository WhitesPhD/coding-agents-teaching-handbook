# Coding Agents for Teaching Economics

A handbook for lecturers on using a coding agent to prepare and run a module: lecture material, problem sets, assessment design, marking, checking, and the rules that apply at UK universities.

The main text is tool-agnostic. Notes headed *In Claude Code* give the specifics for that tool.

## Contents

- `chapters/` the handbook, one file per chapter
- `templates/` the files described on the Templates page, ready to copy
  - `module-template/` an empty module folder with a skeleton instruction file
  - `skill-skeleton/` the parts of a skill, to fill in
  - `claude-code/.claude/` skills (with a bundled script and test cases) and subagent definitions for Claude Code
  - `prompts/`, `student-ai-statement.md`, `assessment-stress-test.md`
- `docs/` the rendered HTML book

## Status

Tool details and university policies were checked on 26 November 2026. The templates have not been tested on a live module.

## Building

Install [Quarto](https://quarto.org), then:

```
quarto render            # HTML book in docs/
quarto render --to pdf   # PDF (needs a LaTeX installation)
```

To publish the HTML with GitHub Pages, set Pages to serve the `docs/` folder of the main branch.

## Author

Daniele Bianchi

## Licence

Text and templates: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). See `LICENSE`.

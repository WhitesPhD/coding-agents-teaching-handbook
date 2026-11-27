# Coding Agents for Teaching Economics

A handbook for lecturers on using a coding agent to prepare and run a module: lecture material, problem sets, assessment design, marking, checking and the rules that apply at UK universities, together with version control, reusable skills and automation.

The main text is tool-agnostic. Notes headed *In Claude Code* give the specifics for that tool.

## Contents

- `chapters/` the handbook, one file per chapter
- `templates/` the files described on the Templates page, ready to copy
  - `module-template/` an empty module folder with a skeleton instruction file and a `.gitignore`
  - `skill-skeleton/` the parts of a skill, to fill in
  - `claude-code/.claude/` skills (with a bundled script and test cases), subagent definitions and a hook for Claude Code
  - `github-actions/` a workflow that compiles documents and runs notebooks on every change
  - `prompts/`, `student-ai-statement.md`, `assessment-stress-test.md`
- `.github/workflows/publish.yml` renders the book and publishes it to GitHub Pages on every push to main

## Status

Tool details and university policies were checked on 26 November 2026. The templates have not been tested on a live module.

## Building

Install [Quarto](https://quarto.org), then:

```
quarto render            # HTML book in docs/, for a local preview
quarto render --to pdf   # PDF (needs a LaTeX installation)
```

`docs/` is not committed. The published site is built by the workflow in `.github/workflows/publish.yml` on every push to main, with Pages set to deploy from GitHub Actions (Settings → Pages → Source). The workflow can also be started by hand from the Actions tab.

## Author

Daniele Bianchi

## Licence

Text and templates: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). See `LICENSE`.

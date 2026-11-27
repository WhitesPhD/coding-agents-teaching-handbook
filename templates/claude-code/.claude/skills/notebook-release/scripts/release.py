#!/usr/bin/env python3
"""Run a solution notebook in a fresh kernel, then write the student version.

Usage: release.py NOTEBOOK.ipynb [--tag solution] [--timeout 600]

The notebook is executed from top to bottom with Jupyter's nbconvert, in the
notebook's own folder, and the script stops at the first error. Only if it
ran is NOTEBOOK-student.ipynb written next to it: cells carrying the tag
(default "solution") are removed, and the outputs of every remaining cell are
cleared so that no answer survives in a saved output. The solution notebook
itself is not changed.

Needs Jupyter (nbconvert and a kernel) installed in the module's environment.
"""
import argparse
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--tag", default="solution", help="tag marking solution cells")
    parser.add_argument("--timeout", type=int, default=600, help="seconds allowed per cell")
    args = parser.parse_args()

    nb_path = args.notebook.resolve()
    if not nb_path.is_file() or nb_path.suffix != ".ipynb":
        print(f"Not a notebook: {nb_path}")
        return 2
    if importlib.util.find_spec("nbconvert") is None:
        print("Jupyter's nbconvert is not installed in this Python environment "
              f"({sys.executable}). Activate the module's environment and rerun.")
        return 2

    # 1. Run from top to bottom in a fresh kernel. The executed copy goes to a
    #    temporary folder, so the solution notebook is left as it was.
    with tempfile.TemporaryDirectory() as tmp:
        start = time.time()
        result = subprocess.run(
            [sys.executable, "-m", "nbconvert", "--to", "notebook", "--execute",
             f"--ExecutePreprocessor.timeout={args.timeout}",
             "--output-dir", tmp, "--output", "executed", str(nb_path)],
            capture_output=True, text=True, cwd=nb_path.parent,
        )
        seconds = time.time() - start
    out_path = nb_path.with_name(nb_path.stem + "-student.ipynb")
    if result.returncode != 0:
        print(f"FAILED after {seconds:.0f} s: the notebook did not run from top to bottom.")
        print(result.stderr[-4000:])
        if out_path.exists():
            print(f"WARNING: {out_path.name} is from an earlier release and is now out of date.")
        return 1
    print(f"Ran from top to bottom in {seconds:.0f} s.")

    # 2. Build the student version from the solution notebook's source.
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    kept, removed = [], []
    for number, cell in enumerate(nb["cells"], start=1):
        if args.tag in cell.get("metadata", {}).get("tags", []):
            removed.append(number)
            continue
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        kept.append(cell)
    nb["cells"] = kept

    out_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Removed cells {', '.join(map(str, removed)) or 'none'} (tag '{args.tag}').")
    print(f"Wrote {out_path.name}.")
    if not removed:
        print(f"WARNING: no cell carries the tag '{args.tag}', "
              "so the student version contains every cell.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

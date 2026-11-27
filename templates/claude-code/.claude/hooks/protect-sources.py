#!/usr/bin/env python3
"""Claude Code PreToolUse hook: block edits to files in the module's sources/.

Claude Code passes the tool call as JSON on standard input. If the file the
tool would write is inside sources/, the hook prints the reason and exits with
code 2, which blocks the call. Otherwise it exits 0 and the call goes ahead.
"""
import json
import os
import sys
from pathlib import Path

call = json.load(sys.stdin)
tool_input = call.get("tool_input") or {}
target = tool_input.get("file_path") or tool_input.get("notebook_path")
if not target:
    sys.exit(0)

cwd = Path(call.get("cwd") or os.getcwd())
project = Path(os.environ.get("CLAUDE_PROJECT_DIR") or cwd).resolve()
path = Path(target)
if not path.is_absolute():
    path = cwd / path
path = path.resolve()

sources = project / "sources"
if path == sources or sources in path.parents:
    print(f"Blocked: {path.relative_to(project)} is in sources/, which is "
          "read-only in this module. Write the change elsewhere or ask the "
          "lecturer.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)

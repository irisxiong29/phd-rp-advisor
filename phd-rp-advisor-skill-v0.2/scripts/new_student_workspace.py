#!/usr/bin/env python3
from pathlib import Path
import argparse

FOLDERS = [
    "00_input",
    "01_icebreaker",
    "02_topic_brainstorm",
    "03_outline",
    "04_annotated_outline",
    "05_full_draft_review",
    "06_final_proofread",
]

parser = argparse.ArgumentParser(description="Create a clean PhD RP student workspace.")
parser.add_argument("name", help="Folder name, e.g. student-lora")
parser.add_argument("--parent", default=".", help="Parent directory (default: current directory)")
args = parser.parse_args()

root = Path(args.parent).expanduser().resolve() / args.name
root.mkdir(parents=True, exist_ok=True)

for folder in FOLDERS:
    (root / folder).mkdir(exist_ok=True)

(root / "README.md").write_text(
    "# Student RP Workspace\n\n"
    "Keep all materials for this student inside this folder.\n"
    "Invoke $phd-rp-advisor in Codex and state the current task/stage.\n",
    encoding="utf-8",
)
print(root)

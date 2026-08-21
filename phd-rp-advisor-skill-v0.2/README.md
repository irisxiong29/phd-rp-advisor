# PhD RP Advisor Skill v0.2

A personal Codex Skill for a staged humanities/social-science PhD research-proposal advising workflow.

## What changed from v0.1

v0.2 is packaged as a **plain GitHub-installable Codex Skill** rather than a plugin.

Removed:
- `.codex-plugin/`
- marketplace configuration
- `install.sh`
- `uninstall.sh`

The repository root now contains `SKILL.md`, so the whole repository can be installed as one Skill.

## Repository structure

```text
phd-rp-advisor/
├── SKILL.md
├── README.md
├── references/
│   ├── workflow-stages.md
│   ├── literature-and-doi.md
│   ├── style-and-authorship.md
│   ├── review-rubric.md
│   ├── transcript-handling.md
│   └── output-templates.md
├── scripts/
│   └── new_student_workspace.py
└── assets/
    └── student-workspace-template/
        └── README.md
```

## Upload to GitHub

1. Create a new GitHub repository, for example `phd-rp-advisor`.
2. Private is recommended if this contains your proprietary advising workflow.
3. Upload **the contents of this folder** to the repository root.
4. Confirm that `SKILL.md` appears at the top level of the GitHub repository.

Correct:

```text
phd-rp-advisor/SKILL.md
```

Avoid accidentally nesting it like this:

```text
phd-rp-advisor/phd-rp-advisor-skill-v0.2/SKILL.md
```

## Install in Codex

After the repository is available to Codex, ask Codex to install it with the built-in skill installer, for example:

```text
$skill-installer install the skill from:
https://github.com/YOUR-USERNAME/phd-rp-advisor
```

If Codex requests a repository path, use the repository root because `SKILL.md` is already at the root.

After installation, fully quit and reopen the Codex App before testing the Skill in a new conversation.

## Test

In any student RP project, try:

```text
$phd-rp-advisor

Tell me the six workflow stages in this skill. Do not read or analyse student files yet.
```

Then, for actual work:

```text
$phd-rp-advisor

This student is currently at Stage 1. Read the available CV, supervisor-selection file and writing sample, then prepare the icebreaker materials according to the skill workflow.
```

## Workflow

1. Icebreaker preparation
2. Topic brainstorming
3. Approximately 800-word RP outline
4. Chinese annotated outline
5. Full draft review
6. Final proofreading

The AI-style/authorship rules apply across drafting and editing stages rather than being treated as a separate stage.

## Optional student workspace helper

To create the standard folder structure for a new student:

```bash
python3 scripts/new_student_workspace.py student-name --parent ~/Documents/RP-Students
```

This helper is optional. The Skill itself does not require students to use this folder structure.

## Updating

Treat GitHub as the master copy. When you revise the Skill, update the GitHub repository first, then reinstall/update the local Skill in Codex as appropriate.

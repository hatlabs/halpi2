---
title: Sub-lists under a numbered step need four spaces of indentation
date: 2026-08-04
category: best-practices
module: documentation
problem_type: best_practice
component: documentation
severity: medium
applies_when:
  - Writing a numbered procedure where a step has sub-points
  - Nesting any list inside an ordered list item under docs/
  - Reviewing PRs that add step-by-step instructions
tags:
  - markdown
  - mkdocs
  - python-markdown
  - lists
  - indentation
---

# Sub-lists under a numbered step need four spaces of indentation

## Context

Python-Markdown decides whether an indented line continues the current list item
by comparing its indentation against the width of the item's marker. For a
bulleted item the marker `- ` is two characters wide, so two spaces are enough.
For a numbered item the marker `1. ` is **three** characters wide, so
continuation content must start at column **four**.

Three spaces looks correct in the source and is enough for a bulleted parent, so
the habit carries over silently. Under a numbered parent it is one space short:
the sub-items are not nested, they are absorbed into the ordered list and
rendered as further numbered steps.

The failure is not cosmetic. On the Getting Started page, `Connect Ethernet
cable` — a detail of step 1 — rendered as step 2 of the setup procedure, and the
two real steps became six. A reader following the numbers is following the wrong
procedure.

This was found in 4 places across 2 pages (`docs/en/getting-started/getting-started.md`,
`docs/en/user-guide/hardware.md`) and had been live on the published site.

## Guidance

Indent a sub-list under a numbered step by **four** spaces. Under a bulleted
item, two is enough — but four is also correct there, so four everywhere is the
simpler rule to remember.

Wrong (renders as one flat numbered list):

```markdown
1. **Network connection (required for headless installation):**
   - Connect Ethernet cable
   - Connect the WiFi/Bluetooth antenna
```

Right:

```markdown
1. **Network connection (required for headless installation):**
    - Connect Ethernet cable
    - Connect the WiFi/Bluetooth antenna
```

## Why This Matters

Neither `mkdocs build --strict` nor GitHub's markdown preview catches this. The
markup is syntactically valid and GitHub's renderer is permissive enough to show
the nesting the author intended, so a PR looks right in review and is wrong on
the published site. That is the same trap as the blank-line rule, and it hides
in exactly the content where correctness matters most — numbered installation
and wiring procedures.

Translations inherit the bug. A translator working from the source reproduces
the indentation faithfully, so one authoring mistake becomes one per language.

## When to Apply

- Always, when a numbered step has sub-points.
- Especially in `getting-started/` and `user-guide/`, which carry most of the
  step-by-step procedures.
- When reviewing: count the numbers in the rendered page. If a procedure claims
  more steps than it has actions, this is why.

## Detection

A quick scan for the pattern — a numbered line followed by a bullet indented
fewer than four spaces:

```bash
python3 - <<'PY'
import re, glob
for f in glob.glob('docs/**/*.md', recursive=True):
    lines = open(f, encoding='utf-8').read().split('\n')
    for i, ln in enumerate(lines):
        if re.match(r'^\d+\. ', ln):
            for nxt in lines[i+1:]:
                if not nxt.strip(): break
                m = re.match(r'^( +)[-*] ', nxt)
                if m and len(m.group(1)) < 4:
                    print(f, i + 1); break
                if not nxt.startswith(' '): break
PY
```

Verification after fixing is visual: run `uv run mkdocs serve` and confirm the
sub-points render as bullets under their step, not as steps of their own.

## Related

- `markdown-lists-need-blank-line-2026-05-16.md` — same root cause (Python-Markdown
  list parsing without `sane_lists`), different trigger
- PR hatlabs/halpi2#26 — where this was found and fixed

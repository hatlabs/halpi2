---
title: Markdown lists need a blank line before the first item
date: 2026-05-16
category: best-practices
module: documentation
problem_type: best_practice
component: documentation
severity: medium
applies_when:
  - Authoring or editing markdown under docs/ for the MkDocs site
  - A list immediately follows a paragraph, bold-label intro, or setext-style line
  - Reviewing PRs that add new prose-plus-list sections
tags:
  - markdown
  - mkdocs
  - python-markdown
  - lists
  - formatting
---

# Markdown lists need a blank line before the first item

## Context

This repo's `docs/` is rendered by MkDocs Material, which uses Python-Markdown. Python-Markdown does **not** enable the `sane_lists` extension by default. Without `sane_lists`, a list that starts on the line immediately after a non-blank, non-list paragraph is folded into that paragraph and rendered as inline text — the `-` and `1.` markers appear as literal characters in a single flowing sentence, not as bullets or numbers.

GitHub's renderer is more permissive and shows the list correctly on the source PR. The mismatch is easy to miss in review, especially since the markdown source "looks like a list."

The list-spacing fixes PR (#18, 2026-05-16) found 43 instances of this across three high-traffic pages (`docs/index.md`, `docs/user-guide/operation.md`, `docs/getting-started/getting-started.md`). Common preceding-line patterns that triggered the bug:

- Bold-label intros — `**Tools:**`, `**Backup Power Duration:**`, `**Marine Installations:**`
- Troubleshooting symptom lines — `❌ **No power/LEDs:**`
- Plain lead-in sentences — `From your HALPI2 package:`
- Section headings immediately followed by a list with no blank line

## Guidance

Always leave a blank line **before** the first item of any top-level list, and a blank line **after** the last item before the next paragraph. Apply this whether the list is bulleted (`-`, `*`, `+`) or numbered (`1.`).

Wrong (renders as one paragraph on the published site):

```markdown
From your HALPI2 package:
- HALPI2 unit with pre-installed CM5 and NVMe SSD
- Power cable with E7T connector (2m length)
```

Right:

```markdown
From your HALPI2 package:

- HALPI2 unit with pre-installed CM5 and NVMe SSD
- Power cable with E7T connector (2m length)
```

Verification when adding or editing content:

- Run `uv run mkdocs serve` and visually confirm lists render as lists, not inline text — do not rely on the GitHub PR preview for this check.
- `uv run mkdocs build --strict` will not catch this; the build succeeds because the markup is syntactically valid, just semantically wrong.

## Why This Matters

The published site at https://docs.hatlabs.fi/halpi2 is the user-facing entry point. A list rendered as a wall of inline text makes setup steps, troubleshooting checklists, and accessory lists hard to scan and can hide critical safety information (e.g., the wire-polarity callouts on the Getting Started page). The cause is invisible in the markdown source and not flagged by `mkdocs build --strict`, so the bug accumulates silently across PRs.

The fix is mechanical and the rule is simple. Enforcing it at authoring time avoids periodic cleanup passes.

## When to Apply

- Always, when writing or reviewing any `.md` file under `docs/`.
- Especially when introducing a list with a colon-terminated line (`Foo:` or `**Foo:**`), which is the most common trigger.
- Headings immediately preceding a list also need a blank line in between.

## Examples

Bold-label intro (operation.md pattern):

```markdown
<!-- wrong -->
**Backup Power Duration:**
- Super-capacitors provide 30-60 seconds of backup power
- Sufficient time for graceful shutdown

<!-- right -->
**Backup Power Duration:**

- Super-capacitors provide 30-60 seconds of backup power
- Sufficient time for graceful shutdown
```

Heading immediately followed by a list (index.md pattern):

```markdown
<!-- wrong -->
### Enclosure Features
- **Waterproof (IP65) aluminum enclosure**, size 200×130×60 mm

<!-- right -->
### Enclosure Features

- **Waterproof (IP65) aluminum enclosure**, size 200×130×60 mm
```

Ordered list with code-fence continuation inside a list item is **not** affected — the items are already part of an open list, and continuation lines indented by 2+ spaces stay inside it:

```markdown
1. First step
2. Run the command:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Third step
```

## Alternative: enable `sane_lists`

The `pymdownx`/`markdown` extension `sane_lists` makes Python-Markdown match the common (GitHub-style) behavior — lists don't need a leading blank line. We have **not** enabled it. If it were enabled in `mkdocs.yml` under `markdown_extensions`, this rule would be unnecessary. The trade-off: `sane_lists` also changes how lists of different types are handled (e.g., switching from `1.` to `-` starts a new list), which can surprise authors. The current decision is to keep the default behavior and enforce the blank-line rule by convention.

## Related

- PR hatlabs/halpi2#18 — initial mass fix (43 instances across 3 files)
- Python-Markdown lists docs: https://python-markdown.github.io/extensions/sane_lists/

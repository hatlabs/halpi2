# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the HALPI2 User Guide documentation, built with MkDocs Material. HALPI2 is a Raspberry Pi Compute Module 5 carrier board designed for marine electronics and industrial applications.

## Build System

**Prerequisites:** Python 3.14 (pinned in `.python-version`) and `uv` must be installed.

**Common Commands:**
- `uv sync` - Install dependencies
- `uv run mkdocs serve` - Start local dev server (http://127.0.0.1:8000)
- `uv run mkdocs build --strict` - Build the documentation (output goes to `./site`)

**Translation checkers**, from the `halos-docs-tools` package pinned in
`pyproject.toml`.

CI runs two of them, `check-anchors site` and `translation-status --check`,
alongside `mkdocs build --strict`, which is MkDocs rather than a checker. The
other four package commands are local-only; nothing enforces them. The gate
judges the whole repository as merged with `main`, so a branch that is clean
locally can still go red after `main` moves.

- `uv run translation-status` - Which translations are current, stale, missing, unstamped or orphaned. Always exits 0
- `uv run translation-status --check` - The same, exiting 1 when any translation is stale, missing, unstamped or orphaned, and 2 when the check could not cover everything — no configured locales, no source pages, or a page under `docs/` in none of the locales. This is the gate
- `uv run stamp-translation <path>` - Record the English blob a translation was written against
- `uv run check-anchors site` - Internal links whose target anchor does not exist
- `uv run check-glossary <locale>` / `uv run check-typography <locale>` - Per-language conventions
- `uv run map-anchors site <locale>` - Report English fragments that should become translated ids; `--apply` rewrites them

**Language selection, the 404 page and per-language search** come from the
`halos-i18n` MkDocs plugin in `halos-docs-tools`, enabled by name under
`plugins:` in `mkdocs.yml`. It redirects a visitor of the English edition to the
edition matching their browser languages, serves one 404 page that picks the
reader's language at runtime, gives each edition its own search index, and fails
the build when the built pages lose any of that. Its behaviour, the 404 wording
override and the local-storage key are documented in the docs-tools README. This
repository has no `hooks/`, no `theme.custom_dir` and no `extra.not_found`; a
`custom_dir` put back would shadow the plugin's templates.

## Documentation Structure

- `mkdocs.yml` - MkDocs configuration and navigation structure
- `docs/en/` - English content, the source every translation is written from:
  - `getting-started/` - Quick start and installation guides
  - `user-guide/` - System operation, hardware, interfaces, software
  - `technical-reference/` - Detailed hardware specs and technical docs
  - `software-development/` - Daemon, integration, Ubuntu installation
  - `appendices/` - Design files, schematics, errata
- `docs/<locale>/` - Translations, one directory per locale, mirroring `docs/en/`
- `docs/stylesheets/extra.css` - Custom CSS (Hat Labs branding)
- `docs/assets/` - Logo and shared assets

## Documentation Status

Check `mkdocs.yml` nav section for the full page list. Some pages are placeholders awaiting content.

## Deployment

GitHub Actions automatically builds and deploys to GitHub Pages on push to `main` branch. See `.github/workflows/deploy.yml`.

## Content Guidelines

- Use GitHub-flavored Markdown
- Use MkDocs Material admonitions (`!!! tip`, `!!! warning`, etc.) instead of blockquote callouts
- Include images with descriptive alt text
- Cross-reference other pages using relative paths
- Technical specs and measurements should be in the technical-reference section
- Step-by-step instructions belong in getting-started or user-guide sections
- Always leave a blank line before and after lists — without it, Python-Markdown folds items into the preceding paragraph and they render as inline text on the published site (see `solutions/best-practices/markdown-lists-need-blank-line-2026-05-16.md`)

## Engineering Notes

`solutions/` — documented solutions and best practices for authoring and tooling, organized by category with YAML frontmatter (`module`, `tags`, `problem_type`). Lives outside `docs/` so it doesn't ship to the published site. Relevant when authoring docs or making decisions in documented areas.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the HALPI2 User Guide documentation, built with MkDocs Material. HALPI2 is a Raspberry Pi Compute Module 5 carrier board designed for marine electronics and industrial applications.

## Build System

**Prerequisites:** Python 3.11+ and `uv` must be installed.

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

**Automatic language selection.** `docs/overrides/main.html` adds an inline head
script to every page of a multi-language build. On a page of the default edition
it matches `navigator.languages` against the locales in `mkdocs.yml` and calls
`location.replace()` on the matching translation of that same page, carrying the
query string over. GitHub Pages serves static files and cannot negotiate
content, so the choice has to happen in the browser. `no` and `nn` both resolve
to the `nb` edition.

Three rules keep the redirect out of the reader's way. A translated page never
redirects, so a link shared in one language keeps its language. A URL with a
fragment never redirects, because heading ids are translated and the anchor
would not survive the move. A page reached from a same-origin referrer never
redirects, which is what makes the header language selector work: picking
English is an in-site navigation, so nothing sends the reader back. The choice
also goes to `localStorage` under `halpi2.docs.language` and outranks the
browser languages on later visits, but the selector still works when storage is
blocked.

The same override declares `hreflang="x-default"` pointing at the English
version of each page, so a search engine has a page to offer for a language the
site is not translated into. The generated `sitemap.xml` carries the per-locale
`hreflang` annotations but no `x-default`; adding one there would mean vendoring
the plugin's `sitemap.xml` template into `docs/overrides/`.

**The 404 page.** GitHub Pages serves `site/404.html` for every URL that does
not resolve, in every edition, and a build can only produce one copy of it. The
i18n plugin builds the default language first and then each remaining locale
with a nested `build()` call, every one of which overwrites that file, so the
copy that survived belonged to whichever locale came last in `mkdocs.yml`.
`hooks/default_404.py` keeps the default edition's copy and writes it back after
each nested build, which makes the chrome stable.

`docs/overrides/404.html` then chooses a language in the browser. It reads the
first path segment of the URL the reader tried, which names the edition they
were in, and falls back to `navigator.languages` when that segment names no
edition. It sets the page language, the wording, the home link, the logo link
and the language selector for that edition. The wording lives in
`extra.not_found` in `mkdocs.yml`, one `title`, `message` and `home` per locale;
a built locale with no entry fails the build.

**Language-selection checks.** `hooks/language_redirect.py` publishes the
default locale, the built locale list and each edition's root path under
`config.extra`, then walks the built site and aborts the build unless every page
declares a configured `lang`, carries exactly one `x-default` link, offers every
built locale in its `ALTERNATES` map, and still has a language selector. The 404
page is checked against its own rules: built as the default locale, and offering
every locale in its editions map. Everything these templates read comes from
`mkdocs-static-i18n` and would otherwise degrade to omitted output, so without
these checks a plugin upgrade could ship a site that silently stopped selecting
a language.

**Per-language search.** `hooks/i18n_search.py` splits the merged
`search/search_index.json` into one index per language edition and repoints
`__config.base` on that edition's pages at the edition root, which is the only
value Material derives the index URL from. It runs at event priority -200, after
the i18n plugin merges the index at -100. The hook aborts the build when an
edition ends up with no entries, so an upgrade that changes either mechanism
fails loudly instead of shipping an empty search box.

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
- `docs/overrides/main.html` - Theme override: Hat Labs header nav and the language-selection script
- `docs/overrides/404.html` - Theme override: the 404 page, which picks a language at runtime
- `hooks/language_redirect.py` - Supplies the locale facts to the theme overrides and asserts the built pages kept the language selection
- `hooks/default_404.py` - Keeps the default edition's 404 page and checks every locale has 404 wording
- `hooks/i18n_search.py` - Post-build hook giving each language edition its own search index

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

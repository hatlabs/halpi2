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

## Documentation Structure

- `mkdocs.yml` - MkDocs configuration and navigation structure
- `docs/` - All markdown content organized by section:
  - `getting-started/` - Quick start and installation guides
  - `user-guide/` - System operation, hardware, interfaces, software
  - `technical-reference/` - Detailed hardware specs and technical docs
  - `software-development/` - Daemon, integration, Ubuntu installation
  - `appendices/` - Design files, schematics, errata
- `docs/stylesheets/extra.css` - Custom CSS (Hat Labs branding)
- `docs/assets/` - Logo and shared assets
- `docs/overrides/` - MkDocs Material theme overrides

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

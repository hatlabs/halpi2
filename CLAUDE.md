# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the HALPI2 User Guide documentation, built with mdBook. HALPI2 is a Raspberry Pi Compute Module 5 carrier board designed for marine electronics and industrial applications.

## Build System

**Prerequisites:** Rust and Cargo must be installed. Then install mdBook:
```bash
cargo install mdbook
```

**Common Commands:**
- `mdbook build` - Build the documentation (output goes to `./book`)
- `mdbook serve --open` - Start local dev server and open in browser
- `mdbook test` - Test code samples in the documentation
- `mdbook clean` - Remove the build directory

## Documentation Structure

- `src/SUMMARY.md` - Table of contents (mdBook navigation structure)
- `src/` - All markdown content organized by section:
  - `getting-started/` - Quick start and installation guides
  - `user-guide/` - System operation, hardware, interfaces, software
  - `technical-reference/` - Detailed hardware specs and technical docs
  - `software-development/` - Daemon, integration, Ubuntu installation
  - `appendices/` - Design files, schematics, errata
- `theme/` - Custom CSS/JS for page TOC functionality
- `book.toml` - mdBook configuration

## Documentation Status

Check `src/SUMMARY.md` for completion status of each page (✅ = complete, ❌ = incomplete/placeholder).

## Deployment

GitHub Actions automatically builds and deploys to GitHub Pages on push to `main` branch. See `.github/workflows/mdbook.yml`.

## Content Guidelines

- Use GitHub-flavored Markdown
- Include images with descriptive alt text
- Cross-reference other pages using relative paths
- Technical specs and measurements should be in the technical-reference section
- Step-by-step instructions belong in getting-started or user-guide sections

# HALPI2 Documentation

This repository contains the HALPI2 User Guide source.

The documentation is written in Markdown format and is built using
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/). The output is
a static website that can be hosted on any web server (in our case, GitHub Pages).

## Prerequisites

Python 3.11+ and [uv](https://docs.astral.sh/uv/) must be installed.

## Getting Started

Install dependencies:

```bash
uv sync
```

Preview the documentation locally:

```bash
uv run mkdocs serve
```

Build for production:

```bash
uv run mkdocs build --strict
```

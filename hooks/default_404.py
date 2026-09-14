"""Keep the default edition's 404 page instead of the last locale built.

`mkdocs-static-i18n` builds the default language in the outer build, then loops
over the remaining locales with nested `build()` calls. Every one of those
writes `site/404.html`, so the file that survives belongs to whichever locale is
last in `mkdocs.yml` — Danish today, with Danish chrome and a logo linking into
the Danish edition. GitHub Pages serves that one file for every URL that does
not resolve, in every edition.

This hook runs at priority 0, ahead of the i18n plugin's nesting at -100. In the
outer build it keeps a copy of the default edition's 404 page; in each nested
build it writes that copy back, so the last write of the build is the one we
want. `docs/overrides/404.html` then picks the reader's language at runtime,
which is what makes a single stable page enough for ten editions.
"""

from pathlib import Path

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority

WORDING = ("title", "message", "home")

_default_edition_404 = None


@event_priority(-200)
def on_config(config):
    """Fail the build when a built locale has no 404 wording."""
    wording = config["extra"].get("not_found") or {}
    missing = [
        locale
        for locale in config["extra"]["locales"]
        if sorted(wording.get(locale) or {}) != sorted(WORDING)
    ]
    if missing:
        raise PluginError(
            f"default_404: extra.not_found needs {list(WORDING)} for {missing}"
        )
    return config


@event_priority(0)
def on_post_build(config):
    """Stash the default edition's 404 page, then restore it after each locale."""
    global _default_edition_404

    i18n = config["plugins"].get("i18n")
    if i18n is None:
        return

    page = Path(config["site_dir"]) / "404.html"
    if not page.exists():
        raise PluginError(f"default_404: no 404 page at {page}")

    if not i18n.building:
        _default_edition_404 = page.read_bytes()
    elif _default_edition_404 is not None:
        page.write_bytes(_default_edition_404)

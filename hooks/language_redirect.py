"""Feed the language-selection template and check what it produced.

`docs/overrides/main.html` sends a visitor of the default edition to the
edition matching their browser languages. It needs one fact the theme context
does not carry, the default locale, and it is built entirely from values
`mkdocs-static-i18n` injects: `config.extra.alternate` and the locale list.

Every one of those assumptions degrades to omitted output rather than a build
error, so a plugin upgrade could ship a site that silently stops selecting a
language. `on_config` supplies the default locale from one place, and
`on_post_build` fails the build when the rendered pages do not carry what the
template promised.

`on_config` runs at priority -100, after the i18n plugin has validated its own
config. `on_post_build` runs at -200, after the plugin's nested per-language
builds have finished.
"""

import json
import re
from pathlib import Path

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority

ALTERNATES_MAP = re.compile(r"var ALTERNATES = (\{.*?\n    \});", re.S)
X_DEFAULT_LINK = re.compile(r'<link rel="alternate" [^>]*hreflang="x-default">')
HTML_LANG = re.compile(r"<html[^>]*\blang=\"([^\"]*)\"")

# Rendered by MkDocs itself rather than from a page, so the template skips it.
UNPAGED = "404.html"


@event_priority(-100)
def on_config(config):
    """Publish the default locale for the language-selection template."""
    languages = _languages(config)
    default = [lang.locale for lang in languages if lang.default]
    if len(default) != 1:
        raise PluginError(
            f"language_redirect: expected exactly one default locale, got {default}"
        )
    config["extra"]["default_locale"] = default[0]
    return config


@event_priority(-200)
def on_post_build(config):
    """Fail the build if the rendered pages lost the language selection."""
    i18n = config["plugins"].get("i18n")
    if i18n is None or i18n.building:
        return

    expected = sorted(lang.locale.lower() for lang in _languages(config) if lang.build)
    if len(expected) < 2:
        return

    site_dir = Path(config["site_dir"])
    for page in sorted(site_dir.rglob("*.html")):
        if page.name == UNPAGED and page.parent == site_dir:
            continue
        _check_page(page, expected)


def _languages(config):
    i18n = config["plugins"].get("i18n")
    if i18n is None:
        raise PluginError("language_redirect: the i18n plugin is not enabled")
    return i18n.config.languages


def _check_page(page, expected):
    text = page.read_text(encoding="utf-8")

    lang = HTML_LANG.search(text)
    if lang is None or lang.group(1).lower() not in expected:
        found = lang.group(1) if lang else "nothing"
        raise PluginError(f"language_redirect: {page} declares lang={found}")

    if len(X_DEFAULT_LINK.findall(text)) != 1:
        raise PluginError(f"language_redirect: no single x-default link in {page}")

    match = ALTERNATES_MAP.search(text)
    if match is None:
        raise PluginError(f"language_redirect: no language script in {page}")
    locales = sorted(json.loads(match.group(1)))
    if locales != expected:
        raise PluginError(
            f"language_redirect: {page} offers {locales}, expected {expected}"
        )

    if '<a href="' not in text or "md-select__link" not in text:
        raise PluginError(f"language_redirect: no language selector in {page}")

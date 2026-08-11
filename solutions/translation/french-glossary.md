---
title: French translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into French under docs/fr/
  - Reviewing a French translation for consistency
  - Adding a new term that has no established French equivalent
tags:
  - translation
  - i18n
  - french
  - terminology
  - mkdocs-static-i18n
---

# French translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into French under `docs/fr/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/fr/`; images and
other assets stay with the English source and are shared.

This file is the reference that keeps terminology from drifting between pages.
Extend it when a page introduces a term that is not listed here, rather than
inventing a one-off translation.

The Finnish glossary (`finnish-glossary.md`) is the sibling of this file and the
place to look for the general approach. The rules below cover what is specific
to French.

## Names that are never translated

Product names, protocol names, hardware standards, and software UI strings stay
in English — the device's own interface is in English, so translating a menu
name would send the reader looking for something that does not exist on screen.

The list is identical to the Finnish glossary's: HALPI2, HaLOS, Signal K,
OpenPlotter, Raspberry Pi OS, Cockpit, Homarr, Authelia, Grafana, Hat Labs,
Compute Module 5 (CM5), NMEA 2000, NMEA 0183, CAN FD, RS-485, NVMe SSD, GPIO,
HDMI, MIPI, USB, RP-SMA, E7T, PG7, SP13, IP65, DHCP, SSH, SSL, ABYC, Cat5e, AWG,
plus every UI path, command, hostname and file path.

Code fences, command output, URLs and image filenames are never touched.

## Style rules

### Address form

Instructions use **the second person plural imperative** (*vouvoiement*):

> Branchez le câble d'alimentation. Vérifiez la polarité au multimètre avant de
> mettre sous tension.

Not the infinitive (*Brancher le câble*), which reads as a parts list rather
than guidance, and not *tu*.

Descriptive passages use a plain statement or the passive:

> L'appareil s'éteint automatiquement lorsque l'alimentation est coupée.

### Typography

French typography is stricter than English and this is the most common source of
sloppy-looking translated pages. The space before `; : ! ?` is not decoration:
an ordinary space lets the line break in front of the punctuation, which is the
first thing a French reader notices.

U+00A0 rather than U+202F (narrow no-break): U+202F is the typographically
precise character but renders inconsistently across fonts, while U+00A0 is
universally supported and is what French technical documentation uses in
practice.

- **No-break space (U+00A0) before** `;` `:` `!` `?` and inside `« »`
- **Guillemets** `« … »` for quotations, not `"…"`
- **Decimal comma**, as in Finnish: `0,9 A`, `5,5 × 2,1 mm`
- **Space before the unit**: `12 V`, `250 kbit/s`, `−20 °C`
- **En dash for ranges**: `3–5 A`

### Units and numbers

Identical handling to Finnish — the English source writes `12V` and `0.9A`, and
both are wrong in French. Convert every one.

| English source | French |
|:---------------|:-------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |

### Links, images, admonitions, navigation

Same rules as the Finnish glossary: paths are copied from the English source
unchanged and never carry an `en/` or `fr/` segment; image captions and alt
texts are translated but filenames are not; screenshots stay English because the
reader's own screen is English; standard admonition titles are translated
centrally in `mkdocs.yml`, custom ones in the page.

## Glossary

### Enclosure, mounting, and installation

| English | French | Note |
|:--------|:-------|:-----|
| carrier board | carte porteuse | Deliberately *not* the Finnish approach — see the note below |
| enclosure | boîtier | |
| heat sink | dissipateur thermique | |
| waterproof | étanche | |
| wall-mount | fixation murale | |
| mounting surface | surface de fixation | |
| pilot hole | avant-trou | |
| mounting template | gabarit de perçage | |
| bilge | cale | |
| bulkhead | cloison | |
| cable gland | presse-étoupe | |
| cable routing | cheminement des câbles | |
| service loop | boucle de service | |
| cable tie | collier de serrage | |
| blind plug | bouchon obturateur | |
| breather plug | bouchon d'équilibrage de pression | |

**A note on `carte porteuse`, and why it differs from Finnish.** Finnish
translates `carrier board` as `emolevy` — literally *motherboard* — chosen for
reader familiarity over accuracy. French deliberately does **not** follow that:
`carte porteuse` says what the board actually is.

Do not "harmonise" the two. They differ on purpose, decided per language and per
audience, and the divergence is the decision rather than an oversight in either
one.

The practical consequence is that French needs *less* care than Finnish here.
`emolevy` inverts the CM5/board relationship and the Finnish glossary tells
translators to write the roles out explicitly in passages where that matters.
`carte porteuse` carries the relationship on its own, so the surrounding sentence
does not have to.

### Electrical

| English | French | Note |
|:--------|:-------|:-----|
| power supply | alimentation | |
| input voltage range | plage de tension d'entrée | |
| polarity | polarité | |
| fuse | fusible | |
| inline fuse | fusible en ligne | |
| circuit breaker | disjoncteur | |
| current limiting | limitation de courant | |
| overcurrent | surintensité | |
| voltage drop | chute de tension | |
| grounding | mise à la terre | |
| short circuit | court-circuit | |
| wire gauge | section du conducteur | French uses mm², not AWG |
| marine-grade wire | conducteur de qualité marine | |
| wire strippers | pince à dénuder | |
| crimping | sertissage | |
| crimper | pince à sertir | |
| heat-shrink tubing | gaine thermorétractable | |
| heat gun | pistolet à air chaud | |
| multimeter | multimètre | |
| terminal block | bornier | |
| strain relief | serre-câble | |
| super-capacitor | supercondensateur | |
| real-time clock | horloge temps réel | |
| backup battery | pile de sauvegarde | |

### Connectors and interfaces

| English | French | Note |
|:--------|:-------|:-----|
| connector | connecteur | |
| barrel connector | connecteur cylindrique | Add *(barrel)* on first mention |
| header | connecteur | `connecteur GPIO 40 broches` |
| pin | broche | |
| backbone | dorsale | NMEA 2000 backbone |
| drop cable | câble de dérivation | |
| T-connector | connecteur en T | |
| termination (120 Ω) | résistance de terminaison | |
| pull-up (resistor) | résistance de tirage | The 2,2 kΩ pull-ups on the MIPI1 I2C lines |
| front panel | panneau avant | |
| jumper | cavalier | |
| male / female | mâle / femelle | |

### System behaviour and status

| English | French | Note |
|:--------|:-------|:-----|
| boat computer | ordinateur de bord | |
| to boot | démarrer | |
| first boot | premier démarrage | |
| shutdown | arrêt | |
| graceful shutdown | arrêt propre | |
| power loss | perte d'alimentation | |
| blackout | coupure de courant | |
| power management | gestion de l'alimentation | |
| status LED | LED d'état | |
| monitoring | surveillance | |
| passive cooling | refroidissement passif | |
| filesystem | système de fichiers | |
| to unmount | démonter | |
| watchdog | chien de garde (watchdog) | Keep the English in parentheses once |
| standby | veille | |

### Software and networking

| English | French | Note |
|:--------|:-------|:-----|
| firmware | firmware | Not *micrologiciel* — matches the Finnish decision to keep the term the trade uses |
| daemon | démon | Established in French Linux usage, unlike Finnish |
| to flash | flasher | |
| operating system image | image système | |
| headless | sans écran | First mention: `sans écran (headless)` |
| container app | application conteneurisée | |
| container image | image de conteneur | |
| dashboard | tableau de bord | |
| WiFi Access Point | point d'accès WiFi | |
| wired / wireless | filaire / sans fil | |
| credentials | identifiants | |
| default password | mot de passe par défaut | |
| single sign-on (SSO) | authentification unique (SSO) | |
| Certificate Authority (CA) | autorité de certification (CA) | |
| web interface | interface web | |
| browser | navigateur | |

### Applications and use cases

| English | French | Note |
|:--------|:-------|:-----|
| chart plotter | traceur de cartes | |
| data logging | enregistrement de données | |
| vessel | navire | |
| fleet management | gestion de flotte | |
| predictive maintenance | maintenance prédictive | |
| remote monitoring | surveillance à distance | |
| compliance | conformité | |
| warranty | garantie | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
5. Every term used on the page that appears in this glossary matches it.

## Related

- `finnish-glossary.md` — the sibling glossary and the general approach
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

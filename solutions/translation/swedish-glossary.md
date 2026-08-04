---
title: Swedish translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Swedish under docs/sv/
  - Reviewing a Swedish translation for consistency
  - Adding a new term that has no established Swedish equivalent
tags:
  - translation
  - i18n
  - swedish
  - terminology
  - mkdocs-static-i18n
---

# Swedish translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Swedish under `docs/sv/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/sv/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md` and `german-glossary.md` are the
siblings of this file. The general approach is the same in all four.

## Four rules where the siblings are wrong for Swedish

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary, and carrying the wrong habit
across has already cost two correction rounds on earlier branches.

1. **Address the reader as `du`, not formally.** Swedish technical and consumer
   documentation uses `du`. French uses *vouvoiement* and German uses *Sie* —
   both wrong here. `Anslut strömkabeln.` / `Kontrollera polariteten med
   multimetern innan du slår på spänningen.`

2. **Quotation marks are `”…”`** — the *same* character (U+201D) on both sides.
   Not German's `„…“`, not French's `« … »`, not straight `"…"`.

3. **No space before `; : ! ?`** — as in German, and unlike French, whose rule is
   the exact opposite and demands a no-break space.

4. **Compounding with a proper name takes one hyphen at the junction, not
   throughout.** Swedish writes `NMEA 2000-nätverk`, `Signal K-server`,
   `Raspberry Pi-antenn`. German writes `NMEA-2000-Netzwerk` — hyphens all the
   way through. Copying the German pattern into Swedish is wrong, and it is the
   single most likely way this glossary gets violated.

## Names that are never translated

Identical to the sibling glossaries: product names, protocol names, hardware
standards and software UI strings stay in English — HALPI2, HaLOS, Signal K,
OpenPlotter, Raspberry Pi OS, Cockpit, Homarr, Authelia, Grafana, Hat Labs,
Compute Module 5 (CM5), NMEA 2000, NMEA 0183, CAN FD, RS-485, NVMe SSD, GPIO,
HDMI, MIPI, USB, RP-SMA, E7T, PG7, SP13, IP65, DHCP, SSH, SSL, ABYC, Cat5e, AWG,
plus every UI path, command, hostname and file path.

Code fences, command output, URLs and image filenames are never touched.

## Units and numbers

Same handling as the other languages — the English source writes `12V` and
`0.9A`, and both are wrong in Swedish.

| English source | Swedish |
|:---------------|:--------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |

## Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry a language segment; image captions and alt texts are
translated but filenames are not; screenshots stay English because the reader's
own screen is English; standard admonition titles are translated centrally in
`mkdocs.yml`, custom ones in the page.

## Glossary

### Enclosure, mounting, and installation

| English | Swedish | Note |
|:--------|:--------|:-----|
| carrier board | bärkort | The accurate term, as in French and German |
| enclosure | kapsling | |
| heat sink | kylfläns | |
| waterproof | vattentät | |
| wall-mount | väggmontage | |
| mounting surface | monteringsyta | |
| pilot hole | förborrat hål | |
| mounting template | borrmall | |
| bilge water | slagvatten | |
| bulkhead | skott | |
| cable gland | kabelgenomföring | |
| cable routing | kabeldragning | |
| service loop | servicelänga | Slack left at both cable ends |
| cable tie | buntband | |
| blind plug | blindplugg | |
| breather plug | tryckutjämningsplugg | |

**A note on `bärkort`.** Swedish takes the accurate term, like French
(`carte porteuse`) and German (`Trägerplatine`), and unlike Finnish (`emolevy`,
literally *motherboard*, chosen there for reader familiarity). The divergence
between the four is deliberate, decided per language and per audience. Do not
harmonise them.

`bärkort` carries the CM5/board relationship on its own, so passages about
reseating the CM5 or troubleshooting a board that will not boot need no extra
explanation. Only the Finnish glossary needs that warning.

### Electrical

| English | Swedish | Note |
|:--------|:--------|:-----|
| power supply | strömförsörjning | The unit itself: *nätaggregat* |
| input voltage range | inspänningsområde | |
| polarity | polaritet | |
| fuse | säkring | |
| inline fuse | linjesäkring | |
| circuit breaker | automatsäkring | |
| current limiting | strömbegränsning | |
| overcurrent | överström | |
| voltage drop | spänningsfall | |
| grounding | jordning | |
| short circuit | kortslutning | |
| wire gauge | ledararea | Swedish uses mm², not AWG |
| marine-grade wire | sjövattenbeständig ledare | |
| wire strippers | avisoleringstång | |
| crimping | krimpning | |
| crimper | krimptång | |
| heat-shrink tubing | krympslang | |
| heat gun | varmluftspistol | |
| multimeter | multimeter | |
| terminal block | kopplingsplint | |
| strain relief | dragavlastning | |
| super-capacitor | superkondensator | |
| real-time clock | realtidsklocka | |
| backup battery | backupbatteri | |

### Connectors and interfaces

| English | Swedish | Note |
|:--------|:--------|:-----|
| connector | kontakt / anslutning | *anslutning* for a board-mounted socket |
| barrel connector | hålkontakt | |
| header | stiftlist | `40-polig GPIO-stiftlist` |
| pin | stift | |
| backbone | backbone | Established in Swedish NMEA 2000 usage |
| drop cable | stickledning | |
| T-connector | T-koppling | |
| termination (120 Ω) | termineringsmotstånd | |
| front panel | frontpanel | |
| jumper | bygel | |
| male / female | hane / hona | |

### System behaviour and status

| English | Swedish | Note |
|:--------|:--------|:-----|
| boat computer | båtdator | |
| to boot | starta | |
| first boot | första start | |
| shutdown | avstängning | |
| graceful shutdown | kontrollerad avstängning | |
| power loss | spänningsbortfall | |
| blackout | strömavbrott | |
| power management | strömhantering | |
| status LED | status-LED | |
| monitoring | övervakning | |
| passive cooling | passiv kylning | |
| filesystem | filsystem | |
| to unmount | avmontera | |
| watchdog | watchdog | |
| standby | vänteläge | |

### Software and networking

| English | Swedish | Note |
|:--------|:--------|:-----|
| firmware | firmware | Not *fast programvara* — matches the sibling decision to keep the trade term |
| daemon | daemon | |
| to flash | flasha | |
| operating system image | systemavbild | |
| headless | utan skärm | First mention: `utan skärm (headless)` |
| container app | containerapp | |
| container image | containeravbild | |
| dashboard | instrumentpanel | Homarr's *dashboard* view |
| WiFi Access Point | WiFi-accesspunkt | |
| wired / wireless | trådbunden / trådlös | |
| credentials | inloggningsuppgifter | |
| default password | standardlösenord | |
| single sign-on (SSO) | enkel inloggning (SSO) | |
| Certificate Authority (CA) | certifikatutfärdare (CA) | |
| web interface | webbgränssnitt | |
| browser | webbläsare | |

### Applications and use cases

| English | Swedish | Note |
|:--------|:--------|:-----|
| chart plotter | kartplotter | |
| data logging | datalagring | |
| vessel | fartyg | |
| fleet management | flotthantering | |
| predictive maintenance | förebyggande underhåll | |
| remote monitoring | fjärrövervakning | |
| compliance | överensstämmelse | |
| warranty | garanti | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
5. Every term used on the page that appears in this glossary matches it.
6. **The four rules at the top are tested against the pages, not re-read.** A
   half-applied typography rule looks followed when you read it. Both the French
   and German branches shipped one to review because it was read rather than
   measured.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md` — siblings
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

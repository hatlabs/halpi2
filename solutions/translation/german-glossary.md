---
title: German translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into German under docs/de/
  - Reviewing a German translation for consistency
  - Adding a new term that has no established German equivalent
tags:
  - translation
  - i18n
  - german
  - terminology
  - mkdocs-static-i18n
---

# German translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into German under `docs/de/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/de/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md` and `french-glossary.md` are the siblings of this file.
The general approach is the same in all three; the rules below cover what is
specific to German.

## Names that are never translated

Identical to the other glossaries: product names, protocol names, hardware
standards and software UI strings stay in English — HALPI2, HaLOS, Signal K,
OpenPlotter, Raspberry Pi OS, Cockpit, Homarr, Authelia, Grafana, Hat Labs,
Compute Module 5 (CM5), NMEA 2000, NMEA 0183, CAN FD, RS-485, NVMe SSD, GPIO,
HDMI, MIPI, USB, RP-SMA, E7T, PG7, SP13, IP65, DHCP, SSH, SSL, ABYC, Cat5e, AWG,
plus every UI path, command, hostname and file path.

Code fences, command output, URLs and image filenames are never touched.

## Style rules

### No space before punctuation

**German does not put a space before `;` `:` `!` `?`** — write `Symptome:`, not
`Symptome :`.

This is stated explicitly because the French glossary requires the opposite, and
that rule cost a 334-site correction on its own branch. Do not carry the French
habit across. German's non-breaking spaces belong elsewhere: between a number
and its unit, and inside abbreviations like `z. B.`.

### Quotation marks

German uses `„…"` — low opening, high closing. Not `"…"`, and not the French
`« … »`.

### Address form

Instructions use the **Sie form imperative**, the standard register for German
consumer and installation manuals:

> Schließen Sie das Stromkabel an. Prüfen Sie die Polarität mit dem Multimeter,
> bevor Sie die Spannung einschalten.

Not the infinitive (*Kabel anschließen*), which reads as a parts list, and not
*du*.

Descriptive passages use a plain statement or the passive:

> Das Gerät schaltet sich automatisch ab, wenn die Stromversorgung getrennt wird.

### Compound nouns

German compounds a multi-word proper name with hyphens throughout, which the
English source does not:

- `NMEA-2000-Netzwerk`, `NMEA-2000-Bus`, `Signal-K-Server`,
  `Raspberry-Pi-Antenne`, `Compute-Module-5-Anschluss`
- `HALPI2-Gehäuse`, `E7T-Stecker`, `HaLOS-Image`, `USB-Tastatur`

A missing hyphen inside such a compound is the most visible marker of a
machine-translated German page.

### Units and numbers

Same handling as the other languages — the English source writes `12V` and
`0.9A`, and both are wrong in German.

| English source | German |
|:---------------|:-------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |

### Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry an `en/`, `de/` or other language segment; image
captions and alt texts are translated but filenames are not; screenshots stay
English because the reader's own screen is English; standard admonition titles
are translated centrally in `mkdocs.yml`, custom ones in the page.

## Glossary

### Enclosure, mounting, and installation

| English | German | Note |
|:--------|:-------|:-----|
| carrier board | Trägerplatine | The accurate term, as in French — see the note below |
| enclosure | Gehäuse | |
| heat sink | Kühlkörper | |
| waterproof | wasserdicht | |
| wall-mount | Wandmontage | |
| mounting surface | Montagefläche | |
| pilot hole | Vorbohrung | |
| mounting template | Bohrschablone | |
| bilge | Bilge | |
| bulkhead | Schott | |
| cable gland | Kabelverschraubung | |
| cable routing | Kabelführung | |
| service loop | Serviceschlaufe | |
| cable tie | Kabelbinder | |
| blind plug | Blindstopfen | |
| breather plug | Druckausgleichsstopfen | |

**A note on `Trägerplatine`.** German takes the accurate term, like French
(`carte porteuse`) and unlike Finnish (`emolevy`, literally *motherboard*, chosen
there for reader familiarity). The divergence between the three is deliberate,
decided per language and per audience. Do not harmonise them.

The practical consequence matches French: `Trägerplatine` carries the CM5/board
relationship on its own, so passages about reseating the CM5 or troubleshooting
a board that will not boot need no extra explanation. The Finnish glossary does
need that warning.

### Electrical

| English | German | Note |
|:--------|:-------|:-----|
| power supply | Stromversorgung | The unit itself: *Netzteil* |
| input voltage range | Eingangsspannungsbereich | |
| polarity | Polarität | |
| fuse | Sicherung | |
| resistor | Widerstand | Value follows the noun: `Widerstände von 0 Ω`, `Pull-up-Widerstände von 2,2 kΩ` |
| inline fuse | Leitungssicherung | |
| circuit breaker | Leitungsschutzschalter | |
| current limiting | Strombegrenzung | |
| overcurrent | Überstrom | |
| voltage drop | Spannungsabfall | |
| grounding | Erdung | |
| short circuit | Kurzschluss | |
| wire gauge | Leiterquerschnitt | German uses mm², not AWG |
| marine-grade wire | seewasserfeste Leitung | |
| wire strippers | Abisolierzange | |
| crimping | Crimpen | |
| crimper | Crimpzange | |
| heat-shrink tubing | Schrumpfschlauch | |
| heat gun | Heißluftpistole | |
| multimeter | Multimeter | |
| terminal block | Klemmenblock | |
| strain relief | Zugentlastung | |
| super-capacitor | Superkondensator | |
| real-time clock | Echtzeituhr | |
| backup battery | Pufferbatterie | |
| uninterruptible power supply (UPS) | unterbrechungsfreie Stromversorgung (USV) | |
| inrush current | Einschaltstrom | |
| load dump | Lastabwurf (Load Dump) | Alternator load dump; keep the English term in parentheses on first mention |

### Connectors and interfaces

| English | German | Note |
|:--------|:-------|:-----|
| connector | Stecker / Anschluss | *Anschluss* for a board-mounted socket |
| onboard | integriert | `integriertes Gerät`, `integrierte Schnittstellen` — on the carrier board, as opposed to user-added |
| barrel connector | Hohlstecker | |
| header | Stiftleiste | `40-polige GPIO-Stiftleiste` |
| pin | Pin | |
| backbone | Backbone | Established in German NMEA 2000 usage |
| drop cable | Stichleitung | |
| T-connector | T-Stück | |
| termination (120 Ω) | Abschlusswiderstand | |
| front panel | Frontplatte | |
| jumper | Jumper | |
| male / female | Stecker / Buchse | |

### System behaviour and status

| English | German | Note |
|:--------|:-------|:-----|
| boat computer | Bordcomputer | |
| to boot | starten | |
| first boot | erster Start | |
| shutdown | Herunterfahren | |
| graceful shutdown | geordnetes Herunterfahren | |
| power loss | Spannungsausfall | |
| blackout | Stromausfall | |
| power management | Energieverwaltung | |
| status LED | Status-LED | |
| monitoring | Überwachung | |
| passive cooling | passive Kühlung | |
| filesystem | Dateisystem | |
| to unmount | aushängen | |
| watchdog | Watchdog | |
| standby | Standby | |
| operating mode | Betriebsart | Solo/Co-op: `Solo-Modus`, `Co-op-Modus` |
| state machine | Zustandsautomat | |
| charge level | Ladezustand | |
| power button | Ein-/Aus-Taste / Power-Taster | *Ein-/Aus-Taste* for the CM5's button input; *Power-Taster* for an external button wired to the header |
| blackout timer | Ausfallzeitgeber | |

### Software and networking

| English | German | Note |
|:--------|:-------|:-----|
| firmware | Firmware | |
| daemon | Daemon | |
| kernel module | Kernelmodul | |
| to flash | flashen | |
| operating system image | Systemabbild | |
| headless | ohne Bildschirm | First mention: `ohne Bildschirm (headless)` |
| container app | Container-Anwendung | |
| container image | Container-Image | |
| dashboard | Dashboard | |
| WiFi Access Point | WLAN-Access-Point | German prose says *WLAN*; keep *WiFi* only where it names a UI string or a physical label |
| wired / wireless | kabelgebunden / drahtlos | |
| credentials | Zugangsdaten | |
| default password | Standardpasswort | |
| single sign-on (SSO) | Single Sign-on (SSO) | |
| Certificate Authority (CA) | Zertifizierungsstelle (CA) | |
| web interface | Weboberfläche | |
| browser | Browser | |

### Applications and use cases

| English | German | Note |
|:--------|:-------|:-----|
| chart plotter | Kartenplotter | |
| data logging | Datenaufzeichnung | |
| vessel | Schiff | |
| fleet management | Flottenmanagement | |
| predictive maintenance | vorausschauende Wartung | |
| remote monitoring | Fernüberwachung | |
| compliance | Konformität | |
| warranty | Garantie | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run check-anchors site` passes.
3. `uv run translation-status` shows the page as current.
4. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
5. Every term used on the page that appears in this glossary matches it.

## Related

- `finnish-glossary.md`, `french-glossary.md` — the sibling glossaries
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

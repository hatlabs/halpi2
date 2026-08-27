---
title: Danish translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Danish under docs/da/
  - Reviewing a Danish translation for consistency
  - Adding a new term that has no established Danish equivalent
tags:
  - translation
  - i18n
  - danish
  - terminology
  - mkdocs-static-i18n
---

# Danish translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Danish under `docs/da/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/da/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
`norwegian-glossary.md` and `swedish-glossary.md` are the siblings of this file.
The general approach is the same in all of them.

## Five rules where the siblings are wrong for Danish

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary. Norwegian is the dangerous one:
it is close enough to Danish that a wrong form does not look wrong, and it is
being written at the same time as this language.

Each rule ends with the count that proves it. Run the counts; do not reread the
prose. Every language branch so far shipped a typography rule that had been read
rather than measured, and it looked followed right up until a reviewer counted.

1. **Quotation marks are `»…«`, pointing outward.** Opening `»` (U+00BB),
   closing `«` (U+00AB). This is the exact reverse of Norwegian's `«…»`, and it
   is neither German's `„…"` nor Swedish's `"…"` nor French's spaced `« … »`.

   *Count:* `grep -roE '«[^»]{0,120}»' docs/da | wc -l` must be **0** — every hit
   is a Norwegian-order quote. `grep -roc '»' docs/da` and `grep -roc '«' docs/da`
   must give the same total.

2. **Address the reader as `du`.** Danish technical and consumer documentation
   uses `du` throughout; the polite `De` is archaic and reads as parody in a
   product manual. German's `Sie` and French's *vouvoiement* are both wrong here.
   Instructions take the imperative: `Tilslut strømkablet.` /
   `Kontrollér polariteten med multimeteret, før du tænder for spændingen.`

   *Count:* `grep -rnE '\b(De|Dem|Deres)\b' docs/da` must return **0** hits that
   are not sentence-initial `De` meaning *they*. Every page with instructions
   must have at least one `du`/`dig`/`din`/`dit`/`dine`.

3. **No space before `; : ! ?`** — as in German, Swedish and Norwegian, and
   unlike French, whose rule is the exact opposite and demands a no-break space.

   *Count:* with code fences stripped, `grep -rnE ' [;:!?]' docs/da` must return
   **0**.

4. **Compounding with a proper name takes one hyphen at the junction, not
   throughout.** Danish writes `NMEA 2000-netværk`, `Signal K-server`,
   `Raspberry Pi-antenne`, `Compute Module 5-stik`. German writes
   `NMEA-2000-Netzwerk` — hyphens all the way through — and copying that pattern
   into Danish is wrong. Ordinary compounds are written **solid**, no hyphen and
   no space: `kabelforskruning`, `strømforsyning`, `strømafbrydelsestimer`,
   `indgangsspændingsområde`. A space inside a compound is the most visible
   marker of a machine-translated Danish page.

   *Count:* `grep -rnE 'NMEA-2000|Signal-K|Raspberry-Pi|Compute-Module' docs/da`
   must return **0**. `grep -rnE 'NMEA 2000[a-zæøå]' docs/da` must return **0**
   (a Danish head word glued on without the hyphen).

5. **Danish is not Norwegian.** These are the forms that leak, in the order they
   leak. Left is Danish and correct; right is Norwegian and must not appear.

   | Write | Never write | Where it shows up |
   |:------|:------------|:------------------|
   | `af` | `av` | everywhere — the highest-frequency tell |
   | `-tion` (`installation`, `konfiguration`, `isolation`) | `-sjon` | every second page |
   | `netværk` | `nettverk` | NMEA 2000, Ethernet |
   | `spænding`, `spændingsfald` | `spenning`, `spenningsfall` | electrical sections |
   | `vand`, `vandtæt`, `lænsevand` | `vann`, `vanntett` | mounting, enclosure |
   | `kun` | `berre` | prerequisites, warnings |
   | `ikke` | `ikkje` | warnings |
   | `hvordan` | `korleis` | procedures |
   | `nedlukning` | `nedstenging` | shutdown sections |

   *Count:* `grep -rniwE 'av|ikkje|berre|korleis|vann|nettverk|spenning' docs/da`
   must return **0**, and `grep -rniE '[a-zæøå]sjon' docs/da` must return **0**.

## Names that are never translated

Identical to the sibling glossaries: product names, protocol names, hardware
standards and software UI strings stay in English — HALPI2, HaLOS, Signal K,
OpenPlotter, Raspberry Pi, Raspberry Pi OS, Compute Module 5 (CM5), Cockpit,
Homarr, Authelia, Grafana, InfluxDB, AvNav, OpenCPN, Hat Labs, NMEA 2000,
NMEA 0183, CAN FD, RS-485, RS-422, SocketCAN, NVMe SSD, GPIO, HDMI, MIPI, USB,
RP-SMA, U.FL, E7T, PG7, SP13, Micro-C, IP65, DHCP, SSH, SSL, VNC, ABYC, Cat5e,
AWG, RP2040, gpsd, plus every UI path, command, hostname, file path,
configuration key and package name.

Command names (`halpi`, `halpid`, `rpiboot`, `candump`), file paths
(`/etc/halpid/halpid.conf`), configuration keys (`auto_restart`,
`led_brightness`, `AUTO_FLASH_ON_INSTALL`) and everything inside a code fence
stay exactly as the English source has them — including comments inside fences.
Command output is never touched. URLs and image filenames are never touched.

Mode names stay English, the head noun is Danish: `Solo-tilstand`,
`Co-op-tilstand`, `boot-tilstand`.

## Units and numbers

Same handling as the other languages — the English source writes `12V` and
`0.9A`, and both are wrong in Danish.

| English source | Danish |
|:---------------|:-------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |
| `250 kbps` | `250 kbit/s` |
| `2m`, `45mm` | `2 m`, `45 mm` |

Decimal comma in every measured value. Version numbers, firmware versions and
file paths keep their dots: `v0.6.1`, `3.1.0`, `/dev/ttyAMA4`.

*Count:* outside code fences, `grep -rnE '[0-9](V|A|W|Hz|Ω|mm|m |kg|°C)' docs/da`
must return **0** (missing space before the unit), and
`grep -rnE '[0-9]+-[0-9]+ *(V|A|°C|mA)' docs/da` must return **0** (hyphen
instead of en dash in a range).

## Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry a language segment; image captions and alt texts are
translated but filenames are not; screenshots stay English because the reader's
own screen is English; standard admonition titles are translated centrally in
`mkdocs.yml`, custom ones in the page.

## Glossary

### Enclosure, mounting, and installation

| English | Danish | Note |
|:--------|:-------|:-----|
| carrier board | bærekort | The accurate term, as in French, German and Swedish |
| enclosure | kabinet | |
| enclosure lid | kabinetlåg | |
| gasket | pakning | |
| heat sink | køleplade | |
| ingress protection (IP rating) | kapslingsklasse | `kapslingsklasse IP65` |
| waterproof | vandtæt | Not the Norwegian `vanntett` |
| wall-mount | vægmontering | |
| mounting surface | monteringsflade | |
| mounting screw | monteringsskrue | |
| countersunk screw | undersænket skrue | |
| standoff | afstandsbolt | |
| pilot hole (you drill it) | styrehul | `Bor styrehuller til monteringsskruerne` |
| pre-drilled hole (already in the enclosure) | forboret hul | `Kabinettet har forborede huller til panelstik` |
| mounting template | boreskabelon | |
| bilge water | lænsevand | `Monter over det forventede lænsevandsniveau` |
| bulkhead | skot | |
| cable gland | kabelforskruning | |
| cable routing | kabelføring | |
| service loop | servicesløjfe | Slack left at both cable ends |
| cable tie | kabelbinder | Not the colloquial `strips` |
| blind plug | blindprop | |
| breather plug | trykudligningsprop | |
| thermal pad | termisk pude | |
| silk screen | silketryk | |

**Two holes, two words.** `styrehul` is a hole *you* drill; `forboret hul` is a
hole the enclosure already ships with. Danish has one obvious root for both
(`forbore`), and using it for both produces the nonsense instruction *bor
forborede huller* — "drill pre-drilled holes" — which is exactly what happened
in Swedish. Keep the two words apart.

**A note on `bærekort`.** Danish takes the accurate term, like French
(`carte porteuse`), German (`Trägerplatine`) and Swedish (`bärkort`), and unlike
Finnish (`emolevy`, literally *motherboard*, chosen there for reader
familiarity). The divergence between the languages is deliberate, decided per
language and per audience. Do not harmonise them.

`bærekort` carries the CM5/board relationship on its own, so passages about
reseating the CM5 or troubleshooting a board that will not boot need no extra
explanation. Only the Finnish glossary needs that warning.

### Power and electrical

| English | Danish | Note |
|:--------|:-------|:-----|
| power supply | strømforsyning | Both the function and the external unit |
| power rail | spændingsskinne | Later mentions: `3,3 V-skinnen` |
| input voltage range | indgangsspændingsområde | |
| polarity | polaritet | |
| reverse polarity protection | beskyttelse mod omvendt polaritet | |
| fuse | sikring | |
| inline fuse | ledningssikring | |
| circuit breaker | automatsikring | |
| current limiting | strømbegrænsning | |
| current limiter | strømbegrænser | |
| current limit switch | strømbegrænsningskontakt | |
| overcurrent | overstrøm | |
| voltage drop | spændingsfald | Not the Norwegian `spenningsfall` |
| grounding | jordforbindelse | |
| ground loop | jordsløjfe | |
| short circuit | kortslutning | |
| galvanic isolation | galvanisk adskillelse | |
| wire gauge | ledertværsnit | Danish uses mm², not AWG |
| marine-grade wire | marinegodkendt ledning | |
| wire strippers | afisoleringstang | |
| crimping | krimpning | |
| crimper | krimptang | |
| heat-shrink tubing | krympeflex | |
| heat gun | varmepistol | |
| multimeter | multimeter | |
| terminal block | klemrække | The pluggable Phoenix connector on the board |
| strain relief | trækaflastning | |
| super-capacitor | superkondensator | |
| real-time clock | realtidsur | |
| backup battery | backupbatteri | |

### Connectors and interfaces

| English | Danish | Note |
|:--------|:-------|:-----|
| connector | stik / tilslutning | `tilslutning` for a board-mounted socket |
| panel connector | panelstik | |
| barrel connector | DC-jackstik | First mention: `DC-jackstik (barrel)` |
| header | stikliste | `40-benet GPIO-stikliste` |
| pin | ben | `Kortslut benene` |
| pitch | benafstand | `3,81 mm benafstand` |
| jumper | jumper | |
| solder jumper | loddejumper | |
| switch (physical) | kontakt | |
| backbone | backbone | Established in Danish NMEA 2000 usage |
| drop cable | dropkabel | |
| T-connector | T-stik | |
| terminator | terminering | The function; the part is `termineringsmodstand` |
| termination resistor (120 Ω) | termineringsmodstand | |
| front panel | frontpanel | |
| flexible flat cable (FFC) | fladkabel (FFC) | |
| male / female | hanstik / hunstik | |
| port | port | |

### Operation and system behaviour

| English | Danish | Note |
|:--------|:-------|:-----|
| boat computer | bådcomputer | |
| to boot | starte | Booting: `opstart` |
| first boot | første opstart | |
| shutdown | nedlukning | Not the Norwegian `nedstenging` |
| to shut down | lukke ned | |
| graceful shutdown | kontrolleret nedlukning | |
| to power-cycle | slukke og tænde igen | Not a noun in Danish |
| reboot / restart | genstart | |
| power loss | strømsvigt | The loss of input power the controller detects |
| blackout | strømafbrydelse | Timer: `strømafbrydelsestimeren` — one solid compound |
| power management | strømstyring | |
| status LED | status-LED | |
| indicator | indikator | |
| monitoring | overvågning | |
| passive cooling | passiv køling | |
| filesystem | filsystem | |
| to unmount | afmontere | Both senses: a filesystem, and physically removing the CM5 or the carrier board |
| to reseat | genmontere | |
| watchdog | watchdog | |
| standby | standby | |
| mode | tilstand | `Solo-tilstand`, `Co-op-tilstand` |
| controller | controller | The RP2040 on the carrier board; also `mikrocontroller` |

### Software and networking

| English | Danish | Note |
|:--------|:-------|:-----|
| firmware | firmware | Not `fast programmel` — matches the sibling decision to keep the trade term |
| daemon | dæmon | First mention: `dæmon (baggrundstjeneste)` |
| kernel module | kernemodul | |
| to flash | flashe | |
| system image | systemimage | `et systemimage`, `systemimaget` — the trade says *image*, not *aftryk* |
| operating system image | styresystemimage | |
| container image | containerimage | |
| container app | containerapp | |
| headless | uden skærm | First mention: `uden skærm (headless)` |
| dashboard | dashboard | Kept: it is the name of the HaLOS page the reader opens |
| web interface | webgrænseflade | |
| browser | browser | |
| credentials | loginoplysninger | |
| username | brugernavn | |
| default password | standardadgangskode | |
| single sign-on (SSO) | single sign-on (SSO) | |
| Certificate Authority (CA) | certifikatmyndighed (CA) | |
| WiFi Access Point | WiFi-adgangspunkt | Keep `WiFi Access Point` where it names a UI string |
| wired / wireless | kablet / trådløs | |
| remote access | fjernadgang | |
| setting | indstilling | |
| update | opdatering | |
| package | pakke | |
| command line tool | kommandolinjeværktøj | |

### Applications and use cases

| English | Danish | Note |
|:--------|:-------|:-----|
| chart plotter | kortplotter | |
| data logging | datalogning | |
| vessel | fartøj | `båd` only where the source says *boat* |
| depth sounder | ekkolod | |
| wind instrument | vindmåler | |
| GPS receiver | GPS-modtager | |
| fleet management | flådestyring | |
| predictive maintenance | forudsigende vedligeholdelse | |
| remote monitoring | fjernovervågning | |
| compliance | overensstemmelse | |
| warranty | garanti | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. `uv run python scripts/check_glossary.py da` passes.
5. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
6. Every number in the English text appears in the translation. A wrong voltage
   or current in an installation guide is a safety problem, not a typo.
7. **The five rules at the top are counted against the pages, not re-read.**
   Every count below must come out at zero:

```bash
# 1 — Norwegian-order quotes
grep -roE '«[^»]{0,120}»' docs/da | wc -l
# 1 — » and « must balance
grep -ro '»' docs/da | wc -l; grep -ro '«' docs/da | wc -l
# 2 — polite address
grep -rnE '\b(De|Dem|Deres)\b' docs/da
# 3 — French spacing
grep -rnE ' [;:!?]' docs/da
# 4 — German hyphen chains, and missing junction hyphen
grep -rnE 'NMEA-2000|Signal-K|Raspberry-Pi|Compute-Module|NMEA 2000[a-zæøå]' docs/da
# 5 — Norwegian forms
grep -rniwE 'av|ikkje|berre|korleis|vann|nettverk|spenning' docs/da
grep -rniE '[a-zæøå]sjon' docs/da
# units
grep -rnE '[0-9](V|A|W|Hz|Ω|mm|kg|°C)' docs/da
grep -rnE '[0-9]+-[0-9]+ *(V|A|mA|°C)' docs/da
# compounds that must be solid
grep -rniE 'kabel forskruning|strøm forsyning|bære kort|super kondensator' docs/da
```

Strip code fences before running the spacing, unit and hyphen counts — commands,
paths and configuration keys legitimately contain all of them:

```bash
python3 - <<'PY'
import re, pathlib
for p in sorted(pathlib.Path('docs/da').rglob('*.md')):
    t = re.sub(r'^---\n.*?\n---\n', '', p.read_text(encoding='utf-8'), flags=re.S)
    t = re.sub(r'```.*?```', ' ', t, flags=re.S)
    t = re.sub(r'`[^`\n]*`', ' ', t)
    print(p, len(re.findall(r' [;:!?]', t)), len(re.findall(r'[0-9](V|A|W|mm|°C)', t)))
PY
```

A non-zero count is the finding. A rule that was read looks followed.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
  `norwegian-glossary.md`, `swedish-glossary.md` — siblings
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

## Terms added during translation

Reported by the page translators, consolidated here rather than written
by each of them, because five agents share this file.

| English | Translation | Note |
|:--------|:------------|:-----|
| apt repository | apt-pakkearkiv | ubuntu-installation.md heading and body; glossary has 'package' but not 'repository'. 'pakkearkiv' is the standard Danish term for a Debian/apt repo;  |
| schematic | kredsløbsdiagram | design-files.md title and body; mkdocs.yml nav_translations already fixes 'Design Files and Schematics' -> 'Designfiler og kredsløbsdiagrammer', so th |
| PCB layout | print-layout | design-files.md; 'print' is the established Danish word for a printed circuit board, and 'layout' is the trade term |
| component footprint | komponent-footprint | design-files.md 0.6.0 changelog; Danish PCB practice keeps 'footprint' untranslated — 'fodaftryk' would not be understood |
| buck converter | buckomformer | design-files.md 0.6.0 changelog; solid compound per rule 4, junction hyphen only against the number: '10 V-buckomformeren' |
| opamp / operational amplifier | operationsforstærker | design-files.md 0.6.0 changelog |
| solder nut | loddemøtrik | design-files.md 0.5.0 changelog |
| copper pour / copper fill | kobberflade / kobberudfyldning | design-files.md and errata.md; 'kobberflade' for the plural pours in the changelog, 'kobberudfyldning' for the errata heading |
| power plane | forsyningsplan | errata.md; later mention shortened to '3,3 V-planet' as the glossary does for spændingsskinne |
| mounting ledge | monteringsafsats | errata.md; the cast ledges inside the enclosure that the board rests on |
| flash (casting residue) | grat / gratkant | errata.md; the English source quotes "flashes" as leftover casting aluminium — unrelated to 'to flash' firmware, which stays 'flashe' |
| solder mask | loddemaske | errata.md |
| inrush current | indkoblingsstrøm | errata.md; distinct from 'overstrøm' in the glossary |
| thermal throttling | termisk nedregulering | troubleshooting.md, CPU temperature section |
| stray voltage | vildfaren spænding | troubleshooting.md rainbow-LED section |
| rollback (firmware) | tilbagerulning / rulle tilbage | troubleshooting.md firmware section |
| single-board computer | enkeltkortcomputer | index.md; solid compound, distinct from 'bærekort' |
| glitch immunity | immunitet over for korte spændingsudfald | index.md hardware feature list; rendered descriptively since Danish has no single trade term |
| cross-compilation | krydskompilering | integration.md placeholder bullet |
| security hardening | sikkerhedshærdning | advanced-config.md placeholder bullet |
| brownout | underspænding | power-supply.md placeholder bullet; 'strømafbrydelse' in the glossary is the full blackout, so a separate word was needed |
| wall wart (plug-in mains power supply) | netadapter | "What You'll Need" list, DC barrel connector bullet. The glossary has 'power supply' -> 'strømforsyning' but nothing for the scare-quoted colloquial ' |
| peripherals | perifere enheder | Heading 'Step 1: Connect Essential Peripherals' and the 'high-current peripherals' sentence in the current-limiting section. Standard Danish IT term;  |
| terminals (crimp-on ring/spade terminals) | kabelsko | 'Heat-shrink tubing and terminals' and 'Install terminals using proper crimping technique'. The glossary's 'terminal block' -> 'klemrække' is the boar |
| cable grommet | gennemføringstyl | 'Install cable glands or cable grommets if routing through bulkheads'. The glossary covers 'cable gland' -> 'kabelforskruning' but not the rubber grom |
| splash screen | startskærm | 'Raspberry Pi OS splash screen' in the First Boot section. |
| mounting hardware | monteringsbeslag | 'Use corrosion-resistant mounting hardware' under Marine Installations. Glossary has 'mounting screw' and 'standoff' but no collective term. |
| chafing | skamfiling | 'Protect cable from chafing and damage' in Cable Preparation; the standard Danish marine word for line/cable wear. |
| electrical code | elregler | 'Ensure compliance with local electrical codes' / 'Comply with local electrical codes'. Glossary has 'compliance' -> 'overensstemmelse' but not the co |
| flow control (hardware flow control) | flowkontrol (hardwarestyret flowkontrol) | technical-reference/interfaces.md, ctsrts paragraph. 'flowkontrol' is the established Danish trade term; 'strømningsstyring' would read as fluid mecha |
| chip select | chip select | technical-reference/interfaces.md CTS/RTS conflict table ('CAN FD chip-select'). Kept English, as Danish PCB/embedded practice does; rendered as 'Chip |
| transceiver (RS-485 transceiver) | transceiver | technical-reference/interfaces.md, rs485 parameter paragraph. Kept English; 'sendemodtager' exists but is not what Danish RS-485 documentation says. N |
| device node | enhedsnode | technical-reference/interfaces.md 'Verifying' section. Solid compound, standard Danish Linux usage. |
| block device | blokenhed | user-guide/software.md step 6 of the USB-boot procedure. Solid compound. |
| mass storage device / mass-storage gadget firmware | masselagerenhed / firmwaren til masselagerenheden | user-guide/software.md steps 4-6. 'masselager' is the standard Danish term; the English 'gadget' is dropped because Danish has no equivalent and it ad |
| port forwarding | portviderestilling | user-guide/software.md, VNC-over-internet paragraph. Solid compound; 'port forwarding' is also heard but the Danish form is unambiguous. |
| marine apps | marineapplikationer | user-guide/software.md image-variant table and Homarr dashboard bullet. Solid compound. Distinct from the glossary's 'containerapp', which names the C |
| login console | loginkonsol | technical-reference/interfaces.md UART intro. Solid compound, consistent with the glossary's 'loginoplysninger'. |
| setup wizard | opsætningsguide | user-guide/software.md, Raspberry Pi OS configuration section. |
| HAT (Raspberry Pi HAT) | HAT / HAT'er | hardware.md, whole 'Using HATs' section. The glossary lists no form for it; kept English as a hardware-standard name and inflected with apostrophe-s i |
| spudger | spudger (åbnerpind) | hardware.md, CM5 removal. No Danish trade word exists; first mention glosses it, following the glossary's own 'dæmon (baggrundstjeneste)' / 'uden skær |
| socket (the tool: 26mm socket, hex socket) | top / sekskanttop | hardware.md, connector removal. Must not collide with 'stik', which the glossary already assigns to the electrical connector sense — a reader meeting  |
| board-to-board connector | kort-til-kort-stik | hardware.md, CM5 replacement. Phrase compound, so hyphens throughout are correct Danish here and do not conflict with rule 4, which governs proper-nam |
| threaded insert | gevindindsats | hardware.md, HAT installation ('pre-installed M2.5 threaded inserts'). Distinct from 'afstandsbolt' (standoff), which the glossary already has and whi |
| device tree overlay | device tree-overlay | hardware.md, interface sharing and software configuration. Kept English because it names the `dtoverlay` config key the reader types; junction hyphen  |
| clearance (vertical clearance above the board) | frihøjde | hardware.md, physical constraints and standoff sizing. The standard Danish term for the free space above a component. |
| voltage bar (LED pattern) | spændingssøjle | operation.md, LED status quick-reference table — the LED row acting as a bar-graph readout of super-capacitor charge. Derived from the glossary's 'spæ |
| grace period | henstandsperiode | operation.md, automatic restart behaviour ('5-second grace period'). |
| wake-up event | opvækningshændelse | operation.md, standby mode feature-status admonition. |
| amber (LED colour) | ravgul | hardware.md, status LED table. Needed a distinct word from 'gul' (yellow), which the same table already uses for LED 3. |
| TVS clamping | TVS-begrænsning | technical-reference/hardware.md, input protection sentence. The glossary has no entry for clamping; 'begrænsning' matches 'strømbegrænsning' already i |
| thermal management | termisk styring | technical-reference/hardware.md H2. Chosen over the more literal 'varmeafledning' because docs/da/user-guide/hardware.md already renders the same Engl |
| load equivalency number (LEN) | Load Equivalency Number (LEN) | user-guide/interfaces.md, NMEA 2000 network loading. Kept in English as an NMEA 2000 standard designation, like the other protocol names; later mentio |
| transmit enable (RS-485) | sendetilladelse | user-guide/interfaces.md, RS-485 hardware configuration. No glossary entry; 'sendetilladelse' is the standard Danish description and avoids leaving an |
| multi-talker / single-talker network | multi-talker- / single-talker-anvendelser, netværk med flere talere / med én taler og flere lyttere | user-guide/interfaces.md. The adjectival compounds keep the NMEA 0183 trade terms; the descriptive form is used where the source spells out 'single-ta |
| form factor (M.2) | formfaktor | technical-reference/hardware.md, M.2 NVMe slot ('formfaktorerne 2230 til 2280'). |
| die-cast aluminium | trykstøbt aluminium | technical-reference/hardware.md, enclosure material rows. Note docs/da/user-guide/hardware.md paraphrases the same English as 'støbt aluminium' withou |
| ferrite bead filtering | filtrering med ferritperler | technical-reference/hardware.md, USB 3.0 ports. |
| normally-open (NO) momentary switch | momentkontakt af typen normalt åben (NO) | user-guide/interfaces.md, button header. The glossary has 'switch (physical) = kontakt' but nothing for the momentary/NO qualifiers. |
| pinout | benforbindelser | technical-reference/hardware.md H2 'Stikkenes benforbindelser' and user-guide/interfaces.md H3 'Benforbindelser på knapstiklisten'. Built on the gloss |
| fan (CM5 / PWM fan) | blæser | Consistency pass. 'ventilator' had appeared in user-guide/hardware.md while technical-reference/hardware.md used 'blæser'. 'blæser' is the Danish trade word for a CPU/PWM fan, and it keeps 'ventilation' free for the airflow-around-the-enclosure sense the getting-started page uses. |
| airflow / air circulation | luftcirkulation | Consistency pass. 'luftstrøm' had appeared once in getting-started.md. Treated as one concept: the same physical thing whether the source says 'airflow' or 'air circulation'. Distinct from 'ventilation', which renders the source's own 'ventilation'. |
| web-managed interface | webstyret grænseflade | Consistency pass. 'webadministreret grænseflade' had appeared in getting-started.md. 'webstyret' is the compact compound and avoids 'webadministreret grænseflade til systemadministration' in user-guide/software.md. Distinct from 'web interface' -> 'webgrænseflade' and 'web-based' -> 'webbaseret'. |
| baud rate | baudhastighed | Consistency pass. 'baudrate' had appeared once in troubleshooting.md. 'baudhastighed' matches the other rate compounds already in use ('opdateringshastighed', 'datahastigheder'). |
| repository (Git/GitHub) | repositorium (bestemt form: repositoriet) | Consistency pass. 'GitHub-arkivet' had appeared in design-files.md. 'arkiv' is reserved for the apt sense ('pakkearkiv'), so the source-code repository takes 'repositorium' — what Danish developers say. |
| diagnostics / diagnostic | diagnostik | Consistency pass. 'diagnose' had appeared once in index.md. In Danish 'diagnose' is the result, 'diagnostik' the activity — the latter is what the source means. |
| resistor (pull-up, 0 Ω series) | modstand ('pull-up-modstand', '0 Ω-modstand') | technical-reference/hardware.md I2C section. The glossary only had the compound 'termineringsmodstand', not the bare head word; the junction hyphen against the value follows rule 4, as in '3,3 V-skinnen'. |
| load dump | load dump | technical-reference/power-supply.md input stage. Kept English as the automotive trade term; 'belastningsdump' is not used in Danish practice. |
| power budget | effektbudget | technical-reference/power-supply.md current-limiting section. Solid compound. |
| input stage | indgangstrin | technical-reference/power-supply.md H2. Definite form 'indgangstrinnet'. |
| state machine | tilstandsmaskine | technical-reference/power-supply.md intro. Standard Danish CS term; matches 'tilstand' already in the glossary. |
| fallback (mode / setting) | reservetilstand / reserveindstilling | technical-reference/controller.md: Solo mode as 'the fallback mode' and 'the firmware fallback' for auto_restart. 'fallback' untranslated would read as jargon; 'reserve-' carries both uses. |
| uninterruptible power supply (UPS) | UPS (nødstrømsforsyning) | operation.md and power-supply.md 'Not a UPS' admonitions. First mention glosses the abbreviation; later mentions are bare 'UPS'. |
| charge-level bar (LED pattern) | ladeniveausøjle | technical-reference/controller.md LED table. Built on 'spændingssøjle' already in the glossary; 'ladeniveau' was already in use in operation.md. |
| to feed the watchdog / watchdog feed | fodre watchdoggen / fodring | controller.md watchdog section. Continues the phrase the old operation.md established ('Fodring af watchdoggen'). |
| residual charge | restladning | technical-reference/controller.md, PowerOff state row. Solid compound. |
| firmware variant | firmwarevariant | user-guide/interfaces.md WiFi-afsnit; `update-alternatives`-valget mellem `standard` og `minimal`. Solid sammensætning efter regel 4 |
| WiFi channel | kanal | Samme afsnit: `kanalvalg` for det automatiske valg, `fast kanal` for et fastlagt |
| access point client | klient | Enhed tilsluttet adgangspunktet; adskilt fra klientprogrammet (SSH-klient) i software.md |

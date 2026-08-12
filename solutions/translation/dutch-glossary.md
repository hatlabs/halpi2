---
title: Dutch translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Dutch under docs/nl/
  - Reviewing a Dutch translation for consistency
  - Adding a new term that has no established Dutch equivalent
tags:
  - translation
  - i18n
  - dutch
  - terminology
  - mkdocs-static-i18n
---

# Dutch translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Dutch under `docs/nl/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/nl/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md`, `german-glossary.md` and
`swedish-glossary.md` are the siblings of this file. The general approach is the
same in all five.

## Seven rules where the siblings are wrong for Dutch

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary. Dutch sits closest to German and
Swedish — solid compounds, no space before punctuation — which is exactly why the
places where it diverges from them get carried across unnoticed.

1. **Address the reader as `u` / `uw`, never `je`, `jij`, `jouw` or `jullie`.**
   Dutch installation, safety and consumer manuals use `u`; Swedish uses `du`,
   and copying that register produces a page that reads as a hobby blog next to
   a warning about 32 V and short circuits.

   The trap is that the Dutch imperative is *identical* for both registers —
   `Sluit de voedingskabel aan.` `Controleer de polariteit met de multimeter
   voordat u de spanning inschakelt.` The register only surfaces in pronouns and
   possessives, so a page can be 90 % correct and still leak `je` in three
   places. That is why this is counted, not read.

   Write `u` and `uw` in lowercase. Capital `U` is an archaic reverential form
   and is wrong here.

2. **Quotation marks are `“…”` — U+201C opening, U+201D closing, two different
   characters.** Not German's `„…“`, not Swedish's `”…”` (the *same* character
   twice), not French's `« … »`, not straight `"…"`. A leaked Swedish habit is
   visible as a `”` count higher than the `“` count.

3. **Dutch does not capitalise common nouns.** German capitalises every noun;
   Dutch capitalises only proper names and the first word of a sentence or
   heading. Write `behuizing`, `voeding`, `carrierboard`, `afsluitweerstand`,
   `bestandssysteem` mid-sentence — never `Behuizing`, `Voeding`,
   `Carrierboard`. This is the single most likely German leak.

   The same rule flattens English title case in headings: `Permanent Power
   Installation` becomes `Vaste voedingsinstallatie`, not `Vaste
   Voedingsinstallatie`.

4. **Compounds are solid, but a compound with a proper name takes exactly one
   hyphen, at the junction.** Dutch writes `NMEA 2000-netwerk`, `Signal
   K-server`, `Raspberry Pi-antenne`, `HALPI2-behuizing`, `E7T-connector`,
   `PG7-kabelwartel`, `M.2-slot`, `CM5-module`. German writes
   `NMEA-2000-Netzwerk` — hyphens all the way through — and that pattern is
   wrong in Dutch.

   Ordinary Dutch compounds carry no hyphen and no space: `voedingskabel`,
   `kabelwartel`, `afsluitweerstand`, `supercondensator`, `frontpaneel`,
   `bestandssysteem`. English two-word terms adopted whole become one Dutch
   word: `carrier board` → `carrierboard`, `access point` → `accesspoint`.

5. **No space before `; : ! ?`** — as in German and Swedish, and unlike French,
   whose rule is the exact opposite and demands a no-break space.

6. **`led` is an ordinary lowercase Dutch word, not an abbreviation.** German
   writes `Status-LED` and Swedish `status-LED`; Dutch writes `status-led`,
   `rgb-led` → `RGB-led`, plural `leds`. Uppercase `LED` belongs only inside
   code, file paths and quoted silkscreen labels. Same for `wifi` (lowercase in
   prose; `WiFi (wlan0)` stays as written when it names the on-screen menu
   item).

7. **HALPI2 is a `de`-word, the carrierboard is a `het`-word.** Grammatical
   gender drifts between pages faster than terminology does, because nothing
   flags it. Fix it here:

   | Article | Nouns |
   |:--------|:------|
   | `de` | HALPI2, behuizing, voeding, zekering, connector, kabelwartel, aardlekbeveiliging, supercondensator, afsluitweerstand, daemon, controller |
   | `het` | carrierboard, frontpaneel, bestandssysteem, schot, klemmenblok, systeemimage, dashboard, energiebeheer |

   English possessives do not survive the crossing: `HALPI2's enclosure` becomes
   `de behuizing van de HALPI2`, never `HALPI2's behuizing`. The apostrophe-`s`
   in Dutch marks the plural of a vowel-final word or an abbreviation
   (`schema's`, `SSD's`, `HAT's`), nothing else.

## Names that are never translated

Product names, protocol names, hardware standards and software UI strings stay
in English — HALPI2, HaLOS, Signal K, OpenPlotter, Raspberry Pi OS, Cockpit,
Homarr, Authelia, Grafana, Hat Labs, Compute Module 5 (CM5), NMEA 2000,
NMEA 0183, CAN FD, RS-485, NVMe SSD, GPIO, HDMI, MIPI, USB, RP-SMA, E7T, PG7,
SP13, IP65, DHCP, SSH, SSL, ABYC, Cat5e, AWG.

So does every **command name** (`halpi`, `halpid`, `raspi-config`, `candump`,
`rpiboot`, `passwd`, `shutdown`), every **file path** (`/dev/ttyAMA4`,
`/etc/halpid/halpid.conf`, `/boot/firmware/config.txt`), every **configuration
key** (`auto_restart`, `led_brightness`, `AUTO_FLASH_ON_INSTALL`,
`watchdog_timeout`), every **hostname and interface name** (`halos.local`,
`can0`, `eth0`, `wlan0`), and every **UI string the reader will see in English on
their own screen** (**Networking**, **WiFi (wlan0)**, **Add**, `Normal`,
`Abnormal`).

Code fences and their contents, command output, URLs and image filenames are
never touched.

## Units and numbers

The English source writes `12V` and `0.9A`. Both are wrong in Dutch and need an
active conversion on nearly every technical page.

| English source | Dutch |
|:---------------|:------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `1.5mm²`, `2m` | `1,5 mm²`, `2 m` |
| `3-5A` | `3–5 A` (en dash for ranges) |
| `250 kbps` | `250 kbit/s` |

- **Decimal comma**, always: `0,9 A`, `5,5 mm`, `3,3 V-rail`, `10,8 V`.
- **A space between the number and its unit**, preferably a no-break space
  (U+00A0), including before `°C` and `Ω`.
- **No thousands separator** in technical values: `115200 bps`, not `115.200`.
- **Dimensions given as a single product spec keep the tight form:**
  `200 × 130 × 60 mm`, with `×` (U+00D7), not the letter `x`.
- **Version numbers, part numbers and addresses are identifiers, not numbers**:
  `v0.6.1`, `M.2`, `0x6d`, `2.54 mm` pitch keeps its decimal comma → `2,54 mm`,
  but `v0.6.1` keeps its points.

## Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry an `en/` or `nl/` segment; image captions and alt
texts are translated but filenames are not; screenshots stay English because the
reader's own screen is English; standard admonition titles are translated
centrally in `mkdocs.yml`, custom ones — `!!! note "Shop Link"` →
`!!! note "Link naar de webshop"` — in the page.

## Glossary

### Enclosure, mounting, and installation

| English | Dutch | Note |
|:--------|:------|:-----|
| carrier board | carrierboard | One word, lowercase, `het`-woord — see the note below |
| enclosure | behuizing | |
| lid | deksel | |
| gasket | afdichtingsrubber | Lid gasket |
| heat sink | koellichaam | Not *koelblok*, which is a cooling block on a chip |
| waterproof | waterdicht | |
| rugged | robuust | |
| wall-mount | wandmontage | |
| mounting surface | montageondergrond | What you drill into |
| pilot hole (to drill) | voorboren (verb) | `Boor de bevestigingsgaten voor.` Never `voorgeboorde gaten boren` |
| pre-drilled hole (already there) | voorgeboord gat | The holes the enclosure ships with |
| mounting template | boormal | |
| clearance | vrije ruimte | |
| bilge water | bilgewater | Also seen as *lenswater*; use `bilgewater` on every page |
| bulkhead | schot | `het schot`, plural `schotten` |
| cable gland | kabelwartel | `PG7-kabelwartel` |
| cable routing | kabelroute | The verb is *leggen* / *leiden* |
| service loop | servicelus | Slack left at both cable ends |
| chafing | schuren | |
| cable tie | kabelbinder | |
| blind plug | blindplug | |
| breather plug | ontluchtingsplug | For *pressure equalization* → *drukvereffening* |
| standoff | afstandsbus | |
| threaded insert | draadinzetstuk | |

**A note on `carrierboard`, and why it differs from the siblings.** French,
German and Swedish each coined an accurate native term (`carte porteuse`,
`Trägerplatine`, `bärkort`); Finnish took the familiar-but-inaccurate `emolevy`
(*motherboard*). Dutch takes neither route: the Dutch marine and Raspberry Pi
trade already says *carrier board*, and Dutch spelling turns an adopted English
two-word term into one word — `carrierboard`.

Do not "harmonise" the five. They differ on purpose, decided per language and
per audience.

Two consequences worth stating:

- **Never write `moederbord`.** That is the Finnish trade-off, and it inverts
  the CM5/board relationship: it would make the board the computer and the CM5
  an add-on, which is the reverse of how HALPI2 is built. `carrierboard` carries
  the relationship correctly on its own, so passages about reseating the CM5 or
  troubleshooting a board that will not boot need no extra explanation.
- **Never write `carrier board` with a space,** and never capitalise it
  mid-sentence. Those are the English and German habits respectively, and both
  are countable.

### Electrical

| English | Dutch | Note |
|:--------|:------|:-----|
| power supply | voeding | The unit itself: *voedingsadapter* |
| power source | voedingsbron | |
| input voltage range | ingangsspanningsbereik | |
| polarity | polariteit | |
| positive (+) / negative (−) | plus (+) / min (−) | |
| fuse | zekering | |
| inline fuse | kabelzekering | A fuse holder fitted in the positive lead |
| circuit breaker | installatieautomaat | The panel breaker; on a boat panel often just *automaat* |
| current limiting | stroombegrenzing | The switch is the *stroombegrenzer* |
| overcurrent | overstroom | |
| inrush current | inschakelstroom | |
| voltage drop | spanningsval | |
| grounding | aarding | |
| ground loop | aardlus | |
| short circuit | kortsluiting | |
| wire gauge | aderdoorsnede | Dutch uses mm², not AWG |
| marine-grade wire | kabel van maritieme kwaliteit | |
| to strip (a wire) | strippen | |
| wire strippers | striptang | |
| crimping | krimpen | Noun: *krimpverbinding* |
| crimper | krimptang | |
| crimp terminal | kabelschoen | |
| heat-shrink tubing | krimpkous | |
| heat gun | heteluchtpistool | |
| multimeter | multimeter | |
| continuity test | doorbelmeting | |
| terminal block | klemmenblok | The pluggable Phoenix MC connector |
| strain relief | trekontlasting | |
| super-capacitor | supercondensator | One word, lowercase |
| real-time clock | realtimeklok | Abbreviate as RTC after first mention |
| backup battery | backupbatterij | The cell itself is a `CR2032-knoopcel` |

### Connectors and interfaces

| English | Dutch | Note |
|:--------|:------|:-----|
| connector | connector / aansluiting | *aansluiting* for a board-mounted socket |
| barrel connector | DC-plug | Add *(barrel connector)* on first mention |
| header | pinheader | `40-pins GPIO-pinheader` |
| pin | pin | |
| pitch | steek | `3,81 mm steek` |
| backbone | backbone | Established in Dutch NMEA 2000 usage |
| drop cable | aftakkabel | |
| T-connector | T-stuk | Also renders *T-adapter* |
| terminator / termination (120 Ω) | afsluitweerstand | The component; the act is *afsluiten* |
| front panel | frontpaneel | |
| jumper | jumper | |
| male / female | male / female | Trade usage; use *stekker / bus* when the plug-socket pair is meant |
| antenna | antenne | |
| extension cable | verlengkabel | |
| flexible flat cable (FFC) | platte flexkabel (FFC) | Keep the abbreviation after first mention |

### Operation, system behaviour and status

| English | Dutch | Note |
|:--------|:------|:-----|
| boat computer | boordcomputer | |
| to boot | opstarten | |
| first boot | eerste start | |
| shutdown | afsluiten | The noun is *het afsluiten* |
| graceful shutdown | gecontroleerd afsluiten | |
| to power down | uitschakelen | Cutting power, as opposed to *afsluiten* |
| power loss | spanningsuitval | The input goes away |
| blackout | stroomuitval | The boat's supply goes away; the firmware timer stays `blackouttimer` |
| glitch immunity | storingsongevoeligheid | |
| power management | energiebeheer | |
| status LED | status-led | Lowercase *led*, plural *leds* |
| LED bar | ledbalk | |
| monitoring | bewaking | |
| passive cooling | passieve koeling | |
| thermal pad | thermisch pad | |
| filesystem | bestandssysteem | |
| to unmount (a filesystem) | ontkoppelen | `het bestandssysteem wordt veilig ontkoppeld` |
| to unmount (a board or module) | demonteren | The English source uses one word for both — this one is mechanical: `het carrierboard demonteren`, `de CM5-module losnemen` |
| to reseat (a module) | opnieuw plaatsen | |
| watchdog | watchdog | |
| standby | standby | `standbymodus`, one word |
| solo mode / co-op mode | solomodus / co-opmodus | Named firmware states; keep them recognisable |

### Software and networking

| English | Dutch | Note |
|:--------|:------|:-----|
| firmware | firmware | Not *bedrijfsprogrammatuur* — the trade term, as in every sibling |
| daemon | daemon | Not *achtergronddienst* |
| kernel module | kernelmodule | |
| to flash | flashen | Past participle *geflasht* |
| system image / operating system image | systeemimage | |
| container image | containerimage | Not *systeemimage* — that is a disk image |
| container app | containerapp | |
| headless | zonder beeldscherm | First mention: `zonder beeldscherm (headless)` |
| deployment | ingebruikname | |
| dashboard | dashboard | Homarr's *dashboard* view; `het dashboard` |
| WiFi Access Point | wifi-accesspoint | `wifi` lowercase in prose; `WiFi (wlan0)` stays as written when naming the menu item |
| wired / wireless | bekabeld / draadloos | |
| credentials | inloggegevens | |
| username / password | gebruikersnaam / wachtwoord | |
| default password | standaardwachtwoord | |
| single sign-on (SSO) | single sign-on (SSO) | Kept in English; it names the Authelia concept |
| Certificate Authority (CA) | certificaatautoriteit (CA) | |
| to trust (a certificate) | vertrouwen | |
| web interface | webinterface | |
| browser | browser | |
| system administration | systeembeheer | |
| package | pakket | Debian package → `Debian-pakket` |

### Applications and use cases

| English | Dutch | Note |
|:--------|:------|:-----|
| chart plotter | kaartplotter | |
| data logging | dataregistratie | |
| vessel | vaartuig | |
| engine parameters | motorgegevens | |
| fleet management | wagenparkbeheer | The source uses this under *Automotive*; for ships it would be *vlootbeheer* |
| process monitoring | procesbewaking | |
| remote monitoring | bewaking op afstand | |
| predictive maintenance | voorspellend onderhoud | |
| electromagnetic interference (EMI/RFI) | elektromagnetische storing (EMI/RFI) | |
| compliance | conformiteit | |
| warranty | garantie | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. `uv run python scripts/check_glossary.py nl` passes.
5. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
6. **The seven rules at the top are counted against the pages, not re-read.**

That last one is the point of this section. A half-applied typography rule looks
followed when you read it, because rereading your own text confirms whatever it
already says. The French and German branches each shipped one to review for
exactly that reason. Run this instead:

```bash
python3 - <<'PY'
import pathlib, re
def prose(p):
    t = re.sub(r'^---\n.*?\n---\n', '', p.read_text(encoding='utf-8'), flags=re.S)
    t = re.sub(r'```.*?```', ' ', t, flags=re.S)   # code fences
    return re.sub(r'`[^`\n]*`', ' ', t)            # inline code
text = '\n'.join(prose(p) for p in sorted(pathlib.Path('docs/nl').rglob('*.md')))
n = lambda pat: len(re.findall(pat, text))
report = [
    ('rule 1  informal address je/jij/jouw/jullie', n(r'\b[Jj](?:e|ij|ouw|ullie)\b')),
    ('rule 1  reverential capital U',               n(r'\bU\b')),
    ('rule 2  wrong quote characters „ « » "',      n(r'[„«»"]')),
    ('rule 2  unpaired “ vs ”',              abs(n('“') - n('”'))),
    ('rule 3  spaced "carrier board"',              n(r'(?i)carrier board')),
    ('rule 3  capitalised Carrierboard/Behuizing',  n(r'(?<![.!?]\s)(?<!^)\b(?:Carrierboard|Behuizing|Voeding|Zekering)\b')),
    ('rule 4  German-style name compounds',         n(r'NMEA-2000|Signal-K|Raspberry-Pi')),
    ('rule 5  space before ; : ! ?',                n(r'\S [;:!?](?:\s|$)')),
    ('rule 6  uppercase LED outside code',          n(r'\bLED')),
    ('rule 7  wrong article "het HALPI2"',          n(r'\bhet HALPI2\b')),
    ("rule 7  English possessive HALPI2's",         n(r"HALPI2['’]s")),
    ('units   unspaced unit (12V, 0,9A, 120Ω)',     n(r'\d(?:V|A|W|Ω|°C|mm|kg)\b')),
    ('units   decimal point instead of comma',      n(r'(?<!v)\d\.\d')),
]
for label, count in report:
    print(f'{count:>4}  {label}')
print('\nevery count must be 0; inspect each hit, do not adjust the pattern')
PY
```

Two of these need judgement rather than a blind zero: version numbers such as
`v0.6.1` are identifiers and legitimately contain points, and a heading may
legitimately start with a capitalised common noun. Read the hits. Everything
else is a defect.

Also confirm, as the skill requires, that every number in the English page
appears in the Dutch page. A wrong voltage in an installation guide is a safety
problem, not a typo.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
  `swedish-glossary.md` — the siblings
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

## Terms added during translation

Reported by the page translators, consolidated here rather than written
by each of them, because five agents share this file.

| English | Translation | Note |
|:--------|:------------|:-----|
| desktop setup | opstelling op het bureau | Heading and repeated body term for the pre-installation bench test. Avoided *desktopopstelling*, which collides with the graphical desktop meaning tha |
| graphical desktop / desktop interface | grafische werkomgeving | The Raspberry Pi OS GUI. Kept distinct from *opstelling op het bureau* so the two English senses of "desktop" do not merge in Dutch. |
| splash screen | opstartscherm | Raspberry Pi OS boot logo screen; no glossary entry. |
| cable management | kabelbeheer | Glossary has *kabelroute* for cable routing, but this is the wider planning/tidiness sense used in the mounting-orientation list. |
| cable grommet | doorvoertule | Appears alongside *cable gland* (kabelwartel), so it needs its own word rather than being folded into the gland. |
| mounting hardware | bevestigingsmateriaal | Corrosion-resistant screws/brackets in the marine list. |
| mounting screws | montageschroeven | Used in three mounting steps and the materials list. |
| transportation damage | transportschade | Appears twice in troubleshooting (unseated CM5, undetected NVMe SSD). |
| ambient (temperature) | omgevingstemperatuur | Renders "-20°C to +60°C ambient" as a single Dutch noun rather than a loose adjective. |
| cable tester | kabeltester | Ethernet troubleshooting step. |
| circuit / dedicated circuit | groep | Dutch electrical-panel usage for a breaker circuit; *circuit* alone would read as an electronic circuit. Glossary already fixes *installatieautomaat*  |
| wire (conductor in a multi-core cable) | ader | "Red wire / black wire" are cores inside one cable, so *ader*, not *draad* or *kabel*. Glossary covers *aderdoorsnede* but not the bare noun. |
| positive / negative terminal | plusklem / minklem | Extends the glossary's plus (+) / min (−) to the terminal at the power source. |
| community forums | communityforums | Hat Labs support channel; *community* is established in Dutch, solid compound per rule 4. |
| rainbow pattern (LED) | regenboogpatroon | Names the LED fault pattern for an unseated CM5. |
| boot mode switch | bootmodusschakelaar | The switch next to the USB Boot connector on software.md. Solid compound per rule 4; "modus" is the established Dutch noun and "boot" stays as the unt |
| amber LED | amberkleurige led | The indicator next to the boot mode switch. Glossary fixes `led` lowercase but not the colour word; "amberkleurig" keeps the distinction from the red/ |
| mass storage device | massaopslagapparaat | What the HALPI2 appears as after `rpiboot` runs. Standard Dutch computing term, solid compound. |
| command line tool | opdrachtregelgereedschap | Used throughout the `halpi` section and in the H2 heading. "opdrachtregel" is the Dutch term for command line; "gereedschap" rather than "tool" keeps  |
| block device | blockdevice | Adopted English two-word term becomes one Dutch word (rule 4), same treatment as carrierboard/accesspoint. "blokapparaat" is not trade usage. |
| device node | apparaatknooppunt | The `/dev/ttyAMA*` entry in the Verifying section of interfaces.md. |
| hardware flow control | hardwarematige flowcontrol | The `ctsrts` parameter in interfaces.md. "flowcontrol" is the trade term; "stromingsregeling" would read as fluid dynamics. |
| chip select | chipselect | The CAN FD conflict row in the CTS/RTS table. One word, adopted whole. |
| Unix domain socket | Unix-domainsocket | The REST API transport. Proper name Unix takes exactly one hyphen at the junction (rule 4); the rest is one adopted word. |
| setup wizard | installatiewizard | The Raspberry Pi OS first-boot flow. "wizard" is established in Dutch software UI language. |
| update manager | updatebeheer | The graphical updates section. Matches the glossary's "beheer" pattern (systeembeheer, energiebeheer, containerbeheer). |
| port forwarding | port forwarding | Kept in English in the VNC section. Dutch network documentation uses the English term; "poortdoorschakeling" exists but is not what a reader will find |
| login console | inlogconsole | The dedicated debug UART `/dev/ttyAMA10` in interfaces.md. |
| silk screen (board legend) | opdruk | Appears three times on hardware.md (the Contacts arrows, the CM5 module outline). The glossary fixes quoted silkscreen *labels* but has no word for th |
| computer mainboard | hoofdprint van de computer | The Internal Layout bullet calls the carrier board "the computer mainboard". The glossary forbids *moederbord* but offers no alternative; *hoofdprint* |
| device tree overlay | device tree overlay | Kept in English in three places. It names a Raspberry Pi OS mechanism and the reader will meet it verbatim in `config.txt` and in HAT documentation; a |
| board-to-board connector | board-to-boardconnector | The CM5 mounting connectors, named seven times. Adopted English term becomes one Dutch word per rule 4, with the internal hyphens of the English term  |
| expansion board | uitbreidingsprint | Third-party HAT-compatible boards in the compatibility section. Distinct from *carrierboard*, so it needs its own word. |
| spudger | spudger | The non-conductive prying tool for the CM5. No Dutch equivalent in trade usage; the reader searching for one will search for *spudger*. |
| guitar pick | plectrum | Listed alongside the spudger as an alternative tool. *Plectrum* is the ordinary Dutch word. |
| to pry / to rock (a connector loose) | wrikken | Used for both the CM5 removal and the HAT removal ("gentle rocking motion"). One verb covers both senses in Dutch and keeps the two procedures reading |
| Label (table column heading) | Aanduiding | Column head of the three connector tables and the LED table. *Label* exists in Dutch but reads as a sticker; *Aanduiding* matches how the German page  |
| socket (hex tool) | dop / dopsleutel | The 26 mm / 10 mm / 8 mm / 17 mm sockets in the connector-removal step. Needed to be kept apart from *aansluiting*, which the glossary already uses fo |
| surface-mounted component | SMD-component | The components near the CM5 connectors that metal tools can damage. SMD is the established Dutch trade abbreviation. |
| countersunk screw | verzonken schroef | The four M4×10 lid screws. Matches the existing Dutch technical-reference page, which already writes "4× M4×10 verzonken, PH2-kop". |
| heat spreading area | warmteafvoervlak | The areas in the enclosure bottom that the CM5 thermal pads meet during final assembly. |
| Blinkenlights | Blinkenlights | Heading left untranslated, matching what the German, Swedish and French pages already do — it is a joke term, not a description. |
| Load Equivalency Number (LEN) | belastingsgetal (LEN) | NMEA 2000 network loading in interfaces.md. Parallel to the siblings (Lastkennzahl / indice de charge / belastningstal); the abbreviation LEN is kept  |
| voltage bar (LED pattern) | spanningsbalk | Names the LED bar acting as a charge-level gauge in the operation.md status table. Glossary has ledbalk for the physical LED bar; this is the pattern  |
| power button | aan/uit-knop | The CM5 power button and the front-panel button on both pages, including "simulated power button presses" (gesimuleerde drukken op de aan/uit-knop). E |
| transmit enable (signal/mode) | zendvrijgave / zendvrijgavesignaal | RS-485 manual vs automatic transmit enable in interfaces.md. Solid compound per rule 4; "zendinschakeling" would read as switching the transmitter on  |
| watchdog timeout | watchdog-time-out | LED table row and the 30-second communication timeout in operation.md. The glossary keeps "watchdog"; "time-out" is the Dutch spelling and already car |
| grace period | wachttijd | The 5-second window before automatic restart in operation.md. "Respijtperiode" is legal register and wrong here. |
| normally-open (NO) momentary switch | drukknop met maakcontact (normally open, NO) | External button wiring in interfaces.md. Dutch electrical trade says maakcontact; the English abbreviation is kept because it is what the switch packa |
| Battery-Backed RAM (BBR) | batterijgebufferd RAM (BBR) | u-blox GNSS settings storage in interfaces.md. Abbreviation kept for the u-blox documentation the reader will consult. |
| half-duplex mode | halfduplexmodus | RS-485 single-pair operation. Solid compound, no hyphen. |
| multi-talker / single-talker network | multi-talkernetwerk / single-talkertoepassing | NMEA 0183 topology terms in interfaces.md; kept in English as trade usage, joined solid to the Dutch noun per rule 4. "single-talker-multiple-listener |
| baud rate / update rate | baudrate / updatesnelheid | u-blox configuration table. "baudrate" already appears in docs/nl/user-guide/troubleshooting.md, so this only records it; "updatesnelheid" is new. |
| progressive fill / solid / dim red (LED states) | oplopende vulling / continu / gedempt rood | The LED quick-reference table in operation.md has no glossary coverage for the pattern vocabulary. "continu" matches "Continu geel" already used in tr |
| wake-up event | wekgebeurtenis | Standby mode admonition in operation.md. |
| Data Browser (Signal K) | Data Browser | Left in English: it is a UI string the reader sees in the Signal K interface on their own screen. |
| bps / kbps / Mbps (bit rate) | bit/s / kbit/s / Mbit/s | Extends the units-table row `250 kbps → 250 kbit/s` to bare and serial-port rates: `38400 bit/s`, `115200 bit/s`, `10 Mbit/s`. The "no thousands separator" bullet writes `115200 bps` only to illustrate the separator, not to license `bps`. |
| Bluetooth | Bluetooth | Capitalised, unlike `wifi`. Dutch trade writing keeps the trademark capital while `wifi` has genericised to lowercase. In compounds it is a proper name and takes exactly one hyphen at the junction (rule 4): `Bluetooth-antenne`, `Bluetooth-verbindingen` — never `bluetoothantenne`. |
| tool / utility | gereedschap | One word for both English nouns: `het gereedschap rpiboot`, `het gebruikelijke Linux CAN-gereedschap`, `het gereedschap Data Browser`. Never *hulpmiddel*, which reads as an aid rather than a program. Matches `opdrachtregelgereedschap`. |
| command | opdracht | `de opdracht shutdown`, `de volgende opdrachten`. Never *commando*, which in Dutch reads as a military order or a commando soldier. Matches `opdrachtregel`. |
| section (of this documentation) | onderdeel | Cross-references between pages: `in het onderdeel Toegang tot de behuizing`. Not *gedeelte* and not *sectie* — *sectie* is reserved for a section of a configuration file, e.g. the `[all]` section of `config.txt`. |
| Ethernet port | ethernetaansluiting | The RJ45 socket on the carrier board and on the panel. It is a board-mounted socket, so the glossary's *aansluiting* branch applies; not *ethernetpoort*. Other ports stay *poort* (`USB-poort`, `HDMI-poort`, `seriële poort`). |
| USB Boot connector | USB-bootconnector | Solid compound per rule 4, matching `USB-bootmodus` and `bootmodusschakelaar`. The silkscreen label itself stays verbatim and quoted: `de USB-C-connector met het opschrift “USB Boot”`. |
| onboard (device, peripheral) | ingebouwd | What sits on the carrier board itself, as opposed to something the user attaches. Already the rendering of *built-in* on four pages (`ingebouwde interfaces`, `ingebouwde USB 3-hub`), so the two English words share one Dutch adjective. |
| dedicated (pins, bus, UART) | speciaal | `speciale CM5-pinnen`, matching `een aparte, speciale debug-UART` in interfaces.md. Not *eigen*, which reads as ownership rather than reserved-for-one-purpose. |
| resistor | weerstand | The bare noun; the glossary covers only the compound *afsluitweerstand*. Values follow the existing page pattern `afsluitweerstand van 120 Ω` → `weerstanden van 0 Ω`, never a `0 Ω-weerstand` compound. |
| charge-level bar (LED pattern) | laadniveaubalk | The controller.md LED table; the bar height shows super-capacitor charge. Successor of *spanningsbalk*, which named the same pattern when the English source still called it a voltage bar. |
| unattended operation | gebruik zonder toezicht | operation.md intro and faq.md; *onbeheerd* reads as abandoned rather than unattended. |
| load dump | load dump | The alternator transient in power-supply.md. Dutch automotive trade keeps the English term. |
| state machine | toestandsmachine | power-supply.md cross-reference to controller.md. |
| power-on threshold | inschakeldrempel | The 8,0 V super-capacitor level (`power_on_threshold`) in power-supply.md; controller.md spells the parameter description out instead. |
| fallback (mode, value) | terugvalmodus / terugvalwaarde | Solo mode as fallback mode; the firmware fallback for `auto_restart` in controller.md. Matches *valt terug op*, already used for the daemon-less case. |
| input stage | ingangstrap | power-supply.md heading; standard Dutch electronics term. |
| rainbow sweep | lopende regenboog | The SystemStartup LED animation in controller.md. |
| solid color (LED) | effen kleur | The startup color cycle in controller.md; distinct from *continu*, which the LED tables use for steady-versus-blinking. |
| residual charge | restlading | The PowerOff state in controller.md: the controller runs on what is left in the super-capacitors. |

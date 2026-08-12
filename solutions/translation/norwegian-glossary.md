---
title: Norwegian Bokmål translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Norwegian Bokmål under docs/nb/
  - Reviewing a Norwegian Bokmål translation for consistency
  - Adding a new term that has no established Norwegian Bokmål equivalent
tags:
  - translation
  - i18n
  - norwegian
  - bokmal
  - terminology
  - mkdocs-static-i18n
---

# Norwegian Bokmål translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Norwegian Bokmål under `docs/nb/`, using the `mkdocs-static-i18n` folder
structure. Each language directory mirrors the same tree, so a translation keeps
its source's path and filename. Only markdown lives under `docs/nb/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
`swedish-glossary.md` and `danish-glossary.md` are the siblings of this file.
The general approach is the same in all of them.

## Six rules where the siblings are wrong for Norwegian Bokmål

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary. Danish is the dangerous
neighbour: it is close enough to read as correct and is being written against
the same English source, so a Danish habit that slips in will not look wrong to
anyone who is not counting.

1. **Quotation marks are `«…»`, pointing inward.** Norwegian opens with `«` and
   closes with `»`. **Danish is the exact opposite** — Danish opens with `»` and
   closes with `«`. Not Swedish's `”…”`, not German's `„…“`, not straight
   `"…"`. And unlike French, **no space inside the guillemets**: write
   `«Abnormal»`, never `« Abnormal »`.

2. **Address the reader as `du`.** Norwegian technical and consumer
   documentation uses `du`. French uses *vouvoiement* and German uses *Sie* —
   both wrong here. `Koble til strømkabelen.` / `Kontroller polariteten med
   multimeteret før du slår på spenningen.` The formal `De`/`Dem`/`Deres` must
   not appear at all.

3. **No space before `; : ! ?`** — as in German and Swedish, and unlike French,
   whose rule is the exact opposite and demands a no-break space.

4. **Compounds are written solid, as one word.** `strømforsyning`,
   `kabelgjennomføring`, `bærekort`, `spenningsfall`, `nedstenging`. Splitting a
   compound in two (*særskriving*, `strøm forsyning`) is the single most visible
   error in written Norwegian and is what English word order invites. English
   `power supply` is two words; Norwegian is one.

5. **Compounding with a proper name takes one hyphen at the junction, not
   throughout.** Norwegian writes `NMEA 2000-nettverk`, `Signal K-server`,
   `Raspberry Pi-antenne`, `HALPI2-kabinett`. German writes
   `NMEA-2000-Netzwerk` — hyphens all the way through. Copying the German
   pattern is wrong, and copying English spacing (`NMEA 2000 nettverk`) is also
   wrong.

6. **Norwegian spelling, not Danish.** The pairs below are the ones this corpus
   actually produces. Left is Norwegian and required; right is Danish and must
   not appear.

   | Norwegian Bokmål | Danish — never write this |
   |:-----------------|:--------------------------|
   | konfigurasjon, installasjon, informasjon, funksjon, terminering | konfiguration, installation, information, funktion |
   | å koble til (infinitive marker `å`) | at tilslutte (infinitive marker `at`) |
   | bare | kun |
   | nå | nu |
   | noen | nogen |
   | mye | meget |
   | enn | end |
   | etter | efter |
   | sette, hjelp, endre | sætte, hjælp, ændre |
   | sjekk | tjek |
   | forbindelsene, kablene (definite plural `-ene`) | forbindelserne, kablerne (`-erne`) |
   | bærekort | bæreprint |

   `kun` is not ungrammatical in Bokmål, but it is the Danish default. Banning
   it here costs nothing and makes a leak from the Danish branch visible in one
   `grep`.

## Names that are never translated

Product names, protocol names, hardware standards and software UI strings stay
in English — the device's own interface is in English, so translating a menu
name would send the reader looking for something that does not exist on screen.

HALPI2, HaLOS, Signal K, OpenPlotter, Raspberry Pi, Raspberry Pi OS, Compute
Module 5 (CM5), Cockpit, Homarr, Authelia, Grafana, InfluxDB, AvNav, OpenCPN,
Hat Labs, NMEA 2000, NMEA 0183, CAN FD, SocketCAN, RS-485, RS-422, Modbus RTU,
NVMe SSD, M.2, GPIO, I2C, SPI, UART, HDMI, MIPI, CSI/DSI, USB, RP-SMA, U.FL,
E7T, PG7, SP13, IP65, DHCP, SSH, SSL, SSO, ABYC, Cat5e, AWG, HAT, RP2040.

**Commands, file paths, configuration keys and code stay in English**, verbatim:
`halpi status`, `systemctl status halpid`, `candump can0`, `/dev/ttyAMA4`,
`/boot/firmware/config.txt`, `auto_restart`, `dtoverlay`, `can0`,
`halos.local`, `halpi2-firmware`. Code fences, command output, URLs and image
filenames are never touched.

## Units and numbers

Same handling as the other languages — the English source writes `12V` and
`0.9A`, and both are wrong in Norwegian.

| English source | Norwegian Bokmål |
|:---------------|:-----------------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |
| `200×130×60 mm` | `200 × 130 × 60 mm` |
| `2m`, `45mm`, `2kg` | `2 m`, `45 mm`, `2 kg` |

**Do not insert a thousands separator.** `115200 bps` and `9600` stay exactly as
in the source. Norwegian typography would allow a no-break space, but the
verification step compares every number in the English text against the
translation, and `115 200` no longer matches `115200`. Digits are copied, not
reformatted — only the decimal separator and the unit spacing change.

Decimal comma everywhere in prose, decimal point never — except inside inline
code and version numbers, which are copied verbatim (`v0.5.0`, `M4x10`, `PH2`).

## Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry an `en/`, `nb/` or other language segment; image
captions and alt texts are translated but filenames are not; screenshots stay
English because the reader's own screen is English; standard admonition titles
are translated centrally in `mkdocs.yml`, custom ones in the page.

Admonition titles used centrally: `note` → Merk, `warning` → Advarsel, `tip` →
Tips, `info` → Informasjon, `danger` → Fare, `example` → Eksempel.

## Glossary

### Enclosure, mounting, and installation

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| carrier board | bærekort | The accurate term, as in Swedish, French and German — see the note below |
| enclosure | kabinett | Not *hus*; *kabinett* is what an electronics box is called |
| lid | lokk | |
| gasket | pakning | |
| heat sink | kjøleribbe | |
| waterproof | vanntett | |
| wall-mount | veggmontering | |
| mounting surface | monteringsflate | |
| pilot hole (to drill) | forbore (verb) | `Forbor hullene for monteringsskruene` — an action the reader performs |
| pre-drilled hole (already there) | ferdigboret hull | The holes the enclosure ships with. Never write `forbor de ferdigborede hullene` — that is the nonsense the Swedish branch shipped |
| mounting template | boremal | |
| bilge water | lensevann | As in *lensepumpe*; not *bunnvann* |
| bulkhead | skott | |
| cable gland | kabelgjennomføring | The PG7 parts specifically may be called `kabelnippel` when the physical part is meant |
| cable routing | kabelføring | |
| service loop | servicesløyfe | Slack left at both cable ends |
| cable tie | kabelstrips | |
| blind plug | blindplugg | |
| breather plug | trykkutjevningsplugg | |
| standoff | avstandsbolt | |
| threaded insert | gjengeinnsats | |
| thermal pad | varmeledende pute | |
| spudger | plastspade | Non-conductive prying tool |

**A note on `bærekort`.** Norwegian takes the accurate term, like Swedish
(`bärkort`), French (`carte porteuse`) and German (`Trägerplatine`), and unlike
Finnish (`emolevy`, literally *motherboard*, chosen there for reader
familiarity). The divergence between the languages is deliberate, decided per
language and per audience. Do not harmonise them.

`bærekort` carries the CM5/board relationship on its own, so passages about
reseating the CM5 or troubleshooting a board that will not boot need no extra
explanation. Only the Finnish glossary needs that warning.

Danish would form this as `bæreprint` (Danish uses *print* for a circuit board).
Norwegian does not: the Norwegian word for a circuit board is `kretskort`, so
the compound is `bærekort`.

### Power and electrical

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| power supply | strømforsyning | The external unit itself: *strømadapter* |
| input voltage range | inngangsspenningsområde | |
| polarity | polaritet | |
| fuse | sikring | |
| inline fuse | linjesikring | |
| circuit breaker | automatsikring | The panel breaker on the boat's electrical panel |
| current limiting | strømbegrensning | `strømbegrensningsbryter` for the switch |
| overcurrent | overstrøm | |
| voltage drop | spenningsfall | |
| grounding | jording | |
| short circuit | kortslutning | |
| wire gauge | ledertverrsnitt | Norwegian uses mm², not AWG |
| marine-grade wire | kabel av marin kvalitet | |
| wire strippers | avisoleringstang | |
| crimping | krimping | See the note below — *not* `krymping` |
| crimper | krimptang | |
| heat-shrink tubing | krympestrømpe | |
| heat gun | varmepistol | |
| multimeter | multimeter | |
| terminal block | koblingsklemme | In this documentation always the pluggable screw terminal on the carrier board, not a DIN-rail *rekkeklemme* |
| strain relief | strekkavlastning | |
| super-capacitor | superkondensator | |
| real-time clock | sanntidsklokke | |
| backup battery | reservebatteri | The CR2032 for the RTC |
| backup power | reservestrøm | What the super-capacitors deliver |
| voltage rail | spenningsskinne | `3,3 V-skinnen`, `5 V-skinnen` |

**A note on `krimping` versus `krymping`.** Norwegian trade usage says both, and
that is exactly the problem: `krympe` also means *to shrink*, and this
documentation talks about heat-shrink tubing (`krympestrømpe`) two lines from
where it talks about crimping terminals. `krimping`/`krimptang` for the crimp
and `krymping`/`krympestrømpe` for the heat-shrink keeps the two apart on the
page. Do not "correct" one into the other.

### Connectors and interfaces

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| connector | kontakt / tilkobling | *kontakt* for the physical part, *tilkobling* for the act of connecting |
| barrel connector | DC-plugg | First mention: `DC-plugg (barrel)` |
| header | pinneliste | `40-pinners GPIO-pinneliste` |
| pin | pinne | |
| pitch | senteravstand | `3,81 mm senteravstand` |
| backbone | backbone | Established in Norwegian NMEA 2000 usage |
| drop cable | stikkledning | Dealer catalogues also say *dropkabel*; this documentation uses *stikkledning* throughout |
| T-connector | T-kobling | The source also writes *T-adapter*; translate both as `T-kobling` |
| terminator (the component) | termineringsmotstand | The 120 Ω resistor and its jumper |
| termination (the state) | terminering | `Kontroller at nettverket er riktig terminert` |
| front panel | frontpanel | |
| jumper | jumper | The physical shunt; `loddebro` for a solder jumper |
| male / female | hann / hun | `hannkontakt`, `hunkontakt` |
| flexible flat cable (FFC) | flatkabel | Keep `(FFC)` on first mention |
| silk screen | silketrykk | |

### Operation and system behaviour

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| boat computer | båtdatamaskin | |
| to boot | starte opp | |
| first boot | første oppstart | |
| shutdown | nedstenging | |
| graceful shutdown | kontrollert nedstenging | |
| to shut down | slå av / stenge ned | |
| power loss | strømbortfall | The event: input power disappears |
| blackout | strømbrudd | The interval the blackout timer measures: `strømbruddstimer` |
| power management | strømstyring | |
| status LED | status-LED | |
| monitoring | overvåking | Not the Swedish *övervakning* |
| passive cooling | passiv kjøling | |
| filesystem | filsystem | |
| to unmount (a filesystem) | avmontere | `filsystemene avmonteres trygt` |
| to unmount (hardware, remove a module) | demontere | Removing the CM5 or the carrier board is *demontering*, never *avmontering* |
| watchdog | watchdog | `watchdog-tidsavbrudd` |
| standby | ventemodus | The CM5 is off while the controller stays awake — not *hvilemodus*, which is sleep |
| power button | strømknapp | |
| reset button | resetknapp | |
| solo mode / co-op mode | solomodus / samspillsmodus | Keep the English in parentheses on first mention |

### Software and networking

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| firmware | firmware | Not *fastvare* — matches the sibling decision to keep the trade term, and the package is named `halpi2-firmware` |
| daemon | daemon | `HALPI-daemonen`; not *tjeneste*, which is a systemd service |
| to flash | flashe | `flashe systembildet til SSD-en` |
| system image | systembilde | Also for *operating system image* |
| container image | containerbilde | |
| container app | containerapp | |
| headless | uten skjerm | First mention: `uten skjerm (headless)` |
| dashboard | dashbord | Homarr's dashboard view. The UI itself says *Dashboard* in English — keep that when naming the on-screen label |
| WiFi Access Point | WiFi-aksesspunkt | |
| wired / wireless | kablet / trådløs | |
| credentials | påloggingsinformasjon | |
| default password | standardpassord | |
| single sign-on (SSO) | enkel pålogging (SSO) | |
| Certificate Authority (CA) | sertifikatutsteder (CA) | |
| web interface | webgrensesnitt | |
| browser | nettleser | |
| to log in | logge på | |
| update | oppdatering | |
| device tree overlay | device tree-overlay | Keep the English term; it names a file the reader edits |

### Applications and use cases

| English | Norwegian Bokmål | Note |
|:--------|:-----------------|:-----|
| chart plotter | kartplotter | |
| data logging | datalogging | |
| vessel | fartøy | |
| fleet management | flåtestyring | |
| predictive maintenance | prediktivt vedlikehold | |
| remote monitoring | fjernovervåking | |
| compliance | samsvar | As in *samsvarserklæring* |
| warranty | garanti | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. `uv run python scripts/check_glossary.py nb` passes.
5. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
6. Every term used on the page that appears in this glossary matches it.

`scripts/check_glossary.py` needs `"nb": "norwegian-glossary.md"` in its
`GLOSSARIES` dict before step 4 can run. Whoever translates the first page adds
that line in the same change.

### The six rules are measured, not reread

**A rule that was read looks followed.** Rereading your own page confirms
whatever it already says. Both the French and German branches shipped a
half-applied typography rule to review for exactly this reason, and Danish is
close enough to Norwegian that a leak from the parallel branch will read as
fine. Run these against `docs/nb/` and act on any non-zero count. Strip code
fences first — every count below is about prose, and inline code is exempt.

| Rule | Command | Expected |
|:-----|:--------|:---------|
| Guillemets pair and point inward | `grep -o '«' -r docs/nb \| wc -l` and the same for `»` | equal counts |
| No Danish outward quotes | `grep -rnE '»[^«»]*«' docs/nb` | no output |
| No space inside guillemets | `grep -rnE '« \| »' docs/nb` | no output |
| Reader is `du` | `grep -rowiE '\b(du\|deg\|din\|ditt\|dine)\b' docs/nb \| wc -l` | well above zero |
| No formal address | `grep -rnE '\b(De\|Dem\|Deres)\b' docs/nb` | no output outside sentence-initial `De` |
| No space before `;:!?` | `grep -rnE ' [;:!?]' docs/nb` | no output |
| No `-tion` (Danish/English) | `grep -rniE '[a-zæøå]{3,}tion(en\|er\|ene\|s)?\b' docs/nb` | no output |
| Infinitive marker is `å` | `grep -rnE '\bat [a-zæøå]+e\b' docs/nb` | no output |
| No Danish function words | `grep -rniwE '(kun\|nu\|nogen\|meget\|end\|efter\|sætte\|hjælp\|ændre\|tjek)' docs/nb` | no output |
| No `-erne` plurals | `grep -rniE '[a-zæøå]{3,}erne\b' docs/nb` | no output |
| No split compounds | `grep -rniE '(strøm forsyning\|kabel gjennomføring\|bære kort\|super kondensator\|status LED-\|spennings fall)' docs/nb` | no output |
| German hyphen chain | `grep -rn 'NMEA-2000\|Signal-K\|Raspberry-Pi' docs/nb` | no output |
| Junction hyphen present | `grep -rn 'NMEA 2000-\|Signal K-' docs/nb` | matches wherever the name is compounded |
| Unit spacing | `grep -rnE '[0-9](V\|A\|W\|Ω\|mm\|kg\|m)\b' docs/nb` | no output |
| Decimal comma | `grep -rnE '[0-9]\.[0-9]' docs/nb` | no output outside version numbers |
| En dash in ranges | `grep -rnE '[0-9]-[0-9] ?(V\|A)' docs/nb` | no output |
| Numbers did not drift | every number in the English page appears in the Norwegian page | all present |

A wrong voltage or current in an installation guide is a safety problem, not a
typo. The last row is not optional.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
  `swedish-glossary.md`, `danish-glossary.md` — siblings
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

## Terms added during translation

Reported by the page translators, consolidated here rather than written
by each of them, because five agents share this file.

| English | Translation | Note |
|:--------|:------------|:-----|
| guitar pick | gitarplekter | Named as an alternative non-conductive prying tool next to the spudger in the CM5 removal procedure. The glossary lists spudger -> plastspade but not  |
| board-to-board connector | kort-til-kort-kontakt | The two high-density connectors joining the CM5 to the carrier board. Central to the CM5 replacement section and its warranty warning, so it needs one |
| amber (LED colour) | ravgul | LED colour column in the status-LED table. Norwegian trade usage also says gul, which would collide with the yellow Ethernet-speed LED two rows above; |
| voltage bar (LED pattern) | spenningssøyle | The LED pattern name in the operation.md quick-reference table, where the five LEDs form a bar-graph charge indicator. |
| hex socket / socket size (tool) | pipe / pipestørrelse | The connector-removal step lists 26 mm, 10 mm, 8 mm and 17 mm sockets. pipe (pipenøkkel) is the Norwegian tool word; nøkkel alone would read as a span |
| countersunk screw | senkeskrue | The four M4x10 lid screws. Appears in the very first procedure on the page. |
| boot mode | oppstartsmodus | USB boot mode / Abnormal boot mode, in the connector table, the LED table and the SSD section. The glossary has to boot -> starte opp but not this com |
| single-sided / double-sided (SSD) | ensidig / tosidig | The M.2 2230-2280 compatibility rule turns on this distinction, so it is load-bearing rather than decorative. |
| chip select | chip select | Kept in English in the GPIO conflict table and prose, like the other SPI signal names (MISO, MOSI, SCK) which are already never-translate. |
| transceiver | transceiver | RS-485 transceiver, in the interface-disabling section. The Norwegian trade term is the English one, consistent with the glossary keeping firmware and |
| grace period | venteperiode | The 5-second window before HALPI2 restarts itself after a manual shutdown. naadeperiode is a legal term and wrong here. |
| feeding the watchdog | mating av watchdogen | The source sets it in quotes as jargon; kept as jargon inside Norwegian guillemets so it still reads as a quoted idiom. |
| heat spreading area | varmespredende flate | The areas on the enclosure bottom the CM5 thermal pads must meet, in the CM5 final-assembly step. |
| solid (LED state) | lyser fast | Opposed to blinker (flashing) throughout the operation.md LED table; needed one fixed rendering to keep the table columns parallel. |
| pressure equalization | trykkutjevning | The stated purpose of the breather plug. The glossary gives the part (trykkutjevningsplugg) but not the function, which the panel-connector list state |
| terminals (crimp-on cable terminals) | kabelsko | Appears twice in the permanent-installation materials list and in "Install terminals using proper crimping technique". The glossary covers terminal bl |
| cable grommet | gummigjennomføring | "Install cable glands or cable grommets if routing through bulkheads" lists it alongside cable gland (kabelgjennomføring). Needed a distinct word so t |
| "wall wart" (power supply type) | «wall wart» (kept English in guillemets) | Jargon in the optional-items list. No idiomatic Norwegian equivalent; kept as a quoted English idiom inside «…», the same treatment the glossary gives |
| mounting clips | monteringsklips | Last item of the materials list, next to cable ties (kabelstrips). Recording it so the next page that mentions clips does not invent klemmer or festek |
| known-good device | en enhet du vet fungerer | NMEA 2000 troubleshooting bullet. Rendered as a relative clause rather than a compound; noting it so the phrase stays the same if it recurs. |
| Load Equivalency Number (LEN) | Load Equivalency Number (LEN) | NMEA 2000 standard term for how much bus power a device draws. Norwegian marine dealers and the standard itself use the English name and the LEN abbre |
| multi-talker / single-talker-multiple-listener | multi-talker / single-talker-multiple-listener | NMEA 0183 / RS-485 topology terms. Kept English but glossed once on first use: 'nettverk med flere sendere (multi-talker)' and 'nettverk med én sender |
| half-duplex | halv dupleks | The RS-485 mode that lets one wire pair both transmit and receive. Two words in Norwegian (halv dupleks) rather than a solid compound, matching establ |
| normally-open (NO) momentary switch | normalt åpen (NO) momentbryter | The switch type required for the external Power/Reset/User buttons. Load-bearing: the wrong switch type makes the button behave inverted. 'momentbryte |
| Battery-Backed RAM (BBR) | batteribackup-RAM (BBR) | Where the u-blox GNSS receiver stores its settings. Explains why the configuration is re-run on every boot, so it needs a stable rendering. Abbreviati |
| PLC (programmable logic controller) | PLS | Industrial RS-485 device listed under common applications. PLS is the standard Norwegian abbreviation (programmerbar logisk styring); writing PLC woul |
| buck converter | buck-omformer | Names the SiC463ED regulating the 10 V intermediate rail in the power-supply table. Norwegian trade usage keeps 'buck' and compounds it with a junctio |
| ferrite bead | ferrittperle | USB 3.0 port filtering in technical-reference/hardware.md. Standard Norwegian component name. |
| pull-up (resistor) | pull-up-motstand | The 2,2 kΩ pull-ups on the controller I2C bus. Norwegian keeps the English 'pull-up' and compounds it, as with the glossary's device tree-overlay. |
| ingress protection | inntrengningsbeskyttelse | The IP65 row in the specifications summary. The separate 'IP rating' row in the enclosure table is rendered 'IP-klasse' — the two English phrasings ar |
| solder nut | loddemutter | The 4× M2.5 fasteners holding the CM5, in the mounting list. Distinct from the glossary's gjengeinnsats (threaded insert), which is the HAT mounting m |
| current limit (the value) | strømgrense | Column header in the USB 3.0 port table, where each cell is a number (0,93 A). The glossary has current limiting -> strømbegrensning for the function  |
| depth sounder / wind instrument | ekkolodd / vindmåler | NMEA 0183 instrument types listed under common applications for RS-485. Both are the ordinary Norwegian boating words. |
| recessive state | resessiv tilstand | The bus state an RS-485 multi-talker interface must hold when not transmitting. Direct loan, as in the CAN literature. |
| power-on / power-off threshold | innkoblingsterskel / utkoblingsterskel | The 8,0 V and 5,5 V supercapacitor thresholds. Chosen as a matched pair so the two table rows read parallel; UVLO is kept as the English abbreviation  |
| user space | brukerrommet (user space) | ubuntu-installation.md describes halpid as a user space daemon that talks to the power-management hardware over I2C. The glossary fixes daemon -> daem |
| thermal throttling | termisk struping | troubleshooting.md, the 'System runs slowly or freezes' step about CPU temperature above 80 °C. The glossary covers passiv kjøling but not the throttl |
| rollback (of a firmware update) | tilbakerulling / rulle tilbake | The whole 'Firmware Update Failed or Rolled Back' section turns on this word, and the LED/firmware sections of software.md already describe the same 3 |
| login prompt | påloggingsledetekst | troubleshooting.md tells the reader to attach HDMI and look for boot errors or a login prompt. The glossary has to log in -> logge på but not the on-s |
| bus contention | konflikt på bussen | The CAN error-counter step in troubleshooting.md lists it alongside wiring problems and wrong baud rate. No single-word Norwegian equivalent is in use |
| 3rd party (operating systems) | tredjeparter | The warning admonition at the top of ubuntu-installation.md. Spelled out as a word rather than kept as a digit, so the numeric-drift check will report |
| errata / known hardware issues | kjente feil | Page title of appendices/errata.md. Taken from the nb nav_translations block in mkdocs.yml ("Errata": "Kjente feil") so the H1 and the sidebar agree,  |
| mounting ledge | monteringsknast | The cast aluminium ledges inside the enclosure that the PCB rests on. Central to the second errata item (heading plus three prose mentions); knast is  |
| flash (casting residue) | støpegrad | The sharp leftover aluminium from the casting process, set in quotes in the English source. Written as stopegrad (with o-slash) and kept inside Norweg |
| solder mask | loddemaske | The PCB coating a casting flash can penetrate, in the errata short-circuit description. |
| copper pour / power plane | kobberflate / spenningsplan | Both appear: copper pours in the v0.5.0 changelog and a 3,3 V power plane in errata. Kept apart because the errata text names the plane as a net, not  |
| inrush current / initial current spike | startstrom | The errata compliance item turns on this quantity (1,1 A against the NMEA 2000 limit of 1 A), so it needed one fixed rendering rather than an ad-hoc p |
| through-hole (THT) | gjennomhullsmontering (THT) | The v0.5.0 jumper-header changelog entry. Abbreviation kept in parentheses as the source has it. |
| footprint (component) | komponentfotavtrykk | Last v0.6.0 changelog entry. Fotavtrykk alone would read as a carbon/disk footprint in a marine document. |
| signal integrity | signalintegritet | Appears twice in design-files (v0.6.1 summary and the v0.6.0 re-routing entry). |
| security hardening | sikkerhetsherding | Bullet in software-development/advanced-config.md. Sikring would collide with the glossary entry fuse -> sikring, which is the reason for choosing her |
| cross-compilation | krysskompilering | Bullet in software-development/integration.md. |
| kernel module | kjernemodul | Bullet in software-development/integration.md; kernel is otherwise never translated in the glossary, but the compound reads badly in English here. |
| goodie bag | tilbehørspose | The bag of extras shipped in the box. Appears only as the index.md image alt text, so nothing else in the corpus pins it down; recorded here so the next page that mentions it does not invent godtepose or tilbehørspakke. |
| to serve (a bus serving a connector) | betjene | The I2C section of technical-reference/hardware.md says which bus serves which display connector ("I2C0 (CM5 SDA0/SCL0) betjener MIPI0"). betjene keeps the bus as the subject; brukes til would make the sentence about the reader's use rather than the board's wiring. |
| layout | oppsett / oppbygning / plassering / kretskortlayout | Four senses the English word covers and Norwegian splits; they are not rivals and must not be harmonised. A set of items chosen from options is oppsett (standardoppsettet, tastaturoppsett, standardoppsettet med 40 pinner). How something is built up internally is oppbygning (the Intern oppbygning heading, and the carrier-board alt text Bærekortets oppbygning, oversiden). Where parts sit on a face is plassering (Kontaktplassering på HALPI2, the index.md alt text). PCB design files are kretskortlayout, the trade loan. |
| uninterruptible power supply (UPS) | avbruddsfri strømforsyning (UPS) | The "Not a UPS" warning in operation.md, power-supply.md and faq.md. UPS is the established Norwegian trade abbreviation; spell the term out on first mention and keep UPS elsewhere. |
| alternator load dump | «load dump» fra dynamoen | The 100 V transient example in power-supply.md. No Norwegian equivalent is in trade use; kept as quoted English jargon inside guillemets, glossed with dynamo for the alternator. |
| state machine | tilstandsmaskin | power-supply.md points to the controller reference for the state machine acting on the measurements. Standard Norwegian CS term. |
| charge-level bar (LED pattern) | ladenivåsøyle | The controller.md LED table names four of them (gul/grønn/oransje/mørkegrønn ladenivåsøyle). Bar patterns generally are søyle, per the existing spenningssøyle entry; the physical row of five LEDs is LED-raden. |
| input stage | inngangstrinn | Section heading in power-supply.md. Standard electronics term. |
| unattended operation | drift uten tilsyn | The design goal stated in operation.md and faq.md. Chosen over ubemannet drift, which suggests crewless vessels rather than a computer left alone. |

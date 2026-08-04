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

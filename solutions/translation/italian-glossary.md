---
title: Italian translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Italian under docs/it/
  - Reviewing an Italian translation for consistency
  - Adding a new term that has no established Italian equivalent
tags:
  - translation
  - i18n
  - italian
  - terminology
  - mkdocs-static-i18n
---

# Italian translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Italian under `docs/it/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/it/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md`, `german-glossary.md` and
`swedish-glossary.md` are the siblings of this file. The general approach is the
same in all five.

The locale code is `it`. mkdocs-material ships built-in UI translations for it,
so nothing in the theme chrome needs a manual string.

## Six rules where the siblings are wrong for Italian

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary. The recorded failure mode in this
repository is exactly that — a rule from a neighbouring language carried across,
or a rule written here and then applied to the first three pages only. Both were
caught by *counting* the finished pages, never by rereading them. Each rule below
is therefore written so it can be counted; the commands are in
[Verification](#verification).

1. **Address the reader impersonally.** Instructions use the **infinitive**, which
   is the standard register of Italian installation and user manuals:

   > Collegare il cavo di alimentazione. Verificare la polarità con il multimetro
   > prima di dare tensione.

   Descriptive passages use the impersonal *si*, the passive, or a plain
   statement:

   > Il dispositivo si spegne automaticamente quando l'alimentazione viene
   > interrotta. È possibile accedere alla custodia dopo aver rimosso le quattro
   > viti del coperchio.

   **Never `tu`** (Swedish uses `du`), **never `Lei`** (German uses `Sie`),
   **never the second person plural** (French uses *vouvoiement*). Italian
   differs from all four siblings here, which makes this the rule most likely to
   drift. No `puoi`, `devi`, `il tuo`, `la Sua`, `potete` anywhere in `docs/it/`.

   The English source is written in the second person (*you can access…*, *your
   HALPI2*). Recast it; do not carry the pronoun over. *your HALPI2* becomes
   `il proprio HALPI2` or simply `HALPI2`.

2. **Quotation marks are `"…"`** — U+201C opening, U+201D closing. **Not** the
   caporali `« … »`: those belong to French here, and choosing them would drag in
   the French no-break-space-inside habit with them. Not the German `„…"`, not
   straight `"…"`.

   Almost everything quoted in this corpus is a physical label on the board or a
   switch position — `"Abnormal"`, `"Normal"`, `"3.3V off"`, `"Pow.Ctrl"`,
   `"south"`, `"east"` — and doppi apici are the Italian convention for exactly
   that. The label text itself stays in English; only the marks around it are
   Italian.

3. **No space before `; : ! ?`** — as in German and Swedish, and unlike French,
   whose rule is the exact opposite and demands a no-break space. Write
   `Sintomi:`, never `Sintomi :`. The French rule cost a 334-site correction on
   its own branch; it must not cross into Italian.

   Italian's only no-break space (U+00A0) is between a number and its unit:
   `12 V`, `0,9 A`.

4. **Never hyphenate a product name into a compound.** German writes
   `NMEA-2000-Netzwerk` and Swedish writes `NMEA 2000-nätverk`. Italian does
   neither: the name follows the noun as a plain apposition.

   - `rete NMEA 2000`, `bus NMEA 2000`, `server Signal K`, `antenna Raspberry Pi`
   - `custodia di HALPI2`, `connettore E7T`, `immagine HaLOS`, `tastiera USB`
   - `connettore del Compute Module 5`

   A hyphen between an English product name and an Italian noun is the single
   most visible marker that a rule was copied from the German or Swedish page.
   Hyphens inside a name that already has one (`RS-485`, `T-connector` as a
   source term, `Micro-C`) are untouched — the rule is about *joining* a name to
   an Italian word.

5. **Typographic apostrophe U+2019, and no apostrophe on `qual è`.** Italian
   elides constantly — `l'alimentazione`, `dell'involucro`, `un'antenna`,
   `all'interno` — and the character is always `'` (U+2019), never the straight
   `'` (U+0027). No sibling glossary states this because no sibling needs it.

   `qual è` is written **without** an apostrophe. `qual'è` is the classic Italian
   spelling error and it is trivially countable.

   Accents are not optional: `perché`, `poiché`, `affinché`, `né`, `sé`, `più`,
   `così`, `è`. The grave-for-acute mistakes (`perchè`, `poichè`) are the second
   trivially countable error.

6. **No English plural `-s` on a loanword.** Italian borrows the singular and
   leaves it invariable: `i jumper`, `i LED`, `gli HAT`, `i container`,
   `le dashboard`, `i firmware`, `i pin`, `i connettori`. Writing `i jumpers` or
   `i LEDs` is the clearest tell of an unedited machine translation, and the
   English source is full of the plural forms that invite it.

## Names that are never translated

Product names, protocol names, hardware standards and software UI strings stay
in English — the device's own interface is in English, so translating a menu
name would send the reader looking for something that does not exist on screen.

HALPI2, HALPI, HaLOS, SH-ESP32, Signal K, OpenPlotter, Raspberry Pi, Raspberry Pi
OS, Compute Module 5 (CM5), Cockpit, Homarr, Authelia, Grafana, InfluxDB, AvNav,
OpenCPN, Hat Labs, NMEA 2000, NMEA 0183, CAN FD, SocketCAN, RS-485, RS-422,
Modbus RTU, NVMe SSD, GPIO, HDMI, MIPI, CSI, DSI, USB, RP-SMA, U.FL, E7T, PG7,
SP13, Micro-C, RJ45, IP65, DHCP, SSH, SSL, VNC, SSO, ABYC, Cat5e, AWG, HAT,
RP2040, gpsd, systemd, APT.

Also never translated:

- **Commands, file paths and configuration keys** — `halpi status`,
  `systemctl status halpid`, `/dev/ttyAMA4`, `/etc/halpid/halpid.conf`,
  `auto_restart`, `AUTO_FLASH_ON_INSTALL`, `can0`, `halos.local`.
- **Code fences and their contents**, including comments inside them, and all
  command output.
- **Silkscreen and switch labels** — `"Normal"`, `"Abnormal"`, `"3.3V off"`,
  `"Pow.Ctrl"`, `"USB Boot"`, `"120R"`, and the board position labels
  **a1**, **c2**, **g1** and the rest.
- **Firmware state names** reported by `halpi status` — `OperationalCoOp`. The
  prose modes built on them are written `modalità Solo` and `modalità Co-op`.
- **URLs and image filenames.**

Gender and article, fixed once so pages do not disagree with each other:

- **HALPI2** takes the elided article, because the `h` is silent: `l'HALPI2`,
  `dell'HALPI2`, `all'HALPI2`. Never `il HALPI2`.
- **CM5 / Compute Module 5** is masculine: `il CM5`, `del CM5`.
- **dashboard** is feminine: `la dashboard`, `dalla dashboard`.
- **jumper, HAT, container, firmware, pin, LED, watchdog, browser** are
  masculine and invariable: `il jumper` / `i jumper`, `il LED` / `i LED`.
- **scheda portante** is feminine: `la scheda portante`.

For bare acronyms, prefer putting an Italian noun in front rather than guessing
an article: `la porta USB`, `l'unità SSD`, `il connettore RJ45`,
`l'interfaccia CAN FD`.

## Glossary

### Enclosure, mounting, and installation

| English | Italian | Note |
|:--------|:--------|:-----|
| carrier board | scheda portante | The accurate term, as in French, German and Swedish — see the note below |
| enclosure | custodia | Not *involucro*, the normative IEC word, which reads as a standards document |
| lid | coperchio | |
| gasket | guarnizione | |
| heat sink | dissipatore di calore | |
| waterproof | impermeabile | One word for the whole corpus; do not alternate with *stagno* |
| wall-mount | montaggio a parete | |
| mounting surface | superficie di montaggio | |
| pilot hole | foro pilota | A hole **the reader drills**: `Praticare i fori pilota per le viti` |
| pre-drilled hole | foro predisposto | A hole **the enclosure ships with** — see the warning below |
| mounting template | dima di foratura | |
| bilge water | acqua di sentina | |
| bulkhead | paratia | |
| cable gland | pressacavo | |
| cable routing | posa dei cavi | |
| service loop | riserva di cavo | Slack left at both cable ends; gloss `(service loop)` on first mention |
| cable tie | fascetta | |
| blind plug | tappo cieco | |
| breather plug | tappo di compensazione | Pressure equalisation; must not be removed |
| thermal pad | pad termico | |
| standoff | distanziale | |
| countersunk screw | vite svasata | |
| socket (tool) | chiave a bussola | `chiave a bussola da 26 mm` |

**`foro pilota` and `foro predisposto` are two different things.** The English
source uses *pilot hole* for a hole the installer drills into the bulkhead, and
*pre-drilled* for the connector openings the enclosure already has. Conflating
them produced a nonsense instruction on the Swedish branch — *drill the
pre-drilled holes*. Keep them apart: `Praticare i fori pilota` for the reader's
drilling step, `posizioni predisposte` / `fori predisposti` for the factory
openings on the front panel.

**A note on `scheda portante`.** Italian takes the accurate term, like French
(`carte porteuse`), German (`Trägerplatine`) and Swedish (`bärkort`), and unlike
Finnish (`emolevy`, literally *motherboard*, chosen there for reader
familiarity). The divergence is deliberate, decided per language and per
audience. Do not harmonise them, and do not reach for `scheda madre`: it names
the wrong board and inverts the CM5 relationship.

`scheda portante` carries the CM5/board relationship on its own, so passages
about reinserting the CM5 or troubleshooting a board that will not boot need no
extra explanation. Only the Finnish glossary needs that warning. Gloss
`(carrier board)` in parentheses on the first mention of each page, because the
English term is what is printed in the schematics the reader may open next.

### Power and electrical

| English | Italian | Note |
|:--------|:--------|:-----|
| power supply | alimentazione | The unit itself: *alimentatore* |
| input voltage range | intervallo di tensione di ingresso | |
| polarity | polarità | |
| rail (3.3V rail) | linea | `la linea da 3,3 V`, `la linea da 5 V` |
| fuse | fusibile | |
| inline fuse | fusibile in linea | |
| circuit breaker | interruttore automatico | |
| current limiting | limitazione di corrente | The switch itself: *limitatore di corrente* |
| overcurrent | sovracorrente | |
| voltage drop | caduta di tensione | |
| grounding | messa a terra | |
| short circuit | cortocircuito | |
| wire gauge | sezione del conduttore | Italian uses mm², not AWG |
| marine-grade wire | cavo per uso nautico | |
| wire strippers | pinza spelafili | |
| crimping | crimpatura | |
| crimper | pinza crimpatrice | |
| heat-shrink tubing | guaina termorestringente | |
| heat gun | pistola termica | |
| multimeter | multimetro | |
| terminal block | morsettiera | |
| strain relief | scarico della trazione | |
| super-capacitor | supercondensatore | Also renders *supercapacitor*, written as one word in the English source |
| real-time clock | orologio in tempo reale | Keep `(RTC)` on first mention |
| backup battery | batteria tampone | |
| power loss | mancanza di alimentazione | |
| blackout | interruzione di corrente | `blackout timer` becomes `timer di interruzione di corrente` |

### Connectors and interfaces

| English | Italian | Note |
|:--------|:--------|:-----|
| connector | connettore | |
| barrel connector | connettore cilindrico | Gloss `(barrel)` on first mention |
| header | connettore a pettine | GPIO: `connettore GPIO a 40 pin` |
| pin | pin | Invariable: `i pin`, never `i pins` |
| pinout | piedinatura | |
| pitch | passo | `passo 3,81 mm` |
| jumper | jumper | Invariable; the word is on the silkscreen |
| backbone | dorsale | `dorsale NMEA 2000` |
| drop cable | cavo di derivazione | |
| T-connector | connettore a T | The source also says *T-adapter*; both become `connettore a T` |
| terminator | resistenza di terminazione | The jumper: `jumper di terminazione` |
| termination | terminazione | The act, or the state of the network |
| front panel | pannello frontale | |
| male / female | maschio / femmina | |
| receptacle | presa | |
| flexible flat cable | cavo piatto flessibile | Keep `(FFC)`; the acronym is used alone afterwards |
| board-to-board connector | connettore scheda-scheda | |

### Operation and system behaviour

| English | Italian | Note |
|:--------|:--------|:-----|
| boat computer | computer di bordo | |
| boot | avvio | The verb: *avviare* / *avviarsi* |
| first boot | primo avvio | |
| shutdown | spegnimento | The verb: *spegnere* |
| graceful shutdown | spegnimento controllato | |
| power management | gestione dell'alimentazione | |
| status LED | LED di stato | `i LED`, never `i LEDs` |
| monitoring | monitoraggio | |
| passive cooling | raffreddamento passivo | |
| filesystem | file system | Two words, masculine, invariable |
| unmount (filesystem) | smontare | `smontare il file system` |
| unmount (module or board) | rimuovere | Physical removal — `rimuovere la scheda portante dalla custodia` |
| reseat | reinserire | `reinserire il CM5 nel connettore` |
| watchdog | watchdog | Invariable |
| standby | standby | `modalità standby`; not *attesa* — it names a firmware state |
| power cycle | spegnere e riaccendere | Verb phrase; there is no good Italian noun |
| chart plotter | plotter cartografico | Gloss `(chartplotter)` on first mention |
| vessel | imbarcazione | Exception: *research vessels* is `navi da ricerca` |
| data logging | registrazione dei dati | |
| fleet management | gestione della flotta | |
| predictive maintenance | manutenzione predittiva | |
| remote monitoring | monitoraggio remoto | |
| compliance | conformità | |
| warranty | garanzia | |

### Software and networking

| English | Italian | Note |
|:--------|:--------|:-----|
| firmware | firmware | Invariable, masculine — matches the sibling decision to keep the trade term |
| daemon | demone | Established in Italian Linux usage |
| kernel module | modulo del kernel | |
| flash (firmware) | flashare | `flashare il firmware dell'RP2040` |
| flash (an image) | scrivere | Writing an OS image to the SSD: `scrivere l'immagine sull'unità SSD` |
| system image | immagine di sistema | Also `immagine del sistema operativo` where the source spells it out |
| headless | senza monitor | First mention: `senza monitor (headless)` |
| container app | applicazione in container | The Cockpit menu is `Container Apps` and stays English |
| container image | immagine del container | |
| dashboard | dashboard | Feminine: `la dashboard`. Homarr's view; not *cruscotto* |
| WiFi Access Point | access point WiFi | Standard Italian usage keeps *access point* |
| wired / wireless | via cavo / wireless | |
| credentials | credenziali | |
| default password | password predefinita | |
| single sign-on | autenticazione unica | Keep `(SSO)` on first mention, then `SSO` |
| Certificate Authority | autorità di certificazione | Keep `(CA)` on first mention, then `CA` |
| web interface | interfaccia web | |
| browser | browser | Invariable |
| remote access | accesso remoto | |
| update | aggiornamento | The verb: *aggiornare* |
| roll back | ripristinare | `ripristinare la versione precedente del firmware` |

## Units and numbers

The English source writes `12V` and `0.9A`, and both are wrong in Italian.
Convert every one. Numbers inside code fences and inline code are never touched.

| English source | Italian |
|:---------------|:--------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |
| `9–36 VDC` | `9–36 V CC` |
| `200×130×60 mm` | `200 × 130 × 60 mm` |

- **Decimal comma** everywhere in prose and tables: `0,9 A`, `3,81 mm`, `10,8 V`.
- **No-break space (U+00A0) between number and unit**, so the line never breaks
  between them.
- **Multiplication sign** `×` (U+00D7) for dimensions and quantities — `4× 25 F`,
  `2× USB 3.0` — never the letter `x`.
- **Minus sign** `−` (U+2212) for negative temperatures, not a hyphen.
- **En dash** `–` (U+2013) for ranges. In running prose `da −20 °C a +60 °C`
  reads better than the dash and is allowed; in tables use the dash form.
- **No thousands separator** in technical figures: `250 kbit/s`, not `250.000`.
- Every numeral in the English page must appear in the Italian page. A wrong
  voltage in an installation guide is a safety defect, not a typo.

## Links, images, admonitions, navigation

Same as the sibling glossaries:

- Paths are copied from the English source unchanged and **never** carry an
  `en/` or `it/` segment. The language comes from the directory the file is in.
- Image captions and alt texts are translated; filenames are not.
- Screenshots stay English, because the reader's own screen is English.
- Standard admonition titles (`note`, `warning`, `tip`, `info`, `danger`,
  `example`) are translated centrally in `mkdocs.yml`. A **custom** title is
  translated in the page: `!!! warning "Importante"`, `!!! danger "Attenzione"`,
  `!!! quote "Informazioni correlate"`.
- Anchors derive from heading text, so a translated heading changes its slug.
  Rewrite every in-page `](#…)` link, and after building read the real ids out
  of the generated HTML rather than guessing. Slugs strip accents:
  `Risoluzione dei problemi` → `risoluzione-dei-problemi`; `Conformità` →
  `conformita`.

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. `uv run python scripts/check_glossary.py it` passes. **This requires `it` to
   be registered in `scripts/check_glossary.py`** — the `GLOSSARIES` dict maps a
   language code to a glossary filename and currently lists only `fi`, `fr`,
   `de` and `sv`. Adding `"it": "italian-glossary.md"` is a prerequisite for the
   Italian branch, not an optional extra.
5. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
6. Every term used on the page that appears in this glossary matches it.

7. **The six rules at the top are counted against the pages, not re-read.** A
   half-applied typography rule looks followed when you read it, because
   rereading your own text confirms whatever it already says. Both the French and
   German branches shipped one to review for that reason. Run these; every one
   must print `0`, and the two quote counts must be equal.

    ```bash
    # Rule 1 — address form: no tu, no Lei, no second person plural
    grep -rEoi '\b(tu|tuo|tuoi|tua|tue|puoi|devi|potrai|dovrai|potete|dovete|vostro|vostra|vostri|vostre)\b' docs/it | wc -l
    grep -rEo '\b(Lei|Suo|Sua|Suoi|Sue)\b' docs/it | wc -l

    # Rule 2 — quotation marks: these two must be EQUAL and non-zero
    grep -rFo '“' docs/it | wc -l
    grep -rFo '”' docs/it | wc -l
    # and these must be 0
    grep -rEo '[«»]' docs/it | wc -l
    grep -rEo '(„|‟)' docs/it | wc -l

    # Rule 3 — no space (ordinary or no-break) before ; : ! ?
    grep -rEn '( |\xc2\xa0)[;:!?]' docs/it | wc -l

    # Rule 4 — no product name hyphenated into an Italian compound
    grep -rEn 'NMEA-2000|Signal K-|Raspberry Pi-|HALPI2-[a-zA-Zàèéìòù]|CM5-[a-z]|HaLOS-[a-z]' docs/it | wc -l

    # Rule 5 — apostrophes and accents
    grep -rFo "'" docs/it | wc -l          # straight U+0027: must be 0
    grep -rEon "qual'è" docs/it | wc -l
    grep -rEoni '\b(perchè|poichè|benchè|affinchè|nè|sè)\b' docs/it | wc -l

    # Rule 6 — no English plural -s on a loanword
    grep -rEoi '\b(jumpers|LEDs|HATs|containers|dashboards|firmwares|demons|pins|headers|drivers|plotters)\b' docs/it | wc -l
    ```

    Exclude code fences before counting rules 2, 3 and 5, since inline code and
    command output legitimately contain straight quotes, apostrophes and colons:

    ```bash
    python3 - <<'PY'
    import re, pathlib
    text = "\n".join(
        re.sub(r'`[^`\n]*`', ' ', re.sub(r'```.*?```', ' ', p.read_text(encoding='utf-8'), flags=re.S))
        for p in sorted(pathlib.Path('docs/it').rglob('*.md'))
    )
    checks = {
        'straight apostrophe': text.count("'"),
        'straight quote': text.count('"'),
        'guillemets': len(re.findall(r'[«»]', text)),
        'space before ;:!?': len(re.findall(r'[  ][;:!?]', text)),
        'open quotes': text.count('“'),
        'close quotes': text.count('”'),
        'tu/Lei forms': len(re.findall(r'\b(tu|tuo|tuoi|tua|tue|puoi|devi|Lei|Suo|Sua|potete|dovete|vostr\w+)\b', text)),
    }
    for k, v in checks.items():
        print(f'{v:6}  {k}')
    print('quotes pair' if checks['open quotes'] == checks['close quotes'] else 'QUOTES DO NOT PAIR')
    PY
    ```

8. **The two-sense terms are counted separately.** `foro pilota` must appear
   exactly where the English says *pilot hole* and nowhere else; `predispost*`
   exactly where it says *pre-drilled*. Same for `smontare` (file system) versus
   `rimuovere` (module), and `flashare` (firmware) versus `scrivere` (image).
   Compare the counts page by page against the English source — this is the pair
   that produced a nonsense instruction in Swedish.

    ```bash
    for t in 'pilot hole' 'pre-drilled' unmount flash; do
      printf '%-12s en=%s\n' "$t" "$(grep -rio "$t" docs/en | wc -l)"; done
    for t in 'foro pilota' predispost smontare rimuover flashare scriver; do
      printf '%-12s it=%s\n' "$t" "$(grep -rio "$t" docs/it | wc -l)"; done
    ```

9. **Every numeral in the English page appears in the Italian page**, allowing
   for the decimal comma. Diff the extracted number lists rather than skimming.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
  `swedish-glossary.md` — the sibling glossaries
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

## Terms added during translation

Reported by the page translators, consolidated here rather than written
by each of them, because five agents share this file.

| English | Translation | Note |
|:--------|:------------|:-----|
| Getting Started (page/guide title) | Guida introduttiva | H1 of the page and the link text to the HaLOS equivalent guide. Standard Italian documentation title; 'Per iniziare' is the alternative but reads less |
| Step (numbered procedure heading) | Passaggio | Used in 5 headings (Step 0-3). Needed a fixed choice so headings do not alternate between 'Passaggio', 'Fase' and 'Punto'. 'Fase' is reserved here for |
| wire (individual conductor: red wire / black wire) | conduttore | The glossary covers 'wire gauge' and 'marine-grade wire' but not the countable conductor. 'Conduttore' distinguishes the individual red/black lead fro |
| terminals (crimp-on ring/spade terminals) | capicorda | Distinct from 'morsettiera' (terminal block), which the glossary already fixes. 'Capicorda' is the standard Italian term for crimped cable-end termina |
| cable grommet | passacavo | Appears alongside 'cable gland' (pressacavo, in glossary) in the same sentence; needed a different word so the pair does not collapse into one term. |
| mounting hardware (corrosion-resistant) | minuteria di fissaggio | Standard Italian for screws/washers/brackets as a class; a literal 'hardware di montaggio' would clash with 'hardware' used for electronics elsewhere  |
| mounting clips | clip di fissaggio | Listed with cable ties in the materials list; kept parallel to 'minuteria di fissaggio'. |
| splash screen | schermata iniziale | Raspberry Pi OS boot screen. Established Italian rendering; the English term is not used in Italian consumer documentation. |
| controller (the RP2040 the HALPI daemon connects to) | controller | SUPERSEDED: this row first said 'controllore'. Resolved to 'controller' — see the 'controller (any controller IC)' row below. |
| rainbow pattern (LED) | sequenza arcobaleno | LED fault indication. Matched to 'sequenze dei LED di stato' used for 'status LED patterns' so the two references agree. |
| known-good device | dispositivo sicuramente funzionante | No idiomatic Italian noun phrase exists; a descriptive rendering is the usual solution in Italian technical manuals. |
| electrical codes | normative elettriche | Used three times (local electrical codes / comply with local electrical codes). 'Normative' rather than 'codici' — 'codice elettrico' is a calque that |
| Automotive Installations | Installazioni su veicoli | Heading parallel to 'Installazioni nautiche' and 'Installazioni industriali'; 'automobilistiche' would wrongly exclude commercial vehicles. |
| service loop (verb phrase 'allow/provide service loops') | prevedere una riserva di cavo | Glossary gives the noun 'riserva di cavo' and requires glossing '(service loop)' on first mention; recorded here as the verb collocation actually used |
| UART | UART (feminine: la UART, le UART) | The glossary lists no gender for UART and warns against guessing articles for bare acronyms. Feminine is the prevailing Italian usage (implicitly 'por |
| device tree overlay | overlay | Kept in English, masculine and invariable, matching the glossary's treatment of jumper/HAT/container. It is the literal name of the config.txt mechani |
| transceiver (RS-485) | transceiver | Kept in English, masculine. 'ricetrasmettitore' exists but is not what Italian electronics documentation calls an RS-485 line driver IC. Invariable pe |
| chip select | chip select | A signal name on the CAN FD controller, not prose. Left in English like the silkscreen labels; used in the conflicts table as 'Chip select del CAN FD' |
| SPI bus / I2C bus | bus SPI / bus I2C | Follows rule 4 (name as plain apposition after the noun), consistent with the glossary's 'bus NMEA 2000'. No hyphen. |
| mass-storage gadget | gadget di archiviazione di massa | Linux USB gadget terminology; 'gadget' has no Italian equivalent in this sense and is kept, with the rest translated. 'mass storage device' likewise b |
| block device | dispositivo a blocchi | Standard Italian Linux usage; not in the glossary. |
| boot mode switch | selettore della modalità di avvio | Built from the glossary's 'boot -> avvio'. The switch positions themselves stay English and quoted: “Normal”, “Abnormal”. |
| login console | console di accesso | The dedicated debug UART in interfaces.md. 'console' is feminine and invariable in Italian. |
| REST API | API REST | Italian inverts the order and treats API as feminine (l'API REST, un'interfaccia API REST). Appears in the heading 'Accesso all'API REST'. |
| port forwarding | port forwarding | Kept in English; the Italian calque 'inoltro delle porte' is not what router UIs or Italian network documentation use. |
| Hardware Guide (page title) | Guida all'hardware | Cross-reference target in software.md. Matches the pattern already established in docs/it: 'Guida introduttiva', 'Guida al software', 'Guida utente'.  |
| hardware flow control | controllo di flusso hardware | Standard Italian term; not in the glossary. |
| device node | nodo di dispositivo | Used in the interfaces.md verification section for the /dev/ttyAMA* entry. |
| header pins (table column) | Pin del connettore | Derived from the glossary's 'header -> connettore a pettine' and 'pin -> pin' (invariable). Shortened for the table column head. |
| taskbar | barra delle applicazioni | Standard Italian desktop terminology, used in the Graphical Updates section. |
| update manager | gestore degli aggiornamenti | Descriptive, not a UI string the reader will see in English on this screen (the source does not capitalise it). |
| pre-built images | immagini precompilate | Distinct from the glossary's 'system image -> immagine di sistema'; describes how Hat Labs ships them. |
| solder jumper | jumper a saldare | The glossary fixes "jumper" as invariable but has no entry for the solder-bridge variant (GPIO6-CAN.CS). "Jumper a saldare" keeps the glossary's loanw |
| backup power | alimentazione di riserva | The glossary has "backup battery = batteria tampone" but nothing for the super-capacitor-fed supply. "Batteria tampone" is wrong here (there is no bat |
| mainboard | scheda principale del computer | Appears once, describing what the carrier board is. The glossary forbids "scheda madre" because it names the wrong board and inverts the CM5 relations |
| voltage bar (LED pattern) | barra di tensione | LED pattern name in the status table, used five times. No glossary entry; "barra" is the usual Italian word for a bar-graph indicator and keeps the ta |
| power-loss detection | rilevamento della mancanza di alimentazione | Built from the glossary's "power loss = mancanza di alimentazione"; recorded so the compound is spelled the same way on other pages rather than drifti |
| silk screen | serigrafia | Used for the printed markings on the board (Contacts arrows, module outline). The glossary covers silkscreen *labels* staying English but not the surf |
| die-cast, powder-coated (enclosure) | pressofuso, verniciato a polvere | Enclosure manufacturing terms in the opening paragraph; both are the standard Italian industrial terms and neither is in the enclosure section of the  |
| spudger | spudger | Tool name in the CM5 removal procedure with no Italian equivalent in common use; kept as in the source alongside the translated alternatives (plettro  |
| single-sided / double-sided (SSD) | a singola faccia / a doppia faccia | M.2 form-factor description in the SSD compatibility section; the standard Italian phrasing, recorded so the two halves of the contrast stay parallel. |
| grace period (before automatic restart) | periodo di attesa | "5-second grace period" in the automatic-restart section. "Periodo di grazia" is a calque; "periodo di attesa" is what Italian technical prose uses fo |
| carrier board controller | controller della scheda portante | The glossary fixes 'carrier board' but never says how 'controller' itself is handled. Kept in English, masculine and invariable (il controller / i con |
| supercapacitor backup | riserva a supercondensatori | The glossary gives 'super-capacitor -> supercondensatore' and 'backup battery -> batteria tampone', but not the compound used as a section heading and |
| kbps / Mbps / bps | kbit/s / Mbit/s / bit/s | The units section prescribes '250 kbit/s' in the no-thousands-separator example but never states the rule generally. Applied uniformly (250 kbit/s, 8  |
| transceiver | transceiver | SUPERSEDED: this row first said 'ricetrasmettitore', contradicting the 'transceiver (RS-485)' row above. Resolved to 'transceiver' — see the 'transceiver (RS-485 line driver)' row below. |
| isolated ground / galvanically isolated | massa isolata / isolato galvanicamente | The glossary gives 'grounding -> messa a terra', which is the protective-earth sense and wrong for GND_CAN and GND_RS485, a floating reference. 'Massa |
| ferrite bead | perlina di ferrite | Component name in the USB section, not in the glossary. 'Perlina di ferrite' is the usual Italian catalogue term. |
| threaded insert / solder nut | inserto filettato / dado da saldare | Mounting section fasteners; the glossary covers standoff and countersunk screw but not these two. |
| powder-coated die-cast aluminium | alluminio pressofuso verniciato a polvere | Enclosure material, appears twice (summary table and mechanical table). Fixed once here so the two tables cannot disagree. |
| depth sounder / wind instrument | ecoscandaglio / strumento del vento | Marine instrument names in the RS-485 'Common Applications' section. 'Ecoscandaglio' is the standard Italian term; 'strumento del vento' matches the u |
| use case | caso d'uso | Page title of use-cases.md; standard Italian software-engineering rendering, written with the typographic apostrophe (caso d’uso). |
| buck converter / overvoltage disconnect | convertitore buck / disconnessione per sovratensione | Power-supply table entries. 'Buck' is kept as the trade term (as the glossary does for jumper/watchdog); the glossary has 'overcurrent -> sovracorrent |
| controller (the RP2040 board controller) | controller | Not in the glossary. I first wrote 'controllore', then aligned to 'controller' because the parallel Italian page docs/it/technical-reference/hardware. |
| mounting ledge | sporgenza di appoggio | errata.md. The cast ledge inside the enclosure that the PCB rests on. Distinct from 'punto di fissaggio' (mounting point) used in design-files.md for  |
| flash (casting defect) | bava | errata.md. Homonym trap: this is the casting sense of 'flash', nothing to do with 'flashare il firmware'. Quoted in the source as "flashes", so it app |
| inrush current | corrente di spunto | errata.md. Standard Italian electrotechnical term; 'corrente di avviamento' would read as motor jargon. |
| copper fill / copper pour | riempimento di rame | errata.md and design-files.md. The source uses both 'copper fill' and 'copper pours' for the same thing; both rendered identically. |
| solder nut | dado da saldare | design-files.md changelog. |
| test point | punto di test | design-files.md changelog. |
| buck converter | convertitore buck | design-files.md. 'convertitore step-down' also exists but 'buck' is what Italian datasheets use. |
| opamp | amplificatore operazionale | design-files.md. Spelled out; 'opamp' is not used in Italian running prose. |
| footprint (component) | impronta | design-files.md. PCB land pattern sense. |
| silkscreen | serigrafia | design-files.md. Distinct from the silkscreen *labels* themselves, which stay English per the glossary. |
| brownout | abbassamento di tensione | power-supply.md. Kept distinct from 'caduta di tensione' (voltage drop, already in the glossary) and from 'interruzione di corrente' (blackout). |
| cross-compilation | compilazione incrociata | integration.md. |
| thermal throttling | limitazione termica delle prestazioni | troubleshooting.md. Kept clear of 'limitazione di corrente' (current limiting) which is the glossary term for a different mechanism. |
| stray voltage | tensione parassita | troubleshooting.md. |
| gigabit ethernet | ethernet gigabit | index.md. Noun-first Italian order; no hyphen, per rule 4. |
| errata | errata corrige | errata.md page title. The standard Italian term. Note this changes the slug to 'errata-corrige'. |
| security hardening | rafforzamento della sicurezza | advanced-config.md. |
| cable plug (E7T cable plug) | spina volante | index.md. The free-hanging mating plug supplied loose, as opposed to the panel receptacle ('presa' in the glossary). |
| goodie bag | busta accessori | index.md image alt text. |
| controller (any controller IC: board controller, CAN FD controller, RP1 I/O controller, system controller) | controller | Rival-term resolution. Three earlier rows disagreed ('controllore' vs 'controller'). One rendering for all of them: `controller`, masculine and invariable (il controller / i controller), like jumper and watchdog. Italian electronics documentation says `controller CAN`, not `controllore`; `controllore` reads as a human inspector. `microcontrollore` is a different English word (*microcontroller*) and keeps its Italian form. |
| transceiver (RS-485 line driver) | transceiver | Rival-term resolution. Two earlier rows disagreed. `transceiver`, masculine and invariable. `ricetrasmettitore` is the Italian for a *radio* transceiver, which on a boat means the VHF set — actively misleading in this corpus. |
| LED pattern (table column and prose) | sequenza dei LED | Rival-term resolution. `Schema dei LED` appeared once as a table header against `Sequenza dei LED` elsewhere. `sequenza` is already fixed by the 'rainbow pattern' row; it now covers every use of *LED pattern*. |
| current limit switch | limitatore di corrente | Rival-term resolution. The main glossary already says the switch itself is `limitatore di corrente`, but the pages also called it `interruttore` and `selettore del limite di corrente`. One name only; refer back to it with a pronoun rather than a second noun. `interruttore` is reserved for circuit breakers and panel switches, `selettore` for the boot mode switch. |
| community | comunità | Rival-term resolution. The pages had both `community` and `comunità`. `comunità` matches the impersonal manual register of rule 1, and the sibling list labels around it are translated (`**Assistenza:**`), so `**Community:**` could not stay English. |
| support (help from Hat Labs or the community) | assistenza | Rival-term resolution. Distinct from `supporto`, which stays for the capability sense — *external antenna support* is `supporto per antenne esterne`, *HALPI2 support* is `supporto per HALPI2`. |
| onboard device | dispositivo integrato | technical-reference/hardware.md. Matches `interfacce integrate` / `periferiche integrate` already used on the page for *built-in*. `a bordo` is a trap in this corpus: it reads as aboard the vessel. |
| resistor (bare component, e.g. a 0 Ω series resistor) | resistenza | technical-reference/hardware.md. The glossary only fixes the compound `terminator -> resistenza di terminazione`. `resistore` exists but Italian electronics documentation and datasheets say `resistenza`. |
| Daily Operation (page title) | Uso quotidiano | H1 of user-guide/operation.md and every link text to it; matches the `nav_translations` value in mkdocs.yml. Replaces the former page title 'Funzionamento del sistema'. |
| Interface Reference (page title) | Riferimento interfacce | H1 of technical-reference/interfaces.md; matches `nav_translations`. Distinct from the user-guide page, which keeps 'Interfacce e connettività'. |
| Power Supply Deep Dive (page title) | Alimentazione in dettaglio | H1 of technical-reference/power-supply.md and link texts to it; matches `nav_translations`. Supersedes the earlier stub H1 'Approfondimento sull'alimentazione'. |
| FAQ (page title) | Domande frequenti | H1 of faq.md; matches `nav_translations`, like the sibling locales (Preguntas frecuentes, Veelgestelde vragen). |
| unattended operation | funzionamento non presidiato | operation.md, faq.md, controller.md. Standard Italian industrial term; 'incustodito' reads as an abandoned object. |
| power button | pulsante di accensione | Already established in user-guide/interfaces.md but never recorded. Used for the CM5 power button, external buttons, and the controller's simulated presses. Not 'pulsante di alimentazione'. |
| watchdog feed | feed del watchdog | controller.md. 'feed' kept English like the glossary's jumper/watchdog; 'alimentazione del watchdog' would collide with power vocabulary. |
| charge-level bar (LED pattern) | barra del livello di carica | controller.md LED table. The English source renamed the former 'voltage bar' (barra di tensione) in the rewritten pages; both rows stay valid for their own source text. |
| UPS / uninterruptible power supply | UPS / gruppo di continuità (UPS) | operation.md, power-supply.md, faq.md. Admonition title 'Not a UPS' -> 'Non è un UPS'. Spell out 'gruppo di continuità (UPS)' when the source spells out 'uninterruptible power supply'. |
| state machine | macchina a stati | power-supply.md. Standard Italian CS term. |
| wake-up (scheduled, from standby) | riattivazione | controller.md, operation.md. The verb is 'riattivarsi'; 'risveglio' reads as human sleep. |
| fallback (mode, firmware default) | di ripiego | controller.md: 'modalità di ripiego' (Solo mode), 'valore di ripiego del firmware' (auto_restart). 'di riserva' is avoided because 'riserva' is taken by backup power. |
| alternator load dump | load dump dell'alternatore | power-supply.md. 'load dump' is the trade term in Italian electronics documentation; no translation exists in common use. |
| power budget | bilancio di potenza | power-supply.md. Standard Italian electrotechnical term. |

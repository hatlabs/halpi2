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

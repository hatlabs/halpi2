---
title: Spanish translation glossary and style rules
date: 2026-08-04
category: translation
module: documentation
problem_type: reference
component: documentation
severity: medium
applies_when:
  - Translating any page from docs/en/ into Spanish under docs/es/
  - Reviewing a Spanish translation for consistency
  - Adding a new term that has no established Spanish equivalent
tags:
  - translation
  - i18n
  - spanish
  - terminology
  - mkdocs-static-i18n
---

# Spanish translation glossary and style rules

## Context

The HALPI2 documentation is written in English under `docs/en/` and translated
into Spanish under `docs/es/`, using the `mkdocs-static-i18n` folder structure.
Each language directory mirrors the same tree, so a translation keeps its
source's path and filename. Only markdown lives under `docs/es/`; images and
other assets stay with the English source and are shared.

`finnish-glossary.md`, `french-glossary.md`, `german-glossary.md` and
`swedish-glossary.md` are the siblings of this file. The general approach is the
same in all five.

The locale is a single generic `es`. There is no `es-ES` and no `es-419` build,
so every regional choice below is made once, for both audiences, and recorded
here.

## Six rules where the siblings are wrong for Spanish

Read this section before anything else. Every one of these is stated the
opposite way in at least one sibling glossary. Each is written so it can be
counted in the finished page rather than nodded at.

1. **The reader is never addressed.** French uses *vouvoiement*, German uses
   *Sie*, Finnish and Swedish use the second person singular. All four are wrong
   here. Spanish technical documentation is impersonal:

   > La unidad se apaga automáticamente cuando se interrumpe la alimentación.

   Procedure steps take the **infinitive**, not an imperative:

   > Conectar el cable de alimentación. Comprobar la polaridad con el multímetro
   > antes de aplicar tensión.

   This is also the only register that survives a generic `es` build: `usted`
   sounds commercial in Spain, `tú` sounds wrong in an installation manual
   anywhere, and `vosotros` does not exist in Latin America. The impersonal has
   no regional split at all.

   *Count:* `usted`, `ustedes`, `tú`, `ti`, `vosotros`, `vosotras` appear **zero**
   times. Every numbered and bulleted procedure step begins with an infinitive —
   count the steps, count the infinitives, the two numbers are equal.

2. **Inverted opening marks are mandatory.** `¿` and `¡` do not exist in the
   English source, so a missing one is never a copy error — it is always an
   omission, and it is the defect a Spanish reader sees first. Headings that are
   questions carry both marks: `## ¿Qué es HALPI2?`

   *Count:* the number of `¿` equals the number of `?` outside code. Exclamations
   in prose are rare here; when one is used it opens with `¡`. Do not count the
   `!` in `!!! warning` or in `![image]` — those are markdown syntax.

3. **Quotation marks are `«…»`** — angular marks, the RAE first level. Not
   German's `„…"`, not Swedish's `”…”`, not straight `"…"`. Use them for quoted
   hardware labels and UI strings that stay in English: `la posición «Abnormal»`,
   `el puente «3.3V off»`.

   **Unlike French, there is no space inside the marks.** `«Abnormal»`, never
   `« Abnormal »`. A French translator's muscle memory puts a no-break space
   there and it is invisible in review.

   *Count:* `«` and `»` occur the same number of times. `"`, `”`, `„` and `“`
   occur zero times outside code. The sequences `« ` and ` »` occur zero times,
   including with U+00A0.

4. **No space before `; : ! ?`** — as in German and Swedish, and the exact
   opposite of French, whose rule demands a no-break space there.

   *Count:* zero occurrences of a space (U+0020 **or** U+00A0) immediately before
   `;`, `:`, `!` or `?` outside code. Check U+00A0 explicitly: it is invisible,
   and it is what arrives when a French sentence pattern is carried across.

5. **A proper name never takes a hyphen in a compound.** German writes
   `NMEA-2000-Netzwerk`, Swedish `NMEA 2000-nätverk`, Finnish `NMEA 2000 -verkko`.
   Spanish uses a plain noun phrase or a preposition:

   - `red NMEA 2000`, `bus NMEA 2000`, `servidor Signal K`, `antena Raspberry Pi`
   - `carcasa del HALPI2`, `conector E7T`, `imagen de HaLOS`, `teclado USB`

   *Count:* `NMEA-2000`, `Signal-K`, `Raspberry-Pi`, `HALPI2-`, `HaLOS-` and
   `E7T-` occur zero times outside code and outside package names such as
   `halpi2-firmware`.

6. **One Spanish, no mixing.** No sibling language has a regional split, so no
   sibling glossary warns about this. Three decisions, made once:

   | Use | Never | Why |
   |:----|:------|:----|
   | ordenador | computadora, computador | One form must win; `ordenador` is chosen for the whole site |
   | supercondensador | supercapacitor | `capacitor` is an Americanism; `condensador` is the general term |
   | supervisión | monitoreo, monitorización | Both alternatives are regionally marked; `supervisión` is not |

   *Count:* each banned word appears zero times.

## What stays in English

Product names, protocol names, hardware standards and software UI strings stay
in English — the device's own interface is in English, so translating a menu
name sends the reader looking for something that is not on the screen.

- **Products and software:** HALPI2, HaLOS, Signal K, OpenPlotter, Raspberry Pi
  OS, Cockpit, Homarr, Authelia, Grafana, Hat Labs, Compute Module 5 (CM5)
- **Hardware and standards:** NMEA 2000, NMEA 0183, CAN FD, RS-485, NVMe SSD,
  GPIO, HDMI, MIPI (DSI/CSI), USB, RP-SMA, E7T, PG7, SP13, IP65, DHCP, SSH, SSL,
  ABYC, Cat5e, AWG
- **Commands, file paths, configuration keys, hostnames and code:**
  `raspi-config`, `passwd`, `halpi status`, `halos.local`, `can0`,
  `/dev/ttyAMA4`, `auto_restart`, `AUTO_FLASH_ON_INSTALL`
- **UI strings the reader will see in English:** **Networking**, **WiFi
  (wlan0)**, **Add**, and the board's own silkscreen labels — `«Normal»`,
  `«Abnormal»`, `«USB Boot»`

Code fences, command output, URLs and image filenames are never touched.

## Units and numbers

The English source writes `12V` and `0.9A`. Both are wrong in Spanish: SI
spacing and a decimal comma are required, and this needs an active conversion on
nearly every technical page.

| English source | Spanish |
|:---------------|:--------|
| `12V`, `0.9A` | `12 V`, `0,9 A` |
| `5.5 x 2.1 mm` | `5,5 × 2,1 mm` |
| `-20°C to +60°C` | `−20 °C … +60 °C` |
| `120Ω` | `120 Ω` |
| `3-5A` | `3–5 A` (en dash for ranges) |
| `1.5mm²`, `2m` | `1,5 mm²`, `2 m` |

Dimensions written as a single product spec keep the tight form:
`200×130×60 mm`.

**No thousands separator anywhere on this site.** Spanish forbids the English
comma (`115,200` reads as a decimal), and the alternatives — a period or a thin
space — buy nothing at the magnitudes used here. Baud rates, port numbers and
firmware versions are identifiers, not measurements: `115200 bps`, `9600`,
`puerto 2947`, `3.1.0` are copied unchanged.

## Links, images, admonitions, navigation

Same as the sibling glossaries: paths are copied from the English source
unchanged and never carry an `en/`, `es/` or other language segment; image
captions and alt texts are translated but filenames are not; screenshots stay
English because the reader's own screen is English; standard admonition titles
are translated centrally in `mkdocs.yml`, custom ones in the page.

Translated headings change their anchors, and `¿` and the accents are stripped
by the slugifier — `## ¿Qué es HALPI2?` does **not** become `#¿que-es-halpi2`.
Do not guess: build the site and read the real ids out of the generated HTML.

## Glossary

### Enclosure and mounting

| English | Spanish | Note |
|:--------|:--------|:-----|
| carrier board | placa portadora | The accurate term, as in French, German and Swedish |
| enclosure | carcasa | |
| heat sink | disipador térmico | The enclosure doubles as one |
| waterproof | estanco | `carcasa estanca (IP65)` |
| rugged | robusto | |
| wall-mount | montaje en pared | |
| mounting surface | superficie de montaje | |
| pilot hole (to be drilled) | agujero guía | `Taladrar los agujeros guía para los tornillos` |
| pre-drilled hole (already there) | orificio pretaladrado | The holes the enclosure ships with |
| mounting template | plantilla de taladrado | |
| clearance | espacio libre | |
| bilge water | agua de sentina | The compartment alone: *sentina* |
| bulkhead | mamparo | |
| cable gland | prensaestopas | `prensaestopas PG7` |
| cable routing | tendido de cables | |
| service loop | bucle de servicio | Slack left at both cable ends |
| cable tie | brida | |
| blind plug | tapón ciego | |
| breather plug | tapón compensador de presión | Must never be removed |

**Two rows, not one, for the holes.** `pilot hole` is a hole that does not exist
yet and has to be drilled; `pre-drilled hole` is one the enclosure arrives with.
The English source uses both, three sections apart. Collapsing them produced a
nonsense instruction in Swedish — *drill the pre-drilled holes* — so never write
`taladrar los orificios pretaladrados`.

**A note on `placa portadora`.** Spanish takes the accurate term, like French
(`carte porteuse`), German (`Trägerplatine`) and Swedish (`bärkort`), and unlike
Finnish (`emolevy`, literally *motherboard*, chosen there for reader
familiarity). The divergence between the five is deliberate, decided per
language and per audience. Do not harmonise them.

`placa portadora` carries the CM5/board relationship on its own, so passages
about reseating the CM5 or troubleshooting a board that will not boot need no
extra explanation. Only the Finnish glossary needs that warning.

### Power and electrical

| English | Spanish | Note |
|:--------|:--------|:-----|
| power supply | alimentación | The unit itself: *fuente de alimentación* |
| power source | fuente de alimentación | |
| input voltage range | rango de tensión de entrada | |
| polarity | polaridad | |
| positive (+) / negative (−) | positivo (+) / negativo (−) | |
| fuse | fusible | |
| inline fuse | fusible en línea | |
| circuit breaker | interruptor automático | Neutral; not *magnetotérmico* or *disyuntor* |
| electrical panel | cuadro eléctrico | |
| current limiting | limitación de corriente | |
| current limiter | limitador de corriente | The circuit |
| current limit | límite de corriente | The `0,9 A` / `2,5 A` setting |
| overcurrent | sobrecorriente | |
| voltage drop | caída de tensión | |
| grounding | puesta a tierra | |
| short circuit | cortocircuito | |
| wire gauge | sección del conductor | Spanish uses mm², not AWG |
| marine-grade wire | cable de calidad náutica | |
| to strip (a wire) | pelar | |
| wire strippers | pelacables | |
| crimping | crimpado | Verb: *crimpar*. Established trade usage, like `firmware` |
| crimper | tenaza de crimpar | |
| heat-shrink tubing | tubo termorretráctil | Two r's |
| heat gun | pistola de aire caliente | |
| multimeter | multímetro | Not *polímetro* |
| continuity test | prueba de continuidad | |
| terminal | terminal | |
| terminal block | bloque de terminales | Not *bornera* or *regleta* |
| strain relief | descarga de tracción | Its absence is why the screw-terminal barrel plug is temporary only |
| super-capacitor | supercondensador | |
| real-time clock | reloj de tiempo real | |
| backup battery | pila de respaldo | The CR2032 for the RTC |

### Connectors and interfaces

| English | Spanish | Note |
|:--------|:--------|:-----|
| connector | conector | |
| barrel connector | conector cilíndrico | Add *(barrel)* on first mention |
| header | conector de pines | `conector GPIO de 40 pines` |
| pin | pin | |
| jumper | puente | Add *(jumper)* on first mention |
| backbone | cable troncal | The NMEA 2000 trunk; the network as a whole: *red troncal* |
| drop cable | cable de derivación | |
| T-connector | conector en T | Also for the source's *T-adapter* |
| terminator | terminador | The bus terminator enabled by the jumper |
| termination resistor | resistencia de terminación | The 120 Ω component |
| termination | terminación | The act, and the network property |
| front panel | panel frontal | |
| antenna | antena | |
| extension cable | cable alargador | |
| male / female | macho / hembra | |

### Operation and system behaviour

| English | Spanish | Note |
|:--------|:--------|:-----|
| boat computer | ordenador de a bordo | See rule 6 on `ordenador` |
| to boot | arrancar | Noun: *arranque* |
| first boot | primer arranque | |
| shutdown | apagado | |
| graceful shutdown | apagado controlado | |
| power loss | pérdida de alimentación | |
| blackout | corte de corriente | `temporizador de corte de corriente` |
| glitch immunity | inmunidad a microcortes | |
| power management | gestión de la alimentación | |
| status LED | LED de estado | |
| LED bar | barra de LED | |
| monitoring | supervisión | Never *monitoreo* or *monitorización* |
| passive cooling | refrigeración pasiva | |
| watchdog | watchdog | Gloss once as *(temporizador de vigilancia)*, then keep the term |
| standby | modo de reposo | The planned state where the CM5 is off and the controller waits |
| filesystem | sistema de archivos | |
| to unmount (a filesystem) | desmontar | `el sistema de archivos se desmonta de forma segura` |
| to unmount (a board or module) | retirar | The source says *unmount* for the carrier board and the CM5 too; `desmontar` there reads as *dismantle* |
| to reseat (a module) | volver a asentar | |

### Software and networking

| English | Spanish | Note |
|:--------|:--------|:-----|
| firmware | firmware | Not *microprogramación* — matches the sibling decision to keep the trade term |
| daemon | demonio | Established in Spanish Linux usage, as in French |
| to flash (firmware or an image) | grabar | Noun: *grabación*. Never *flashear* |
| to flash (an LED) | parpadear | A machine translator renders both English senses the same way; these are different words in Spanish |
| system image | imagen del sistema | |
| operating system image | imagen del sistema operativo | |
| headless | sin pantalla | First mention: `sin pantalla (headless)` |
| deployment | puesta en marcha | |
| container app | aplicación en contenedor | |
| container image | imagen de contenedor | Not *imagen del sistema* |
| dashboard | panel de control | Homarr's *dashboard* view |
| WiFi Access Point | punto de acceso WiFi | |
| wired / wireless | por cable / inalámbrico | |
| credentials | credenciales | |
| username / password | nombre de usuario / contraseña | |
| default password | contraseña predeterminada | |
| single sign-on (SSO) | inicio de sesión único (SSO) | |
| Certificate Authority (CA) | autoridad de certificación (CA) | |
| to trust (a certificate) | confiar en | |
| web interface | interfaz web | Feminine: *la interfaz* |
| browser | navegador | |
| system administration | administración del sistema | |

### Applications and use cases

| English | Spanish | Note |
|:--------|:--------|:-----|
| chart plotter | plóter cartográfico | |
| data logging | registro de datos | |
| vessel | embarcación | Not *buque*, which implies a ship |
| engine parameters | parámetros del motor | |
| fleet management | gestión de flotas | |
| predictive maintenance | mantenimiento predictivo | |
| process monitoring | supervisión de procesos | |
| remote monitoring | supervisión remota | |
| electromagnetic interference (EMI/RFI) | interferencias electromagnéticas (EMI/RFI) | |
| compliance | conformidad | |
| warranty | garantía | |

## Verification

A translated page is not done until:

1. `uv run mkdocs build --strict` passes.
2. `uv run python scripts/check_anchors.py site` passes.
3. `uv run python scripts/translation_status.py` shows the page as current.
4. `uv run python scripts/check_glossary.py es` passes.
5. Structure matches the source — see `.claude/skills/translate-page/SKILL.md`.
6. Every term used on the page that appears in this glossary matches it.
7. **The six rules at the top are measured against the pages, not re-read.** A
   half-applied typography rule looks followed when you read it, because
   rereading your own text confirms whatever it already says. The French and
   German branches each shipped one to review for exactly this reason. Every
   rule above carries a *Count:* line; run the counts.

The four that catch the most on a Spanish page, as one command from the repo
root:

```bash
python3 - <<'PY'
import re, pathlib
text = "\n".join(
    re.sub(r"`[^`\n]*`", " ", re.sub(r"```.*?```", " ", p.read_text(encoding="utf-8"), flags=re.S))
    for p in sorted(pathlib.Path("docs/es").rglob("*.md"))
)
print("¿ vs ?          ", text.count("¿"), text.count("?"))
print("« vs »          ", text.count("«"), text.count("»"))
print("stray quotes    ", sum(text.count(c) for c in '"”„“'))
print("space before ;:!?", len(re.findall(r"[  ][;:!?]", text)))
print("reader addressed", len(re.findall(r"\b(usted|ustedes|tú|ti|vosotr[oa]s)\b", text, re.I)))
print("regional mixing ", len(re.findall(r"\b(computador[a]?|supercapacitor|monitoreo|monitorizaci[óo]n)\b", text, re.I)))
PY
```

Every number on the right must be zero except the first two pairs, which must be
equal within each pair.

## Related

- `finnish-glossary.md`, `french-glossary.md`, `german-glossary.md`,
  `swedish-glossary.md` — the siblings
- `.claude/skills/translate-page/SKILL.md` — the procedure
- `../best-practices/` — the two markdown traps that survive `--strict`

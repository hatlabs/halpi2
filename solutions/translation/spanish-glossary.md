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
| kernel module | módulo del kernel | Not *módulo del núcleo* — matches integration.md |
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

## Terms added during translation

Reported by the page translators, consolidated here rather than written
by each of them, because five agents share this file.

| English | Translation | Note |
|:--------|:------------|:-----|
| Getting Started (page/section title) | Primeros pasos | Page H1 and the HaLOS guide link text. Standard Spanish docs heading; avoids turning a noun phrase into a question that would need ¿…? |
| desktop setup (on a desk/bench, as opposed to permanent installation) | configuración de sobremesa | Recurs six times on this page as the counterpart of `instalación permanente`. Not the GUI desktop — `escritorio` would be wrong here. |
| wall wart (power supply) | «wall wart» (transformador de enchufe) | Quoted colloquial English in the source. Kept in guillemets per rule 3 with a short gloss on first and only mention; there is no established Spanish t |
| splash screen | pantalla de inicio | Raspberry Pi OS boot screen; needed a fixed rendering so it does not drift to `pantalla de bienvenida` on other pages. |
| cable grommet | pasacables | Appears alongside `cable gland` (prensaestopas) in the same sentence; the two must stay distinct, as with the pilot-hole / pre-drilled-hole pair. |
| mounting hardware (screws, brackets) | herrajes de montaje | "Corrosion-resistant mounting hardware" — `hardware` alone would read as electronics in a hardware manual. |
| cable tie / mounting clip | brida / clip de sujeción | `brida` is already in the glossary; `mounting clip` is not and is paired with it in the materials list. |
| rainbow pattern (LED fault indication) | patrón de arcoíris | Diagnostic LED pattern for an unseated CM5; a fixed wording matters because it is the symptom a reader searches for. |
| cable tester | comprobador de cables | Troubleshooting tool, distinct from `multímetro` which the glossary already fixes. |
| over-torque (verb) | excederse en el par (de apriete) | Mounting-screw instruction; `sobrepar` is not idiomatic Spanish. |
| Container Apps store (Cockpit) | tienda de aplicaciones en contenedor | Built on the glossary's `aplicación en contenedor`. Cockpit's own label is English, but the source uses it descriptively rather than as a quoted butto |
| known-good device | dispositivo que se sepa que funciona | Troubleshooting idiom with no compact Spanish equivalent; a literal `dispositivo bueno conocido` is meaningless. |
| device tree overlay | overlay | interfaces.md, 3 occurrences. Kept as the trade term, consistent with the glossary's decision to keep `firmware`. `superposicion de arbol de dispositi |
| chip-select | chip-select | interfaces.md table, `CAN FD chip-select`. A signal name on the board, not prose; `seleccion de chip` would not match anything the reader can look up. |
| transceiver | transceptor | interfaces.md, `an RS-485 transceiver's enable line`. Standard Spanish electronics term. |
| hardware flow control | control de flujo por hardware | interfaces.md, introduces the `ctsrts` parameter. |
| mass storage device | dispositivo de almacenamiento masivo | software.md, USB-boot procedure, 3 occurrences. The state the HALPI2 presents itself in during `rpiboot` flashing. |
| block device | dispositivo de bloques | software.md step 6, `any other tool that can write to a block device`. |
| boot mode switch | interruptor de modo de arranque | software.md, 3 occurrences in the USB-boot steps. Built on the glossary's `arranque`; the associated silkscreen labels stay English as `«Normal»` / `« |
| power cycle (noun) / to power-cycle | ciclo de alimentacion / realizar un ciclo de alimentacion | software.md, 3 occurrences including the admonition title. Distinct from `apagado` and from `reinicio`, and the firmware-update section depends on the |
| marine apps | aplicaciones náuticas | software.md image-variant table and Homarr description, 4 occurrences. The glossary has `vessel -> embarcacion` but no adjective for the application c |
| firewall | cortafuegos | software.md, VNC and Raspberry Pi Connect sections. |
| port forwarding | redireccion de puertos | software.md VNC section, alongside VPN. |
| taskbar | barra de tareas | software.md, Graphical Updates section. |
| update manager | gestor de actualizaciones | software.md, Graphical Updates section. |
| hostname | nombre de host | software.md, Raspberry Pi Imager customisations. Kept close to the English because the Imager field itself reads `hostname`. |
| to roll back (firmware) | volver a la version anterior | software.md Firmware Safety Features. Verbal phrase rather than a noun, so it composes with the impersonal register required by rule 1. |
| login console | consola de inicio de sesion | interfaces.md, the dedicated debug UART. Reuses the glossary's `inicio de sesion` from `single sign-on`. |
| power rail (3.3V rail, 5V rail) | línea (línea de 3,3 V, línea de 5 V) | Not in the glossary and it occurs eight times across both pages. Chose «línea» over the calque «raíl»/«riel» because it is regionally neutral (rule 6) |
| flange (wide flange required on inside) | reborde | The obvious equivalent «brida» is already assigned to *cable tie* in the glossary, so using it here would collide. «Reborde» names the wide collar of  |
| standoff | separador | HAT mounting hardware; appears five times in the HAT installation section and had no glossary entry. |
| spudger | espátula (spudger) | No Spanish equivalent in common trade use; glossed on first mention and the English kept in parentheses, following the glossary's `sin pantalla (headl |
| solder jumper | puente de soldadura | Distinct from the removable `jumper` already in the glossary (`puente`); this one is a PCB trace that has to be cut. |
| Solo Mode / Co-op Mode | modo solo / modo cooperativo (co-op) | Firmware operating modes, not UI strings the reader sees on screen, so translated. «co-op» kept in parentheses on first mention because `halpi status` |
| VDC (11-32 VDC, 100 VDC) | V CC (11–32 V CC, 100 V CC) | SI/Spanish convention for direct-current voltage; the glossary sets unit spacing but does not cover the DC suffix. |
| chip select | selección de chip (chip select) | SPI signal name; translated with the English glossed once because the table row abbreviates it as `SPI CS`. |
| watchdog timeout | tiempo de espera del watchdog agotado | The glossary fixes `watchdog` itself but not `timeout`; «tiempo de espera» is used consistently for all four timeout occurrences across both pages. |
| blinkenlights | Blinkenlights | Left untranslated. It is a jargon in-joke, not a technical term, and any Spanish rendering loses the joke while gaining nothing; flagged here so a rev |
| rail (power rail: 5V rail, 3.3V rail) | línea (línea de 5 V, línea de 3,3 V) | Not in the glossary but already used in docs/es/user-guide/operation.md:121 ("La línea de 5 V se desactiva") and hardware.md:92. Adopted for consisten |
| pitch (connector pitch) | paso | Appears constantly in hardware.md (3.81 mm, 2.54 mm, 0.5 mm). Already established in docs/es/user-guide/hardware.md ("tipo Phoenix MC, paso de 3,81 mm |
| hub (USB hub) | concentrador | Already established in docs/es/user-guide/hardware.md:114-116 and appendices/design-files.md ("concentrador USB3"). |
| pinout | asignación de pines | Heading term in both pages. Already established in docs/es/user-guide/hardware.md:185,247. Chosen over "patillaje", which is Spain-marked. |
| VDC | V CC | Unit form, not a protocol name, so it is translated. Already established in docs/es/index.md:30, operation.md:43 and troubleshooting.md:11. |
| Load Equivalency Number (LEN) | número de equivalencia de carga (LEN) | NMEA 2000 term. Acronym kept in English because it is what the reader sees on cabling datasheets; the expansion is glossed once on first mention. |
| multi-talker / single-talker / single-talker-multiple-listener | multiemisor / de un solo emisor / de un emisor y varios receptores | RS-485 and NMEA 0183 topology terms used three times in interfaces.md. "Talker" has no established Spanish loan here; "emisor"/"receptor" is the stand |
| normally-open (NO) momentary switch | pulsador momentáneo normalmente abierto (NA) | Switch specification, not a UI string, so the abbreviation is translated (NO → NA) per Spanish electrical convention. |
| thermal pad | almohadilla térmica | Thermal management table in hardware.md. Distinct from "disipador térmico" (heat sink), which the glossary already covers. |
| half-duplex | semidúplex | RAE-accepted form; used once in the RS-485 section. |
| flexible flat cable (FFC) | cable plano flexible (FFC) | Used for the HDMI and MIPI connectors; the acronym stays English because it is the part-ordering term. |
| buck converter | convertidor reductor | Power supply table. "Convertidor buck" is also common but the Spanish form is unambiguous and needs no gloss. |
| receptacle (USB receptacle) / socket (M.2 Socket M) | conector hembra / zócalo | Two different English words for connector openings in hardware.md; kept distinct because the M.2 one is a card slot and the USB one is a cable port. |
| pigtail (panel connector) | latiguillo | Product name in the shop link in the RS-485 wiring section. |
| threaded insert / countersunk / gasket | inserto roscado / avellanado / junta | Mechanical specifications table; none appear in the glossary's enclosure section. |
| VDC (unit suffix, e.g. 32 VDC) | V CC | The glossary's units table covers V, A, Ω, °C, mm² but not the DC suffix. Spanish writes corriente continua, so the SI-spaced form is `32 V CC`. Appea |
| mounting ledge | resalte de montaje | errata.md, twice. Distinct from `punto de montaje` (mounting point, design-files.md) and from `superficie de montaje` (mounting surface, already in th |
| flash (casting defect, in quotes in the source) | rebaba | errata.md. The source quotes it as "flashes" and glosses it as leftover aluminium from casting. Standard Spanish foundry term. Written «rebabas» per r |
| inrush current | corriente de irrupción | errata.md. The glossary has `overcurrent` → sobrecorriente and `current limiting` → limitación de corriente, but not the power-up surge. `corriente de |
| copper pour / copper fill | vertido de cobre | design-files.md and errata.md. PCB-layout term; `relleno de cobre` used for the errata heading where the source says "Copper Fill", `vertidos de cobre |
| power plane / rail | plano de alimentación / línea | errata.md (`3.3V power plane` → plano de alimentación de 3,3 V) and design-files.md (`3.3V rail` → la línea de 3,3 V). Kept distinct because the sourc |
| solder nut | tuerca soldable | design-files.md, twice. |
| footprint (PCB component) | huella | design-files.md. Established KiCad terminology in Spanish. |
| opamp (operational amplifier) | amplificador operacional | design-files.md. |
| test point | punto de prueba | design-files.md. |
| silkscreen | serigrafía | design-files.md. The glossary already refers to "the board's own silkscreen labels" in the what-stays-English section but does not give the Spanish no |
| PCB layout | trazado del PCB | design-files.md. Verb form for `to re-route`: volver a trazar. |
| signal integrity | integridad de señal | design-files.md, twice. |
| cable plug (the loose connector supplied for custom wiring) | clavija de cable | index.md (`E7T cable plug` → Clavija de cable E7T). Distinct from `conector` (the mating connector on the enclosure) and from `conector cilíndrico (ba |
| cutout (in the enclosure, for an extra connector) | troquel | index.md (`cutouts for 2 extra SMA connectors`). Not the same as `orificio pretaladrado`, which the glossary reserves for holes the enclosure already  |
| thermal throttling | limitación térmica | troubleshooting.md. |
| runaway process | proceso desbocado | troubleshooting.md. |
| stray voltage | tensión parásita | troubleshooting.md, twice. The source says "stray voltages" injected by a connected device. |
| bus contention | contención en el bus | troubleshooting.md. |
| baud rate / bit rate (prose) | velocidad de transmisión | troubleshooting.md (`incorrect baud rate`). The glossary's number rules cover how to write `115200 bps` but not the prose noun. |
| differential signaling | señalización diferencial | troubleshooting.md (RS-485 A/B lines). |
| differential pair | par diferencial | design-files.md (`USB3 hub RX differential pairs`). |
| USB hub | concentrador | design-files.md. |
| clock oscillator | oscilador de reloj | design-files.md. |
| balancing circuit (super-capacitor) | circuito de equilibrado | design-files.md, twice. Verb/noun: equilibrado, not balanceo. |
| 3rd party | de terceros | ubuntu-installation.md (3rd party operating systems) and resources.md (third-party software compatibility). Used consistently across both. |
| user space | espacio de usuario | ubuntu-installation.md (`the user space halpid daemon`). |
| prebuilt package | paquete precompilado | ubuntu-installation.md. |
| command line tool | herramienta de línea de comandos | ubuntu-installation.md. The glossary keeps command names in English but does not give the phrase. |
| cross-compilation | compilación cruzada | integration.md. |
| custom image building | creación de imágenes personalizadas | integration.md. Built on the glossary's `imagen del sistema`. |
| security hardening | refuerzo de la seguridad | advanced-config.md. |
| backup and recovery (data, not power) | copia de seguridad y recuperación | advanced-config.md. Deliberately not `respaldo`, which the glossary assigns to the super-capacitor and RTC battery senses (`pila de respaldo`, `respal |
| performance tuning | ajuste del rendimiento | advanced-config.md. |
| brownout | caída de tensión | power-supply.md. Reuses the glossary's `voltage drop` → caída de tensión; kept distinct from `corte de corriente` (blackout), which the glossary alrea |
| load management | gestión de la carga | power-supply.md. |
| status reporting | notificación del estado | controller.md. Paired with the glossary's `monitoring` → supervisión in the same bullet. |
| CE marking | marcado CE | compliance.md. Official EU term. |
| environmental rating | clasificación ambiental | compliance.md. |
| chart plotter (plural) | plóteres cartográficos | index.md. Confirms the plural of the glossary's `plóter cartográfico`; plóteres, not plóters. |
| single-board computer | ordenador de placa única | index.md. Follows rule 6 on ordenador. |
| in-vehicle infotainment | infoentretenimiento a bordo | index.md. |
| telematics | telemática | index.md. |
| environmental sensing | detección ambiental | index.md. |
| quick start guide | guía de inicio rápido | index.md. Note this is the printed leaflet in the box, distinct from the nav section `Getting Started` → `Primeros pasos`, which mkdocs.yml already fi |
| goodie bag | bolsa de accesorios | index.md, image alt text only. |
| clean shutdown | apagado controlado | troubleshooting.md. The source varies its wording (`clean shutdown` here, `graceful shutdown` elsewhere) for one concept; Spanish keeps the single rendering the glossary already assigns to `graceful shutdown`. Not `apagado limpio`. |
| power connector / power socket | conector de alimentación | The English source alternates the two words for the same E7T port; Spanish uses one. `toma` is reserved for nothing here — see `receptacle / socket` above for the connector-opening senses. |
| pull-up resistor | resistencia de pull-up | technical-reference/hardware.md, I2C section. The English term is kept, as with `firmware` and `watchdog`: `resistencia de polarización` names a different function and `resistencia elevadora` is a calque no datasheet uses. |
| to serve (a bus feeding a connector) | dar servicio a | technical-reference/hardware.md, I2C section, where one bus serves MIPI0 and another MIPI1. Neutral and impersonal per rule 1; `alojar` is already used for the devices sitting on a bus, so a second verb is needed for the bus reaching a connector. |
| UPS (uninterruptible power supply) | SAI (sistema de alimentación ininterrumpida) | operation.md, power-supply.md and faq.md, including the admonition title «No es un SAI». Standard Spanish acronym; glossed once on first mention per page where it appears in prose. |
| unattended operation | funcionamiento desatendido | operation.md and faq.md. Recurs as the design premise of the power management chapter. |
| fallback mode | modo de respaldo | controller.md, Solo mode. Reuses the glossary's `respaldo` (backup) sense: the mode the controller falls back on. |
| state machine | máquina de estados | power-supply.md, twice. Established Spanish CS term. |
| load dump (alternator) | desconexión brusca de carga (load dump) | power-supply.md, input stage. The English term is what automotive EMC datasheets use, so it is glossed in parentheses on the single mention. |
| power budget | presupuesto de potencia | power-supply.md, current limiting section. |
| watchdog feed (noun) | señal de alimentación del watchdog | controller.md. The verb phrase «alimentar el watchdog» was already established; this is the noun the daemon sends. |
| add-on | complemento | operation.md, the HALPI2 blinkenlights add-on. |
| firmware variant | variante de firmware | user-guide/interfaces.md, sección WiFi; la elección de `update-alternatives` entre `standard` y `minimal` |
| WiFi channel | canal | Misma sección: `selección de canal` para la elección automática, `canal fijo` para uno fijado |
| access point client | cliente | Dispositivo conectado al punto de acceso; distinto del programa cliente (cliente SSH) en software.md |

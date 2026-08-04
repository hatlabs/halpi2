# Konstruktionsfiler och kopplingsscheman

Den här sidan tillhandahåller kopplingsscheman och mekaniska konstruktionsfiler för HALPI2.

HALPI2:s elektronik konstrueras i KiCad. Konstruktionsfilerna finns i [GitHub-repositoriet](https://github.com/hatlabs/HALPI2-hardware). Varje släppt version har en motsvarande tagg i repositoriet.

Kopplingsschemana finns nedan som PDF-filer för enkelhetens skull. Kretskortets layoutfiler finns endast i GitHub-repositoriet.

Mekaniska konstruktionsfiler finns tills vidare bara för kapslingen. Konstruktionen är gjord i Autocad Fusion, men exportfilerna i STEP-format går att öppna i de flesta CAD-program.

## Version 0.6.1

En rättningsversion med förbättringar av signalintegritet och jordning som upptäcktes under produktionstesterna.

Ändringar:

- Klockoscillator tillagd för NVMe SUSCLK, vilket åtgärdar kompatibilitetsproblem med vissa NVMe SSD-enheter
- Saknade kondensatorer tillagda på USB3-hubbens RX-differentialpar
- Jordning ordnad vid varje monteringspunkt

### Konstruktionsfiler

- KiCad-konstruktionsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Kopplingsschema (PDF): [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Version 0.6.0

HALPI2:s tredje produktionsversion med ytterligare mindre rättningar på bärkortet. Kortets funktioner är desamma som i version 0.5.0.

Ändringar:

- 3,3 V-utgången styrs nu av styrkretsen i stället för att alltid vara på
- Testpunkter tillagda för bättre produktionstester
- HDMI-, MIPI- och USB3-gränssnitten omdragna för bättre signalintegritet
- Kortets FFC-anslutningar sitter nu vågrätt
- Stabiliteten hos 10 V-nedomvandlaren förbättrad — den viner inte längre under några omständigheter
- Balanseringskretsen för superkondensatorerna omgjord med en enda fyrfaldig operationsförstärkare
- Vissa komponenters fotavtryck ändrade för bättre tillgänglighet

### Konstruktionsfiler

- KiCad-konstruktionsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Kopplingsschema (PDF): [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Version 0.5.0

HALPI2:s andra produktionsversion med mindre rättningar på bärkortet. Kortets funktion är densamma som i version 0.4.0.

Ändringar:

- Mindre fel i texttrycket rättade
- 3,3 V-kopparytor borttagna från undersidan intill monteringsstrukturerna
- Lödmuttrar tillagda för enklare montering av HAT-kort
- Lödmuttrar tillagda för säkrare montering av Compute Module
- Byglarnas stiftlister återförda till hålmontage (THT) för bättre mekanisk hållfasthet
- Egen +5 V-indikeringslysdiod tillagd
- Balanseringen av superkondensatorerna mildrad
- Byglarnas stiftlister omgrupperade för bättre användbarhet

### Konstruktionsfiler

- KiCad-konstruktionsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Kopplingsschema (PDF): [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- 3D-modell av kapslingen: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (samma som i version 0.4.0)

## Version 0.4.0

HALPI2:s första publika version.

### Konstruktionsfiler

- KiCad-konstruktionsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Kopplingsschema (PDF): [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- 3D-modell av kapslingen: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

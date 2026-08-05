---
translated_from: fc7ea79249b080c0f717303d066b9f6ea6d64795
---

# Designfiler og kredsløbsdiagrammer

Denne side indeholder kredsløbsdiagrammer og mekaniske designfiler til HALPI2.

Det elektriske design af HALPI2 er lavet i KiCad. Designfilerne er tilgængelige i [GitHub-arkivet](https://github.com/hatlabs/HALPI2-hardware). Hver udgivet version har et tilsvarende tag i arkivet.

Kredsløbsdiagrammerne stilles for nemheds skyld til rådighed som PDF-filer nedenfor. Print-layoutene findes kun i GitHub-arkivet.

Mekaniske designfiler stilles i første omgang kun til rådighed for kabinettet. Designet er lavet i Autocad Fusion, men de eksporterede filer i STEP-format kan læses af de fleste CAD-programmer.

## Version 0.6.1

En patch-udgivelse, der retter forhold omkring signalintegritet og jordforbindelse, som blev fundet under produktionstest.

Ændringer:

- Tilføj en clockoscillator til NVMe SUSCLK for at rette kompatibilitetsproblemer med visse NVMe SSD'er
- Tilføj manglende kondensatorer til USB3-hubbens RX-differentialpar
- Sørg for jordforbindelse ved hvert monteringspunkt

### Designfiler

- KiCad-designfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Kredsløbsdiagram som PDF: [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Version 0.6.0

Den tredje produktionsudgivelse af HALPI2 med flere mindre rettelser på bærekortet. Kortets funktioner er de samme som i version 0.5.0.

Ændringer:

- Udgangen på 3,3 V-skinnen slås nu til og fra af controlleren i stedet for at være permanent tændt
- Tilføj testpunkter for bedre produktionstest
- Omlæg HDMI-, MIPI- og USB3-grænsefladerne for bedre signalintegritet
- Kortets FFC-stik er nu vandrette
- Bedre stabilitet i 10 V-buckomformeren — den hviner ikke længere under nogen omstændigheder
- Superkondensatorernes balanceringskredsløb er genimplementeret med en enkelt firedobbelt operationsforstærker
- Nogle komponent-footprints er ændret for at forbedre tilgængeligheden

### Designfiler

- KiCad-designfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Kredsløbsdiagram som PDF: [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Version 0.5.0

Den anden produktionsudgivelse af HALPI2 med mindre rettelser på bærekortet. Kortets funktionalitet er den samme som i version 0.4.0.

Ændringer:

- Rettet mindre fejl i silketrykket
- Fjernet 3,3 V-kobberflader fra bundlaget ved siden af monteringsstrukturerne
- Tilføj loddemøtrikker, så HAT'er er lettere at montere
- Tilføj loddemøtrikker, så Compute Module sidder mere sikkert
- Skift jumperstiklisterne tilbage til THT for bedre mekanisk styrke
- Tilføj en dedikeret LED for +5 V-forsyningen
- Lempet balancering af superkondensatorerne
- Omorganiser jumperstiklisterne for bedre brugervenlighed

### Designfiler

- KiCad-designfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Kredsløbsdiagram som PDF: [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- 3D-model af kabinettet: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (samme som i version 0.4.0)

## Version 0.4.0

Den første offentlige udgivelse af HALPI2.

### Designfiler

- KiCad-designfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Kredsløbsdiagram som PDF: [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- 3D-model af kabinettet: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

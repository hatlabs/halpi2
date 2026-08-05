---
translated_from: fc7ea79249b080c0f717303d066b9f6ea6d64795
---

# Konstruksjonsfiler og koblingsskjemaer

Denne siden inneholder koblingsskjemaene og de mekaniske konstruksjonsfilene for HALPI2.

Elektronikken i HALPI2 er konstruert i KiCad. Konstruksjonsfilene er tilgjengelige i [GitHub-repositoriet](https://github.com/hatlabs/HALPI2-hardware). Hver utgitt versjon har en tilsvarende tagg i repositoriet.

Koblingsskjemaene er lagt ved som PDF-filer nedenfor for enkelhets skyld. Kretskortlayoutene er bare tilgjengelige i GitHub-repositoriet.

Mekaniske konstruksjonsfiler finnes foreløpig bare for kabinettet. Konstruksjonen er gjort i Autocad Fusion, men eksportfilene i STEP-format kan leses av de fleste CAD-programmer.

## Versjon 0.6.1

En rettelsesutgave med forbedringer av signalintegritet og jording som ble oppdaget under produksjonstestingen.

Endringer:

- Lagt til en klokkeoscillator for NVMe SUSCLK som løser kompatibilitetsproblemer med enkelte NVMe SSD-er
- Lagt til manglende kondensatorer på RX-differensialparene til USB3-huben
- Sørget for jording i hvert monteringspunkt

### Konstruksjonsfiler

- KiCad-konstruksjonsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Koblingsskjema (PDF): [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Versjon 0.6.0

Den tredje produksjonsutgaven av HALPI2, med flere mindre rettelser på bærekortet. Funksjonene på kortet er de samme som i versjon 0.5.0.

Endringer:

- 3,3 V-skinnen slås nå av og på av kontrolleren i stedet for å være permanent på
- Lagt til testpunkter for bedre produksjonstesting
- Lagt om HDMI-, MIPI- og USB3-grensesnittene for bedre signalintegritet
- FFC-kontaktene på kortet ligger nå vannrett
- Forbedret stabiliteten til 10 V-nedomformeren – den piper ikke lenger under noen omstendigheter
- Balanseringskretsen for superkondensatorene bygget om med én enkelt 4-kanals operasjonsforsterker
- Noen komponentfotavtrykk er endret for å bedre tilgjengeligheten

### Konstruksjonsfiler

- KiCad-konstruksjonsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Koblingsskjema (PDF): [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Versjon 0.5.0

Den andre produksjonsutgaven av HALPI2, med mindre rettelser på bærekortet. Funksjonaliteten på kortet er den samme som i versjon 0.4.0.

Endringer:

- Rettet mindre feil i silketrykket
- Fjernet 3,3 V-kobberflater fra undersiden ved siden av monteringsstrukturene
- Lagt til loddemuttere for enklere montering av HAT-er
- Lagt til loddemuttere for sikrere montering av Compute Module
- Ført jumper-pinnelistene tilbake til gjennomhullsmontering (THT) for bedre mekanisk styrke
- Lagt til en egen +5 V-strøm-LED
- Mildnet balanseringen av superkondensatorene
- Omorganisert jumper-pinnelistene for bedre brukervennlighet

### Konstruksjonsfiler

- KiCad-konstruksjonsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Koblingsskjema (PDF): [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- 3D-modell av kabinettet: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (samme som i versjon 0.4.0)

## Versjon 0.4.0

Den første offentlige utgaven av HALPI2.

### Konstruksjonsfiler

- KiCad-konstruksjonsfiler: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Koblingsskjema (PDF): [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- 3D-modell av kabinettet: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

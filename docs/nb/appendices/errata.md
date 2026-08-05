---
translated_from: 930b506809e4abe2b54e4fea058658a9d6d94461
---

# Kjente feil

Denne siden lister opp kjente maskinvareproblemer i ulike versjoner av HALPI2.

## Enheter av versjon 0.4.0

#### Strømtopp ved påslag

Når enheten slås på med helt utladede superkondensatorer, kan startstrømmen et kort øyeblikk nå 1,1 A. Det gjør at enheten nominelt ikke oppfyller NMEA 2000-kravet om maksimalt 1 A inngangsstrøm.

Den høyere startstrømmen enn spesifisert skyldes et vanskelig gjennomskuelig samspill mellom de analoge inngangene på RP2040-mikrokontrolleren og strømbegrensningskretsen.

#### Kobberflate under monteringsknastene

Et 3,3 V-spenningsplan på undersiden av kretskortet strekker seg ut over monteringsknastene. I noen kabinetter har monteringsknastene rester av skarpe «støpegrader» (biter av aluminium fra støpeprosessen). Hvis kanten på en støpegrad trenger gjennom loddemasken på kretskortet, kan den skape en kortslutning mot 3,3 V-planet og hindre at enheten lar seg slå på.

Problemet kan løses ved å legge elektrikertape av PVC oppå monteringsknastene.

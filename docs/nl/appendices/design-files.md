# Ontwerpbestanden en schema's

Op deze pagina vindt u de schema's en de mechanische ontwerpbestanden van de HALPI2.

Het elektrisch ontwerp van de HALPI2 is gemaakt in KiCad. De ontwerpbestanden zijn beschikbaar in de [GitHub-repository](https://github.com/hatlabs/HALPI2-hardware). Elke uitgebrachte versie heeft een bijbehorende tag in de repository.

De schema's staan hieronder voor het gemak als pdf-bestand. De ontwerpen van de printplaatlay-out zijn alleen in de GitHub-repository beschikbaar.

Mechanische ontwerpbestanden zijn in eerste instantie alleen voor de behuizing beschikbaar. Het ontwerp is gemaakt met Autocad Fusion, maar de geëxporteerde bestanden in STEP-formaat zijn leesbaar voor de meeste CAD-software.

## Versie 0.6.1

Een patchrelease met verbeteringen in de signaalintegriteit en de aarding die tijdens het productietesten aan het licht kwamen.

Wijzigingen:

- Klokoscillator voor NVMe SUSCLK toegevoegd om compatibiliteitsproblemen met bepaalde NVMe SSD's te verhelpen
- Ontbrekende condensatoren toegevoegd aan de differentiële RX-paren van de USB3-hub
- Aarding op elk bevestigingspunt

### Ontwerpbestanden

- KiCad-ontwerpbestanden: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Schema in pdf: [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Versie 0.6.0

De derde productierelease van de HALPI2, met nog enkele kleine correcties aan het carrierboard. De functies van het board blijven gelijk aan die van versie 0.5.0.

Wijzigingen:

- De uitgang van de 3,3 V-rail wordt nu door de controller geschakeld in plaats van altijd aan te staan
- Testpunten toegevoegd voor beter testen tijdens de productie
- HDMI-, MIPI- en USB3-interfaces opnieuw gerouteerd voor een betere signaalintegriteit
- De FFC-connectoren op het board zijn nu horizontaal
- Stabiliteit van de 10 V-buckconverter verbeterd — piept onder geen enkele omstandigheid meer
- Balanceerschakeling van de supercondensatoren opnieuw uitgevoerd met één viervoudige opamp
- Enkele componentfootprints gewijzigd voor een betere beschikbaarheid

### Ontwerpbestanden

- KiCad-ontwerpbestanden: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Schema in pdf: [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Versie 0.5.0

De tweede productierelease van de HALPI2, met kleine correcties aan het carrierboard. De functionaliteit van het board blijft gelijk aan die van versie 0.4.0.

Wijzigingen:

- Kleine fouten in de zeefdruk hersteld
- 3,3 V-kopervlakken verwijderd uit de onderste laag naast de bevestigingsconstructies
- Soldeermoeren toegevoegd voor eenvoudiger monteren van HAT's
- Soldeermoeren toegevoegd voor een steviger bevestiging van de Compute Module
- Jumperheaders teruggebracht naar THT voor meer mechanische sterkte
- Aparte +5 V-voedingsled toegevoegd
- Balancering van de supercondensatoren minder strak afgeregeld
- Jumperheaders opnieuw ingedeeld voor een beter gebruiksgemak

### Ontwerpbestanden

- KiCad-ontwerpbestanden: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Schema in pdf: [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- 3D-model van de behuizing: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (gelijk aan versie 0.4.0)

## Versie 0.4.0

De eerste publieke release van de HALPI2.

### Ontwerpbestanden

- KiCad-ontwerpbestanden: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Schema in pdf: [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- 3D-model van de behuizing: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

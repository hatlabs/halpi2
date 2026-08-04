---
translated_from: fc7ea79249b080c0f717303d066b9f6ea6d64795
---

# Suunnittelutiedostot ja kytkentäkaaviot

Tällä sivulla ovat HALPI2:n kytkentäkaaviot ja mekaniikkasuunnittelun tiedostot.

HALPI2:n elektroniikka on suunniteltu KiCadilla. Suunnittelutiedostot ovat saatavilla [GitHub-repositoriossa](https://github.com/hatlabs/HALPI2-hardware). Jokaisella julkaistulla versiolla on repositoriossa vastaava tagi.

Kytkentäkaaviot ovat alla PDF-tiedostoina käytön helpottamiseksi. Piirilevyn layout-suunnitelmat ovat saatavilla vain GitHub-repositoriossa.

Mekaniikkasuunnittelun tiedostot on toistaiseksi julkaistu vain kotelosta. Suunnittelu on tehty Autocad Fusionilla, mutta STEP-muotoiset vientitiedostot aukeavat useimmissa CAD-ohjelmistoissa.

## Versio 0.6.1

Korjausjulkaisu, joka parantaa signaalin eheyttä ja maadoitusta tuotantotestauksessa havaittujen puutteiden perusteella.

Muutokset:

- Lisätty kellogeneraattori NVMe SUSCLK -signaalille, mikä korjaa yhteensopivuusongelmat tiettyjen NVMe SSD -levyjen kanssa
- Lisätty puuttuvat kondensaattorit USB3-hubin RX-differentiaalipareihin
- Maadoitus tuotu jokaiseen kiinnityspisteeseen

### Suunnittelutiedostot

- KiCad-suunnittelutiedostot: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Kytkentäkaavio (PDF): [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Versio 0.6.0

HALPI2:n kolmas tuotantojulkaisu, jossa on pieniä korjauksia emolevyyn. Kortin ominaisuudet ovat samat kuin versiossa 0.5.0.

Muutokset:

- 3,3 V:n lähtöä ohjaa nyt ohjain sen sijaan että se olisi jatkuvasti päällä
- Lisätty testipisteitä tuotantotestauksen parantamiseksi
- HDMI-, MIPI- ja USB3-liitännät reititetty uudelleen signaalin eheyden parantamiseksi
- Kortin FFC-liittimet ovat nyt vaakasuorassa
- Parannettu 10 V:n alentavan hakkurin vakautta — se ei enää vingu missään olosuhteissa
- Superkondensaattorien tasauspiiri toteutettu uudelleen yhdellä neliosaisella operaatiovahvistimella
- Joidenkin komponenttien jalanjälkiä muutettu saatavuuden parantamiseksi

### Suunnittelutiedostot

- KiCad-suunnittelutiedostot: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Kytkentäkaavio (PDF): [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Versio 0.5.0

HALPI2:n toinen tuotantojulkaisu, jossa on pieniä korjauksia emolevyyn. Kortin toiminnallisuus on sama kuin versiossa 0.4.0.

Muutokset:

- Korjattu pieniä silkkipainovirheitä
- Poistettu 3,3 V:n kuparitäytöt alapinnalta kiinnitysrakenteiden vierestä
- Lisätty juotosmutterit HATtien helpompaan kiinnitykseen
- Lisätty juotosmutterit Compute Modulen tukevampaan kiinnitykseen
- Jumpperiliittimet palautettu läpiladottaviksi (THT) mekaanisen lujuuden vuoksi
- Lisätty oma +5 V:n merkkivalo
- Superkondensaattorien tasausta löysennetty
- Jumpperiliittimet järjestetty uudelleen käytettävyyden parantamiseksi

### Suunnittelutiedostot

- KiCad-suunnittelutiedostot: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Kytkentäkaavio (PDF): [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- Kotelon 3D-malli: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (sama kuin versiossa 0.4.0)

## Versio 0.4.0

HALPI2:n ensimmäinen julkinen versio.

### Suunnittelutiedostot

- KiCad-suunnittelutiedostot: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Kytkentäkaavio (PDF): [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- Kotelon 3D-malli: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

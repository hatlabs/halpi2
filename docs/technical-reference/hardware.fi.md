# Laitteiston tekniset tiedot

Tällä sivulla ovat HALPI2:n sähköiset, mekaaniset ja ympäristöä koskevat tekniset tiedot. Toimintaohjeet (asennus, huolto, osien vaihto) löytyvät [Laitteisto-oppaasta](../user-guide/hardware.md). Liitäntöjen protokollatiedot ovat sivulla [Liitännät ja tiedonsiirto](./interfaces.md).

## Tekniset tiedot lyhyesti

| Ominaisuus | Arvo |
|:-----------|:-----|
| Laskentamoduuli | Raspberry Pi CM5 (yhteensopiva CM4:n kanssa) |
| Emolevyn ohjain | RP2040 (Arm Cortex-M0+, kaksiytiminen, 133 MHz) |
| Syöttöjännite | 9–36 V DC (absoluuttinen maksimi 38,6 V, transienttisuojaus 100 V:iin asti) |
| Tehonkulutus | 250 mA joutokäynnillä, 590 mA kuormitettuna (12 V:n syöttö, HaLOS ilman näyttöä) |
| Virranrajoituksen asetukset | 0,9 A tai 2,5 A (valittavissa) |
| Superkondensaattorivarmennus | 4× 25 F / 2,7 V sarjassa (tehollisesti 6,25 F, enintään 10,8 V) |
| Käyttölämpötila | −20 °C … +60 °C |
| Kotelon mitat | 200 × 130 × 60 mm (ilman liittimiä) |
| Kotelon paino | TODO |
| Kotelon materiaali | Jauhemaalattu painevalettu alumiini |
| Kotelointiluokka | IP65 |
| Lisenssi | CERN-OHL-S v2 (laitteisto) |

## Sähköiset tiedot

### Virransyöttö

Virransyöttö hyväksyy laajan tasajännitealueen ja tuottaa säädetyt 5 V:n ja 3,3 V:n jännitteet CM5:lle ja oheislaitteille. Tulosuojaukseen kuuluvat käänteisen napaisuuden suojaus (LM74800), ylijännitteen irtikytkentä 38,6 V:ssa, TVS-rajoitus sekä yhteis- ja eromuotoisten EMI-häiriöiden suodatus.

| Ominaisuus | Arvo |
|:-----------|:-----|
| Suositeltu syöttöjännite | 9–36 V DC |
| Absoluuttinen maksimisyöttöjännite | 38,6 V (jatkuva), 100 V (transientti, TVS-rajoitettu) |
| Suurin syöttövirta | 0,9 A tai 2,5 A (valittava virranrajoitin) |
| Tulosulake | 7 A (vain vikasuojaus) |
| 10 V:n välijännite | nimellisesti 10,25 V (SiC463ED-hakkuri) |
| 5 V:n jännite | 5,1 V / 4 A (TPS566238, syöttää CM5:n ja USB-portit) |
| 3,3 V:n jännite | 3,33 V / 3 A (TPS566238, ohjaimen kytkemä versiosta 0.6.0 alkaen) |
| 3,3 V:n alijännitekatkaisun raja | 4,5 V superkondensaattorijännitettä |
| Varhainen 3,3 V:n LDO | SE8633K2 (ohjaimen ja superkondensaattorien tasauspiirin käynnistykseen) |

### Superkondensaattorivarmennus

Superkondensaattoripankki syöttää varavirtaa hallittuun sammutukseen jännitteen katketessa.

| Ominaisuus | Arvo |
|:-----------|:-----|
| Kokoonpano | 4× 25 F / 2,7 V kennoa sarjassa |
| Tehollinen kapasitanssi | 6,25 F, enintään 10,8 V |
| Tasaus | Aktiivinen tasaus |
| Latausjännitealue | 0–10,8 V (ohjaimen AD-muuntimen valvoma) |
| Käynnistysraja | 8,0 V (säädettävissä firmwaresta) |
| Sammutusraja | 5,5 V (säädettävissä firmwaresta) |

### Virrankulutus

Mitattu 12 V:n syötöllä, Raspberry Pi CM5 ja HaLOSin näytötön levykuva.

| Tilanne | Virranotto |
|:--------|:-----------|
| Järjestelmä joutokäynnillä | n. 250 mA |
| Tyypillinen kuorma | n. 400 mA |
| Huippukuorma | n. 590 mA |

!!! note
    Mittaukset eivät sisällä ulkoisten USB-laitteiden kulutusta. Kukin USB 3.0 -portti voi syöttää enintään 0,93 A, joten järjestelmän kokonaisvirranotto riippuu voimakkaasti kytketyistä oheislaitteista.

## Liittimien nastajärjestykset

### Virransyöttöliitin

Phoenix MC -tyyppi, 3,81 mm:n jako, 2-napainen. Etupaneelin E7T-pyöröliitin kytkeytyy tähän liittimeen.

| Nasta | Toiminto |
|:------|:---------|
| 1 | GND |
| 2 | VIN (9–36 V DC) |

### CAN FD -liitin

Phoenix MC -tyyppi, 3,81 mm:n jako, 4-napainen. Galvaanisesti erotettu.

| Nasta | Toiminto |
|:------|:---------|
| 1 | GND_CAN (erotettu maa) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Päätevastusjumpperi (merkintä "120R") kytkee 120 Ω:n päätevastuksen CAN_H:n ja CAN_L:n väliin.

### RS-485-liitin

Phoenix MC -tyyppi, 3,81 mm:n jako, 5-napainen. Galvaanisesti erotettu.

| Nasta | Toiminto |
|:------|:---------|
| 1 | GND_RS485 (erotettu maa) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Painikeliitin

2×3-nastainen liitin, 2,54 mm:n jako. Kukin painikepari on GND + signaali.

| Nastapari | Toiminto |
|:----------|:---------|
| Power | CM5:n virtapainike (kaksoisnapautus = sammutus, pitkä painallus = pakotettu virrankatkaisu) |
| Reset | RP2040:n laitteistotason nollaus (RUN-nasta) |
| User | Käyttäjän määritettävissä (odottaa firmware-toteutusta) |

### HDMI-liittimet (HDMI0, HDMI1)

20-napaiset vaakasuorat FPC-liittimet, 0,5 mm:n jako (FPC0.5-SMT-20P). Kummallakin kanavalla on ESD-suojaus (RCLAMP0524P) ja virtarajoitettu 5 V:n syöttö (AP2553W6-7).

### MIPI CSI/DSI -liittimet (MIPI0, MIPI1)

22-napaiset vaakasuorat FPC-liittimet, 0,5 mm:n jako. Kummallakin kanavalla on ESD-suojaus (RCLAMP0524P). Yhteensopivia Raspberry Pi:n kamera- ja näyttömoduulien kanssa.

### M.2 NVMe -paikka (PCIe M.2 M-key)

M.2 Socket M NVMe SSD -levyille, tukee kokoja 2230–2280. Liitetty PCIe Gen 2 x1 -väylällä. Sisältää oman SUSCLK-oskillaattorin NVMe:n lepotilayhteensopivuutta varten (lisätty versiossa 0.6.1).

### Tuuletinliittimet (CM5 Fan)

4-napaiset PWM-tuuletinliittimet (HC-1.0-4PLT) emolevyn ylä- ja alapuolella. Kytketty rinnan — käytä vain toista kerrallaan.

| Nasta | Toiminto |
|:------|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0 -portit

| Liitin | Kytkentä | Virtarajoitus |
|:-------|:---------|:--------------|
| USB3-0 | Suoraan CM5:n USB 3.0:aan | 0,93 A (AP22652W6-7) |
| USB3-1-0 | USB3-hubin portti 1 (UPD720210) | 0,93 A |
| USB3-1-1 | USB3-hubin portti 2 | 0,93 A |
| USB3-1-2 | USB3-hubin portti 3 | 0,93 A |

Kaikissa porteissa on ESD-suojaus (RCLAMP0524P) ja ferriittihelmisuodatus.

### Ohjaimen USB-portti (MCU USB)

Micro-USB-liitin, vain USB 2.0 -oheislaitetila. Käytetään RP2040:n firmware-päivityksiin (UF2-flashaus). ESD-suojattu (RCLAMP0524P).

### USB-käynnistysportti (USB Boot)

USB Type-C -liitin, USB 2.0 -oheislaitetila. Kytketty CM5:n USB 2.0 OTG -porttiin USB-massamuistista käynnistämistä varten. ESD-suojattu (RCLAMP0524P).

## 40-nastainen GPIO-liitin (Raspberry Pi GPIO Header)

GPIO-liitin noudattaa Raspberry Pi:n vakiomuotoista 40-nastaista järjestystä. HALPI2:n kortilla olevat oheislaitteet käyttävät seuraavia nastoja:

| GPIO | Nasta | Toiminto | Liitäntä | Jaettu? |
|:-----|:------|:---------|:---------|:--------|
| 2 | 3 | I2C1 SDA | Järjestelmän I2C | Kyllä (osoite 0x6d varattu) |
| 3 | 5 | I2C1 SCL | Järjestelmän I2C | Kyllä (osoite 0x6d varattu) |
| 6 | 31 | SPI0 CS | CAN FD -ohjain | Oma CS — voi toimia vakio-CS-nastojen rinnalla |
| 9 | 21 | SPI0 MISO | CAN FD -ohjain | Jaettu SPI0-väylä |
| 10 | 19 | SPI0 MOSI | CAN FD -ohjain | Jaettu SPI0-väylä |
| 11 | 23 | SPI0 SCLK | CAN FD -ohjain | Jaettu SPI0-väylä |
| 12 | 32 | UART4 TX | RS-485 | Vapaa, jos RS-485 pois käytöstä |
| 13 | 33 | UART4 RX | RS-485 | Vapaa, jos RS-485 pois käytöstä |
| 24 | 18 | RS-485 EN | RS-485 (käsiohjaustila) | Vapaa automaattitilassa |
| 26 | 37 | CAN INT | CAN FD -ohjain | Ei |

Kaikki muut GPIO-nastat ovat käytettävissä HATeille ja käyttäjän sovelluksille. HATtien yhteensopivuudesta ja sisäisten liitäntöjen poistamisesta käytöstä kerrotaan [Laitteisto-oppaassa](../user-guide/hardware.md#hattien-kaytto).

## I2C-laitteet

Järjestelmän I2C-väylällä (I2C1, GPIO 2/3) on seuraavat laitteet:

| Osoite | Laite | Toiminto |
|:-------|:------|:---------|
| 0x4b | TMP112A | Kortin lämpötila-anturi |
| 0x6d | RP2040 | Emolevyn ohjain (orjatilassa) |

Ohjaimen I2C-väylää (I2C0, emolevyn sisäinen) käytetään HDMI:n DDC-liikenteeseen ja MIPI-näyttöjen tiedonsiirtoon, ja siinä on 2,2 kΩ:n ylösvetovastukset.

## Galvaaninen erotus

CAN FD- ja RS-485-liitännät on erotettu galvaanisesti muusta järjestelmästä. Kummallakin liitännällä on oma erotettu virransyöttö (B0505S-1WR3-hakkuri) ja signaalierotus.

| Liitäntä | Signaalierotus | Virransyötön erotus | Erotettu maa |
|:---------|:---------------|:--------------------|:-------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Näin CAN- tai RS-485-verkon viat, maasilmukat ja häiriöt eivät voi vaurioittaa päälaitteistoa tai häiritä sen toimintaa.

## Mekaaniset tiedot

### Kotelo

| Ominaisuus | Arvo |
|:-----------|:-----|
| Materiaali | Jauhemaalattu painevalettu alumiini |
| Mitat | 200 × 130 × 60 mm (ilman liittimiä) |
| Paino | TODO |
| Kotelointiluokka | IP65 |
| Vapaa korkeus emolevyn yläpuolella | 45 mm (mahtuu enintään kaksi päällekkäistä HATtia) |
| Kannen ruuvit | 4× M4×10 uppokanta, PH2 |
| Tiiviste | Kannen tiiviste säänkestävyyttä varten |
| Paineentasaus | Tasausventtiili (ei saa poistaa) |

### Paneelin paikat

Etupaneelissa on valmiit paikat näille:

- 1× E7T-virtaliitin
- 1× NMEA 2000 Micro-C -liitin
- 1× RJ45-ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-antenniliitin (WiFi/Bluetooth)
- 2× SMA-antennipaikkaa (toimitetaan umpitulpilla)
- 1× tasausventtiili
- 3× PG7-läpivientipaikkaa (toimitetaan umpitulpilla)

### Kiinnitys

- Emolevyn kiinnitys: 4× M4×6 ruuvia kotelon pohjaan
- HATtien kiinnitys: 4× M2.5-kierreholkkia (versiosta 0.5.0 alkaen; versiossa 0.4.0 mutterit on asennettava käsin)
- CM5:n kiinnitys: 4× M2.5-juotosmutteria

## Lämmönhallinta

CM5 on kiinnitetty emolevyn alapuolelle. Lämpö siirtyy CM5:n SoC-piiristä ja RP1-piirisarjasta lämmönjohtotyynyjen kautta alumiinikotelon pohjaan, joka toimii jäähdytyselementtinä.

| Komponentti | Lämmönjohtotyynyn paksuus |
|:------------|:--------------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Virransyötön komponentit | 2 mm |

Vakiokotelo jäähtyy passiivisesti ilman tuuletinta. 4-napainen PWM-tuuletinliitin on käytettävissä räätälöityihin koteloihin tai korkean ympäristölämpötilan sovelluksiin.

!!! quote "Aiheeseen liittyvää"
    - **Kytkentäkaaviot ja suunnittelutiedostot:** katso [Suunnittelutiedostot ja kytkentäkaaviot](../appendices/design-files.md)
    - **Virranhallinnan toiminta:** katso [Virransyöttö tarkemmin](./power-supply.md)
    - **Liitäntäprotokollat:** katso [Liitännät ja tiedonsiirto](./interfaces.md)
    - **Ohjain ja I2C-protokolla:** katso [Emolevyn ohjain](./controller.md)
    - **Fyysinen asennus:** katso [Laitteisto-opas](../user-guide/hardware.md)

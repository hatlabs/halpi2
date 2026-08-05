---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Hardwarereference

Denne side indeholder de elektriske, mekaniske og miljømæssige specifikationer for HALPI2. Vejledning i fremgangsmåder (installation, vedligeholdelse, udskiftning) finder du i [Hardwarevejledningen](../user-guide/hardware.md). Detaljer om grænsefladernes protokoller står i [Grænseflader og forbindelser](./interfaces.md).

## Oversigt over specifikationer

| Parameter | Værdi |
|:----------|:------|
| Compute Module | Raspberry Pi CM5 (CM4-kompatibel) |
| Bærekortets controller | RP2040 (Arm Cortex-M0+, to kerner, 133 MHz) |
| Indgangsspænding | 9–36 V DC (absolut maks. 38,6 V, transientbeskyttelse op til 100 V) |
| Strømforbrug | 250 mA i tomgang til 590 mA under belastning (12 V indgang, HaLOS uden skærm) |
| Indstillinger for strømbegrænsning | 0,9 A eller 2,5 A (kan vælges) |
| Superkondensatorbackup | 4× 25 F / 2,7 V i serie (6,25 F effektivt ved maks. 10,8 V) |
| Driftstemperatur | −20 °C … +60 °C |
| Kabinettets mål | 200 × 130 × 60 mm (uden stik) |
| Kabinettets vægt | TODO |
| Kabinettets materiale | Pulverlakeret trykstøbt aluminium |
| Kapslingsklasse | IP65 |
| Licens | CERN-OHL-S v2 (hardware) |

## Elektriske specifikationer

### Strømforsyning

Strømforsyningen accepterer et bredt DC-indgangsområde og leverer regulerede 5 V- og 3,3 V-skinner til CM5 og periferienheder. Indgangsbeskyttelsen omfatter beskyttelse mod omvendt polaritet (LM74800), overspændingsfrakobling ved 38,6 V, TVS-begrænsning og EMI-filtrering af både common mode og differentielle signaler.

| Parameter | Værdi |
|:----------|:------|
| Anbefalet indgangsspænding | 9–36 V DC |
| Absolut maksimal indgangsspænding | 38,6 V (kontinuerligt), 100 V (transient, begrænset af TVS) |
| Maksimal indgangsstrøm | 0,9 A eller 2,5 A (valgbar strømbegrænser) |
| Indgangssikring | 7 A (kun fejlbeskyttelse) |
| 10 V-mellemskinne | 10,25 V nominelt (SiC463ED-buckomformer) |
| 5 V-skinne | 5,1 V / 4 A (TPS566238, forsyner CM5 og USB-portene) |
| 3,3 V-skinne | 3,33 V / 3 A (TPS566238, kan tændes og slukkes af controlleren fra v0.6.0) |
| UVLO-tærskel for 3,3 V | 4,5 V på superkondensatoren |
| Tidlig 3,3 V-LDO | SE8633K2 (til opstart af controlleren og superkondensatorbalanceringen) |

### Superkondensatorbackup

Superkondensatorbanken leverer reservestrøm til en kontrolleret nedlukning ved strømsvigt.

| Parameter | Værdi |
|:----------|:------|
| Opbygning | 4× 25 F / 2,7 V-celler i serie |
| Effektiv kapacitet | 6,25 F ved maksimalt 10,8 V |
| Balancering | Aktiv balancering |
| Ladespændingsområde | 0–10,8 V (overvåges af controllerens ADC) |
| Tændetærskel | 8,0 V (kan konfigureres i firmwaren) |
| Slukketærskel | 5,5 V (kan konfigureres i firmwaren) |

### Strømforbrug

Målt ved 12 V indgangsspænding med et Raspberry Pi CM5, der kører HaLOS-imaget uden skærm (headless).

| Tilstand | Strømforbrug |
|:----------|:-------------|
| Systemet i tomgang | ~250 mA |
| Typisk belastning | ~400 mA |
| Spidsbelastning | ~590 mA |

!!! note
    Disse målinger omfatter ikke forbruget i eksterne USB-enheder. Hver USB 3.0-port kan levere op til 0,93 A, så systemets samlede forbrug afhænger i høj grad af de tilsluttede periferienheder.

## Stikkenes benforbindelser

### Strømindgangsstik

Phoenix MC-type, 3,81 mm benafstand, 2 ben. E7T-stikket på frontpanelet er forbundet til denne stikliste.

| Ben | Funktion |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 V DC) |

### CAN FD-stik

Phoenix MC-type, 3,81 mm benafstand, 4 ben. Galvanisk adskilt.

| Ben | Funktion |
|:----|:---------|
| 1 | GND_CAN (adskilt jord) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Termineringsjumperen (mærket »120R«) aktiverer en termineringsmodstand på 120 Ω mellem CAN_H og CAN_L.

### RS-485-stik

Phoenix MC-type, 3,81 mm benafstand, 5 ben. Galvanisk adskilt.

| Ben | Funktion |
|:----|:---------|
| 1 | GND_RS485 (adskilt jord) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Knapstikliste

2×3-benet stikliste, 2,54 mm benafstand. Hvert knappepar består af GND + signal.

| Benpar | Funktion |
|:---------|:---------|
| Power | Tænd/sluk-knap til CM5 (dobbeltklik = nedlukning, langt tryk = tvungen slukning) |
| Reset | Hardwarereset af RP2040 (RUN-ben) |
| User | Kan konfigureres af brugeren (afventer implementering i firmwaren) |

### HDMI-stik (HDMI0, HDMI1)

20-benede vandrette FPC-stik, 0,5 mm benafstand (FPC0.5-SMT-20P). Hver kanal har ESD-beskyttelse (RCLAMP0524P) og strømbegrænset 5 V-forsyning (AP2553W6-7).

### MIPI CSI/DSI-stik (MIPI0, MIPI1)

22-benede vandrette FPC-stik, 0,5 mm benafstand. Hver kanal har ESD-beskyttelse (RCLAMP0524P). Kompatible med kamera- og skærmmoduler fra Raspberry Pi.

### M.2 NVMe-slot (PCIe M.2 M-key)

M.2 Socket M til NVMe SSD'er, understøtter formfaktorerne 2230 til 2280. Tilsluttet via PCIe Gen 2 x1. Indeholder en dedikeret SUSCLK-oscillator, der sikrer kompatibilitet med suspend/resume på NVMe (tilføjet i v0.6.1).

### Blæserstik (CM5 Fan)

4-benede PWM-blæserstik (HC-1.0-4PLT) findes både på over- og undersiden af bærekortet. De er forbundet parallelt — brug kun ét ad gangen.

| Ben | Funktion |
|:----|:---------|
| 1 | +5 V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0-porte

| Stik | Forbindelse | Strømgrænse |
|:----------|:-----------|:-------------|
| USB3-0 | Direkte til CM5'ens USB 3.0 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | USB3-hubbens port 1 (UPD720210) | 0,93 A |
| USB3-1-1 | USB3-hubbens port 2 | 0,93 A |
| USB3-1-2 | USB3-hubbens port 3 | 0,93 A |

Alle porte har ESD-beskyttelse (RCLAMP0524P) og filtrering med ferritperler.

### Controllerens USB-port (MCU USB)

Micro-USB-hunstik, kun USB 2.0 i peripheral-tilstand. Bruges til firmwareopdateringer af RP2040 (UF2-flashning). ESD-beskyttet (RCLAMP0524P).

### USB-boot-port (USB Boot)

USB Type-C-hunstik, USB 2.0 i peripheral-tilstand. Forbundet til CM5'ens USB 2.0 OTG-port, så systemet kan starte fra en USB-lagerenhed. ESD-beskyttet (RCLAMP0524P).

## 40-benet GPIO-stikliste (Raspberry Pi GPIO-stikliste)

GPIO-stiklisten følger Raspberry Pi's standardlayout med 40 ben. Følgende ben bruges af HALPI2's indbyggede periferienheder:

| GPIO | Ben | Funktion | Grænseflade | Delt? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | System-I2C | Ja (adressen 0x6d er reserveret) |
| 3 | 5 | I2C1 SCL | System-I2C | Ja (adressen 0x6d er reserveret) |
| 6 | 31 | SPI0 CS | CAN FD-controller | Særskilt CS — kan sameksistere med standard-CS-benene |
| 9 | 21 | SPI0 MISO | CAN FD-controller | Delt SPI0-bus |
| 10 | 19 | SPI0 MOSI | CAN FD-controller | Delt SPI0-bus |
| 11 | 23 | SPI0 SCLK | CAN FD-controller | Delt SPI0-bus |
| 12 | 32 | UART4 TX | RS-485 | Fri, hvis RS-485 er deaktiveret |
| 13 | 33 | UART4 RX | RS-485 | Fri, hvis RS-485 er deaktiveret |
| 24 | 18 | RS-485 EN | RS-485 (manuel tilstand) | Fri i automatisk tilstand |
| 26 | 37 | CAN INT | CAN FD-controller | Nej |

Alle øvrige GPIO-ben er til rådighed for HAT'er og brugerens egne applikationer. Se [Hardwarevejledningen](../user-guide/hardware.md#brug-af-hater) for detaljer om HAT-kompatibilitet og vejledning i at deaktivere de indbyggede grænseflader.

## I2C-enheder

På system-I2C-bussen (I2C1, GPIO 2/3) sidder følgende enheder:

| Adresse | Enhed | Funktion |
|:--------|:-------|:---------|
| 0x4b | TMP112A | Temperatursensor på kortet |
| 0x6d | RP2040 | Bærekortets controller (secondary-tilstand) |

Controllerens I2C-bus (I2C0, intern på bærekortet) bruges til HDMI DDC og til kommunikation med MIPI-skærme og har pull-up-modstande på 2,2 kΩ.

## Opbygning af den galvaniske adskillelse

CAN FD- og RS-485-grænsefladerne er galvanisk adskilt fra resten af systemet. Hver grænseflade har sin egen adskilte forsyning (B0505S-1WR3 DC-DC-omformer) og sin egen signaladskillelse.

| Grænseflade | Signaladskillelse | Forsyningsadskillelse | Adskilt jord |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Det betyder, at busfejl, jordsløjfer og støj på CAN- eller RS-485-netværkene hverken kan beskadige eller forstyrre hovedsystemet.

## Mekaniske specifikationer

### Kabinet

| Parameter | Værdi |
|:----------|:------|
| Materiale | Pulverlakeret trykstøbt aluminium |
| Mål | 200 × 130 × 60 mm (uden stik) |
| Vægt | TODO |
| Kapslingsklasse | IP65 |
| Indvendig frihøjde over bærekortet | 45 mm (plads til op til 2 stablede HAT'er) |
| Skruer til låget | 4× M4×10 undersænket, PH2-hoved |
| Pakning | Lågpakning, der tætner mod vejrliget |
| Trykudligning | Trykudligningsprop (må ikke fjernes) |

### Positioner på panelet

Frontpanelet har forborede positioner til:

- 1× E7T-strømstik
- 1× NMEA 2000 Micro-C-stik
- 1× RJ45-ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-antennestik (til Wi-Fi/Bluetooth)
- 2× SMA-antennepositioner (leveres med blindpropper)
- 1× trykudligningsprop
- 3× positioner til PG7-kabelforskruninger (leveres med blindpropper)

### Montering

- Montering af bærekortet: 4× M4×6-skruer i kabinettets bund
- Montering af HAT'er: 4× M2,5-gevindindsatser (fra v0.5.0; v0.4.0 kræver, at møtrikkerne monteres manuelt)
- Montering af CM5: 4× M2,5-loddemøtrikker

## Termisk styring

CM5 er monteret på undersiden af bærekortet. Varmen ledes fra CM5'ens SoC og RP1-chipsæt gennem termiske puder til kabinettets bund i aluminium, som fungerer som køleplade.

| Komponent | Tykkelse på termisk pude |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Strømforsyningens komponenter | 2 mm |

Standardkabinettet giver passiv køling uden blæser. Et 4-benet PWM-blæserstik er til rådighed til specialkabinetter eller anvendelser med høj omgivelsestemperatur.


!!! quote "Relaterede oplysninger"
    - **Kredsløbsdiagrammer og designfiler:** Se [Designfiler og kredsløbsdiagrammer](../appendices/design-files.md)
    - **Strømstyringens virkemåde:** Se [Strømforsyningen i detaljer](./power-supply.md)
    - **Grænsefladernes protokoller:** Se [Grænseflader og forbindelser](./interfaces.md)
    - **Controlleren og I2C-protokollen:** Se [Bærekortets controller](./controller.md)
    - **Fysisk installation:** Se [Hardwarevejledning](../user-guide/hardware.md)

---
translated_from: 20e29f3f3d0abb0b55c899b0dec2e915f0574e19
---

# Maskinvarereferanse

Denne siden gir de elektriske, mekaniske og miljømessige spesifikasjonene for HALPI2. For prosedyrer (installasjon, vedlikehold, utskifting) se [Maskinvareveiledning](../user-guide/hardware.md). For detaljer om grensesnittprotokollene se [Grensesnitt og tilkoblingsmuligheter](./interfaces.md).

## Sammendrag av spesifikasjoner

| Parameter | Verdi |
|:----------|:------|
| Compute-modul | Raspberry Pi CM5 (kompatibel med CM4) |
| Kontroller på bærekortet | RP2040 (Arm Cortex-M0+, to kjerner, 133 MHz) |
| Inngangsspenning | 10–32 V DC (absolutt maks 38,6 V, transientbeskyttelse til 100 V) |
| Strømforbruk | 250 mA i tomgang til 590 mA under belastning (12 V inn, HaLOS uten skjerm) |
| Innstillinger for strømbegrensning | 0,9 A eller 2,5 A (valgbart) |
| Reservestrøm fra superkondensatorer | 4× 25 F / 2,7 V i serie (6,25 F effektivt ved maks 10,8 V) |
| Driftstemperatur | −20 °C … +60 °C |
| Mål på kabinettet | 200 × 130 × 60 mm (uten kontakter) |
| Vekt på kabinettet | TODO |
| Materiale i kabinettet | Pulverlakkert støpt aluminium |
| Inntrengningsbeskyttelse | IP65 |
| Lisens | CERN-OHL-S v2 (maskinvare) |

## Elektriske spesifikasjoner

### Strømforsyning

Strømforsyningen tar imot et bredt DC-inngangsområde og leverer regulerte 5 V- og 3,3 V-skinner til CM5-en og eksterne enheter. Inngangsbeskyttelsen omfatter beskyttelse mot omvendt polaritet (LM74800), utkobling ved overspenning på 38,6 V, TVS-klamping og EMI-filtrering for både common mode og differensialmodus.

| Parameter | Verdi |
|:----------|:------|
| Anbefalt inngangsspenning | 10–32 V DC |
| Absolutt maksimal inngangsspenning | 38,6 V (kontinuerlig), 100 V (transient, TVS-begrenset) |
| Maksimal inngangsstrøm | 0,9 A eller 2,5 A (valgbar strømbegrenser) |
| Inngangssikring | 7 A (bare feilbeskyttelse) |
| 10 V mellomskinne | 10,25 V nominelt (SiC463ED buck-omformer) |
| 5 V-skinne | 5,1 V / 4 A (TPS566238, forsyner CM5-en og USB-portene) |
| 3,3 V-skinne | 3,33 V / 3 A (TPS566238, styres av kontrolleren på v0.6.0 og senere) |
| UVLO-terskel for 3,3 V | 4,5 V på superkondensatorene |
| Tidlig 3,3 V-LDO | SE8633K2 (for oppstart av kontrolleren og balanseringen av superkondensatorene) |

### Reservestrøm fra superkondensatorer

Superkondensatorbanken gir reservestrøm til kontrollert nedstenging ved strømbortfall.

| Parameter | Verdi |
|:----------|:------|
| Konfigurasjon | 4× 25 F / 2,7 V-celler i serie |
| Effektiv kapasitet | 6,25 F ved maks 10,8 V |
| Balansering | Aktiv balansering |
| Ladespenningsområde | 0–10,8 V (overvåkes av ADC-en i kontrolleren) |
| Innkoblingsterskel | 8,0 V (kan konfigureres i firmware) |
| Utkoblingsterskel | 5,5 V (kan konfigureres i firmware) |

### Strømforbruk

Målt ved 12 V inngangsspenning med en Raspberry Pi CM5 som kjører HaLOS-systembildet uten skjerm.

| Tilstand | Strømtrekk |
|:----------|:-------------|
| Systemet i tomgang | ~250 mA |
| Typisk belastning | ~400 mA |
| Topplast | ~590 mA |

!!! note
    Disse målingene omfatter ikke forbruket til eksterne USB-enheter. Hver USB 3.0-port kan levere opptil 0,93 A, så det totale strømtrekket til systemet avhenger sterkt av hvilke enheter som er tilkoblet.

## Pinnebelegg for kontaktene

### Strømkontakt

Phoenix MC-type, 3,81 mm senteravstand, 2 pinner. På frontpanelet er E7T-DC-pluggen (barrel) koblet til denne pinnelisten.

| Pinne | Funksjon |
|:----|:---------|
| 1 | GND |
| 2 | VIN (10–32 V DC) |

### CAN FD-kontakt

Phoenix MC-type, 3,81 mm senteravstand, 4 pinner. Galvanisk isolert.

| Pinne | Funksjon |
|:----|:---------|
| 1 | GND_CAN (isolert jord) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Termineringsjumperen (merket «120R») aktiverer en termineringsmotstand på 120 Ω mellom CAN_H og CAN_L.

### RS-485-kontakt

Phoenix MC-type, 3,81 mm senteravstand, 5 pinner. Galvanisk isolert.

| Pinne | Funksjon |
|:----|:---------|
| 1 | GND_RS485 (isolert jord) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Pinneliste for knapper

2×3-pinners pinneliste, 2,54 mm senteravstand. Hvert knappepar består av GND + signal.

| Pinnepar | Funksjon |
|:---------|:---------|
| Power | Strømknapp for CM5 (dobbeltklikk = nedstenging, langt trykk = tvungen avslåing) |
| Reset | Maskinvarereset av RP2040 (RUN-pinnen) |
| User | Kan konfigureres av brukeren (venter på implementering i firmware) |

### HDMI-kontakter (HDMI0, HDMI1)

20-pinners horisontale FPC-kontakter, 0,5 mm senteravstand (FPC0.5-SMT-20P). Hver kanal har ESD-beskyttelse (RCLAMP0524P) og strømbegrenset 5 V-forsyning (AP2553W6-7).

### MIPI CSI/DSI-kontakter (MIPI0, MIPI1)

22-pinners horisontale FPC-kontakter, 0,5 mm senteravstand. Hver kanal har ESD-beskyttelse (RCLAMP0524P). Kompatible med kamera- og skjermmoduler fra Raspberry Pi.

### M.2 NVMe-spor (PCIe M.2 M-key)

M.2 Socket M for NVMe SSD-er, med støtte for formfaktorene 2230 til 2280. Koblet til via PCIe Gen 2 x1. Har en egen SUSCLK-oscillator for kompatibilitet med suspend/resume på NVMe (lagt til i v0.6.1).

### Viftekontakter (CM5 Fan)

4-pinners PWM-viftekontakter (HC-1.0-4PLT) finnes både på oversiden og undersiden av bærekortet. De er koblet parallelt – bruk bare én av gangen.

| Pinne | Funksjon |
|:----|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0-porter

| Kontakt | Tilkobling | Strømgrense |
|:----------|:-----------|:-------------|
| USB3-0 | Direkte til USB 3.0 på CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | USB3-hub, port 1 (UPD720210) | 0,93 A |
| USB3-1-1 | USB3-hub, port 2 | 0,93 A |
| USB3-1-2 | USB3-hub, port 3 | 0,93 A |

Alle portene har ESD-beskyttelse (RCLAMP0524P) og filtrering med ferrittperler.

### USB-port for kontrolleren (MCU USB)

Micro-USB-kontakt, bare USB 2.0 i periferimodus. Brukes til firmwareoppdateringer av RP2040 (flashing av UF2). ESD-beskyttet (RCLAMP0524P).

### USB Boot-port (USB Boot)

USB Type-C-kontakt, USB 2.0 i periferimodus. Koblet til USB 2.0 OTG-porten på CM5-en for oppstart fra USB-masselagring. ESD-beskyttet (RCLAMP0524P).

## 40-pinners GPIO-pinneliste (Raspberry Pi GPIO Header)

GPIO-pinnelisten følger standardoppsettet med 40 pinner fra Raspberry Pi. Følgende pinner brukes av de innebygde funksjonene i HALPI2:

| GPIO | Pinne | Funksjon | Grensesnitt | Delt? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | System-I2C | Ja (adresse 0x6d er reservert) |
| 3 | 5 | I2C1 SCL | System-I2C | Ja (adresse 0x6d er reservert) |
| 6 | 31 | SPI0 CS | CAN FD-kontroller | Egendefinert chip select – kan sameksistere med standard CS-pinner |
| 9 | 21 | SPI0 MISO | CAN FD-kontroller | Delt SPI0-buss |
| 10 | 19 | SPI0 MOSI | CAN FD-kontroller | Delt SPI0-buss |
| 11 | 23 | SPI0 SCLK | CAN FD-kontroller | Delt SPI0-buss |
| 12 | 32 | UART4 TX | RS-485 | Ledig hvis RS-485 er deaktivert |
| 13 | 33 | UART4 RX | RS-485 | Ledig hvis RS-485 er deaktivert |
| 24 | 18 | RS-485 EN | RS-485 (manuell modus) | Ledig i automatisk modus |
| 26 | 37 | CAN INT | CAN FD-kontroller | Nei |

Alle øvrige GPIO-pinner er tilgjengelige for HAT-er og brukerprogrammer. Se [Maskinvareveiledning](../user-guide/hardware.md#bruk-av-hat-er) for detaljer om HAT-kompatibilitet og for hvordan du deaktiverer de innebygde grensesnittene.

## I2C-enheter

System-I2C-bussen (I2C1, GPIO 2/3) har én enhet på kortet:

| Adresse | Enhet | Funksjon |
|:--------|:-------|:---------|
| 0x6d | RP2040 | Kontroller på bærekortet (secondary-modus) |

MIPI- og HDMI-kontaktene bruker separate busser. I2C0 (CM5 SDA0/SCL0) betjener MIPI0. MIPI1 bruker ID_SD/ID_SC-pinnene på CM5-en gjennom 0 Ω-motstander, med pull-up-motstander på 2,2 kΩ. HDMI DDC går fra dedikerte pinner på CM5-en til HDMI-kontaktene.

## Isolasjonsarkitektur

CAN FD- og RS-485-grensesnittene er galvanisk isolert fra resten av systemet. Hvert grensesnitt har uavhengig isolert strømforsyning (B0505S-1WR3 DC-DC-omformer) og signalisolasjon.

| Grensesnitt | Signalisolasjon | Strømisolasjon | Isolert jord |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Det betyr at bussfeil, jordsløyfer og støy på CAN- eller RS-485-nettverkene verken kan skade hovedsystemet eller forstyrre det.

## Mekaniske spesifikasjoner

### Kabinett

| Parameter | Verdi |
|:----------|:------|
| Materiale | Pulverlakkert støpt aluminium |
| Mål | 200 × 130 × 60 mm (uten kontakter) |
| Vekt | TODO |
| IP-klasse | IP65 |
| Innvendig klaring over bærekortet | 45 mm (rom for opptil 2 HAT-er oppå hverandre) |
| Lokkskruer | 4× M4×10 senkeskruer, PH2-hode |
| Pakning | Pakning i lokket for værtetting |
| Trykkutjevning | Trykkutjevningsplugg (må ikke fjernes) |

### Panelposisjoner

Frontpanelet har ferdigborede posisjoner for:

- 1× E7T-strømkontakt
- 1× NMEA 2000 Micro-C-kontakt
- 1× RJ45 Ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-antennekontakt (for WiFi/Bluetooth)
- 2× SMA-antenneposisjoner (leveres med blindplugger)
- 1× trykkutjevningsplugg
- 3× PG7-posisjoner for kabelgjennomføring (leveres med blindplugger)

### Montering

- Montering av bærekortet: 4× M4x6-skruer i bunnen av kabinettet
- Montering av HAT-er: 4× M2.5-gjengeinnsatser (fra v0.5.0; v0.4.0 krever manuell montering av muttere)
- Montering av CM5: 4× M2.5-loddemuttere

## Varmehåndtering

CM5-en er montert på undersiden av bærekortet. Varmen ledes fra SoC-en og RP1-brikkesettet på CM5-en gjennom varmeledende puter til bunnen av aluminiumskabinettet, som fungerer som kjøleribbe.

| Komponent | Tykkelse på varmeledende pute |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Komponenter i strømforsyningen | 2 mm |

Standardkabinettet gir passiv kjøling uten vifte. En 4-pinners PWM-viftekontakt er tilgjengelig for tilpassede kabinetter eller bruk ved høy omgivelsestemperatur.


!!! quote "Relatert informasjon"
    - **Koblingsskjemaer og konstruksjonsfiler:** Se [Konstruksjonsfiler og koblingsskjemaer](../appendices/design-files.md)
    - **Oppførsel ved strømstyring:** Se [Strømforsyningen i detalj](./power-supply.md)
    - **Grensesnittprotokoller:** Se [Grensesnitt og tilkoblingsmuligheter](./interfaces.md)
    - **Kontrolleren og I2C-protokollen:** Se [Bærekortets mikrokontroller](./controller.md)
    - **Fysisk installasjon:** Se [Maskinvareveiledning](../user-guide/hardware.md)

---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Hårdvarureferens

Den här sidan innehåller HALPI2:s elektriska, mekaniska och miljörelaterade specifikationer. För arbetsgångar (installation, underhåll, byte), se [Hårdvaruguiden](../user-guide/hardware.md). För detaljer om gränssnittens protokoll, se [Gränssnitt och anslutningar](./interfaces.md).

## Specifikationer i korthet

| Parameter | Värde |
|:----------|:------|
| Beräkningsmodul | Raspberry Pi CM5 (kompatibel med CM4) |
| Bärkortets styrkrets | RP2040 (Arm Cortex-M0+, två kärnor, 133 MHz) |
| Inspänning | 9–36 V DC (absolut max 38,6 V, transientskydd upp till 100 V) |
| Effektförbrukning | 250 mA i vila till 590 mA under belastning (12 V ingång, HaLOS utan skärm) |
| Inställningar för strömbegränsning | 0,9 A eller 2,5 A (valbart) |
| Backup med superkondensatorer | 4× 25 F / 2,7 V i serie (effektivt 6,25 F vid högst 10,8 V) |
| Driftstemperatur | −20 °C … +60 °C |
| Kapslingens mått | 200 × 130 × 60 mm (utan kontakter) |
| Kapslingens vikt | TODO |
| Kapslingens material | Pulverlackerad pressgjuten aluminium |
| Kapslingsklass | IP65 |
| Licens | CERN-OHL-S v2 (hårdvara) |

## Elektriska specifikationer

### Strömförsörjning

Strömförsörjningen tar emot ett brett likspänningsområde och ger reglerade 5 V- och 3,3 V-skenor till CM5 och kringenheterna. Ingångsskyddet omfattar skydd mot omvänd polaritet (LM74800), överspänningsfrånkoppling vid 38,6 V, TVS-begränsning samt EMI-filtrering för både common mode och differentiella störningar.

| Parameter | Värde |
|:----------|:------|
| Rekommenderad inspänning | 9–36 V DC |
| Absolut högsta inspänning | 38,6 V (kontinuerligt), 100 V (transient, TVS-begränsad) |
| Högsta inström | 0,9 A eller 2,5 A (valbar strömbegränsare) |
| Ingångssäkring | 7 A (endast felskydd) |
| 10 V-mellanskena | nominellt 10,25 V (nedomvandlare SiC463ED) |
| 5 V-skena | 5,1 V / 4 A (TPS566238, matar CM5 och USB-portarna) |
| 3,3 V-skena | 3,33 V / 3 A (TPS566238, styrkretsstyrd från v0.6.0) |
| Underspänningströskel 3,3 V | 4,5 V på superkondensatorerna |
| Tidig 3,3 V-LDO | SE8633K2 (för start av styrkrets och balanseringskrets) |

### Backup med superkondensatorer

Superkondensatorbanken ger backupström för en kontrollerad avstängning vid spänningsbortfall.

| Parameter | Värde |
|:----------|:------|
| Uppbyggnad | 4 celler 25 F / 2,7 V i serie |
| Effektiv kapacitans | 6,25 F vid högst 10,8 V |
| Balansering | Aktiv balansering |
| Laddspänningsområde | 0–10,8 V (övervakas av styrkretsens AD-omvandlare) |
| Påslagströskel | 8,0 V (ställbar i firmwaren) |
| Avstängningströskel | 5,5 V (ställbar i firmwaren) |

### Strömförbrukning

Uppmätt vid 12 V inspänning med en Raspberry Pi CM5 som kör HaLOS-avbilden utan skärm.

| Tillstånd | Strömuttag |
|:----------|:-----------|
| Systemet i vila | ca 250 mA |
| Typisk belastning | ca 400 mA |
| Toppbelastning | ca 590 mA |

!!! note
    Mätvärdena omfattar inte förbrukningen hos externa USB-enheter. Varje USB 3.0-port kan leverera upp till 0,93 A, så systemets totala strömuttag beror i hög grad på anslutna kringenheter.

## Kontakternas stiftlägen

### Kontakt för strömförsörjning

Typ Phoenix MC, delning 3,81 mm, 2-polig. På frontpanelen ansluts E7T-hålkontakten till den här anslutningen.

| Stift | Funktion |
|:------|:---------|
| 1 | GND |
| 2 | VIN (9–36 V DC) |

### CAN FD-kontakt

Typ Phoenix MC, delning 3,81 mm, 4-polig. Galvaniskt isolerad.

| Stift | Funktion |
|:------|:---------|
| 1 | GND_CAN (isolerad jord) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Termineringsbygeln (märkt ”120R”) kopplar in ett termineringsmotstånd på 120 Ω mellan CAN_H och CAN_L.

### RS-485-kontakt

Typ Phoenix MC, delning 3,81 mm, 5-polig. Galvaniskt isolerad.

| Stift | Funktion |
|:------|:---------|
| 1 | GND_RS485 (isolerad jord) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Knappanslutning

2×3-polig stiftlist, delning 2,54 mm. Varje knappar utgörs av GND och en signal.

| Stiftpar | Funktion |
|:---------|:---------|
| Power | CM5:ns strömknapp (dubbelklick = avstängning, långt tryck = framtvingad avstängning) |
| Reset | Hårdvarureset av RP2040 (RUN-stiftet) |
| User | Konfigurerbar av användaren (väntar på implementation i firmwaren) |

### HDMI-kontakter (HDMI0, HDMI1)

20-poliga vågräta FFC-kontakter, delning 0,5 mm (FPC0.5-SMT-20P). Varje kanal har ESD-skydd (RCLAMP0524P) och strömbegränsad 5 V-matning (AP2553W6-7).

### MIPI CSI/DSI-kontakter (MIPI0, MIPI1)

22-poliga vågräta FFC-kontakter, delning 0,5 mm. Varje kanal har ESD-skydd (RCLAMP0524P). Kompatibla med Raspberry Pi:s kamera- och skärmmoduler.

### M.2 NVMe-plats (PCIe M.2 M-key)

M.2 Socket M för NVMe SSD-enheter, stöder formaten 2230 till 2280. Ansluten via PCIe Gen 2 x1. Har en egen SUSCLK-oscillator för kompatibilitet med NVMe-enheters viloläge (tillagd i v0.6.1).

### Fläktanslutningar (CM5 Fan)

4-poliga PWM-fläktanslutningar (HC-1.0-4PLT) finns på bärkortets över- och undersida. De är parallellkopplade — använd bara en åt gången.

| Stift | Funktion |
|:------|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0-portar

| Kontakt | Anslutning | Strömbegränsning |
|:--------|:-----------|:-----------------|
| USB3-0 | Direkt till CM5:ns USB 3.0 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | Port 1 på USB3-hubben (UPD720210) | 0,93 A |
| USB3-1-1 | Port 2 på USB3-hubben | 0,93 A |
| USB3-1-2 | Port 3 på USB3-hubben | 0,93 A |

Alla portar har ESD-skydd (RCLAMP0524P) och filtrering med ferritpärlor.

### Styrkretsens USB-port (MCU USB)

Micro-USB-uttag, endast USB 2.0 i enhetsläge. Används för firmwareuppdatering av RP2040 (UF2-flashning). ESD-skyddad (RCLAMP0524P).

### USB-startport (USB Boot)

USB Type-C-uttag, USB 2.0 i enhetsläge. Ansluten till CM5:ns USB 2.0 OTG-port för start från USB-masslagring. ESD-skyddad (RCLAMP0524P).

## 40-polig GPIO-stiftlist (Raspberry Pi GPIO Header)

GPIO-stiftlisten följer Raspberry Pi:s vanliga 40-poliga utförande. Följande stift används av HALPI2:s inbyggda kringenheter:

| GPIO | Stift | Funktion | Gränssnitt | Delas? |
|:-----|:------|:---------|:-----------|:-------|
| 2 | 3 | I2C1 SDA | Systemets I2C | Ja (adress 0x6d reserverad) |
| 3 | 5 | I2C1 SCL | Systemets I2C | Ja (adress 0x6d reserverad) |
| 6 | 31 | SPI0 CS | CAN FD-styrkrets | Eget kretsval — kan samexistera med standardstiften för CS |
| 9 | 21 | SPI0 MISO | CAN FD-styrkrets | Delad SPI0-buss |
| 10 | 19 | SPI0 MOSI | CAN FD-styrkrets | Delad SPI0-buss |
| 11 | 23 | SPI0 SCLK | CAN FD-styrkrets | Delad SPI0-buss |
| 12 | 32 | UART4 TX | RS-485 | Ledigt om RS-485 är avstängt |
| 13 | 33 | UART4 RX | RS-485 | Ledigt om RS-485 är avstängt |
| 24 | 18 | RS-485 EN | RS-485 (manuellt läge) | Ledigt i automatiskt läge |
| 26 | 37 | CAN INT | CAN FD-styrkrets | Nej |

Alla övriga GPIO-stift är tillgängliga för HAT-kort och egna tillämpningar. [Hårdvaruguiden](../user-guide/hardware.md#att-anvanda-hat-kort) beskriver HAT-kompatibiliteten och hur de inbyggda gränssnitten stängs av.

## I2C-enheter

På systemets I2C-buss (I2C1, GPIO 2/3) sitter följande enheter:

| Adress | Enhet | Funktion |
|:-------|:------|:---------|
| 0x4b | TMP112A | Temperatursensor på kortet |
| 0x6d | RP2040 | Bärkortets styrkrets (slavläge) |

Styrkretsens I2C-buss (I2C0, intern på bärkortet) används för HDMI:s DDC-kommunikation och för MIPI-skärmar, med pull-up-motstånd på 2,2 kΩ.

## Isolationens uppbyggnad

CAN FD- och RS-485-gränssnitten är galvaniskt isolerade från resten av systemet. Varje gränssnitt har egen isolerad matning (DC-DC-omvandlare B0505S-1WR3) och egen signalisolation.

| Gränssnitt | Signalisolation | Matningsisolation | Isolerad jord |
|:-----------|:----------------|:------------------|:--------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Fel på bussen, jordslingor och störningar i CAN- eller RS-485-nätverken kan därför varken skada huvudsystemet eller störa det.

## Mekaniska specifikationer

### Kapsling

| Parameter | Värde |
|:----------|:------|
| Material | Pulverlackerad pressgjuten aluminium |
| Mått | 200 × 130 × 60 mm (utan kontakter) |
| Vikt | TODO |
| IP-klass | IP65 |
| Fri höjd ovanför bärkortet | 45 mm (rymmer upp till två staplade HAT-kort) |
| Lockets skruvar | 4× M4×10 försänkt skalle, PH2 |
| Packning | Lockpackning för väderbeständighet |
| Tryckutjämning | Tryckutjämningsplugg (får inte tas bort) |

### Platser på frontpanelen

Frontpanelen har förborrade platser för:

- 1× E7T-strömkontakt
- 1× NMEA 2000 Micro-C-kontakt
- 1× RJ45-ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-antennkontakt (WiFi/Bluetooth)
- 2× SMA-antennplatser (levereras med blindpluggar)
- 1× tryckutjämningsplugg
- 3× platser för PG7-kabelgenomföring (levereras med blindpluggar)

### Montering

- Montering av bärkortet: 4× M4×6-skruvar i kapslingens botten
- Montering av HAT-kort: 4× M2.5-gänginsatser (från v0.5.0; v0.4.0 kräver att muttrarna sätts för hand)
- Montering av CM5: 4× M2.5-lödmuttrar

## Värmehantering

CM5 sitter på bärkortets undersida. Värmen från CM5:ns SoC och RP1-kretsuppsättning leds via värmeledande dynor till kapslingens aluminiumbotten, som fungerar som kylfläns.

| Komponent | Dynans tjocklek |
|:----------|:----------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Strömförsörjningens komponenter | 2 mm |

Standardkapslingen kyls passivt, utan fläkt. En 4-polig PWM-fläktanslutning finns för egna kapslingar eller tillämpningar med hög omgivningstemperatur.

!!! quote "Relaterad information"
    - **Kopplingsscheman och konstruktionsfiler:** se [Konstruktionsfiler och kopplingsscheman](../appendices/design-files.md)
    - **Strömhanteringens beteende:** se [Strömförsörjningen i detalj](./power-supply.md)
    - **Gränssnittsprotokoll:** se [Gränssnitt och anslutningar](./interfaces.md)
    - **Styrkrets och I2C-protokoll:** se [Bärkortets styrkrets](./controller.md)
    - **Fysisk installation:** se [Hårdvaruguiden](../user-guide/hardware.md)

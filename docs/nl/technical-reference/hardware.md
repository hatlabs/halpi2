---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Hardwarereferentie

Deze pagina bevat de elektrische, mechanische en omgevingsspecificaties van de HALPI2. Voor procedurele informatie (installatie, onderhoud, vervanging) zie de [hardwarehandleiding](../user-guide/hardware.md). Voor details over de interfaceprotocollen zie [Interfaces en connectiviteit](./interfaces.md).

## Overzicht van de specificaties

| Parameter | Waarde |
|:----------|:------|
| Computemodule | Raspberry Pi CM5 (CM4-compatibel) |
| Controller van het carrierboard | RP2040 (Arm Cortex-M0+, dualcore, 133 MHz) |
| Ingangsspanning | 9–36 V DC (absoluut maximum 38,6 V, transiëntbeveiliging tot 100 V) |
| Stroomverbruik | 250 mA in rust tot 590 mA onder belasting (12 V ingang, HaLOS zonder beeldscherm) |
| Instellingen stroombegrenzing | 0,9 A of 2,5 A (instelbaar) |
| Backup met supercondensatoren | 4× 25 F / 2,7 V in serie (6,25 F effectief bij max. 10,8 V) |
| Bedrijfstemperatuur | −20 °C … +60 °C |
| Afmetingen behuizing | 200 × 130 × 60 mm (exclusief connectoren) |
| Gewicht behuizing | TODO |
| Materiaal behuizing | Gepoedercoat spuitgietaluminium |
| Beschermingsgraad | IP65 |
| Licentie | CERN-OHL-S v2 (hardware) |

## Elektrische specificaties

### Voeding

De voeding accepteert een breed DC-ingangsbereik en levert gestabiliseerde rails van 5 V en 3,3 V voor de CM5 en de randapparatuur. De ingangsbeveiliging omvat beveiliging tegen ompoling (LM74800), overspanningsafschakeling bij 38,6 V, TVS-klemming en EMI-filtering voor common mode en differentiaal.

| Parameter | Waarde |
|:----------|:------|
| Aanbevolen ingangsspanning | 9–36 V DC |
| Absolute maximale ingangsspanning | 38,6 V (continu), 100 V (transiënt, begrensd door TVS) |
| Maximale ingangsstroom | 0,9 A of 2,5 A (instelbare stroombegrenzer) |
| Ingangszekering | 7 A (alleen als storingsbeveiliging) |
| Tussenrail van 10 V | 10,25 V nominaal (SiC463ED-buckconverter) |
| 5 V-rail | 5,1 V / 4 A (TPS566238, voedt de CM5 en de USB-poorten) |
| 3,3 V-rail | 3,33 V / 3 A (TPS566238, vanaf v0.6.0+ geschakeld door de controller) |
| UVLO-drempel van de 3,3 V-rail | 4,5 V supercondensator |
| Vroege 3,3 V-LDO | SE8633K2 (voor het opstarten van de controller en de balancer van de supercondensatoren) |

### Backup met supercondensatoren

De bank met supercondensatoren levert backupvoeding om bij spanningsuitval gecontroleerd af te sluiten.

| Parameter | Waarde |
|:----------|:------|
| Configuratie | 4× cellen van 25 F / 2,7 V in serie |
| Effectieve capaciteit | 6,25 F bij maximaal 10,8 V |
| Balancering | Actieve balancering |
| Laadspanningsbereik | 0–10,8 V (bewaakt door de ADC van de controller) |
| Inschakeldrempel | 8,0 V (instelbaar in de firmware) |
| Uitschakeldrempel | 5,5 V (instelbaar in de firmware) |

### Stroomverbruik

Gemeten bij 12 V ingangsspanning met een Raspberry Pi CM5 die de HaLOS-image zonder beeldscherm (headless) draait.

| Situatie | Stroomafname |
|:----------|:-------------|
| Systeem in rust | ~250 mA |
| Typische belasting | ~400 mA |
| Piekbelasting | ~590 mA |

!!! note
    Deze metingen zijn exclusief het verbruik van externe USB-apparaten. Elke USB 3.0-poort kan tot 0,93 A leveren, dus de totale stroomafname van het systeem hangt sterk af van de aangesloten randapparatuur.

## Pinbezetting van de connectoren

### Voedingsingangsconnector

Type Phoenix MC, 3,81 mm steek, 2-polig. Op het frontpaneel sluit de E7T-connector aan op deze pinheader.

| Pin | Functie |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 V DC) |

### CAN FD-connector

Type Phoenix MC, 3,81 mm steek, 4-polig. Galvanisch gescheiden.

| Pin | Functie |
|:----|:---------|
| 1 | GND_CAN (gescheiden massa) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Met de afsluitjumper (opschrift “120R”) schakelt u een afsluitweerstand van 120 Ω tussen CAN_H en CAN_L in.

### RS-485-connector

Type Phoenix MC, 3,81 mm steek, 5-polig. Galvanisch gescheiden.

| Pin | Functie |
|:----|:---------|
| 1 | GND_RS485 (gescheiden massa) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Pinheader voor knoppen

Pinheader van 2×3 pinnen, 2,54 mm steek. Elk knoppenpaar bestaat uit GND + signaal.

| Pinpaar | Functie |
|:---------|:---------|
| Power | Aan/uit-knop van de CM5 (dubbelklik = afsluiten, lang indrukken = geforceerd uitschakelen) |
| Reset | Hardwarereset van de RP2040 (RUN-pin) |
| User | Vrij configureerbaar door de gebruiker (implementatie in de firmware volgt nog) |

### HDMI-connectoren (HDMI0, HDMI1)

Horizontale FPC-connectoren met 20 pinnen, 0,5 mm steek (FPC0.5-SMT-20P). Elk kanaal heeft ESD-beveiliging (RCLAMP0524P) en een stroombegrensde 5 V-voeding (AP2553W6-7).

### MIPI CSI/DSI-connectoren (MIPI0, MIPI1)

Horizontale FPC-connectoren met 22 pinnen, 0,5 mm steek. Elk kanaal heeft ESD-beveiliging (RCLAMP0524P). Compatibel met camera- en beeldschermmodules van de Raspberry Pi.

### M.2-slot voor NVMe (PCIe M.2 M-key)

M.2 Socket M voor NVMe-SSD's, geschikt voor de formaten 2230 tot en met 2280. Aangesloten via PCIe Gen 2 x1. Bevat een eigen SUSCLK-oscillator voor compatibiliteit met suspend/resume van NVMe (toegevoegd in v0.6.1).

### Ventilatorconnectoren (CM5 Fan)

PWM-ventilatorconnectoren met 4 pinnen (HC-1.0-4PLT), aanwezig aan zowel de boven- als de onderzijde van het carrierboard. Ze zijn parallel geschakeld — gebruik er slechts één tegelijk.

| Pin | Functie |
|:----|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0-poorten

| Connector | Verbinding | Stroombegrenzing |
|:----------|:-----------|:-------------|
| USB3-0 | Rechtstreeks naar USB 3.0 van de CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | USB3-hub, poort 1 (UPD720210) | 0,93 A |
| USB3-1-1 | USB3-hub, poort 2 | 0,93 A |
| USB3-1-2 | USB3-hub, poort 3 | 0,93 A |

Alle poorten hebben ESD-beveiliging (RCLAMP0524P) en filtering met ferrietkralen.

### USB-poort van de controller (MCU USB)

Micro-USB-bus, uitsluitend USB 2.0 in peripheral mode. Wordt gebruikt om de firmware van de RP2040 bij te werken (flashen met UF2). Voorzien van ESD-beveiliging (RCLAMP0524P).

### USB-bootpoort (USB Boot)

USB Type-C-bus, USB 2.0 in peripheral mode. Aangesloten op de USB 2.0-OTG-poort van de CM5 om vanaf een USB-massaopslagapparaat op te starten. Voorzien van ESD-beveiliging (RCLAMP0524P).

## 40-pins GPIO-pinheader (Raspberry Pi GPIO Header)

De GPIO-pinheader volgt de standaard 40-pins indeling van de Raspberry Pi. De volgende pinnen worden gebruikt door de randapparatuur op de HALPI2 zelf:

| GPIO | Pin | Functie | Interface | Gedeeld? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | Systeem-I2C | Ja (adres 0x6d gereserveerd) |
| 3 | 5 | I2C1 SCL | Systeem-I2C | Ja (adres 0x6d gereserveerd) |
| 6 | 31 | SPI0 CS | CAN FD-controller | Aangepaste CS — kan samengaan met de standaard CS-pinnen |
| 9 | 21 | SPI0 MISO | CAN FD-controller | Gedeelde SPI0-bus |
| 10 | 19 | SPI0 MOSI | CAN FD-controller | Gedeelde SPI0-bus |
| 11 | 23 | SPI0 SCLK | CAN FD-controller | Gedeelde SPI0-bus |
| 12 | 32 | UART4 TX | RS-485 | Vrij als RS-485 is uitgeschakeld |
| 13 | 33 | UART4 RX | RS-485 | Vrij als RS-485 is uitgeschakeld |
| 24 | 18 | RS-485 EN | RS-485 (handmatige modus) | Vrij in de automatische modus |
| 26 | 37 | CAN INT | CAN FD-controller | Nee |

Alle overige GPIO-pinnen zijn beschikbaar voor HAT's en eigen toepassingen. Zie de [hardwarehandleiding](../user-guide/hardware.md#hats-gebruiken) voor details over de compatibiliteit van HAT's en voor instructies om ingebouwde interfaces uit te schakelen.

## I2C-apparaten

Op de I2C-bus van het systeem (I2C1, GPIO 2/3) zitten de volgende apparaten:

| Adres | Apparaat | Functie |
|:--------|:-------|:---------|
| 0x4b | TMP112A | Temperatuursensor van het carrierboard |
| 0x6d | RP2040 | Controller van het carrierboard (secondary-modus) |

De I2C-bus van de controller (I2C0, intern op het carrierboard) wordt gebruikt voor HDMI DDC en de communicatie met MIPI-beeldschermen, met pull-ups van 2,2 kΩ.

## Isolatiearchitectuur

De CAN FD- en RS-485-interfaces zijn galvanisch gescheiden van de rest van het systeem. Elke interface heeft een eigen gescheiden voeding (DC-DC-converter B0505S-1WR3) en signaalscheiding.

| Interface | Signaalscheiding | Voedingsscheiding | Gescheiden massa |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Dit betekent dat busstoringen, aardlussen en ruis op het CAN- of RS-485-netwerk het hoofdsysteem niet kunnen beschadigen of verstoren.

## Mechanische specificaties

### Behuizing

| Parameter | Waarde |
|:----------|:------|
| Materiaal | Gepoedercoat spuitgietaluminium |
| Afmetingen | 200 × 130 × 60 mm (exclusief connectoren) |
| Gewicht | TODO |
| IP-klasse | IP65 |
| Vrije ruimte boven het carrierboard | 45 mm (biedt plaats aan maximaal 2 gestapelde HAT's) |
| Dekselschroeven | 4× M4×10 verzonken, PH2-kop |
| Afdichtingsrubber | Afdichtingsrubber van het deksel voor een weerbestendige afdichting |
| Drukvereffening | Ontluchtingsplug (mag niet worden verwijderd) |

### Paneelposities

Het frontpaneel heeft voorgeboorde posities voor:

- 1× E7T-voedingsconnector
- 1× NMEA 2000-Micro-C-connector
- 1× RJ45-ethernetaansluiting
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-antenneconnector (voor wifi en Bluetooth)
- 2× SMA-antenneposities (geleverd met blindpluggen)
- 1× ontluchtingsplug
- 3× posities voor PG7-kabelwartels (geleverd met blindpluggen)

### Montage

- Montage van het carrierboard: 4× M4×6 schroeven in de bodem van de behuizing
- Montage van HAT's: 4× M2,5-draadinzetstukken (v0.5.0+; bij v0.4.0 moeten de moeren met de hand worden aangebracht)
- Montage van de CM5: 4× M2,5-soldeermoeren

## Warmtebeheer

De CM5 is aan de onderzijde van het carrierboard gemonteerd. De warmte van de SoC en de RP1-chipset van de CM5 wordt via thermische pads afgevoerd naar de aluminium bodem van de behuizing, die als koellichaam dient.

| Component | Dikte thermisch pad |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Componenten van de voeding | 2 mm |

De standaardbehuizing biedt passieve koeling zonder ventilator. Voor eigen behuizingen of toepassingen met een hoge omgevingstemperatuur is een PWM-ventilatorconnector met 4 pinnen beschikbaar.


!!! quote "Gerelateerde informatie"
    - **Schema's en ontwerpbestanden:** zie [Ontwerpbestanden en schema's](../appendices/design-files.md)
    - **Gedrag van het energiebeheer:** zie [Verdieping in de voeding](./power-supply.md)
    - **Interfaceprotocollen:** zie [Interfaces en connectiviteit](./interfaces.md)
    - **Controller en I2C-protocol:** zie [Controller van het carrierboard](./controller.md)
    - **Fysieke installatie:** zie [Hardwarehandleiding](../user-guide/hardware.md)

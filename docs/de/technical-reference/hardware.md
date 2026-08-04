---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Hardware-Referenz

Diese Seite enthält die elektrischen, mechanischen und umweltbezogenen Spezifikationen des HALPI2. Für Arbeitsabläufe (Installation, Wartung, Austausch) siehe das [Hardware-Handbuch](../user-guide/hardware.md). Für Einzelheiten zu den Schnittstellenprotokollen siehe [Schnittstellen und Konnektivität](./interfaces.md).

## Spezifikationen im Überblick

| Parameter | Wert |
|:----------|:-----|
| Rechenmodul | Raspberry Pi CM5 (CM4-kompatibel) |
| Controller der Trägerplatine | RP2040 (Arm Cortex-M0+, zwei Kerne, 133 MHz) |
| Eingangsspannung | 9–36 V DC (absolutes Maximum 38,6 V, Transientenschutz bis 100 V) |
| Leistungsaufnahme | 250 mA im Leerlauf bis 590 mA unter Last (12 V Eingang, HaLOS ohne Bildschirm) |
| Einstellungen der Strombegrenzung | 0,9 A oder 2,5 A (wählbar) |
| Pufferung durch Superkondensatoren | 4× 25 F / 2,7 V in Reihe (effektiv 6,25 F bei maximal 10,8 V) |
| Betriebstemperatur | −20 °C … +60 °C |
| Gehäusemaße | 200 × 130 × 60 mm (ohne Anschlüsse) |
| Gehäusegewicht | TODO |
| Gehäusematerial | Pulverbeschichteter Aluminium-Druckguss |
| Schutzart | IP65 |
| Lizenz | CERN-OHL-S v2 (Hardware) |

## Elektrische Spezifikationen

### Stromversorgung

Die Stromversorgung nimmt einen weiten Gleichspannungsbereich auf und stellt geregelte 5-V- und 3,3-V-Schienen für das CM5 und die Peripherie bereit. Zum Eingangsschutz gehören ein Verpolungsschutz (LM74800), eine Überspannungsabschaltung bei 38,6 V, eine TVS-Begrenzung sowie eine EMV-Filterung für Gleich- und Gegentaktstörungen.

| Parameter | Wert |
|:----------|:-----|
| Empfohlene Eingangsspannung | 9–36 V DC |
| Absolute maximale Eingangsspannung | 38,6 V (dauerhaft), 100 V (transient, TVS-begrenzt) |
| Maximaler Eingangsstrom | 0,9 A oder 2,5 A (wählbare Strombegrenzung) |
| Eingangssicherung | 7 A (nur Fehlerschutz) |
| 10-V-Zwischenschiene | nominell 10,25 V (Abwärtswandler SiC463ED) |
| 5-V-Schiene | 5,1 V / 4 A (TPS566238, versorgt CM5 und USB-Anschlüsse) |
| 3,3-V-Schiene | 3,33 V / 3 A (TPS566238, ab v0.6.0 vom Controller geschaltet) |
| Unterspannungsschwelle 3,3 V | 4,5 V an den Superkondensatoren |
| Früher 3,3-V-LDO | SE8633K2 (für den Start von Controller und Symmetrierschaltung) |

### Pufferung durch Superkondensatoren

Die Superkondensatorbank liefert die Energie für ein geordnetes Herunterfahren bei Spannungsausfall.

| Parameter | Wert |
|:----------|:-----|
| Aufbau | 4 Zellen 25 F / 2,7 V in Reihe |
| Effektive Kapazität | 6,25 F bei maximal 10,8 V |
| Symmetrierung | Aktive Symmetrierung |
| Ladespannungsbereich | 0–10,8 V (vom AD-Wandler des Controllers überwacht) |
| Einschaltschwelle | 8,0 V (in der Firmware einstellbar) |
| Abschaltschwelle | 5,5 V (in der Firmware einstellbar) |

### Stromaufnahme

Gemessen bei 12 V Eingangsspannung mit einem Raspberry Pi CM5 und dem HaLOS-Image ohne Bildschirm.

| Zustand | Stromaufnahme |
|:--------|:--------------|
| System im Leerlauf | ca. 250 mA |
| Typische Last | ca. 400 mA |
| Spitzenlast | ca. 590 mA |

!!! note
    Diese Messwerte enthalten nicht den Verbrauch externer USB-Geräte. Jeder USB-3.0-Anschluss kann bis zu 0,93 A liefern; die Gesamtaufnahme des Systems hängt daher stark von den angeschlossenen Peripheriegeräten ab.

## Steckerbelegungen

### Anschluss der Stromversorgung

Typ Phoenix MC, Raster 3,81 mm, 2-polig. An der Frontplatte wird der E7T-Hohlstecker mit diesem Anschluss verbunden.

| Pin | Funktion |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 V DC) |

### CAN-FD-Anschluss

Typ Phoenix MC, Raster 3,81 mm, 4-polig. Galvanisch getrennt.

| Pin | Funktion |
|:----|:---------|
| 1 | GND_CAN (getrennte Masse) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Der Abschluss-Jumper (Beschriftung „120R") schaltet einen Abschlusswiderstand von 120 Ω zwischen CAN_H und CAN_L.

### RS-485-Anschluss

Typ Phoenix MC, Raster 3,81 mm, 5-polig. Galvanisch getrennt.

| Pin | Funktion |
|:----|:---------|
| 1 | GND_RS485 (getrennte Masse) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Tastenanschluss

2×3-polige Stiftleiste, Raster 2,54 mm. Jedes Tastenpaar besteht aus GND und Signal.

| Pinpaar | Funktion |
|:--------|:---------|
| Power | Ein-/Aus-Taste des CM5 (Doppelklick = Herunterfahren, langer Druck = erzwungenes Abschalten) |
| Reset | Hardware-Reset des RP2040 (RUN-Pin) |
| User | Vom Benutzer konfigurierbar (Umsetzung in der Firmware steht aus) |

### HDMI-Anschlüsse (HDMI0, HDMI1)

20-polige waagerechte FPC-Anschlüsse, Raster 0,5 mm (FPC0.5-SMT-20P). Jeder Kanal besitzt einen ESD-Schutz (RCLAMP0524P) und eine strombegrenzte 5-V-Versorgung (AP2553W6-7).

### MIPI-CSI/DSI-Anschlüsse (MIPI0, MIPI1)

22-polige waagerechte FPC-Anschlüsse, Raster 0,5 mm. Jeder Kanal besitzt einen ESD-Schutz (RCLAMP0524P). Kompatibel mit Kamera- und Displaymodulen von Raspberry Pi.

### M.2-NVMe-Steckplatz (PCIe M.2 M-Key)

M.2 Socket M für NVMe-SSDs, unterstützt die Bauformen 2230 bis 2280. Angebunden über PCIe Gen 2 x1. Enthält einen eigenen SUSCLK-Oszillator für die Kompatibilität mit dem Ruhezustand von NVMe-SSDs (ergänzt in v0.6.1).

### Lüfteranschlüsse (CM5 Fan)

4-polige PWM-Lüfteranschlüsse (HC-1.0-4PLT) auf der Ober- und Unterseite der Trägerplatine. Sie sind parallel geschaltet — verwenden Sie jeweils nur einen.

| Pin | Funktion |
|:----|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB-3.0-Anschlüsse

| Anschluss | Anbindung | Strombegrenzung |
|:----------|:----------|:----------------|
| USB3-0 | Direkt an USB 3.0 des CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | Port 1 des USB3-Hubs (UPD720210) | 0,93 A |
| USB3-1-1 | Port 2 des USB3-Hubs | 0,93 A |
| USB3-1-2 | Port 3 des USB3-Hubs | 0,93 A |

Alle Anschlüsse besitzen einen ESD-Schutz (RCLAMP0524P) und eine Filterung über Ferritperlen.

### USB-Anschluss des Controllers (MCU USB)

Micro-USB-Buchse, ausschließlich USB-2.0-Peripheriebetrieb. Dient der Firmware-Aktualisierung des RP2040 (UF2-Flashen). ESD-geschützt (RCLAMP0524P).

### USB-Startanschluss (USB Boot)

USB-Type-C-Buchse, USB-2.0-Peripheriebetrieb. Verbunden mit dem USB-2.0-OTG-Anschluss des CM5 für den Start von einem USB-Massenspeicher. ESD-geschützt (RCLAMP0524P).

## 40-polige GPIO-Stiftleiste (Raspberry Pi GPIO Header)

Die GPIO-Stiftleiste folgt der 40-poligen Standardbelegung des Raspberry Pi. Die folgenden Pins werden von der Peripherie des HALPI2 belegt:

| GPIO | Pin | Funktion | Schnittstelle | Geteilt? |
|:-----|:----|:---------|:--------------|:---------|
| 2 | 3 | I2C1 SDA | System-I2C | Ja (Adresse 0x6d reserviert) |
| 3 | 5 | I2C1 SCL | System-I2C | Ja (Adresse 0x6d reserviert) |
| 6 | 31 | SPI0 CS | CAN-FD-Controller | Eigenes Chip-Select — kann neben den Standard-CS-Pins bestehen |
| 9 | 21 | SPI0 MISO | CAN-FD-Controller | Gemeinsamer SPI0-Bus |
| 10 | 19 | SPI0 MOSI | CAN-FD-Controller | Gemeinsamer SPI0-Bus |
| 11 | 23 | SPI0 SCLK | CAN-FD-Controller | Gemeinsamer SPI0-Bus |
| 12 | 32 | UART4 TX | RS-485 | Frei, wenn RS-485 deaktiviert ist |
| 13 | 33 | UART4 RX | RS-485 | Frei, wenn RS-485 deaktiviert ist |
| 24 | 18 | RS-485 EN | RS-485 (manueller Modus) | Frei im Automatikmodus |
| 26 | 37 | CAN INT | CAN-FD-Controller | Nein |

Alle übrigen GPIO-Pins stehen für HATs und eigene Anwendungen zur Verfügung. Das [Hardware-Handbuch](../user-guide/hardware.md#hats-verwenden) beschreibt die HAT-Kompatibilität und das Deaktivieren der integrierten Schnittstellen.

## I2C-Geräte

Am System-I2C-Bus (I2C1, GPIO 2/3) hängen die folgenden Geräte:

| Adresse | Gerät | Funktion |
|:--------|:------|:---------|
| 0x4b | TMP112A | Temperatursensor der Platine |
| 0x6d | RP2040 | Controller der Trägerplatine (Slave-Betrieb) |

Der I2C-Bus des Controllers (I2C0, platinenintern) dient der DDC-Kommunikation von HDMI und der Ansteuerung von MIPI-Displays, mit Pull-up-Widerständen von 2,2 kΩ.

## Aufbau der galvanischen Trennung

Die CAN-FD- und RS-485-Schnittstellen sind galvanisch vom übrigen System getrennt. Jede Schnittstelle besitzt eine eigene getrennte Versorgung (DC-DC-Wandler B0505S-1WR3) und eine eigene Signaltrennung.

| Schnittstelle | Signaltrennung | Versorgungstrennung | Getrennte Masse |
|:--------------|:---------------|:--------------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Busfehler, Masseschleifen und Störungen in den CAN- oder RS-485-Netzwerken können das Hauptsystem daher weder beschädigen noch beeinträchtigen.

## Mechanische Spezifikationen

### Gehäuse

| Parameter | Wert |
|:----------|:-----|
| Material | Pulverbeschichteter Aluminium-Druckguss |
| Maße | 200 × 130 × 60 mm (ohne Anschlüsse) |
| Gewicht | TODO |
| Schutzart | IP65 |
| Freie Höhe über der Trägerplatine | 45 mm (Platz für bis zu zwei gestapelte HATs) |
| Deckelschrauben | 4× M4×10 Senkkopf, PH2 |
| Dichtung | Deckeldichtung für die Wetterfestigkeit |
| Druckausgleich | Druckausgleichsstopfen (darf nicht entfernt werden) |

### Positionen an der Frontplatte

Die Frontplatte besitzt vorgebohrte Positionen für:

- 1× E7T-Stromanschluss
- 1× NMEA-2000-Micro-C-Anschluss
- 1× RJ45-Ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× RP-SMA-Antennenanschluss (WLAN/Bluetooth)
- 2× SMA-Antennenpositionen (mit Blindstopfen ausgeliefert)
- 1× Druckausgleichsstopfen
- 3× PG7-Kabelverschraubungspositionen (mit Blindstopfen ausgeliefert)

### Befestigung

- Befestigung der Trägerplatine: 4 Schrauben M4×6 am Gehäuseboden
- Befestigung von HATs: 4 Gewindeeinsätze M2.5 (ab v0.5.0; bei v0.4.0 müssen die Muttern von Hand gesetzt werden)
- Befestigung des CM5: 4 Einpressmuttern M2.5

## Wärmemanagement

Das CM5 sitzt auf der Unterseite der Trägerplatine. Die Wärme des SoC und des RP1-Chipsatzes wird über Wärmeleitpads an den Aluminiumboden des Gehäuses abgeführt, der als Kühlkörper dient.

| Bauteil | Dicke des Wärmeleitpads |
|:--------|:------------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Bauteile der Stromversorgung | 2 mm |

Das Standardgehäuse kühlt passiv, ohne Lüfter. Für eigene Gehäuse oder Anwendungen mit hoher Umgebungstemperatur steht ein 4-poliger PWM-Lüfteranschluss bereit.

!!! quote "Weiterführende Informationen"
    - **Schaltpläne und Konstruktionsdateien:** siehe [Konstruktionsdateien und Schaltpläne](../appendices/design-files.md)
    - **Verhalten der Energieverwaltung:** siehe [Stromversorgung im Detail](./power-supply.md)
    - **Schnittstellenprotokolle:** siehe [Schnittstellen und Konnektivität](./interfaces.md)
    - **Controller und I2C-Protokoll:** siehe [Controller der Trägerplatine](./controller.md)
    - **Physische Installation:** siehe [Hardware-Handbuch](../user-guide/hardware.md)

---
translated_from: e9e4f459212f6282e404954def18772911ead89c
---

# Schnittstellen-Referenz

Diese Seite beschreibt, wie die Schnittstellen des CM5 auf der Trägerplatine des
HALPI2 herausgeführt sind. Zur alltäglichen Nutzung der integrierten CAN-FD- und
RS-485-Anschlüsse siehe das Benutzerhandbuch
[Schnittstellen und Konnektivität](../user-guide/interfaces.md).

## Serielle Schnittstellen (UART)

Das Compute Module 5 erreicht die 40-polige Stiftleiste über seinen
RP1-I/O-Controller, der fünf UARTs bereitstellt (`uart0`–`uart4`). Jeder UART ist
fest mit einem GPIO-Paar verdrahtet — anders als bei früheren Pi-Modellen lassen
sich die Pins nicht umlegen. Die Anmeldekonsole ist ein separater, eigener
Debug-UART (`/dev/ttyAMA10`) und gehört nicht dazu.

| UART | TX / RX | Pins der Stiftleiste | Linux-Gerät | Verfügbarkeit am HALPI2 |
|:-----|:--------|:---------------------|:------------|:------------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Frei. Übliche serielle HAT-Schnittstelle; wird von GNSS-HATs genutzt. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Frei. Dies sind die Pins des HAT-Kennungs-EEPROMs (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Frei. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Vom CAN-FD-Controller belegt (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Von RS-485 belegt. |

### Einen UART aktivieren

Tragen Sie das passende `-pi5`-Overlay in `/boot/firmware/config.txt` ein und
starten Sie das Gerät neu:

```
dtoverlay=uart2-pi5
```

`uart0` wird stattdessen mit `dtparam=uart0=on` aktiviert. (Auf einem CM5 leitet
die Firmware die einfachen `uartN`-Overlays auf ihre `uartN-pi5`-Entsprechungen
um, beide Namen funktionieren also; die `-pi5`-Form wird hier der Klarheit halber
verwendet.)

Die Hardware-Flusssteuerung wird ausdrücklich mit dem Parameter `ctsrts`
aktiviert, und die Overlays können die Freigabeleitung eines
RS-485-Transceivers mit dem Parameter `rs485` direkt ansteuern:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS belegen das nächste GPIO-Paar, das am HALPI2 häufig bereits vergeben ist:

| UART | CTS / RTS | Konflikt mit |
|:-----|:----------|:-------------|
| `uart1` | GPIO2 / 3 | System-I2C-Bus (I2C1) |
| `uart2` | GPIO6 / 7 | Chip-Select des CAN FD |
| `uart3` | GPIO10 / 11 | SPI-Bus des CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` ist daher praktisch nur als reiner TX/RX-Anschluss brauchbar.

### Einen belegten UART freigeben

`uart3` und `uart4` überschneiden sich mit den integrierten CAN-FD- und
RS-485-Schnittstellen:

- **`uart3`** teilt sich den SPI0-Bus mit dem CAN-FD-Controller — GPIO9 ist
  dessen Datenausgang (SDO). Die Nutzung von `uart3` setzt voraus, dass die
  CAN-Schnittstelle deaktiviert und die Hardware geändert wird; auf der
  Standardplatine wird das nicht unterstützt.
- **`uart4`** ist der RS-485-Anschluss. Das Entfernen des RX-Freigabe-Jumpers
  trennt den RS-485-Empfänger von GPIO13 und gibt `uart4` zur allgemeinen
  Nutzung frei. RS-485 steht dann nicht mehr zur Verfügung.

Die Schritte an der Hardware sind unter
[Integrierte Schnittstellen deaktivieren](../user-guide/hardware.md#hats-verwenden)
beschrieben.

### Überprüfung

Prüfen Sie nach dem Neustart, ob der Geräteknoten vorhanden ist und die Pins die
erwartete Funktion tragen:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

Die gewählten Pins sollten ihre UART-Funktion melden (`a2` für `uart1`–`uart4`,
`a4` für `uart0`).

## Weitere Themen

- Einzelheiten zur NMEA-2000-Umsetzung
- USB-3.0-Spezifikationen und Energieverwaltung
- Ethernet und Netzwerk
- Anforderungen an M.2-NVMe-Speicher

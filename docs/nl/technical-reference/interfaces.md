---
translated_from: 9497de10027831b20a1e2278a32df0c12d9a4a39
---

# Interfaces en connectiviteit

Deze pagina beschrijft hoe de interfaces van de CM5 op het HALPI2-carrierboard
beschikbaar zijn gemaakt. Zie voor het dagelijks gebruik van de ingebouwde
CAN FD- en RS-485-poorten de gebruikershandleiding
[Interfaces en connectiviteit](../user-guide/interfaces.md).

## Seriële poorten (UART)

De Compute Module 5 bereikt de 40-pins pinheader via zijn RP1-I/O-controller,
die vijf UART's beschikbaar stelt (`uart0`–`uart4`). Elke UART is bedraad naar
één vast GPIO-paar — anders dan bij eerdere Pi-modellen kunnen de pinnen niet
worden verlegd. De inlogconsole is een aparte, speciale debug-UART
(`/dev/ttyAMA10`) en hoort niet bij deze vijf.

| UART | TX / RX | Headerpinnen | Linux-apparaat | Beschikbaarheid op HALPI2 |
|:-----|:--------|:------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Vrij. Gebruikelijke seriële HAT-poort; gebruikt voor GNSS-HAT's. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Vrij. Dit zijn de pinnen van de HAT-ID-EEPROM (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Vrij. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Gebruikt door de CAN FD-controller (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Gebruikt door RS-485. |

### Een UART inschakelen

Voeg de bijbehorende `-pi5`-overlay toe aan `/boot/firmware/config.txt` en start opnieuw op:

```
dtoverlay=uart2-pi5
```

`uart0` wordt in plaats daarvan ingeschakeld met `dtparam=uart0=on`. (Op een CM5
stuurt de firmware de gewone `uartN`-overlays door naar hun `uartN-pi5`-equivalenten,
dus beide namen werken; hier wordt de `-pi5`-vorm gebruikt voor de duidelijkheid.)

Hardwarematige flowcontrol is optioneel en wordt ingeschakeld met de parameter
`ctsrts`; met de parameter `rs485` kunnen de overlays de enable-lijn van een
RS-485-transceiver rechtstreeks aansturen:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS bezetten het volgende GPIO-paar, dat op de HALPI2 vaak al in gebruik is:

| UART | CTS / RTS | Conflicteert met |
|:-----|:----------|:---------------|
| `uart1` | GPIO2 / 3 | Systeem-I2C-bus (I2C1) |
| `uart2` | GPIO6 / 7 | Chipselect van de CAN FD |
| `uart3` | GPIO10 / 11 | SPI-bus van de CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` is daarom alleen bruikbaar als poort met uitsluitend TX/RX.

### Een bezette UART vrijmaken

`uart3` en `uart4` overlappen met de ingebouwde CAN FD- en RS-485-interfaces:

- **`uart3`** deelt de SPI0-bus met de CAN FD-controller — GPIO9 is de
  data-uitgang (SDO) van de controller. Gebruik van `uart3` vereist het
  uitschakelen van de CAN-interface en een hardwaremodificatie, en wordt op het
  standaardboard niet ondersteund.
- **`uart4`** is de RS-485-poort. Door de RX-enable-jumper van het board te
  verwijderen wordt de RS-485-ontvanger losgekoppeld van GPIO13, waardoor
  `uart4` vrijkomt voor algemeen gebruik. RS-485 is dan niet meer beschikbaar.

Zie [Ingebouwde interfaces uitschakelen](../user-guide/hardware.md#hats-gebruiken) voor de
hardwarestappen.

### Controleren

Controleer na het opnieuw opstarten of het apparaatknooppunt bestaat en of de
pinnen de verwachte functie hebben:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

De geselecteerde pinnen moeten hun UART-functie melden (`a2` voor `uart1`–`uart4`,
`a4` voor `uart0`).

## Overige onderwerpen

- Implementatiedetails van NMEA 2000
- USB 3.0-specificaties en energiebeheer
- Ethernet en netwerken
- Opslagvereisten voor M.2-NVMe

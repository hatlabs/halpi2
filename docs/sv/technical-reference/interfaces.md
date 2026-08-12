---
translated_from: e9e4f459212f6282e404954def18772911ead89c
---

# Gränssnittsreferens

Den här sidan beskriver hur CM5:ns gränssnitt är utförda på HALPI2:s bärkort.
För daglig användning av de inbyggda CAN FD- och RS-485-portarna, se
användarhandboken [Gränssnitt och anslutningar](../user-guide/interfaces.md).

## Serieportar (UART)

Compute Module 5 når den 40-poliga stiftlisten via sin RP1-I/O-styrkrets, som
tillhandahåller fem UART:ar (`uart0`–`uart4`). Varje UART är fast kopplad till
ett bestämt GPIO-par — till skillnad från tidigare Pi-modeller går stiften inte
att flytta. Inloggningskonsolen är en separat, dedikerad felsöknings-UART
(`/dev/ttyAMA10`) och hör inte till dessa.

| UART | TX / RX | Stift på listen | Linux-enhet | Tillgänglighet på HALPI2 |
|:-----|:--------|:----------------|:------------|:-------------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Ledig. Vanlig seriell HAT-port; används av GNSS-HAT-kort. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Ledig. Detta är stiften för HAT-identifieringens EEPROM (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Ledig. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Upptagen av CAN FD-styrkretsen (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Upptagen av RS-485. |

### Aktivera en UART

Lägg till motsvarande `-pi5`-overlay i `/boot/firmware/config.txt` och starta om:

```
dtoverlay=uart2-pi5
```

`uart0` aktiveras i stället med `dtparam=uart0=on`. (På en CM5 styr firmwaren om
de enkla `uartN`-overlayerna till sina `uartN-pi5`-motsvarigheter, så båda namnen
fungerar; `-pi5`-formen används här för tydlighetens skull.)

Hårdvarustyrd flödeskontroll aktiveras uttryckligen med parametern `ctsrts`, och
overlayerna kan styra en RS-485-transceivers aktiveringssignal direkt med
parametern `rs485`:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS upptar nästa GPIO-par, som på HALPI2 ofta redan är i bruk:

| UART | CTS / RTS | Krockar med |
|:-----|:----------|:------------|
| `uart1` | GPIO2 / 3 | Systemets I2C-buss (I2C1) |
| `uart2` | GPIO6 / 7 | CAN FD:s kretsval |
| `uart3` | GPIO10 / 11 | CAN FD:s SPI-buss |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` är därför i praktiken bara användbar som ren TX/RX-port.

### Frigöra en upptagen UART

`uart3` och `uart4` överlappar kortets CAN FD- och RS-485-gränssnitt:

- **`uart3`** delar SPI0-bussen med CAN FD-styrkretsen — GPIO9 är styrkretsens
  datautgång (SDO). Att använda `uart3` kräver att CAN-gränssnittet stängs av
  och att hårdvaran modifieras, och stöds inte på standardkortet.
- **`uart4`** är RS-485-porten. Om kortets bygel för RX-aktivering tas bort
  kopplas RS-485-mottagaren från GPIO13 och `uart4` frigörs för allmän
  användning. RS-485 är då inte tillgängligt.

Stegen på hårdvarusidan beskrivs under
[Stänga av inbyggda gränssnitt](../user-guide/hardware.md#att-anvanda-hat-kort).

### Kontroll

Kontrollera efter omstarten att enhetsnoden finns och att stiften har den
förväntade funktionen:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

De valda stiften ska rapportera sin UART-funktion (`a2` för `uart1`–`uart4`,
`a4` för `uart0`).

## Övriga ämnen

- Detaljer kring NMEA 2000-implementationen
- USB 3.0-specifikationer och strömhantering
- Ethernet och nätverk
- Krav på M.2 NVMe-lagring

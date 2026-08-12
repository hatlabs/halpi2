---
translated_from: e9e4f459212f6282e404954def18772911ead89c
---

# Grensesnittreferanse

Denne siden dokumenterer hvordan grensesnittene til CM5 er ført ut på
HALPI2-bærekortet. For daglig bruk av de innebygde CAN FD- og RS-485-portene, se
brukerveiledningen [Grensesnitt og tilkoblingsmuligheter](../user-guide/interfaces.md).

## Serieporter (UART)

Compute Module 5 når 40-pinners pinnelisten gjennom RP1 I/O-kontrolleren sin,
som gjør fem UART-er tilgjengelige (`uart0`–`uart4`). Hver UART er fast koblet
til ett bestemt GPIO-par – i motsetning til tidligere Pi-modeller kan pinnene
ikke flyttes. Innloggingskonsollen er en egen, dedikert debug-UART
(`/dev/ttyAMA10`) og er ikke en av disse.

| UART | TX / RX | Pinner på pinnelisten | Linux-enhet | Tilgjengelighet på HALPI2 |
|:-----|:--------|:------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Ledig. Vanlig serieport for HAT-er; brukes av GNSS-HAT-er. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Ledig. Dette er pinnene til ID-EEPROM-en på HAT-en (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Ledig. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Brukes av CAN FD-kontrolleren (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Brukes av RS-485. |

### Aktivere en UART

Legg til det tilhørende `-pi5`-overlayet i `/boot/firmware/config.txt` og start på nytt:

```
dtoverlay=uart2-pi5
```

`uart0` aktiveres i stedet med `dtparam=uart0=on`. (På en CM5 sender firmwaren de
vanlige `uartN`-overlayene videre til sine `uartN-pi5`-motparter, så begge navn
fungerer; `-pi5`-formen brukes her for tydelighetens skyld.)

Maskinvarebasert flytkontroll må slås på eksplisitt med parameteren `ctsrts`, og
overlayene kan styre enable-linjen til en RS-485-transceiver direkte med
parameteren `rs485`:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS legger beslag på det neste GPIO-paret, som på HALPI2 ofte allerede er i bruk:

| UART | CTS / RTS | Kolliderer med |
|:-----|:----------|:---------------|
| `uart1` | GPIO2 / 3 | System-I2C-bussen (I2C1) |
| `uart2` | GPIO6 / 7 | Chip select for CAN FD |
| `uart3` | GPIO10 / 11 | SPI-bussen til CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` er derfor bare brukbar som en ren TX/RX-port.

### Frigjøre en opptatt UART

`uart3` og `uart4` overlapper med de innebygde CAN FD- og RS-485-grensesnittene:

- **`uart3`** deler SPI0-bussen med CAN FD-kontrolleren – GPIO9 er datautgangen
  til kontrolleren (SDO). Å bruke `uart3` krever at CAN-grensesnittet slås av og
  at maskinvaren endres, og støttes ikke på standardkortet.
- **`uart4`** er RS-485-porten. Fjerner du RX-enable-jumperen på kortet, kobles
  RS-485-mottakeren fra GPIO13, og `uart4` frigjøres til generell bruk. RS-485
  er da utilgjengelig.

Se [Slå av innebygde grensesnitt](../user-guide/hardware.md#bruk-av-hat-er) for
maskinvaretrinnene.

### Verifisering

Etter omstart bekrefter du at enhetsnoden finnes og at pinnene har den forventede funksjonen:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

De valgte pinnene skal rapportere UART-funksjonen sin (`a2` for `uart1`–`uart4`,
`a4` for `uart0`).

## Andre emner

- Implementasjonsdetaljer for NMEA 2000
- USB 3.0-spesifikasjoner og strømstyring
- Ethernet og nettverk
- Krav til M.2 NVMe-lagring

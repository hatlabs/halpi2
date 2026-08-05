---
translated_from: 9497de10027831b20a1e2278a32df0c12d9a4a39
---

# Grænseflader og forbindelser

Denne side beskriver, hvordan CM5'ens grænseflader er ført ud på HALPI2's
bærekort. Den daglige brug af de indbyggede CAN FD- og RS-485-porte er beskrevet
i brugervejledningen [Grænseflader og forbindelser](../user-guide/interfaces.md).

## Serielle porte (UART)

Compute Module 5 når den 40-benede stikliste via sin RP1-I/O-controller, som
stiller fem UART'er til rådighed (`uart0`–`uart4`). Hver UART er fast forbundet
til ét bestemt GPIO-par — i modsætning til tidligere Pi-modeller kan benene ikke
flyttes. Loginkonsollen er en separat, dedikeret fejlfindings-UART
(`/dev/ttyAMA10`) og hører ikke til disse.

| UART | TX / RX | Ben på stiklisten | Linux-enhed | Tilgængelighed på HALPI2 |
|:-----|:--------|:------------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Ledig. Almindelig seriel HAT-port; bruges af GNSS-HAT'er. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Ledig. Det er benene til HAT-identifikationens EEPROM (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Ledig. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Optaget af CAN FD-controlleren (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Optaget af RS-485. |

### Aktivering af en UART

Tilføj det tilsvarende `-pi5`-overlay i `/boot/firmware/config.txt`, og genstart:

```
dtoverlay=uart2-pi5
```

`uart0` aktiveres i stedet med `dtparam=uart0=on`. (På en CM5 leder firmwaren de
almindelige `uartN`-overlays videre til deres `uartN-pi5`-modstykker, så begge
navne virker; `-pi5`-formen bruges her for tydelighedens skyld.)

Hardwarestyret flowkontrol skal slås til udtrykkeligt med parameteren `ctsrts`,
og overlayene kan styre en RS-485-transceivers enable-linje direkte med
parameteren `rs485`:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS optager det næste GPIO-par, som på HALPI2 ofte allerede er i brug:

| UART | CTS / RTS | Konflikt med |
|:-----|:----------|:-------------|
| `uart1` | GPIO2 / 3 | Systemets I2C-bus (I2C1) |
| `uart2` | GPIO6 / 7 | Chip select til CAN FD |
| `uart3` | GPIO10 / 11 | CAN FD'ens SPI-bus |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` er derfor i praksis kun brugbar som ren TX/RX-port.

### Frigørelse af en optaget UART

`uart3` og `uart4` overlapper kortets indbyggede CAN FD- og RS-485-grænseflader:

- **`uart3`** deler SPI0-bussen med CAN FD-controlleren — GPIO9 er controllerens
  dataudgang (SDO). Brug af `uart3` kræver, at CAN-grænsefladen deaktiveres, og
  at hardwaren ændres, og understøttes ikke på standardkortet.
- **`uart4`** er RS-485-porten. Fjerner du kortets jumper til RX-aktivering,
  kobles RS-485-modtageren fra GPIO13, så `uart4` frigøres til almindelig brug.
  RS-485 er så ikke tilgængelig.

Trinnene på hardwaresiden er beskrevet under
[Deaktivering af indbyggede grænseflader](../user-guide/hardware.md#brug-af-hater).

### Kontrol

Kontrollér efter genstarten, at enhedsnoden findes, og at benene har den
forventede funktion:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

Hvert af de valgte ben bør melde sin UART-funktion (`a2` for `uart1`–`uart4`,
`a4` for `uart0`).

## Andre emner

- Detaljer om implementeringen af NMEA 2000
- USB 3.0-specifikationer og strømstyring
- Ethernet og netværk
- Krav til M.2 NVMe-lagring

# Interfaces and Connectivity

This page documents how the CM5's interfaces are exposed on the HALPI2 carrier
board. For everyday use of the built-in CAN FD and RS-485 ports, see the
[Interfaces and Connectivity](../user-guide/interfaces.md) user guide.

## Serial ports (UART)

The Compute Module 5 reaches the 40-pin header through its RP1 I/O controller,
which exposes five UARTs (`uart0`–`uart4`). Each UART is wired to one fixed GPIO
pair — unlike earlier Pi models, the pins cannot be remapped. The login console
is a separate dedicated debug UART (`/dev/ttyAMA10`) and is not one of these.

| UART | TX / RX | Header pins | Linux device | Availability on HALPI2 |
|:-----|:--------|:------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Free. Conventional HAT serial port; used for GNSS HATs. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Free. These are the HAT ID EEPROM pins (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Free. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Used by the CAN FD controller (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Used by RS-485. |

### Enabling a UART

Add the matching `-pi5` overlay to `/boot/firmware/config.txt` and reboot:

```
dtoverlay=uart2-pi5
```

`uart0` is enabled with `dtparam=uart0=on` instead.

!!! warning "Use the `-pi5` overlays"
    The plain `uartN` overlays target the legacy Broadcom mini-UART and do
    nothing useful on a CM5. Always use the `uartN-pi5` form (`uart1-pi5`,
    `uart2-pi5`, …).

Hardware flow control is opt-in with the `ctsrts` parameter, and the overlays can
drive an RS-485 transceiver's enable line directly with the `rs485` parameter:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS occupy the next GPIO pair, which on HALPI2 is often already in use:

| UART | CTS / RTS | Conflicts with |
|:-----|:----------|:---------------|
| `uart1` | GPIO2 / 3 | System I2C bus (I2C1) |
| `uart2` | GPIO6 / 7 | CAN FD chip-select |
| `uart3` | GPIO10 / 11 | CAN FD SPI bus |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` is therefore practical only as a TX/RX-only port.

### Freeing an occupied UART

`uart3` and `uart4` overlap the onboard CAN FD and RS-485 interfaces:

- **`uart3`** shares the SPI0 bus with the CAN FD controller — GPIO9 is the
  controller's data output (SDO). Using `uart3` requires disabling the CAN
  interface and a hardware modification, and is not supported on the standard
  board.
- **`uart4`** is the RS-485 port. Removing the board's RX-enable jumper
  disconnects the RS-485 receiver from GPIO13, freeing `uart4` for general use.
  RS-485 is then unavailable.

See [Disabling built-in interfaces](../user-guide/hardware.md#using-hats) for the
hardware steps.

### Verifying

After rebooting, confirm the device node exists and the pins carry the expected
function:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

The selected pins should report their UART function (`a2` for `uart1`–`uart4`,
`a4` for `uart0`).

## Other topics

- NMEA 2000 implementation details
- USB 3.0 specifications and power management
- Ethernet and networking
- M.2 NVMe storage requirements

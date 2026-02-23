# Hardware Reference

This page provides the electrical, mechanical and environmental specifications for HALPI2. For procedural information (installation, maintenance, replacement), see the [Hardware Guide](../user-guide/hardware.md). For interface protocol details, see [Interfaces and Connectivity](./interfaces.md).

## Specifications Summary

| Parameter | Value |
|:----------|:------|
| Compute module | Raspberry Pi CM5 (CM4 compatible) |
| Carrier board controller | RP2040 (Arm Cortex-M0+, dual core, 133 MHz) |
| Input voltage | 9–36 VDC (absolute max 38.6V, transient protection to 100V) |
| Power consumption | 250 mA idle to 590 mA under load (12V input, HaLOS headless) |
| Current limit settings | 0.9A or 2.5A (selectable) |
| Supercapacitor backup | 4× 25F / 2.7V in series (6.25F effective at 10.8V max) |
| Operating temperature | −20°C to +60°C |
| Enclosure dimensions | 200 × 130 × 60 mm (excluding connectors) |
| Enclosure weight | TODO |
| Enclosure material | Powder-coated die-cast aluminium |
| Ingress protection | IP65 |
| License | CERN-OHL-S v2 (hardware) |

## Electrical Specifications

### Power Supply

The power supply accepts a wide DC input range and provides regulated 5V and 3.3V rails for the CM5 and peripherals. Input protection includes reverse polarity protection (LM74800), overvoltage disconnect at 38.6V, TVS clamping, and common-mode/differential EMI filtering.

| Parameter | Value |
|:----------|:------|
| Recommended input voltage | 9–36 VDC |
| Absolute maximum input voltage | 38.6V (continuous), 100V (transient, TVS-limited) |
| Maximum input current | 0.9A or 2.5A (selectable current limiter) |
| Input fuse | 7A (fault protection only) |
| 10V intermediate rail | 10.25V nominal (SiC463ED buck converter) |
| 5V rail | 5.1V / 4A (TPS566238, powers CM5 and USB ports) |
| 3.3V rail | 3.33V / 3A (TPS566238, controller-toggled on v0.6.0+) |
| 3.3V UVLO threshold | 4.5V supercap |
| Early 3.3V LDO | SE8633K2 (for controller and supercap balancer startup) |

### Supercapacitor Backup

The supercapacitor bank provides backup power for graceful shutdown during power loss.

| Parameter | Value |
|:----------|:------|
| Configuration | 4× 25F / 2.7V cells in series |
| Effective capacity | 6.25F at 10.8V maximum |
| Balancing | Active balancing |
| Charge voltage range | 0–10.8V (monitored by controller ADC) |
| Power-on threshold | 8.0V (firmware-configurable) |
| Power-off threshold | 5.5V (firmware-configurable) |

### Current Consumption

Measured at 12V input with a Raspberry Pi CM5 running HaLOS headless image.

| Condition | Current draw |
|:----------|:-------------|
| System idle | ~250 mA |
| Typical load | ~400 mA |
| Peak load | ~590 mA |

!!! note
    These measurements exclude external USB device consumption. Each USB 3.0 port can supply up to 0.93A, so total system draw depends heavily on connected peripherals.

## Connector Pinouts

### Power Input Connector

Phoenix MC type, 3.81 mm pitch, 2-pin. On the front panel, the E7T barrel connector connects to this header.

| Pin | Function |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 VDC) |

### CAN FD Connector

Phoenix MC type, 3.81 mm pitch, 4-pin. Galvanically isolated.

| Pin | Function |
|:----|:---------|
| 1 | GND_CAN (isolated ground) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

The termination jumper (label "120R") enables a 120Ω termination resistor between CAN_H and CAN_L.

### RS-485 Connector

Phoenix MC type, 3.81 mm pitch, 5-pin. Galvanically isolated.

| Pin | Function |
|:----|:---------|
| 1 | GND_RS485 (isolated ground) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Button Header

2×3 pin header, 2.54 mm pitch. Each button pair is GND + signal.

| Pin pair | Function |
|:---------|:---------|
| Power | CM5 power button (double-click = shutdown, long press = force off) |
| Reset | RP2040 hardware reset (RUN pin) |
| User | User-configurable (pending firmware implementation) |

### HDMI Connectors (HDMI0, HDMI1)

20-pin horizontal FPC connectors, 0.5 mm pitch (FPC0.5-SMT-20P). Each channel has ESD protection (RCLAMP0524P) and current-limited 5V supply (AP2553W6-7).

### MIPI CSI/DSI Connectors (MIPI0, MIPI1)

22-pin horizontal FPC connectors, 0.5 mm pitch. Each channel has ESD protection (RCLAMP0524P). Compatible with Raspberry Pi camera and display modules.

### M.2 NVMe Slot (PCIe M.2 M-key)

M.2 Socket M for NVMe SSDs, supporting 2230 through 2280 form factors. Connected via PCIe Gen 2 x1. Includes a dedicated SUSCLK oscillator for NVMe suspend/resume compatibility (added in v0.6.1).

### Fan Connectors (CM5 Fan)

4-pin PWM fan connectors (HC-1.0-4PLT) available on both top and bottom sides of the carrier board. Connected in parallel — use only one at a time.

| Pin | Function |
|:----|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### USB 3.0 Ports

| Connector | Connection | Current limit |
|:----------|:-----------|:-------------|
| USB3-0 | Direct to CM5 USB 3.0 | 0.93A (AP22652W6-7) |
| USB3-1-0 | USB3 hub port 1 (UPD720210) | 0.93A |
| USB3-1-1 | USB3 hub port 2 | 0.93A |
| USB3-1-2 | USB3 hub port 3 | 0.93A |

All ports have ESD protection (RCLAMP0524P) and ferrite bead filtering.

### Controller USB Port (MCU USB)

Micro-USB receptacle, USB 2.0 peripheral mode only. Used for RP2040 firmware updates (UF2 flashing). ESD-protected (RCLAMP0524P).

### USB Boot Port (USB Boot)

USB Type-C receptacle, USB 2.0 peripheral mode. Connected to the CM5's USB 2.0 OTG port for USB mass storage booting. ESD-protected (RCLAMP0524P).

## 40-Pin GPIO Header (Raspberry Pi GPIO Header)

The GPIO header follows the standard Raspberry Pi 40-pin layout. The following pins are used by HALPI2's onboard peripherals:

| GPIO | Pin | Function | Interface | Shared? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | System I2C | Yes (address 0x6d reserved) |
| 3 | 5 | I2C1 SCL | System I2C | Yes (address 0x6d reserved) |
| 6 | 31 | SPI0 CS | CAN FD controller | Custom CS — can coexist with standard CS pins |
| 9 | 21 | SPI0 MISO | CAN FD controller | Shared SPI0 bus |
| 10 | 19 | SPI0 MOSI | CAN FD controller | Shared SPI0 bus |
| 11 | 23 | SPI0 SCLK | CAN FD controller | Shared SPI0 bus |
| 12 | 32 | UART4 TX | RS-485 | Free if RS-485 disabled |
| 13 | 33 | UART4 RX | RS-485 | Free if RS-485 disabled |
| 24 | 18 | RS-485 EN | RS-485 (manual mode) | Free in auto mode |
| 26 | 37 | CAN INT | CAN FD controller | No |

All remaining GPIO pins are available for HATs and user applications. See the [Hardware Guide](../user-guide/hardware.md#using-hats) for HAT compatibility details and instructions for disabling built-in interfaces.

## I2C Devices

The system I2C bus (I2C1, GPIO 2/3) hosts the following devices:

| Address | Device | Function |
|:--------|:-------|:---------|
| 0x4b | TMP112A | Board temperature sensor |
| 0x6d | RP2040 | Carrier board controller (secondary mode) |

The controller I2C bus (I2C0, internal to carrier board) is used for HDMI DDC and MIPI display communication, with 2.2kΩ pull-ups.

## Isolation Architecture

The CAN FD and RS-485 interfaces are galvanically isolated from the rest of the system. Each interface has independent isolated power (B0505S-1WR3 DC-DC converter) and signal isolation.

| Interface | Signal isolation | Power isolation | Isolated ground |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7121DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

This means bus faults, ground loops and noise on the CAN or RS-485 networks cannot damage or interfere with the main system.

## Mechanical Specifications

### Enclosure

| Parameter | Value |
|:----------|:------|
| Material | Powder-coated die-cast aluminium |
| Dimensions | 200 × 130 × 60 mm (excluding connectors) |
| Weight | TODO |
| IP rating | IP65 |
| Internal clearance above carrier board | 45 mm (accommodates up to 2 stacked HATs) |
| Lid screws | 4× M4×10 countersunk, PH2 head |
| Gasket | Lid gasket for weather sealing |
| Pressure equalization | Breather plug (must not be removed) |

### Panel Positions

The front panel includes pre-drilled positions for:

- 1× E7T power connector
- 1× NMEA 2000 Micro-C connector
- 1× RJ45 Ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1x RP-SMA antenna connector (for Wi-Fi/Bluetooth)
- 2× SMA antenna positions (shipped with blind plugs)
- 1× Breather plug
- 3× PG7 cable gland positions (shipped with blind plugs)

### Mounting

- Carrier board mounting: 4x M4x6 screw-mounted to enclosure base
- HAT mounting: 4× M2.5 threaded inserts (v0.5.0+; v0.4.0 requires manual nut installation)
- CM5 mounting: 4× M2.5 solder nuts

## Thermal Management

The CM5 is mounted on the underside of the carrier board. Heat is transferred from the CM5's SoC and RP1 chipset through thermal pads to the aluminium enclosure base, which acts as the heatsink.

| Component | Thermal pad thickness |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Power supply components | 2 mm |

The standard enclosure provides passive cooling without a fan. A 4-pin PWM fan connector is available for custom enclosures or high-ambient-temperature applications.


!!! quote "Related Information"
    - **Schematics and design files:** See [Design Files and Schematics](../appendices/design-files.md)
    - **Power management behavior:** See [Power Supply Deep Dive](./power-supply.md)
    - **Interface protocols:** See [Interfaces and Connectivity](./interfaces.md)
    - **Controller and I2C protocol:** See [Carrier Board Controller](./controller.md)
    - **Physical installation:** See [Hardware Guide](../user-guide/hardware.md)

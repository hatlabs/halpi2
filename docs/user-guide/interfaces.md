# Interfaces and Connectivity

## CAN FD / NMEA 2000

HALPI2 features a fully isolated [CAN FD](https://en.wikipedia.org/wiki/CAN_FD) interface that supports both marine [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) networks and automotive or industrial applications. The interface provides high-speed data communication with complete electrical isolation for noise immunity.

### Interface Specifications

The CAN FD interface supports both standard CAN and CAN FD protocols. For NMEA 2000 applications, the interface operates in regular CAN mode at the standard 250 kbps data rate. When used for automotive or industrial applications, the interface can utilize the full CAN FD capabilities with data rates up to 8 Mbps.

The front panel features a Micro-C connector that is compatible with standard NMEA 2000 cabling and components. This allows direct integration with existing marine networks using standard T-connectors and drop cables.

### Power Configuration and Network Loading

HALPI2's impact on NMEA 2000 network power depends on the power configuration chosen. In the standard configuration using external power via the E7T connector, the device requires no power from the NMEA 2000 network, resulting in a Load Equivalency Number (LEN) of 0.

When configured for NMEA 2000 bus power, the device's current draw needs to be limited to 0.9A by the internal current limiter. This corresponds to a LEN rating of 18. When powering HALPI2 via NMEA 2000, the device should be connected to the network backbone close to the power feed cable to minimize voltage drop and ensure reliable operation.

### Hardware Configuration

The carrier board includes a 120Ω termination resistor that can be enabled via a jumper. Device termination should be avoided in NMEA 2000 applications as the standard does not allow it. However, for automotive or industrial applications where point-to-point communication is used, the jumper can be set to enable the termination resistor.

For network diagnostics and troubleshooting, the carrier board features dedicated RX and TX LEDs that indicate network activity. These LEDs provide immediate visual feedback about data transmission and reception, making it easier to diagnose connectivity issues.

### Network Installation

Connection to NMEA 2000 networks is accomplished using a standard T-connector (not supplied) installed on the network backbone and a drop cable connecting the T-connector to HALPI2's Micro-C connector.

### Software Integration

The CAN interface integrates seamlessly with Linux through the SocketCAN framework, appearing as network device `can0`. This standard interface allows the use of common Linux CAN utilities for monitoring and diagnostics. The network interface is preconfigured in the operating system images provided by Hat Labs.

Signal K server integration is preconfigured in the OpenPlotter image, automatically detecting and utilizing the CAN interface for NMEA 2000 data processing. The Signal K server handles PGN decoding and provides web-based access to real-time network data.

### Troubleshooting

Network troubleshooting begins with the RX/TX LEDs on the carrier board. Normal operation shows intermittent LED activity corresponding to network traffic. Missing RX activity may indicate wiring issues or improper termination, while missing TX activity could suggest network conflicts or wiring.

The Linux `candump` command can be used to monitor the CAN bus directly from the command line. This tool provides detailed information about all messages on the bus, allowing for in-depth diagnostics. In its simplest form, you can run:

```bash
candump can0
```

This will display all incoming raw CAN messages in real-time.

The Signal K server dashboard provides additional network monitoring capabilities. It displays real-time NMEA 2000 data rates from the CAN interface. The data browser tool allows viewing of decoded NMEA 2000 data.

> 📖 **Related Information**
>
> - **Power configuration:** See [Getting Started](../getting-started/getting-started.md#permanent-power-installation)
> - **Software setup:** See [Software Guide](./software.md)
> - **Network troubleshooting:** See [Troubleshooting Guide](./troubleshooting.md)


## RS-485 (NMEA 0183)

HALPI2 includes an isolated [RS-485](https://en.wikipedia.org/wiki/RS-485) interface that provides serial communication for marine [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422] networks and industrial applications.

[^rs422]: Technically, NMEA 0183 uses the RS-422 standard, but RS-485 is downwards compatible, allowing HALPI2 to communicate with both RS-422 and RS-485 devices.

### Interface Specifications

The RS-485 transceiver operates at speeds up to 10 Mbps, though typical NMEA 0183 applications use standard baud rates of 4800 or 38400 bps. The interface features galvanic isolation and is compliant with the NMEA 0183 specification, protecting the HALPI2 from ground loops and electrical noise commonly found in marine environments.

The interface is connected internally to UART 4 of the Raspberry Pi, appearing as `/dev/ttyAMA4` in the Linux operating system. This standard serial device can be accessed by any application that supports serial communication, including Signal K server, OpenCPN, and custom software applications.

### Hardware Configuration

The carrier board includes dedicated RX and TX LEDs that indicate communication activity on the RS-485 interface. These LEDs provide immediate visual feedback during installation and troubleshooting, making it easy to verify that data is being transmitted and received correctly.

When operating as a generic RS-485 interface, the device can be configured for either automatic or manual transmit enable mode. In the manual mode, a GPIO pin is used to control the transmit enable signal, allowing software to manage when the interface is in transmit or receive mode. This is required for multi-talker applications in which the interface needs to be in a recessive state when not transmitting. The automatic mode allows the hardware to activate the transmit enable signal when data is sent, simplifying the setup for single-talker applications.

Furthermore, the RS-485 interface supports a half-duplex mode, allowing it to operate in both transmit and receive modes on the same pair of wires.

The interface can also be completely disabled via hardware configuration if UART 4 is needed for other purposes.

### Wiring and Connectivity

The RS-485 interface requires a cable gland or panel connector that must be supplied by the user. One good option is [an SP13 pigtail panel connector](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). The interface is downward compatible with RS-422 signaling used in NMEA 0183, supporting both RS-485 multi-talker networks and RS-422 single-talker-multiple-listener networks. It uses balanced differential pairs, labeled TX+/TX- and RX+/RX-.

### Software Integration

The OpenPlotter image comes preconfigured with the RS-485 interface ready for NMEA 0183 applications. The Signal K server automatically detects the interface and will automatically receive transmitted NMEA 0183 data.

For custom applications, the interface behaves as a standard Linux serial port. Applications can open `/dev/ttyAMA4` and configure the baud rate, data bits, stop bits, and parity as required by the connected equipment. Python, Node.js, and C/C++ applications can all easily access the interface using standard serial communication libraries.

### Common Applications

In marine environments, the RS-485 interface typically connects to GPS receivers, depth sounders, wind instruments, AIS transponders or other devices that use NMEA 0183 protocol. Industrial applications might include connection to PLCs, sensors, and other automation equipment using Modbus RTU or other RS-485 protocols.

The high-speed capability of the interface also supports non-standard applications such as high-rate sensor data collection or custom communication protocols, making HALPI2 suitable for research vessels and specialized monitoring applications.

> 📖 **Related Information**
>
> - **Software configuration:** See [Software Guide](./software.md)
> - **NMEA connections:** See [Marine Electronics Integration](./marine-integration.md)
> - **Troubleshooting:** See [Troubleshooting Guide](./troubleshooting.md)


## Ethernet

HALPI2 includes a Gigabit Ethernet interface that provides high-speed network connectivity for data transfer, remote access, and integration with onboard networks. The ethernet port on the carrier board is a standard RJ45 connector. It is broken out to a panel connector that can be connected to an external Ethernet cable.

## USB

HALPI2 features a total of four onboard USB 3.0 Type A ports, providing high-speed connectivity for a variety of peripherals and devices. One port is routed directly to the CM5 USB 3.0 interface, while the other three are connected via an onboard USB 3 hub. In the standard configuration, two of the ports are broken out to the front panel, while two are available on the carrier board for internal connections.

## HDMI

HALPI2 includes two HDMI 2.0 ports (HDMI0 and HDMI1) for video output. The carrier board provides flexible flat cable (FFC) connectors for both HDMI ports. These are broken out to the front panel using custom FFC cables. The front panel connectors are regular HDMI Type A connectors.

The HALPI2 HDMI output reliably supports dual Full HD (1080p) video streams. 4K video output may work but is not guaranteed.

## MIPI (CSI/DSI)

The carrier board includes two MIPI CSI/DSI connectors for camera and display interfaces. The connectors are 22-pin FFC (Flexible Flat Cable) connectors with 0.5 mm pitch. They should work as-is with newer Raspberry Pi compatible cameras and displays.

Due to waterproofing concerns, use of FFC cables should be limited to internal connections only.

## External Buttons

HALPI2 provides a 2×3 pin header on the carrier board for connecting external buttons. The enclosure does not include built-in buttons, allowing users to customize button placement and types according to their specific needs.

### Button Header Pinout

The carrier board includes a 6-pin header with three labeled button functions:

| Label | Function | Description |
|:------|:---------|:------------|
| Reset | Controller reset | Hardware reset (RP2040 RUN pin) |
| Power | Raspberry Pi power | CM5 power button (PWR_BUT input) |
| User | User-configurable | User-defined event (not yet implemented) |

Each button connection uses two pins: one for the button signal and one for ground. Use normally-open (NO) momentary switches that connect the signal pin to ground when pressed.

### Button Functions

**Reset Button:**
The reset button provides a hardware-level system reset by pulling down the RP2040 RUN pin. This action performs a complete system reset that affects the controller, CM5, and all connected peripherals. The reset button is particularly useful for emergency recovery situations when software shutdown procedures have failed and the system has become unresponsive.

**Power Button:**
The power button connects directly to the CM5 power button input and operates identically to the Raspberry Pi 5 power button. A double-click of the power button requests a graceful shutdown of the system, allowing the operating system to properly close applications and unmount filesystems before powering off. A long press of the power button forces an immediate power-off, which should only be used when the system is unresponsive.

**User Button:**
The user button functionality is currently pending software implementation and will provide user-configurable functionality in future firmware releases. Once implemented, this button will be intended for custom actions and application-specific triggers, allowing users to define their own button behaviors based on their specific operational requirements.

### Button Installation

#### Direct Enclosure Mounting

For direct mounting to the HALPI2 enclosure, use the available 6mm or 13mm holes that are already provided in the enclosure design. Begin by removing the appropriate blind plugs from these holes and install a waterproof button assembly that matches the hole diameter. Connect the button to the carrier board header using an appropriate cable, ensuring proper strain relief and weatherproof sealing at the enclosure penetration.

#### External Panel Mounting

When mounting buttons on a remote control panel, select a suitable location that provides convenient access while maintaining weatherproof integrity. Use cable glands for the cable entry points and connect the buttons using extension cable with 22-26 AWG conductors, keeping the total cable length under 3 meters to maintain signal integrity. For installations exposed to moisture or harsh environments, employ waterproof connectors at junction points to ensure reliable long-term operation.

#### Connection

All button connections to the carrier board should use 2.54mm pitch female header connectors. Ensure proper pin alignment and secure connection to prevent contact issues during operation.

> 📖 **Related Information**
>
> - **Power management:** See [Power Management and Shutdown Procedures](#power-management-and-shutdown-procedures)
> - **Hardware access:** See [Hardware Maintenance](./hardware.md)

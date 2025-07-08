# Quick Start Guide

## Hardware Setup

### Powering

HALPI2 can be powered either using the dedicated E7T power connector (compatible
with Amphenol LTW Ceres Mini) and the
provided power cable, or via NMEA 2000. The power supply should provide a voltage
between 11 and 32 VDC.

#### Powering via E7T Connector

By default, the power input is via the E7T connector. Connect the provided
power cable to the boat electrical system, ensuring the correct polarity.
The power cable needs to be fused with a fuse rated for 3 or 5 A, either with
an inline fuse or in the electrical panel.

#### Powering via NMEA 2000

If you want to power the HALPI2 via NMEA 2000, open the enclosure and connect the
green terminal connector on the NMEA 2000 wiring harness to the carrier board
power connector, replacing the existing terminal block. The NMEA 2000 drop cable
should be close to the power feed cable to avoid excessive voltage drop on the
NMEA 2000 trunk.

#### Input Current Limiting

The default input current limit is set to 0.9 A, which is suitable for most
applications. If you need to increase the limit to supply more power to peripherals
or to speed up the initial charging of the super-capacitors, you can change the
Input Current Limit toggle switch on the carrier board to the 2.5 A position.

When using NMEA 2000, the input current limit must be set to 0.9 A, as
NMEA 2000 devices are not allowed to draw more than 1 A from the bus.

### Mounting

HALPI2 can be wall-mounted using 4 mm screws or M4 bolts. The screw holes can be
found under the enclosure lid. If possible, mount the computer with the
connectors facing downwards to reduce the risk of water ingress.

### Connecting Peripherals

Connecting peripherals is straightforward. Use the appropriate connectors and
cables to link your devices to the HALPI2.

If you need to modify the connector configuration, remove the existing panel
connectors using a socket wrench socket without the ratchet arm - finger
tightening is sufficient for the plastic threads! The large connectors take
a 26 mm socket. The bottom row blind plugs can be removed with a large flat head
screwdriver. The SMA connector nylon bolts can be removed with a 10 mm socket.
When installing new SMA connectors, the brass nut can be finger-tightened using
an 8 mm socket. Use only waterproof SMA connectors that have a wide flange
on the inside of the enclosure to ensure a good seal.

## Software Setup

Hat Labs provides pre-built images for HALPI2, which can be downloaded from
[GitHub](https://github.com/hatlabs/openplotter-halpi/releases). The pre-built
images include the necessary configuration and customizations for the HALPI2
hardware.

All pre-built images have the CAN (NMEA 2000) interface enabled by default, as
network device `can0`. RS-485 (NMEA 0183) is available as `/dev/ttyAMA0`.

### OpenPlotter

OpenPlotter is a Raspberry Pi OS operating system image with useful
additions for marine applications. The pre-installed image is based on the
OpenPlotter Headless edition that enables a WiFi Access Point for easy
configuration and access to the HALPI2.

If you are not using a display, keyboard and a mouse with the HALPI2, you can
connect to the computer either using an Ethernet cable or via the WiFi Access Point.

With either, you can access the HALPI2 computer using VNC or SSH. VNC provides
a remote desktop interface to access the HALPI2 desktop, while SSH
allows you to access the command line interface. You need to download RealVNC's
[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) to use VNC.

Since both the access point and the
default user come with default passwords, it is imperative that the passwords
are changed immediately after the first boot. The process is described in
the [OpenPlotter documentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Raspberry Pi OS and Raspberry Pi OS Lite

If you prefer to use the standard Raspberry Pi OS, you can download the latest
image with HALPI2 support from [the GitHub repository](https://github.com/hatlabs/openplotter-halpi/releases).
Flash the image to the SSD disk using Raspberry Pi Imager. When flashing, you
can apply customizations such as setting the hostname, enabling SSH, and
configuring WiFi.

If you decide to not apply customizations, you need to have a display and
keyboard connected to the HALPI2 to complete the initial setup. You will be asked
to provide a username and password at the first boot.

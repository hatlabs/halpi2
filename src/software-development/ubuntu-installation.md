# Ubuntu Installation

The Ubuntu distribution has an official [ubuntu image for the Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, which is used with HALPI2. 
This guide provides step-by-step instructions to install Ubuntu on your HALPI2 device. These instructions may also work with other debian-based distributions, 
but they have not been tested.

## Prerequisites

Once your chosen ubuntu (or other debian-based) image is installed on the pi, ensure that you have the latest software updates:
```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```
The following packages should then be installed as they are needed for the installation process:
```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools python3-dev python3-pip debhelper-compat dh-virtualenv iw git
```

## Hatlabs Repository
The prebuilt packages for the HALPI2 is provided by Hatlabs, and is available through their apt repository.
To add this repository, you need to run the following commands with root privileges (from `sudo bash`):
```bash
sudo bash
curl -fsSL https://apt.hatlabs.fi/hat-labs-apt-key.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/hatlabs.gpg
cat > /etc/apt/sources.list.d/hatlabs.sources << EOF
Types: deb
URIs: https://apt.hatlabs.fi/
Suites: stable
Components: main
Signed-By: /etc/apt/trusted.gpg.d/hatlabs.gpg
EOF
apt update
exit
```

## HALPI2 Common Firmware

The firmware for common devices on the HALPI2 board can be configured by editing `/boot/firmware/config.txt` and adding the following lines to the `[all]` section:
```text
# --- HALPI2 / Raspberry Pi 5 IO setup ---

# Use antenna path #2 for Wi-Fi/BT
dtparam=ant2

# Enable SPI0 and relocate CS1 to GPIO6 (BCM6) for the CAN controller.
dtoverlay=spi0-2cs,cs1_pin=6

# Attach a Microchip MCP2517FD/2518FD CAN-FD controller to SPI0 Chip-Select 1.
#  - spi0-1        : controller is on SPI0, CS1 (wired to GPIO6 by the overlay above)
#  - interrupt=26  : MCP251xFD INT pin wired to GPIO26
#  - oscillator=40000000 : external crystal is 40 MHz
# Produces a SocketCAN interface (e.g. can0).
dtoverlay=mcp251xfd,spi0-1,interrupt=26,oscillator=40000000

# Enable PL011 UART4.  Creates /dev/ttyAMA4 for NMEA 0183 communication.
dtoverlay=uart4-pi5
```
Then the I2C interface needs to be enabled so that the user space `halpid` daemon can communicate with the power management hardware.
This is done by creating a file `/etc/modules-load.d/i2c-dev.conf` with:
```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```
## CAN Bus (NMEA 2000) Setup
The following command with enable the CAN Bus for NMEA 2000 communication on the HALPI2:
```bash
sudo bash
apt install can-utils
cat > /etc/systemd/network/80-can.network << EOF
[Match]
Name=can*

[CAN]
BitRate=250000
RestartSec=100ms
EOF
chmod 644 /etc/systemd/network/80-can.network
echo 'SUBSYSTEM=="net", KERNEL=="can*", ACTION=="add|change", ATTR{tx_queue_len}="1000"' > /etc/udev/rules.d/80-can.rules
chmod 644 /etc/udev/rules.d/80-can.rules
systemctl enable systemd-networkd
reboot
```

Once the system has rebooted, you can check that the CAN interface is available with either of the commands:
```bash 
ip link show can0
ifconfig can0
```
`
## HALPI2 Daemon
The HALPI2 Daemon is used to monitor and control the HALPI2 carrier board and provide the `halpi` command line tool. 
The `halpid` package is available from the Hatlabs repository, but it currently does not work with ubuntu.  
The following instructions will build and install the HALPI2 Daemon from source.

```bash
sudo bash
cd
mkdir src
cd src
git clone https://github.com/hatlabs/HALPI2-daemon.git
cd HALPI2-daemon
snap install --classic astral-uv
./run build-debian
cd ..
dpkg -i halpid_*_arm64.deb
apt-mark unhold halpid
```

The HALPI2 Daemon should now be running and the `halpi` command available. You can check the status of the daemon with:
```bash 
halpi status
```

## HALPI2 Firmware Installation

Now that the `halpi` command is available, the `hapli2-firmware` package can be installed,m which will flash the latest firmware to the HALPI2 board:
```bash
apt install halpi2-firmware
```

The firmware can be manually flashed with:
```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Signal K Server Setup
The Signal K server is a popular choice for marine data management and can interface with both NMEA 2000 and NMEA 0183 data sources. 
The Signal K server can be installed using npm. The following commands will install the Signal K server and run the initial setup:
```bash
npm i -g signalk-server
signalk-server-setup
```
You can then access the signalK server from a browser at the port that you configured.

### SignalK NMEA 2000 Connection
To setup a NMEA 2000 Connection to the HALPI CAN interface you need to use a SignalK admin account and go to the `Server > Data Connections` section of the menu.
There you can click the `+Add` button and create a connector with the following properties:
```text
          Data Type: NMEA2000
            Enabled: Yes 
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Restart and check the dashboard to see if data is being received.

### SignalK NMEA 0183 Connection
To setup a NMEA 2000 Connection to the HALPI CAN interface you need to use a SignalK admin account and go to the `Server > Data Connections` section of the menu.
There you can click the `+Add` button and create a connector with at least the following properties:
```text
          Data Type: NMEA0183
            Enabled: Yes 
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Restart and check the dashboard to see if data is being received.



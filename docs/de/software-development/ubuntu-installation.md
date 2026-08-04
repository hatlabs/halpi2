# Andere Debian-basierte Distributionen verwenden

!!! warning "Hinweis"
    Hat Labs kann keinen Support für die Installation und Nutzung von Betriebssystemen Dritter leisten. Die folgenden Anleitungen sind ein Entgegenkommen an Anwender, die den HALPI2 mit einer eigenen Softwarezusammenstellung betreiben möchten.

Der HALPI2 läuft mit jedem Betriebssystem, das das Raspberry Pi Compute Module 5 unterstützt. Damit der volle Funktionsumfang der HALPI2-Hardware einschließlich Energieverwaltung und Überwachung zur Verfügung steht, muss das Betriebssystem den HALPI2-Daemon (`halpid`) unterstützen; außerdem sind einige Einstellungen nötig. Auf Debian-basierten Linux-Distributionen sind diese Schritte recht unkompliziert. Dieser Abschnitt beschreibt die Installation von Ubuntu auf dem HALPI2 Schritt für Schritt. Für andere Debian-basierte Distributionen können kleinere Anpassungen erforderlich sein.

Von Ubuntu gibt es ein offizielles [Ubuntu-Image für das Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, das sich mit dem HALPI2 verwenden lässt.

## Voraussetzungen

Sobald das gewählte Ubuntu-Image (oder ein anderes Debian-basiertes Image) auf dem Pi installiert ist, bringen Sie die Software auf den neuesten Stand:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Installieren Sie anschließend die folgenden Pakete, die für die Installation benötigt werden:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat-Labs-Paketquelle

Die vorkompilierten Pakete für den HALPI2 stammen von Hat Labs und stehen in einer apt-Paketquelle bereit. Zum Hinzufügen dieser Paketquelle führen Sie die folgenden Befehle mit Root-Rechten aus (aus `sudo bash` heraus):

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

## Gemeinsame Firmware des HALPI2

Die Firmware der gemeinsamen Komponenten auf der HALPI2-Platine wird konfiguriert, indem Sie `/boot/firmware/config.txt` bearbeiten und die folgenden Zeilen im Abschnitt `[all]` ergänzen:

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

Anschließend muss die I2C-Schnittstelle aktiviert werden, damit der im Benutzerbereich laufende Daemon `halpid` mit der Hardware der Energieverwaltung kommunizieren kann. Legen Sie dazu die Datei `/etc/modules-load.d/i2c-dev.conf` an:

```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```

## Einrichtung des CAN-Busses (NMEA 2000)

Der folgende Befehl aktiviert den CAN-Bus für die NMEA-2000-Kommunikation auf dem HALPI2:

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

Nach dem Neustart können Sie mit einem der folgenden Befehle prüfen, ob die CAN-Schnittstelle verfügbar ist:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-Daemon

Der HALPI2-Daemon überwacht und steuert die Trägerplatine des HALPI2 und stellt das Kommandozeilenwerkzeug `halpi` bereit. Installieren Sie das Paket `halpid` aus der Hat-Labs-Paketquelle:

```bash
sudo apt install halpid
```

Der HALPI2-Daemon sollte nun laufen und der Befehl `halpi` verfügbar sein. Den Status des Daemons prüfen Sie mit:

```bash
halpi status
```

## Installation der HALPI2-Firmware

Da der Befehl `halpi` nun verfügbar ist, lässt sich das Paket `halpi2-firmware` installieren, das die neueste Firmware auf die HALPI2-Platine flasht:

```bash
apt install halpi2-firmware
```

Die Firmware kann auch von Hand geflasht werden:

```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Einrichtung des Signal-K-Servers

Der Signal-K-Server ist eine verbreitete Wahl für die Verwaltung von Schiffsdaten und kann sowohl NMEA-2000- als auch NMEA-0183-Datenquellen einbinden. Er lässt sich mit npm installieren. Die folgenden Befehle installieren den Server und starten die Ersteinrichtung:

```bash
npm i -g signalk-server
signalk-server-setup
```

Anschließend erreichen Sie den Signal-K-Server im Browser über den von Ihnen konfigurierten Port.

### NMEA-2000-Verbindung in Signal K

Für eine NMEA-2000-Verbindung zur CAN-Schnittstelle des HALPI benötigen Sie ein Signal-K-Administratorkonto. Rufen Sie im Menü `Server > Data Connections` auf, klicken Sie auf `+Add` und legen Sie eine Verbindung mit den folgenden Eigenschaften an:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Starten Sie neu und prüfen Sie im Dashboard, ob Daten eintreffen.

### NMEA-0183-Verbindung in Signal K

Auch für eine NMEA-0183-Verbindung benötigen Sie ein Signal-K-Administratorkonto. Rufen Sie im Menü `Server > Data Connections` auf, klicken Sie auf `+Add` und legen Sie eine Verbindung mit mindestens den folgenden Eigenschaften an:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Starten Sie neu und prüfen Sie im Dashboard, ob Daten eintreffen.

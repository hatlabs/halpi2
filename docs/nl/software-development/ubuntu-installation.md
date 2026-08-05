# Andere Debian-distributies gebruiken

!!! warning "Let op"
    Hat Labs kan geen ondersteuning bieden bij het installeren en gebruiken van besturingssystemen van derden. Onderstaande aanwijzingen worden aangeboden als service aan gebruikers die de HALPI2 met een eigen softwareopstelling willen gebruiken.

De HALPI2 draait moeiteloos elk besturingssysteem dat de Raspberry Pi Compute Module 5 ondersteunt. Om de volledige functionaliteit van de HALPI2-hardware te benutten, inclusief energiebeheer en bewaking, moet het besturingssysteem de HALPI2-daemon (`halpid`) ondersteunen en is enige configuratie nodig. Op Debian-gebaseerde Linux-distributies zijn die stappen tamelijk eenvoudig. Dit hoofdstuk beschrijft stap voor stap hoe u Ubuntu op de HALPI2 installeert. Voor andere op Debian gebaseerde distributies zijn mogelijk kleine aanpassingen nodig.

Ubuntu biedt een officiële [Ubuntu-image voor de Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, die met de HALPI2 gebruikt kan worden.

## Vereisten

Zodra de gekozen Ubuntu-image (of een andere op Debian gebaseerde image) op de Pi is geïnstalleerd, zorgt u dat u over de nieuwste software-updates beschikt:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Vervolgens installeert u de volgende pakketten, omdat ze nodig zijn voor het installatieproces:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat Labs-repository

De kant-en-klare pakketten voor de HALPI2 worden geleverd door Hat Labs en zijn beschikbaar via een apt-repository.
Om deze repository toe te voegen, voert u de volgende commando's uit met rootrechten (vanuit `sudo bash`):

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

## Algemene firmware voor de HALPI2

De firmware voor de algemene onderdelen op het HALPI2-board configureert u door `/boot/firmware/config.txt` te bewerken en de volgende regels toe te voegen aan de sectie `[all]`:

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

Daarna moet de I2C-interface worden ingeschakeld, zodat de `halpid`-daemon in de gebruikersruimte met de hardware voor energiebeheer kan communiceren.
Dat doet u door een bestand `/etc/modules-load.d/i2c-dev.conf` aan te maken met:

```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```
## CAN-bus (NMEA 2000) instellen

Met het volgende commando schakelt u de CAN-bus voor NMEA 2000-communicatie op de HALPI2 in:

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

Zodra het systeem opnieuw is opgestart, controleert u met een van de volgende commando's of de CAN-interface beschikbaar is:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-daemon

De HALPI2-daemon bewaakt en bestuurt het carrierboard van de HALPI2 en levert het commandoregelprogramma `halpi`.
Installeer het pakket `halpid` uit de Hat Labs-repository:

```bash
sudo apt install halpid
```

De HALPI2-daemon hoort nu te draaien en het commando `halpi` beschikbaar te zijn. De status van de daemon controleert u met:
```bash
halpi status
```

## Firmware van de HALPI2 installeren

Nu het commando `halpi` beschikbaar is, kunt u het pakket `halpi2-firmware` installeren, dat de nieuwste firmware naar het HALPI2-board flasht:
```bash
apt install halpi2-firmware
```

De firmware kan handmatig worden geflasht met:
```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Signal K-server instellen

De Signal K-server is een populaire keuze voor het beheer van maritieme gegevens en kan zowel NMEA 2000- als NMEA 0183-gegevensbronnen aan.
De Signal K-server kan met npm worden geïnstalleerd. De volgende commando's installeren de Signal K-server en starten de eerste configuratie:

```bash
npm i -g signalk-server
signalk-server-setup
```

Daarna benadert u de Signal K-server vanuit een browser op de poort die u hebt ingesteld.

### Signal K-verbinding voor NMEA 2000

Om een NMEA 2000-verbinding met de CAN-interface van de HALPI in te stellen, hebt u een Signal K-beheerdersaccount nodig en gaat u in het menu naar `Server > Data Connections`.
Daar klikt u op de knop `+Add` en maakt u een verbinding aan met de volgende eigenschappen:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Start opnieuw op en controleer op het dashboard of er gegevens binnenkomen.

### Signal K-verbinding voor NMEA 0183

Om een NMEA 0183-verbinding met de CAN-interface van de HALPI in te stellen, hebt u een Signal K-beheerdersaccount nodig en gaat u in het menu naar `Server > Data Connections`.
Daar klikt u op de knop `+Add` en maakt u een verbinding aan met ten minste de volgende eigenschappen:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Start opnieuw op en controleer op het dashboard of er gegevens binnenkomen.

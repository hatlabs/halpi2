---
translated_from: 8c2d1560ad56e730c3fe6476cd5cf075b632b539
---

# Brug af andre Debian-baserede distributioner

!!! warning "Bemærk"
    Hat Labs kan ikke yde support til installation og brug af styresystemer fra tredjepart. Nedenstående vejledning stilles til rådighed som en service over for brugere, der ønsker at bruge HALPI2 med en tilpasset softwareopsætning.

HALPI2 kører gerne ethvert styresystem, der understøtter Raspberry Pi Compute Module 5. For at få fuldt udbytte af HALPI2-hardwaren, herunder funktionerne til strømstyring og overvågning, skal styresystemet understøtte HALPI2-dæmonen (`halpid`), og der kræves lidt konfiguration. Disse trin er ret ligetil på Debian-baserede Linux-distributioner. Dette afsnit indeholder en trinvis vejledning i at installere Ubuntu på HALPI2. Vejledningen kan kræve mindre tilpasninger til andre Debian-baserede distributioner.

Ubuntu-distributionen har et officielt [Ubuntu-image til Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, som kan bruges sammen med HALPI2.

## Forudsætninger

Når det valgte Ubuntu-image (eller et andet Debian-baseret image) er installeret på din Pi, skal du sikre dig, at du har de nyeste softwareopdateringer:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Derefter bør følgende pakker installeres, da de er nødvendige for installationsprocessen:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat Labs-pakkearkivet

Hat Labs leverer de færdigbyggede pakker til HALPI2, og de er tilgængelige via et apt-pakkearkiv.
For at tilføje dette arkiv skal du køre følgende kommandoer med root-rettigheder (fra `sudo bash`):

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

## Fælles firmware til HALPI2

Firmwaren til de fælles enheder på HALPI2-kortet konfigureres ved at redigere `/boot/firmware/config.txt` og tilføje følgende linjer i afsnittet `[all]`:

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

Derefter skal I2C-grænsefladen aktiveres, så `halpid`-dæmonen i brugerrummet kan kommunikere med hardwaren til strømstyring.
Det gøres ved at oprette filen `/etc/modules-load.d/i2c-dev.conf` med:

```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```
## Opsætning af CAN-bussen (NMEA 2000)

Følgende kommandoer aktiverer CAN-bussen til NMEA 2000-kommunikation på HALPI2:

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

Når systemet er genstartet, kan du kontrollere, at CAN-grænsefladen er tilgængelig, med en af disse kommandoer:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-dæmonen

HALPI2-dæmonen bruges til at overvåge og styre HALPI2-bærekortet og stiller kommandolinjeværktøjet `halpi` til rådighed.
Installer pakken `halpid` fra Hat Labs-pakkearkivet:

```bash
sudo apt install halpid
```

HALPI2-dæmonen bør nu køre, og kommandoen `halpi` være tilgængelig. Du kan kontrollere dæmonens status med:
```bash
halpi status
```

## Installation af HALPI2-firmware

Nu hvor kommandoen `halpi` er tilgængelig, kan pakken `halpi2-firmware` installeres. Den flasher den nyeste firmware til HALPI2-kortet:
```bash
apt install halpi2-firmware
```

Firmwaren kan flashes manuelt med:
```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Opsætning af Signal K-server

Signal K-serveren er et populært valg til håndtering af marine data og kan forbindes med både NMEA 2000- og NMEA 0183-datakilder.
Signal K-serveren kan installeres med npm. Følgende kommandoer installerer Signal K-serveren og kører den indledende opsætning:

```bash
npm i -g signalk-server
signalk-server-setup
```

Du kan derefter tilgå Signal K-serveren fra en browser på den port, du har konfigureret.

### Signal K-forbindelse til NMEA 2000

For at opsætte en NMEA 2000-forbindelse til CAN-grænsefladen på HALPI skal du bruge en Signal K-administratorkonto og gå til menupunktet `Server > Data Connections`.
Der kan du klikke på knappen `+Add` og oprette en forbindelse med følgende egenskaber:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Genstart, og kontrollér på dashboardet, om der modtages data.

### Signal K-forbindelse til NMEA 0183

For at opsætte en NMEA 0183-forbindelse til CAN-grænsefladen på HALPI skal du bruge en Signal K-administratorkonto og gå til menupunktet `Server > Data Connections`.
Der kan du klikke på knappen `+Add` og oprette en forbindelse med mindst følgende egenskaber:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Genstart, og kontrollér på dashboardet, om der modtages data.

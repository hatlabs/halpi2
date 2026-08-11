---
translated_from: 9b2819d37e8c666f7908c658418aa61209985b55
---

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
Om deze repository toe te voegen, voert u de volgende opdrachten uit met rootrechten (vanuit `sudo bash`):

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

!!! danger "Controleer uw opstartapparaat voordat u dit plakt"
    Het blok hieronder eindigt met `dtparam=sd=off`. Op een Compute Module 5 schakelt die regel de ingebouwde microSD-sleuf uit en, op een module met eMMC, ook de eMMC. Behoud de regel als u opstart vanaf NVMe, de standaardconfiguratie van de HALPI2. Verwijder hem als u opstart vanaf microSD of eMMC, anders start het apparaat na de volgende herstart niet meer op.

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

# Enable the ARM I2C bus.  The halpid daemon reaches the power management
# controller over /dev/i2c-1.
dtparam=i2c_arm=on

# Disable the SD interface.  Without this, shutdown stalls long enough that the
# supercapacitors can run out before the controller powers the board down.
# This also disables the onboard microSD slot and the eMMC on a CM5 that has
# one, so omit the line if you boot from either.
# See: https://github.com/raspberrypi/linux/issues/7014
dtparam=sd=off
```

!!! warning "I2C moet ingeschakeld zijn"
    In Raspberry Pi OS staat `dtparam=i2c_arm=on` uitgecommentarieerd, en andere distributies doen dat mogelijk ook. Zonder die regel is er geen `/dev/i2c-1` en bereikt `halpid` de hardware voor energiebeheer niet.

Daarnaast moet de kernelmodule `i2c-dev` bij het opstarten worden geladen, zodat de `halpid`-daemon in de gebruikersruimte de bus kan gebruiken.
Dat doet u door een bestand `/etc/modules-load.d/i2c-dev.conf` aan te maken met:

```bash
echo i2c-dev | sudo tee /etc/modules-load.d/i2c-dev.conf
```

Start opnieuw op om de wijzigingen door te voeren en controleer daarna of de I2C-bus aanwezig is:

```bash
sudo reboot
```

```bash
ls /dev/i2c-1
```

Bestaat `/dev/i2c-1` niet, loop dan de wijzigingen in `config.txt` na voordat u verdergaat. De `halpid`-daemon kan zonder die bus niet starten.

## CAN-bus (NMEA 2000) instellen

Met de volgende opdracht schakelt u de CAN-bus voor NMEA 2000-communicatie op de HALPI2 in:

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

Zodra het systeem opnieuw is opgestart, controleert u met een van de volgende opdrachten of de CAN-interface beschikbaar is:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-daemon

De HALPI2-daemon bewaakt en bestuurt het carrierboard van de HALPI2 en levert het opdrachtregelgereedschap `halpi`.
Installeer het pakket `halpid` uit de Hat Labs-repository:

```bash
sudo apt install halpid
```

De HALPI2-daemon hoort nu te draaien en de opdracht `halpi` beschikbaar te zijn. De status van de daemon controleert u met:
```bash
halpi status
```

De socket van de daemon is alleen leesbaar voor de groep `halpid`. Het pakket voegt uw gebruiker aan die groep toe, maar het lidmaatschap geldt pas in nieuwe aanmeldsessies. Kan de opdracht geen verbinding maken, meld u dan af en weer aan, of gebruik `sudo halpi status`.

## Firmware van de HALPI2 installeren

Nu de opdracht `halpi` beschikbaar is, installeert u het pakket `halpi2-firmware`, dat de firmwarebestanden onder `/usr/share/halpi2-firmware/` levert:
```bash
sudo apt install halpi2-firmware
```


!!! warning "Flash de firmware zelf"
    Het pakket probeert tijdens de installatie te flashen, maar die poging mislukt geruisloos in de huidige uitgaven ([`HALPI2-firmware` #40](https://github.com/hatlabs/HALPI2-firmware/issues/40)). Apt meldt toch succes, dus flash handmatig en controleer het resultaat.

Flash de firmware en schakel het apparaat daarna uit. Een herstart neemt de nieuwe firmware niet in gebruik:
```bash
sudo halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_*.bin
sudo shutdown -h now
```

Schakel het apparaat weer in en controleer de versie met `halpi status`. Bij een installatie zonder scherm moet u de aan-uitschakelaar kunnen bereiken voordat u het afsluiten uitvoert.

De [softwarehandleiding](../user-guide/software.md#firmware-handmatig-installeren) beschrijft het automatische updatemechanisme en hoe u dat uitschakelt.

## Signal K-server instellen

De Signal K-server is een populaire keuze voor het beheer van maritieme gegevens en kan zowel NMEA 2000- als NMEA 0183-gegevensbronnen aan.
De Signal K-server kan met npm worden geïnstalleerd. De volgende opdrachten installeren de Signal K-server en starten de eerste configuratie:

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
          Baud Rate: 4800 | 38400
```

Start opnieuw op en controleer op het dashboard of er gegevens binnenkomen.

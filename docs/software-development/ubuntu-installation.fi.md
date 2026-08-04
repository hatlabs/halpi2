# Muiden Debian-pohjaisten jakeluiden käyttö

!!! warning "Huomio"
    Hat Labs ei voi tarjota tukea kolmannen osapuolen käyttöjärjestelmien asennukseen ja käyttöön. Alla olevat ohjeet on tarkoitettu palveluksena käyttäjille, jotka haluavat käyttää HALPI2:ta räätälöidyllä ohjelmistokokoonpanolla.

HALPI2 toimii millä tahansa käyttöjärjestelmällä, joka tukee Raspberry Pi Compute Module 5:tä. Jotta HALPI2:n laitteiston kaikki ominaisuudet — mukaan lukien virranhallinta ja valvonta — ovat käytettävissä, käyttöjärjestelmän on tuettava HALPI2-daemonia (`halpid`), ja joitakin asetuksia on tehtävä. Debian-pohjaisissa Linux-jakeluissa nämä vaiheet ovat melko suoraviivaisia. Tässä osiossa on vaiheittaiset ohjeet Ubuntun asentamiseen HALPI2:lle. Muissa Debian-pohjaisissa jakeluissa ohjeisiin voi tarvita pieniä muutoksia.

Ubuntusta on olemassa virallinen [Ubuntu-levykuva Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5:lle, ja sitä voi käyttää HALPI2:n kanssa.

## Esivalmistelut

Kun valitsemasi Ubuntu-levykuva (tai muu Debian-pohjainen levykuva) on asennettu Pi:lle, varmista että ohjelmistopäivitykset ovat ajan tasalla:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Asenna seuraavaksi nämä paketit, joita asennusprosessi tarvitsee:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat Labsin pakettivarasto

HALPI2:n valmiiksi käännetyt paketit tulevat Hat Labsilta ja ovat saatavilla apt-pakettivarastosta. Varaston lisääminen edellyttää seuraavien komentojen ajamista pääkäyttäjän oikeuksilla (`sudo bash`):

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

## HALPI2:n yhteiset firmware-asetukset

HALPI2-kortin yleisten laitteiden firmware määritetään muokkaamalla tiedostoa `/boot/firmware/config.txt` ja lisäämällä seuraavat rivit `[all]`-osioon:

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

Tämän jälkeen I2C-liitäntä on otettava käyttöön, jotta käyttäjätilan `halpid`-daemon voi keskustella virranhallintalaitteiston kanssa. Tämä tehdään luomalla tiedosto `/etc/modules-load.d/i2c-dev.conf`:

```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```

## CAN-väylän (NMEA 2000) asetukset

Seuraava komento ottaa CAN-väylän käyttöön NMEA 2000 -liikennettä varten HALPI2:ssa:

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

Kun järjestelmä on käynnistynyt uudelleen, voit tarkistaa CAN-liitännän saatavuuden kummalla tahansa komennolla:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-daemon

HALPI2-daemon valvoo ja ohjaa HALPI2:n emolevyä ja tarjoaa `halpi`-komentorivityökalun. Asenna `halpid`-paketti Hat Labsin pakettivarastosta:

```bash
sudo apt install halpid
```

HALPI2-daemonin pitäisi nyt olla käynnissä ja `halpi`-komennon käytettävissä. Voit tarkistaa daemonin tilan komennolla:

```bash
halpi status
```

## HALPI2:n firmwaren asennus

Nyt kun `halpi`-komento on käytettävissä, voidaan asentaa `halpi2-firmware`-paketti, joka flashaa uusimman firmwaren HALPI2-kortille:

```bash
apt install halpi2-firmware
```

Firmwaren voi flashata käsin komennolla:

```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Signal K -palvelimen asetukset

Signal K -palvelin on suosittu valinta veneen tietojen hallintaan, ja se osaa lukea sekä NMEA 2000- että NMEA 0183 -lähteitä. Signal K -palvelimen voi asentaa npm:llä. Seuraavat komennot asentavat palvelimen ja käynnistävät alkuasetukset:

```bash
npm i -g signalk-server
signalk-server-setup
```

Tämän jälkeen Signal K -palvelimeen pääsee selaimella määrittämästäsi portista.

### Signal K:n NMEA 2000 -yhteys

NMEA 2000 -yhteyden luominen HALPIn CAN-liitäntään edellyttää Signal K:n ylläpitäjätunnusta. Siirry valikossa kohtaan `Server > Data Connections`, napsauta `+Add` ja luo yhteys seuraavilla asetuksilla:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Käynnistä uudelleen ja tarkista koontinäytöltä, saapuuko dataa.

### Signal K:n NMEA 0183 -yhteys

NMEA 0183 -yhteyden luominen edellyttää niin ikään Signal K:n ylläpitäjätunnusta. Siirry valikossa kohtaan `Server > Data Connections`, napsauta `+Add` ja luo yhteys vähintään seuraavilla asetuksilla:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Käynnistä uudelleen ja tarkista koontinäytöltä, saapuuko dataa.

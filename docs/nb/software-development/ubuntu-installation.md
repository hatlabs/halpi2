---
translated_from: 9b2819d37e8c666f7908c658418aa61209985b55
---

# Bruk av andre Debian-baserte distribusjoner

!!! warning "Merk"
    Hat Labs kan ikke tilby støtte for installasjon og bruk av operativsystemer fra tredjeparter. Instruksjonene nedenfor er gitt som en tjeneste til brukere som ønsker å bruke HALPI2 med et tilpasset programvareoppsett.

HALPI2 kjører uten videre ethvert operativsystem som støtter Raspberry Pi Compute Module 5. For å få full nytte av HALPI2-maskinvaren, inkludert funksjonene for strømstyring og overvåking, må operativsystemet støtte HALPI2-daemonen (`halpid`), og noe konfigurasjon er nødvendig. Disse trinnene er ganske enkle på Debian-baserte Linux-distribusjoner. Dette avsnittet gir trinnvise instruksjoner for å installere Ubuntu på HALPI2. Instruksjonene kan trenge mindre justeringer for andre Debian-baserte distribusjoner.

Ubuntu-distribusjonen har et offisielt [Ubuntu-systembilde for Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, som kan brukes med HALPI2.

## Forutsetninger

Når det Ubuntu-systembildet du har valgt (eller et annet Debian-basert systembilde) er installert på Pi-en, må du sørge for at du har de nyeste programvareoppdateringene:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Deretter bør følgende pakker installeres, siden de trengs i installasjonsprosessen:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat Labs-repositoriet

De ferdigbygde pakkene for HALPI2 leveres av Hat Labs og er tilgjengelige gjennom et apt-repositorium.
For å legge til dette repositoriet må du kjøre følgende kommandoer med root-rettigheter (fra `sudo bash`):

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

## Felles firmware for HALPI2

Firmwaren for de vanlige enhetene på HALPI2-kortet konfigureres ved å redigere `/boot/firmware/config.txt` og legge til følgende linjer i `[all]`-avsnittet:

!!! danger "Kontroller oppstartsenheten før du limer inn dette"
    Blokken nedenfor slutter med `dtparam=sd=off`. På en Compute Module 5 deaktiverer den linjen det innebygde microSD-sporet og, på en modul med eMMC, også eMMC-en. Behold linjen hvis du starter opp fra NVMe, som er standardoppsettet for HALPI2. Fjern den hvis du starter opp fra microSD eller eMMC, ellers starter ikke enheten etter neste omstart.

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

!!! warning "I2C må være aktivert"
    I Raspberry Pi OS er `dtparam=i2c_arm=on` kommentert ut, og andre distribusjoner kan gjøre det samme. Uten den finnes ikke `/dev/i2c-1`, og `halpid` når ikke maskinvaren for strømstyring.

Kjernemodulen `i2c-dev` må dessuten lastes ved oppstart, slik at daemonen `halpid` i brukerrommet (user space) kan bruke bussen.
Det gjør du ved å opprette filen `/etc/modules-load.d/i2c-dev.conf` med:

```bash
echo i2c-dev | sudo tee /etc/modules-load.d/i2c-dev.conf
```

Start på nytt for å ta i bruk endringene, og kontroller deretter at I2C-bussen finnes:

```bash
sudo reboot
```

```bash
ls /dev/i2c-1
```

Hvis `/dev/i2c-1` mangler, gå gjennom endringene i `config.txt` før du fortsetter. Daemonen `halpid` kan ikke starte uten den.

## Oppsett av CAN-buss (NMEA 2000)

Følgende kommandoer aktiverer CAN-bussen for NMEA 2000-kommunikasjon på HALPI2:

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

Når systemet har startet på nytt, kan du kontrollere at CAN-grensesnittet er tilgjengelig med en av disse kommandoene:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-daemonen

HALPI2-daemonen brukes til å overvåke og styre HALPI2-bærekortet, og den gir kommandolinjeverktøyet `halpi`.
Installer pakken `halpid` fra Hat Labs-repositoriet:

```bash
sudo apt install halpid
```

HALPI2-daemonen skal nå kjøre, og kommandoen `halpi` skal være tilgjengelig. Du kan sjekke statusen til daemonen med:
```bash
halpi status
```

Socketen til daemonen kan bare leses av gruppen `halpid`. Pakken legger brukeren din til i gruppen, men medlemskapet gjelder først i nye påloggingsøkter. Hvis kommandoen ikke får kontakt, logg ut og inn igjen, eller bruk `sudo halpi status`.

## Installasjon av HALPI2-firmware

Nå som kommandoen `halpi` er tilgjengelig, installer pakken `halpi2-firmware`, som inneholder firmware-filene under `/usr/share/halpi2-firmware/`:
```bash
sudo apt install halpi2-firmware
```


!!! warning "Flash firmwaren selv"
    Pakken forsøker å flashe under installasjonen, men forsøket mislykkes stille i de nåværende utgivelsene ([`HALPI2-firmware` #40](https://github.com/hatlabs/HALPI2-firmware/issues/40)). Apt melder likevel om vellykket installasjon, så flash manuelt og kontroller resultatet.

Flash firmwaren, og slå deretter av enheten. En omstart tar ikke den nye firmwaren i bruk:
```bash
sudo halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_*.bin
sudo shutdown -h now
```

Slå enheten på igjen og bekreft versjonen med `halpi status`. Ved en installasjon uten skjerm må du kunne nå strømbryteren før du kjører nedstengingen.

[Programvareveiledningen](../user-guide/software.md#manuell-installasjon-av-firmware) beskriver den automatiske oppdateringsmekanismen og hvordan du slår den av.

## Oppsett av Signal K-server

Signal K-serveren er et populært valg for håndtering av maritime data, og den kan koble seg til datakilder både på NMEA 2000 og NMEA 0183.
Signal K-serveren kan installeres med npm. Kommandoene nedenfor installerer Signal K-serveren og kjører det første oppsettet:

```bash
npm i -g signalk-server
signalk-server-setup
```

Du kan deretter nå Signal K-serveren fra en nettleser på porten du har konfigurert.

### Signal K-tilkobling for NMEA 2000

For å sette opp en NMEA 2000-tilkobling til CAN-grensesnittet på HALPI må du bruke en Signal K-administratorkonto og gå til menypunktet `Server > Data Connections`.
Der kan du klikke på knappen `+Add` og opprette en tilkobling med disse egenskapene:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Start på nytt og sjekk dashbordet for å se om det kommer inn data.

### Signal K-tilkobling for NMEA 0183

For å sette opp en NMEA 0183-tilkobling til CAN-grensesnittet på HALPI må du bruke en Signal K-administratorkonto og gå til menypunktet `Server > Data Connections`.
Der kan du klikke på knappen `+Add` og opprette en tilkobling med minst disse egenskapene:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 38400
```

Start på nytt og sjekk dashbordet for å se om det kommer inn data.

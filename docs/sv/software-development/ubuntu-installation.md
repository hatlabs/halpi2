---
translated_from: 9b2819d37e8c666f7908c658418aa61209985b55
---

# Använda andra Debian-baserade distributioner

!!! warning "Obs"
    Hat Labs kan inte ge support för installation och användning av operativsystem från tredje part. Anvisningarna nedan är en service till användare som vill köra HALPI2 med en egen programvaruuppsättning.

HALPI2 fungerar med vilket operativsystem som helst som stöder Raspberry Pi Compute Module 5. För att få tillgång till hela HALPI2-hårdvarans funktionalitet, inklusive strömhantering och övervakning, måste operativsystemet stödja HALPI2-daemonen (`halpid`), och en del inställningar krävs. På Debian-baserade Linux-distributioner är stegen ganska enkla. Det här avsnittet går igenom installationen av Ubuntu på HALPI2 steg för steg. För andra Debian-baserade distributioner kan mindre justeringar behövas.

Ubuntu har en officiell [Ubuntu-avbild för Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5 som går att använda med HALPI2.

## Förutsättningar

När den valda Ubuntu-avbilden (eller någon annan Debian-baserad avbild) är installerad på din Pi, se till att programvaran är uppdaterad:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Installera sedan följande paket, som behövs för installationen:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Hat Labs paketförråd

De färdigbyggda paketen för HALPI2 kommer från Hat Labs och finns i ett apt-paketförråd. För att lägga till förrådet kör du följande kommandon med root-behörighet (från `sudo bash`):

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

## HALPI2:s gemensamma firmware

Firmwaren för de gemensamma enheterna på HALPI2-kortet konfigureras genom att du redigerar `/boot/firmware/config.txt` och lägger till följande rader i avsnittet `[all]`:

!!! danger "Kontrollera din startenhet innan du klistrar in"
    Blocket nedan avslutas med `dtparam=sd=off`. På en Compute Module 5 stänger den raden av det inbyggda microSD-facket och, på en modul med eMMC, även eMMC:n. Behåll raden om du startar från NVMe, vilket är HALPI2:s standardkonfiguration. Ta bort den om du startar från microSD eller eMMC, annars startar enheten inte efter nästa omstart.

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

!!! warning "I2C måste aktiveras"
    I Raspberry Pi OS är `dtparam=i2c_arm=on` bortkommenterad, och andra distributioner kan göra likadant. Utan den finns ingen `/dev/i2c-1`, och `halpid` når inte strömhanteringens hårdvara.

Kärnmodulen `i2c-dev` måste dessutom läsas in vid uppstart, så att daemonen `halpid`, som körs i användarrymden, kan använda bussen. Det gör du genom att skapa filen `/etc/modules-load.d/i2c-dev.conf`:

```bash
echo i2c-dev | sudo tee /etc/modules-load.d/i2c-dev.conf
```

Starta om för att verkställa ändringarna och kontrollera sedan att I2C-bussen finns:

```bash
sudo reboot
```

```bash
ls /dev/i2c-1
```

Om `/dev/i2c-1` saknas, gå tillbaka till ändringarna i `config.txt` innan du fortsätter. Daemonen `halpid` kan inte starta utan den.

## Uppsättning av CAN-bussen (NMEA 2000)

Följande kommando aktiverar CAN-bussen för NMEA 2000-kommunikation på HALPI2:

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

När systemet har startat om kan du kontrollera att CAN-gränssnittet finns med något av kommandona:

```bash
ip link show can0
ifconfig can0
```

## HALPI2-daemon

HALPI2-daemonen övervakar och styr HALPI2:s bärkort och tillhandahåller kommandoradsverktyget `halpi`. Installera paketet `halpid` från Hat Labs paketförråd:

```bash
sudo apt install halpid
```

HALPI2-daemonen ska nu vara igång och kommandot `halpi` tillgängligt. Du kontrollerar daemonens status med:

```bash
halpi status
```

Daemonens socket är bara läsbar för gruppen `halpid`. Paketet lägger till din användare i gruppen, men medlemskapet gäller först i nya inloggningssessioner. Om kommandot inte kan ansluta, logga ut och in igen, eller använd `sudo halpi status`.

## Installation av HALPI2:s firmware

Nu när kommandot `halpi` är tillgängligt installerar du paketet `halpi2-firmware`, som innehåller firmware-filerna under `/usr/share/halpi2-firmware/`:

```bash
sudo apt install halpi2-firmware
```


!!! warning "Flasha firmwaren själv"
    Paketet försöker flasha under installationen, men försöket misslyckas tyst i nuvarande utgåvor ([`HALPI2-firmware` #40](https://github.com/hatlabs/HALPI2-firmware/issues/40)). Apt rapporterar ändå att allt gick bra, så flasha manuellt och kontrollera resultatet.

Flasha firmwaren och stäng sedan av enheten. En omstart tar inte den nya firmwaren i bruk:
```bash
sudo halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_*.bin
sudo shutdown -h now
```

Slå på enheten igen och kontrollera versionen med `halpi status`. Vid en installation utan skärm behöver du komma åt strömbrytaren innan du kör avstängningen.

[Programvaruguiden](../user-guide/software.md#installera-firmware-manuellt) beskriver den automatiska uppdateringsmekanismen och hur du stänger av den.

## Uppsättning av Signal K-server

Signal K-servern är ett populärt val för hantering av marina data och kan läsa både NMEA 2000- och NMEA 0183-källor. Den installeras med npm. Följande kommandon installerar servern och kör den inledande konfigurationen:

```bash
npm i -g signalk-server
signalk-server-setup
```

Därefter når du Signal K-servern från en webbläsare på den port du har ställt in.

### NMEA 2000-anslutning i Signal K

För att skapa en NMEA 2000-anslutning till HALPI:s CAN-gränssnitt behöver du ett administratörskonto i Signal K. Gå till `Server > Data Connections` i menyn, klicka på `+Add` och skapa en anslutning med följande egenskaper:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Starta om och kontrollera på instrumentpanelen om data kommer in.

### NMEA 0183-anslutning i Signal K

Även för en NMEA 0183-anslutning behöver du ett administratörskonto i Signal K. Gå till `Server > Data Connections` i menyn, klicka på `+Add` och skapa en anslutning med minst följande egenskaper:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 38400
```

Starta om och kontrollera på instrumentpanelen om data kommer in.

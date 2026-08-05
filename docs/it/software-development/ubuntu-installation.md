# Utilizzo di altre distribuzioni basate su Debian

!!! warning "Nota"
    Hat Labs non è in grado di fornire assistenza per l’installazione e l’uso di sistemi operativi di terze parti. Le istruzioni riportate di seguito sono fornite per cortesia agli utenti che desiderano utilizzare HALPI2 con una configurazione software personalizzata.

HALPI2 esegue senza difficoltà qualsiasi sistema operativo che supporti il Raspberry Pi Compute Module 5. Per sfruttare tutte le funzionalità dell’hardware HALPI2, comprese la gestione dell’alimentazione e le funzioni di monitoraggio, il sistema operativo deve supportare il demone HALPI2 (`halpid`) ed è necessaria qualche configurazione. Sulle distribuzioni Linux basate su Debian questi passaggi sono piuttosto semplici. Questa sezione fornisce istruzioni dettagliate per installare Ubuntu su HALPI2. Per altre distribuzioni basate su Debian le istruzioni possono richiedere piccoli adattamenti.

La distribuzione Ubuntu mette a disposizione un’[immagine Ubuntu ufficiale per il Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, utilizzabile con HALPI2.

## Prerequisiti

Una volta installata sul Pi l’immagine Ubuntu (o altra immagine basata su Debian) scelta, assicurarsi di disporre degli aggiornamenti software più recenti:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Occorre quindi installare i pacchetti seguenti, necessari per la procedura di installazione:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Repository Hat Labs

I pacchetti precompilati per HALPI2 sono forniti da Hat Labs e sono disponibili tramite un repository apt.
Per aggiungere questo repository occorre eseguire i comandi seguenti con privilegi di root (da `sudo bash`):

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

## Firmware comune di HALPI2

Il firmware dei dispositivi comuni presenti sulla scheda HALPI2 può essere configurato modificando `/boot/firmware/config.txt` e aggiungendo le righe seguenti alla sezione `[all]`:

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

È quindi necessario abilitare l’interfaccia I2C, affinché il demone `halpid` in spazio utente possa comunicare con l’hardware di gestione dell’alimentazione.
A tale scopo si crea il file `/etc/modules-load.d/i2c-dev.conf` con:

```bash
sudo echo i2c-dev > /etc/modules-load.d/i2c-dev.conf
```
## Configurazione del bus CAN (NMEA 2000)

I comandi seguenti abilitano il bus CAN per la comunicazione NMEA 2000 su HALPI2:

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

Una volta riavviato il sistema, è possibile verificare che l’interfaccia CAN sia disponibile con uno dei comandi seguenti:

```bash
ip link show can0
ifconfig can0
```

## Demone HALPI2

Il demone HALPI2 serve a monitorare e controllare la scheda portante (carrier board) di HALPI2 e mette a disposizione lo strumento da riga di comando `halpi`.
Installare il pacchetto `halpid` dal repository Hat Labs:

```bash
sudo apt install halpid
```

A questo punto il demone HALPI2 dovrebbe essere in esecuzione e il comando `halpi` disponibile. Lo stato del demone si verifica con:
```bash
halpi status
```

## Installazione del firmware di HALPI2

Ora che il comando `halpi` è disponibile, si può installare il pacchetto `halpi2-firmware`, che flasherà il firmware più recente sulla scheda HALPI2:
```bash
apt install halpi2-firmware
```

Il firmware può essere flashato manualmente con:
```bash
halpi flash /usr/share/halpi2/firmware/halpi2-rs-firmware_VERSION.bin
```

## Configurazione del server Signal K

Il server Signal K è una scelta molto diffusa per la gestione dei dati nautici e può interfacciarsi con sorgenti dati sia NMEA 2000 sia NMEA 0183.
Il server Signal K può essere installato tramite npm. I comandi seguenti installano il server Signal K ed eseguono la configurazione iniziale:

```bash
npm i -g signalk-server
signalk-server-setup
```

È quindi possibile accedere al server Signal K da un browser, sulla porta configurata.

### Connessione NMEA 2000 in Signal K

Per configurare una connessione NMEA 2000 verso l’interfaccia CAN di HALPI occorre utilizzare un account amministratore Signal K e accedere alla sezione di menu `Server > Data Connections`.
Da lì si può fare clic sul pulsante `+Add` e creare un connettore con le proprietà seguenti:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Riavviare e controllare la dashboard per verificare se i dati vengono ricevuti.

### Connessione NMEA 0183 in Signal K

Per configurare una connessione NMEA 0183 verso l’interfaccia CAN di HALPI occorre utilizzare un account amministratore Signal K e accedere alla sezione di menu `Server > Data Connections`.
Da lì si può fare clic sul pulsante `+Add` e creare un connettore almeno con le proprietà seguenti:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 34800
```

Riavviare e controllare la dashboard per verificare se i dati vengono ricevuti.

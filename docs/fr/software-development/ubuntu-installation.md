---
translated_from: 9b2819d37e8c666f7908c658418aa61209985b55
---

# Utiliser d'autres distributions basées sur Debian

!!! warning "Note"
    Hat Labs ne peut pas assurer l'assistance pour l'installation et l'utilisation de systèmes d'exploitation tiers. Les instructions ci-dessous sont fournies à titre de service aux utilisateurs souhaitant faire fonctionner le HALPI2 avec une configuration logicielle personnalisée.

Le HALPI2 fonctionne avec n'importe quel système d'exploitation prenant en charge le Raspberry Pi Compute Module 5. Pour bénéficier de toutes les fonctions du matériel HALPI2, y compris la gestion et la surveillance de l'alimentation, le système doit prendre en charge le démon HALPI2 (`halpid`) et quelques réglages sont nécessaires. Ces étapes sont assez simples sur les distributions Linux basées sur Debian. Cette section détaille l'installation d'Ubuntu sur le HALPI2. Les instructions peuvent demander de légers ajustements pour d'autres distributions basées sur Debian.

Ubuntu propose une [image Ubuntu officielle pour le Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, utilisable avec le HALPI2.

## Prérequis

Une fois l'image Ubuntu (ou toute autre image basée sur Debian) installée sur le Pi, assurez-vous que les mises à jour logicielles sont à jour :

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

Installez ensuite les paquets suivants, nécessaires à la procédure d'installation :

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Dépôt Hat Labs

Les paquets précompilés pour le HALPI2 sont fournis par Hat Labs et disponibles dans un dépôt apt. Pour ajouter ce dépôt, exécutez les commandes suivantes avec les privilèges root (depuis `sudo bash`) :

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

## Firmware commun du HALPI2

Le firmware des périphériques communs de la carte HALPI2 se configure en modifiant `/boot/firmware/config.txt` et en ajoutant les lignes suivantes dans la section `[all]` :

!!! danger "Vérifiez votre périphérique de démarrage avant de coller ceci"
    Le bloc ci-dessous se termine par `dtparam=sd=off`. Sur un Compute Module 5, cette ligne désactive le lecteur microSD intégré et, sur un module doté d'eMMC, l'eMMC également. Conservez-la si vous démarrez depuis un NVMe, ce qui est la configuration standard du HALPI2. Supprimez-la si vous démarrez depuis la microSD ou l'eMMC, sans quoi l'appareil ne démarrera plus au prochain redémarrage.

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

!!! warning "L'I2C doit être activé"
    Sur Raspberry Pi OS, `dtparam=i2c_arm=on` est en commentaire, et d'autres distributions peuvent faire de même. Sans cette ligne, `/dev/i2c-1` n'existe pas et `halpid` n'atteint pas le matériel de gestion de l'alimentation.

Le module du noyau `i2c-dev` doit en outre être chargé au démarrage pour que le démon `halpid`, qui s'exécute en espace utilisateur, puisse utiliser le bus. Créez pour cela le fichier `/etc/modules-load.d/i2c-dev.conf` :

```bash
echo i2c-dev | sudo tee /etc/modules-load.d/i2c-dev.conf
```

Redémarrez pour appliquer les changements, puis vérifiez que le bus I2C est présent :

```bash
sudo reboot
```

```bash
ls /dev/i2c-1
```

Si `/dev/i2c-1` n'existe pas, reprenez les modifications de `config.txt` avant de continuer. Le démon `halpid` ne peut pas démarrer sans lui.

## Configuration du bus CAN (NMEA 2000)

La commande suivante active le bus CAN pour les communications NMEA 2000 sur le HALPI2 :

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

Une fois le système redémarré, vous pouvez vérifier la disponibilité de l'interface CAN avec l'une ou l'autre de ces commandes :

```bash
ip link show can0
ifconfig can0
```

## Démon HALPI2

Le démon HALPI2 surveille et pilote la carte porteuse du HALPI2 et fournit l'outil en ligne de commande `halpi`. Installez le paquet `halpid` depuis le dépôt Hat Labs :

```bash
sudo apt install halpid
```

Le démon HALPI2 devrait maintenant être en cours d'exécution et la commande `halpi` disponible. Vous pouvez vérifier l'état du démon avec :

```bash
halpi status
```

Le socket du démon n'est lisible que par le groupe `halpid`. Le paquet ajoute votre utilisateur à ce groupe, mais l'appartenance ne prend effet que dans les nouvelles sessions. Si la commande n'arrive pas à se connecter, déconnectez-vous puis reconnectez-vous, ou utilisez `sudo halpi status`.

## Installation du firmware du HALPI2

Maintenant que la commande `halpi` est disponible, installez le paquet `halpi2-firmware`, qui fournit les fichiers de firmware dans `/usr/share/halpi2-firmware/` :

```bash
sudo apt install halpi2-firmware
```


!!! warning "Flashez le firmware vous-même"
    Le paquet tente de flasher pendant l'installation, mais la tentative échoue silencieusement dans les versions actuelles ([`HALPI2-firmware` #40](https://github.com/hatlabs/HALPI2-firmware/issues/40)). Apt signale malgré tout une réussite : flashez donc manuellement et vérifiez le résultat.

Flashez le firmware, puis mettez l'appareil hors tension. Un redémarrage n'applique pas le nouveau firmware :
```bash
sudo halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_*.bin
sudo shutdown -h now
```

Remettez l'appareil sous tension et vérifiez la version avec `halpi status`. Sur une installation sans écran, assurez-vous de pouvoir atteindre l'interrupteur avant de lancer l'arrêt.

Le [guide logiciel](../user-guide/software.md#installation-manuelle-du-firmware) décrit le mécanisme de mise à jour automatique et la façon de le désactiver.

## Configuration du serveur Signal K

Le serveur Signal K est un choix répandu pour la gestion des données de navigation ; il sait exploiter aussi bien les sources NMEA 2000 que NMEA 0183. Il s'installe avec npm. Les commandes suivantes installent le serveur et lancent la configuration initiale :

```bash
npm i -g signalk-server
signalk-server-setup
```

Vous pouvez ensuite accéder au serveur Signal K depuis un navigateur, sur le port que vous avez configuré.

### Connexion NMEA 2000 dans Signal K

Créer une connexion NMEA 2000 vers l'interface CAN du HALPI nécessite un compte administrateur Signal K. Dans le menu, allez dans `Server > Data Connections`, cliquez sur `+Add` et créez une connexion avec les propriétés suivantes :

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Redémarrez, puis vérifiez sur le tableau de bord que des données arrivent.

### Connexion NMEA 0183 dans Signal K

Créer une connexion NMEA 0183 nécessite également un compte administrateur Signal K. Dans le menu, allez dans `Server > Data Connections`, cliquez sur `+Add` et créez une connexion avec au moins les propriétés suivantes :

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 38400
```

Redémarrez, puis vérifiez sur le tableau de bord que des données arrivent.

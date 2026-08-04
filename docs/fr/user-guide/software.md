---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Guide logiciel

## Images système

Hat Labs fournit des images prêtes à l'emploi pour le HALPI2. Toutes comportent la configuration et les adaptations nécessaires au matériel HALPI2 : le CAN (NMEA 2000) comme périphérique réseau `can0`, le RS-485 (NMEA 0183) comme `/dev/ttyAMA4`, ainsi que le paquet `halpi2-firmware`.

### HaLOS (par défaut)

[HaLOS](https://docs.halos.fi) est une distribution Linux à base de conteneurs conçue pour les applications marines et industrielles. Elle propose une interface web pour l'administration système, la gestion des applications et la surveillance — sans écran, clavier ni VNC.

**Variantes de l'image :**

| Image | Description |
|:------|:------------|
| Halos-HALPI2 | Image de base sans écran, avec Cockpit et la gestion des conteneurs |
| Halos-HALPI2-Desktop | Image de base avec le bureau Raspberry Pi |
| Halos-HALPI2-Marine | Sans écran, avec les applications marines (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Bureau avec les applications marines |

Téléchargez les images HaLOS depuis la [page des versions HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest). La documentation détaillée se trouve sur [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter est une image basée sur Raspberry Pi OS, enrichie d'applications de navigation. Elle offre un environnement de bureau classique avec accès distant par VNC, et intègre Signal K et OpenCPN préinstallés.

Si vous n'utilisez ni écran, ni clavier, ni souris avec le HALPI2, vous pouvez vous connecter à l'ordinateur soit par câble Ethernet, soit par le point d'accès WiFi (`OpenPlotter`, mot de passe `12345678`).

Dans les deux cas, l'accès à l'ordinateur HALPI2 se fait par VNC ou SSH. Pour le VNC, téléchargez [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) de RealVNC.

Le point d'accès comme le compte utilisateur par défaut ayant des mots de passe par défaut, il est impératif de les changer dès le premier démarrage. La marche à suivre est décrite dans la [documentation OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Téléchargez les images OpenPlotter depuis [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS et Raspberry Pi OS Lite

Si vous préférez le Raspberry Pi OS standard, vous pouvez télécharger l'image la plus récente prenant en charge le HALPI2 depuis [le dépôt GitHub](https://github.com/hatlabs/openplotter-halpi/releases). Flashez l'image sur le SSD avec Raspberry Pi Imager. Lors du flashage, vous pouvez appliquer des réglages comme le nom d'hôte, l'activation de SSH et la configuration du WiFi.

Si vous n'appliquez pas ces réglages, il vous faudra un écran et un clavier raccordés au HALPI2 pour effectuer la configuration initiale. Un nom d'utilisateur et un mot de passe vous seront demandés au premier démarrage.


## Flasher une image système sur le SSD

Il existe deux méthodes pour flasher une image système sur le SSD NVMe du HALPI2 : retirer le SSD et utiliser un adaptateur USB-NVMe, ou flasher directement sur l'appareil. L'adaptateur USB-NVMe est recommandé pour sa simplicité : ces adaptateurs se trouvent facilement en ligne à bas prix et la procédure est directe.

### Flashage avec un adaptateur USB-NVMe

Commencez par retirer le SSD NVMe du HALPI2 en suivant la procédure décrite dans le [Guide du matériel](./hardware.md#remplacer-le-ssd-nvme). Téléchargez ensuite une image compatible HALPI2 — soit une [image HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest), soit une [image OpenPlotter ou Raspberry Pi OS](https://github.com/hatlabs/openplotter-halpi/releases) — en veillant à choisir celle qui correspond à votre usage.

Insérez le SSD dans l'adaptateur USB-NVMe et raccordez-le à votre ordinateur. Flashez l'image téléchargée sur le SSD NVMe avec Raspberry Pi Imager. S'il s'agit d'une image Raspberry Pi OS, vous pouvez modifier et appliquer les réglages de personnalisation du système pendant le flashage. Sans ces réglages, il vous faudra un clavier et une souris USB raccordés au HALPI2 pour la configuration initiale après l'installation.

Avec les images HaLOS, les réglages de personnalisation ne doivent **pas** être appliqués pendant le flashage. HaLOS se configure après le démarrage, depuis son interface web.

De même, avec l'image OpenPlotter, les réglages de personnalisation ne doivent **pas** être appliqués pendant le flashage. La configuration se fait après le premier démarrage, avec les outils de configuration de Raspberry Pi et d'OpenPlotter.

Une fois le flashage terminé, débranchez l'adaptateur et retirez le SSD. Réinstallez-le dans le HALPI2 en suivant la procédure d'installation du Guide du matériel, puis refermez le boîtier conformément au même guide.

### Flashage directement sur le HALPI2

Vous pouvez aussi flasher l'image système directement sur le HALPI2, sans retirer le SSD. Cette méthode suit la procédure standard de flashage d'un Compute Module, décrite dans la [documentation Raspberry Pi](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Les instructions de préparation y sont écrites pour la carte CM5 IO Board, mais la démarche est comparable sur le HALPI2.

**Prérequis.** Installez l'outil `rpiboot` depuis le [dépôt `usbboot`](https://github.com/raspberrypi/usbboot) de Raspberry Pi. Sous Linux et macOS, compilez-le et installez-le depuis les sources comme l'indique le README du dépôt ; sous Windows, installez Raspberry Pi Imager ou le programme d'installation `rpiboot` autonome, accessible depuis la même page.

Pour préparer le HALPI2 au flashage par USB :

1. Mettez le système complètement hors tension et ouvrez le couvercle du boîtier en suivant la procédure du [Guide du matériel](./hardware.md#ouverture-du-boitier).
2. Repérez le connecteur USB-C marqué « USB Boot », à droite de l'emplacement HAT sur la carte porteuse, et basculez le sélecteur de mode de démarrage voisin en position « Abnormal ». (Aucune LED ne le confirme encore : l'appareil est hors tension.)
3. Raccordez un câble USB entre votre ordinateur et le connecteur USB Boot du HALPI2, puis remettez l'appareil sous tension. Une LED ambre s'allume à côté du sélecteur, confirmant que le HALPI2 est en mode de démarrage USB.
4. Sur votre ordinateur, lancez `rpiboot`. L'outil détecte le HALPI2 et charge le firmware de périphérique de stockage de masse ; le HALPI2 apparaît alors comme un périphérique de stockage USB.
5. Une fois `rpiboot` terminé et le périphérique de stockage visible, remettez le sélecteur de mode de démarrage en position « Normal ». Cela n'interrompt pas le flashage et garantit que le HALPI2 démarrera normalement sur l'image fraîchement flashée à la prochaine mise sous tension. Laissé sur « Abnormal », l'appareil repasserait en mode de démarrage USB au lieu de lancer le nouveau système.
6. Flashez l'image système avec Raspberry Pi Imager (ou tout autre outil capable d'écrire sur un périphérique bloc), en visant le nouveau périphérique de stockage.
7. Une fois le flashage terminé, débranchez le câble USB, coupez puis rétablissez l'alimentation du HALPI2, et refermez le boîtier.

!!! tip "Redémarrer sans débrancher"
    Le boîtier étant déjà ouvert, le moyen le plus rapide de redémarrer le HALPI2 est de court-circuiter brièvement les deux broches inférieures du connecteur de boutons, à côté de la prise USB-C. Toucher les deux broches à la fois avec la coque métallique d'un connecteur de câble USB-C fonctionne bien et ne présente pas de danger.

## Configuration initiale du système

Après le premier flashage et le premier démarrage du HALPI2, plusieurs réglages sont nécessaires pour garantir un fonctionnement sûr et correct.

### Configuration de HaLOS

HaLOS se configure entièrement depuis son interface web. Après le premier démarrage, accédez à Cockpit sur `https://halos.local:9090/` et au tableau de bord sur `https://halos.local/`. Changez immédiatement les mots de passe par défaut — voir le guide [Prise en main](../getting-started/getting-started.md#configuration-au-premier-demarrage) et la [documentation HaLOS](https://docs.halos.fi/getting-started/first-boot/).

### Configuration d'OpenPlotter

Avec l'image OpenPlotter, le système démarre avec des mots de passe par défaut, tant pour le point d'accès WiFi que pour le compte utilisateur. Pour des raisons de sécurité, il est impératif de les changer dès le premier démarrage.

La procédure de changement des mots de passe et la configuration initiale sont décrites dans le guide [Prise en main](../getting-started/getting-started.md#configuration-au-premier-demarrage) et dans la [documentation OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Configuration de Raspberry Pi OS

Si vous avez choisi le Raspberry Pi OS standard plutôt qu'OpenPlotter, suivez la procédure de configuration Raspberry Pi habituelle qui s'affiche au premier démarrage. Cet assistant vous guide pour créer les comptes utilisateurs, définir les mots de passe, configurer le WiFi et activer les services essentiels comme SSH pour l'accès distant.

Pendant cette configuration initiale, pensez également à régler le fuseau horaire, la disposition du clavier et les autres préférences régionales adaptées à votre environnement. L'outil de configuration Raspberry Pi (`raspi-config`) donne accès à d'autres réglages système, modifiables une fois la configuration initiale terminée.

## Accès à distance

Le HALPI2 propose plusieurs moyens d'accès à distance, qui permettent de surveiller et de piloter le système sans y accéder physiquement. C'est particulièrement utile lorsque l'appareil est installé sans écran, dans un endroit difficile d'accès.

### Accès web (HaLOS)

HaLOS fournit une interface d'administration web complète, sans logiciel supplémentaire :

- **Tableau de bord** (`https://halos.local/`) : le tableau de bord Homarr donne accès à toutes les applications installées, dont Signal K, Grafana et les autres applications marines.
- **Cockpit** (`https://halos.local:9090/`) : administration système, avec accès au terminal, mises à jour logicielles, configuration réseau et gestion des applications conteneurisées.

### SSH (Secure Shell)

SSH donne un accès sécurisé en ligne de commande au système HALPI2 : exécution de commandes, transfert de fichiers et administration à distance. SSH est activé par défaut sur les images HaLOS sans écran et sur OpenPlotter. Sur les variantes HaLOS Desktop et sur Raspberry Pi OS, il s'active avec `raspi-config`.

Pour vous connecter en SSH, utilisez un client SSH tel que le terminal intégré de macOS et Linux, ou une application comme PuTTY sous Windows. La commande de connexion de base est :

```bash
ssh username@halpi2-ip-address
```

Les connexions SSH sont chiffrées et sûres : correctement configurées avec une authentification robuste, elles conviennent aux réseaux publics. Elles consomment en outre très peu de bande passante, ce qui les rend idéales pour un accès distant sur des liaisons lentes ou à forte latence.

### VNC (Virtual Network Computing)

!!! note
    Le VNC ne concerne que les images OpenPlotter et Raspberry Pi OS Desktop. HaLOS utilise à la place un accès web — voir ci-dessus.

Le VNC donne accès à distance à l'interface graphique du HALPI2 : vous interagissez avec le bureau comme si vous étiez devant l'appareil. Il est préinstallé et préconfiguré sur les images OpenPlotter. Sur une installation Raspberry Pi OS, il s'active avec l'outil de configuration `raspi-config`.

Pour vous connecter au bureau du HALPI2 à distance, utilisez l'application [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) de RealVNC, disponible pour Windows, macOS, Linux, iOS et Android. Le VNC fonctionne très bien en réseau local et hors ligne, ce qui le rend idéal pour les installations à bord où la connexion Internet peut être limitée ou absente.

Pour un accès à distance par Internet, le VNC demande une configuration réseau supplémentaire, comme une redirection de ports ou un VPN : le protocole ne traverse pas nativement les pare-feu et les équipements NAT.

### Raspberry Pi Connect

Raspberry Pi Connect propose une approche web moderne de l'accès distant au bureau : vous vous connectez au bureau du HALPI2 avec un simple navigateur, sans installer de logiciel. Le service traverse automatiquement les pare-feu et les configurations NAT, ce qui le rend particulièrement adapté à l'accès distant par Internet sans configuration réseau complexe.

Contrairement au VNC, Raspberry Pi Connect gère seul les subtilités réseau et offre un accès simple depuis n'importe quelle connexion Internet. Il exige toutefois que le HALPI2 lui-même dispose d'une connexion Internet active.

## Mises à jour logicielles

Des mises à jour régulières sont recommandées pour préserver les performances et la sécurité du système.

### Mises à jour de HaLOS

Sous HaLOS, les paquets système (y compris le firmware du HALPI2) se mettent à jour depuis Cockpit ou en ligne de commande avec `apt`. Les applications conteneurisées (Signal K, Grafana, etc.) se mettent à jour depuis l'interface Container Apps de Cockpit, qui recherche les nouvelles versions des images de conteneur.

### Mises à jour en ligne de commande (toutes les images)

La méthode la plus fiable pour mettre à jour le système passe par la ligne de commande. Ouvrez un terminal et exécutez :

```bash
sudo apt update
sudo apt upgrade
```

La première commande (`apt update`) actualise la base de données des paquets avec les dernières versions disponibles ; la seconde (`apt upgrade`) télécharge et installe toutes les mises à jour. Cette opération met à jour l'ensemble des paquets installés, y compris le système Raspberry Pi OS de base, les composants OpenPlotter et les logiciels propres au HALPI2.

Pendant la mise à jour, il peut vous être demandé de confirmer l'installation de certains paquets ou le redémarrage de services. Vous pouvez généralement accepter, sauf raison particulière de refuser.

### Mises à jour graphiques

Pour ceux qui préfèrent une interface graphique, l'environnement de bureau signale visuellement les mises à jour disponibles. Une icône de téléchargement apparaît en haut à droite de la barre des tâches lorsque des mises à jour sont prêtes à être installées. Un clic sur cette icône ouvre le gestionnaire de mises à jour, qui permet de les passer en revue et de les installer simplement.

## Mises à jour du firmware

Le firmware du contrôleur HALPI2 se met à jour par la procédure de mise à jour habituelle de Raspberry Pi OS, ce qui en fait une opération intégrée et sans friction. Ces mises à jour régulières sont importantes pour les performances, l'accès aux nouvelles fonctions et la compatibilité avec les logiciels qui évoluent.

### Mises à jour automatiques du firmware

Les mises à jour du firmware sont distribuées par le mécanisme de mise à jour standard, sous forme de paquets Debian dans un dépôt APT. Pour les rechercher et les installer, ouvrez un terminal et exécutez :

```bash
sudo apt update
sudo apt upgrade
```

Lorsqu'un nouveau firmware HALPI2 est disponible, il est téléchargé et installé automatiquement dans le cadre de la mise à jour. Le système vous signale si des mises à jour de firmware figurent parmi les paquets disponibles.

Une fois le paquet de firmware mis à jour, il est indispensable de redémarrer le système correctement pour que les changements prennent effet. Utilisez la commande d'arrêt afin de garantir une coupure complète de l'alimentation :

```bash
sudo shutdown -h now
```

**Important :** un simple redémarrage ne suffit pas pour une mise à jour de firmware. Un arrêt complet suivi d'un démarrage est nécessaire, car c'est à ce moment que le contrôleur redémarre et applique le nouveau firmware. Le firmware du contrôleur n'est mis à jour qu'à la mise sous tension.

### Sécurités du firmware

Le HALPI2 intègre des mécanismes de sécurité contre la corruption du firmware. Si l'appareil est redémarré dans les 30 secondes suivant l'application d'une mise à jour, le système revient automatiquement à la version précédente. Cette protection évite qu'une mise à jour problématique n'empêche le fonctionnement normal.

### Installation manuelle du firmware

Pour les utilisateurs avertis ou dans certains cas de dépannage, le firmware peut être installé manuellement avec l'outil en ligne de commande HALPI. Les fichiers de firmware se trouvent dans le répertoire `/usr/share/halpi2-firmware/` et se flashent directement :

```bash
halpi flash <firmware_file>.bin
```

### Désactiver les mises à jour automatiques du firmware

Vous pouvez souhaiter désactiver les mises à jour automatiques pour rester sur une version précise. Cela se fait en modifiant le fichier de configuration du HALPI2 :

```bash
sudo nano /etc/halpid/firmware.conf
```

Repérez le réglage `AUTO_FLASH_ON_INSTALL` et donnez-lui la valeur `no` :

```bash
AUTO_FLASH_ON_INSTALL=no
```

Enregistrez le fichier et quittez l'éditeur. Le HALPI2 ne flashera plus automatiquement de nouveau firmware lors des mises à jour ordinaires : vous gardez la maîtrise complète du moment où elles sont appliquées. Vous pouvez toujours installer une mise à jour manuellement avec la commande `halpi flash`.


## Outil en ligne de commande HALPI

L'interface logicielle du HALPI2 se compose du service démon `halpid` et de l'outil en ligne de commande `halpi`. Ensemble, ils assurent la surveillance, la configuration et le pilotage du système.

### Démon HALPI (`halpid`)

Le démon HALPI s'exécute comme service système et assure la communication entre le système d'exploitation et le contrôleur du HALPI2. C'est lui qui rend possible le mode coopératif, avec toutes les fonctions de surveillance et de gestion de l'alimentation.

#### Gestion du service

Le démon se pilote avec systemd :

```bash
# Check daemon status
systemctl status halpid

# Start the daemon
sudo systemctl start halpid

# Stop the daemon
sudo systemctl stop halpid

# Enable auto-start at boot
sudo systemctl enable halpid

# Disable auto-start
sudo systemctl disable halpid

# View daemon logs
journalctl -u halpid -f
```

#### Configuration

La configuration du démon se trouve dans `/etc/halpid/halpid.conf`. Pour la modifier :

```bash
sudo nano /etc/halpid/halpid.conf
```

Toute modification nécessite le redémarrage du démon :

```bash
sudo systemctl restart halpid
```

### Outil en ligne de commande HALPI (`halpi`)

La commande `halpi` donne un accès direct aux fonctions du contrôleur et à l'état du système. Elle dialogue avec le démon pour exécuter des commandes et récupérer des informations sur l'état de fonctionnement, la configuration et les mesures matérielles du HALPI2.

#### État du système et surveillance

La fonction principale de l'outil en ligne de commande HALPI est de fournir un état complet du système : mesures matérielles, état de fonctionnement et données de surveillance en temps réel.

Afficher l'état du système :

```bash
# Display comprehensive system status
halpi status
```

Cette commande donne une vue d'ensemble de l'état courant du HALPI2 : tensions, consommation de courant, températures et état du contrôleur.

```
$ halpi status
 hardware_version               N/A
 firmware_version             3.1.0
 state              OperationalCoOp
 5v_output_enabled             True
 watchdog_enabled              True
 watchdog_timeout              10.0  s
 watchdog_elapsed               0.0  s
 V_in                          12.2  V
 I_in                          0.38  A
 V_supercap                   10.27  V
 T_mcu                         43.3  °C
 T_pcb                         35.2  °C
```

Pour ne suivre qu'une seule valeur, récupérez-la ainsi :

```bash
# Show controller firmware version
halpi get firmware_version
```

Pour écrire des scripts, mieux vaut utiliser l'API REST, décrite à la section [Accès à l'API REST](#acces-a-lapi-rest).

#### Gestion de la configuration

L'outil en ligne de commande HALPI permet de consulter les réglages courants et de modifier les paramètres de fonctionnement.

Consulter la configuration courante :

```bash
# Show current configuration
halpi config
```

Cela affiche tous les paramètres configurables et leurs valeurs actuelles :

```
$ halpi config
 Key                       Value
 watchdog_timeout           10.0
 power_on_threshold          8.0
 solo_power_off_threshold    5.5
 led_brightness               40
 auto_restart               True
 solo_depleting_timeout      5.0
```

#### Commande des LED

L'un des réglages les plus souvent ajustés est la luminosité des LED, que l'on peut adapter à l'environnement et aux préférences de chacun.

Exemples de commandes pour régler la luminosité des LED :

```bash
# Get current LED brightness (0-255)
halpi config get led_brightness

# Set LED brightness to low level for night operation
halpi config set led_brightness 40

# Set moderate brightness
halpi config set led_brightness 64

# Turn LEDs off completely
halpi config set led_brightness 0

# Maximum brightness for daylight operation
halpi config set led_brightness 255
```

La luminosité accepte des valeurs de 0 (extinction complète) à 255 (luminosité maximale), ce qui permet un réglage fin des LED du panneau avant.

#### Gestion de l'alimentation

L'outil en ligne de commande HALPI offre les fonctions de gestion de l'alimentation nécessaires à un fonctionnement sûr.

Exemples de commandes :

```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

La commande d'arrêt garantit une mise hors tension en sécurité : le système d'exploitation ferme les applications et démonte correctement les systèmes de fichiers avant que le contrôleur ne coupe l'alimentation.

#### Accès à l'API REST

Pour les utilisateurs avertis et les applications sur mesure, le démon HALPI expose également une API REST accessible par socket Unix. Elle offre un accès programmatique plus rapide aux données du système :

Quelques exemples d'utilisation :

```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

L'API REST est particulièrement utile aux applications de surveillance, aux systèmes d'enregistrement de données ou à tout logiciel devant accéder en temps réel à l'état du HALPI2.

La documentation complète de l'API REST figure au chapitre [Développement logiciel : démon HALPI2](../software-development/daemon.md).

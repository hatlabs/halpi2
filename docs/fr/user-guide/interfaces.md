---
translated_from: da8aa35c462e57bc7c0b00d50046a1df518e97dd
---

# Interfaces et connectivité

## CAN FD / NMEA 2000

Le HALPI2 dispose d'une interface [CAN FD](https://en.wikipedia.org/wiki/CAN_FD) entièrement isolée, compatible aussi bien avec les réseaux [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) de plaisance qu'avec les applications automobiles et industrielles. Elle assure une transmission de données rapide, avec une isolation électrique complète qui garantit l'immunité aux perturbations.

### Spécifications de l'interface

L'interface CAN FD prend en charge le protocole CAN standard comme le CAN FD. En usage NMEA 2000, elle fonctionne en mode CAN classique au débit normalisé de 250 kbit/s. En usage automobile ou industriel, elle peut exploiter toutes les capacités du CAN FD, jusqu'à 8 Mbit/s.

Le panneau avant est équipé d'un connecteur Micro-C compatible avec le câblage et les composants NMEA 2000 standard. L'appareil s'intègre ainsi directement aux réseaux existants à l'aide de connecteurs en T et de câbles de dérivation classiques.

### Configuration de l'alimentation et charge du réseau

L'impact du HALPI2 sur l'alimentation du réseau NMEA 2000 dépend du mode d'alimentation retenu. En configuration standard, avec une alimentation externe par le connecteur E7T, l'appareil ne prélève rien sur le réseau NMEA 2000 : son indice de charge (LEN) est donc de 0.

Lorsqu'il est alimenté par le bus NMEA 2000, son courant doit être limité à 0,9 A par le limiteur interne, ce qui correspond à un LEN de 18. Dans ce cas, raccordez l'appareil à la dorsale du réseau à proximité du câble d'alimentation, afin de limiter la chute de tension et d'assurer un fonctionnement fiable.

### Configuration matérielle

La carte porteuse comporte une résistance de terminaison de 120 Ω activable par cavalier. La terminaison au niveau de l'appareil doit être évitée en NMEA 2000, la norme ne l'autorisant pas. En revanche, pour les applications automobiles ou industrielles en liaison point à point, le cavalier peut être positionné pour activer la résistance de terminaison.

Pour le diagnostic du réseau, la carte porteuse dispose de LED RX et TX dédiées qui signalent l'activité. Elles donnent un retour visuel immédiat sur l'émission et la réception, ce qui facilite l'identification des problèmes de liaison.

### Raccordement au réseau

Le raccordement à un réseau NMEA 2000 se fait au moyen d'un connecteur en T standard (non fourni) installé sur la dorsale, et d'un câble de dérivation reliant ce connecteur au connecteur Micro-C du HALPI2.

### Intégration logicielle

L'interface CAN s'intègre nativement à Linux via le cadre SocketCAN et apparaît comme le périphérique réseau `can0`. Cette interface standard permet d'utiliser les outils CAN habituels de Linux pour la surveillance et le diagnostic. Elle est préconfigurée dans toutes les images système du HALPI2 (HaLOS, OpenPlotter et Raspberry Pi OS).

L'intégration au serveur Signal K est disponible sur les images HaLOS Marine et sur OpenPlotter : elles détectent l'interface CAN automatiquement et l'utilisent pour traiter les données NMEA 2000. Sur les images HaLOS non marines, Signal K s'installe depuis la boutique Container Apps de Cockpit. Le serveur Signal K décode les PGN et donne accès aux données du réseau en temps réel depuis un navigateur.

### Dépannage

Le diagnostic du réseau commence par les LED RX/TX de la carte porteuse. En fonctionnement normal, elles clignotent au rythme du trafic. L'absence d'activité sur la LED RX peut signaler un problème de câblage ou une terminaison incorrecte ; l'absence d'activité sur la LED TX peut évoquer un conflit sur le réseau ou un défaut de câblage.

La commande Linux `candump` permet d'observer le bus CAN directement en ligne de commande. Cet outil affiche le détail de tous les messages présents sur le bus et autorise un diagnostic approfondi. Dans sa forme la plus simple :

```bash
candump can0
```

Cette commande affiche en temps réel tous les messages CAN bruts reçus.

Le tableau de bord du serveur Signal K offre des moyens de surveillance supplémentaires. Il affiche en temps réel les débits de données NMEA 2000 issus de l'interface CAN, et son explorateur de données permet de consulter les données NMEA 2000 décodées.

!!! quote "Voir aussi"
    - **Configuration de l'alimentation :** voir [Prise en main](../getting-started/getting-started.md#installation-definitive-de-lalimentation)
    - **Mise en place logicielle :** voir le [Guide logiciel](./software.md)
    - **Dépannage réseau :** voir le [Dépannage](./troubleshooting.md)


## RS-485 (NMEA 0183)

Le HALPI2 comporte une interface [RS-485](https://en.wikipedia.org/wiki/RS-485) isolée, qui assure la liaison série avec les réseaux [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422] de plaisance et les applications industrielles.

[^rs422]: Techniquement, le NMEA 0183 s'appuie sur la norme RS-422, mais le RS-485 est rétrocompatible : le HALPI2 peut donc dialoguer avec des appareils RS-422 comme RS-485.

### Spécifications de l'interface

L'émetteur-récepteur RS-485 fonctionne jusqu'à 10 Mbit/s, même si les applications NMEA 0183 courantes utilisent les débits normalisés de 4800 ou 38400 bit/s. L'interface est isolée galvaniquement et conforme à la spécification NMEA 0183 ; elle protège le HALPI2 des boucles de masse et des perturbations électriques fréquentes en milieu marin.

Elle est raccordée en interne à l'UART 4 du Raspberry Pi et apparaît sous Linux comme `/dev/ttyAMA4`. Ce port série standard est accessible à toute application prenant en charge la liaison série, notamment le serveur Signal K, OpenCPN et vos propres logiciels.

### Configuration matérielle

La carte porteuse comporte des LED RX et TX dédiées qui signalent l'activité de l'interface RS-485. Elles donnent un retour visuel immédiat pendant l'installation et le dépannage, et permettent de vérifier facilement que les données sont bien émises et reçues.

En interface RS-485 générique, l'appareil peut être configuré en mode d'activation d'émission automatique ou manuel. En mode manuel, une broche GPIO commande le signal d'activation d'émission : le logiciel décide donc quand l'interface émet et quand elle reçoit. C'est nécessaire pour les applications multi-émetteurs, où l'interface doit rester à l'état récessif lorsqu'elle n'émet pas. En mode automatique, le matériel active lui-même le signal à l'émission des données, ce qui simplifie les montages à émetteur unique.

L'interface RS-485 prend en outre en charge le mode semi-duplex, qui lui permet d'émettre et de recevoir sur la même paire de conducteurs.

Elle peut également être entièrement désactivée par configuration matérielle si l'UART 4 est nécessaire à un autre usage.

### Câblage et raccordement

L'interface RS-485 nécessite un presse-étoupe ou un connecteur de panneau, à fournir par l'utilisateur. Le [connecteur de panneau SP13 avec queue de cochon](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug) constitue un bon choix. L'interface est rétrocompatible avec la signalisation RS-422 employée en NMEA 0183 et prend en charge aussi bien les réseaux RS-485 multi-émetteurs que les réseaux RS-422 à émetteur unique et récepteurs multiples. Elle utilise des paires différentielles symétriques, repérées TX+/TX- et RX+/RX-.

### Intégration logicielle

Toutes les images du HALPI2 sont livrées avec l'interface RS-485 prête à l'emploi. Sur les images HaLOS Marine et sur OpenPlotter, le serveur Signal K détecte l'interface automatiquement et reçoit les données NMEA 0183 émises.

Pour vos propres applications, l'interface se comporte comme un port série Linux standard. Une application peut ouvrir `/dev/ttyAMA4` et régler le débit, le nombre de bits de données, les bits d'arrêt et la parité selon les besoins de l'équipement raccordé. Les applications Python, Node.js et C/C++ y accèdent sans difficulté au moyen des bibliothèques de liaison série habituelles.

### Applications courantes

En milieu marin, l'interface RS-485 est généralement raccordée à des récepteurs GPS, des sondeurs, des girouettes-anémomètres, des transpondeurs AIS ou d'autres appareils utilisant le protocole NMEA 0183. En milieu industriel, elle peut relier des automates programmables, des capteurs et d'autres équipements d'automatisation utilisant Modbus RTU ou d'autres protocoles RS-485.

Son débit élevé autorise aussi des usages moins classiques, comme l'acquisition rapide de données de capteurs ou des protocoles de communication sur mesure, ce qui rend le HALPI2 adapté aux navires de recherche et aux applications de surveillance spécialisées.

!!! quote "Voir aussi"
    - **Configuration logicielle :** voir le [Guide logiciel](./software.md)
    - **Dépannage :** voir le [Dépannage](./troubleshooting.md)


## GNSS (GPS)

Le HALPI2 prend en charge les HAT récepteurs GNSS raccordés à l'UART0 (`/dev/ttyAMA0`). Tout récepteur GNSS branché sur ce port fonctionne avec gpsd sans configuration particulière.

Pour les récepteurs u-blox (comme le Max-M8Q), les images HaLOS Marine fournissent en outre une configuration automatique optimisée pour la navigation.

### Configuration automatique (récepteurs u-blox)

Sur les images HaLOS Marine, un service systemd (`configure-ublox-marine`) détecte et configure automatiquement les récepteurs u-blox à chaque démarrage :

| Paramètre | Valeur |
|:----------|:-------|
| Débit | 115200 bit/s (valeur d'usine : 9600) |
| Fréquence de rafraîchissement | 10 Hz (100 ms) |
| Modèle dynamique | Sea (optimisé pour la navigation) |

La configuration est réappliquée à chaque démarrage car les modules u-blox à ROM (comme le MAX-M8Q) ne disposent pas de mémoire flash. Les réglages sont conservés en mémoire vive sauvegardée par pile (BBR), qui peut se vider si l'alimentation de sauvegarde est interrompue — par exemple lorsque l'appareil reste longtemps hors tension. Cette reconfiguration est transparente et allonge le démarrage de gpsd d'environ 2 secondes.

Si aucun récepteur n'est détecté, le service s'arrête sans rien signaler. Un HAT GNSS nouvellement installé sera configuré automatiquement au redémarrage suivant.

### Accès aux données

Les données GPS sont fournies par [gpsd](https://gpsd.io/) sur le port TCP 2947. Sur les images HaLOS Marine, Signal K se connecte automatiquement à gpsd : aucune configuration supplémentaire n'est nécessaire.

Pour le diagnostic, utilisez les outils en ligne de commande fournis avec gpsd :

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Images autres que HaLOS

Sur Raspberry Pi OS ou d'autres systèmes, installez et configurez gpsd manuellement :

```bash
sudo apt install gpsd gpsd-clients
```

Modifiez `/etc/default/gpsd` pour y définir `DEVICES="/dev/ttyAMA0"`, puis redémarrez le service. Le récepteur fonctionnera avec ses réglages d'usine (9600 bit/s, 1 Hz) tant qu'il n'aura pas été configuré avec `ubxtool`, fourni par le paquet `gpsd-clients`.

!!! quote "Voir aussi"
    - **gpsd sur HaLOS :** voir la [documentation GPS de HaLOS](https://docs.halos.fi/user-guide/gps/)
    - **Mise en place logicielle :** voir le [Guide logiciel](./software.md)


## Ethernet

Le HALPI2 dispose d'une interface Ethernet gigabit qui assure une liaison réseau rapide pour le transfert de données, l'accès à distance et l'intégration aux réseaux de bord. Le port Ethernet de la carte porteuse est un connecteur RJ45 standard, déporté vers un connecteur de panneau auquel se raccorde un câble Ethernet externe.

## USB

Le HALPI2 comporte au total quatre ports USB 3.0 Type A intégrés, qui assurent une connexion rapide à toutes sortes de périphériques. Un port est relié directement à l'interface USB 3.0 du CM5, les trois autres passent par un concentrateur USB 3 embarqué. En configuration standard, deux ports sont déportés sur le panneau avant et deux restent disponibles sur la carte porteuse pour des raccordements internes.

## HDMI

Le HALPI2 comporte deux ports HDMI 2.0 (HDMI0 et HDMI1) pour la sortie vidéo. La carte porteuse propose des connecteurs FFC (câble plat souple) pour ces deux ports, déportés vers le panneau avant par des câbles FFC spécifiques. Les connecteurs du panneau avant sont des HDMI Type A classiques.

La sortie HDMI du HALPI2 gère de façon fiable deux flux vidéo Full HD (1080p). La sortie 4K peut fonctionner, mais elle n'est pas garantie.

## MIPI (CSI/DSI)

La carte porteuse comporte deux connecteurs MIPI CSI/DSI pour caméras et écrans. Ce sont des connecteurs FFC (câble plat souple) 22 broches au pas de 0,5 mm. Ils fonctionnent en principe tels quels avec les caméras et écrans récents compatibles Raspberry Pi.

Pour des raisons d'étanchéité, l'usage des câbles FFC doit rester limité aux raccordements internes.

## Boutons externes

La carte porteuse du HALPI2 comporte un connecteur 2×3 broches pour raccorder des boutons externes. Le boîtier ne comporte pas de boutons intégrés, ce qui laisse à l'utilisateur le choix de leur emplacement et de leur type.

### Brochage du connecteur de boutons

La carte porteuse comporte un connecteur 6 broches avec trois fonctions repérées :

| Repère | Fonction | Description |
|:-------|:---------|:------------|
| Reset | Réinitialisation du contrôleur | Réinitialisation matérielle (broche RUN du RP2040) |
| Power | Alimentation du Raspberry Pi | Bouton d'alimentation du CM5 (entrée PWR_BUT) |
| User | Configurable par l'utilisateur | Événement défini par l'utilisateur (non encore implémenté) |

Chaque bouton occupe deux broches : une pour le signal, une pour la masse. Utilisez des boutons-poussoirs à contact normalement ouvert (NO) reliant la broche de signal à la masse lorsqu'on appuie.

### Fonctions des boutons

**Bouton Reset :**
Le bouton de réinitialisation provoque une réinitialisation matérielle du système en tirant la broche RUN du RP2040 vers la masse. Cette action réinitialise l'ensemble : contrôleur, CM5 et tous les périphériques raccordés. Il est particulièrement utile en cas d'urgence, lorsque l'arrêt logiciel a échoué et que le système ne répond plus.

**Bouton Power :**
Le bouton d'alimentation est relié directement à l'entrée du bouton d'alimentation du CM5 et se comporte exactement comme celui d'un Raspberry Pi 5. Un double appui demande un arrêt propre du système : le système d'exploitation ferme correctement les applications et démonte les systèmes de fichiers avant la mise hors tension. Un appui long force une coupure immédiate, à n'utiliser que si le système ne répond plus.

**Bouton User :**
La fonction du bouton utilisateur attend encore son implémentation logicielle ; elle deviendra configurable dans de futures versions du firmware. Une fois disponible, ce bouton servira à déclencher des actions personnalisées et propres à chaque application, selon les besoins de l'utilisateur.

### Installation des boutons

#### Fixation directe sur le boîtier

Pour fixer un bouton directement sur le boîtier du HALPI2, utilisez les trous de 6 mm ou 13 mm déjà prévus. Retirez d'abord les bouchons obturateurs correspondants, puis installez un bouton étanche au diamètre du trou. Raccordez-le au connecteur de la carte porteuse avec un câble adapté, en veillant à un bon serre-câble et à une étanchéité durable au passage du boîtier.

#### Fixation sur un panneau déporté

Pour installer les boutons sur un pupitre de commande déporté, choisissez un emplacement facilement accessible tout en préservant l'étanchéité. Utilisez des presse-étoupe aux points d'entrée de câble et raccordez les boutons par une rallonge à conducteurs de 22 à 26 AWG, en maintenant la longueur totale sous 3 mètres pour préserver la qualité du signal. Dans les environnements humides ou sévères, utilisez des connecteurs étanches aux jonctions pour garantir un fonctionnement fiable dans la durée.

#### Raccordement

Tous les raccordements de boutons à la carte porteuse doivent utiliser des connecteurs femelles au pas de 2,54 mm. Veillez à l'alignement correct des broches et à la fermeté du raccordement, afin d'éviter les problèmes de contact en service.

!!! quote "Voir aussi"
    - **Gestion de l'alimentation :** voir [Gestion de l'alimentation et procédures d'arrêt](./operation.md#gestion-de-lalimentation-et-procedures-darret)
    - **Accès au matériel :** voir le [Guide du matériel](./hardware.md)

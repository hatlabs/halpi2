---
translated_from: 6e5802b5be19c03e5a1ca6cf292d8785a9f37601
---

# Prise en main

Ce guide vous permet de mettre le HALPI2 en service en moins de 30 minutes et couvre également l'installation définitive. Suivez les étapes dans l'ordre pour une mise en route sans accroc : commencez par un montage sur table pour vérifier que tout fonctionne, puis passez à l'installation définitive.

## Sécurité et précautions de manipulation

!!! warning "Avant de commencer"
    - Assurez-vous que l'installation électrique est hors tension avant tout raccordement
    - Utilisez des fusibles adaptés (3–5 A) pour les raccordements d'alimentation
    - Manipulez l'appareil avec soin — bien que robuste, il peut être endommagé intérieurement par une chute ou un choc
    - Vérifiez la polarité au moment de brancher les câbles d'alimentation
    - Évitez les décharges d'électricité statique — reliez-vous à la masse et évitez de frotter des chats ou de l'ambre avant de toucher les composants internes

## Ce dont vous aurez besoin

Fourni dans l'emballage du HALPI2 :

- L'unité HALPI2 avec CM5 et SSD NVMe préinstallés
- Un câble d'alimentation à connecteur E7T (2 m)

Éléments optionnels (inclus dans l'emballage de vente) :

- Une paire de connecteurs cylindriques CC (5,5 × 2,1 mm), si vous utilisez un bloc secteur 12 V standard
- L'antenne WiFi/Bluetooth Raspberry Pi (nécessaire si le WiFi sert à la configuration initiale)

À prévoir en plus (non fourni) :

- Une source d'alimentation 12 V ou 24 V
- Un autre ordinateur pour la configuration sans écran (si vous n'utilisez pas d'écran raccordé)
- Un câble réseau (facultatif, pour une liaison filaire)
- Un écran avec entrée HDMI (facultatif)
- Un clavier et une souris USB (facultatif, pour un accès direct)

!!! tip "Astuce"
    La plupart des équipements réseau, routeurs et points d'accès WiFi, utilisent une alimentation 12 V qui convient aussi au HALPI2. Fouillez votre pile de vieux matériel !

## Montage sur table

Nous recommandons d'essayer le HALPI2 sur un bureau ou un établi avant de l'installer définitivement. La configuration initiale peut se faire soit sans écran (headless), par le réseau, soit avec un écran, un clavier et une souris raccordés. Sans écran, elle peut passer par une liaison Ethernet filaire ou par le point d'accès WiFi du HALPI2.

### Étape 1 : raccorder les périphériques indispensables

#### Pour la configuration initiale :

1. **Liaison réseau (indispensable pour une installation sans écran) :**
    - Branchez le câble Ethernet
    - Branchez l'antenne WiFi/Bluetooth

2. **Raccordement d'un écran (facultatif) :**
    - Branchez un écran HDMI pour un accès direct
    - Ajoutez un clavier et une souris USB si vous utilisez un écran

![Connecteurs du panneau avant](./front-panel-connectors.jpg)
*Connecteurs du panneau avant*

### Étape 2 : raccordement NMEA 2000 (facultatif)

Si vous installez le HALPI2 directement sur un bateau, ou si vous disposez d'une installation NMEA 2000 sur table, vous pouvez déjà le raccorder au réseau NMEA 2000.

Un [réseau NMEA 2000](https://docs.hatlabs.fi/nmea2000/) se compose d'un câble dorsal auquel tous les appareils se raccordent par des connecteurs en T et des câbles de dérivation. Ajoutez un connecteur en T sur la dorsale du réseau NMEA 2000. Raccordez le connecteur micro NMEA 2000 du HALPI2 à ce connecteur en T à l'aide d'un câble de dérivation NMEA 2000.

### Étape 3 : raccordement de l'alimentation

!!! tip "À propos de l'alimentation par le NMEA 2000"
    Le HALPI2 peut aussi être alimenté par le bus NMEA 2000. Voir [Alimentation par le bus NMEA 2000](#alimentation-par-le-bus-nmea-2000), dans la section Installation définitive ci-dessous.

Pour le montage sur table, nous utiliserons le câble d'alimentation E7T fourni. Raccordez les extrémités de ses conducteurs à la fiche cylindrique femelle comme suit :

- **Conducteur rouge = pôle positif (+)**
- **Conducteur noir = pôle négatif (−)**

![Du connecteur E7T au connecteur cylindrique](./e7t-barrel.jpg)
*Exemple de câblage entre le connecteur E7T et le connecteur cylindrique*

Branchez une alimentation 12 V ou 24 V standard sur le connecteur cylindrique. Assurez-vous qu'elle est calibrée pour au moins 1 A, afin de couvrir les besoins du HALPI2.

!!! warning "Avertissement"
    Faute de serre-câble, le connecteur cylindrique à bornes à vis ne doit servir qu'à des installations temporaires. Une traction accidentelle sur le câble peut débrancher les conducteurs et les laisser à nu.

## Premier démarrage

Le HALPI2 est livré avec [HaLOS](https://docs.halos.fi), une distribution Linux à base de conteneurs, administrée depuis le web et conçue pour les applications marines et industrielles. Si vous préférez un autre système, comme OpenPlotter ou Raspberry Pi OS, voir le [Guide logiciel](../user-guide/software.md).

!!! info "Documentation HaLOS"
    Ce guide traite du matériel HALPI2 et de la première mise sous tension. Tout ce qui concerne le système d'exploitation — configuration au premier démarrage, réseau, applications, certificats et usage quotidien — se trouve dans la **[documentation HaLOS](https://docs.halos.fi)**. Gardez-la sous la main en suivant les étapes ci-dessous.

**Mettez le HALPI2 sous tension** en raccordant l'alimentation, si ce n'est déjà fait. Au bout de quelques secondes, la barre de LED doit commencer à se remplir de rouge, signe que les supercondensateurs se chargent. Les LED passent au jaune lorsque le système démarre, puis au vert lorsque le système d'exploitation fonctionne et que le démon HALPI est en liaison avec le contrôleur.

Si un écran est raccordé, vous devriez voir l'écran d'accueil de Raspberry Pi OS, puis un bureau graphique.

!!! tip "Astuce"
    Les motifs des LED d'état sont décrits dans [Utilisation quotidienne](../user-guide/operation.md#led-detat).

### Accéder au HALPI2 sans écran

Sans écran raccordé, vous pouvez accéder au HALPI2 par son point d'accès WiFi ou par une liaison Ethernet. HaLOS propose une interface web : aucun logiciel supplémentaire n'est nécessaire[^ssh].

[^ssh]: SSH est également disponible sur les images HaLOS sans écran (activé par défaut). Sur les variantes Desktop, activez SSH avec `raspi-config`. Identifiants par défaut : nom d'utilisateur `pi`, mot de passe `halos`.

Attendez d'abord que les LED passent au vert, signe que le système a complètement démarré. Procédez ensuite ainsi :

**Option 1 — connexion par le point d'accès WiFi :** HaLOS crée un point d'accès WiFi nommé `Halos-XXXX` (propre à chaque appareil), avec le mot de passe `halos1234`. Connectez votre ordinateur à ce réseau.

Ce point d'accès n'a pas d'accès Internet propre : l'étape suivante consiste donc à raccorder le HALPI2 à un réseau WiFi qui en dispose, afin de télécharger les applications conteneurisées au premier démarrage.

1. Ouvrez Cockpit sur `https://halos.local:9090/` et connectez-vous (nom d'utilisateur `pi`, mot de passe `halos`).
2. Allez dans **Networking** et cliquez sur **WiFi (wlan0)**.
3. Attendez l'affichage de la liste des réseaux disponibles, puis cliquez sur le vôtre.
4. Saisissez le mot de passe et cliquez sur **Add**.

Le HALPI2 maintient le point d'accès `Halos-XXXX` pendant qu'il rejoint votre réseau : votre ordinateur peut donc s'en déconnecter brièvement, puis s'y reconnecter tout seul.

**Option 2 — connexion par Ethernet filaire :** si vous avez raccordé le HALPI2 à votre réseau par Ethernet, il obtient automatiquement une adresse IP par DHCP.

Une fois connecté, ouvrez un navigateur et rendez-vous sur :

- **Tableau de bord :** `https://halos.local/` — le tableau de bord Homarr, avec des liens vers toutes les applications installées
- **Administration système :** `https://halos.local:9090/` — Cockpit, pour la gestion du système, les mises à jour et les applications conteneurisées

!!! note "Avertissement de certificat SSL"
    À la première ouverture du tableau de bord ou de Cockpit, votre navigateur affiche un avertissement « Non sécurisé ». HaLOS signe ses services web avec une autorité de certification (CA) qu'il génère lui-même sur l'appareil, et votre navigateur ne lui fait pas encore confiance. Acceptez l'avertissement pour continuer.

    Pour supprimer définitivement cet avertissement, installez une fois la CA de l'appareil sur votre ordinateur : tous les services HaLOS seront ensuite validés correctement, sur tous les ports. Ouvrez `https://halos.local/ca/` pour un installateur guidé selon votre système, ou consultez [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) dans la documentation HaLOS.

!!! info "Connexion Internet requise au premier démarrage"
    L'interface Cockpit est disponible immédiatement, mais le tableau de bord principal et les autres applications conteneurisées ont besoin d'une connexion Internet au premier démarrage pour télécharger leurs images de conteneur. Raccordez le HALPI2 à Internet par Ethernet, ou configurez le WiFi depuis Cockpit.

### Configuration au premier démarrage

!!! warning "Avertissement"
    HaLOS est livré avec des mots de passe par défaut qui **doivent** être changés dès le premier démarrage, afin d'empêcher tout accès non autorisé à votre appareil.

HaLOS comporte deux jeux d'identifiants :

| Type d'accès | Nom d'utilisateur | Mot de passe par défaut | Utilisé pour |
|:-------------|:------------------|:------------------------|:-------------|
| SSO (applications web) | `admin` | `halos` | Tableau de bord, Signal K, Grafana et autres applications web |
| Système (SSH/Cockpit) | `pi` | `halos` | Accès SSH, administration système dans Cockpit |

#### Changer les mots de passe

- **Mot de passe SSO :** se change depuis Authelia (accessible depuis le tableau de bord)
- **Mot de passe système :** se change dans Cockpit (`https://halos.local:9090/`), dans les paramètres du compte utilisateur, ou en SSH avec `passwd`

Pour des instructions détaillées sur le premier démarrage, voir le [guide de prise en main HaLOS](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Vous utilisez OpenPlotter ou Raspberry Pi OS ?"
    Si vous avez flashé un autre système d'exploitation, consultez le [Guide logiciel](../user-guide/software.md#configuration-initiale-du-systeme) pour les instructions de configuration propres à ce système.

### Vérifier la liaison NMEA 2000 (facultatif)

Le plus simple pour vérifier la connectivité NMEA 2000 est de consulter l'état du serveur Signal K. Sur les images HaLOS Marine, Signal K est préinstallé et accessible depuis le tableau de bord, sur `https://halos.local/`. Sur les images HaLOS non marines, Signal K s'installe depuis la boutique Container Apps de Cockpit.

Ouvrez l'interface web de Signal K et observez l'activité de la connexion `can0` : du trafic devrait apparaître en réception.

![Activité des connexions du serveur Signal K](./sk-n2k-deltas.jpg)

## Éteindre l'appareil

Le HALPI2 est conçu pour s'éteindre automatiquement lorsqu'on le débranche de son alimentation. Pour l'arrêter, coupez simplement le courant, au tableau électrique ou en débranchant le connecteur d'alimentation. Le système lance alors de lui-même une séquence d'arrêt logiciel, qui garantit la fermeture correcte des applications et le démontage sûr du système de fichiers.

Pendant l'arrêt, les LED s'atténuent d'abord (coupure détectée), passent au violet pendant le déroulement de l'arrêt, puis s'éteignent une fois celui-ci terminé. Le comportement à l'arrêt — y compris le redémarrage automatique optionnel après un arrêt logiciel — est décrit dans [Utilisation quotidienne](../user-guide/operation.md#arret).

## Dépannage de la mise en route

### Problèmes courants et moins courants

❌ **Aucune alimentation, aucune LED :**

- Vérifiez les raccordements d'alimentation et la polarité
- Contrôlez l'état du fusible
- Assurez-vous que la tension est comprise entre 10 et 32 V

❌ **Le point d'accès WiFi n'apparaît pas :**

- Vérifiez que l'antenne est correctement raccordée
- Essayez de vous connecter depuis un autre appareil
- Vérifiez que le HALPI2 a fini de démarrer (les LED doivent être vertes)
- Essayez d'abord une connexion par Ethernet

❌ **Impossible d'accéder à l'appareil par `halos.local` :**

- Essayez plutôt l'adresse IP attribuée (consultez la liste des clients DHCP de votre routeur)

❌ **Un écran est raccordé mais n'affiche rien :**

- Vérifiez que le câble HDMI est bien enfoncé
- Vérifiez que l'écran est allumé et réglé sur la bonne entrée
- Essayez un autre câble HDMI ou un autre port de l'écran
- Assurez-vous que le HALPI2 est allumé (les LED doivent être jaunes ou vertes)
- Si les LED clignotent en arc-en-ciel, le Compute Module 5 n'est pas correctement enfoncé sur la carte porteuse. Cela peut résulter d'un dommage lors du transport. Suivez les instructions du [Guide du matériel](../user-guide/hardware.md#remplacer-le-compute-module-5) pour le remettre en place, ou contactez l'assistance.

❌ **L'écran raccordé affiche un message d'erreur mentionnant « nvme » :**

- Cela signifie que le SSD NVMe n'est pas détecté ou n'est pas correctement initialisé. Cela peut résulter d'un dommage lors du transport. Suivez les instructions du [Guide du matériel](../user-guide/hardware.md#remplacer-le-ssd-nvme) pour le remettre en place, ou contactez l'assistance.

### Où trouver de l'aide

- **Documentation :** consultez les sections concernées pour un dépannage détaillé
- **Communauté :** rejoignez les forums de la communauté Hat Labs
- **Assistance :** contactez le support technique pour les problèmes matériels

---

## Installation définitive

Une fois que tout fonctionne sur votre bureau, suivez ces étapes pour la fixation et le câblage définitifs.

### Préparer l'installation

!!! tip "Astuce"
    Photographiez le câblage existant avant toute modification — cela aide beaucoup en cas de dépannage ultérieur.

Prenez le temps de préparer l'installation. Réfléchissez à :

- **L'emplacement de fixation** — accessibilité, protection, ventilation
- **Le cheminement des câbles** — trajets les plus courts, protection contre les dommages
- **La source d'alimentation** — circuit dédié ou partagé, protection par fusible
- **L'intégration au réseau** — NMEA 2000, Ethernet, couverture WiFi
- **Les contraintes d'environnement** — température, humidité, vibrations

#### Outils et fournitures nécessaires

**Outils :**

- Perceuse et forets
- Jeu de tournevis (PH2 cruciforme, gros tournevis plat)
- Pince à dénuder et pince à sertir pour les raccordements d'alimentation
- Multimètre pour les mesures
- Pistolet à air chaud ou briquet (pour la gaine thermorétractable)

**Fournitures (non incluses) :**

- Vis de fixation (4 mm ou M4, selon la surface de fixation)
- Fusibles adaptés (3–5 A) ou disjoncteurs de tableau au calibre correspondant
- Conducteur de qualité marine (1,5 mm² ou 16 AWG pour l'alimentation, si le câble fourni est trop court)
- Gaine thermorétractable et cosses
- Colliers de serrage et attaches

### Fixation

#### Choix de l'emplacement

Choisissez un emplacement de fixation qui offre :

!!! tip "Conditions de fixation idéales"
    - **Plage de température :** −20 °C … +60 °C en ambiance
    - **Ventilation :** un dégagement suffisant autour du boîtier
    - **Protection :** à l'abri des projections d'eau directes et des chocs
    - **Accessibilité :** un accès facile aux connecteurs et aux LED d'état
    - **Solidité :** une surface capable de supporter 2 kg plus les câbles
    - **Espace :** au moins 100 mm de dégagement devant les connecteurs du panneau pour le cheminement des câbles

Même si ce guide traite des installations fixes, il suffit souvent en pratique de poser l'appareil sur une étagère ou une table, à condition que l'emplacement soit stable et à l'abri de l'humidité et des chocs.

#### Recommandations selon l'environnement

**Installations sur bateau :**

- Fixez l'appareil au-dessus du niveau d'eau de cale attendu
- Évitez les zones exposées aux projections directes ou à l'eau stagnante
- Tenez compte des mouvements et des vibrations du bateau, et sécurisez tous les raccordements
- Utilisez une visserie résistante à la corrosion

**Installations automobiles :**

- Protégez l'appareil de la chaleur et des vibrations du moteur
- Assurez une ventilation suffisante dans les espaces confinés
- Prévoyez l'accès pour la maintenance
- Utilisez une fixation résistante aux vibrations

**Installations industrielles :**

- Protégez l'appareil des produits chimiques de procédé et des températures extrêmes
- Tenez compte des sources de perturbations électromagnétiques
- Assurez la conformité aux réglementations électriques locales
- Prévoyez l'accès pour la maintenance courante

#### Orientation de fixation

!!! info "Orientation recommandée"
    **À privilégier :** connecteurs vers le bas

    - Réduit le risque de pénétration d'eau
    - Facilite le cheminement des câbles
    - Facilite l'accès pour la maintenance

    **Acceptable :** connecteurs sur le côté

    - Assurez un bon écoulement de l'eau
    - Utilisez des joints d'entrée de câble

    **À éviter :** connecteurs vers le haut

    - Augmente le risque de pénétration d'eau
    - Complique le cheminement des câbles

#### Étapes de fixation

##### Étape 0 : télécharger et imprimer le gabarit de perçage

Téléchargez le [gabarit de perçage du HALPI2](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) et imprimez-le à l'échelle 100 %. Il vous aidera à marquer précisément les trous de fixation. Sans imprimante, vous pouvez aussi reporter les cotes du gabarit à la main, ou vous servir du boîtier lui-même pour marquer directement les trous sur la surface de fixation.

[![Gabarit de perçage](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Étape 1 : préparer la surface de fixation

1. **Nettoyez la surface de fixation**
2. **Marquez les trous de fixation** à l'aide du gabarit imprimé
3. **Présentez le boîtier** avant l'installation
4. **Percez les avant-trous** pour les vis de fixation

##### Étape 2 : installer le HALPI2

1. **Positionnez le boîtier**, connecteurs dans l'orientation retenue
2. **Vissez les vis de fixation** — serrées, mais sans excès

### Installation définitive de l'alimentation

#### Choix de la source d'alimentation

**Option 1 : connecteur d'alimentation dédié**

- Le plus fiable et le plus souple
- Permet d'exploiter toute la puissance disponible
- Facilite la maintenance et le dépannage

**Option 2 : alimentation par le bus NMEA 2000**

- Simplifie le câblage dans les installations nautiques
- Limitée à 0,9 A de courant absorbé
- Impose une attention particulière à la chute de tension

#### Réglage de la limitation de courant

Le HALPI2 intègre un limiteur de courant d'entrée qui gère la charge initiale des supercondensateurs et protège l'installation des surintensités. La limite se règle sur 0,9 A ou 2,5 A, selon la source d'alimentation et les besoins de l'application. Le réglage par défaut de 0,9 A convient à la plupart des usages.

Pour accélérer le démarrage initial ou alimenter des périphériques gourmands, vous pouvez passer à 2,5 A. Suivez la procédure du [Guide du matériel](../user-guide/hardware.md#reglage-de-la-limitation-de-courant) pour modifier ce réglage.

#### Raccordement à une alimentation dédiée

##### Préparation du câble

1. **Cheminez le câble d'alimentation** du HALPI2 vers la source
2. **Prévoyez des boucles de service** aux deux extrémités
3. **Protégez le câble** du frottement et des dommages
4. **Recoupez-le à la longueur voulue** en gardant une marge de travail suffisante

##### Raccordement côté source d'alimentation

1. **Assurez la protection du conducteur** en prévoyant un disjoncteur de 3–5 A ou en installant un fusible en ligne
2. **Dénudez les extrémités des conducteurs** sur la longueur voulue
3. **Posez les cosses** avec une technique de sertissage correcte
4. **Raccordez à la source d'alimentation :**
    - **Conducteur rouge :** borne positive (+)
    - **Conducteur noir :** borne négative (−)
5. **Vérifiez la polarité** au multimètre avant de mettre sous tension

##### Raccordement côté HALPI2

Le connecteur E7T est précâblé et ne demande aucun raccordement sur site. Il suffit de le brancher sur la prise d'alimentation du HALPI2.

#### Alimentation par le bus NMEA 2000

!!! info "Prérequis"
    - Le sélecteur de limitation de courant **doit** être réglé sur 0,9 A
    - Le réseau NMEA 2000 doit disposer d'une capacité d'alimentation suffisante
    - Le câble de dérivation doit être proche du point d'injection pour limiter la chute de tension

##### Composants nécessaires

- Un câble de dérivation NMEA 2000 (non fourni)
- Un connecteur en T pour le raccordement à la dorsale (non fourni)

##### Étapes d'installation

1. **Mettez hors tension** tous les appareils NMEA 2000
2. **Ouvrez le boîtier du HALPI2** (voir le [Guide du matériel](../user-guide/hardware.md#ouverture-du-boitier) pour la procédure)
3. **Repérez le connecteur d'alimentation de la carte porteuse**
4. **Débranchez le bornier en place**
5. **Raccordez le bornier d'alimentation NMEA 2000 interne** au connecteur d'alimentation de la carte porteuse
6. **Vérifiez que la limitation de courant** est bien réglée sur 0,9 A
7. **Raccordez à la dorsale** avec un câble de dérivation et un connecteur en T adaptés
8. **Testez l'installation** avant de refermer
9. **Refermez le boîtier**

![Câblage de l'alimentation NMEA 2000](./n2k-power-conx.jpg)
*Pour alimenter le HALPI2 par le NMEA 2000, débranchez le bornier 1 et remplacez-le par le bornier 2.*

### Raccordements réseau et données

#### Liaison de données NMEA 2000

Même avec une alimentation dédiée, vous pouvez souhaiter une liaison de données NMEA 2000 :

1. **Installez un connecteur en T** sur la dorsale NMEA 2000
2. **Raccordez un câble de dérivation** entre ce connecteur et le HALPI2
3. **Vérifiez la terminaison** du réseau NMEA 2000
4. **Testez la liaison** après l'installation

#### Liaison Ethernet

Pour la connectivité réseau :

1. **Utilisez un câble de qualité marine** ou adapté à l'environnement
2. **Posez des presse-étoupe ou des passe-câbles** si le câble traverse une cloison
3. **Prévoyez des boucles de service** aux deux extrémités
4. **Testez la liaison** avant l'installation définitive

#### Antenne WiFi/Bluetooth

1. **Installez l'antenne** sur le connecteur RP-SMA
2. **Placez-la pour une couverture optimale** — à l'écart des obstacles métalliques. Dans une armoire métallique, une rallonge RP-SMA mâle-femelle peut être nécessaire.
3. **Testez la puissance du signal** à l'emplacement définitif

### Dépannage de l'installation

#### Problèmes d'alimentation

❌ **Aucune indication d'alimentation :**

- Contrôlez l'état et le calibre du fusible
- Vérifiez la tension de la source (10–32 V)
- Confirmez la polarité
- Testez la continuité des câbles d'alimentation

❌ **Alimentation intermittente :**

- Vérifiez le serrage de tous les raccordements
- Recherchez des cosses corrodées
- Vérifiez que la section des conducteurs convient au courant

#### Connectivité réseau

❌ **Aucune communication NMEA 2000 :**

- Vérifiez la terminaison du réseau (120 Ω à chaque extrémité)
- Contrôlez l'installation du connecteur en T
- Vérifiez l'intégrité du câble de dérivation
- Testez avec un appareil dont le bon fonctionnement est établi

❌ **Aucune connectivité Ethernet :**

- Testez le câble avec un testeur
- Vérifiez la configuration du commutateur ou du routeur
- Recherchez des conflits d'adresses IP
- Vérifiez la catégorie du câble (Cat5e au minimum)

#### Problèmes liés à l'environnement

❌ **Pénétration d'humidité :**

- Inspectez l'état de tous les joints
- Vérifiez l'orientation des connecteurs
- Contrôlez les points d'entrée de câble
- Envisagez une protection complémentaire

❌ **Surchauffe :**

- Éloignez l'appareil des sources de chaleur
- Vérifiez que la circulation d'air autour du boîtier n'est pas entravée

### Sécurité et conformité

#### Sécurité électrique

- **Utilisez des fusibles adaptés** pour la protection contre les surintensités
- **Assurez une mise à la terre correcte** conformément aux réglementations locales
- **Protégez contre les courts-circuits** par un cheminement soigné

#### Installations sur bateau

- **Respectez les normes locales ou les normes ABYC** pour les installations électriques
- **Utilisez des composants de qualité marine** sur l'ensemble de l'installation

#### Installations industrielles

- **Respectez les réglementations électriques locales**
- **Assurez une protection EMI/RFI** suffisante
- **Documentez l'installation** selon les exigences du site

## Et ensuite

Une fois votre HALPI2 en service :

1. **Lisez [Utilisation quotidienne](../user-guide/operation.md)** pour comprendre la signification des LED et le fonctionnement de l'arrêt
2. **Explorez le [Guide logiciel](../user-guide/software.md)** pour les mises à jour, l'accès à distance et la commande `halpi`
3. **Consultez la Référence technique** pour les spécifications détaillées
4. **Rejoignez la communauté** pour des conseils, des astuces et de l'aide

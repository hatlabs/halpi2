---
translated_from: 9741366021074655d667fcf3a93a634f86f3519a
---

# Guide du matériel

## Ouverture du boîtier

Le HALPI2 est logé dans un boîtier en aluminium moulé sous pression et thermolaqué, percé pour les connecteurs de panneau. Lorsqu'une intervention interne ou une maintenance est nécessaire, ouvrez-le en suivant les procédures ci-dessous.

### Ouvrir le boîtier

Avant d'accéder aux composants internes, assurez-vous que l'appareil est complètement hors tension et que les câbles d'alimentation sont débranchés. Le couvercle est maintenu par quatre vis M4×10 à tête fraisée, empreinte PH2. Retirez-les avec un tournevis PH2, puis déposez le couvercle.

### Remontage

Avant de refermer le boîtier, vérifiez que tous les raccordements internes sont fermes et correctement engagés. Cheminez les câbles avec soin, sans les pincer ni leur imposer de coudes serrés.

Il est facile de brancher un câble plat souple (FFC) à l'envers par mégarde. Vérifiez le sens à l'aide des flèches « Contacts » de la sérigraphie.

Portez une attention particulière au joint du couvercle : recherchez tout dommage, salissure ou déplacement susceptible de compromettre l'étanchéité.

Remettez les quatre vis M4×10 du couvercle avec le tournevis PH2. Ne serrez pas excessivement.


## Connecteurs de panneau

### Configuration standard

Le HALPI2 est livré avec une configuration de connecteurs standard, adaptée à la plupart des usages. Elle comprend :

- **Connecteur d'alimentation E7T**
- **Connecteur micro NMEA 2000**
- **RJ45 Ethernet gigabit**
- **Sortie HDMI**
- **2× USB 3.0 Type-A**
- **3× emplacements de presse-étoupe PG7** (avec bouchons obturateurs)
- **2× emplacements d'antenne RP-SMA** (avec bouchons obturateurs)
- **Bouchon d'équilibrage** de pression

![Connecteurs et bouchons obturateurs du panneau avant](./front-panel-connectors-all.jpg)
*Connecteurs et bouchons obturateurs du panneau avant. Les connecteurs entourés en vert font partie de la configuration standard. Les emplacements en jaune sont des bouchons obturateurs, remplaçables par des connecteurs si besoin. L'emplacement en rouge est le bouchon d'équilibrage de pression, qui ne doit pas être retiré.*

### Autres choix de connecteurs

Si vous avez besoin d'autres types de connecteurs, la configuration du panneau peut être modifiée :

#### Retirer un connecteur

!!! warning "Important"
    N'intervenez sur les connecteurs que lorsque l'appareil est hors tension et débranché de toute source.

    Les filetages en plastique s'abîment en cas de serrage excessif. Utilisez des douilles six pans standard, mais serrez uniquement à la main.

1. **Utilisez la bonne taille de douille :**
    - Gros connecteurs : douille de 26 mm
    - Boulons nylon M6 : douille de 10 mm
    - Connecteurs RP-SMA : douille de 8 mm
    - Emplacements PG7 : gros tournevis plat, douille de 17 mm

2. **Retirez avec précaution** — les filetages en plastique s'abîment en cas de serrage excessif

3. **Conservez les pièces déposées** pour un usage ultérieur

#### Installer de nouveaux connecteurs

1. **N'utilisez que des connecteurs de qualité marine** ou adaptés à l'environnement
2. **Assurez une bonne étanchéité** — une large collerette est nécessaire côté intérieur
3. **Serrez uniquement à la main** — ne forcez pas sur les filetages en plastique
4. **Faites un essai de montage** avant l'installation définitive

## Architecture interne

- La carte porteuse du HALPI2 est la carte principale de l'ordinateur : elle reçoit le Compute Module 5 (CM5) sur sa face inférieure et assure la gestion de l'alimentation, les indicateurs et les raccordements de toutes les interfaces.

### Zones fonctionnelles de la carte porteuse

Les principales zones fonctionnelles de la carte porteuse apparaissent sur l'image ci-dessous.

![Implantation de la face supérieure de la carte porteuse](./carrier-board-top-layout.jpg)
*Implantation de la face supérieure de la carte porteuse, avec ses zones fonctionnelles.*

### Connecteurs de la carte porteuse

Les fonctions sont accessibles par un ensemble de connecteurs, présentés sur l'image ci-dessous.

![Connecteurs de la carte porteuse, face supérieure](./carrier-board-top-conx.jpg)
*Connecteurs de la carte porteuse, face supérieure.*

Voici la liste des connecteurs de la face supérieure.

| Repère | Description |
|:-------|:------------|
| **a1** | Connecteur d'alimentation (type Phoenix MC, pas de 3,81 mm) |
| **a2** | Sélecteur de limitation du courant d'entrée (0,9 A ou 2,5 A) |
| **a3** | Cavalier de commande d'alimentation. Court-circuitez les broches « 3.3V off » pour forcer la coupure de la ligne 3,3 V. Court-circuitez les broches « 5V on » pour forcer l'activation de la ligne 5 V. **NB :** sur les cartes en version 0.4.0, les connecteurs **a3** et **c2** sont disposés différemment. |
| **b1** | Port Ethernet (RJ45) |
| **c1** | Port USB du contrôleur. Sert au flashage du firmware du microcontrôleur RP2040. |
| **c2** | Connecteur à cavalier MCU USB BOOT. Court-circuitez les broches pour placer le RP2040 en mode de démarrage USB. |
| **c3** | Connecteur de débogage du contrôleur |
| **c4** | Connecteur GPIO du contrôleur, non monté |
| **c5** | Connecteurs de boutons. Servent à raccorder les boutons Power, Reset et User. |
| **c6** | Bouton d'alimentation. Sert à mettre le Compute Module 5 sous et hors tension. |
| **d1** | Connecteur GPIO 40 broches du Raspberry Pi |
| **e1** | Connecteur MIPI0 pour caméra ou écran |
| **e2** | Connecteur MIPI1 pour caméra ou écran |
| **f1** | Connecteur HDMI0 |
| **f2** | Connecteur HDMI1 |
| **g1** | Connecteur M.2 pour SSD NVMe |
| **h1** | Interface CAN FD (type Phoenix MC, pas de 3,81 mm) |
| **h2** | Cavalier de terminaison CAN. Court-circuitez les broches pour activer la terminaison du bus CAN FD. |
| **i1** | Interface RS-485 (type Phoenix MC, pas de 3,81 mm) |
| **i2** | Cavalier de mode automatique/manuel du RS-485. |
| **i4** | Cavalier XRS-485 RX Enable. Court-circuitez les broches pour activer la réception RS-485. |
| **j1** | Connecteur USB Boot du Compute Module. Sert au flashage du firmware du Compute Module 5. |
| **j2** | Sélecteur de mode de démarrage du Compute Module. Position « Normal » pour un fonctionnement normal, « Abnormal » pour le mode de démarrage USB. Une LED d'avertissement s'allume en position « Abnormal ». |
| **m1** | Connecteur USB3 0. Relié directement au CM5. |
| **m2** | Connecteur USB3 1-0. Relié au concentrateur USB3 de la carte. |
| **m3** | Connecteur USB3 1-1. Relié au concentrateur USB3 de la carte. |
| **m4** | Connecteur USB3 1-2. Relié au concentrateur USB3 de la carte. |
| **n1** | Porte-pile CR2032 pour l'horloge temps réel (RTC) |
| **q1** | Connecteur de ventilateur du CM5. Le ventilateur peut améliorer la circulation d'air dans le boîtier. Il est inutile avec le boîtier standard. |

![Connecteurs de la carte porteuse, face inférieure](./carrier-board-bottom-conx.jpg)
*Connecteurs de la carte porteuse, face inférieure.*

Voici la liste des connecteurs de la face inférieure.

| Repère | Description |
|:-------|:------------|
| **p1** | Connecteur du Compute Module 5. |
| **q1** | Connecteur de ventilateur du CM5, emplacement alternatif. Il permet de raccorder un ventilateur au-dessus du module CM5 lors de l'utilisation d'un boîtier sur mesure. **NB :** les connecteurs **q1** et **q2** sont câblés en parallèle et ne doivent pas être utilisés simultanément. |

Enfin, le connecteur d'antenne WiFi et Bluetooth se trouve sur le Compute Module 5 lui-même. Il apparaît sur l'image ci-dessous.

![Connecteur d'antenne WiFi](./cm5-top-conx.jpg)
*Connecteur d'antenne U.FL sur le Compute Module 5.*

| Repère | Description |
|:-------|:------------|
| **r1** | Connecteur U.FL pour l'antenne WiFi et Bluetooth. |

### Blinkenlights

La carte porteuse comporte plusieurs LED d'état pour la surveillance du système.

![LED d'état de la carte porteuse](./carrier-board-top-leds.jpg)
*LED d'état de la carte porteuse et leurs couleurs.*

Les LED d'état renseignent sur l'alimentation et l'activité du système. En voici la liste.

| Repère | Couleur | Description |
|--------|:--------|:------------|
| **1** | RGB | Cinq LED RGB. Elles indiquent l'état et l'activité du système sur le panneau avant. |
| **2** | Rouge | LED d'alimentation des lignes 3,3 V et 5 V. Elles indiquent l'état de ces lignes. |
| **3** | Jaune | Indicateur de débit Ethernet. Allumé lorsque le port Ethernet a négocié une liaison à 100/1000 Mbit/s. |
| **4** | Vert | Indicateur d'activité Ethernet. Clignote en présence de trafic sur le port Ethernet. |
| **5** | Bleu | Indicateur d'activité du SSD. Clignote lors des lectures et écritures sur le SSD NVMe M.2. |
| **6** | Rouge | Indicateur d'alimentation du Pi. Allumé lorsque le système est alimenté mais éteint. |
| **7** | Vert | Indicateur d'activité du Pi. Clignote en cas d'activité sur le Raspberry Pi. |
| **8** | Ambre | Avertissement de mode de démarrage « Abnormal ». Allumé lorsque le sélecteur de démarrage USB est sur « Abnormal ». Il signale que l'appareil est configuré pour être flashé par le connecteur USB Boot et ne démarrera pas normalement. |
| **9** | Vert | LED TX/RX du CAN. Elles clignotent à la réception (RX) ou à l'émission (TX) de données sur l'interface CAN. |
| **10** | Vert | LED TX/RX du RS-485. Elles clignotent à la réception (RX) ou à l'émission (TX) de données sur l'interface RS-485. |

Les motifs des LED RGB sont décrits dans le [Fonctionnement du système](./operation.md#led-detat).

## Réglage de la limitation de courant

La carte porteuse comporte un sélecteur de limitation de courant qui fixe le courant maximal fourni aux périphériques. Pour le localiser, repérez le sélecteur **a2** sur l'image de la section [Connecteurs de la carte porteuse](#connecteurs-de-la-carte-porteuse).

!!! info "Réglages de limitation de courant"
    **0,9 A (par défaut) :**

    - Obligatoire pour l'alimentation par le bus NMEA 2000
    - Convient au fonctionnement de base

    **2,5 A :**

    - Pour les périphériques gourmands
    - Charge plus rapide des supercondensateurs
    - Uniquement avec une alimentation dédiée

Pour modifier ce réglage, mettez d'abord le HALPI2 complètement hors tension et déposez le couvercle du boîtier en suivant la procédure de la section Ouverture du boîtier. Repérez le sélecteur de limitation de courant sur la carte porteuse et placez-le sur la position voulue (0,9 A ou 2,5 A). Une fois le réglage modifié, refermez le boîtier en vérifiant que tous les raccordements restent fermes.

## Utiliser des HAT

### Compatibilité des HAT

Le HALPI2 prend en charge les HAT Raspberry Pi standard par son connecteur GPIO 40 broches, en pleine compatibilité électrique et mécanique avec la spécification HAT du Raspberry Pi. La carte porteuse reprend le même brochage GPIO qu'un Raspberry Pi standard, ce qui permet à la plupart des HAT conçus pour les Raspberry Pi 4 et 5 de fonctionner sans modification. Cela vaut aussi bien pour les HAT officiels Raspberry Pi que pour les cartes d'extension tierces respectant la norme HAT.

### Contraintes physiques

Le boîtier du HALPI2 offre 45 mm de hauteur libre au-dessus de la carte porteuse, ce qui permet d'empiler jusqu'à deux HAT. La zone située à gauche de l'emplacement HAT est occupée par les supercondensateurs, ce qui restreint la place disponible pour les HAT dépassant l'encombrement standard de 65 × 56 mm. Soyez attentif aux HAT dotés de connecteurs latéraux : ceux orientés vers le « sud » ou l'« est » ne posent en principe pas de problème, mais ceux orientés vers l'« ouest » risquent de buter sur les supercondensateurs.

### Conflits de broches GPIO

Plusieurs broches GPIO sont utilisées par les interfaces intégrées du HALPI2 et doivent être prises en compte au moment de choisir un HAT. Le tableau suivant détaille les broches réservées et leurs fonctions :

| Numéro GPIO | Fonction | Interface | Remarques |
|-------------|----------|-----------|-----------|
| GPIO 2 | I2C SDA | I2C système | Partageable ; adresse 0x6d réservée |
| GPIO 3 | I2C SCL | I2C système | Partageable ; adresse 0x6d réservée |
| GPIO 6 | SPI CS | CAN FD | Sélection de puce dédiée au contrôleur CAN |
| GPIO 9 | SPI MISO | CAN FD | Bus SPI0 partagé |
| GPIO 10 | SPI MOSI | CAN FD | Bus SPI0 partagé |
| GPIO 11 | SPI SCK | CAN FD | Bus SPI0 partagé |
| GPIO 12 | UART TX | RS-485 | Émission de l'UART4 |
| GPIO 13 | UART RX | RS-485 | Réception de l'UART4 |
| GPIO 24 | RS-485 EN | RS-485 | Signal d'activation (mode manuel uniquement) |
| GPIO 26 | CAN INT | CAN FD | Ligne d'interruption du contrôleur CAN |

### Partage des interfaces et conflits

Le bus I2C sur GPIO 2 et 3 peut être partagé avec des HAT, l'I2C acceptant plusieurs appareils sur un même bus. Les HAT ne doivent toutefois pas utiliser l'adresse I2C 0x6d, réservée au contrôleur système du HALPI2. La plupart des HAT I2C fonctionnent sans difficulté, mais vérifiez les adresses utilisées avant l'installation.

Le bus SPI0 employé par l'interface CAN FD peut éventuellement être partagé avec d'autres périphériques SPI, le HALPI2 utilisant des broches de sélection de puce (GPIO 6) et d'interruption (GPIO 26) qui lui sont propres. Les HAT utilisant SPI0 avec les broches de sélection standard (GPIO 7 ou GPIO 8) peuvent cohabiter avec l'interface CAN, mais peuvent demander une configuration supplémentaire par overlay de device tree.

### Désactiver les interfaces intégrées

Si un HAT exige l'usage exclusif de broches occupées par les interfaces intégrées du HALPI2, ces interfaces peuvent être désactivées par modification matérielle. L'interface CAN FD se libère entièrement en retirant le cavalier soudé GPIO6-CAN.CS, situé sur la face inférieure de la carte porteuse. Cette modification déconnecte le contrôleur CAN du bus SPI et libère les GPIO 6, 9, 10, 11 et 26 pour le HAT.

L'interface RS-485 se désactive en retirant le cavalier RX Enable (i4) de la carte porteuse. Le récepteur RS-485 ne reçoit alors plus de données et les GPIO 12 et 13 sont libérés. Si la commande manuelle d'activation d'émission n'est pas nécessaire, le GPIO 24 peut également être réaffecté en plaçant le cavalier automatique/manuel du RS-485 (i2) en mode automatique.

### Procédure d'installation

Commencez par mettre le système hors tension et débrancher toutes les sources d'alimentation. Déposez le couvercle du boîtier en suivant la procédure de la section Ouverture du boîtier.

Les cartes porteuses en version 0.5.0 et ultérieures comportent des inserts filetés M2.5 préinstallés aux quatre points de fixation des HAT, ce qui simplifie le montage. Les cartes v0.4.0 antérieures imposent de poser les écrous M2.5 à la main, ce qui suppose de déposer temporairement la carte porteuse — sans nécessairement débrancher tous les câbles.

Pour de nombreux HAT courants, des entretoises de 15 mm conviennent, mais mesurez la hauteur du connecteur femelle du HAT pour vérifier le dégagement. L'embase du connecteur mâle mesure 2,5 mm de haut : ajoutez cette valeur à la hauteur du connecteur femelle pour déterminer la longueur d'entretoise nécessaire.

Vissez les entretoises dans les trous de fixation, ou fixez-les par des écrous depuis le dessous sur les cartes v0.4.0. Alignez le HAT sur le connecteur GPIO 40 broches en vérifiant la position de toutes les broches, puis appuyez uniformément pour engager le connecteur. Le HAT doit reposer parallèlement à la carte porteuse, sans jeu visible au niveau du connecteur GPIO.

Fixez le HAT avec des vis M2.5 ou des entretoises supplémentaires, à travers ses trous de fixation. Ces vis ne sont pas fournies avec le HALPI2 et doivent être achetées séparément. Serrez juste assez pour immobiliser le HAT, sans faire fléchir le circuit imprimé.

### Cheminement des câbles

Si le HAT comporte des connecteurs devant être accessibles depuis l'extérieur du boîtier, envisagez d'installer des connecteurs de panneau adaptés dans les emplacements de presse-étoupe PG7 disponibles. La protection du boîtier est ainsi préservée tout en offrant un accès extérieur commode.

### Procédure de dépose

La dépose d'un HAT reprend la procédure d'installation en sens inverse. Mettez le système complètement hors tension et débranchez toutes les sources d'alimentation avant d'ouvrir le boîtier. Retirez les vis de fixation M2.5 et soulevez le HAT bien droit hors du connecteur GPIO, en évitant tout effort latéral susceptible de tordre les broches.

Si le HAT semble coincé, vérifiez qu'aucune vis ni aucun câble n'a été oublié avant de forcer davantage. Certains HAT à connecteurs serrés demandent un léger balancement pendant la traction. Balancez le HAT dans l'axe nord-sud ; un balancement est-ouest risquerait de tordre les broches au moment où le connecteur se libère brusquement.

### Configuration logicielle

Après l'installation matérielle, le HAT peut nécessiter une configuration logicielle pour fonctionner. Beaucoup de HAT s'accompagnent d'overlays de device tree à activer dans la configuration du Raspberry Pi. Modifiez `/boot/firmware/config.txt` en y ajoutant les lignes `dtoverlay` indiquées dans la documentation de votre HAT.

!!! quote "Voir aussi"
    - **Brochage GPIO :** voir la [Référence matérielle](../technical-reference/hardware.md)
    - **Configuration logicielle :** voir la [Configuration avancée](../software-development/advanced-config.md)
    - **Modifications du boîtier :** voir [Autres choix de connecteurs](#autres-choix-de-connecteurs)

## Remplacer le SSD NVMe

### Compatibilité des SSD

Le HALPI2 accepte les SSD NVMe M.2 aux formats 2230 à 2280, en configuration simple face standard. Les modèles courts 2230 peuvent être double face, le dégagement étant suffisant à cet emplacement, mais les modèles plus longs doivent être simple face pour tenir sur la carte porteuse.

La compatibilité n'est garantie qu'avec les SSD fournis par Hat Labs et les SSD officiels Raspberry Pi. Si vous envisagez un modèle tiers, vérifiez avant l'achat sa compatibilité avec le Raspberry Pi 5, en consultant les retours d'utilisateurs et les listes de compatibilité en ligne. Les modèles incompatibles provoquent fréquemment une consommation excessive, une surchauffe, des échecs de démarrage ou une instabilité du système.

### Préparer le nouveau SSD

Avant d'installer un nouveau SSD dans le HALPI2, il convient d'y flasher le système d'exploitation. Il est possible de flasher le SSD après installation, via le connecteur USB Boot du CM5 (j1), mais un adaptateur USB-NVMe externe est plus simple et plus rapide. La procédure de flashage est décrite dans le [Guide logiciel](./software.md).

### Couper la tension système de 3,3 V

Les supercondensateurs peuvent maintenir la ligne 3,3 V de la carte porteuse sous tension pendant un temps appréciable après la coupure de l'alimentation principale. Le SSD étant alimenté par cette ligne, elle doit être coupée pour garantir que le SSD est totalement hors tension avant toute dépose ou installation.

Commencez par mettre le HALPI2 hors tension et débrancher l'alimentation. Ouvrez le boîtier en suivant la procédure de la section Ouverture du boîtier.

Repérez le cavalier « 3.3V off » sur la carte porteuse. Son emplacement varie selon la version de la carte. Sur les cartes v0.4.0, il se trouve tout près des supercondensateurs, du côté « sud ». À partir de la v0.5.0, repérez le connecteur « Pow.Ctrl » à l'« est » des supercondensateurs : les broches « 3.3V off » sont les deux broches supérieures.

Placez le cavalier de façon à court-circuiter les broches « 3.3V off ». La ligne 3,3 V est alors coupée, ce que confirme l'extinction des LED.

### Procédure de dépose

L'emplacement M.2 se trouve sur le bord « sud » de la carte porteuse. Repérez le connecteur M.2 marqué **g1** sur l'image de la section [Connecteurs de la carte porteuse](#connecteurs-de-la-carte-porteuse).

À l'aide d'un tournevis PH1, retirez la vis de fixation M2.5. Une fois la vis ôtée, le SSD se relève en biais. Soulevez-le doucement par son extrémité de fixation et dégagez-le du connecteur M.2 par de petits mouvements. Manipulez le SSD par les bords pour ne pas endommager les composants ni les connecteurs.

### Procédure d'installation

Insérez le SSD préparé dans le connecteur M.2 avec un angle d'environ 30 degrés, en veillant à ce que son détrompeur corresponde à celui du connecteur. Le module doit glisser sans forcer. Une fois bien engagé, rabattez son extrémité de fixation à plat contre l'entretoise.

Fixez le SSD avec la vis M2.5 à l'aide d'un tournevis PH1. Serrez juste assez pour l'immobiliser fermement. Le SSD doit reposer parfaitement à plat, sans courbure ni flexion visible.

Une fois le SSD en place, retirez le cavalier des broches « 3.3V off » pour rétablir la ligne 3,3 V. Conservez le cavalier sur le connecteur pour un usage ultérieur.

Refermez le boîtier comme indiqué à la section Ouverture du boîtier. Pour la configuration logicielle et le dépannage, reportez-vous au [Guide logiciel](./software.md).

!!! quote "Voir aussi"
    - **Images système :** voir le [Guide logiciel](./software.md)
    - **Procédures de démarrage :** voir [Fonctionnement du système](./operation.md)
    - **Accès au matériel :** voir [Ouverture du boîtier](#ouverture-du-boitier)

## Remplacer le Compute Module 5

### Prérequis

Le remplacement du Compute Module 5 demande de la précaution : les connecteurs carte à carte sont fragiles. Le CM5 utilise deux connecteurs haute densité qui s'endommagent facilement en cas d'effort excessif ou de mauvaise technique. Ne déposez un module installé que si c'est indispensable, par exemple s'il est endommagé ou doit être remplacé par un modèle supérieur. Les dommages aux connecteurs de fixation du Compute Module, côté CM5 comme côté carte porteuse, ne sont pas couverts par la garantie.

Avant de commencer, prévoyez des pads thermiques pour le transfert de chaleur. La configuration standard utilise un pad de 1 mm d'épaisseur sur le SoC et des pads de 2 mm sur la puce RP1 et les composants d'alimentation internes. Les pads existants peuvent être réutilisés s'ils sont intacts et propres.

### Accéder au Compute Module

Mettez le HALPI2 hors tension et débranchez la source d'alimentation. Déposez le couvercle du boîtier en suivant la procédure de la section Ouverture du boîtier. Le CM5 étant monté sous la carte porteuse, il faut d'abord déposer celle-ci du boîtier. De nombreux câbles y sont raccordés : prenez quelques photos des connexions avant de poursuivre.

Débranchez les câbles qui empêchent de soulever la carte porteuse. Retirez ses vis de fixation et sortez-la du boîtier.

### Déposer le module existant

!!! danger "Attention"
    Si le module CM5 est débranché un connecteur à la fois, les efforts de torsion peuvent arracher le connecteur du module. Ce dommage n'est pas couvert par la garantie.

Le CM5 est maintenu par deux connecteurs carte à carte qui exigent des précautions. N'utilisez jamais d'outil métallique : il pourrait endommager les connecteurs ou les composants montés en surface à proximité. Employez un outil d'ouverture en bois ou en plastique, un médiator de guitare ou tout autre outil non conducteur équivalent.

Placez l'outil au milieu du petit côté gauche du module CM5, entre le module et la carte porteuse. Appuyez fermement sur les angles du côté droit. Faites levier doucement vers le haut, avec un minimum d'effort : le module doit se libérer dans un léger déclic, les deux connecteurs se détachant simultanément.

![Dépose du module CM5](./unmount-cm5.jpg)
*Déposez le module CM5 en appuyant sur les angles du bord droit tout en faisant levier vers le haut au milieu du bord gauche. Les deux connecteurs doivent se détacher en même temps.*

### Installer le nouveau module

Alignez le nouveau module CM5 sur les connecteurs de la carte porteuse, en vous guidant sur le contour sérigraphié. Ce contour imprimé doit correspondre exactement aux dimensions du CM5 lorsqu'il est correctement orienté.

Une fois l'alignement fait, appuyez doucement et uniformément à l'emplacement des connecteurs, sur les deux petits côtés du module. Vous devez sentir les connecteurs s'engager dans un léger déclic. Appuyez fermement mais évitez de faire fléchir la carte porteuse — soutenez-la par en dessous si nécessaire. Les deux connecteurs doivent être complètement engagés pour un fonctionnement correct.

Posez ensuite les pads thermiques sur le module CM5, aux bons emplacements : un pad de 1 mm sur le SoC principal, des pads de 2 mm sur la puce RP1 et sur les composants d'alimentation. Si vous réutilisez d'anciens pads, vérifiez qu'ils sont propres et correctement positionnés.

![Positionnement des pads thermiques sur le CM5](./cm5-thermal-pads-annotated.jpg)
*Positionnement des pads thermiques sur le Compute Module 5. Utilisez un pad de 1 mm d'épaisseur sur le SoC (au centre) et des pads de 2 mm sur le RP1 et les composants d'alimentation. Les formes et dimensions réelles des pads peuvent varier.*

### Raccordement de l'antenne

Avant de remonter la carte porteuse, raccordez le câble d'antenne U.FL au connecteur d'antenne du CM5. Ce raccordement devient impossible une fois la carte porteuse reposée. Le connecteur U.FL exige un alignement précis et une pression ferme pour s'engager correctement : vous devez sentir un déclic net. Veillez à ne pas déformer la coque du connecteur pendant l'opération.

### Assemblage final

Vérifiez l'installation du module : les deux connecteurs doivent être complètement engagés et le module doit reposer à plat contre la carte porteuse, sans jeu. Les pads thermiques doivent toucher les composants qui dégagent de la chaleur.

Replacez la carte porteuse dans le boîtier en veillant à ce que les pads thermiques du CM5 coïncident avec les zones de dissipation correspondantes du fond du boîtier. Remettez toutes les vis de fixation de la carte porteuse et rebranchez les câbles débranchés lors de la dépose.

Terminez le remontage selon la procédure habituelle de fermeture du boîtier. Au premier démarrage, le système doit reconnaître automatiquement le nouveau CM5.

!!! warning "Avertissement sur les connecteurs"
    Les connecteurs carte à carte sont les éléments les plus fragiles de cette opération. N'utilisez jamais d'outil métallique à proximité, n'appliquez qu'un effort vertical à la dépose comme à l'installation, et vérifiez l'alignement avant d'appuyer. Un connecteur endommagé impose généralement le remplacement de la carte porteuse.

!!! quote "Voir aussi"
    - **Mise en service après remplacement :** voir le [Guide logiciel](./software.md)
    - **Dépannage du démarrage :** voir le [Dépannage](./troubleshooting.md)
    - **Gestion thermique :** voir la [Référence matérielle](../technical-reference/hardware.md)

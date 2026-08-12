---
translated_from: 20e29f3f3d0abb0b55c899b0dec2e915f0574e19
---

# Référence matérielle

Cette page rassemble les spécifications électriques, mécaniques et environnementales du HALPI2. Pour les procédures (installation, maintenance, remplacement), voir le [Guide du matériel](../user-guide/hardware.md). Pour le détail des protocoles d'interface, voir [Interfaces et connectivité](./interfaces.md).

## Spécifications en bref

| Paramètre | Valeur |
|:----------|:-------|
| Module de calcul | Raspberry Pi CM5 (compatible CM4) |
| Contrôleur de la carte porteuse | RP2040 (Arm Cortex-M0+, double cœur, 133 MHz) |
| Tension d'entrée | 10–32 V CC (maximum absolu 38,6 V, protection transitoire jusqu'à 100 V) |
| Consommation | de 250 mA au repos à 590 mA en charge (entrée 12 V, HaLOS sans écran) |
| Réglages de limitation de courant | 0,9 A ou 2,5 A (au choix) |
| Sauvegarde par supercondensateurs | 4× 25 F / 2,7 V en série (6,25 F effectifs à 10,8 V max) |
| Température de fonctionnement | −20 °C … +60 °C |
| Dimensions du boîtier | 200 × 130 × 60 mm (hors connecteurs) |
| Masse du boîtier | TODO |
| Matériau du boîtier | Aluminium moulé sous pression, thermolaqué |
| Indice de protection | IP65 |
| Licence | CERN-OHL-S v2 (matériel) |

## Spécifications électriques

### Alimentation

L'alimentation accepte une large plage de tension continue et fournit des lignes régulées 5 V et 3,3 V au CM5 et aux périphériques. La protection d'entrée comprend une protection contre l'inversion de polarité (LM74800), une coupure en surtension à 38,6 V, un écrêtage TVS et un filtrage EMI en mode commun et différentiel.

| Paramètre | Valeur |
|:----------|:-------|
| Tension d'entrée recommandée | 10–32 V CC |
| Tension d'entrée maximale absolue | 38,6 V (continu), 100 V (transitoire, limité par TVS) |
| Courant d'entrée maximal | 0,9 A ou 2,5 A (limiteur de courant au choix) |
| Fusible d'entrée | 7 A (protection contre les défauts uniquement) |
| Ligne intermédiaire 10 V | 10,25 V nominal (convertisseur abaisseur SiC463ED) |
| Ligne 5 V | 5,1 V / 4 A (TPS566238, alimente le CM5 et les ports USB) |
| Ligne 3,3 V | 3,33 V / 3 A (TPS566238, commandée par le contrôleur à partir de la v0.6.0) |
| Seuil de sous-tension 3,3 V | 4,5 V aux supercondensateurs |
| LDO 3,3 V de démarrage | SE8633K2 (démarrage du contrôleur et de l'équilibrage des supercondensateurs) |

### Sauvegarde par supercondensateurs

Le banc de supercondensateurs fournit l'énergie de secours nécessaire à un arrêt propre en cas de perte d'alimentation.

| Paramètre | Valeur |
|:----------|:-------|
| Configuration | 4 cellules 25 F / 2,7 V en série |
| Capacité effective | 6,25 F à 10,8 V maximum |
| Équilibrage | Équilibrage actif |
| Plage de tension de charge | 0–10,8 V (surveillée par le convertisseur analogique-numérique du contrôleur) |
| Seuil de mise sous tension | 8,0 V (configurable dans le firmware) |
| Seuil de mise hors tension | 5,5 V (configurable dans le firmware) |

### Consommation de courant

Mesures effectuées sous 12 V avec un Raspberry Pi CM5 exécutant l'image HaLOS sans écran.

| Situation | Courant absorbé |
|:----------|:----------------|
| Système au repos | environ 250 mA |
| Charge typique | environ 400 mA |
| Charge maximale | environ 590 mA |

!!! note
    Ces mesures excluent la consommation des périphériques USB externes. Chaque port USB 3.0 peut fournir jusqu'à 0,93 A ; la consommation totale du système dépend donc fortement des périphériques raccordés.

## Brochages des connecteurs

### Connecteur d'entrée d'alimentation

Type Phoenix MC, pas de 3,81 mm, 2 broches. Sur le panneau avant, le connecteur cylindrique E7T se raccorde à ce connecteur.

| Broche | Fonction |
|:-------|:---------|
| 1 | GND |
| 2 | VIN (10–32 V CC) |

### Connecteur CAN FD

Type Phoenix MC, pas de 3,81 mm, 4 broches. Isolé galvaniquement.

| Broche | Fonction |
|:-------|:---------|
| 1 | GND_CAN (masse isolée) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Le cavalier de terminaison (repère « 120R ») insère une résistance de terminaison de 120 Ω entre CAN_H et CAN_L.

### Connecteur RS-485

Type Phoenix MC, pas de 3,81 mm, 5 broches. Isolé galvaniquement.

| Broche | Fonction |
|:-------|:---------|
| 1 | GND_RS485 (masse isolée) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Connecteur de boutons

Connecteur 2×3 broches, pas de 2,54 mm. Chaque paire de broches associe la masse et un signal.

| Paire de broches | Fonction |
|:-----------------|:---------|
| Power | Bouton d'alimentation du CM5 (double appui = arrêt, appui long = coupure forcée) |
| Reset | Réinitialisation matérielle du RP2040 (broche RUN) |
| User | Configurable par l'utilisateur (en attente d'implémentation dans le firmware) |

### Connecteurs HDMI (HDMI0, HDMI1)

Connecteurs FPC horizontaux 20 broches, pas de 0,5 mm (FPC0.5-SMT-20P). Chaque canal dispose d'une protection ESD (RCLAMP0524P) et d'une alimentation 5 V à courant limité (AP2553W6-7).

### Connecteurs MIPI CSI/DSI (MIPI0, MIPI1)

Connecteurs FPC horizontaux 22 broches, pas de 0,5 mm. Chaque canal dispose d'une protection ESD (RCLAMP0524P). Compatibles avec les caméras et écrans Raspberry Pi.

### Emplacement M.2 NVMe (PCIe M.2 M-key)

Emplacement M.2 Socket M pour SSD NVMe, formats 2230 à 2280. Raccordé en PCIe Gen 2 x1. Comprend un oscillateur SUSCLK dédié pour la compatibilité avec la mise en veille des SSD NVMe (ajouté en v0.6.1).

### Connecteurs de ventilateur (CM5 Fan)

Connecteurs de ventilateur PWM 4 broches (HC-1.0-4PLT), présents sur les faces supérieure et inférieure de la carte porteuse. Ils sont raccordés en parallèle : n'en utilisez qu'un seul à la fois.

| Broche | Fonction |
|:-------|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### Ports USB 3.0

| Connecteur | Raccordement | Limite de courant |
|:-----------|:-------------|:------------------|
| USB3-0 | Directement à l'USB 3.0 du CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | Port 1 du concentrateur USB3 (UPD720210) | 0,93 A |
| USB3-1-1 | Port 2 du concentrateur USB3 | 0,93 A |
| USB3-1-2 | Port 3 du concentrateur USB3 | 0,93 A |

Tous les ports disposent d'une protection ESD (RCLAMP0524P) et d'un filtrage par perles de ferrite.

### Port USB du contrôleur (MCU USB)

Prise micro-USB, mode périphérique USB 2.0 uniquement. Sert aux mises à jour du firmware du RP2040 (flashage UF2). Protégé contre les décharges électrostatiques (RCLAMP0524P).

### Port de démarrage USB (USB Boot)

Prise USB Type-C, mode périphérique USB 2.0. Raccordée au port USB 2.0 OTG du CM5 pour le démarrage depuis un périphérique de stockage USB. Protégé contre les décharges électrostatiques (RCLAMP0524P).

## Connecteur GPIO 40 broches (Raspberry Pi GPIO Header)

Le connecteur GPIO suit le brochage standard 40 broches du Raspberry Pi. Les broches suivantes sont utilisées par les périphériques intégrés du HALPI2 :

| GPIO | Broche | Fonction | Interface | Partagée ? |
|:-----|:-------|:---------|:----------|:-----------|
| 2 | 3 | I2C1 SDA | I2C système | Oui (adresse 0x6d réservée) |
| 3 | 5 | I2C1 SCL | I2C système | Oui (adresse 0x6d réservée) |
| 6 | 31 | SPI0 CS | Contrôleur CAN FD | Sélection dédiée — peut coexister avec les broches CS standard |
| 9 | 21 | SPI0 MISO | Contrôleur CAN FD | Bus SPI0 partagé |
| 10 | 19 | SPI0 MOSI | Contrôleur CAN FD | Bus SPI0 partagé |
| 11 | 23 | SPI0 SCLK | Contrôleur CAN FD | Bus SPI0 partagé |
| 12 | 32 | UART4 TX | RS-485 | Libre si le RS-485 est désactivé |
| 13 | 33 | UART4 RX | RS-485 | Libre si le RS-485 est désactivé |
| 24 | 18 | RS-485 EN | RS-485 (mode manuel) | Libre en mode automatique |
| 26 | 37 | CAN INT | Contrôleur CAN FD | Non |

Toutes les autres broches GPIO restent disponibles pour les HAT et les applications de l'utilisateur. Le [Guide du matériel](../user-guide/hardware.md#utiliser-des-hat) détaille la compatibilité des HAT et la désactivation des interfaces intégrées.

## Périphériques I2C

Le bus I2C système (I2C1, GPIO 2/3) accueille un seul périphérique intégré :

| Adresse | Périphérique | Fonction |
|:--------|:-------------|:---------|
| 0x6d | RP2040 | Contrôleur de la carte porteuse (mode esclave) |

Les connecteurs MIPI et HDMI utilisent des bus distincts. I2C0 (SDA0/SCL0 du CM5) dessert MIPI0. MIPI1 utilise les broches ID_SD/ID_SC du CM5 via des résistances de 0 Ω, avec des résistances de tirage de 2,2 kΩ. Le DDC HDMI passe par des broches dédiées du CM5 jusqu'aux connecteurs HDMI.

## Architecture d'isolation

Les interfaces CAN FD et RS-485 sont isolées galvaniquement du reste du système. Chaque interface dispose de son alimentation isolée (convertisseur B0505S-1WR3) et de son isolation de signal.

| Interface | Isolation du signal | Isolation de l'alimentation | Masse isolée |
|:----------|:--------------------|:----------------------------|:-------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Les défauts de bus, les boucles de masse et les perturbations présentes sur les réseaux CAN ou RS-485 ne peuvent donc ni endommager le système principal ni en perturber le fonctionnement.

## Spécifications mécaniques

### Boîtier

| Paramètre | Valeur |
|:----------|:-------|
| Matériau | Aluminium moulé sous pression, thermolaqué |
| Dimensions | 200 × 130 × 60 mm (hors connecteurs) |
| Masse | TODO |
| Indice IP | IP65 |
| Hauteur libre au-dessus de la carte porteuse | 45 mm (permet d'empiler jusqu'à deux HAT) |
| Vis du couvercle | 4× M4×10 à tête fraisée, empreinte PH2 |
| Joint | Joint de couvercle pour l'étanchéité |
| Équilibrage de pression | Bouchon d'équilibrage (ne doit pas être retiré) |

### Emplacements du panneau

Le panneau avant comporte des emplacements prépercés pour :

- 1× connecteur d'alimentation E7T
- 1× connecteur NMEA 2000 Micro-C
- 1× RJ45 Ethernet
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× connecteur d'antenne RP-SMA (WiFi/Bluetooth)
- 2× emplacements d'antenne SMA (livrés avec bouchons obturateurs)
- 1× bouchon d'équilibrage de pression
- 3× emplacements de presse-étoupe PG7 (livrés avec bouchons obturateurs)

### Fixation

- Fixation de la carte porteuse : 4 vis M4×6 sur le fond du boîtier
- Fixation des HAT : 4 inserts filetés M2.5 (à partir de la v0.5.0 ; la v0.4.0 impose de poser les écrous à la main)
- Fixation du CM5 : 4 écrous à souder M2.5

## Gestion thermique

Le CM5 est monté sous la carte porteuse. La chaleur du SoC et du jeu de composants RP1 est transférée par des pads thermiques vers le fond du boîtier en aluminium, qui fait office de dissipateur.

| Composant | Épaisseur du pad thermique |
|:----------|:---------------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Composants d'alimentation | 2 mm |

Le boîtier standard assure un refroidissement passif, sans ventilateur. Un connecteur de ventilateur PWM 4 broches est disponible pour les boîtiers sur mesure ou les applications à température ambiante élevée.

!!! quote "Voir aussi"
    - **Schémas et fichiers de conception :** voir [Fichiers de conception et schémas](../appendices/design-files.md)
    - **Comportement de la gestion d'alimentation :** voir [L'alimentation en détail](./power-supply.md)
    - **Protocoles d'interface :** voir [Interfaces et connectivité](./interfaces.md)
    - **Contrôleur et protocole I2C :** voir [Contrôleur de la carte porteuse](./controller.md)
    - **Installation physique :** voir [Guide du matériel](../user-guide/hardware.md)

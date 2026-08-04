# Introduction

Le HALPI2 est un ordinateur de bord prêt à l'emploi basé sur le Raspberry Pi Compute Module 5 (CM5). Il offre un ensemble complet de fonctions bien adaptées aux applications marines, automobiles et à de nombreuses applications industrielles.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Lien vers la boutique"
    Achetez le HALPI2 sur la [boutique en ligne Hat Labs](https://shop.hatlabs.fi/products/halpi2-computer).

## Qu'est-ce que le HALPI2 ?

Le HALPI2 représente la dernière évolution de l'informatique embarquée durcie : il associe la puissance et l'écosystème du Raspberry Pi à des fonctions spécialisées pour les environnements exigeants. Contrairement aux ordinateurs monocartes classiques, le HALPI2 a été conçu dès l'origine pour un fonctionnement continu dans des conditions difficiles, là où la fiabilité est primordiale.

Le système associe un Raspberry Pi Compute Module 5 à une carte porteuse spécifique, le tout logé dans un boîtier en aluminium étanche qui fait également office de dissipateur thermique. Cette conception apporte la puissance de calcul nécessaire aux applications modernes tout en conservant la robustesse qu'exigent les usages marins et industriels.

## Principales caractéristiques

### Caractéristiques du boîtier

- **Boîtier en aluminium étanche (IP65)**, dimensions 200 × 130 × 60 mm
- **Connecteurs standard** : alimentation, NMEA 2000, ethernet gigabit, HDMI, 2× USB 3.0 et antenne WiFi/Bluetooth
- **Connectique flexible** : 3× presse-étoupe PG7 ou connecteurs étanches SP13
- **Antennes externes** : découpes prévues pour 2 connecteurs SMA supplémentaires
- **Conçu pour la fixation murale**, connecteurs positionnés pour faciliter l'installation

![Disposition des connecteurs du HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Caractéristiques matérielles

- **Large plage de tension d'entrée** de 10 à 32 V CC, protection jusqu'à 100 V CC
- **Limitation de courant intelligente** : courant d'entrée maximal de 0,9 ou 2,5 A, au choix de l'utilisateur
- **Deux modes d'alimentation** : raccordement direct en 12 V/24 V, ou alimentation par le bus NMEA 2000 en 12 V
- **Sauvegarde par supercondensateurs** pour l'immunité aux micro-coupures et l'arrêt propre en cas de perte d'alimentation
- **Gestion avancée de l'alimentation** avec détection automatique des coupures
- **Refroidissement passif** : le CM5 est en contact direct avec le boîtier
- **Stockage rapide** via une interface M.2 NVMe SSD standard
- **Extensibilité** par le connecteur GPIO 40 broches standard du Raspberry Pi
- **Entrées/sorties complètes** : 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, ethernet gigabit
- **Interfaces dédiées au nautisme** : CAN FD (NMEA 2000) et RS-485 (NMEA 0183)
- **Horloge temps réel** avec pile de sauvegarde pour une heure exacte
- **Indication visuelle de l'état** par cinq LED RGB
- **Interaction utilisateur** par connecteurs de boutons configurables

![Vue intérieure du HALPI2](./halpi2-interior.jpg)
*Vue intérieure du HALPI2 montrant la carte porteuse et les différents connecteurs.*

### Caractéristiques logicielles

- **Images système préconfigurées** prêtes à l'emploi : [HaLOS](https://docs.halos.fi) (par défaut), OpenPlotter, Raspberry Pi OS et Raspberry Pi OS Lite
- **Surveillance complète** de la tension, du courant et de la température
- **Mises à jour du firmware transparentes** via l'interface I2C

## Domaines d'application

### Applications marines

- **Systèmes de navigation** avec traceurs de cartes et intégration GPS
- **Enregistrement de données** : paramètres moteur, capteurs environnementaux et performances du navire
- **Serveurs Signal K** pour une gestion unifiée des données du bateau
- **Informatique de bord polyvalente** pour l'accès à Internet et les communications
- **Diagnostic des réseaux NMEA 2000** pour une meilleure fiabilité du système

### Applications industrielles

- **Surveillance de procédés** et systèmes de commande
- **Mesure environnementale** et acquisition de données
- **Stations de surveillance à distance**
- **Automatisation et commande d'équipements**
- **Systèmes de maintenance prédictive**

### Applications automobiles

- **Systèmes de gestion de flotte**
- **Télématique** et suivi de véhicules
- **Systèmes d'info-divertissement embarqués**
- **Plateformes de diagnostic et de surveillance**

## Contenu de l'emballage

L'emballage du HALPI2 contient :

- **L'unité HALPI2** avec Compute Module 5 et SSD NVMe préinstallés (sauf si commandée sans)
- **Un câble d'alimentation** à connecteur E7T (compatible Amphenol LTW Ceres Mini), longueur 2 m
- **Une fiche de câble E7T** pour les installations sur mesure
- **Une paire de connecteurs cylindriques CC** (5,5 × 2,1 mm) pour les alimentations 12 V/24 V standard
- **Une antenne Raspberry Pi** pour le WiFi et le Bluetooth
- **3 presse-étoupe PG7** pour interfaces supplémentaires
- **Un guide de démarrage rapide et les documents de garantie**

![Contenu de la pochette d'accessoires du HALPI2](./goodie-bag-contents.jpg)

Accessoires disponibles séparément :

- **Câble de dérivation NMEA 2000** pour les installations alimentées par le bus
- **Kits de connecteurs divers** pour les installations sur mesure

## Comment utiliser cette documentation

Cette documentation s'adresse aussi bien aux utilisateurs finaux à la recherche de conseils pratiques qu'aux développeurs ayant besoin d'informations techniques détaillées.

### Pour les utilisateurs finaux

- Commencez par le guide **Prise en main** pour l'installation et la mise en service
- Parcourez les **cas d'usage courants** pour des conseils adaptés à votre application
- Consultez le **Dépannage** en cas de problème

### Pour les développeurs

- Consultez la **Référence technique** pour les spécifications détaillées
- Étudiez les sections **Développement logiciel** pour vos applications sur mesure
- Examinez les **Fichiers de conception** pour préparer votre intégration
- Reportez-vous à la **Configuration avancée** pour optimiser les performances

### Conventions de la documentation

- 💡 Les encadrés **Astuce** donnent des raccourcis pour les tâches courantes
- ⚠️ Les encadrés **Avertissement** et **Attention** signalent des informations de sécurité importantes
- 🔧 Les sections **Détails techniques** approfondissent la mise en œuvre
- 📖 Les **renvois** relient les sujets connexes dans toute la documentation

Que vous installiez votre premier ordinateur de bord ou que vous développiez une solution industrielle sur mesure, cette documentation vous accompagnera à chaque étape.

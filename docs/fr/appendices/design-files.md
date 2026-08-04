---
translated_from: fc7ea79249b080c0f717303d066b9f6ea6d64795
---

# Fichiers de conception et schémas

Cette page met à disposition les schémas et les fichiers de conception mécanique du HALPI2.

La conception électronique du HALPI2 est réalisée sous KiCad. Les fichiers de conception sont disponibles dans le [dépôt GitHub](https://github.com/hatlabs/HALPI2-hardware). Chaque version publiée possède une étiquette correspondante dans le dépôt.

Les schémas sont fournis ci-dessous au format PDF pour plus de commodité. Les fichiers de routage du circuit imprimé ne sont disponibles que dans le dépôt GitHub.

Les fichiers de conception mécanique ne couvrent pour l'instant que le boîtier. La conception a été réalisée sous Autocad Fusion, mais les exports au format STEP sont lisibles par la plupart des logiciels de CAO.

## Version 0.6.1

Version corrective apportant des améliorations d'intégrité du signal et de mise à la masse identifiées lors des tests de production.

Modifications :

- Ajout d'un oscillateur d'horloge pour le signal NVMe SUSCLK, corrigeant des problèmes de compatibilité avec certains SSD NVMe
- Ajout des condensateurs manquants sur les paires différentielles RX du concentrateur USB3
- Mise à la masse assurée à chaque point de fixation

### Fichiers de conception

- Fichiers de conception KiCad : [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Schéma (PDF) : [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Version 0.6.0

Troisième version de production du HALPI2, avec de nouvelles corrections mineures sur la carte porteuse. Les fonctions de la carte restent identiques à celles de la version 0.5.0.

Modifications :

- La sortie 3,3 V est désormais commandée par le contrôleur au lieu d'être toujours active
- Ajout de points de test pour améliorer les tests de production
- Nouveau routage des interfaces HDMI, MIPI et USB3 pour une meilleure intégrité du signal
- Les connecteurs FFC de la carte sont désormais horizontaux
- Stabilité améliorée du convertisseur abaisseur 10 V — il ne siffle plus en aucune circonstance
- Circuit d'équilibrage des supercondensateurs réimplémenté avec un seul amplificateur opérationnel quadruple
- Empreintes de certains composants modifiées pour améliorer la disponibilité

### Fichiers de conception

- Fichiers de conception KiCad : [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Schéma (PDF) : [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Version 0.5.0

Deuxième version de production du HALPI2, avec des corrections mineures sur la carte porteuse. Le fonctionnement de la carte reste identique à celui de la version 0.4.0.

Modifications :

- Correction de petites erreurs de sérigraphie
- Suppression des plans de cuivre 3,3 V de la face inférieure, près des structures de fixation
- Ajout d'écrous à souder pour faciliter le montage des HAT
- Ajout d'écrous à souder pour une fixation plus sûre du Compute Module
- Retour aux connecteurs à cavaliers traversants (THT) pour une meilleure tenue mécanique
- Ajout d'une LED d'alimentation +5 V dédiée
- Assouplissement de l'équilibrage des supercondensateurs
- Réorganisation des connecteurs à cavaliers pour une meilleure ergonomie

### Fichiers de conception

- Fichiers de conception KiCad : [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Schéma (PDF) : [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- Modèle 3D du boîtier : [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (identique à la version 0.4.0)

## Version 0.4.0

Première version publique du HALPI2.

### Fichiers de conception

- Fichiers de conception KiCad : [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Schéma (PDF) : [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- Modèle 3D du boîtier : [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

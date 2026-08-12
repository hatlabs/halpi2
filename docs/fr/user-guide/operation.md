---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Utilisation quotidienne

Le HALPI2 est conçu pour fonctionner sans surveillance. Avec l'image HaLOS préinstallée — ou tout système d'exploitation doté du [démon HALPI](./software.md#outil-en-ligne-de-commande-halpi) — la gestion de l'alimentation est automatique : l'appareil charge ses supercondensateurs de secours, encaisse les micro-coupures, arrête proprement le système d'exploitation en cas de perte d'alimentation et redémarre au retour du courant. Rien de tout cela ne demande d'intervention de l'utilisateur.

## Mise sous tension

Le HALPI2 n'a pas de bouton d'alimentation sur le boîtier : il démarre dès que l'alimentation d'entrée est raccordée. (Un bouton d'alimentation externe peut être câblé sur la carte porteuse — voir [Boutons externes](./interfaces.md#boutons-externes).) La barre de LED se remplit d'abord de rouge pendant la charge des supercondensateurs (de quelques secondes à une demi-minute, selon le [réglage de la limitation de courant](./hardware.md#reglage-de-la-limitation-de-courant)). Les LED jouent ensuite une courte animation arc-en-ciel suivie d'un cycle de couleurs pendant le démarrage du Compute Module, affichent une barre jaune pendant le démarrage du système d'exploitation, puis passent au vert une fois le système d'exploitation en marche et le démon HALPI connecté.

## Arrêt

Pour arrêter le HALPI2, coupez l'alimentation d'entrée — par exemple avec un interrupteur du tableau électrique. Le système détecte la perte d'alimentation, arrête proprement le système d'exploitation sur l'énergie des supercondensateurs et reste éteint. Les LED affichent une barre violette pendant le déroulement de l'arrêt et s'éteignent une fois celui-ci terminé.

Vous pouvez aussi arrêter le système par logiciel — depuis le menu du bureau, avec la commande `shutdown` ou avec `halpi shutdown`. L'appareil se met alors hors tension et le reste jusqu'à une coupure puis un rétablissement de l'alimentation d'entrée (ou jusqu'à un appui sur le [bouton d'alimentation externe](./interfaces.md#boutons-externes), s'il y en a un).

En option, le contrôleur peut redémarrer automatiquement le système environ 5 secondes après un arrêt logiciel tant que l'alimentation d'entrée reste raccordée, afin qu'une commande d'arrêt accidentelle ne condamne jamais une installation difficile d'accès. Activez ce comportement avec `halpi config set auto_restart true` ; le réglage est conservé dans le contrôleur. Les appareils produits avant début 2026 étaient livrés avec ce comportement activé — vérifiez le vôtre avec `halpi config get auto_restart`.

Le système peut aussi être mis en veille : il se met hors tension et se réveille à une heure programmée — voir la référence [Contrôleur de la carte porteuse](../technical-reference/controller.md#veille).

## LED d'état

Les cinq LED du panneau avant montrent ce que fait le système :

| Motif des LED | Signification |
|:--------------|:--------------|
| Barre rouge qui se remplit | Charge des supercondensateurs avant le démarrage — patientez |
| Arc-en-ciel et cycle de couleurs | Démarrage du Compute Module. Si le motif se répète sans progresser, le module n'a pas démarré — voir le [Dépannage](./troubleshooting.md#led-en-arc-en-ciel) |
| Barre jaune | Système en marche, démon HALPI non connecté — normal pendant un court instant au démarrage. Si cela persiste, voir le [Dépannage](./troubleshooting.md#les-led-restent-jaunes) |
| Barre verte | Fonctionnement normal |
| Barre orange ou vert foncé | Alimentation d'entrée perdue, fonctionnement sur l'alimentation de secours — l'arrêt suit si le courant ne revient pas en quelques secondes |
| Barre violette | Arrêt en cours |
| Toutes rouges fixes | Système d'exploitation qui ne répond plus — le contrôleur le redémarrera automatiquement |
| Toutes clignotantes en rouge | Défaut des supercondensateurs — contactez l'assistance |
| Toutes bleues fixes | Mise en veille en cours |
| Toutes en rouge atténué | Veille |
| Toutes éteintes | Hors tension |

Dans les motifs en barre, le nombre de LED allumées indique le niveau de charge des supercondensateurs. Les plages de tension exactes et la correspondance complète des états figurent dans la référence [Contrôleur de la carte porteuse](../technical-reference/controller.md#reference-des-led-detat).

La luminosité des LED est réglable — voir [Commande des LED](./software.md#commande-des-led). Les LED peuvent aussi être réaffectées à l'affichage de métriques système et de données marines (activité réseau, niveaux de cuves, valeurs NMEA 2000 et Signal K) avec le module complémentaire [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights).

## En cas de perte d'alimentation

Il n'y a rien à faire. Les creux et micro-coupures brefs — jusqu'à 5 secondes par défaut — sont couverts par les supercondensateurs et le fonctionnement continue sans perturbation. Lors d'une coupure plus longue, le système s'arrête proprement de lui-même sur les 30 à 60 secondes d'énergie de secours que contiennent les supercondensateurs. Au retour de l'alimentation d'entrée, le système redémarre automatiquement.

!!! warning "Pas un onduleur"
    Les supercondensateurs servent à couvrir les micro-coupures et à alimenter un arrêt en sécurité. Pour continuer à fonctionner pendant une coupure prolongée, un onduleur externe est nécessaire.

## Vérifier l'état du système

Une barre de LED verte signifie que le système est en bonne santé. Pour le détail, la commande `halpi` affiche l'état du contrôleur, les tensions, le courant et les températures :

```bash
halpi status
```

Si quelque chose semble anormal, voir le [Dépannage](./troubleshooting.md) et le [Guide logiciel](./software.md#outil-en-ligne-de-commande-halpi).

## Fonctionnement sans le démon

Sur les systèmes d'exploitation dépourvus du démon HALPI, le contrôleur se rabat sur un mode de protection de base : il détecte toujours les pertes d'alimentation et demande un arrêt, mais par des appuis simulés sur le bouton d'alimentation — ce qui échoue si le système est figé — et la surveillance comme la configuration sont indisponibles. Si vous utilisez un système d'exploitation personnalisé, installez le démon ; voir [Autres distributions Debian](../software-development/ubuntu-installation.md). Le fonctionnement des deux modes est décrit dans la référence [Contrôleur de la carte porteuse](../technical-reference/controller.md#modes-de-fonctionnement).

!!! quote "Voir aussi"
    - **Fonctionnement interne de la gestion de l'alimentation :** voir [Contrôleur de la carte porteuse](../technical-reference/controller.md)
    - **Détails du système d'alimentation :** voir [L'alimentation en détail](../technical-reference/power-supply.md)
    - **La commande `halpi` et le démon :** voir le [Guide logiciel](./software.md)
    - **Problèmes :** voir le [Dépannage](./troubleshooting.md)

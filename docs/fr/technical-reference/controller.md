---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Contrôleur de la carte porteuse

La carte porteuse du HALPI2 comporte un microcontrôleur RP2040 qui gère l'alimentation, surveille le système et commande les LED du panneau avant. Le contrôleur fonctionne indépendamment du Compute Module : il est actif dès que l'alimentation d'entrée est raccordée, avant le démarrage du système d'exploitation et après son arrêt. Le Compute Module communique avec lui par I2C (bus 1, adresse `0x6d`) par l'intermédiaire du [démon HALPI](../user-guide/software.md#outil-en-ligne-de-commande-halpi).

Cette page décrit les modes de fonctionnement, les transitions d'état et la configuration du contrôleur. Elle documente le firmware en version 3.3.x. Rien de tout cela n'est nécessaire à l'usage courant — voir plutôt [Utilisation quotidienne](../user-guide/operation.md).

## Modes de fonctionnement

Le contrôleur fonctionne selon l'un de deux modes, selon que le démon HALPI communique ou non avec lui.

### Mode coopératif

Le mode coopératif est le mode de fonctionnement normal. Il est actif lorsque le démon HALPI (`halpid`) tourne et communique avec le contrôleur. L'image HaLOS préinstallée et toutes les images système de Hat Labs incluent le démon.

En mode coopératif :

- Le contrôleur et le démon échangent des données en temps réel : tensions, courant, températures et état.
- Les pertes d'alimentation sont signalées au démon, qui déclenche un arrêt propre du système d'exploitation.
- Le chien de garde (watchdog) protège contre les blocages du système d'exploitation (voir [Protection par chien de garde](#protection-par-chien-de-garde)).
- La configuration se consulte et se modifie avec l'outil en ligne de commande `halpi`.

### Mode solo

Le mode solo est le mode de repli. Le contrôleur y entre en l'absence de communication avec le démon :

- au démarrage, avant le lancement du démon ;
- si le démon n'est pas installé, a été désactivé ou a planté ;
- sur les systèmes d'exploitation sans prise en charge du HALPI2.

En mode solo, le contrôleur protège toujours contre les pertes d'alimentation, mais par un mécanisme plus rudimentaire : il demande l'arrêt par des appuis simulés sur le bouton d'alimentation, et il ne peut pas savoir si le système d'exploitation a réellement mené l'arrêt à bien.

!!! tip "Fiabilité du mode solo"
    Le mode solo apporte une protection essentielle, mais reste moins fiable que le mode coopératif. Les appuis simulés sur le bouton ne fonctionnent pas si le système d'exploitation est figé. Si vous utilisez un système d'exploitation personnalisé, installez le démon HALPI — voir [Autres distributions Debian](../software-development/ubuntu-installation.md).

## Perte d'alimentation et séquences d'arrêt

Le contrôleur surveille la tension d'entrée en continu. L'alimentation d'entrée est considérée comme perdue lorsque la tension descend sous 9,0 V. Une temporisation de coupure (5 secondes par défaut) distingue les micro-coupures des véritables coupures : les supercondensateurs couvrent l'intervalle, et si le courant revient avant l'expiration de la temporisation, rien d'autre ne se produit.

### Séquence d'arrêt en mode coopératif

1. Le démon détecte la perte d'alimentation d'après les mesures de tension du contrôleur.
2. Le démon attend l'expiration du délai de coupure (5 secondes par défaut).
3. Le démon exécute la commande d'arrêt configurée (par défaut `/sbin/poweroff`).
4. Le système d'exploitation s'arrête proprement sur l'énergie des supercondensateurs.
5. Le contrôleur détecte la mise hors tension du Compute Module et coupe la ligne 5 V.
6. Si l'arrêt n'est pas terminé au bout de 60 secondes, le contrôleur force la coupure.
7. Le système reste hors tension jusqu'au retour de l'alimentation d'entrée, puis redémarre automatiquement.

### Séquence d'arrêt en mode solo

1. Le contrôleur détecte la perte d'alimentation et lance la temporisation de coupure (5 secondes par défaut).
2. À l'expiration de la temporisation, le contrôleur simule un double appui sur le bouton d'alimentation.
3. Le système d'exploitation réagit et entame un arrêt propre sur l'énergie des supercondensateurs.
4. Si l'arrêt n'est pas terminé au bout de 60 secondes, le contrôleur force la coupure.
5. Le système reste hors tension jusqu'au retour de l'alimentation d'entrée, puis redémarre automatiquement.

### Comportement de redémarrage après un arrêt logiciel

Un arrêt lancé par logiciel alors que l'alimentation d'entrée reste disponible (par exemple avec la commande `shutdown` ou depuis le menu du bureau) aboutit à l'état *hors tension*. La suite dépend du paramètre de configuration `auto_restart` :

- `auto_restart` désactivé (réglage d'usine des appareils produits depuis début 2026) : le système reste éteint jusqu'à une coupure puis un rétablissement de l'alimentation d'entrée, ou jusqu'à un appui sur un bouton d'alimentation.
- `auto_restart` activé (valeur de repli du firmware, et réglage d'usine des appareils antérieurs) : le contrôleur redémarre le système au bout de 5 secondes, afin qu'un système sans surveillance ne reste pas éteint à cause d'un arrêt accidentel.

Modifiez le réglage avec `halpi config set auto_restart <true|false>`.

Un appui sur le bouton d'alimentation ou un cycle de l'alimentation d'entrée redémarre toujours le système, quel que soit le réglage `auto_restart`.

## Protection par chien de garde

En mode coopératif, un chien de garde (watchdog) protège contre les blocages du système d'exploitation :

- Le démon doit envoyer régulièrement au contrôleur un signal de réarmement du chien de garde.
- Si aucun signal n'arrive dans le délai imparti (10 secondes par défaut), le contrôleur considère que l'hôte ne répond plus, affiche le motif d'alerte (toutes les LED rouges fixes) et coupe puis rétablit l'alimentation du Compute Module pour rétablir le fonctionnement.
- Le délai se configure avec `halpi config set watchdog_timeout <seconds>`.

## Veille

La veille met le Compute Module hors tension tandis que le contrôleur reste actif, en attente d'un réveil programmé :

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Pendant la transition, toutes les LED sont bleues fixes ; en veille, elles sont en rouge atténué. Le contrôleur redémarre le système à l'heure programmée, sur un appui du bouton d'alimentation ou après un cycle de l'alimentation d'entrée.

## Référence des LED d'état

Les cinq LED RGB du panneau avant reflètent l'état du contrôleur. Ce tableau est la correspondance de référence entre les états du contrôleur et les motifs des LED ; la page [Utilisation quotidienne](../user-guide/operation.md#led-detat) en présente une version simplifiée.

| État du contrôleur | Motif des LED |
|:-------------------|:--------------|
| PowerOff (pas d'alimentation d'entrée utilisable ; contrôleur sur la charge résiduelle) | LED 5 rouge fixe |
| OffCharging | Barre rouge se remplissant pendant la charge des supercondensateurs |
| SystemStartup | Balayage arc-en-ciel, puis cycle de couleurs unies |
| OperationalSolo | Barre de niveau de charge jaune |
| OperationalCoOp | Barre de niveau de charge verte |
| BlackoutSolo | Barre de niveau de charge orange |
| BlackoutCoOp | Barre de niveau de charge vert foncé |
| BlackoutShutdown, ManualShutdown | Barre de niveau de charge violette |
| PoweredDownBlackout, PoweredDownManual | Toutes éteintes |
| HostUnresponsive (expiration du chien de garde) | Toutes rouges fixes |
| EnteringStandby | Toutes bleues fixes |
| Standby | Toutes en rouge atténué |
| Alarme de surtension des supercondensateurs | Toutes les LED clignotant en rouge |

Dans les motifs en barre de niveau de charge, chaque LED allumée représente un volt de tension des supercondensateurs :

| LED | Plage de tension |
|:----|:-----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Paramètres de configuration

La configuration est stockée dans la mémoire flash du contrôleur et survit aux coupures d'alimentation. Elle se consulte et se modifie avec `halpi config` — voir le [Guide logiciel](../user-guide/software.md#gestion-de-la-configuration).

| Paramètre | Valeur par défaut | Description |
|:----------|:------------------|:------------|
| `auto_restart` | `false` sur les appareils actuels (réglé au test de production) ; valeur de repli du firmware `true` | Redémarrage automatique 5 s après un arrêt logiciel si l'alimentation d'entrée est présente |
| `watchdog_timeout` | 10 s | Délai du chien de garde en mode coopératif |
| `power_on_threshold` | 8,0 V | Tension des supercondensateurs requise avant la mise sous tension du Compute Module |
| `solo_power_off_threshold` | 5,5 V | Tension des supercondensateurs à laquelle le contrôleur force la coupure en mode solo |
| `solo_depleting_timeout` | 5 s | Temporisation de coupure du mode solo |
| `led_brightness` | 48 | Luminosité des LED du panneau avant (0–255) |

La temporisation de coupure du mode coopératif et la commande d'arrêt sont des réglages du démon, définis dans `/etc/halpid/halpid.conf` (`blackout-time-limit`, 5 s par défaut ; `poweroff`, `/sbin/poweroff` par défaut).

!!! quote "Voir aussi"
    - **Usage courant :** voir [Utilisation quotidienne](../user-guide/operation.md)
    - **Détails du système d'alimentation :** voir [L'alimentation en détail](./power-supply.md)
    - **Mises à jour du firmware :** voir le [Guide logiciel](../user-guide/software.md#mises-a-jour-du-firmware)
    - **Sources du firmware et protocole I2C :** voir le [dépôt HALPI2-firmware](https://github.com/hatlabs/HALPI2-firmware)

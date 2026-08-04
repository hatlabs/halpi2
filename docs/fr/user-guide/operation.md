---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Fonctionnement du système

## LED d'état

Le HALPI2 dispose de cinq LED RGB qui renseignent visuellement sur l'état du système et de l'alimentation.

### Aide-mémoire des LED

| Motif des LED | Couleur | Signification |
|---------------|---------|---------------|
| LED 5 fixe | Rouge | Sous tension, en attente de charge |
| Remplissage progressif | Rouge | Charge des supercondensateurs |
| Arc-en-ciel et cycle de couleurs | Multicolore | Le CM5 n'a pas démarré |
| Barre de tension | Jaune | Fonctionnement en mode solo |
| Barre de tension | Vert | Fonctionnement en mode coopératif |
| Barre de tension | Orange | Alimentation de secours active (solo) |
| Barre de tension | Vert foncé | Alimentation de secours active (coopératif) |
| Toutes clignotantes | Rouge | Surtension des supercondensateurs |
| Toutes fixes | Rouge | Expiration du chien de garde |
| Barre de tension | Violet | Arrêt en cours |
| Toutes fixes | Bleu | Mise en veille en cours |
| Toutes fixes | Rouge atténué | Veille |
| Toutes éteintes | — | Système hors tension |

### Indication de la tension des supercondensateurs

En fonctionnement, les LED font office d'indicateur de tension et montrent le niveau de charge des supercondensateurs :

- **LED 1** : 5,0–6,0 V
- **LED 2** : 6,0–7,0 V
- **LED 3** : 7,0–8,0 V
- **LED 4** : 8,0–9,0 V
- **LED 5** : 9,0–10,0 V

## Gestion de l'alimentation et procédures d'arrêt

Le HALPI2 est doté d'une alimentation conçue pour supporter les pics de tension, les micro-coupures et les coupures brèves.

### Vue d'ensemble du système d'alimentation

La gestion de l'alimentation du HALPI2 comprend :

- **Une alimentation à large plage** (entrée 11–32 V CC, protection jusqu'à 100 V CC)
- **Une sauvegarde par supercondensateurs** pour les arrêts propres en cas de perte d'alimentation
- **Une limitation de courant** (0,9 A ou 2,5 A au choix)
- **La détection des coupures** et le déclenchement automatique de l'arrêt
- **La surveillance de la tension et du courant d'entrée**

Le système fonctionne selon deux modes : le mode solo et le mode coopératif.

### Mode solo

Le mode solo assure un fonctionnement autonome de base lorsque le démon HALPI n'est pas actif. Le contrôleur travaille seul, sans communication avec le logiciel.

#### Caractéristiques du mode solo

- **Aucune communication logicielle requise**
- **Protection de base contre les coupures** : surveille la tension d'entrée et réagit aux pertes d'alimentation
- **Arrêt automatique par appuis simulés sur le bouton d'alimentation**
- **Possibilités de surveillance et de configuration limitées**

#### Perte d'alimentation et arrêt en mode solo

**Détection de la perte d'alimentation :**
Le contrôleur surveille la tension d'entrée et détecte les coupures. Une temporisation de coupure (5 secondes par défaut) évite les arrêts lors d'interruptions brèves.

**Séquence d'arrêt automatique :**

1. **Le contrôleur détecte la perte d'alimentation**
2. **La temporisation de coupure démarre**, pour distinguer une micro-coupure d'une véritable perte
3. **Appuis simulés sur le bouton d'alimentation** : le contrôleur envoie un double appui au Compute Module
4. **Le système d'exploitation réagit** et entame un arrêt propre
5. **Les supercondensateurs maintiennent l'alimentation** (30 à 60 secondes en général)
6. **Protection par temporisation de 60 secondes** : coupure forcée si l'arrêt propre échoue
7. **Le système reste hors tension** jusqu'au retour de l'alimentation
8. **Redémarrage automatique** au retour de l'alimentation

**Arrêt manuel en mode solo :**

- Le système d'exploitation s'arrête normalement
- Le système redémarre automatiquement au bout de 5 secondes si l'alimentation d'entrée est toujours présente
- Pour un arrêt définitif, coupez l'alimentation d'entrée après avoir lancé l'arrêt propre

#### Quand le mode solo est actif

Le mode solo s'applique :

- au tout début du démarrage, avant le lancement du démon HALPI ;
- si le démon HALPI ne démarre pas ou est désactivé ;
- sur les systèmes d'exploitation non pris en charge, dépourvus du démon ;
- lorsque le démon a planté ou ne répond plus.

!!! tip "Fiabilité du mode solo"
    Le mode solo apporte une protection essentielle, mais reste moins fiable que le mode coopératif. Le contrôleur demande l'arrêt par des appuis simulés sur le bouton, ce qui peut ne pas fonctionner si le système est figé.

### Mode coopératif

Le mode coopératif offre toutes les fonctions de gestion de l'alimentation lorsque le démon HALPI est actif et dialogue avec le contrôleur.

#### Fonctions du mode coopératif

- **Communication directe avec le logiciel** : échange de données en temps réel entre le contrôleur et le démon
- **Protection par chien de garde** : une temporisation de 30 secondes garantit la stabilité du système
- **Comportement d'arrêt configurable** : délais et commandes ajustables
- **Surveillance en temps réel** : suivi complet des paramètres d'alimentation
- **Options de configuration avancées**

#### Perte d'alimentation et arrêt en mode coopératif

**Détection de la perte d'alimentation :**
Le contrôleur surveille l'alimentation d'entrée et transmet les événements directement au démon HALPI. La temporisation de coupure configurable (5 secondes par défaut) autorise de brèves interruptions sans déclencher d'arrêt.

**Séquence d'arrêt automatique :**

1. **Le contrôleur détecte la perte d'alimentation** et en informe le démon HALPI
2. **Évaluation de la temporisation de coupure** : le démon vérifie si la coupure dépasse le seuil
3. **Exécution de la commande d'arrêt** : le démon lance la commande configurée (par défaut `/sbin/poweroff`)
4. **Arrêt propre du système d'exploitation** : les applications se ferment et les systèmes de fichiers sont démontés en sécurité
5. **L'alimentation de secours par supercondensateurs** fournit l'énergie pendant tout l'arrêt
6. **Le contrôleur suit la fin de la procédure** : il détecte la mise hors tension du Compute Module
7. **La ligne 5 V est coupée** une fois l'arrêt terminé
8. **Le système reste hors tension** jusqu'au retour de l'alimentation d'entrée
9. **Gestion du redémarrage** : selon la configuration, le système redémarre automatiquement ou reste éteint

**Arrêt manuel en mode coopératif :**

- Un arrêt propre standard a lieu lorsqu'il est lancé depuis le logiciel
- Le système redémarre automatiquement au bout de 5 secondes si l'alimentation d'entrée est toujours présente
- Pour empêcher le redémarrage automatique, coupez l'alimentation ou réglez `auto_restart` sur `false`

#### Protection par chien de garde

Le mode coopératif comprend un chien de garde (watchdog) :

- **Temporisation de communication de 30 secondes** : le démon doit dialoguer régulièrement avec le contrôleur
- **Reprise automatique** : le système redémarre si la communication s'interrompt
- **Protection contre les défaillances logicielles** : garantit la reprise après un plantage du démon ou un blocage du système
- **« Nourrir le chien de garde »** : le démon envoie régulièrement son état, ce qui réarme la temporisation

#### Quand le mode coopératif est actif

Le mode coopératif s'applique lorsque :

- le démon HALPI est actif et fonctionne normalement ;
- la communication entre le démon et le contrôleur est établie ;
- le système utilise un système d'exploitation pris en charge ;
- toutes les fonctions de surveillance et de commande sont disponibles.

!!! info "Vérifier le mode coopératif"
    État du démon : `systemctl status halpid`

    État du contrôleur : `halpi status`

    Pour en savoir plus sur la commande `halpi`, voir le [Guide logiciel](./software.md#demon-halpi-halpid).

### Alimentation de secours et supercondensateurs

Les deux modes s'appuient sur les supercondensateurs pour garantir un arrêt propre :

**Autonomie de l'alimentation de secours :**

- Les supercondensateurs fournissent 30 à 60 secondes d'autonomie
- La durée dépend de la charge du système et des périphériques raccordés
- Elle suffit à fermer le système de fichiers et à terminer les processus en sécurité
- Elle n'est pas prévue pour prolonger le fonctionnement pendant une coupure longue

**Caractéristiques de charge :**

- Temps de charge : 25 secondes avec une limitation à 0,9 A
- Temps de charge : 9 secondes avec une limitation à 2,5 A
- La progression de la charge est visible au remplissage des LED (motif rouge)

!!! warning "Limite de la protection contre les coupures"
    Le système à supercondensateurs est conçu pour l'arrêt propre, pas pour prolonger le fonctionnement. Ne comptez pas dessus en cas de coupure prolongée.

### Remarques sur l'arrêt manuel

Le HALPI2 privilégie le fonctionnement et la reprise automatiques, ce qui influe sur le comportement lors d'un arrêt manuel.

#### Redémarrage automatique

Par défaut, le HALPI2 redémarre après un arrêt manuel si l'alimentation d'entrée est toujours présente :

- Un arrêt manuel provoque l'arrêt normal du système d'exploitation
- Un délai de grâce de 5 secondes suit la fin de l'arrêt
- Le système redémarre automatiquement pour rester disponible
- Cela garantit la reprise après un arrêt accidentel

#### Comment arrêter l'appareil définitivement

Deux méthodes sont possibles :

**Coupure de l'alimentation :**

1. Lancez un arrêt propre depuis le logiciel
2. Attendez la fin de l'arrêt (les LED s'éteignent)
3. Coupez l'alimentation d'entrée pour empêcher le redémarrage automatique

**Modification de la configuration :**

1. Désactivez le redémarrage automatique : `halpi config set auto_restart false`
2. Lancez l'arrêt depuis le logiciel
3. Le système reste éteint une fois l'arrêt terminé

**Mode veille (à venir) :**

!!! info "État de la fonction"
    Le mode veille est prévu pour de futures versions du firmware. Il permettra de mettre le Compute Module hors tension pendant que le contrôleur du HALPI2 reste actif, en attente d'un événement de réveil.

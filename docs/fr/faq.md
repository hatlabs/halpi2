---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# FAQ

## Pourquoi le HALPI2 redémarre-t-il après que je l'ai arrêté ?

Le redémarrage automatique est activé sur votre appareil : avec `auto_restart` réglé sur `true`, le contrôleur redémarre le système environ 5 secondes après un arrêt logiciel tant que l'alimentation d'entrée est raccordée. Les appareils produits avant début 2026 étaient livrés ainsi ; les appareils actuels sont livrés avec ce réglage désactivé. Désactivez-le avec `halpi config set auto_restart false` — ou conservez-le, puisqu'il garantit qu'un système sans surveillance ne reste pas éteint après une commande d'arrêt accidentelle. S'il est activé, arrêtez définitivement l'appareil en coupant l'alimentation d'entrée. Voir [Arrêt](user-guide/operation.md#arret).

## Comment éteindre le HALPI2 ?

Coupez l'alimentation d'entrée. Le système détecte la perte d'alimentation et s'arrête proprement sur l'énergie des supercondensateurs — c'est le mode d'extinction prévu. Voir [Arrêt](user-guide/operation.md#arret).

## Faut-il faire quelque chose quand le courant est coupé ?

Non. Les micro-coupures sont couvertes par les supercondensateurs, les coupures plus longues déclenchent un arrêt automatique en sécurité, et le système redémarre de lui-même au retour du courant. Voir [En cas de perte d'alimentation](user-guide/operation.md#en-cas-de-perte-dalimentation).

## Combien de temps dure l'alimentation de secours ?

Les supercondensateurs fournissent 30 à 60 secondes, selon la charge du système. C'est assez pour un arrêt en sécurité avec de la marge, mais le HALPI2 n'est pas un onduleur — il ne continue pas à fonctionner pendant une coupure prolongée. Voir [L'alimentation en détail](technical-reference/power-supply.md).

## Le HALPI2 peut-il rester sous tension en permanence ?

Oui. Le HALPI2 est conçu pour un fonctionnement continu sans surveillance, et sa gestion de l'alimentation part de ce principe : le système se remet des pertes d'alimentation et des blocages du système d'exploitation sans intervention de l'utilisateur.

## Que signifient des LED qui restent jaunes ?

Une barre jaune signifie que le système est en marche mais que le démon HALPI ne s'est pas connecté — c'est normal pendant un court instant au démarrage. Une barre jaune persistante signifie que le système d'exploitation ne démarre pas ou que le démon n'est pas installé. Voir le [Dépannage](user-guide/troubleshooting.md#les-led-restent-jaunes).

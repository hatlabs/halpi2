# Problèmes connus

Cette page recense les problèmes matériels connus des différentes versions du HALPI2.

## Appareils en version 0.4.0

#### Pic de courant à la mise sous tension

Lorsque l'appareil est mis sous tension avec des supercondensateurs entièrement déchargés, le courant d'appel initial peut atteindre 1,1 A pendant un bref instant. L'appareil est de ce fait nominalement non conforme à l'exigence NMEA 2000 d'un courant d'entrée maximal de 1 A.

Ce courant initial supérieur à la spécification provient d'une interaction difficile à cerner entre les entrées analogiques du microcontrôleur RP2040 et le circuit de limitation de courant.

#### Plan de cuivre sous les rebords de fixation

Un plan d'alimentation 3,3 V situé sur la face inférieure du circuit imprimé s'étend au-dessus des rebords de fixation. Dans certains boîtiers, ces rebords portent encore des bavures de fonderie coupantes (résidus d'aluminium issus du moulage). Si l'arête d'une bavure traverse le vernis épargne du circuit imprimé, elle peut créer un court-circuit avec le plan 3,3 V et empêcher la mise sous tension de l'appareil.

Le problème se corrige en appliquant du ruban isolant PVC sur les rebords de fixation.

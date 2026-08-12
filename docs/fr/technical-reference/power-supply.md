---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# L'alimentation en détail

L'alimentation du HALPI2 est conçue pour l'environnement électrique instable des bateaux et des véhicules : elle tolère les pics de tension et les micro-coupures, limite le courant d'appel et emmagasine assez d'énergie pour arrêter le système en sécurité en cas de perte de l'alimentation d'entrée.

Pour les spécifications électriques, voir la [Référence matérielle](./hardware.md). Pour la machine à états qui exploite les mesures décrites ici, voir la référence [Contrôleur de la carte porteuse](./controller.md).

## Étage d'entrée

La plage d'entrée nominale est de 10–32 V CC, ce qui couvre les installations 12 V comme 24 V. L'étage d'entrée est protégé contre l'inversion de polarité et contre les surtensions transitoires jusqu'à 100 V, comme les délestages d'alternateur (load dump).

### Limitation de courant

Un limiteur de courant d'entrée fixe le courant maximal tiré de la source, réglable entre 0,9 A et 2,5 A par un sélecteur sur la carte porteuse. Cette limite remplit deux rôles :

- Elle plafonne le courant d'appel lorsque les supercondensateurs déchargés commencent à se charger à la mise sous tension.
- Elle maintient la consommation totale dans le budget de puissance de la source — le réglage 0,9 A (LEN 18) permet d'alimenter le HALPI2 sans risque par un bus NMEA 2000.

Le réglage par défaut est 0,9 A. Choisissez 2,5 A lorsque le système alimente des périphériques gourmands ou pour un démarrage plus rapide. L'emplacement du sélecteur et la procédure de modification sont décrits dans le [Guide du matériel](../user-guide/hardware.md#reglage-de-la-limitation-de-courant).

## Sauvegarde par supercondensateurs

Un banc de supercondensateurs fournit l'énergie de secours des arrêts propres. Contrairement à un onduleur à batterie, les supercondensateurs ne s'usent pas, fonctionnent sur toute la plage de température et se chargent en quelques secondes — au prix d'une réserve d'énergie beaucoup plus faible.

### Charge

Les supercondensateurs se chargent dès que l'alimentation d'entrée est présente. À partir d'une charge nulle, la charge prend environ :

- 25 secondes avec la limitation à 0,9 A ;
- 9 secondes avec la limitation à 2,5 A.

Les LED du panneau avant montrent la progression de la charge sous la forme d'une barre rouge qui se remplit. Le Compute Module est mis sous tension dès que la tension des supercondensateurs atteint le seuil de mise sous tension (8,0 V par défaut).

### Autonomie de secours

En cas de perte de l'alimentation d'entrée, les supercondensateurs portent toute la charge du système. Ils fournissent 30 à 60 secondes d'autonomie, selon la charge du système et les périphériques raccordés — de quoi mener un arrêt propre du système d'exploitation avec de la marge.

!!! warning "Pas un onduleur"
    Le système à supercondensateurs est conçu pour couvrir les micro-coupures et alimenter un arrêt en sécurité. Il n'est pas prévu pour prolonger le fonctionnement pendant une coupure durable.

## Détection des pertes d'alimentation

Le contrôleur mesure la tension d'entrée en continu et considère l'alimentation d'entrée comme perdue lorsque la tension descend sous 9,0 V. Une temporisation de coupure (5 secondes par défaut) évite l'arrêt lors des interruptions brèves : les supercondensateurs couvrent l'intervalle et le fonctionnement continue sans perturbation si le courant revient à temps. Les coupures plus longues déclenchent les séquences d'arrêt automatique décrites dans la référence [Contrôleur de la carte porteuse](./controller.md#perte-dalimentation-et-sequences-darret).

## Surveillance

Le contrôleur mesure la tension d'entrée, le courant d'entrée et la tension des supercondensateurs, et les expose par le démon HALPI :

```bash
halpi status
```

Les valeurs sont aussi accessibles par programme via l'API REST du démon — voir le [Guide logiciel](../user-guide/software.md#acces-a-lapi-rest).

!!! quote "Voir aussi"
    - **Spécifications électriques :** voir la [Référence matérielle](./hardware.md)
    - **Machine à états et séquences d'arrêt :** voir [Contrôleur de la carte porteuse](./controller.md)
    - **Comportement de l'alimentation au quotidien :** voir [Utilisation quotidienne](../user-guide/operation.md)

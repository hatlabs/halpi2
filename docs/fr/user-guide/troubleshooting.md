---
translated_from: 232aac811fb62f4cc46a1955e832ea282dc92332
---

# Dépannage

Cette page présente les problèmes courants que vous pouvez rencontrer en utilisant le HALPI2, et la manière de les résoudre.

## Problèmes d'alimentation et de démarrage

### Le système ne s'allume pas

**Symptômes :** aucune activité des LED, aucun signe de vie après le raccordement de l'alimentation.

1. Vérifiez au multimètre, sur le connecteur E7T, que la tension d'entrée est dans la plage admise (10–32 V CC).
2. Contrôlez les raccordements du câble d'alimentation — assurez-vous que le connecteur E7T est bien enfoncé.
3. Si vous alimentez l'appareil par le bus NMEA 2000, vérifiez que le limiteur de courant est réglé sur 0,9 A et que le réseau peut fournir un courant suffisant.
4. Ouvrez le boîtier et recherchez des dommages visibles ou des connexions internes desserrées.

### LED en arc-en-ciel

**Symptômes :** les LED défilent en arc-en-ciel et n'atteignent jamais un état stable.

Le motif arc-en-ciel signifie que le contrôleur est sous tension mais que le CM5 n'est pas détecté. Cela peut se produire si :

- le Compute Module n'est pas installé ou n'est pas correctement enfoncé ;
- le Compute Module est défectueux ;
- un appareil raccordé injecte des tensions parasites qui empêchent le CM5 de démarrer — essayez de débrancher le câble HDMI.

1. Débranchez tous les écrans HDMI et redémarrez pour écarter l'hypothèse des tensions parasites.
2. Si le problème persiste, ouvrez le boîtier et vérifiez que le module CM5 est bien enfoncé dans son connecteur — cela suppose de déposer la carte porteuse.

### Les LED restent jaunes

**Symptômes :** les LED passent du rouge (charge) au jaune (sous tension) mais n'atteignent jamais le vert.

L'état jaune signifie que le contrôleur a mis le CM5 sous tension et attend la réponse du démon. Si les LED restent jaunes, soit le système d'exploitation ne démarre pas, soit le démon HALPI n'est pas installé.

1. Vérifiez que le sélecteur de mode de démarrage est en position « Normal » — la LED jaune située à côté s'allume lorsque le mode est réglé sur « Abnormal » (démarrage USB).
2. Raccordez un écran en HDMI pour voir les erreurs de démarrage ou l'invite de connexion.
3. Vérifiez que le SSD NVMe est bien enfoncé dans son emplacement M.2.
4. Si le système démarre correctement, vérifiez que le démon est installé : `systemctl status halpid`
5. Si le démon est installé mais ne tourne pas, consultez ses journaux : `journalctl -u halpid -e`

### Le système s'arrête de façon inattendue

**Symptômes :** le système se met hors tension sans intervention, alors que l'alimentation externe est raccordée.

1. Contrôlez la stabilité de la tension d'entrée — de brèves chutes sous le seuil déclenchent la temporisation de coupure. Suivez `V_in` en temps réel avec `halpi status`.
2. Inspectez le câble d'alimentation à la recherche de connexions desserrées ou de conducteurs abîmés susceptibles de provoquer un contact intermittent.
3. Si vous alimentez l'appareil par le bus NMEA 2000, vérifiez que la tension du réseau reste stable en charge. D'autres appareils gourmands sur le réseau peuvent provoquer des chutes de tension.

## Mise à jour du firmware échouée ou annulée

Si le système redémarre dans les 30 secondes suivant une mise à jour du firmware, celui-ci revient automatiquement à la version précédente, par sécurité.

1. Vérifiez la version actuelle du firmware : `halpi get firmware_version`
2. Relancez la mise à jour : `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Une fois la mise à jour installée, effectuez un arrêt propre : `sudo shutdown -h now`
4. Attendez la mise hors tension complète avant de rebrancher — laissez au moins 30 secondes avant le redémarrage suivant pour ne pas déclencher le mécanisme de retour arrière.

## Problèmes de réseau et d'interfaces

### Aucune donnée NMEA 2000

**Symptômes :** `candump can0` n'affiche rien, ou Signal K ne reçoit aucune donnée.

1. Vérifiez l'état de l'interface CAN :
    ```bash
    ip link show can0
    ```
    L'interface doit être `UP`. Si elle est `DOWN`, activez-la :
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Observez la LED RX sur la carte porteuse — elle doit clignoter lorsqu'il y a du trafic sur le réseau. Si la LED RX reste éteinte :
    - vérifiez le raccordement du câble Micro-C et la position du connecteur en T ;
    - assurez-vous que le réseau NMEA 2000 est alimenté et que d'autres appareils émettent ;
    - vérifiez que le cavalier de terminaison 120 Ω n'est **pas** activé sur un réseau NMEA 2000.

3. Si la LED RX clignote mais que `candump` n'affiche rien, le problème est logiciel. Vérifiez la configuration de l'interface CAN :
    ```bash
    ip -details link show can0
    ```

4. Recherchez des erreurs sur le bus CAN :
    ```bash
    ip -statistics link show can0
    ```
    Un nombre d'erreurs élevé suggère un problème de câblage, un débit incorrect ou une contention sur le bus.

### Aucune donnée NMEA 0183 sur le RS-485

**Symptômes :** aucune donnée sur `/dev/ttyAMA4`, ou l'appareil raccordé ne répond pas.

1. Ouvrez le boîtier et observez les LED de l'interface RS-485 — la LED RX doit clignoter à la réception de données.
2. Vérifiez que le port série existe et est accessible :
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Contrôlez la polarité du câblage — le RS-485 utilise une signalisation différentielle sur les lignes A et B. Une inversion de A et B empêche toute communication.

### Le lien Ethernet ne s'établit pas

1. Vérifiez le câble Ethernet et le connecteur RJ45. Essayez un autre câble.
2. Ouvrez le boîtier et observez les LED Ethernet pour connaître l'état du lien.
3. Vérifiez l'état du lien : `ip link show eth0`
4. Si le lien est actif mais qu'aucune adresse IP n'est attribuée, vérifiez le DHCP : `sudo dhclient eth0`
5. En configuration IP fixe, vérifiez les réglages dans `/etc/network/interfaces` ou dans NetworkManager.

## Problèmes liés au système d'exploitation

### Impossible de se connecter en SSH

1. Vérifiez que SSH est activé : `sudo systemctl status ssh`
2. Vérifiez la connectivité réseau — l'appareil répond-il au ping ?
3. SSH est activé par défaut sur les images HaLOS sans écran et sur OpenPlotter. Sur les variantes HaLOS Desktop et sur Raspberry Pi OS, SSH s'active avec `raspi-config`.

### Le système est lent ou se fige

1. Vérifiez la température du processeur — une température ambiante extrême peut provoquer un bridage thermique. Utilisez :
    ```bash
    vcgencmd measure_temp
    ```
    Une température supérieure à 80 °C indique un problème thermique. Essayez de réduire la température ambiante ou d'améliorer la circulation d'air autour du boîtier.

2. Vérifiez l'utilisation de la mémoire : `free -h`
3. Vérifiez l'espace disque : `df -h` — un SSD NVMe plein dégrade fortement les performances.
4. Recherchez les processus emballés : `top` ou `htop`

### L'heure est fausse après une coupure

Le HALPI2 dispose d'une horloge temps réel (RTC) avec pile de sauvegarde, qui conserve l'heure pendant les coupures. Si l'horloge se réinitialise :

1. Vérifiez la pile de la RTC — elle peut être à remplacer si l'appareil est resté longtemps hors tension.
2. Vérifiez la synchronisation NTP lorsque le réseau est disponible : `timedatectl status`
3. Réglez l'heure manuellement si nécessaire : `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Diagnostic par les LED

Les motifs des LED permettent d'identifier rapidement l'état du système :

| Symptôme | Motif des LED | Cause probable |
|:---------|:--------------|:---------------|
| Le système ne démarre pas | Aucune LED | Pas d'alimentation d'entrée ou défaut matériel |
| Bloqué au démarrage | Remplissage rouge progressif | Supercondensateurs encore en charge — patientez |
| Bloqué au démarrage | Motif arc-en-ciel | CM5 non détecté — vérifiez la mise en place du module et débranchez les écrans |
| Reste au jaune | Barre jaune | Le système ne démarre pas ou le démon n'est pas installé |
| Arrêt inattendu | Barre orange ou vert foncé, puis violette | Alimentation d'entrée perdue, arrêt sur l'alimentation de secours — vérifiez l'alimentation d'entrée |
| Le système redémarre tout seul | Toutes les LED rouges fixes avant le redémarrage | Expiration du chien de garde — le système d'exploitation ne répondait plus et le contrôleur l'a redémarré |
| Défaut | Toutes les LED clignotant en rouge | Surtension des supercondensateurs — contactez l'assistance |

!!! quote "Voir aussi"
    - **Motifs des LED :** voir [LED d'état](./operation.md#led-detat)
    - **Comportement en cas de perte d'alimentation :** voir [En cas de perte d'alimentation](./operation.md#en-cas-de-perte-dalimentation)
    - **Gestion du démon :** voir le [Guide logiciel](./software.md#demon-halpi-halpid)
    - **Détails de l'interface CAN :** voir [Interfaces et connectivité](./interfaces.md#can-fd-nmea-2000)
    - **Détails de l'interface RS-485 :** voir [Interfaces et connectivité](./interfaces.md#rs-485-nmea-0183)

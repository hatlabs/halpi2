---
translated_from: 9497de10027831b20a1e2278a32df0c12d9a4a39
---

# Interfaces et connectivité

Cette page décrit la manière dont les interfaces du CM5 sont exposées sur la
carte porteuse du HALPI2. Pour l'usage courant des ports CAN FD et RS-485
intégrés, voir le guide de l'utilisateur
[Interfaces et connectivité](../user-guide/interfaces.md).

## Ports série (UART)

Le Compute Module 5 atteint le connecteur 40 broches par l'intermédiaire de son
contrôleur d'entrées/sorties RP1, qui expose cinq UART (`uart0`–`uart4`). Chaque
UART est câblé sur une paire de broches GPIO fixe : contrairement aux modèles de
Pi antérieurs, les broches ne peuvent pas être réaffectées. La console de
connexion est un UART de débogage distinct et dédié (`/dev/ttyAMA10`) ; elle ne
fait pas partie de cette liste.

| UART | TX / RX | Broches du connecteur | Périphérique Linux | Disponibilité sur le HALPI2 |
|:-----|:--------|:----------------------|:-------------------|:----------------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Libre. Port série HAT conventionnel ; utilisé par les HAT GNSS. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Libre. Ce sont les broches de l'EEPROM d'identification HAT (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Libre. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Utilisé par le contrôleur CAN FD (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Utilisé par le RS-485. |

### Activer un UART

Ajoutez l'overlay `-pi5` correspondant dans `/boot/firmware/config.txt`, puis
redémarrez :

```
dtoverlay=uart2-pi5
```

`uart0` s'active plutôt avec `dtparam=uart0=on`. (Sur un CM5, le firmware
redirige les overlays `uartN` simples vers leurs équivalents `uartN-pi5` : les
deux noms fonctionnent, la forme `-pi5` est employée ici par souci de clarté.)

Le contrôle de flux matériel s'active explicitement avec le paramètre `ctsrts`,
et les overlays peuvent piloter directement la ligne d'activation d'un
émetteur-récepteur RS-485 avec le paramètre `rs485` :

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS occupent la paire de broches GPIO suivante, souvent déjà utilisée sur le
HALPI2 :

| UART | CTS / RTS | Entre en conflit avec |
|:-----|:----------|:----------------------|
| `uart1` | GPIO2 / 3 | Bus I2C système (I2C1) |
| `uart2` | GPIO6 / 7 | Sélection de puce du CAN FD |
| `uart3` | GPIO10 / 11 | Bus SPI du CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` n'est donc utilisable en pratique qu'en port TX/RX seul.

### Libérer un UART occupé

`uart3` et `uart4` recouvrent les interfaces CAN FD et RS-485 de la carte :

- **`uart3`** partage le bus SPI0 avec le contrôleur CAN FD : GPIO9 est la sortie
  de données du contrôleur (SDO). Utiliser `uart3` impose de désactiver
  l'interface CAN et de modifier le matériel ; ce n'est pas pris en charge sur la
  carte standard.
- **`uart4`** est le port RS-485. Retirer le cavalier d'activation de réception
  déconnecte le récepteur RS-485 de GPIO13 et libère `uart4` pour un usage
  général. Le RS-485 n'est alors plus disponible.

Les étapes matérielles sont décrites dans
[Désactiver les interfaces intégrées](../user-guide/hardware.md#utiliser-des-hat).

### Vérification

Après redémarrage, vérifiez que le nœud de périphérique existe et que les
broches portent bien la fonction attendue :

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

Les broches sélectionnées doivent indiquer leur fonction UART (`a2` pour
`uart1`–`uart4`, `a4` pour `uart0`).

## Autres sujets

- Détails de mise en œuvre du NMEA 2000
- Spécifications USB 3.0 et gestion de l'alimentation
- Ethernet et réseau
- Exigences de stockage M.2 NVMe

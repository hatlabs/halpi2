---
translated_from: 930b506809e4abe2b54e4fea058658a9d6d94461
---

# Errores conocidos

En esta página se enumeran los problemas de hardware conocidos de las distintas versiones de HALPI2.

## Dispositivos de la versión 0.4.0

#### Pico de corriente inicial en el encendido

Cuando el dispositivo se enciende con los supercondensadores completamente descargados, la corriente de irrupción inicial puede alcanzar 1,1 A durante un breve instante. Esto hace que el dispositivo no cumpla nominalmente el requisito de NMEA 2000 de una corriente de entrada máxima de 1 A.

Esta corriente inicial superior a la especificada se debe a una interacción poco evidente entre las entradas analógicas del microcontrolador RP2040 y el circuito de limitación de corriente.

#### Relleno de cobre bajo los resaltes de montaje

Un plano de alimentación de 3,3 V situado en la capa inferior del PCB se extiende por encima de los resaltes de montaje. En algunas carcasas, los resaltes de montaje conservan restos de «rebabas» afiladas (fragmentos de aluminio sobrantes del proceso de fundición). Si los bordes de las rebabas atraviesan la máscara de soldadura del PCB, pueden crear un cortocircuito con el plano de 3,3 V e impedir que el dispositivo se encienda.

El problema se resuelve aplicando cinta aislante de PVC sobre los resaltes de montaje.

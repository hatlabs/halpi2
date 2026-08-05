---
translated_from: 930b506809e4abe2b54e4fea058658a9d6d94461
---

# Errata corrige

In questa pagina sono elencati i problemi hardware noti per le diverse versioni dell’HALPI2.

## Dispositivi della versione 0.4.0

#### Picco di corrente iniziale all’accensione

Quando il dispositivo viene acceso con i supercondensatori completamente scarichi, la corrente di spunto iniziale può raggiungere 1,1 A per un breve istante. Ciò rende il dispositivo nominalmente non conforme al requisito NMEA 2000 di una corrente di ingresso massima di 1 A.

La corrente iniziale superiore al valore specificato è dovuta a un’interazione poco evidente tra gli ingressi analogici del microcontrollore RP2040 e il circuito di limitazione di corrente.

#### Riempimento di rame sotto le sporgenze di appoggio

Un piano di alimentazione a 3,3 V sullo strato inferiore del PCB si estende al di sopra delle sporgenze di appoggio. In alcune custodie le sporgenze di appoggio presentano residui di “bave” taglienti (frammenti di alluminio lasciati dal processo di fusione). Se i bordi delle bave penetrano il solder mask del PCB, possono creare un cortocircuito verso il piano a 3,3 V, impedendo l’accensione del dispositivo.

Il problema si può risolvere applicando nastro isolante in PVC sopra le sporgenze di appoggio.

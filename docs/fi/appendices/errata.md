# Tunnetut virheet

Tällä sivulla on lueteltu eri HALPI2-versioiden tunnetut laitteisto-ongelmat.

## Version 0.4.0 -laitteet

#### Virtapiikki käynnistyksessä

Kun laite käynnistetään superkondensaattorien ollessa täysin tyhjät, alkuvirta voi hetkellisesti nousta 1,1 A:iin. Tämä tekee laitteesta nimellisesti NMEA 2000 -vaatimusten vastaisen, sillä suurin sallittu syöttövirta on 1 A.

Määriteltyä suurempi alkuvirta johtuu vaikeasti havaittavasta yhteisvaikutuksesta RP2040-mikro-ohjaimen analogiatulojen ja virranrajoituspiirin välillä.

#### Kuparitäyttö kiinnityskorvakkeiden alla

Piirilevyn alapinnan 3,3 V:n jännitetaso ulottuu kiinnityskorvakkeiden yläpuolelle. Joissakin koteloissa kiinnityskorvakkeisiin on jäänyt teräviä valujäysteitä (valuprosessista jääneitä alumiininpaloja). Jos jäysteen reuna läpäisee piirilevyn juotteenestolakan, se voi aiheuttaa oikosulun 3,3 V:n tasoon ja estää laitteen käynnistymisen.

Ongelman voi korjata asettamalla sähköteippiä kiinnityskorvakkeiden päälle.

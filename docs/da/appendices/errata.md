# Kendte fejl

Kendte hardwareproblemer i de forskellige HALPI2-versioner er anført på denne side.

## Enheder med version 0.4.0

#### Strømspids ved opstart

Når enheden tændes med helt afladede superkondensatorer, kan den indledende indkoblingsstrøm kortvarigt nå 1,1 A. Det gør enheden nominelt ikke-overensstemmende med NMEA 2000-kravet om en indgangsstrøm på maksimalt 1 A.

Den højere startstrøm end den specificerede skyldes et uigennemskueligt samspil mellem RP2040-mikrocontrollerens analoge indgange og strømbegrænsningskredsløbet.

#### Kobberudfyldning under monteringsafsatser

Et forsyningsplan på 3,3 V i printets bundlag rager ud over monteringsafsatserne. I nogle kabinetter har monteringsafsatserne rester af skarpe »grater« (rester af aluminium fra støbeprocessen). Hvis gratkanterne trænger gennem printets loddemaske, kan de skabe en kortslutning til 3,3 V-planet, så enheden ikke kan tændes.

Problemet kan afhjælpes ved at lægge elektrikertape af PVC oven på monteringsafsatserne.

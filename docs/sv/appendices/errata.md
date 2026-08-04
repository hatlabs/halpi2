# Kända fel

På den här sidan listas kända hårdvaruproblem i olika versioner av HALPI2.

## Enheter av version 0.4.0

#### Strömtopp vid påslag

När enheten slås på med helt urladdade superkondensatorer kan startströmmen ett kort ögonblick nå 1,1 A. Det gör att enheten nominellt inte uppfyller NMEA 2000-kravet på högst 1 A inström.

Den högre startströmmen beror på ett svårfångat samspel mellan de analoga ingångarna på mikrokontrollern RP2040 och strömbegränsningskretsen.

#### Kopparyta under monteringsklackarna

Ett 3,3 V-spänningsplan på kretskortets undersida sträcker sig ovanför monteringsklackarna. I vissa kapslingar har klackarna kvar vassa gjutgrader (rester av aluminium från gjutningen). Om en grads kant tränger igenom kretskortets lödmask kan den orsaka kortslutning mot 3,3 V-planet och hindra enheten från att starta.

Problemet åtgärdas genom att sätta eltejp av PVC ovanpå monteringsklackarna.

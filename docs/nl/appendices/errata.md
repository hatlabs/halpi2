# Bekende fouten

Op deze pagina staan de bekende hardwareproblemen van de verschillende HALPI2-versies.

## Apparaten van versie 0.4.0

#### Stroompiek bij het inschakelen

Wanneer het apparaat wordt ingeschakeld terwijl de supercondensatoren volledig leeg zijn, kan de inschakelstroom kortstondig oplopen tot 1,1 A. Daarmee voldoet het apparaat nominaal niet aan de NMEA 2000-eis van maximaal 1 A ingangsstroom.

De hoger dan gespecificeerde inschakelstroom komt door een moeilijk te doorgronden wisselwerking tussen de analoge ingangen van de RP2040-microcontroller en de stroombegrenzingsschakeling.

#### Kopervulling onder de montagerichels

Een 3,3 V-voedingsvlak op de onderste laag van de printplaat loopt door tot boven de montagerichels. In sommige behuizingen zitten op de montagerichels nog scherpe “bramen” (restjes aluminium uit het gietproces). Als die bramen door het soldeermasker van de printplaat heen dringen, kunnen ze kortsluiting maken met het 3,3 V-vlak, waardoor het apparaat niet ingeschakeld kan worden.

Het probleem is te verhelpen door pvc-isolatietape op de montagerichels aan te brengen.

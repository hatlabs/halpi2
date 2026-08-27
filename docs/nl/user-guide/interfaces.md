---
translated_from: 3cd9ceed5d700bf85ebce22f50f5e15a3f08013e
---

# Interfaces en connectiviteit

## CAN FD / NMEA 2000

De HALPI2 heeft een volledig galvanisch gescheiden [CAN FD](https://en.wikipedia.org/wiki/CAN_FD)-interface die zowel maritieme [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000)-netwerken als toepassingen in de automotive- en industriesector ondersteunt. De interface biedt snelle datacommunicatie en is door de volledige elektrische scheiding ongevoelig voor stoorsignalen.

### Specificaties van de interface

De CAN FD-interface ondersteunt zowel het standaard CAN-protocol als CAN FD. Voor NMEA 2000-toepassingen werkt de interface in de gewone CAN-modus met de standaarddatasnelheid van 250 kbit/s. Bij toepassingen in de automotive- of industriesector kan de interface de volledige CAN FD-mogelijkheden benutten, met datasnelheden tot 8 Mbit/s.

Op het frontpaneel zit een Micro-C-connector die compatibel is met standaard NMEA 2000-bekabeling en -componenten. Daardoor is rechtstreekse integratie in bestaande maritieme netwerken mogelijk met standaard T-stukken en aftakkabels.

### Voedingsconfiguratie en netwerkbelasting

Hoeveel de HALPI2 het NMEA 2000-netwerk belast, hangt af van de gekozen voedingsconfiguratie. In de standaardconfiguratie met externe voeding via de E7T-connector heeft het apparaat geen voeding uit het NMEA 2000-netwerk nodig, waardoor het belastingsgetal (LEN) 0 is.

Wordt het apparaat via de NMEA 2000-bus gevoed, dan moet de stroomafname door de interne stroombegrenzer tot 0,9 A worden beperkt. Dat komt overeen met een LEN-waarde van 18. Sluit de HALPI2 bij voeding via NMEA 2000 dicht bij de voedingskabel op de backbone van het netwerk aan, om de spanningsval te beperken en een betrouwbare werking te waarborgen.

### Hardwareconfiguratie

Het carrierboard bevat een afsluitweerstand van 120 Ω die via een jumper kan worden ingeschakeld. Afsluiting bij het apparaat zelf moet bij NMEA 2000-toepassingen worden vermeden, omdat de standaard dit niet toestaat. Bij toepassingen in de automotive- of industriesector met point-to-pointcommunicatie kan de jumper wel worden gezet om de afsluitweerstand in te schakelen.

Voor netwerkdiagnose en probleemoplossing heeft het carrierboard eigen RX- en TX-leds die netwerkactiviteit aangeven. Deze leds geven direct visuele terugkoppeling over het verzenden en ontvangen van gegevens, waardoor verbindingsproblemen eenvoudiger zijn vast te stellen.

### Netwerkinstallatie

De verbinding met NMEA 2000-netwerken komt tot stand met een standaard T-stuk (niet meegeleverd) in de backbone van het netwerk en een aftakkabel tussen het T-stuk en de Micro-C-connector van de HALPI2.

### Software-integratie

De CAN-interface integreert naadloos met Linux via het SocketCAN-framework en verschijnt als netwerkapparaat `can0`. Via deze standaardinterface kan het gebruikelijke Linux CAN-gereedschap voor bewaking en diagnose worden gebruikt. De netwerkinterface is in alle HALPI2-systeemimages (HaLOS, OpenPlotter en Raspberry Pi OS) voorgeconfigureerd.

Integratie met de Signal K-server is beschikbaar op de HaLOS Marine-imagevarianten en op OpenPlotter; de server detecteert de CAN-interface automatisch en gebruikt deze voor de verwerking van NMEA 2000-gegevens. Op niet-maritieme HaLOS-images kan Signal K worden geïnstalleerd via de Container Apps-store in Cockpit. De Signal K-server verzorgt de PGN-decodering en biedt webgebaseerde toegang tot de netwerkgegevens in realtime.

### Probleemoplossing

Netwerkdiagnose begint bij de RX/TX-leds op het carrierboard. Bij normale werking is er met tussenpozen ledactiviteit die overeenkomt met het netwerkverkeer. Ontbrekende RX-activiteit kan wijzen op bekabelingsproblemen of een onjuiste afsluiting; ontbrekende TX-activiteit kan duiden op conflicten op het netwerk of op bekabeling.

Met de Linux-opdracht `candump` kunt u de CAN-bus rechtstreeks vanaf de opdrachtregel volgen. Dit gereedschap geeft gedetailleerde informatie over alle berichten op de bus en maakt zo diepgaande diagnose mogelijk. In zijn eenvoudigste vorm voert u uit:

```bash
candump can0
```

Hiermee worden alle binnenkomende ruwe CAN-berichten in realtime getoond.

Het dashboard van de Signal K-server biedt aanvullende mogelijkheden voor netwerkbewaking. Het toont de actuele NMEA 2000-datasnelheden van de CAN-interface. Met het gereedschap Data Browser bekijkt u de gedecodeerde NMEA 2000-gegevens.

!!! quote "Gerelateerde informatie"
    - **Voedingsconfiguratie:** zie [Aan de slag](../getting-started/getting-started.md#vaste-voedingsinstallatie)
    - **Softwareconfiguratie:** zie [Softwarehandleiding](./software.md)
    - **Netwerkproblemen oplossen:** zie [Probleemoplossing](./troubleshooting.md)


## RS-485 (NMEA 0183)

De HALPI2 heeft een galvanisch gescheiden [RS-485](https://en.wikipedia.org/wiki/RS-485)-interface die seriële communicatie biedt voor maritieme [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422]-netwerken en voor industriële toepassingen.

[^rs422]: Technisch gezien gebruikt NMEA 0183 de RS-422-standaard, maar RS-485 is neerwaarts compatibel, waardoor de HALPI2 met zowel RS-422- als RS-485-apparaten kan communiceren.

### Specificaties van de interface

De RS-485-transceiver werkt met snelheden tot 10 Mbit/s, hoewel typische NMEA 0183-toepassingen de standaardbaudrates 4800 of 38400 bit/s gebruiken. De interface is galvanisch gescheiden en voldoet aan de NMEA 0183-specificatie, waardoor de HALPI2 beschermd is tegen aardlussen en tegen de elektrische ruis die in maritieme omgevingen veel voorkomt.

De interface is intern verbonden met UART 4 van de Raspberry Pi en verschijnt in het Linux-besturingssysteem als `/dev/ttyAMA4`. Dit standaard seriële apparaat is toegankelijk voor elke applicatie die seriële communicatie ondersteunt, waaronder de Signal K-server, OpenCPN en eigen softwaretoepassingen.

### Hardwareconfiguratie

Het carrierboard heeft eigen RX- en TX-leds die de communicatieactiviteit op de RS-485-interface aangeven. Deze leds geven tijdens installatie en probleemoplossing direct visuele terugkoppeling, zodat eenvoudig te controleren is of gegevens correct worden verzonden en ontvangen.

Wanneer het apparaat als algemene RS-485-interface wordt gebruikt, kan het worden ingesteld op automatische of handmatige zendvrijgave. In de handmatige modus stuurt een GPIO-pin het zendvrijgavesignaal aan, zodat de software bepaalt wanneer de interface zendt of ontvangt. Dat is nodig bij multi-talkertoepassingen, waarbij de interface in een recessieve toestand moet staan zolang deze niet zendt. In de automatische modus activeert de hardware het zendvrijgavesignaal zodra er gegevens worden verzonden, wat de opzet voor single-talkertoepassingen vereenvoudigt.

Daarnaast ondersteunt de RS-485-interface een halfduplexmodus, waardoor zenden en ontvangen over hetzelfde aderpaar mogelijk zijn.

De interface kan via de hardwareconfiguratie ook volledig worden uitgeschakeld als UART 4 voor andere doeleinden nodig is.

### Bedrading en aansluiting

Voor de RS-485-interface is een kabelwartel of paneelconnector nodig, die de gebruiker zelf moet aanschaffen. Een goede optie is [een SP13-pigtail-paneelconnector](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). De interface is neerwaarts compatibel met de RS-422-signalering van NMEA 0183 en ondersteunt zowel RS-485-multi-talkernetwerken als RS-422-netwerken met één talker en meerdere listeners. De interface werkt met gebalanceerde differentiële paren, aangeduid met TX+/TX- en RX+/RX-.

### Software-integratie

Alle HALPI2-images worden geleverd met een gebruiksklaar geconfigureerde RS-485-interface. Op HaLOS Marine-images en op OpenPlotter detecteert de Signal K-server de interface automatisch en ontvangt hij de verzonden NMEA 0183-gegevens.

Voor eigen toepassingen gedraagt de interface zich als een gewone seriële Linux-poort. Applicaties kunnen `/dev/ttyAMA4` openen en de baudrate, databits, stopbits en pariteit instellen zoals de aangesloten apparatuur vereist. Applicaties in Python, Node.js en C/C++ benaderen de interface alle eenvoudig met de gebruikelijke bibliotheken voor seriële communicatie.

### Veelvoorkomende toepassingen

In maritieme omgevingen wordt de RS-485-interface meestal verbonden met gps-ontvangers, dieptemeters, windmeters, AIS-transponders of andere apparaten die het NMEA 0183-protocol gebruiken. Industriële toepassingen zijn bijvoorbeeld de aansluiting van PLC's, sensoren en andere automatiseringsapparatuur die Modbus RTU of andere RS-485-protocollen gebruikt.

Door de hoge snelheid van de interface zijn ook niet-standaardtoepassingen mogelijk, zoals het verzamelen van sensorgegevens met een hoge frequentie of eigen communicatieprotocollen. Daarmee is de HALPI2 ook geschikt voor onderzoeksschepen en gespecialiseerde bewakingstoepassingen.

!!! quote "Gerelateerde informatie"
    - **Softwareconfiguratie:** zie [Softwarehandleiding](./software.md)
    - **Probleemoplossing:** zie [Probleemoplossing](./troubleshooting.md)


## GNSS (GPS)

De HALPI2 ondersteunt HAT's met GNSS-ontvanger die op UART0 (`/dev/ttyAMA0`) zijn aangesloten. Elke GNSS-ontvanger op deze poort werkt zonder verdere instellingen samen met gpsd.

Voor u-blox-ontvangers (zoals de Max-M8Q) bieden de HaLOS Marine-images bovendien een automatische configuratie die voor maritiem gebruik is geoptimaliseerd.

### Automatische configuratie (u-blox-ontvangers)

Op HaLOS Marine-images detecteert en configureert een systemd-dienst (`configure-ublox-marine`) bij elke start automatisch de aanwezige u-blox-ontvangers:

| Parameter | Waarde |
|:----------|:------|
| Baudrate | 115200 bit/s (fabrieksinstelling: 9600) |
| Updatesnelheid | 10 Hz (100 ms) |
| Dynamisch model | Sea (geoptimaliseerd voor maritiem gebruik) |

De configuratie draait bij elke start, omdat u-blox-modules met ROM (zoals de MAX-M8Q) geen flashgeheugen hebben. De instellingen worden opgeslagen in batterijgebufferd RAM (BBR) en kunnen verloren gaan wanneer de voeding van de backupbatterij wordt onderbroken — bijvoorbeeld wanneer het apparaat langere tijd spanningsloos is. De herconfiguratie verloopt onmerkbaar en verlengt de start van gpsd met ongeveer 2 seconden.

Wordt er geen ontvanger gedetecteerd, dan sluit de dienst zonder melding af. Een pas geïnstalleerde GNSS-HAT wordt bij de volgende herstart automatisch geconfigureerd.

### Toegang tot de gegevens

De gps-gegevens worden geleverd door [gpsd](https://gpsd.io/) op TCP-poort 2947. Op HaLOS Marine-images maakt Signal K automatisch verbinding met gpsd — verdere configuratie is niet nodig.

Gebruik voor diagnose het standaardgereedschap van gpsd op de opdrachtregel:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Andere images dan HaLOS

Op Raspberry Pi OS of andere besturingssystemen installeert en configureert u gpsd handmatig:

```bash
sudo apt install gpsd gpsd-clients
```

Bewerk `/etc/default/gpsd` om `DEVICES="/dev/ttyAMA0"` in te stellen en start de dienst opnieuw. De ontvanger werkt met de fabrieksinstellingen (9600 baud, 1 Hz), tenzij hij met `ubxtool` uit het pakket `gpsd-clients` wordt geconfigureerd.

!!! quote "Gerelateerde informatie"
    - **gpsd op HaLOS:** zie [de HaLOS-documentatie over gps](https://docs.halos.fi/user-guide/gps/)
    - **Softwareconfiguratie:** zie [Softwarehandleiding](./software.md)


## Ethernet

De HALPI2 heeft een gigabit-ethernetinterface die snelle netwerkverbindingen biedt voor gegevensoverdracht, toegang op afstand en integratie met netwerken aan boord. De ethernetaansluiting op het carrierboard is een standaard RJ45-connector. Die is doorverbonden naar een paneelconnector waarop een externe ethernetkabel kan worden aangesloten.

## Wifi

De Compute Module 5 heeft een eigen wifi- en Bluetooth-radio, een Cypress CYW43455. De antenne wordt aangesloten op de U.FL-connector op de CM5 en is doorverbonden naar de RP-SMA-connector op het frontpaneel. De plaats van de connector staat in de [Hardwarehandleiding](./hardware.md).

### Firmwarevarianten voor het accesspoint

Raspberry Pi OS levert twee firmwarevarianten voor deze radio en kiest ertussen met `update-alternatives`. De variant `minimal` is afgestemd op gebruik als accesspoint, maar mist functies die `standard` wel heeft.

| Variant | Clients op het accesspoint | Firmwareversie |
|:--------|:---------------------------|:---------------|
| `standard` (standaard) | ongeveer 7 | 7.45.265 (2023) |
| `minimal` | ongeveer 19 | 7.45.241 (2021) |

Gebruik de variant `minimal` op elke HALPI2 waarvan het accesspoint echt in gebruik is. Het aantal clients is de kleinste reden: in de praktijk loopt de variant `standard` al met een paar verbonden clients vast en laat daarna helemaal geen client meer toe.

Schakel de variant om:

```bash
sudo update-alternatives --config cyfmac43455-sdio.bin
```

Kies de regel `cyfmac43455-sdio-minimal.bin` en start het apparaat daarna opnieuw op. `update-alternatives` legt de keuze vast, zodat latere updates van het firmwarepakket die behouden.

De variant `minimal` maakt geheugen in de chip vrij voor die extra clientplaatsen door functies weg te laten:

- Automatische kanaalkeuze.
- DFS-radardetectie, waardoor de 5 GHz-kanalen die dat vereisen niet beschikbaar zijn.
- Roamingondersteuning volgens 802.11k/v/r en antennediversiteit.

Als het accesspoint na de omschakeling niet start, stel er dan een vast kanaal voor in, want de variant `minimal` kan er zelf geen kiezen. Op HaLOS heet het standaardprofiel van het accesspoint `Halos-AP`:

```bash
sudo nmcli connection modify Halos-AP wifi.band bg wifi.channel 6
```

Om terug te gaan naar de standaardfirmware voert u dezelfde opdracht uit en kiest u de regel `standard`, of voert u `sudo update-alternatives --auto cyfmac43455-sdio.bin` uit.

!!! quote "Gerelateerde informatie"
    - **Accesspoint instellen op HaLOS:** zie [HaLOS-netwerkdocumentatie](https://docs.halos.fi/user-guide/networking/)

## USB

De HALPI2 heeft in totaal vier ingebouwde USB 3.0-poorten van het type A, die snelle verbindingen bieden voor uiteenlopende randapparatuur. Eén poort is rechtstreeks doorverbonden met de USB 3.0-interface van de CM5; de andere drie lopen via een ingebouwde USB 3-hub. In de standaardconfiguratie zijn twee poorten naar het frontpaneel doorverbonden, terwijl twee poorten op het carrierboard beschikbaar zijn voor interne aansluitingen.

## HDMI

De HALPI2 heeft twee HDMI 2.0-poorten (HDMI0 en HDMI1) voor video-uitvoer. Het carrierboard biedt voor beide HDMI-poorten connectoren voor platte flexkabels (FFC). Deze zijn met speciale FFC-kabels naar het frontpaneel doorverbonden. De connectoren op het frontpaneel zijn gewone HDMI-connectoren van het type A.

De HDMI-uitgang van de HALPI2 ondersteunt betrouwbaar twee Full HD-videostromen (1080p). 4K-video-uitvoer werkt mogelijk wel, maar is niet gegarandeerd.

## MIPI (CSI/DSI)

Het carrierboard heeft twee MIPI-CSI/DSI-connectoren voor camera's en beeldschermen. Het zijn 22-pins FFC-connectoren (platte flexkabel) met een steek van 0,5 mm. Ze horen zonder aanpassingen te werken met nieuwere camera's en beeldschermen die compatibel zijn met de Raspberry Pi.

Vanwege de waterdichtheid moet het gebruik van FFC-kabels beperkt blijven tot interne verbindingen.

## Externe knoppen

De HALPI2 heeft op het carrierboard een 2×3-pinheader voor het aansluiten van externe knoppen. De behuizing heeft geen ingebouwde knoppen, zodat u de plaats en het type van de knoppen zelf kunt kiezen.

### Pinout van de knoppenheader

Het carrierboard heeft een 6-pins pinheader met drie benoemde knopfuncties:

| Opschrift | Functie | Beschrijving |
|:------|:---------|:------------|
| Reset | Reset van de controller | Hardwarereset (RUN-pin van de RP2040) |
| Power | Voeding van de Raspberry Pi | Aan/uit-knop van de CM5 (PWR_BUT-ingang) |
| User | Vrij instelbaar | Door de gebruiker gedefinieerde gebeurtenis (nog niet geïmplementeerd) |

Elke knopaansluiting gebruikt twee pinnen: één voor het knopsignaal en één voor massa. Gebruik drukknoppen met maakcontact (normally open, NO), die de signaalpin bij het indrukken met massa verbinden.

### Functies van de knoppen

**Resetknop:**
De resetknop voert een hardwarematige systeemreset uit door de RUN-pin van de RP2040 laag te trekken. Daarmee worden de controller, de CM5 en alle aangesloten randapparatuur volledig gereset. De resetknop is vooral nuttig bij noodherstel, wanneer het afsluiten via software is mislukt en het systeem niet meer reageert.

**Aan/uit-knop:**
De aan/uit-knop is rechtstreeks verbonden met de aan/uit-ingang van de CM5 en werkt precies zoals de aan/uit-knop van de Raspberry Pi 5. Met een dubbele druk op de knop wordt het systeem gecontroleerd afgesloten, zodat het besturingssysteem applicaties netjes kan sluiten en bestandssystemen kan ontkoppelen voordat de spanning wegvalt. Met een lange druk op de knop wordt het systeem meteen uitgeschakeld; gebruik dat alleen wanneer het systeem niet meer reageert.

**Gebruikersknop:**
De functie van de gebruikersknop wacht nog op implementatie in de software en wordt in toekomstige firmwareversies vrij instelbaar. Zodra de functie beschikbaar is, is deze knop bedoeld voor eigen acties en toepassingsspecifieke triggers, zodat u het gedrag van de knop kunt afstemmen op uw eigen werkwijze.

### Installatie van knoppen

#### Rechtstreekse montage in de behuizing

Voor rechtstreekse montage in de behuizing van de HALPI2 gebruikt u de gaten van 6 mm of 13 mm die al in het ontwerp van de behuizing aanwezig zijn. Verwijder eerst de bijbehorende blindpluggen uit deze gaten en monteer een waterdichte knop die bij de gatdiameter past. Sluit de knop met een geschikte kabel aan op de pinheader van het carrierboard en zorg voor een goede trekontlasting en een weerbestendige afdichting bij de doorvoer in de behuizing.

#### Montage op een extern paneel

Wilt u de knoppen op een bedieningspaneel op afstand monteren, kies dan een plaats die goed bereikbaar is en die weerbestendig blijft. Gebruik kabelwartels voor de kabeldoorvoeren en sluit de knoppen aan met een verlengkabel met aders van 22–26 AWG; houd de totale kabellengte onder de 3 m om de signaalkwaliteit te behouden. Gebruik bij installaties die aan vocht of zware omstandigheden blootstaan waterdichte connectoren op de verbindingspunten, zodat de werking op lange termijn betrouwbaar blijft.

#### Aansluiting

Alle knopaansluitingen op het carrierboard moeten female headerconnectoren met een steek van 2,54 mm gebruiken. Zorg voor een juiste uitlijning van de pinnen en een stevige verbinding, zodat er tijdens het gebruik geen contactproblemen ontstaan.

!!! quote "Gerelateerde informatie"
    - **Energiebeheer:** zie [Controller van het carrierboard](../technical-reference/controller.md)
    - **Hardwaretoegang:** zie [Hardwareonderhoud](./hardware.md)

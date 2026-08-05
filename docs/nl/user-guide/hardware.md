---
translated_from: 9741366021074655d667fcf3a93a634f86f3519a
---

# Hardwarehandleiding

## Toegang tot de behuizing

De HALPI2 heeft een gepoedercoate behuizing van spuitgietaluminium met voorgeboorde gaten voor paneelconnectoren. Wanneer inwendige aanpassingen of onderhoud nodig zijn, kunt u de behuizing openen volgens de onderstaande procedures.

### De behuizing openen

Zorg er om bij de inwendige onderdelen te komen eerst voor dat het apparaat volledig is uitgeschakeld en dat de voedingskabels zijn losgekoppeld. Het deksel is bevestigd met vier verzonken M4×10-schroeven met PH2-kop. Draai deze schroeven los met een PH2-schroevendraaier en neem het deksel weg.

### Opnieuw monteren

Controleer voordat u de behuizing weer sluit rustig of alle inwendige verbindingen goed vastzitten en juist zijn geplaatst. Leg de kabels zorgvuldig, zodat ze niet bekneld raken en geen scherpe bochten maken.

Het is gemakkelijk om de platte flexkabels (FFC's) per ongeluk verkeerd om aan te sluiten. Kijk naar de pijlen bij “Contacts” op de opdruk om de juiste richting te controleren.

Let vooral op het afdichtingsrubber van het deksel: controleer op beschadigingen, vuil of verschuiving die de weerbestendige afdichting van de behuizing kunnen aantasten.

Draai de vier M4×10-dekselschroeven weer vast met de PH2-schroevendraaier. Draai ze niet te vast aan.


## Paneelconnectoren

### Standaardconfiguratie

De HALPI2 wordt geleverd met een standaard connectorconfiguratie die voor de meeste toepassingen volstaat. De standaardindeling omvat:

- **E7T-voedingsconnector**
- **NMEA 2000-microconnector**
- **Gigabit-ethernet RJ45**
- **HDMI-uitgang**
- **2× USB 3.0 Type-A**
- **3× posities voor PG7-kabelwartels** (met blindpluggen)
- **2× RP-SMA-antenneposities** (met blindpluggen)
- **Ontluchtingsplug** voor drukvereffening

![Connectoren en blindpluggen op het frontpaneel](./front-panel-connectors-all.jpg)
*Connectoren en blindpluggen op het frontpaneel. De groen gemarkeerde connectoren maken deel uit van de standaardconfiguratie. De gele posities zijn blindpluggen die desgewenst door connectoren kunnen worden vervangen. De rode positie is de ontluchtingsplug, die niet mag worden verwijderd.*

### Eigen connectoropties

Hebt u andere connectortypen nodig, dan kunt u de paneelconfiguratie aanpassen:

#### Connectoren verwijderen

!!! warning "Belangrijk"
    Pas connectoren alleen aan wanneer het apparaat is uitgeschakeld en van alle bronnen is losgekoppeld.

    Kunststof schroefdraad kan beschadigen als u te vast aandraait. Gebruik gewone dopsleutels, maar draai alleen handvast aan.

1. **Gebruik de juiste dopmaat:**
    - Grote connectoren: dop van 26 mm
    - Nylon M6-bouten: dop van 10 mm
    - RP-SMA-connectoren: dop van 8 mm
    - PG7-posities: grote platte schroevendraaier, dop van 17 mm

2. **Verwijder ze voorzichtig** – kunststof schroefdraad kan beschadigen als u te vast aandraait

3. **Bewaar de verwijderde onderdelen** voor eventueel later gebruik

#### Nieuwe connectoren installeren

1. **Gebruik uitsluitend connectoren van maritieme kwaliteit** of connectoren die geschikt zijn voor de omgeving
2. **Zorg voor een goede afdichting** – aan de binnenzijde is een brede flens nodig
3. **Draai alleen handvast aan** – draai kunststof schroefdraad niet te vast
4. **Pas de onderdelen eerst proef** voor de definitieve montage

## Inwendige indeling

- Het carrierboard van de HALPI2 is de hoofdprint van de computer: het draagt de Compute Module 5 (CM5) aan de onderzijde en verzorgt het energiebeheer, de indicatoren en de aansluitingen voor alle interfaces.

### Functionele gebieden van het carrierboard

De belangrijkste functionele gebieden van het carrierboard zijn te zien op de onderstaande afbeelding.

![Indeling van het carrierboard, bovenzijde](./carrier-board-top-layout.jpg)
*Indeling van de bovenzijde van het carrierboard, met de belangrijkste functionele gebieden.*

### Connectoren op het carrierboard

De functies zijn bereikbaar via een aantal connectoren op het board, te zien op de onderstaande afbeelding.

![Connectoren op het carrierboard, bovenzijde](./carrier-board-top-conx.jpg)
*Connectoren op de bovenzijde van het carrierboard.*

Hieronder staat een overzicht van de connectoren aan de bovenzijde.

| Aanduiding | Beschrijving |
|:------|:------------|
| **a1** | Voedingsconnector (type Phoenix MC, 3,81 mm steek) |
| **a2** | Schakelaar voor de begrenzing van de ingangsstroom (0,9 A of 2,5 A) |
| **a3** | Jumper voor de voedingsregeling. Overbrug de pinnen “3.3V off” om de 3,3 V-rail geforceerd uit te schakelen. Overbrug de pinnen “5V on” om de 5 V-rail geforceerd in te schakelen. **NB:** op boards van versie 0.4.0 zijn de connectoren **a3** en **c2** anders ingedeeld. |
| **b1** | Ethernetaansluiting (RJ45) |
| **c1** | USB-poort van de controller. Wordt gebruikt om de firmware van de RP2040-microcontroller te flashen. |
| **c2** | Jumperheader “MCU USB BOOT”. Overbrug de pinnen om de RP2040 in de USB-bootmodus te zetten. |
| **c3** | Debugheader van de controller |
| **c4** | Niet-bestukte GPIO-pinheader van de controller |
| **c5** | Knoppenheaders. Voor het aansluiten van de knoppen Power, Reset en User. |
| **c6** | Aan/uit-knop. Voor het in- en uitschakelen van de Compute Module 5. |
| **d1** | 40-pins GPIO-pinheader van de Raspberry Pi |
| **e1** | MIPI0-connector voor een camera- of beeldscherminterface |
| **e2** | MIPI1-connector voor een camera- of beeldscherminterface |
| **f1** | HDMI0-connector |
| **f2** | HDMI1-connector |
| **g1** | M.2-connector voor de NVMe SSD |
| **h1** | CAN FD-interface (type Phoenix MC, 3,81 mm steek) |
| **h2** | Jumper voor de CAN-afsluitweerstand. Overbrug de pinnen om de afsluitweerstand van de CAN FD-bus in te schakelen. |
| **i1** | RS-485-interface (type Phoenix MC, 3,81 mm steek) |
| **i2** | Jumper voor de automatische/handmatige RS-485-enable. |
| **i4** | Jumper “XRS-485 RX Enable”. Overbrug de pinnen om het ontvangen van RS-485-verkeer in te schakelen. |
| **j1** | USB-bootconnector van de Compute Module. Wordt gebruikt om de firmware van de Compute Module 5 te flashen. |
| **j2** | Keuzeschakelaar voor de bootmodus van de Compute Module. Zet hem op `Normal` voor normaal gebruik en op `Abnormal` voor de USB-bootmodus. Er gaat een waarschuwingsled branden wanneer de schakelaar op `Abnormal` staat. |
| **m1** | USB3-connector 0. Rechtstreeks verbonden met de CM5. |
| **m2** | USB3-connector 1-0. Verbonden met de USB3-hub op het board. |
| **m3** | USB3-connector 1-1. Verbonden met de USB3-hub op het board. |
| **m4** | USB3-connector 1-2. Verbonden met de USB3-hub op het board. |
| **n1** | CR2032-batterijhouder voor de realtimeklok (RTC) |
| **q1** | Ventilatorconnector voor de CM5. Met een ventilator kunt u de luchtcirculatie in de behuizing verbeteren. Bij de standaardbehuizing is dat niet nodig. |

![Connectoren op het carrierboard, onderzijde](./carrier-board-bottom-conx.jpg)
*Connectoren op de onderzijde van het carrierboard.*

Hieronder staat een overzicht van de connectoren aan de onderzijde.

| Aanduiding | Beschrijving |
|:------|:------------|
| **p1** | Connector voor de Compute Module 5. |
| **q1** | Ventilatorconnector voor de CM5, alternatieve plaats. Op deze header kunt u bij een eigen behuizing een processorventilator boven de CM5-module aansluiten. **NB:** de connectoren **q1** en **q2** zijn parallel geschakeld en mogen niet tegelijk worden gebruikt. |

Tot slot zit de antenneconnector voor wifi en Bluetooth op de Compute Module 5 zelf. Hij is te zien op de onderstaande afbeelding.

![Antenneconnector voor wifi](./cm5-top-conx.jpg)
*U.FL-antenneconnector op de Compute Module 5.*

| Aanduiding | Beschrijving |
|:------|:------------|
| **r1** | U.FL-connector voor de wifi- en bluetoothantenne. |

### Blinkenlights

Het carrierboard heeft verschillende statusleds voor de bewaking van het systeem.

![Statusleds op het carrierboard](./carrier-board-top-leds.jpg)
*Statusleds op het carrierboard en hun kleuren.*

De statusleds geven informatie over de voedings- en activiteitstoestand van het systeem. Hieronder staat een overzicht van de statusleds.

| Aanduiding | Kleur | Beschrijving |
|-------|:-------|:------------|
| **1** | RGB | Vijf RGB-leds. Deze leds geven op het frontpaneel de systeemstatus en de activiteit aan. |
| **2** | Rood | Voedingsleds voor de 3,3 V- en de 5 V-rail. Deze leds geven de voedingsstatus van de betreffende spanningsrails aan. |
| **3** | Geel | Snelheidsindicator van ethernet. Brandt wanneer de ethernetaansluiting een verbinding van 100/1000 Mbit/s heeft onderhandeld. |
| **4** | Groen | Activiteitsindicator van ethernet. Knippert wanneer er netwerkverkeer op de ethernetaansluiting is. |
| **5** | Blauw | Activiteitsindicator van de SSD. Knippert wanneer er lees- of schrijfactiviteit op de M.2 NVMe SSD is. |
| **6** | Rood | Voedingsstatusindicator van de Pi. Brandt wanneer het systeem spanning heeft maar is afgesloten. |
| **7** | Groen | Activiteitsindicator van de Pi. Knippert wanneer er activiteit op de Raspberry Pi is. |
| **8** | Amberkleurig | Waarschuwing voor de abnormale bootmodus. Brandt wanneer de USB-bootmodusschakelaar op `Abnormal` staat. Dat betekent dat het apparaat is ingesteld om te flashen via de USB-bootconnector en niet normaal opstart. |
| **9** | Groen | TX/RX-leds van CAN. Deze leds knipperen wanneer er gegevens worden ontvangen (RX) of verzonden (TX) op de CAN-interface. |
| **10** | Groen | TX/RX-leds van RS-485. Deze leds knipperen wanneer er gegevens worden ontvangen (RX) of verzonden (TX) op de RS-485-interface. |

De patronen van de RGB-leds staan beschreven in de [Systeemwerking](./operation.md#statusleds).

## Instelling van de stroombegrenzing

Het carrierboard heeft een stroombegrenzer waarmee u de maximale stroom naar de randapparatuur instelt. Om de schakelaar te vinden, kijkt u naar de plaats van schakelaar **a2** op de afbeelding in het onderdeel [Connectoren op het carrierboard](#connectoren-op-het-carrierboard).

!!! info "Instellingen van de stroombegrenzing"
    **Stand 0,9 A (standaard):**

    - Verplicht bij busvoeding via NMEA 2000
    - Geschikt voor normaal gebruik

    **Stand 2,5 A:**

    - Voor randapparatuur met een hoog stroomverbruik
    - Sneller opladen van de supercondensatoren
    - Alleen bij een eigen voedingsaansluiting

Schakel de HALPI2 eerst volledig uit en verwijder het deksel van de behuizing volgens de procedure in het onderdeel Toegang tot de behuizing. Zoek de stroombegrenzer op het carrierboard en zet de schakelaar in de gewenste stand (0,9 A of 2,5 A). Zet de behuizing na het wijzigen van de instelling weer in elkaar en controleer of alle verbindingen goed vastzitten.

## HAT's gebruiken

### Compatibiliteit van HAT's

De HALPI2 ondersteunt standaard Raspberry Pi-HAT's via de 40-pins GPIO-pinheader en is volledig elektrisch en mechanisch compatibel met de HAT-specificatie van de Raspberry Pi. Het carrierboard heeft dezelfde GPIO-pinbezetting als een gewone Raspberry Pi, zodat de meeste HAT's die voor de Raspberry Pi 4 en 5 zijn ontworpen zonder aanpassing werken. Dat geldt zowel voor officiële Raspberry Pi-HAT's als voor uitbreidingsprinten van derden die de HAT-standaard volgen.

### Fysieke beperkingen

De behuizing van de HALPI2 biedt 45 mm vrije ruimte boven het carrierboard, genoeg voor maximaal twee gestapelde HAT's. Het gebied links van de aangegeven HAT-zone wordt ingenomen door de supercondensatoren, waardoor er minder ruimte is voor HAT's die groter zijn dan de standaardafmetingen van 65 × 56 mm. Let vooral op HAT's met connectoren aan de zijkant. Connectoren die naar het “zuiden” of “oosten” wijzen passen doorgaans wel, maar connectoren die naar het “westen” wijzen kunnen tegen de supercondensatoren aan komen.

### Conflicten met GPIO-pinnen

Een aantal GPIO-pinnen wordt gebruikt door de ingebouwde interfaces van de HALPI2 en moet u meewegen bij het kiezen van een compatibele HAT. De onderstaande tabel geeft de gereserveerde GPIO-pinnen en hun functies:

| GPIO-nummer | Functie | Interface | Opmerkingen |
|----------|----------|-----------|-------|
| GPIO 2 | I2C SDA | Systeem-I2C | Deelbaar; adres 0x6d gereserveerd |
| GPIO 3 | I2C SCL | Systeem-I2C | Deelbaar; adres 0x6d gereserveerd |
| GPIO 6 | SPI CS | CAN FD | Aangepaste chipselect voor de CAN-controller |
| GPIO 9 | SPI MISO | CAN FD | Gedeelde SPI0-bus |
| GPIO 10 | SPI MOSI | CAN FD | Gedeelde SPI0-bus |
| GPIO 11 | SPI SCK | CAN FD | Gedeelde SPI0-bus |
| GPIO 12 | UART TX | RS-485 | UART4 zenden |
| GPIO 13 | UART RX | RS-485 | UART4 ontvangen |
| GPIO 24 | RS-485 EN | RS-485 | Enable-signaal (alleen in de handmatige modus) |
| GPIO 26 | CAN INT | CAN FD | Interruptlijn voor de CAN-controller |

### Interfaces delen en conflicten

De I2C-bus op GPIO 2 en 3 kunt u delen met apparaten op een HAT, omdat I2C meerdere apparaten op dezelfde bus ondersteunt. HAT's mogen echter niet het I2C-adres 0x6d gebruiken; dat is gereserveerd voor de systeemcontroller van de HALPI2. De meeste I2C-HAT's werken zonder problemen, maar controleer de gebruikte I2C-adressen voor de installatie.

De SPI0-bus die voor de CAN FD-interface wordt gebruikt, kunt u mogelijk delen met andere SPI-apparaten, omdat de HALPI2 een aangepaste chipselectpin (GPIO 6) en interruptpin (GPIO 26) gebruikt. HAT's die SPI0 met de standaard chipselectpinnen (GPIO 7 of GPIO 8) gebruiken, kunnen naast de CAN-interface functioneren, maar vergen mogelijk extra configuratie met een device tree overlay.

### Ingebouwde interfaces uitschakelen

Heeft een HAT exclusief gebruik nodig van pinnen die door de ingebouwde interfaces van de HALPI2 bezet zijn, dan kunt u die interfaces uitschakelen met een hardwareaanpassing. De CAN FD-interface komt volledig vrij door de soldeerjumper GPIO6-CAN.CS aan de onderzijde van het carrierboard te verwijderen. Daarmee wordt de CAN-controller van de SPI-bus losgekoppeld en komen GPIO 6, 9, 10, 11 en 26 vrij voor de HAT.

De RS-485-interface schakelt u uit door de RX-enable-jumper (i4) op het carrierboard te verwijderen. Daarmee kan de RS-485-transceiver geen gegevens meer ontvangen en komen GPIO 12 en 13 vrij voor ander gebruik. Is handmatige besturing van de zend-enable niet nodig, dan kunt u ook GPIO 24 anders inzetten door de jumper voor de automatische/handmatige RS-485-enable (i2) in de automatische stand te zetten.

### Installatieprocedure

Schakel het systeem uit en koppel alle voedingsbronnen los voordat u begint. Verwijder het deksel van de behuizing volgens de procedure in het onderdeel Toegang tot de behuizing.

Carrierboards van versie 0.5.0 en later hebben op de vier HAT-montageposities al M2,5-draadinzetstukken zitten, wat de installatie vereenvoudigt. Bij oudere boards van v0.4.0 moet u de M2,5-moeren zelf aanbrengen. Daarvoor moet het carrierboard tijdelijk worden gedemonteerd. Dat kan zonder alle kabels los te koppelen.

Voor veel gangbare HAT's voldoen afstandsbussen van 15 mm, maar meet de hoogte van de female header op de HAT om te zorgen voor de juiste vrije ruimte. De voet van de male header is 2,5 mm hoog; tel die op bij de hoogte van de female header om de benodigde lengte van de afstandsbus te bepalen.

Draai de afstandsbussen in de bevestigingsgaten, of zet ze bij v0.4.0-boards van onderaf vast met moeren. Lijn de HAT uit met de 40-pins GPIO-pinheader en controleer of alle pinnen goed staan voordat u met gelijkmatige druk de connector aandrukt. De HAT hoort evenwijdig aan het carrierboard te zitten, zonder zichtbare spleet bij de GPIO-verbinding.

Zet de HAT vast met M2,5-schroeven of met extra afstandsbussen door de bevestigingsgaten van de HAT in de onderliggende afstandsbussen. Deze schroeven worden niet bij de HALPI2 geleverd; u moet ze apart aanschaffen. Draai de schroeven net zo ver aan dat de HAT vastzit zonder dat de print doorbuigt.

### Kabelbeheer

Heeft de HAT connectoren die van buiten de behuizing bereikbaar moeten zijn, overweeg dan geschikte paneelconnectoren te plaatsen op de beschikbare posities voor PG7-kabelwartels. Zo blijft de omgevingsbescherming van de behuizing behouden en hebt u toch eenvoudig toegang van buitenaf.

### Verwijderingsprocedure

Het verwijderen van een HAT verloopt in omgekeerde volgorde van de installatie. Schakel het systeem volledig uit en koppel alle voedingsbronnen los voordat u de behuizing opent. Verwijder de M2,5-montageschroeven en til de HAT voorzichtig recht omhoog van de GPIO-pinheader, zonder zijdelingse kracht die de pinnen van de header kan verbuigen.

Zit de HAT vast, controleer dan eerst op over het hoofd gezien bevestigingsmateriaal of kabels voordat u meer kracht zet. Bij sommige HAT's met strak zittende connectoren is een lichte wrikkende beweging tijdens het omhoogtrekken nodig. Wrik de HAT in de noord-zuidrichting; wrikken in de oost-westrichting kan de pinnen van de header verbuigen wanneer de connector plotseling loskomt.

### Softwareconfiguratie

Na de hardware-installatie heeft de HAT mogelijk nog softwareconfiguratie nodig om goed te werken. Veel HAT's brengen device tree overlays mee die in de configuratie van de Raspberry Pi moeten worden ingeschakeld. Bewerk `/boot/firmware/config.txt` en voeg de juiste `dtoverlay`-regels toe zoals beschreven in de documentatie van uw HAT.

!!! quote "Gerelateerde informatie"
    - **Referentie van de GPIO-pinbezetting:** zie [Hardwarereferentie](../technical-reference/hardware.md)
    - **Softwareconfiguratie:** zie [Geavanceerde configuratie](../software-development/advanced-config.md)
    - **Aanpassingen aan de behuizing:** zie [Eigen connectoropties](#eigen-connectoropties)

## De NVMe SSD vervangen

### Compatibiliteit van SSD's

De HALPI2 ondersteunt M.2-NVMe-SSD's van 2230 tot en met 2280 in de standaard enkelzijdige uitvoering. Kortere 2230-modellen mogen dubbelzijdig zijn dankzij de extra vrije ruimte op die montagepositie, maar langere modellen moeten enkelzijdig zijn om op het carrierboard te passen.

Compatibiliteit kan alleen worden gegarandeerd voor SSD's die door Hat Labs worden geleverd en voor officiële Raspberry Pi-SSD's. Overweegt u een schijf van een andere fabrikant, controleer dan voor aanschaf de compatibiliteit met de Raspberry Pi 5 aan de hand van gebruikerservaringen en compatibiliteitslijsten op internet. Veelvoorkomende problemen met incompatibele schijven zijn een te hoog stroomverbruik, oververhitting en opstartfouten of een instabiel systeem.

### De nieuwe SSD voorbereiden

Voordat u een nieuwe SSD in de HALPI2 plaatst, moet het besturingssysteem op de schijf worden geflasht. Het is ook mogelijk de SSD na de installatie te flashen via de USB-bootconnector (j1) van de CM5, maar met een externe USB-naar-NVMe-adapter gaat het eenvoudiger en sneller. De flashprocedure staat beschreven in de [Softwarehandleiding](./software.md).

### De 3,3 V-systeemspanning uitschakelen

De supercondensatoren kunnen de 3,3 V-rail van het carrierboard nog geruime tijd van spanning voorzien nadat de hoofdvoeding is losgekoppeld. Omdat de SSD uit de 3,3 V-rail wordt gevoed, moet u die rail uitschakelen zodat de SSD bij het verwijderen of plaatsen gegarandeerd spanningsloos is.

Schakel eerst de HALPI2 uit en koppel de voeding los. Open de behuizing volgens de procedure in het onderdeel Toegang tot de behuizing.

Zoek de jumper “3.3V off” op het carrierboard. De plaats verschilt per boardversie. Op v0.4.0-boards zit de jumper vlak bij de supercondensatoren, aan hun “zuidzijde”. Op boards van v0.5.0 en later zoekt u de header “Pow.Ctrl” ten “oosten” van de supercondensatoren. De pinnen “3.3V off” zijn de bovenste twee op die header.

Verplaats de jumper zodat de pinnen “3.3V off” worden overbrugd. Daarmee schakelt u de 3,3 V-rail uit, wat te zien is doordat de leds uitgaan.

### Verwijderingsprocedure

Het M.2-slot bevindt zich aan de zuidrand van het carrierboard. Raadpleeg de afbeelding in het onderdeel [Connectoren op het carrierboard](#connectoren-op-het-carrierboard) om de M.2-connector met de aanduiding **g1** te vinden.

Verwijder de M2,5-montageschroef met een PH1-schroevendraaier. Zodra de schroef eruit is, veert de SSD schuin omhoog. Til de schijf voorzichtig op aan de bevestigingszijde en beweeg hem met kleine bewegingen uit de M.2-connector. Pak de SSD bij de randen vast om de componenten en connectoren niet te beschadigen.

### Installatieprocedure

Steek de voorbereide SSD onder een hoek van ongeveer 30 graden in de M.2-connector en zorg dat de inkeping in de SSD samenvalt met de sleutel in de connector. De schijf hoort soepel naar binnen te glijden, zonder kracht. Druk daarna de bevestigingszijde van de SSD omlaag tot die vlak op de afstandsbus ligt.

Zet de SSD vast met de M2,5-montageschroef en een PH1-schroevendraaier. Draai de schroef net zo ver aan dat de schijf stevig op zijn plaats blijft. De SSD hoort volkomen vlak te liggen, zonder zichtbare buiging.

Zodra de SSD op zijn plaats zit, haalt u de jumper van de pinnen “3.3V off” om de 3,3 V-rail weer in te schakelen. Bewaar de jumper op de header voor later gebruik.

Zet de behuizing weer in elkaar zoals beschreven in het onderdeel Toegang tot de behuizing.
Voor softwareconfiguratie of het oplossen van problemen raadpleegt u de [Softwarehandleiding](./software.md).

!!! quote "Gerelateerde informatie"
    - **Systeemimages:** zie [Softwarehandleiding](./software.md)
    - **Opstartprocedures:** zie [Systeemwerking](./operation.md)
    - **Toegang tot de hardware:** zie [Toegang tot de behuizing](#toegang-tot-de-behuizing)

## De Compute Module 5 vervangen

### Voorwaarden vooraf

Het vervangen van de Compute Module 5 vraagt om zorgvuldig werken, omdat de board-to-boardconnectoren kwetsbaar zijn. De CM5 gebruikt twee connectoren met een hoge pindichtheid die gemakkelijk beschadigen bij te veel kracht of een verkeerde techniek. Demonteer een geplaatste module alleen wanneer het echt nodig is, bijvoorbeeld als de module defect is of moet worden vervangen door een zwaardere uitvoering. Schade aan de montageconnectoren van de compute module — op de CM5 of op het carrierboard — valt niet onder de garantie.

Zorg dat u vooraf thermische pads voor de warmteafvoer bij de hand hebt. In de standaarduitvoering zit een pad van 1 mm dik op de SoC en zitten er pads van 2 mm dik op de RP1-chip en op de componenten van de interne voeding. Bestaande thermische pads kunt u hergebruiken als ze onbeschadigd en schoon zijn.

### Bij de Compute Module komen

Schakel de HALPI2 uit en koppel de voedingsbron los. Verwijder het deksel van de behuizing volgens de procedure in het onderdeel Toegang tot de behuizing. De CM5 zit aan de onderzijde van het carrierboard, dus u moet eerst het carrierboard uit de behuizing demonteren. Maak vooraf een paar foto's van de aansluitingen, zodat u het overzicht houdt over de vele kabels die op het carrierboard zijn aangesloten.

Koppel alle kabels los die het uitnemen van het carrierboard in de weg zitten. Verwijder de montageschroeven van het carrierboard en til het board uit de behuizing.

### De aanwezige module verwijderen

!!! danger "Let op"
    Als u de CM5-module connector voor connector loskoppelt, kunnen de wringkrachten de connector van de CM5-module afscheuren. Deze schade valt niet onder de garantie.

De CM5 wordt vastgehouden door twee board-to-boardconnectoren die zorgvuldig behandeld moeten worden. Gebruik hierbij nooit metalen gereedschap: dat kan de connectoren of nabijgelegen SMD-componenten beschadigen. Gebruik een houten of kunststof spudger, een plectrum of vergelijkbaar niet-geleidend gereedschap.

Plaats het gereedschap midden op de linker korte zijde van de CM5-module, tussen de module en het carrierboard. Druk de hoeken aan de rechterzijde stevig omlaag. Wrik voorzichtig en met minimale kracht omhoog – de module hoort met een lichte klik los te komen, waarbij beide connectoren tegelijk losschieten.

![De CM5-module demonteren](./unmount-cm5.jpg)
*Demonteer de CM5-module door de hoeken aan de rechterrand omlaag te drukken en tegelijk midden aan de linkerrand omhoog te wrikken. Beide connectoren horen tegelijk los te komen.*

### De nieuwe module plaatsen

Lijn de nieuwe CM5-module uit met de connectoren op het carrierboard en gebruik daarbij de omtrek op de opdruk van het carrierboard als hulp. Bij de juiste oriëntatie komt de op het carrierboard gedrukte omtrek van de module exact overeen met de afmetingen van de CM5.

Oefen na het uitlijnen zachte, gelijkmatige druk uit op de plaats van de connectoren aan beide korte zijden van de module. De connectoren horen met een lichte, voelbare klik vast te klikken. Druk stevig, maar buig het carrierboard niet door – ondersteun het board zo nodig van onderaf. Beide connectoren moeten volledig zijn ingedrukt voor een goede werking.

Breng vervolgens de thermische pads aan op de CM5-module. Let op de juiste plaatsing: een pad van 1 mm op de hoofd-SoC en pads van 2 mm op de RP1-chip en op de componenten van de voeding. Hergebruikt u bestaande pads, zorg er dan voor dat ze schoon zijn en goed liggen.

![Plaatsing van de thermische pads op de CM5](./cm5-thermal-pads-annotated.jpg)
*Plaatsing van de thermische pads op de Compute Module 5. Gebruik een pad van 1 mm dik op de SoC (midden) en pads van 2 mm dik op de RP1 en op de componenten van de voeding. De werkelijke vorm en afmetingen van de thermische pads kunnen afwijken.*

### De antenne aansluiten

Sluit de U.FL-antennekabel aan op de draadloze antenneconnector van de CM5 voordat u het carrierboard terugplaatst. Zodra het carrierboard weer is gemonteerd, is deze aansluiting onbereikbaar. De U.FL-connector moet nauwkeurig worden uitgelijnd en met stevige druk worden vastgeklikt. Er is een duidelijke klik voelbaar zodra de connector volledig vastzit. Let op dat u de huls van de connector niet verbuigt tijdens het aansluiten.

### Eindmontage

Controleer de montage van de module: beide connectoren moeten volledig zijn ingedrukt en de module moet vlak op het carrierboard liggen, zonder spleten. De thermische pads horen contact te maken met de warmteproducerende componenten van de module.

Plaats het carrierboard terug in de behuizing en zorg dat de thermische pads op de CM5 samenvallen met de bijbehorende warmteafvoervlakken in de bodem van de behuizing. Draai alle montageschroeven van het carrierboard weer vast en sluit de kabels aan die u tijdens het demonteren hebt losgekoppeld.

Rond de montage af volgens de standaardprocedure voor het sluiten van de behuizing. Bij de eerste start hoort het systeem de nieuwe CM5 automatisch te herkennen.

!!! warning "Waarschuwing over de connectoren"
    De board-to-boardconnectoren zijn de kwetsbaarste onderdelen in deze procedure. Gebruik nooit metalen gereedschap in de buurt van de connectoren, oefen bij het verwijderen en plaatsen uitsluitend verticale kracht uit, en zorg voor een perfecte uitlijning voordat u druk zet. Beschadigde connectoren betekenen doorgaans dat het carrierboard vervangen moet worden.

!!! quote "Gerelateerde informatie"
    - **Systeeminstellingen na vervanging:** zie [Softwarehandleiding](./software.md)
    - **Problemen bij het opstarten:** zie [Probleemoplossing](./troubleshooting.md)
    - **Warmtebeheer:** zie [Hardwarereferentie](../technical-reference/hardware.md)

---
translated_from: a51e1cfe53d070c073a563641f9301fd3383a418
---

# Aan de slag

Deze handleiding zorgt ervoor dat uw HALPI2 binnen 30 minuten draait en behandelt ook de vaste installatie. Volg deze stappen in volgorde voor een zo soepel mogelijke installatie — begin met een opstelling op het bureau om te controleren of alles werkt, en ga daarna verder met de vaste installatie.

## Veiligheid en voorzorgsmaatregelen

!!! warning "Voordat u begint"
    - Zorg dat de spanning van uw elektrische systeem is afgeschakeld voordat u aansluitingen maakt
    - Gebruik geschikte zekeringen (3–5 A) voor de voedingsaansluitingen
    - Behandel het apparaat voorzichtig — hoewel het robuust is, kunnen vallen of stoten interne componenten beschadigen
    - Controleer de juiste polariteit bij het aansluiten van de voedingskabels
    - Voorkom ontladingen van statische elektriciteit — aard uzelf en wrijf niet over katten of barnstenen voorwerpen voordat u interne componenten aanraakt

## Wat u nodig hebt

Uit uw HALPI2-pakket:

- HALPI2-apparaat met vooraf geïnstalleerde CM5 en NVMe SSD
- Voedingskabel met E7T-connector (2 m lang)

Optionele onderdelen (meegeleverd in de verkoopverpakking):

- Set DC-pluggen (barrel connectors, 5,5 × 2,1 mm), wanneer u een standaard 12 V-voedingsadapter van het type “wall wart” gebruikt
- Raspberry Pi-antenne voor wifi en Bluetooth (vereist als wifi wordt gebruikt voor de eerste installatie)

Aanvullende onderdelen (niet meegeleverd):

- 12 V- of 24 V-voedingsbron
- Een aparte computer voor installatie zonder beeldscherm (headless), als er geen beeldscherm is aangesloten
- Netwerkkabel (optioneel, voor een bekabelde verbinding)
- Beeldscherm met HDMI-ingang (optioneel)
- USB-toetsenbord en -muis (optioneel, voor directe toegang)

!!! tip "Handige tip"
    Netwerkapparatuur zoals een router of wifi-accesspoint gebruikt meestal een 12 V-voedingsadapter waarmee u ook de HALPI2 kunt voeden. Kijk eens in uw stapel oude hardware!

## Opstelling op het bureau

Wij raden aan de HALPI2 eerst op een bureau of werkbank uit te proberen voordat u hem vast installeert. De eerste installatie kunt u uitvoeren zonder beeldscherm (headless) via een netwerkverbinding, of met een aangesloten beeldscherm, toetsenbord en muis. Een installatie zonder beeldscherm verloopt via een bekabelde ethernetverbinding of via het wifi-accesspoint van de HALPI2.

### Stap 1: essentiële randapparatuur aansluiten

#### Voor de eerste installatie:

1. **Netwerkverbinding (vereist voor installatie zonder beeldscherm):**
    - Sluit de ethernetkabel aan
    - Sluit de antenne voor wifi en Bluetooth aan

2. **Beeldschermaansluiting (optioneel):**
    - Sluit een HDMI-beeldscherm aan voor directe toegang
    - USB-toetsenbord en -muis als u een beeldscherm gebruikt

![Connectoren op het frontpaneel](./front-panel-connectors.jpg)
*Connectoren op het frontpaneel*

### Stap 2: NMEA 2000-aansluiting (optioneel)

Als u de HALPI2 rechtstreeks op een boot installeert of een NMEA 2000-opstelling op uw bureau hebt, kunt u hem nu al op het NMEA 2000-netwerk aansluiten.

Een [NMEA 2000-netwerk](https://docs.hatlabs.fi/nmea2000/) bestaat uit een backbonekabel waarop alle apparaten via T-stukken en aftakkabels worden aangesloten. Plaats een T-stuk in de backbone van het NMEA 2000-netwerk. Sluit de NMEA 2000-microconnector van de HALPI2 met een NMEA 2000-aftakkabel aan op het T-stuk.

### Stap 3: voedingsaansluiting

!!! tip "Opmerking over voeding via NMEA 2000"
    De HALPI2 kan ook via de NMEA 2000-bus worden gevoed. Zie [Voedingsaansluiting via de NMEA 2000-bus](#voedingsaansluiting-via-de-nmea-2000-bus) in het gedeelte over de vaste installatie hieronder.

Voor de opstelling op het bureau gebruiken we de meegeleverde E7T-voedingskabel. Sluit de aders van de voedingskabel als volgt aan op de female DC-plug:

- **Rode ader = plus (+)**
- **Zwarte ader = min (−)**

![E7T naar DC-plug](./e7t-barrel.jpg)
*Een voorbeeld van de bedrading van E7T naar DC-plug*

Sluit een standaard 12 V- of 24 V-voedingsadapter aan op de DC-plug. Zorg dat de voedingsadapter minstens 1 A kan leveren om aan de eisen van de HALPI2 te voldoen.

!!! warning "Waarschuwing"
    Omdat er geen trekontlasting aanwezig is, mag de DC-plug met schroefklemmen alleen voor tijdelijke opstellingen worden gebruikt. Per ongeluk aan de kabel trekken kan de aders losmaken en blootleggen.

## Eerste start

De HALPI2 wordt geleverd met [HaLOS](https://docs.halos.fi), een containergebaseerde Linux-distributie met een webinterface, ontworpen voor maritieme en industriële toepassingen. Geeft u de voorkeur aan een ander besturingssysteem, zoals OpenPlotter of Raspberry Pi OS, raadpleeg dan de [softwarehandleiding](../user-guide/software.md).

!!! info "HaLOS-documentatie"
    Deze handleiding behandelt de HALPI2-hardware en het voor het eerst inschakelen. Alles over het besturingssysteem — de instellingen bij de eerste start, netwerken, apps, certificaten en dagelijks gebruik — staat in de **[HaLOS-documentatie](https://docs.halos.fi)**. Houd die bij de hand terwijl u de onderstaande stappen doorloopt.

**Schakel de HALPI2 in** door de voedingsadapter aan te sluiten, als u dat nog niet hebt gedaan. Na enkele seconden
loopt de ledbalk vol met rode lichtjes, wat aangeeft dat de supercondensatoren worden opgeladen. De leds worden geel zodra het systeem opstart, en ten slotte groen wanneer het besturingssysteem draait en de HALPI-daemon verbinding heeft met de controller.

Als er een beeldscherm is aangesloten, ziet u het opstartscherm van Raspberry Pi OS en verschijnt ten slotte een grafische werkomgeving.

!!! tip "Tip"
    De patronen van de status-leds zijn beschreven in de [bedieningshandleiding](../user-guide/operation.md).

### De HALPI2 gebruiken zonder beeldscherm

Als er geen beeldscherm is aangesloten, kunt u de HALPI2 benaderen via het wifi-accesspoint of via een ethernetverbinding. HaLOS biedt een webinterface — extra software is niet nodig[^ssh].

[^ssh]: SSH is ook beschikbaar op HaLOS-images zonder beeldscherm (standaard ingeschakeld). Schakel SSH op de desktopvarianten in via `raspi-config`. Standaardinloggegevens: gebruikersnaam `pi`, wachtwoord `halos`.

Wacht eerst tot de leds groen worden; dat betekent dat het systeem volledig is opgestart. Volg daarna deze stappen:

**Optie 1 — verbinden via het wifi-accesspoint:** HaLOS maakt een wifi-accesspoint met de naam `Halos-XXXX` (uniek per apparaat) en het wachtwoord `halos1234`. Verbind uw computer met dit netwerk.

Het accesspoint heeft zelf geen internetverbinding, dus de volgende stap is de HALPI2 te verbinden met een wifi-netwerk dat die wel heeft (nodig om bij de eerste start de containerapps te downloaden):

1. Open Cockpit op `https://halos.local:9090/` en log in (gebruikersnaam `pi`, wachtwoord `halos`).
2. Ga naar **Networking** en klik op **WiFi (wlan0)**.
3. Wacht tot de lijst met beschikbare netwerken verschijnt en klik op uw netwerk.
4. Voer het wachtwoord in en klik op **Add**.

De HALPI2 houdt het accesspoint `Halos-XXXX` actief terwijl hij verbinding maakt met uw netwerk, dus uw computer kan de verbinding met het accesspoint even verliezen en daarna vanzelf opnieuw verbinding maken.

**Optie 2 — verbinden via bekabeld ethernet:** Als u de HALPI2 via ethernet op uw netwerk hebt aangesloten, krijgt hij automatisch een IP-adres via DHCP.

Open na het verbinden een browser en ga naar:

- **Dashboard:** `https://halos.local/` — het centrale Homarr-dashboard met links naar alle geïnstalleerde applicaties
- **Systeembeheer:** `https://halos.local:9090/` — Cockpit voor systeembeheer, updates en containerapps

!!! note "Waarschuwing over het SSL-certificaat"
    De eerste keer dat u het dashboard of Cockpit opent, toont uw browser de waarschuwing “Not secure”. HaLOS ondertekent zijn webdiensten met een certificaatautoriteit (CA) die het apparaat zelf aanmaakt, en uw browser vertrouwt die CA nog niet. Accepteer de waarschuwing om voorlopig verder te gaan.

    Wilt u de waarschuwing definitief kwijt, installeer dan de CA van het apparaat eenmalig op uw computer — daarna valideert elke HaLOS-dienst probleemloos op elke poort. Open `https://halos.local/ca/` voor een begeleide installatie per platform, of zie [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) in de HaLOS-documentatie.

!!! info "Internetverbinding vereist bij de eerste start"
    Cockpit is meteen beschikbaar, maar het centrale dashboard en de andere containergebaseerde applicaties hebben bij de eerste start een internetverbinding nodig om hun containerimages te downloaden. Sluit de HALPI2 via ethernet aan op het internet of stel wifi in via Cockpit.

### Configuratie bij de eerste start

!!! warning "Waarschuwing"
    HaLOS wordt geleverd met standaardwachtwoorden die bij de eerste start **moeten** worden gewijzigd om ongeautoriseerde toegang tot uw apparaat te voorkomen.

HaLOS heeft twee sets inloggegevens:

| Type toegang | Gebruikersnaam | Standaardwachtwoord | Gebruikt voor |
|:------------|:---------|:-----------------|:---------|
| SSO (webapps) | `admin` | `halos` | Dashboard, Signal K, Grafana en andere webapplicaties |
| Systeem (SSH/Cockpit) | `pi` | `halos` | SSH-toegang, systeembeheer via Cockpit |

#### Wachtwoorden wijzigen

- **SSO-wachtwoord:** wijzig dit via Authelia (bereikbaar vanaf het dashboard)
- **Systeemwachtwoord:** wijzig dit via Cockpit (`https://halos.local:9090/`) bij de instellingen van het gebruikersaccount, of via SSH met `passwd`

Uitgebreide instructies voor de eerste start vindt u in de [HaLOS Getting Started-handleiding](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Gebruikt u OpenPlotter of Raspberry Pi OS?"
    Als u een ander besturingssysteem hebt geflasht, raadpleeg dan de [softwarehandleiding](../user-guide/software.md#eerste-systeemconfiguratie) voor configuratie-instructies die specifiek zijn voor dat besturingssysteem.

### De NMEA 2000-verbinding controleren (optioneel)

De NMEA 2000-verbinding controleert u het eenvoudigst via de status van de Signal K-server. In de HaLOS Marine-imagevarianten is Signal K vooraf geïnstalleerd en bereikbaar vanaf het dashboard op `https://halos.local/`. Bij niet-maritieme HaLOS-images kunt u Signal K installeren via de Container Apps-store in Cockpit.

Open de webinterface van Signal K en bekijk de activiteit van de verbinding `can0`: er zou verkeer binnen moeten komen.

![Verbindingsactiviteit van de Signal K-server](./sk-n2k-deltas.jpg)

## Het apparaat afsluiten

De HALPI2 is ontworpen om automatisch af te sluiten wanneer de voeding wordt losgekoppeld. Wilt u het apparaat afsluiten, schakel dan simpelweg de spanning uit, met een schakelaar op het elektrisch paneel of door de voedingsconnector los te nemen. Het systeem start dan automatisch een gecontroleerde afsluitprocedure, zodat alle applicaties netjes worden gesloten en het bestandssysteem veilig wordt ontkoppeld.

Sluit u het systeem af via de grafische werkomgeving of met opdrachtregelprogramma's (zoals de opdracht `shutdown`), dan start het apparaat na ongeveer 5 seconden automatisch opnieuw op. Dat komt doordat het energiebeheer vaststelt dat er nog externe voeding aanwezig is.

Tijdens het afsluiten kunt u de systeemstatus volgen aan de leds op het frontpaneel. Zodra de spanning wegvalt, dimmen de groene leds om een stroomuitval aan te geven. Na 5 seconden worden de leds violet; dat is een duidelijk teken dat het apparaat bezig is met afsluiten. Zodra het afsluiten voltooid is, gaan alle leds uit.

Onder normale omstandigheden duurt het afsluiten meestal maar enkele seconden. Soms hebben bepaalde diensten echter meer tijd nodig om netjes te stoppen. In dat geval kan het apparaat de supercondensatoren bijna volledig leegtrekken voordat het afsluit. Deze langere afsluittijd is normaal en duidt niet op een storing in het systeem.

## Problemen oplossen bij de eerste ingebruikname

### Veelvoorkomende en minder gebruikelijke problemen:

❌ **Geen voeding of leds:**

- Controleer de voedingsaansluitingen en de polariteit
- Controleer de toestand van de zekering
- Zorg dat de spanning binnen het bereik 11–32 V ligt

❌ **Wifi-accesspoint niet zichtbaar:**

- Zorg dat de antenne goed is aangesloten
- Probeer verbinding te maken met een ander apparaat
- Controleer of de HALPI2 volledig is opgestart (de leds moeten groen zijn)
- Probeer eerst verbinding te maken via ethernet

❌ **Geen toegang tot het apparaat via `halos.local`:**

- Gebruik in plaats daarvan het toegewezen IP-adres (kijk in de DHCP-clientlijst van uw router)

❌ **Beeldscherm aangesloten, maar het toont niets:**

- Zorg dat de HDMI-kabel goed vastzit
- Zorg dat het beeldscherm aanstaat en op de juiste ingang is ingesteld
- Probeer een andere HDMI-kabel of een andere poort op het beeldscherm
- Controleer of de HALPI2 aanstaat (de leds moeten geel of groen zijn)
- Knipperen de leds in een regenboogpatroon, dan zit de Compute Module 5 niet goed op zijn plaats. Dit kan door transportschade komen. Volg de instructies in de [gebruikershandleiding](../user-guide/operation.md) om de CM5 opnieuw te plaatsen, of neem contact op met de ondersteuning.

❌ **Het aangesloten beeldscherm toont een foutmelding over ‘nvme’:**

- Dit betekent dat de NVMe SSD niet wordt gedetecteerd of niet goed is geïnitialiseerd. Dit kan door transportschade komen. Volg de instructies in de [gebruikershandleiding](../user-guide/operation.md) om de NVMe SSD opnieuw te plaatsen, of neem contact op met de ondersteuning.

### Hulp krijgen:

- **Documentatie:** raadpleeg de betreffende hoofdstukken voor uitgebreide probleemoplossing
- **Community:** neem deel aan de communityforums van Hat Labs
- **Support:** neem bij hardwareproblemen contact op met de technische ondersteuning

---

## Vaste installatie

Zodra u op uw bureau hebt vastgesteld dat alles werkt, volgt u deze stappen voor de vaste montage en bedrading.

### Uw installatie plannen

!!! tip "Handige tip"
    Maak foto's van de bestaande bedrading voordat u iets wijzigt — dat helpt later bij het oplossen van problemen.

Neem de tijd om uw installatie te plannen. Denk aan:

- **Montageplaats** — bereikbaarheid, bescherming, ventilatie
- **Kabelroute** — zo kort mogelijk, beschermd tegen beschadiging
- **Voedingsbron** — een eigen groep of een gedeelde, en de eisen aan de zekering
- **Netwerkintegratie** — NMEA 2000, ethernet, wifi-dekking
- **Omgevingsfactoren** — temperatuur, vocht, trillingen

#### Benodigd gereedschap en materiaal

**Gereedschap:**

- Boormachine met boren
- Schroevendraaierset (PH2 kruiskop, grote platte kop)
- Striptang en krimptang voor de voedingsaansluitingen
- Multimeter om te meten
- Heteluchtpistool of aansteker (voor krimpkous)

**Materiaal (niet meegeleverd):**

- Montageschroeven (4 mm of M4, afhankelijk van de montageondergrond)
- Geschikte zekeringen (3–5 A) of installatieautomaten met dezelfde waarde in het elektrisch paneel
- Kabel van maritieme kwaliteit (1,5 mm² of 16 AWG voor de voeding, als de meegeleverde kabel te kort is)
- Krimpkous en kabelschoenen
- Kabelbinders en bevestigingsclips

### Montage

#### Keuze van de plaats

Kies een montageplaats die het volgende biedt:

!!! tip "Optimale montageomstandigheden"
    - **Temperatuurbereik:** omgevingstemperatuur −20 °C … +60 °C
    - **Ventilatie:** voldoende vrije ruimte rond de behuizing
    - **Bescherming:** uit de buurt van rechtstreeks opspattend water en mechanische beschadiging
    - **Toegang:** goede bereikbaarheid van de connectoren en de status-leds
    - **Draagkracht:** stevige montageondergrond die 2 kg plus kabels kan dragen
    - **Ruimte:** houd minstens 100 mm vrije ruimte vóór de connectoren op het paneel voor het kabelbeheer.

Hoewel deze handleiding zich richt op vaste installaties, volstaat het in de praktijk vaak om het apparaat op een plank of tafelblad te zetten, mits het stabiel staat en beschermd is tegen vocht en stoten.

#### Richtlijnen per omgeving

**Maritieme installaties:**

- Monteer het apparaat boven het verwachte niveau van het bilgewater
- Vermijd plaatsen met opspattend of stilstaand water
- Houd rekening met de bewegingen en trillingen van de boot en zet alle verbindingen goed vast
- Gebruik corrosiebestendig bevestigingsmateriaal

**Installaties in voertuigen:**

- Bescherm het apparaat tegen motorwarmte en trillingen
- Zorg voor voldoende ventilatie in gesloten ruimten
- Houd rekening met de bereikbaarheid voor onderhoud
- Gebruik een trillingsbestendige bevestiging

**Industriële installaties:**

- Bescherm het apparaat tegen proceschemicaliën en extreme temperaturen
- Houd rekening met bronnen van elektromagnetische storing
- Zorg voor conformiteit met de plaatselijke elektrotechnische voorschriften
- Plan de bereikbaarheid voor regulier onderhoud

#### Montagerichting

!!! info "Aanbevolen richting"
    **Voorkeur:** connectoren naar beneden gericht

    - Beperkt het risico op binnendringend water
    - Maakt het kabelbeheer eenvoudiger
    - Betere bereikbaarheid voor onderhoud

    **Aanvaardbaar:** connectoren zijwaarts gericht

    - Zorg voor voldoende afwatering
    - Gebruik afdichtingen bij de kabeldoorvoeren

    **Vermijden:** connectoren naar boven gericht

    - Vergroot het risico op binnendringend water
    - Bemoeilijkt het kabelbeheer

#### Montagestappen

##### Stap 0: de boormal downloaden en afdrukken

Download de [HALPI2-boormal](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) en druk hem af op 100% schaal. Met deze mal markeert u de bevestigingsgaten nauwkeurig. Hebt u geen printer, gebruik dan de maten uit de mal om de gaten met de hand af te tekenen, of gebruik de behuizing zelf om de gaten rechtstreeks op de montageondergrond te markeren.

[![Boormal](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Stap 1: de montageondergrond voorbereiden

1. **Maak de montageondergrond schoon**
2. **Teken de bevestigingsgaten af** met de afgedrukte mal
3. **Pas de behuizing proef** vóór de montage
4. **Boor de gaten voor de montageschroeven voor**

##### Stap 2: de HALPI2 monteren

1. **Plaats de behuizing** met de connectoren in de gewenste richting
2. **Draai de montageschroeven vast** — stevig, maar niet te vast

### Vaste voedingsinstallatie

#### Keuze van de voedingsbron

**Optie 1: een eigen voedingsconnector**

- Het betrouwbaarst en het flexibelst
- Ondersteunt het volledige vermogen
- Eenvoudiger onderhoud en probleemoplossing

**Optie 2: voeding via de NMEA 2000-bus**

- Vereenvoudigt de bedrading in maritieme installaties
- Beperkt tot een stroomafname van 0,9 A
- Vraagt extra aandacht voor de spanningsval

#### Instelling van de stroombegrenzing

De HALPI2 heeft een ingebouwde stroombegrenzer aan de ingang die het eerste opladen van de supercondensatoren regelt en de installatie beschermt tegen overstroom. De stroombegrenzing kan op 0,9 A of op 2,5 A worden ingesteld, afhankelijk van uw voedingsbron en uw toepassing. De standaardinstelling van 0,9 A voldoet voor de meeste toepassingen.

Wilt u sneller opstarten of moet u randapparatuur met een hoge stroomafname voeden, dan kunt u overschakelen naar de instelling van 2,5 A. Volg de stappen in de [gebruikershandleiding](../user-guide/operation.md) om de stroombegrenzing te wijzigen.

#### Aparte voedingsaansluiting

##### De kabel voorbereiden

1. **Leg de voedingskabel** van de HALPI2 naar de voedingsbron
2. **Houd servicelussen aan** aan beide uiteinden
3. **Bescherm de kabel** tegen schuren en beschadiging
4. **Kort de kabel af** en houd voldoende werkruimte over

##### Aansluiting op de voedingsbron

1. **Zorg voor kabelbeveiliging** met een installatieautomaat van 3–5 A of een kabelzekering
2. **Strip de aders** over de juiste lengte
3. **Monteer de kabelschoenen** met de juiste krimptechniek
4. **Sluit aan op de voedingsbron:**
    - **Rode ader:** plusklem (+)
    - **Zwarte ader:** minklem (−)
5. **Controleer de polariteit** met de multimeter voordat u de spanning inschakelt

##### Aansluiting op de HALPI2

De E7T-connector is voorbedraad en hoeft ter plaatse niet te worden afgemonteerd. Steek hem gewoon in de voedingsaansluiting van de HALPI2.

#### Voedingsaansluiting via de NMEA 2000-bus

!!! info "Voorwaarden"
    - De schakelaar van de stroombegrenzer **moet** op 0,9 A staan
    - Het NMEA 2000-netwerk moet voldoende voedingscapaciteit hebben
    - De aftakkabel moet dicht bij het voedingspunt zitten om de spanningsval te beperken

##### Benodigde onderdelen

- NMEA 2000-aftakkabel (niet meegeleverd)
- T-stuk voor opname in de backbone (niet meegeleverd)

##### Installatiestappen

1. **Schakel** alle NMEA 2000-apparaten **uit**
2. **Open de behuizing van de HALPI2** (zie de [gebruikershandleiding](../user-guide/operation.md) voor instructies)
3. **Zoek de voedingsconnector op het carrierboard**
4. **Neem het aanwezige klemmenblok los**
5. **Sluit het interne NMEA 2000-voedingsklemmenblok** aan op de voedingsconnector van het carrierboard
6. **Controleer of de stroombegrenzing** op 0,9 A staat
7. **Sluit aan op de backbone** met een geschikte aftakkabel en een T-stuk
8. **Test de installatie** voordat u de behuizing sluit
9. **Zet de behuizing weer in elkaar**

![Voedingsbedrading via NMEA 2000](./n2k-power-conx.jpg)
*Om de HALPI2 via NMEA 2000 te voeden, neemt u klemmenblok 1 los en vervangt u het door klemmenblok 2.*

### Netwerk- en dataverbindingen

#### NMEA 2000-dataverbinding

Ook met een aparte voedingsaansluiting wilt u misschien NMEA 2000-data ontvangen:

1. **Plaats een T-stuk** in de NMEA 2000-backbone
2. **Sluit de aftakkabel aan** tussen het T-stuk en de HALPI2
3. **Controleer of het NMEA 2000-netwerk correct is afgesloten**
4. **Test de verbinding** na de installatie

#### Ethernetaansluiting

Voor een netwerkverbinding:

1. **Gebruik kabel van maritieme kwaliteit** of kabel die geschikt is voor de omgeving
2. **Monteer kabelwartels of doorvoertules** als u door schotten gaat
3. **Houd servicelussen aan** aan beide uiteinden
4. **Test de verbinding** voordat u alles definitief monteert

#### Antenne voor wifi en Bluetooth

1. **Monteer de antenne** op de RP-SMA-connector
2. **Richt hem voor een optimale dekking** — uit de buurt van metalen obstakels. In metalen kasten is mogelijk een RP-SMA-verlengkabel male-female nodig.
3. **Meet de signaalsterkte** op de definitieve plaats

### Installatieproblemen oplossen

#### Voedingsproblemen

❌ **Geen indicatie van voeding:**

- Controleer de toestand en de waarde van de zekering
- Controleer de spanning van de voedingsbron (11–32 V)
- Controleer of de polariteit klopt
- Voer een doorbelmeting uit op de voedingskabels

❌ **Wegvallende voeding:**

- Controleer of alle verbindingen goed vastzitten
- Controleer de klemmen op corrosie
- Controleer of de aderdoorsnede past bij de stroom

#### Netwerkverbinding

❌ **Geen NMEA 2000-communicatie:**

- Controleer de afsluiting van het netwerk (120 Ω aan beide uiteinden)
- Controleer de montage van het T-stuk
- Controleer of de aftakkabel onbeschadigd is
- Test met een apparaat waarvan bekend is dat het werkt

❌ **Geen ethernetverbinding:**

- Test de kabel met een kabeltester
- Controleer de configuratie van de switch of de router
- Controleer op conflicten tussen IP-adressen
- Controleer de kabelklasse (minimaal Cat5e)

#### Omgevingsproblemen

❌ **Binnendringend vocht:**

- Controleer de staat van alle afdichtingen
- Controleer de richting van de connectoren
- Controleer de kabeldoorvoeren
- Overweeg extra bescherming

❌ **Oververhitting:**

- Plaats het apparaat verder van warmtebronnen
- Controleer of de luchtstroom rond de behuizing nergens wordt belemmerd

### Veiligheid en conformiteit

#### Elektrische veiligheid

- **Gebruik geschikte zekeringen** als beveiliging tegen overstroom
- **Zorg voor een correcte aarding** volgens de plaatselijke voorschriften
- **Bescherm tegen kortsluiting** door de kabels goed te leggen

#### Maritieme installaties

- **Volg de plaatselijke normen of de ABYC-normen** voor elektrische installaties
- **Gebruik overal componenten van maritieme kwaliteit**

#### Industriële installaties

- **Houd u aan de plaatselijke elektrotechnische voorschriften**
- **Zorg voor een goede bescherming tegen EMI/RFI**
- **Documenteer de installatie** volgens de eisen van de locatie

## Volgende stappen

Zodra uw HALPI2 draait:

1. **Verken de [gebruikershandleiding](../user-guide/operation.md)** voor uitgebreide bedieningsinstructies
2. **Bekijk de veelvoorkomende toepassingen** voor een op uw toepassing afgestemde inrichting
3. **Raadpleeg de technische referentie** voor geavanceerde configuratiemogelijkheden
4. **Sluit u aan bij de community** voor tips, trucs en ondersteuning

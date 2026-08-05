---
translated_from: e4d4a4c5108676be9c19bdd2a82a321b24b14191
---

# Inleiding

De HALPI2 is een kant-en-klare boordcomputer op basis van de Raspberry Pi Compute Module 5 (CM5). Hij biedt een uitgebreid pakket functies dat uitstekend past bij maritieme, automotive en veel industriële toepassingen.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Link naar de webshop"
    Koop de HALPI2 in de [webshop van Hat Labs](https://shop.hatlabs.fi/products/halpi2-computer).

## Wat is de HALPI2?

De HALPI2 vertegenwoordigt de nieuwste stap in robuuste embedded computers en combineert de rekenkracht en het ecosysteem van Raspberry Pi met specifieke voorzieningen voor veeleisende omgevingen. Anders dan gewone singleboardcomputers is de HALPI2 vanaf de grond ontworpen voor 24/7-gebruik onder zware omstandigheden, waar betrouwbaarheid alles is.

Het systeem combineert een Raspberry Pi Compute Module 5 met een speciaal ontworpen carrierboard, ondergebracht in een waterdichte aluminium behuizing die tegelijk als koellichaam dient. Dit ontwerp levert de rekenkracht die moderne toepassingen nodig hebben, met behoud van de robuustheid die maritiem en industrieel gebruik vraagt.

## Belangrijkste kenmerken en mogelijkheden

### Kenmerken van de behuizing

- **Waterdichte aluminium behuizing (IP65)**, afmetingen 200 × 130 × 60 mm
- **Standaardconnectoren** voor voeding, NMEA 2000, gigabit-ethernet, HDMI, 2× USB 3.0 en de WiFi/Bluetooth-antenne
- **Flexibele aansluitmogelijkheden**, met keuze uit 3× PG7-kabelwartel of waterdichte SP13-connectoren
- **Ondersteuning voor externe antennes** via uitsparingen voor 2 extra SMA-connectoren
- **Ontwerp voor wandmontage**, met connectoren op een plaats die installeren eenvoudig maakt

![Connectorindeling van de HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Hardwarekenmerken

- **Breed ingangsspanningsbereik** van 10 tot 32 V DC, met bescherming tot 100 V DC
- **Intelligente stroombegrenzing**: maximale ingangsstroom 0,9 of 2,5 A, door de gebruiker in te stellen
- **Twee voedingsopties**: rechtstreekse aansluiting op 12 V/24 V of 12 V-busvoeding via NMEA 2000
- **Supercondensator als buffer** voor storingsongevoeligheid en gecontroleerd afsluiten bij spanningsuitval
- **Geavanceerd energiebeheer** met automatische detectie van spanningsuitval
- **Passieve koeling**, waarbij de CM5 rechtstreeks contact maakt met de behuizing
- **Snelle opslag** via een standaard M.2-interface voor NVMe SSD
- **Uitbreidingsmogelijkheden** via de standaard 40-pins GPIO-pinheader van de Raspberry Pi
- **Ruime I/O-mogelijkheden**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, gigabit-ethernet
- **Maritieme interfaces**: CAN FD (NMEA 2000) en RS-485 (NMEA 0183)
- **Realtimeklok** met backupbatterij voor een nauwkeurige tijdsaanduiding
- **Visuele statusweergave** via vijf RGB-leds
- **Interactie met de gebruiker** via configureerbare knoppenheaders

![Binnenaanzicht van de HALPI2](./halpi2-interior.jpg)
*Binnenaanzicht van de HALPI2 met het carrierboard en de verschillende connectoren.*

### Softwarekenmerken

- **Voorgeconfigureerde systeemimages** die direct in gebruik kunnen worden genomen: [HaLOS](https://docs.halos.fi) (standaard), OpenPlotter, Raspberry Pi OS en Raspberry Pi OS Lite
- **Uitgebreide bewaking** van spanning, stroom en temperatuur
- **Transparante firmware-updates** via de I2C-interface

## Toepassingsgebieden

### Maritieme toepassingen

- **Navigatiesystemen** met kaartplotters en gps-integratie
- **Dataregistratie** van motorgegevens, omgevingssensoren en de prestaties van het vaartuig
- **Signal K-servers** voor eenduidig beheer van scheepsgegevens
- **Algemene boordcomputertaken**, zoals internettoegang en communicatie
- **Foutopsporing in NMEA 2000-netwerken** voor een betrouwbaarder systeem

### Industriële toepassingen

- **Procesbewaking** en besturingssystemen
- **Omgevingsmetingen** en data-acquisitie
- **Meetstations voor bewaking op afstand**
- **Automatisering en besturing** van apparatuur
- **Systemen voor voorspellend onderhoud**

### Automotive-toepassingen

- **Systemen voor wagenparkbeheer**
- **Telematica** en voertuigvolgsystemen
- **Infotainmentsystemen** in voertuigen
- **Diagnose- en bewakingsplatformen**

## Inhoud van de verpakking

Uw HALPI2-pakket bevat:

- **HALPI2-unit** met vooraf geïnstalleerde Compute Module 5 en NVMe SSD (tenzij zonder besteld)
- **Voedingskabel** met E7T-connector (compatibel met Amphenol LTW Ceres Mini), lengte 2 m
- **E7T-kabelstekker** voor eigen installaties
- **Paar DC-pluggen (barrel connectors)** (5,5 × 2,1 mm) voor gebruik met standaardvoedingen van 12 V/24 V
- **Raspberry Pi-antenne** voor wifi- en bluetoothverbindingen
- **3 PG7-kabelwartels** voor extra interfaces
- **Snelstartgids en garantiedocumentatie** om op weg te helpen

![Inhoud van het HALPI2-accessoirezakje](./goodie-bag-contents.jpg)

Los verkrijgbare accessoires:

- **NMEA 2000-aftakkabel** voor toepassingen met busvoeding
- **Diverse connectorsets** voor eigen installaties

## Hoe u deze documentatie gebruikt

Deze documentatie is zo opgezet dat zij zowel eindgebruikers bedient die praktische aanwijzingen zoeken, als professionele ontwikkelaars die gedetailleerde technische informatie nodig hebben.

### Voor eindgebruikers

- Begin met de handleiding **Aan de slag** voor installatie en ingebruikname
- Bekijk **Veelvoorkomende toepassingen** voor aanwijzingen per toepassing
- Raadpleeg **Probleemoplossing** wanneer er iets misgaat

### Voor ontwikkelaars

- Neem de **Technische referentie** door voor gedetailleerde specificaties
- Bestudeer de hoofdstukken over **Softwareontwikkeling** voor eigen toepassingen
- Bekijk de **Ontwerpbestanden** voor het plannen van integratie
- Raadpleeg **Geavanceerde configuratie** voor het optimaliseren van prestaties

### Tips voor het gebruik van de documentatie

- 💡 **Snelle tips** geven kortere wegen voor veelvoorkomende taken
- ⚠️ Meldingen met **Waarschuwing** en **Let op** wijzen op belangrijke veiligheidsinformatie
- 🔧 Onderdelen met **Technische details** gaan dieper in op de uitvoering
- 📖 **Kruisverwijzingen** verbinden verwante onderwerpen door de hele documentatie heen

Of u nu uw eerste maritieme computer installeert of een eigen industriële oplossing ontwikkelt, deze documentatie leidt u door elke stap van het werken met de HALPI2.

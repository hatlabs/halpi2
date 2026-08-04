# Introduktion

HALPI2 är en färdig båtdator baserad på Raspberry Pi Compute Module 5 (CM5). Den har ett brett funktionsutbud som passar väl för marina tillämpningar, fordonstillämpningar och många industriella användningsområden.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Länk till butiken"
    Köp HALPI2 i [Hat Labs webbutik](https://shop.hatlabs.fi/products/halpi2-computer).

## Vad är HALPI2?

HALPI2 är den senaste utvecklingen inom tålig inbyggd datorteknik: den förenar Raspberry Pi:s prestanda och ekosystem med funktioner för krävande miljöer. Till skillnad från vanliga enkortsdatorer är HALPI2 konstruerad från grunden för kontinuerlig drift under svåra förhållanden, där tillförlitlighet är avgörande.

Systemet kombinerar en Raspberry Pi Compute Module 5 med ett specialkonstruerat bärkort, allt inbyggt i en vattentät aluminiumkapsling som samtidigt fungerar som kylfläns. Konstruktionen ger den beräkningskraft moderna tillämpningar kräver och behåller samtidigt den tålighet som marin och industriell användning förutsätter.

## Viktigaste egenskaper

### Kapslingens egenskaper

- **Vattentät aluminiumkapsling (IP65)**, mått 200 × 130 × 60 mm
- **Standardanslutningar** för strömförsörjning, NMEA 2000, gigabit-ethernet, HDMI, 2× USB 3.0 och WiFi-/Bluetooth-antenn
- **Flexibla anslutningsalternativ**: 3× PG7-kabelgenomföring eller vattentäta SP13-kontakter
- **Stöd för externa antenner**: uttag för 2 extra SMA-kontakter
- **Konstruerad för väggmontage**, med anslutningarna placerade för enkel installation

![HALPI2:s anslutningar](./user-guide/front-panel-connectors-all.jpg)

### Hårdvarans egenskaper

- **Brett inspänningsområde** från 10 till 32 V DC, med skydd upp till 100 V DC
- **Intelligent strömbegränsning**: maximal inström 0,9 eller 2,5 A, valbart av användaren
- **Två sätt att mata ström**: direkt anslutning med 12 V/24 V, eller matning från NMEA 2000-bussen med 12 V
- **Backup med superkondensatorer** för störningstålighet och kontrollerad avstängning vid spänningsbortfall
- **Avancerad strömhantering** med automatisk detektering av spänningsbortfall
- **Passiv kylning**: CM5 har direkt kontakt med kapslingen
- **Snabb lagring** via ett vanligt M.2 NVMe SSD-gränssnitt
- **Utbyggbarhet** via Raspberry Pi:s 40-poliga GPIO-stiftlist
- **Rikligt med in- och utgångar**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, gigabit-ethernet
- **Gränssnitt för marint bruk**: CAN FD (NMEA 2000) och RS-485 (NMEA 0183)
- **Realtidsklocka** med backupbatteri för korrekt tid
- **Synlig statusindikering** via fem RGB-lysdioder
- **Användarinteraktion** via konfigurerbara knappanslutningar

![Vy inuti HALPI2](./halpi2-interior.jpg)
*Vy inuti HALPI2 med bärkortet och de olika anslutningarna.*

### Programvarans egenskaper

- **Förkonfigurerade systemavbilder** klara att använda direkt: [HaLOS](https://docs.halos.fi) (standard), OpenPlotter, Raspberry Pi OS och Raspberry Pi OS Lite
- **Omfattande övervakning** av spänning, ström och temperatur
- **Diskreta firmwareuppdateringar** via I2C-gränssnittet

## Användningsområden

### Marina tillämpningar

- **Navigationssystem** med kartplotter och GPS-integration
- **Datalagring** av motorvärden, miljösensorer och fartygets prestanda
- **Signal K-servrar** för enhetlig hantering av båtens data
- **Allmän dator ombord** för internetuppkoppling och kommunikation
- **Felsökning av NMEA 2000-nätverk** för högre systemtillförlitlighet

### Industriella tillämpningar

- **Processövervakning** och styrsystem
- **Miljömätning** och datainsamling
- **Stationer för fjärrövervakning**
- **Automation och styrning av utrustning**
- **System för förebyggande underhåll**

### Fordonstillämpningar

- **System för flotthantering**
- **Telematik** och fordonsspårning
- **Infotainmentsystem i fordon**
- **Plattformar för diagnostik och övervakning**

## Förpackningens innehåll

HALPI2-förpackningen innehåller:

- **HALPI2-enheten** med förinstallerad Compute Module 5 och NVMe SSD (om den inte beställts utan)
- **En strömkabel** med E7T-kontakt (kompatibel med Amphenol LTW Ceres Mini), längd 2 m
- **En E7T-kabelkontakt** för egna installationer
- **Ett par DC-hålkontakter** (5,5 × 2,1 mm) för vanliga nätaggregat på 12 V/24 V
- **En Raspberry Pi-antenn** för WiFi och Bluetooth
- **3 st PG7-kabelgenomföringar** för ytterligare gränssnitt
- **En snabbstartsguide och garantihandlingar**

![Innehållet i HALPI2:s tillbehörspåse](./goodie-bag-contents.jpg)

Tillbehör som säljs separat:

- **NMEA 2000-stickledning** för installationer med bussmatning
- **Olika kontaktsatser** för egna installationer

## Så använder du den här dokumentationen

Dokumentationen vänder sig både till slutanvändare som söker praktisk vägledning och till utvecklare som behöver detaljerad teknisk information.

### För slutanvändare

- Börja med guiden **Kom igång** för installation och driftsättning
- Läs om **vanliga användningsfall** för råd som passar din tillämpning
- Gå till **Felsökning** när problem uppstår

### För utvecklare

- Läs **Teknisk referens** för detaljerade specifikationer
- Studera avsnitten om **Programvaruutveckling** för egna tillämpningar
- Titta på **Konstruktionsfilerna** när du planerar en integration
- Se **Avancerad konfiguration** för prestandaoptimering

### Konventioner i dokumentationen

- 💡 **Tips**-rutor ger genvägar för vanliga uppgifter
- ⚠️ **Varning** och **Observera** lyfter fram viktig säkerhetsinformation
- 🔧 **Tekniska detaljer** går djupare in på hur något är genomfört
- 📖 **Korsreferenser** binder samman besläktade ämnen genom hela dokumentationen

Oavsett om du sätter upp din första båtdator eller utvecklar en egen industriell lösning tar den här dokumentationen dig genom varje steg.

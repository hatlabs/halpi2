---
translated_from: 9741366021074655d667fcf3a93a634f86f3519a
---

# Hardwarevejledning

## Adgang til kabinettet

HALPI2 har et pulverlakeret kabinet i trykstøbt aluminium med forborede huller til panelstik. Når der er behov for indvendige ændringer eller vedligeholdelse, får du adgang til kabinettet ved at følge fremgangsmåderne nedenfor.

### Sådan åbner du kabinettet

For at komme til de indvendige komponenter skal du først sikre dig, at enheden er helt slukket, og at strømkablerne er frakoblet. Låget er fastgjort med fire undersænkede M4x10-skruer med PH2-hoved. Brug en PH2-skruetrækker til at fjerne skruerne, og tag låget af.

### Samling igen

Før du samler kabinettet igen, skal du tage dig tid til at kontrollere, at alle indvendige forbindelser sidder fast og er korrekt monteret. Før kablerne omhyggeligt, så de ikke kommer i klemme eller får skarpe knæk.

Det er nemt at komme til at vende fladkablerne (FFC) forkert. Se pilene ved `Contacts` på silketrykket for at kontrollere, at orienteringen er rigtig.

Vær særligt opmærksom på kabinetlågets pakning, og se efter skader, snavs eller forskydninger, der kan forringe kabinettets tætning mod vejrliget.

Monter de fire M4x10-lågskruer igen med PH2-skruetrækkeren. Spænd dem ikke for hårdt.


## Panelstik

### Standardkonfiguration

HALPI2 leveres med en standardkonfiguration af stik, som passer til de fleste anvendelser. Standardopsætningen omfatter:

- **E7T-strømstik**
- **NMEA 2000-microstik**
- **Gigabit-ethernet RJ45**
- **HDMI-udgang**
- **2× USB 3.0 Type-A**
- **3× PG7-positioner til kabelforskruninger** (med blindpropper)
- **2× RP-SMA-antennepositioner** (med blindpropper)
- **Trykudligningsprop** til udligning af trykforskelle

![Frontpanelets stik og blindpropper](./front-panel-connectors-all.jpg)
*Frontpanelets stik og blindpropper. Stik markeret med grønt indgår i standardkonfigurationen. De gule positioner er blindpropper, der kan udskiftes med stik efter behov. Den røde position er trykudligningsproppen, som ikke må fjernes.*

### Alternative stikmuligheder

Hvis du har brug for andre stiktyper, kan du ændre panelkonfigurationen:

#### Fjernelse af stik

!!! warning "Vigtigt"
    Ændr kun stikkene, når enheden er slukket og frakoblet alle strømkilder.

    Plastgevind kan blive beskadiget, hvis de spændes for hårdt. Brug almindelige sekskanttoppe, men spænd kun med fingerkraft.

1. **Brug den rigtige topstørrelse:**
    - Store stik: 26 mm top
    - M6-nylonbolte: 10 mm top
    - RP-SMA-stik: 8 mm top
    - PG7-positioner: stor kærvskruetrækker, 17 mm top

2. **Fjern dem forsigtigt** – plastgevind kan blive beskadiget, hvis de spændes for hårdt

3. **Gem de afmonterede dele** til eventuel senere brug

#### Montering af nye stik

1. **Brug kun marinegodkendte stik** eller stik, der er godkendt til miljøet
2. **Sørg for korrekt tætning** – der kræves en bred flange på indersiden
3. **Spænd kun med fingerkraft** – spænd ikke plastgevindene for hårdt
4. **Prøvemonter** før den endelige installation

## Indvendig opbygning

- HALPI2's bærekort er computerens hovedkort, som huser Compute Module 5 (CM5) på undersiden og står for strømstyring, indikatorer og forbindelser til alle grænseflader.

### Bærekortets funktionsområder

Bærekortets vigtigste funktionsområder er vist på billedet nedenfor.

![Bærekortets opbygning, oversiden](./carrier-board-top-layout.jpg)
*Bærekortets opbygning på oversiden med de vigtigste funktionsområder.*

### Bærekortets stik

Funktionerne tilgås via en række stik på kortet, som er vist på billedet nedenfor.

![Bærekortets stik, oversiden](./carrier-board-top-conx.jpg)
*Bærekortets stik på oversiden.*

Nedenfor er en oversigt over stikkene på oversiden.

| Mærke | Beskrivelse |
|:------|:------------|
| **a1** | Strømstik (Phoenix MC-type, 3,81 mm benafstand) |
| **a2** | Strømbegrænsningskontakt for indgangsstrømmen (0,9 A eller 2,5 A) |
| **a3** | Jumper til strømstyring. Kortslut benene `3.3V off` for at tvinge 3,3 V-skinnen af. Kortslut benene `5V on` for at tvinge 5 V-skinnen til. **NB:** På kort med version 0.4.0 er stikkene **a3** og **c2** placeret anderledes. |
| **b1** | Ethernetport (RJ45) |
| **c1** | Controllerens USB-port. Bruges til at flashe RP2040-mikrocontrollerens firmware. |
| **c2** | Jumperstikliste til MCU USB BOOT. Kortslut benene for at sætte RP2040 i USB-boot-tilstand. |
| **c3** | Stikliste til fejlfinding på controlleren |
| **c4** | Umonteret GPIO-stikliste til controlleren |
| **c5** | Knapstiklister. Bruges til at tilslutte knapperne Power, Reset og User. |
| **c6** | Tænd/sluk-knap. Bruges til at tænde og slukke Compute Module 5. |
| **d1** | 40-benet GPIO-stikliste fra Raspberry Pi |
| **e1** | MIPI0-stik til kamera- eller displaygrænseflade |
| **e2** | MIPI1-stik til kamera- eller displaygrænseflade |
| **f1** | HDMI0-stik |
| **f2** | HDMI1-stik |
| **g1** | M.2 NVMe SSD-stik |
| **h1** | CAN FD-grænseflade (Phoenix MC-type, 3,81 mm benafstand) |
| **h2** | Jumper til CAN-terminering. Kortslut benene for at aktivere termineringen af CAN FD-bussen. |
| **i1** | RS-485-grænseflade (Phoenix MC-type, 3,81 mm benafstand) |
| **i2** | Jumper til automatisk/manuel aktivering af RS-485. |
| **i4** | Jumper til XRS-485 RX Enable. Kortslut benene for at aktivere modtagelse af RS-485-trafik. |
| **j1** | Compute Module USB Boot-stik. Bruges til at flashe firmwaren på Compute Module 5. |
| **j2** | Vælgerkontakt til boot-tilstand for Compute Module. Sæt den på `Normal` ved normal drift og på `Abnormal` ved USB-boot-tilstand. En advarsels-LED lyser, når kontakten står på `Abnormal`. |
| **m1** | USB3-stik 0. Forbundet direkte til CM5. |
| **m2** | USB3-stik 1-0. Forbundet til den indbyggede USB3-hub. |
| **m3** | USB3-stik 1-1. Forbundet til den indbyggede USB3-hub. |
| **m4** | USB3-stik 1-2. Forbundet til den indbyggede USB3-hub. |
| **n1** | CR2032-batteriholder til RTC'en (realtidsuret) |
| **q1** | Blæserstik til CM5. Blæseren kan bruges til at forbedre luftcirkulationen inde i kabinettet. Den er ikke nødvendig, når standardkabinettet anvendes. |

![Bærekortets stik, undersiden](./carrier-board-bottom-conx.jpg)
*Bærekortets stik på undersiden.*

Nedenfor er en oversigt over stikkene på undersiden.

| Mærke | Beskrivelse |
|:------|:------------|
| **p1** | Compute Module 5-stik. |
| **q1** | Blæserstik til CM5, alternativ placering. Denne stikliste kan bruges til at tilslutte en CPU-blæser over CM5-modulet, når der anvendes et specialkabinet. **NB:** Stikkene **q1** og **q2** er forbundet parallelt og må ikke bruges samtidig. |

Til sidst sidder stikket til WiFi- og Bluetooth-antennen på selve Compute Module 5. Det er vist på billedet nedenfor.

![WiFi-antennestik](./cm5-top-conx.jpg)
*U.FL-antennestik på Compute Module 5.*

| Mærke | Beskrivelse |
|:------|:------------|
| **r1** | U.FL-stik til WiFi- og Bluetooth-antennen. |

### Blinkenlights

Bærekortet har flere status-LED'er til overvågning af systemet.

![Bærekortets status-LED'er](./carrier-board-top-leds.jpg)
*Bærekortets status-LED'er og deres farver.*

Status-LED'erne giver oplysninger om systemets strøm- og aktivitetstilstand. Nedenfor er en oversigt over status-LED'erne.

| Mærke | Farve | Beskrivelse |
|-------|:-------|:------------|
| **1** | RGB   | Fem RGB-LED'er. Disse LED'er bruges til at vise systemets status og aktivitet på frontpanelet. |
| **2** | Rød   | Strøm-LED'er for 3,3 V- og 5 V-skinnerne. Disse LED'er viser forsyningsstatus for de respektive spændingsskinner. |
| **3** | Gul| Indikator for ethernethastighed. Lyser, når ethernetporten har forhandlet en forbindelse på 100/1000 Mbit/s. |
| **4** | Grøn | Indikator for ethernetaktivitet. Blinker, når der er netværkstrafik på ethernetporten. |
| **5** | Blå | Indikator for SSD-aktivitet. Blinker, når der læses eller skrives på M.2 NVMe SSD'en. |
| **6** | Rød | Statusindikator for strøm til Pi'en. Lyser, når systemet har strøm, men er lukket ned. |
| **7** | Grøn | Aktivitetsindikator for Pi'en. Blinker, når der er aktivitet på Raspberry Pi'en. |
| **8** | Ravgul | Advarsel om boot-tilstanden `Abnormal`. Lyser, når kontakten til USB-boot-tilstand står på `Abnormal`. Det betyder, at enheden er indstillet til at blive flashet via USB Boot-stikket og ikke starter normalt. |
| **9** | Grøn | CAN TX/RX-LED'er. Disse LED'er blinker, når der modtages (RX) eller sendes (TX) data på CAN-grænsefladen. |
| **10** | Grøn | RS-485 TX/RX-LED'er. Disse LED'er blinker, når der modtages (RX) eller sendes (TX) data på RS-485-grænsefladen. |

RGB-LED'ernes mønstre er beskrevet under [Systemdrift](./operation.md#status-led-indikatorer).

## Konfiguration af strømbegrænsning

Bærekortet har en strømbegrænsningskontakt, hvor du indstiller den maksimale strøm til de perifere enheder. Kontakten finder du som **a2** på billedet i afsnittet [Bærekortets stik](#brekortets-stik).

!!! info "Indstillinger for strømbegrænsning"
    **Indstillingen 0,9 A (standard):**

    - Obligatorisk ved busforsyning fra NMEA 2000
    - Egnet til almindelig drift

    **Indstillingen 2,5 A:**

    - Til perifere enheder med stort strømforbrug
    - Hurtigere opladning af superkondensatorerne
    - Kun ved dedikeret strømtilslutning

Sluk helt for HALPI2, og fjern kabinetlåget efter fremgangsmåden i afsnittet Adgang til kabinettet, før du ændrer strømbegrænsningen. Find strømbegrænsningskontakten på bærekortet, og sæt kontakten i den ønskede position (enten 0,9 A eller 2,5 A). Når indstillingen er ændret, samler du kabinettet igen og kontrollerer, at alle forbindelser stadig sidder fast.

## Brug af HAT'er

### HAT-kompatibilitet

HALPI2 understøtter almindelige Raspberry Pi-HAT'er via sin 40-benede GPIO-stikliste og er fuldt elektrisk og mekanisk kompatibel med Raspberry Pi-HAT-specifikationen. Bærekortet har samme GPIO-benforbindelser som en almindelig Raspberry Pi, så de fleste HAT'er, der er lavet til Raspberry Pi 4 og 5, virker uden ændringer. Kompatibiliteten gælder både officielle Raspberry Pi-HAT'er og udvidelseskort fra tredjepart, der følger HAT-standarden.

### Fysiske begrænsninger

HALPI2-kabinettet giver 45 mm frihøjde over bærekortet, hvilket er nok til op til to HAT'er oven på hinanden. Området til venstre for det markerede installationsområde til HAT'er er optaget af superkondensatorerne, hvilket begrænser pladsen til HAT'er, der rækker ud over standardmålene på 65 × 56 mm. Vær særligt opmærksom på HAT'er med stik i siden. Stik, der vender mod »syd« eller »øst«, giver normalt ingen problemer, mens stik mod »vest« kan støde ind i superkondensatorerne.

### Konflikter mellem GPIO-ben

Flere GPIO-ben bruges af HALPI2's indbyggede grænseflader og skal tages i betragtning, når du vælger kompatible HAT'er. Tabellen nedenfor viser de reserverede GPIO-ben og deres funktioner:

| GPIO-nummer | Funktion | Grænseflade | Bemærkninger |
|----------|----------|-----------|-------|
| GPIO 2 | I2C SDA | System-I2C | Kan deles; adressen 0x6d er reserveret |
| GPIO 3 | I2C SCL | System-I2C | Kan deles; adressen 0x6d er reserveret |
| GPIO 6 | SPI CS | CAN FD | Særskilt chip select til CAN-controlleren |
| GPIO 9 | SPI MISO | CAN FD | Delt SPI0-bus |
| GPIO 10 | SPI MOSI | CAN FD | Delt SPI0-bus |
| GPIO 11 | SPI SCK | CAN FD | Delt SPI0-bus |
| GPIO 12 | UART TX | RS-485 | UART4 send |
| GPIO 13 | UART RX | RS-485 | UART4 modtag |
| GPIO 24 | RS-485 EN | RS-485 | Aktiveringssignal (kun i manuel tilstand) |
| GPIO 26 | CAN INT | CAN FD | Afbrydelseslinje til CAN-controlleren |

### Deling af grænseflader og konflikter

I2C-bussen på GPIO 2 og 3 kan deles med enheder på en HAT, da I2C understøtter flere enheder på samme bus. HAT'er må dog ikke bruge I2C-adressen 0x6d, som er reserveret til HALPI2's systemcontroller. De fleste I2C-HAT'er virker uden problemer, men kontrollér de anvendte I2C-adresser før installationen.

SPI0-bussen, der bruges til CAN FD-grænsefladen, kan eventuelt deles med andre SPI-enheder, fordi HALPI2 bruger særskilte ben til chip select (GPIO 6) og afbrydelse (GPIO 26). HAT'er, der bruger SPI0 med standardbenene til chip select (GPIO 7 eller GPIO 8), kan sameksistere med CAN-grænsefladen, men de kan kræve yderligere konfiguration med device tree-overlays.

### Deaktivering af indbyggede grænseflader

Hvis en HAT kræver eneret til ben, der er optaget af HALPI2's indbyggede grænseflader, kan disse grænseflader deaktiveres med ændringer i hardwaren. CAN FD-grænsefladen kan frigøres helt ved at fjerne loddejumperen GPIO6-CAN.CS på bærekortets underside. Denne ændring afbryder forbindelsen mellem CAN-controlleren og SPI-bussen og frigør GPIO 6, 9, 10, 11 og 26 til brug for HAT'en.

RS-485-grænsefladen kan deaktiveres ved at fjerne jumperen RX Enable (i4) på bærekortet. Det forhindrer RS-485-transceiveren i at modtage data og frigør GPIO 12 og 13 til andre formål. Hvis der ikke er brug for manuel styring af sendeaktiveringen, kan GPIO 24 også bruges til andre formål ved at sætte jumperen til automatisk/manuel aktivering af RS-485 (i2) i automatisk tilstand.

### Installationsprocedure

Begynd installationen med at slukke systemet og frakoble alle strømkilder. Fjern kabinetlåget efter fremgangsmåden i afsnittet Adgang til kabinettet.

Bærekort fra version 0.5.0 og senere har formonterede M2.5-gevindindsatser i de fire monteringspositioner til HAT'er, hvilket gør installationen enklere. På tidligere v0.4.0-kort skal M2.5-møtrikkerne monteres manuelt. Ved montering af møtrikker skal bærekortet afmonteres midlertidigt. Det kan lade sig gøre uden at frakoble alle kabler.

Til mange almindelige HAT'er passer 15 mm afstandsbolte, men mål hunstiklistens højde på HAT'en for at sikre den rigtige frihøjde. Hanstiklistens sokkel er 2,5 mm høj, så læg dette til hunstiklistens højde for at finde den nødvendige længde på afstandsboltene.

Skru afstandsboltene i monteringshullerne, eller fastgør dem med møtrikker fra undersiden på v0.4.0-kort. Ret HAT'en ind efter den 40-benede GPIO-stikliste, og kontrollér, at alle ben sidder rigtigt, før du trykker stikket i bund med et jævnt tryk. HAT'en skal sidde parallelt med bærekortet uden synlig afstand ved GPIO-forbindelsen.

Fastgør HAT'en med M2.5-skruer eller flere afstandsbolte gennem HAT'ens monteringshuller og ned i afstandsboltene. Disse skruer følger ikke med HALPI2 og skal skaffes separat. Spænd skruerne netop så meget, at HAT'en sidder fast, uden at printet bøjer.

### Kabelføring

Hvis HAT'en har udvendige stik, der skal kunne nås uden for kabinettet, kan du overveje at montere passende panelstik i de ledige PG7-positioner til kabelforskruninger. På den måde bevarer kabinettet sin beskyttelse mod omgivelserne, samtidig med at du får nem adgang udefra.

### Afmonteringsprocedure

En HAT afmonteres i omvendt rækkefølge af installationen. Sluk systemet helt, og frakobl alle strømkilder, før du åbner kabinettet. Fjern M2.5-monteringsskruerne, og løft forsigtigt HAT'en lige op fra GPIO-stiklisten, så du undgår sidevejs kræfter, der kan bøje benene på stiklisten.

Hvis HAT'en sidder fast, skal du se efter oversete monteringsbeslag eller kabler, før du bruger mere kraft. Nogle HAT'er med stramtsiddende stik kan kræve en forsigtig vippende bevægelse, mens du trækker opad. Vip HAT'en i nord-syd-retningen; vipper du øst-vest, risikerer du at bøje benene på stiklisten, når stikket pludselig slipper.

### Softwarekonfiguration

Efter hardwareinstallationen kan HAT'en kræve softwarekonfiguration for at fungere korrekt. Mange HAT'er har device tree-overlays, som skal aktiveres i Raspberry Pi-konfigurationen. Redigér `/boot/firmware/config.txt`, og tilføj de relevante `dtoverlay`-linjer som beskrevet i dokumentationen til din HAT.

!!! quote "Relaterede oplysninger"
    - **Reference for GPIO-benforbindelser:** Se [Hardwarereference](../technical-reference/hardware.md)
    - **Softwarekonfiguration:** Se [Avanceret konfiguration](../software-development/advanced-config.md)
    - **Ændringer af kabinettet:** Se [Alternative stikmuligheder](#alternative-stikmuligheder)

## Udskiftning af NVMe SSD'en

### SSD-kompatibilitet

HALPI2 understøtter M.2 2230-2280 NVMe SSD'er i den almindelige enkeltsidede udgave. Kortere 2230-drev må gerne være dobbeltsidede, fordi der er ekstra frihøjde i den monteringsposition, men længere drev skal være enkeltsidede for at kunne være på bærekortet.

Kompatibiliteten kan kun garanteres for SSD'er leveret af Hat Labs og officielle Raspberry Pi-SSD'er. Hvis du overvejer et drev fra tredjepart, skal du kontrollere dets kompatibilitet med Raspberry Pi 5 før købet ved at læse brugerrapporter og kompatibilitetslister på nettet. Almindelige problemer med inkompatible drev er for højt strømforbrug, overophedning samt opstartsfejl eller ustabilt system.

### Forberedelse af den nye SSD

Før du monterer en ny SSD i HALPI2, bør styresystemet være flashet over på drevet. Det er godt nok muligt at flashe SSD'en efter monteringen via CM5'ens USB Boot-stik (j1), men det er nemmere og hurtigere at bruge en ekstern USB-til-NVMe-adapter. Fremgangsmåden ved flashning er beskrevet i [Softwarevejledningen](./software.md).

### Deaktivering af systemets 3,3 V-spænding

Superkondensatorerne kan holde bærekortets 3,3 V-skinne forsynet i lang tid, efter at hovedstrømmen er frakoblet. Da SSD'en forsynes fra 3,3 V-skinnen, skal skinnen deaktiveres, så SSD'en er helt spændingsløs før afmontering eller montering.

Begynd med at slukke HALPI2 og frakoble strømforsyningen. Åbn kabinettet efter fremgangsmåden i afsnittet Adgang til kabinettet.

Find jumperen `3.3V off` på bærekortet. Placeringen afhænger af kortets version. På v0.4.0-kort sidder jumperen meget tæt på superkondensatorerne, på deres »syd«-side. På v0.5.0-kort og senere finder du stiklisten `Pow.Ctrl` »øst« for superkondensatorerne. Benene `3.3V off` er de to øverste på stiklisten.

Flyt jumperen, så benene `3.3V off` kortsluttes. Det deaktiverer 3,3 V-skinnen, hvilket ses ved, at LED'erne slukker.

### Afmonteringsprocedure

M.2-slotten sidder ved bærekortets sydlige kant. Se billedet i afsnittet [Bærekortets stik](#brekortets-stik) for at finde M.2-stikket, der er mærket **g1**.

Fjern M2.5-monteringsskruen med en PH1-skruetrækker. Når skruen er fjernet, springer SSD'en op i en vinkel. Løft forsigtigt drevet i monteringsenden, og vip det ud af M.2-stikket. Hold SSD'en i kanterne, så du ikke beskadiger komponenter eller stik.

### Installationsprocedure

Sæt den forberedte SSD i M.2-stikket i en vinkel på ca. 30 grader, og sørg for, at indhakket i SSD'en flugter med tappen i stikket. Drevet skal glide let ind uden brug af kraft. Når det sidder helt i bund, trykker du monteringsenden af SSD'en ned, til den ligger fladt mod afstandsbolten.

Fastgør SSD'en med M2.5-monteringsskruen ved hjælp af en PH1-skruetrækker. Spænd skruen netop så meget, at drevet sidder solidt fast. SSD'en skal ligge helt fladt uden synlig bøjning.

Når SSD'en er på plads, fjerner du jumperen fra benene `3.3V off` for at aktivere 3,3 V-skinnen igen. Lad jumperen sidde på stiklisten til senere brug.

Saml kabinettet igen som beskrevet i afsnittet Adgang til kabinettet.
Hvis du har brug for softwarekonfiguration eller fejlfinding, kan du læse mere i [Softwarevejledningen](./software.md).

!!! quote "Relaterede oplysninger"
    - **Systemimages:** Se [Softwarevejledning](./software.md)
    - **Opstartsprocedurer:** Se [Systemdrift](./operation.md)
    - **Adgang til hardwaren:** Se [Adgang til kabinettet](#adgang-til-kabinettet)

## Udskiftning af Compute Module 5

### Forudsætninger

Udskiftning af Compute Module 5 kræver omhyggelig håndtering, fordi kort-til-kort-stikkene er sarte. CM5 bruger to stik med høj tæthed, som let beskadiges, hvis der bruges for stor kraft eller forkert teknik. Afmonter kun et monteret modul, hvis det er absolut nødvendigt, for eksempel hvis modulet er beskadiget eller skal opgraderes. Skader på Compute Module-monteringsstikkene på enten CM5 eller bærekortet er ikke dækket af garantien.

Sørg for at have termiske puder klar til varmeoverførsel, før du går i gang. Standardkonfigurationen bruger en 1 mm tyk pude på SoC'en og 2 mm tykke puder på RP1-chippen og komponenterne i den indvendige strømforsyning. Eksisterende termiske puder kan genbruges, hvis de er hele og rene.

### Adgang til Compute Module

Sluk HALPI2, og frakobl strømkilden. Fjern kabinetlåget efter fremgangsmåden i afsnittet Adgang til kabinettet. CM5 sidder på undersiden af bærekortet, så du skal først afmontere bærekortet fra kabinettet for at komme til den. For at holde styr på de mange kabler, der er tilsluttet bærekortet, anbefales det at tage et par billeder af forbindelserne, før du går videre.

Frakobl de kabler, der forhindrer bærekortet i at blive løftet. Fjern bærekortets monteringsskruer, og løft kortet ud af kabinettet.

### Afmontering af det eksisterende modul

!!! danger "Forsigtig"
    Hvis CM5-modulet frakobles ét stik ad gangen, kan vridningskræfterne rive stikket af CM5-modulet. Denne skade er ikke dækket af garantien.

CM5 holdes fast af to kort-til-kort-stik, der skal håndteres varsomt. Brug aldrig værktøj af metal til dette, da det kan beskadige stikkene eller overfladmonterede komponenter i nærheden. Brug en spudger (åbnerpind) af træ eller plast, et guitarplekter eller lignende ikke-ledende værktøj.

Placér værktøjet midt på CM5-modulets korte venstre kant, mellem modulet og bærekortet. Tryk fast ned i hjørnerne i højre side. Lirk forsigtigt opad med så lidt kraft som muligt — modulet skal slippe med et let klik, hvor begge stik løsner sig samtidig.

![Afmontering af CM5-modulet](./unmount-cm5.jpg)
*Afmonter CM5-modulet ved at trykke ned i hjørnerne ved højre kant, mens du lirker opad midt på venstre kant. Begge stik bør slippe samtidig.*

### Montering af det nye modul

Ret det nye CM5-modul ind efter stikkene på bærekortet, og brug omridset i silketrykket på bærekortet som rettesnor. Modulets omrids, der er trykt på bærekortet, skal passe nøjagtigt med CM5'ens fysiske mål, når modulet vender rigtigt.

Når modulet er rettet ind, trykker du forsigtigt og jævnt ved stikkene på begge modulets korte kanter. Du skal kunne mærke, at stikkene griber fat med et svagt klik. Tryk fast, men undgå at bøje bærekortet — understøt om nødvendigt kortet nedefra. Begge stik skal sidde helt i bund, for at systemet fungerer korrekt.

Læg nu termiske puder på CM5-modulet. De termiske puder skal placeres rigtigt: 1 mm pude på hoved-SoC'en og 2 mm puder på RP1-chippen og strømforsyningens komponenter. Hvis du genbruger eksisterende puder, skal du sikre dig, at de er rene og placeret rigtigt.

![Placering af termiske puder på CM5](./cm5-thermal-pads-annotated.jpg)
*Placering af termiske puder på Compute Module 5. Brug en 1 mm tyk pude på SoC'en (i midten) og 2 mm tykke puder på RP1 og strømforsyningens komponenter. De termiske puders faktiske form og størrelse kan variere.*

### Antennetilslutning

Før du monterer bærekortet igen, skal du tilslutte U.FL-antennekablet til CM5'ens stik til den trådløse antenne. Denne forbindelse er umulig at komme til, når bærekortet er monteret igen. U.FL-stikket kræver omhyggelig indretning og et fast tryk for at sidde rigtigt. Du skal kunne mærke et tydeligt klik, når stikket er helt i indgreb. Pas på ikke at bøje stikkets kappe under monteringen.

### Endelig samling

Efterse monteringen af modulet, og kontrollér, at begge stik sidder helt i bund, og at modulet ligger fladt mod bærekortet uden mellemrum. De termiske puder skal have kontakt med de komponenter på modulet, der udvikler varme.

Placér bærekortet tilbage i kabinettet, og sørg for, at de termiske puder på CM5 flugter med de tilsvarende varmeafledende flader i kabinettets bund. Monter alle bærekortets monteringsskruer igen, og tilslut de kabler, der blev frakoblet under afmonteringen.

Gør samlingen færdig efter den almindelige fremgangsmåde for lukning af kabinettet. Ved første opstart bør systemet automatisk genkende den nye CM5.

!!! warning "Advarsel om stikkene"
    Kort-til-kort-stikkene er de mest skrøbelige komponenter i denne procedure. Brug aldrig værktøj af metal i nærheden af stikkene, brug kun lodret kraft ved afmontering og montering, og kontrollér, at alt flugter perfekt, før du trykker til. Beskadigede stik kræver som regel, at bærekortet udskiftes.

!!! quote "Relaterede oplysninger"
    - **Opsætning af systemet efter udskiftning:** Se [Softwarevejledning](./software.md)
    - **Fejlfinding ved opstart:** Se [Fejlfinding](./troubleshooting.md)
    - **Termisk styring:** Se [Hardwarereference](../technical-reference/hardware.md)

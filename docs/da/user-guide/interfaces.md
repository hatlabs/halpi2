---
translated_from: da8aa35c462e57bc7c0b00d50046a1df518e97dd
---

# Grænseflader og forbindelser

## CAN FD / NMEA 2000

HALPI2 har en fuldt adskilt [CAN FD](https://en.wikipedia.org/wiki/CAN_FD)-grænseflade, der understøtter både marine [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000)-netværk og anvendelser inden for automotive og industri. Grænsefladen giver hurtig datakommunikation med fuldstændig elektrisk adskillelse, så den er ufølsom over for støj.

### Grænsefladens specifikationer

CAN FD-grænsefladen understøtter både standard-CAN og CAN FD-protokollerne. I NMEA 2000-anvendelser kører grænsefladen i almindelig CAN-tilstand med standardhastigheden 250 kbit/s. Til automotive- og industrianvendelser kan grænsefladen udnytte CAN FD fuldt ud med datahastigheder op til 8 Mbit/s.

Frontpanelet har et Micro-C-stik, der er kompatibelt med almindelige NMEA 2000-kabler og -komponenter. Det gør det muligt at koble direkte ind i eksisterende marine netværk med almindelige T-stik og dropkabler.

### Strømkonfiguration og belastning af netværket

Hvor meget HALPI2 belaster strømforsyningen i et NMEA 2000-netværk, afhænger af den valgte strømkonfiguration. I standardkonfigurationen med ekstern forsyning via E7T-stikket trækker enheden ingen strøm fra NMEA 2000-netværket, og Load Equivalency Number (LEN) er derfor 0.

Når enheden konfigureres til busforsyning fra NMEA 2000, skal strømforbruget begrænses til 0,9 A med den indbyggede strømbegrænser. Det svarer til en LEN-værdi på 18. Når HALPI2 forsynes via NMEA 2000, bør enheden tilsluttes netværkets backbone tæt på indfødningskablet, så spændingsfaldet bliver mindst muligt, og driften bliver pålidelig.

### Hardwarekonfiguration

Bærekortet har en termineringsmodstand på 120 Ω, som kan aktiveres med en jumper. Terminering i selve enheden bør undgås i NMEA 2000-anvendelser, da standarden ikke tillader det. I automotive- eller industrianvendelser med punkt-til-punkt-kommunikation kan jumperen derimod sættes, så termineringsmodstanden aktiveres.

Til diagnostik og fejlfinding på netværket har bærekortet dedikerede RX- og TX-LED'er, der viser aktiviteten på netværket. LED'erne giver øjeblikkelig visuel tilbagemelding om afsendelse og modtagelse af data, så det er nemmere at finde årsagen til forbindelsesproblemer.

### Installation i netværket

Tilslutning til NMEA 2000-netværk sker med et almindeligt T-stik (medfølger ikke), der monteres på netværkets backbone, og et dropkabel, der forbinder T-stikket med HALPI2's Micro-C-stik.

### Softwareintegration

CAN-grænsefladen spiller problemfrit sammen med Linux via SocketCAN-frameworket og optræder som netværksenheden `can0`. Denne standardgrænseflade gør det muligt at bruge de almindelige CAN-værktøjer i Linux til overvågning og diagnostik. Netværksgrænsefladen er forudkonfigureret i alle HALPI2's styresystemimages (HaLOS, OpenPlotter og Raspberry Pi OS).

Integration med Signal K-serveren findes i HaLOS Marine-varianterne og i OpenPlotter, hvor CAN-grænsefladen automatisk registreres og bruges til behandling af NMEA 2000-data. På HaLOS-images uden for marinesegmentet kan Signal K installeres fra Container Apps-butikken i Cockpit. Signal K-serveren står for afkodningen af PGN'er og giver webbaseret adgang til netværkets data i realtid.

### Fejlfinding

Fejlfinding på netværket begynder ved RX/TX-LED'erne på bærekortet. Ved normal drift blinker LED'erne uregelmæssigt i takt med trafikken på netværket. Manglende RX-aktivitet kan tyde på kabelproblemer eller forkert terminering, mens manglende TX-aktivitet kan tyde på konflikter på netværket eller på kablingen.

Linux-kommandoen `candump` kan bruges til at overvåge CAN-bussen direkte fra kommandolinjen. Værktøjet giver detaljerede oplysninger om alle meddelelser på bussen og gør grundig diagnostik mulig. I sin enkleste form kan du køre:

```bash
candump can0
```

Det viser alle indkommende rå CAN-meddelelser i realtid.

Signal K-serverens dashboard giver yderligere muligheder for at overvåge netværket. Det viser datahastighederne for NMEA 2000 fra CAN-grænsefladen i realtid. Med værktøjet data browser kan du se de afkodede NMEA 2000-data.

!!! quote "Relaterede oplysninger"
    - **Strømkonfiguration:** Se [Kom godt i gang](../getting-started/getting-started.md#permanent-strmtilslutning)
    - **Opsætning af software:** Se [Softwarevejledning](./software.md)
    - **Fejlfinding på netværket:** Se [Fejlfinding](./troubleshooting.md)


## RS-485 (NMEA 0183)

HALPI2 har en galvanisk adskilt [RS-485](https://en.wikipedia.org/wiki/RS-485)-grænseflade, der giver seriel kommunikation til marine [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422]-netværk og industrielle anvendelser.

[^rs422]: Teknisk set bruger NMEA 0183 RS-422-standarden, men RS-485 er nedadkompatibel, så HALPI2 kan kommunikere med både RS-422- og RS-485-enheder.

### Grænsefladens specifikationer

RS-485-transceiveren kan køre med hastigheder op til 10 Mbit/s, men typiske NMEA 0183-anvendelser bruger standardhastighederne 4800 eller 38400 bit/s. Grænsefladen er galvanisk adskilt og opfylder NMEA 0183-specifikationen, så HALPI2 beskyttes mod jordsløjfer og den elektriske støj, der er almindelig i marine miljøer.

Grænsefladen er internt forbundet til UART 4 på Raspberry Pi og optræder som `/dev/ttyAMA4` i Linux-styresystemet. Denne almindelige serielle enhed kan bruges af enhver applikation, der understøtter seriel kommunikation, herunder Signal K-serveren, OpenCPN og egne softwareapplikationer.

### Hardwarekonfiguration

Bærekortet har dedikerede RX- og TX-LED'er, der viser kommunikationsaktiviteten på RS-485-grænsefladen. LED'erne giver øjeblikkelig visuel tilbagemelding under installation og fejlfinding, så det er nemt at kontrollere, at data sendes og modtages korrekt.

Når enheden bruges som en almindelig RS-485-grænseflade, kan den konfigureres til enten automatisk eller manuel styring af sendetilladelsen. I manuel tilstand styres signalet for sendetilladelse af et GPIO-ben, så softwaren bestemmer, hvornår grænsefladen er i sende- eller modtagetilstand. Det er nødvendigt i multi-talker-anvendelser, hvor grænsefladen skal være i recessiv tilstand, når den ikke sender. I automatisk tilstand aktiverer hardwaren selv sendetilladelsen, når der sendes data, hvilket forenkler opsætningen i single-talker-anvendelser.

Desuden understøtter RS-485-grænsefladen halv duplex, så den kan både sende og modtage på det samme ledningspar.

Grænsefladen kan også deaktiveres helt via hardwarekonfigurationen, hvis UART 4 skal bruges til andre formål.

### Kabling og tilslutning

RS-485-grænsefladen kræver en kabelforskruning eller et panelstik, som du selv skal skaffe. En god mulighed er [et SP13-panelstik med pigtail](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). Grænsefladen er nedadkompatibel med den RS-422-signalering, NMEA 0183 bruger, og understøtter både RS-485-netværk med flere talere og RS-422-netværk med én taler og flere lyttere. Den bruger balancerede differentielle par, mærket TX+/TX- og RX+/RX-.

### Softwareintegration

Alle HALPI2-images er forudkonfigureret, så RS-485-grænsefladen er klar til brug. På HaLOS Marine-images og i OpenPlotter registrerer Signal K-serveren automatisk grænsefladen og modtager de NMEA 0183-data, der sendes.

I egne applikationer opfører grænsefladen sig som en almindelig seriel port i Linux. Applikationer kan åbne `/dev/ttyAMA4` og indstille baudhastighed, databits, stopbits og paritet efter det tilsluttede udstyrs krav. Applikationer i Python, Node.js og C/C++ kan alle nemt bruge grænsefladen med de gængse biblioteker til seriel kommunikation.

### Almindelige anvendelser

I marine miljøer forbindes RS-485-grænsefladen typisk til GPS-modtagere, ekkolod, vindmålere, AIS-transpondere eller andre enheder, der bruger NMEA 0183-protokollen. Industrielle anvendelser kan omfatte tilslutning af PLC'er, sensorer og andet automationsudstyr, der bruger Modbus RTU eller andre RS-485-protokoller.

Grænsefladens høje hastighed understøtter også anvendelser uden for standarden, for eksempel indsamling af sensordata med høj hastighed eller egne kommunikationsprotokoller, og det gør HALPI2 velegnet til forskningsfartøjer og specialiserede overvågningsopgaver.

!!! quote "Relaterede oplysninger"
    - **Softwarekonfiguration:** Se [Softwarevejledning](./software.md)
    - **Fejlfinding:** Se [Fejlfinding](./troubleshooting.md)


## GNSS (GPS)

HALPI2 understøtter GNSS-modtager-HAT'er, der tilsluttes UART0 (`/dev/ttyAMA0`). Enhver GNSS-modtager på denne port virker med gpsd med det samme.

For u-blox-modtagere (for eksempel Max-M8Q) giver HaLOS Marine-images desuden en automatisk konfiguration, der er optimeret til marin brug.

### Automatisk konfiguration (u-blox-modtagere)

På HaLOS Marine-images registrerer og konfigurerer en systemd-tjeneste (`configure-ublox-marine`) automatisk u-blox-modtagere ved hver opstart:

| Parameter | Værdi |
|:----------|:------|
| Baudhastighed | 115200 bit/s (fabriksindstilling: 9600) |
| Opdateringshastighed | 10 Hz (100 ms) |
| Dynamisk model | Sea (optimeret til marin brug) |

Konfigurationen køres ved hver opstart, fordi ROM-baserede u-blox-moduler (for eksempel MAX-M8Q) ikke har flashhukommelse. Indstillingerne gemmes i Battery-Backed RAM (BBR), og de kan gå tabt, hvis backupbatteriets forsyning afbrydes — for eksempel når enheden står uden strøm i længere tid. Omkonfigurationen er gennemsigtig og forlænger opstarten af gpsd med cirka 2 sekunder.

Hvis der ikke findes nogen modtager, afslutter tjenesten stille. En nyinstalleret GNSS-HAT konfigureres automatisk ved næste genstart.

### Adgang til data

GPS-data leveres af [gpsd](https://gpsd.io/) på TCP-port 2947. På HaLOS Marine-images forbinder Signal K automatisk til gpsd — der kræves ingen yderligere konfiguration.

Til diagnostik kan du bruge de almindelige kommandolinjeværktøjer til gpsd:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Images uden HaLOS

På Raspberry Pi OS eller andre styresystemer skal du installere og konfigurere gpsd manuelt:

```bash
sudo apt install gpsd gpsd-clients
```

Rediger `/etc/default/gpsd`, så `DEVICES="/dev/ttyAMA0"` er sat, og genstart tjenesten. Modtageren kører med fabriksindstillingerne (9600 baud, 1 Hz), medmindre den konfigureres med `ubxtool` fra pakken `gpsd-clients`.

!!! quote "Relaterede oplysninger"
    - **gpsd på HaLOS:** Se [HaLOS' GPS-dokumentation](https://docs.halos.fi/user-guide/gps/)
    - **Opsætning af software:** Se [Softwarevejledning](./software.md)


## Ethernet

HALPI2 har en gigabit-ethernetgrænseflade, der giver hurtig netværksforbindelse til dataoverførsel, fjernadgang og integration med netværk om bord. Ethernetporten på bærekortet er et almindeligt RJ45-stik. Den er ført ud til et panelstik, som et eksternt ethernetkabel kan tilsluttes.

## USB

HALPI2 har i alt fire indbyggede USB 3.0 Type A-porte, der giver hurtig tilslutning af mange forskellige periferienheder. Den ene port er ført direkte til CM5'ens USB 3.0-grænseflade, mens de tre andre er tilsluttet via en indbygget USB 3-hub. I standardkonfigurationen er to af portene ført ud til frontpanelet, mens to er tilgængelige på bærekortet til interne forbindelser.

## HDMI

HALPI2 har to HDMI 2.0-porte (HDMI0 og HDMI1) til videoudgang. Bærekortet har fladkabelstik (FFC) til begge HDMI-porte. De er ført ud til frontpanelet med specialfremstillede FFC-kabler. Stikkene på frontpanelet er almindelige HDMI Type A-stik.

HALPI2's HDMI-udgang understøtter pålideligt to samtidige videostrømme i Full HD (1080p). 4K-video fungerer måske, men er ikke garanteret.

## MIPI (CSI/DSI)

Bærekortet har to MIPI CSI/DSI-stik til kamera- og skærmgrænseflader. Stikkene er 22-benede FFC-stik (fladkabel) med 0,5 mm benafstand. De bør fungere uden videre med nyere Raspberry Pi-kompatible kameraer og skærme.

Af hensyn til vandtætheden bør FFC-kabler kun bruges til interne forbindelser.

## Eksterne knapper

HALPI2 har en 2×3-benet stikliste på bærekortet til tilslutning af eksterne knapper. Kabinettet har ingen indbyggede knapper, så du selv kan vælge knappernes placering og type efter dit behov.

### Benforbindelser på knapstiklisten

Bærekortet har en 6-benet stikliste med tre mærkede knapfunktioner:

| Mærkning | Funktion | Beskrivelse |
|:------|:---------|:------------|
| Reset | Reset af controlleren | Hardwarereset (RP2040 RUN-ben) |
| Power | Tænd/sluk for Raspberry Pi | Tænd/sluk-knap til CM5 (PWR_BUT-indgang) |
| User | Kan konfigureres af brugeren | Brugerdefineret hændelse (endnu ikke implementeret) |

Hver knaptilslutning bruger to ben: et til knappens signal og et til jord. Brug momentkontakter af typen normalt åben (NO), der forbinder signalbenet til jord, når de trykkes ind.

### Knappernes funktioner

**Reset-knap:**
Reset-knappen giver et hardwarereset af systemet ved at trække RP2040'ens RUN-ben lavt. Handlingen udfører en fuldstændig nulstilling af systemet, som påvirker controlleren, CM5 og alle tilsluttede periferienheder. Reset-knappen er især nyttig i nødsituationer, hvor softwarens nedlukningsprocedurer er slået fejl, og systemet ikke længere reagerer.

**Tænd/sluk-knap:**
Tænd/sluk-knappen er forbundet direkte til CM5'ens indgang til tænd/sluk-knap og fungerer på samme måde som tænd/sluk-knappen på Raspberry Pi 5. Et dobbeltklik på knappen anmoder om en kontrolleret nedlukning af systemet, så styresystemet kan lukke applikationerne korrekt og afmontere filsystemerne, før strømmen slås fra. Et langt tryk på knappen fremtvinger øjeblikkelig slukning, hvilket kun bør bruges, når systemet ikke reagerer.

**Brugerknap:**
Brugerknappens funktion afventer stadig implementering i softwaren og vil give brugerkonfigurerbar funktionalitet i kommende firmwareudgivelser. Når den er implementeret, er knappen tænkt til egne handlinger og applikationsspecifikke udløsere, så du kan definere knappens opførsel ud fra dine egne driftsbehov.

### Montering af knapper

#### Montering direkte i kabinettet

Ved montering direkte i HALPI2's kabinet kan du bruge de huller på 6 mm eller 13 mm, der allerede findes i kabinettet. Begynd med at fjerne de rigtige blindpropper fra hullerne, og montér en vandtæt knapenhed, der passer til hullets diameter. Forbind knappen til stiklisten på bærekortet med et passende kabel, og sørg for ordentlig trækaflastning og vejrbestandig tætning ved gennemføringen i kabinettet.

#### Montering i et eksternt panel

Når knapperne monteres i et fjernbetjeningspanel, skal du vælge et sted, der både er let at nå og bevarer vejrbestandigheden. Brug kabelforskruninger ved kabelindføringerne, og forbind knapperne med et forlængerkabel med ledere i 22–26 AWG. Hold den samlede kabellængde under 3 m, så signalkvaliteten bevares. I installationer, der udsættes for fugt eller barske miljøer, bør du bruge vandtætte stik ved samlingerne, så driften bliver pålidelig på lang sigt.

#### Tilslutning

Alle knaptilslutninger til bærekortet bør bruge hunstik med 2,54 mm benafstand. Sørg for, at benene flugter, og at forbindelsen sidder fast, så der ikke opstår kontaktproblemer under drift.

!!! quote "Relaterede oplysninger"
    - **Strømstyring:** Se [Strømstyring og nedlukningsprocedurer](./operation.md#strmstyring-og-nedlukningsprocedurer)
    - **Adgang til hardwaren:** Se [Vedligeholdelse af hardwaren](./hardware.md)

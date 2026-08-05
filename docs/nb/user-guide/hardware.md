# Maskinvareveiledning

## Tilgang til kabinettet

HALPI2 har et pulverlakkert kabinett i støpt aluminium med ferdigborede hull for panelkontakter. Når det er behov for interne endringer eller vedlikehold, får du tilgang til kabinettet ved å følge prosedyrene nedenfor.

### Åpne kabinettet

For å komme til de interne komponentene begynner du med å forsikre deg om at enheten er helt avslått og at strømkablene er koblet fra. Lokket er festet med fire senkeskruer M4x10 med PH2-hode. Bruk en PH2-skrutrekker til å fjerne skruene, og ta av lokket.

### Sette sammen igjen

Før du setter kabinettet sammen igjen, bør du ta deg tid til å kontrollere at alle interne forbindelser sitter godt og er riktig plassert. Legg kablene forsiktig slik at de ikke kommer i klem eller får skarpe knekk.

Det er lett å koble flatkablene (FFC) inn feil vei ved et uhell. Følg «Contacts»-pilene på silketrykket for å kontrollere at retningen er riktig.

Vær spesielt oppmerksom på pakningen i lokket. Se etter skader, smuss eller forskyvning som kan svekke værtettheten til kabinettet.

Monter de fire M4x10-lokkskruene igjen med PH2-skrutrekkeren. Ikke trekk til for hardt.


## Panelkontakter

### Standardkonfigurasjon

HALPI2 leveres med en standard kontaktkonfigurasjon som passer til de fleste bruksområder. Standardoppsettet omfatter:

- **E7T-strømkontakt**
- **NMEA 2000 micro-kontakt**
- **Gigabit Ethernet RJ45**
- **HDMI-utgang**
- **2× USB 3.0 Type-A**
- **3× PG7-posisjoner for kabelgjennomføring** (med blindplugger)
- **2× RP-SMA-antenneposisjoner** (med blindplugger)
- **Trykkutjevningsplugg** for trykkutjevning

![Front Panel Connectors and Blind Plugs](./front-panel-connectors-all.jpg)
*Kontakter og blindplugger på frontpanelet. Kontaktene som er merket med grønt, inngår i standardkonfigurasjonen. De gule posisjonene er blindplugger som kan byttes ut med kontakter ved behov. Den røde posisjonen er trykkutjevningspluggen, som ikke må fjernes.*

### Tilpassede kontaktvalg

Hvis du trenger andre kontakttyper, kan du endre panelkonfigurasjonen:

#### Fjerne kontakter

!!! warning "Viktig"
    Endre kontaktene bare når enheten er slått av og koblet fra alle kilder.

    Plastgjenger kan skades av for høyt tiltrekkingsmoment. Bruk vanlige pipenøkler, men trekk bare til for hånd.

1. **Bruk riktig pipestørrelse:**
    - Store kontakter: 26 mm pipe
    - M6 nylonbolter: 10 mm pipe
    - RP-SMA-kontakter: 8 mm pipe
    - PG7-posisjoner: stor flat skrutrekker, 17 mm pipe

2. **Fjern forsiktig** – plastgjenger kan skades av for høyt tiltrekkingsmoment

3. **Ta vare på delene du fjerner** til eventuell senere bruk

#### Montere nye kontakter

1. **Bruk bare kontakter av marin kvalitet** eller kontakter som er godkjent for miljøet
2. **Sørg for god tetting** – bred flens kreves på innsiden
3. **Trekk bare til for hånd** – ikke overbelast plastgjengene
4. **Prøvemonter** før endelig montering

## Intern oppbygning

- HALPI2-bærekortet er hovedkortet i datamaskinen. Det huser Compute Module 5 (CM5) på undersiden og gir strømstyring, indikatorer og tilkoblinger for alle grensesnitt.

### Funksjonsområder på bærekortet

De viktigste funksjonsområdene på bærekortet er vist i bildet nedenfor.

![Carrier Board Layout, Top-side](./carrier-board-top-layout.jpg)
*Oversiden av bærekortet, med de viktigste funksjonsområdene.*

### Kontakter på bærekortet

Funksjonaliteten nås gjennom en rekke kontakter på kortet, vist i bildet nedenfor.

![Carrier Board Connectors, Top-side](./carrier-board-top-conx.jpg)
*Kontakter på oversiden av bærekortet.*

En oversikt over kontaktene på oversiden er gitt nedenfor.

| Merking | Beskrivelse |
|:------|:------------|
| **a1** | Strømkontakt (Phoenix MC-type, 3,81 mm senteravstand) |
| **a2** | Bryter for begrensning av inngangsstrøm (0,9 A eller 2,5 A) |
| **a3** | Jumper for strømstyring. Kortslutt «3.3V off»-pinnene for å tvinge 3,3 V-skinnen av. Kortslutt «5V on»-pinnene for å tvinge 5 V-skinnen på. **NB:** På kort med versjon 0.4.0 er kontaktene **a3** og **c2** organisert annerledes. |
| **b1** | Ethernet-port (RJ45) |
| **c1** | USB-port for kontrolleren. Brukes til å flashe firmware til RP2040-mikrokontrolleren. |
| **c2** | MCU USB BOOT-jumperpinneliste. Kortslutt pinnene for å sette RP2040 i USB-oppstartsmodus. |
| **c3** | Feilsøkingspinneliste for kontrolleren |
| **c4** | Ubestykket GPIO-pinneliste for kontrolleren |
| **c5** | Pinnelister for knapper. Brukes til å koble til Power-, Reset- og User-knappene. |
| **c6** | Strømknapp. Brukes til å slå Compute Module 5 på og av. |
| **d1** | Raspberry Pi 40-pinners GPIO-pinneliste |
| **e1** | MIPI0-kontakt for kamera- eller skjermgrensesnitt |
| **e2** | MIPI1-kontakt for kamera- eller skjermgrensesnitt |
| **f1** | HDMI0-kontakt |
| **f2** | HDMI1-kontakt |
| **g1** | M.2 NVMe SSD-kontakt |
| **h1** | CAN FD-grensesnitt (Phoenix MC-type, 3,81 mm senteravstand) |
| **h2** | Jumper for CAN-terminering. Kortslutt pinnene for å aktivere termineringsmotstanden på CAN FD-bussen. |
| **i1** | RS-485-grensesnitt (Phoenix MC-type, 3,81 mm senteravstand) |
| **i2** | Jumper for auto/manuell aktivering av RS-485. |
| **i4** | XRS-485 RX Enable-jumper. Kortslutt pinnene for å aktivere mottak av RS-485-trafikk. |
| **j1** | Compute Module USB Boot-kontakt. Brukes til å flashe firmware til Compute Module 5. |
| **j2** | Velgerbryter for oppstartsmodus på Compute Module. Sett den til «Normal» for normal drift og «Abnormal» for USB-oppstartsmodus. En varsel-LED lyser når bryteren står på «Abnormal». |
| **m1** | USB3-kontakt 0. Koblet direkte til CM5. |
| **m2** | USB3-kontakt 1-0. Koblet til den innebygde USB3-huben. |
| **m3** | USB3-kontakt 1-1. Koblet til den innebygde USB3-huben. |
| **m4** | USB3-kontakt 1-2. Koblet til den innebygde USB3-huben. |
| **n1** | CR2032-batteriholder for RTC (sanntidsklokke) |
| **q1** | Viftekontakt for CM5. Viften kan brukes til å bedre luftsirkulasjonen inne i kabinettet. Den trengs ikke når standardkabinettet brukes. |

![Carrier Board Connectors, Bottom side](./carrier-board-bottom-conx.jpg)
*Kontakter på undersiden av bærekortet.*

En oversikt over kontaktene på undersiden er gitt nedenfor.

| Merking | Beskrivelse |
|:------|:------------|
| **p1** | Kontakt for Compute Module 5. |
| **q1** | Viftekontakt for CM5, alternativ plassering. Denne pinnelisten kan brukes til å koble en CPU-vifte over CM5-modulen når du bruker et tilpasset kabinett. **NB:** Kontaktene **q1** og **q2** er koblet parallelt og må ikke brukes samtidig. |

Til slutt sitter antennekontakten for WiFi og Bluetooth på selve Compute Module 5. Den er vist i bildet nedenfor.

![WiFi Antenna Connector](./cm5-top-conx.jpg)
*U.FL-antennekontakt på Compute Module 5.*

| Merking | Beskrivelse |
|:------|:------------|
| **r1** | U.FL-kontakt for WiFi- og Bluetooth-antennen. |

### Blinkenlights

Bærekortet har flere status-LED-er for overvåking av systemet.

![Carrier Board Status LEDs](./carrier-board-top-leds.jpg)
*Status-LED-ene på bærekortet og fargene deres.*

Status-LED-ene gir informasjon om strøm- og aktivitetstilstanden til systemet. En oversikt over status-LED-ene er gitt nedenfor.

| Merking | Farge | Beskrivelse |
|-------|:-------|:------------|
| **1** | RGB   | Fem RGB-LED-er. Disse LED-ene brukes til å vise systemstatus og aktivitet på frontpanelet. |
| **2** | Rød   | Strøm-LED-er for 3,3 V- og 5 V-skinnene. Disse LED-ene viser strømstatusen til de respektive spenningsskinnene. |
| **3** | Gul| Hastighetsindikator for Ethernet. Lyser når Ethernet-porten har forhandlet fram en forbindelse på 100/1000 Mbps. |
| **4** | Grønn | Aktivitetsindikator for Ethernet. Blinker når det er nettverkstrafikk på Ethernet-porten. |
| **5** | Blå | Aktivitetsindikator for SSD. Blinker når det er lese- eller skriveaktivitet på M.2 NVMe SSD-en. |
| **6** | Rød | Statusindikator for Pi-strøm. Lyser når systemet har strøm, men er stengt ned. |
| **7** | Grønn | Aktivitetsindikator for Pi. Blinker når det er aktivitet på Raspberry Pi-en. |
| **8** | Ravgul | Varsel om unormal oppstartsmodus. Lyser når bryteren for USB-oppstartsmodus står på «Abnormal». Det betyr at enheten er stilt inn for flashing via USB Boot-kontakten og ikke starter opp normalt. |
| **9** | Grønn | CAN TX/RX-LED-er. Disse LED-ene blinker når data enten mottas (RX) eller sendes (TX) på CAN-grensesnittet. |
| **10** | Grønn | RS-485 TX/RX-LED-er. Disse LED-ene blinker når data enten mottas (RX) eller sendes (TX) på RS-485-grensesnittet. |

Mønstrene for RGB-LED-ene er dokumentert i [driftsveiledningen](./operation.md#status-led-indicators).

## Konfigurasjon av strømbegrensning

Bærekortet har en strømbegrensningsbryter for å stille inn den største strømmen som leveres til eksterne enheter. Bryteren finner du som **a2** i bildet i avsnittet [Kontakter på bærekortet](#carrier-board-connectors).

!!! info "Innstillinger for strømbegrensning"
    **0,9 A-innstilling (standard):**

    - Obligatorisk ved strømforsyning fra NMEA 2000-bussen
    - Egnet for grunnleggende drift

    **2,5 A-innstilling:**

    - For eksterne enheter med høyt strømforbruk
    - Raskere lading av superkondensatorene
    - Bare med dedikert strømtilkobling

For å endre strømgrensen slår du først HALPI2 helt av og tar av kabinettlokket etter prosedyren i avsnittet om tilgang til kabinettet. Finn strømbegrensningsbryteren på bærekortet og sett bryteren i ønsket stilling (enten 0,9 A eller 2,5 A). Når innstillingen er endret, setter du kabinettet sammen igjen og passer på at alle forbindelser fortsatt sitter godt.

## Bruk av HAT-er

### HAT-kompatibilitet

HALPI2 støtter standard Raspberry Pi HAT-er via 40-pinners GPIO-pinnelisten og er fullt elektrisk og mekanisk kompatibel med HAT-spesifikasjonen for Raspberry Pi. Bærekortet har samme GPIO-pinneoppsett som en vanlig Raspberry Pi, slik at de fleste HAT-er som er laget for Raspberry Pi 4 og 5, virker uten endringer. Dette gjelder både offisielle Raspberry Pi-HAT-er og utvidelseskort fra tredjeparter som følger HAT-standarden.

### Fysiske begrensninger

HALPI2-kabinettet gir 45 mm klaring i høyden over bærekortet, nok til å romme opptil to HAT-er oppå hverandre. Området til venstre for det opptegnede monteringsområdet for HAT-er er opptatt av superkondensatorene, noe som begrenser plassen for HAT-er som er større enn standardmålene på 65 × 56 mm. Vær spesielt oppmerksom på HAT-er med kontakter på siden. Kontakter som vender mot «sør» eller «øst», går som regel greit, men kontakter som vender mot «vest», kan komme i konflikt med superkondensatorene.

### GPIO-pinnekonflikter

Flere GPIO-pinner brukes av de innebygde grensesnittene i HALPI2 og må tas hensyn til når du velger kompatible HAT-er. Tabellen nedenfor viser de reserverte GPIO-pinnene og funksjonene deres:

| GPIO-nummer | Funksjon | Grensesnitt | Merknader |
|----------|----------|-----------|-------|
| GPIO 2 | I2C SDA | System-I2C | Kan deles; adresse 0x6d er reservert |
| GPIO 3 | I2C SCL | System-I2C | Kan deles; adresse 0x6d er reservert |
| GPIO 6 | SPI CS | CAN FD | Egendefinert chip select for CAN-kontrolleren |
| GPIO 9 | SPI MISO | CAN FD | Delt SPI0-buss |
| GPIO 10 | SPI MOSI | CAN FD | Delt SPI0-buss |
| GPIO 11 | SPI SCK | CAN FD | Delt SPI0-buss |
| GPIO 12 | UART TX | RS-485 | UART4 sending |
| GPIO 13 | UART RX | RS-485 | UART4 mottak |
| GPIO 24 | RS-485 EN | RS-485 | Aktiveringssignal (bare i manuell modus) |
| GPIO 26 | CAN INT | CAN FD | Avbruddslinje for CAN-kontrolleren |

### Deling av grensesnitt og konflikter

I2C-bussen på GPIO 2 og 3 kan deles med HAT-enheter, siden I2C støtter flere enheter på samme buss. HAT-er må likevel ikke bruke I2C-adressen 0x6d, som er reservert for systemkontrolleren i HALPI2. De fleste I2C-HAT-er virker uten problemer, men kontroller hvilke I2C-adresser de bruker før montering.

SPI0-bussen som brukes til CAN FD-grensesnittet, kan i prinsippet deles med andre SPI-enheter, siden HALPI2 bruker egendefinerte pinner for chip select (GPIO 6) og avbrudd (GPIO 26). HAT-er som bruker SPI0 med de vanlige chip select-pinnene (GPIO 7 eller GPIO 8), kan fungere sammen med CAN-grensesnittet, men kan kreve ekstra konfigurasjon med device tree-overlay.

### Deaktivere innebygde grensesnitt

Hvis en HAT trenger eksklusiv tilgang til pinner som brukes av de innebygde grensesnittene i HALPI2, kan disse grensesnittene deaktiveres med maskinvareendringer. CAN FD-grensesnittet kan frigjøres helt ved å fjerne loddebroen GPIO6-CAN.CS på undersiden av bærekortet. Denne endringen kobler CAN-kontrolleren fra SPI-bussen og frigjør GPIO 6, 9, 10, 11 og 26 til bruk for HAT-en.

RS-485-grensesnittet kan deaktiveres ved å fjerne RX Enable-jumperen (i4) på bærekortet. Det hindrer RS-485-transceiveren i å motta data og frigjør GPIO 12 og 13 til andre formål. Hvis du ikke trenger manuell styring av sendeaktivering, kan også GPIO 24 brukes til noe annet ved å sette jumperen for auto/manuell aktivering av RS-485 (i2) i automatisk stilling.

### Monteringsprosedyre

Begynn monteringen med å slå av systemet og koble fra alle strømkilder. Ta av kabinettlokket etter prosedyren i avsnittet om tilgang til kabinettet.

Bærekort fra versjon 0.5.0 og senere har ferdigmonterte M2.5-gjengeinnsatser i de fire monteringspunktene for HAT-er, noe som forenkler monteringen. Eldre v0.4.0-kort krever at M2.5-muttere monteres manuelt. For å montere mutterne må bærekortet demonteres midlertidig. Det er mulig å gjøre dette uten å koble fra alle kablene.

For mange vanlige HAT-er passer 15 mm avstandsbolter, men mål høyden på hunpinnelisten på HAT-en for å sikre riktig klaring. Sokkelen på hannpinnelisten er 2,5 mm høy, så legg dette til høyden på hunpinnelisten for å finne nødvendig lengde på avstandsboltene.

Skru avstandsboltene inn i monteringshullene, eller fest dem med muttere fra undersiden på v0.4.0-kort. Rett HAT-en inn mot 40-pinners GPIO-pinnelisten og kontroller at alle pinnene står riktig før du trykker jevnt for å få kontakten på plass. HAT-en skal ligge parallelt med bærekortet uten synlig glipe ved GPIO-forbindelsen.

Fest HAT-en med M2.5-skruer eller flere avstandsbolter gjennom monteringshullene i HAT-en og ned i avstandsboltene. Disse skruene følger ikke med HALPI2 og må skaffes separat. Trekk skruene bare så hardt til at HAT-en sitter fast, uten at kretskortet bøyes.

### Kabelhåndtering

Hvis HAT-en har eksterne kontakter som må nås fra utsiden av kabinettet, kan du vurdere å montere egnede panelkontakter i de ledige PG7-posisjonene for kabelgjennomføring. Da beholder kabinettet tettheten mot omgivelsene samtidig som du får enkel tilgang utenfra.

### Demonteringsprosedyre

Demontering av en HAT følger monteringsprosedyren i motsatt rekkefølge. Slå systemet helt av og koble fra alle strømkilder før du åpner kabinettet. Fjern M2.5-monteringsskruene og løft HAT-en rett opp fra GPIO-pinnelisten, uten sidekrefter som kan bøye pinnene.

Hvis HAT-en ser ut til å sitte fast, må du se etter oversett festemateriell eller kabler før du bruker mer kraft. Noen HAT-er med stramme kontakter kan trenge en forsiktig vippebevegelse mens du drar oppover. Vipp HAT-en i nord–sør-retningen; vipping øst–vest kan bøye pinnene i pinnelisten når kontakten plutselig slipper.

### Programvarekonfigurasjon

Etter maskinvaremonteringen kan HAT-en trenge programvarekonfigurasjon for å virke som den skal. Mange HAT-er har device tree-overlay som må aktiveres i konfigurasjonen til Raspberry Pi. Rediger `/boot/firmware/config.txt` og legg til de riktige `dtoverlay`-linjene slik dokumentasjonen for HAT-en angir.

!!! quote "Relatert informasjon"
    - **Referanse for GPIO-pinneoppsett:** Se [Maskinvarereferanse](../technical-reference/hardware.md)
    - **Programvarekonfigurasjon:** Se [Avansert konfigurasjon](../software-development/advanced-config.md)
    - **Endringer på kabinettet:** Se [Tilpassede kontaktvalg](#custom-connector-options)

## Bytte NVMe SSD-en

### SSD-kompatibilitet

HALPI2 støtter M.2 2230–2280 NVMe SSD-er i vanlig ensidig utførelse. Kortere 2230-disker kan være tosidige på grunn av den ekstra klaringen i den monteringsposisjonen, men lengre disker må være ensidige for å få plass på bærekortet.

Kompatibilitet kan bare garanteres for SSD-er levert av Hat Labs og offisielle Raspberry Pi-SSD-er. Hvis du vurderer en disk fra en tredjepart, bør du kontrollere at den er kompatibel med Raspberry Pi 5 før du kjøper den, ved å se på brukerrapporter og kompatibilitetslister på nettet. Vanlige problemer med inkompatible disker er for høyt strømforbruk, overoppheting og oppstartsfeil eller ustabilt system.

### Klargjøre den nye SSD-en

Før du monterer en ny SSD i HALPI2, bør operativsystemet flashes til disken. Det er mulig å flashe SSD-en etter monteringen med USB Boot-kontakten til CM5-en (j1), men det er enklere og raskere å bruke en ekstern USB-til-NVMe-adapter. Flasheprosedyren er beskrevet i [programvareveiledningen](./software.md).

### Deaktivere systemets 3,3 V-spenning

Superkondensatorene kan holde 3,3 V-skinnen på bærekortet strømsatt lenge etter at hovedstrømmen er koblet fra. Siden SSD-en får strøm fra 3,3 V-skinnen, må skinnen deaktiveres for å sikre at SSD-en er helt strømløs før den fjernes eller monteres.

Begynn med å slå av HALPI2 og koble fra strømforsyningen. Åpne kabinettet etter prosedyren i avsnittet om tilgang til kabinettet.

Finn «3.3V off»-jumperen på bærekortet. Plasseringen varierer med kortversjonen. På v0.4.0-kortene sitter jumperen svært nær superkondensatorene, på «sør»-siden av dem. På kort fra v0.5.0 og senere finner du pinnelisten «Pow.Ctrl» «øst» for superkondensatorene. «3.3V off»-pinnene er de to øverste på pinnelisten.

Flytt jumperen slik at den kortslutter «3.3V off»-pinnene. Det deaktiverer 3,3 V-skinnen, og LED-ene slukker.

### Demonteringsprosedyre

M.2-sporet sitter ved sørkanten av bærekortet. Se bildet i avsnittet [Kontakter på bærekortet](#carrier-board-connectors) for å finne M.2-kontakten merket **g1**.

Bruk en PH1-skrutrekker til å fjerne M2.5-monteringsskruen. Når skruen er fjernet, spretter SSD-en opp i en vinkel. Løft disken forsiktig i monteringsenden og vrikk den ut av M.2-kontakten. Hold SSD-en i kantene for å unngå å skade komponenter eller kontakter.

### Monteringsprosedyre

Sett den klargjorte SSD-en inn i M.2-kontakten i omtrent 30 graders vinkel, og pass på at hakket i SSD-en er rettet inn mot sporet i kontakten. Disken skal gli lett inn uten bruk av kraft. Når den sitter helt inne, trykker du monteringsenden av SSD-en ned til den ligger flatt mot avstandsbolten.

Fest SSD-en med M2.5-monteringsskruen ved hjelp av en PH1-skrutrekker. Trekk skruen bare så hardt til at disken sitter godt fast. SSD-en skal ligge helt flatt, uten synlig bøy.

Når SSD-en er på plass, fjerner du jumperen fra «3.3V off»-pinnene for å aktivere 3,3 V-skinnen igjen. La jumperen bli sittende på pinnelisten til senere bruk.

Sett kabinettet sammen igjen slik det er beskrevet i avsnittet om tilgang til kabinettet.
For programvarekonfigurasjon og feilsøking, se [programvareveiledningen](./software.md).

!!! quote "Relatert informasjon"
    - **Systembilder:** Se [Programvareveiledning](./software.md)
    - **Oppstartsprosedyrer:** Se [Systemdrift](./operation.md)
    - **Tilgang til maskinvaren:** Se [Tilgang til kabinettet](#enclosure-access)

## Bytte Compute Module 5

### Forutsetninger

Bytte av Compute Module 5 krever forsiktig håndtering fordi kort-til-kort-kontaktene er ømfintlige. CM5-en bruker to kontakter med høy tetthet som lett kan skades hvis det brukes for mye kraft eller feil teknikk. Demonter en eksisterende modul bare når det er helt nødvendig, for eksempel når modulen er skadet eller skal oppgraderes. Skader på monteringskontaktene for compute-modulen, enten på CM5-en eller på bærekortet, dekkes ikke av garantien.

Før du begynner, må du ha varmeledende puter tilgjengelig for varmeoverføring. Standardoppsettet bruker en 1 mm tykk pute på SoC-en og 2 mm tykke puter på RP1-brikken og de interne strømforsyningskomponentene. Eksisterende varmeledende puter kan gjenbrukes hvis de er hele og rene.

### Tilgang til Compute Module

Slå av HALPI2 og koble fra strømkilden. Ta av kabinettlokket etter prosedyren i avsnittet om tilgang til kabinettet. For å komme til CM5-en, som er montert på undersiden av bærekortet, må du først demontere bærekortet fra kabinettet. For å holde orden på de mange kablene som er koblet til bærekortet, anbefales det å ta noen bilder av forbindelsene før du går videre.

Koble fra kabler som hindrer at bærekortet kan løftes. Fjern monteringsskruene til bærekortet og løft kortet ut av kabinettet.

### Fjerne den eksisterende modulen

!!! danger "Forsiktig"
    Hvis CM5-modulen løsnes én kontakt av gangen, kan vridningskreftene rive kontakten av CM5-modulen. Denne skaden dekkes ikke av garantien.

CM5-en er festet med to kort-til-kort-kontakter som må håndteres forsiktig. Bruk aldri metallverktøy til dette, siden det kan skade kontaktene eller nærliggende overflatemonterte komponenter. Bruk et vippeverktøy av tre eller plast (plastspade), et gitarplekter eller et tilsvarende ikke-ledende verktøy.

Plasser verktøyet midt på den korte venstrekanten av CM5-modulen, mellom modulen og bærekortet. Trykk bestemt ned i hjørnene på høyre side. Vipp forsiktig oppover med minimal kraft – modulen skal løsne med et lett klikk, slik at begge kontaktene slipper samtidig.

![Unmounting CM5 Module](./unmount-cm5.jpg)
*Demonter CM5-modulen ved å trykke ned i hjørnene på høyre kant mens du vipper oppover midt på venstre kant. Begge kontaktene skal slippe samtidig.*

### Montere den nye modulen

Rett den nye CM5-modulen inn mot kontaktene på bærekortet, og bruk omrisset i silketrykket på bærekortet som veiledning. Modulomrisset som er trykt på bærekortet, skal stemme nøyaktig med de fysiske målene til CM5-en når modulen er riktig orientert.

Når modulen er rettet inn, trykker du forsiktig og jevnt der kontaktene sitter på begge kortsidene av modulen. Du skal kjenne at kontaktene griper med et lite klikk. Trykk bestemt, men unngå å bøye bærekortet – støtt kortet fra undersiden om nødvendig. Begge kontaktene må sitte helt inne for at systemet skal virke riktig.

Legg deretter varmeledende puter på CM5-modulen. Putene skal plasseres riktig: 1 mm pute på hoved-SoC-en, og 2 mm puter på RP1-brikken og strømforsyningskomponentene. Hvis du gjenbruker eksisterende puter, må du kontrollere at de er rene og riktig plassert.

![Thermal Pad Placement on CM5](./cm5-thermal-pads-annotated.jpg)
*Plassering av varmeledende puter på Compute Module 5. Bruk en 1 mm tykk pute på SoC-en (i midten) og 2 mm tykke puter på RP1 og strømforsyningskomponentene. De faktiske formene og størrelsene på putene kan variere.*

### Antennetilkobling

Før du monterer bærekortet tilbake, kobler du U.FL-antennekabelen til den trådløse antennekontakten på CM5-en. Denne forbindelsen er umulig å komme til når bærekortet er montert igjen. U.FL-kontakten krever nøyaktig innretting og et fast trykk for å sitte riktig. Du skal kjenne et tydelig knepp når kontakten er helt på plass. Vær forsiktig så du ikke bøyer kontakthuset under monteringen.

### Sluttmontering

Kontroller monteringen av modulen for å forsikre deg om at begge kontaktene sitter helt inne, og at modulen ligger flatt mot bærekortet uten glipe. De varmeledende putene skal ha kontakt med de varmeutviklende komponentene på modulen.

Sett bærekortet tilbake i kabinettet, og pass på at de varmeledende putene på CM5-en treffer de tilsvarende varmespredende flatene i bunnen av kabinettet. Monter alle monteringsskruene til bærekortet igjen og koble til kablene som ble frakoblet under demonteringen.

Fullfør sammensettingen etter den vanlige prosedyren for lukking av kabinettet. Ved første oppstart skal systemet kjenne igjen den nye CM5-en automatisk.

!!! warning "Advarsel om kontaktene"
    Kort-til-kort-kontaktene er de mest skjøre komponentene i denne prosedyren. Bruk aldri metallverktøy nær kontaktene, bruk bare vertikal kraft ved demontering og montering, og kontroller at innrettingen er helt riktig før du trykker. Skadde kontakter krever som regel at bærekortet byttes.

!!! quote "Relatert informasjon"
    - **Systemoppsett etter bytte:** Se [Programvareveiledning](./software.md)
    - **Feilsøking av oppstart:** Se [Feilsøking](./troubleshooting.md)
    - **Varmehåndtering:** Se [Maskinvarereferanse](../technical-reference/hardware.md)

---
translated_from: da8aa35c462e57bc7c0b00d50046a1df518e97dd
---

# Grensesnitt og tilkoblingsmuligheter

## CAN FD / NMEA 2000

HALPI2 har et fullstendig isolert [CAN FD](https://en.wikipedia.org/wiki/CAN_FD)-grensesnitt som støtter både maritime [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000)-nettverk og bruk i kjøretøy og industri. Grensesnittet gir datakommunikasjon med høy hastighet og fullstendig elektrisk isolasjon for god støyimmunitet.

### Spesifikasjoner for grensesnittet

CAN FD-grensesnittet støtter både vanlig CAN og CAN FD-protokollen. I NMEA 2000-sammenheng arbeider grensesnittet i vanlig CAN-modus med standard datahastighet på 250 kbps. Ved bruk i kjøretøy eller industri kan grensesnittet utnytte alle mulighetene i CAN FD, med datahastigheter opptil 8 Mbps.

Frontpanelet har en Micro-C-kontakt som er kompatibel med vanlig NMEA 2000-kabling og -komponenter. Det gir direkte integrasjon med eksisterende maritime nettverk ved hjelp av vanlige T-koblinger og stikkledninger.

### Strømkonfigurasjon og belastning av nettverket

Hvor mye HALPI2 belaster strømforsyningen i NMEA 2000-nettverket, avhenger av hvilken strømkonfigurasjon du velger. I standardkonfigurasjonen med ekstern strøm via E7T-kontakten trenger enheten ingen strøm fra NMEA 2000-nettverket, og Load Equivalency Number (LEN) blir dermed 0.

Når enheten skal få strøm fra NMEA 2000-bussen, må strømtrekket begrenses til 0,9 A med den innebygde strømbegrenseren. Det tilsvarer en LEN-verdi på 18. Når HALPI2 forsynes via NMEA 2000, bør enheten kobles til nettverkets backbone nær strøminnmatingskabelen for å holde spenningsfallet lavt og sikre pålitelig drift.

### Maskinvarekonfigurasjon

Bærekortet har en termineringsmotstand på 120 Ω som kan aktiveres med en jumper. Terminering i selve enheten bør unngås i NMEA 2000-sammenheng, siden standarden ikke tillater det. Ved bruk i kjøretøy eller industri der kommunikasjonen er punkt-til-punkt, kan jumperen derimot settes slik at termineringsmotstanden aktiveres.

For diagnostikk og feilsøking i nettverket har bærekortet egne RX- og TX-LED-er som viser nettverksaktivitet. Disse LED-ene gir umiddelbar visuell tilbakemelding om sending og mottak av data, slik at det blir enklere å finne årsaken til tilkoblingsproblemer.

### Nettverksinstallasjon

Tilkobling til NMEA 2000-nettverk skjer med en vanlig T-kobling (følger ikke med) montert på nettverkets backbone og en stikkledning mellom T-koblingen og Micro-C-kontakten på HALPI2.

### Programvareintegrasjon

CAN-grensesnittet er sømløst integrert i Linux gjennom SocketCAN-rammeverket og vises som nettverksenheten `can0`. Dette standardgrensesnittet gjør at du kan bruke vanlige CAN-verktøy i Linux til overvåking og diagnostikk. Nettverksgrensesnittet er ferdig konfigurert i alle systembildene til HALPI2 (HaLOS, OpenPlotter og Raspberry Pi OS).

Integrasjon med Signal K-serveren finnes i de maritime variantene av HaLOS-systembildet og i OpenPlotter. Den oppdager CAN-grensesnittet automatisk og bruker det til å behandle NMEA 2000-data. På HaLOS-systembilder som ikke er maritime, kan Signal K installeres fra Container Apps-butikken i Cockpit. Signal K-serveren dekoder PGN-er og gir webbasert tilgang til sanntidsdata fra nettverket.

### Feilsøking

Feilsøking i nettverket begynner med RX/TX-LED-ene på bærekortet. Ved normal drift blinker LED-ene i takt med nettverkstrafikken. Manglende RX-aktivitet kan tyde på feil i kablingen eller feil terminering, mens manglende TX-aktivitet kan tyde på konflikter i nettverket eller feil i kablingen.

Linux-kommandoen `candump` kan brukes til å overvåke CAN-bussen direkte fra kommandolinjen. Verktøyet gir detaljert informasjon om alle meldingene på bussen og gjør grundig diagnostikk mulig. I sin enkleste form kan du kjøre:

```bash
candump can0
```

Da vises alle innkommende rå CAN-meldinger i sanntid.

Dashbordet i Signal K-serveren gir flere muligheter for overvåking av nettverket. Det viser datahastighetene for NMEA 2000 fra CAN-grensesnittet i sanntid. Med Data Browser-verktøyet kan du se dekodede NMEA 2000-data.

!!! quote "Relatert informasjon"
    - **Strømkonfigurasjon:** Se [Kom i gang](../getting-started/getting-started.md#permanent-strminstallasjon)
    - **Programvareoppsett:** Se [Programvareveiledning](./software.md)
    - **Feilsøking i nettverket:** Se [Feilsøking](./troubleshooting.md)


## RS-485 (NMEA 0183)

HALPI2 har et isolert [RS-485](https://en.wikipedia.org/wiki/RS-485)-grensesnitt som gir seriekommunikasjon for maritime [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422]-nettverk og industrielle bruksområder.

[^rs422]: Teknisk sett bruker NMEA 0183 RS-422-standarden, men RS-485 er nedoverkompatibel, slik at HALPI2 kan kommunisere med både RS-422- og RS-485-enheter.

### Spesifikasjoner for grensesnittet

RS-485-transceiveren arbeider med hastigheter opptil 10 Mbps, men typiske NMEA 0183-bruksområder bruker standard baudrater på 4800 eller 38400 bps. Grensesnittet er galvanisk isolert og i samsvar med NMEA 0183-spesifikasjonen, og beskytter dermed HALPI2 mot jordsløyfer og elektrisk støy som er vanlig i maritime miljøer.

Grensesnittet er internt koblet til UART 4 på Raspberry Pi-en og vises som `/dev/ttyAMA4` i Linux. Denne standard serielle enheten kan brukes av alle programmer som støtter seriekommunikasjon, blant annet Signal K-serveren, OpenCPN og egenutviklet programvare.

### Maskinvarekonfigurasjon

Bærekortet har egne RX- og TX-LED-er som viser kommunikasjonsaktivitet på RS-485-grensesnittet. Disse LED-ene gir umiddelbar visuell tilbakemelding under installasjon og feilsøking, slik at det er enkelt å kontrollere at data sendes og mottas riktig.

Når enheten brukes som et generelt RS-485-grensesnitt, kan den settes opp med enten automatisk eller manuell aktivering av sending. I manuell modus styres sendeaktiveringssignalet av en GPIO-pinne, slik at programvaren bestemmer når grensesnittet sender og når det mottar. Dette kreves i multi-talker-nettverk der grensesnittet må være i resessiv tilstand når det ikke sender. I automatisk modus aktiverer maskinvaren selv sendesignalet når data sendes, noe som forenkler oppsettet i single-talker-nettverk.

I tillegg støtter RS-485-grensesnittet halv dupleks, slik at det kan både sende og motta på det samme lederparet.

Grensesnittet kan også deaktiveres helt med en maskinvareendring hvis UART 4 trengs til andre formål.

### Kabling og tilkobling

RS-485-grensesnittet krever en kabelgjennomføring eller en panelkontakt som du må skaffe selv. Et godt alternativ er [en SP13 pigtail-panelkontakt](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). Grensesnittet er nedoverkompatibelt med RS-422-signaleringen som brukes i NMEA 0183, og støtter både RS-485-nettverk med flere sendere (multi-talker) og RS-422-nettverk med én sender og flere lyttere (single-talker-multiple-listener). Det bruker balanserte differensialpar, merket TX+/TX- og RX+/RX-.

### Programvareintegrasjon

Alle systembildene til HALPI2 leveres ferdig konfigurert med RS-485-grensesnittet klart til bruk. På HaLOS Marine-systembilder og i OpenPlotter oppdager Signal K-serveren grensesnittet automatisk og tar imot NMEA 0183-data som sendes.

For egenutviklede programmer oppfører grensesnittet seg som en vanlig seriell port i Linux. Programmer kan åpne `/dev/ttyAMA4` og stille inn baudrate, databiter, stoppbiter og paritet slik det tilkoblede utstyret krever. Programmer i Python, Node.js og C/C++ når alle grensesnittet enkelt med vanlige biblioteker for seriekommunikasjon.

### Vanlige bruksområder

I maritime miljøer kobles RS-485-grensesnittet typisk til GPS-mottakere, ekkolodd, vindmålere, AIS-transpondere eller andre enheter som bruker NMEA 0183-protokollen. I industrien kan det være snakk om tilkobling til PLS-er, sensorer og annet automasjonsutstyr som bruker Modbus RTU eller andre RS-485-protokoller.

Den høye hastigheten grensesnittet takler, gjør det også egnet for bruk utenfor standarden, som innsamling av sensordata med høy oppdateringsfrekvens eller egne kommunikasjonsprotokoller. Det gjør HALPI2 aktuell for forskningsfartøy og spesialiserte overvåkingsoppgaver.

!!! quote "Relatert informasjon"
    - **Programvarekonfigurasjon:** Se [Programvareveiledning](./software.md)
    - **Feilsøking:** Se [Feilsøking](./troubleshooting.md)


## GNSS (GPS)

HALPI2 støtter GNSS-mottaker-HAT-er koblet til UART0 (`/dev/ttyAMA0`). Alle GNSS-mottakere på denne porten virker med gpsd uten videre oppsett.

For u-blox-mottakere (for eksempel Max-M8Q) gir HaLOS Marine-systembildene i tillegg en automatisk konfigurasjon som er optimalisert for maritim bruk.

### Automatisk konfigurasjon (u-blox-mottakere)

På HaLOS Marine-systembilder oppdager og konfigurerer en systemd-tjeneste (`configure-ublox-marine`) u-blox-mottakere automatisk ved hver oppstart:

| Parameter | Verdi |
|:----------|:------|
| Baudrate | 115200 bps (fabrikkstandard: 9600) |
| Oppdateringsfrekvens | 10 Hz (100 ms) |
| Dynamisk modell | Sea (optimalisert for maritim bruk) |

Konfigurasjonen kjøres ved hver oppstart fordi ROM-baserte u-blox-moduler (for eksempel MAX-M8Q) ikke har flashminne. Innstillingene lagres i batteribackup-RAM (BBR), som kan gå tapt hvis strømmen fra reservebatteriet brytes – for eksempel når enheten står uten strøm over lengre tid. Omkonfigureringen merkes ikke og legger omtrent 2 sekunder til oppstarten av gpsd.

Hvis ingen mottaker blir funnet, avslutter tjenesten uten melding. En nyinstallert GNSS-HAT blir konfigurert automatisk ved neste omstart.

### Tilgang til dataene

GPS-dataene leveres av [gpsd](https://gpsd.io/) på TCP-port 2947. På HaLOS Marine-systembilder kobler Signal K seg til gpsd automatisk – ingen ekstra konfigurasjon er nødvendig.

Til diagnostikk bruker du de vanlige kommandolinjeverktøyene til gpsd:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Systembilder uten HaLOS

På Raspberry Pi OS eller andre operativsystemer installerer og konfigurerer du gpsd manuelt:

```bash
sudo apt install gpsd gpsd-clients
```

Rediger `/etc/default/gpsd` slik at `DEVICES="/dev/ttyAMA0"` settes, og start tjenesten på nytt. Mottakeren kjører med fabrikkinnstillingene sine (9600 baud, 1 Hz) med mindre den konfigureres med `ubxtool` fra pakken `gpsd-clients`.

!!! quote "Relatert informasjon"
    - **gpsd på HaLOS:** Se [HaLOS GPS-dokumentasjon](https://docs.halos.fi/user-guide/gps/)
    - **Programvareoppsett:** Se [Programvareveiledning](./software.md)


## Ethernet

HALPI2 har et Gigabit Ethernet-grensesnitt som gir rask nettverkstilkobling for dataoverføring, fjerntilgang og integrasjon med nettverkene om bord. Ethernet-porten på bærekortet er en vanlig RJ45-kontakt. Den er ført ut til en panelkontakt som kan kobles til en ekstern Ethernet-kabel.

## USB

HALPI2 har til sammen fire USB 3.0 Type A-porter på kortet, som gir rask tilkobling av mange slags enheter og utstyr. Én port er ført direkte til USB 3.0-grensesnittet på CM5-en, mens de tre andre er koblet til via en USB 3-hub på kortet. I standardkonfigurasjonen er to av portene ført ut til frontpanelet, mens to er tilgjengelige på bærekortet for interne tilkoblinger.

## HDMI

HALPI2 har to HDMI 2.0-porter (HDMI0 og HDMI1) for videoutgang. Bærekortet har flatkabelkontakter (FFC) for begge HDMI-portene. De er ført ut til frontpanelet med spesiallagde FFC-kabler. Kontaktene på frontpanelet er vanlige HDMI Type A-kontakter.

HDMI-utgangen på HALPI2 støtter pålitelig to samtidige videostrømmer i Full HD (1080p). Videoutgang i 4K kan fungere, men er ikke garantert.

## MIPI (CSI/DSI)

Bærekortet har to MIPI CSI/DSI-kontakter for kamera- og skjermgrensesnitt. Kontaktene er 22-pinners flatkabelkontakter (FFC) med 0,5 mm senteravstand. De skal fungere som de er med nyere kameraer og skjermer som er kompatible med Raspberry Pi.

Av hensyn til vanntettheten bør FFC-kabler bare brukes til interne tilkoblinger.

## Eksterne knapper

HALPI2 har en 2×3-pinners pinneliste på bærekortet for tilkobling av eksterne knapper. Kabinettet har ingen innebygde knapper, slik at du selv kan velge plassering og type knapper etter behov.

### Pinnebelegg for knappepinnelisten

Bærekortet har en 6-pinners pinneliste med tre merkede knappefunksjoner:

| Merking | Funksjon | Beskrivelse |
|:------|:---------|:------------|
| Reset | Reset av kontrolleren | Maskinvarereset (RUN-pinnen på RP2040) |
| Power | Strøm til Raspberry Pi | Strømknapp for CM5 (PWR_BUT-inngangen) |
| User | Kan konfigureres av brukeren | Brukerdefinert hendelse (ikke implementert ennå) |

Hver knappetilkobling bruker to pinner: én for knappesignalet og én for jord. Bruk normalt åpne (NO) momentbrytere som forbinder signalpinnen med jord når de trykkes inn.

### Knappefunksjoner

**Resetknapp:**
Resetknappen gir en systemreset på maskinvarenivå ved å trekke RUN-pinnen på RP2040 lav. Det utfører en fullstendig systemreset som påvirker kontrolleren, CM5-en og alt tilkoblet utstyr. Resetknappen er særlig nyttig i nødssituasjoner der nedstenging fra programvaren har mislyktes og systemet har låst seg.

**Strømknapp:**
Strømknappen er koblet direkte til strømknappinngangen på CM5-en og virker akkurat som strømknappen på en Raspberry Pi 5. Et dobbeltklikk på strømknappen ber om en kontrollert nedstenging av systemet, slik at operativsystemet får avsluttet programmene og avmontert filsystemene før strømmen kuttes. Et langt trykk på strømknappen tvinger fram umiddelbar avslåing, og bør bare brukes når systemet har låst seg.

**Brukerknapp:**
Funksjonen til brukerknappen venter foreløpig på implementering i programvaren og vil gi funksjonalitet som brukeren kan konfigurere, i kommende firmwareversjoner. Når den er på plass, er knappen tenkt for egendefinerte handlinger og programspesifikke utløsere, slik at du kan bestemme hva knappen skal gjøre ut fra dine egne driftsbehov.

### Montering av knapper

#### Direkte montering i kabinettet

For direkte montering i HALPI2-kabinettet bruker du de ledige hullene på 6 mm eller 13 mm som allerede finnes i kabinettet. Begynn med å fjerne de aktuelle blindpluggene fra disse hullene, og monter en vanntett knappeenhet som passer til hulldiameteren. Koble knappen til pinnelisten på bærekortet med en egnet kabel, og sørg for god strekkavlastning og værtett tetting der kabelen går gjennom kabinettet.

#### Montering i eksternt panel

Når knappene monteres i et eksternt betjeningspanel, velger du et sted som er lett tilgjengelig og som samtidig holder værtettheten. Bruk kabelgjennomføringer der kablene går inn, og koble knappene med skjøtekabel med ledere på 22–26 AWG. Hold den samlede kabellengden under 3 meter for å bevare signalkvaliteten. I installasjoner som utsettes for fuktighet eller harde forhold, bruker du vanntette kontakter i skjøtepunktene for pålitelig drift over tid.

#### Tilkobling

Alle knappetilkoblinger til bærekortet bør bruke hunkontakter med 2,54 mm senteravstand. Kontroller at pinnene står riktig, og at forbindelsen sitter godt, for å unngå kontaktproblemer under drift.

!!! quote "Relatert informasjon"
    - **Strømstyring:** Se [Strømstyring og nedstengingsprosedyrer](./operation.md#strmstyring-og-nedstengingsprosedyrer)
    - **Tilgang til maskinvaren:** Se [Vedlikehold av maskinvaren](./hardware.md)

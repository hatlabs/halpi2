---
translated_from: a51e1cfe53d070c073a563641f9301fd3383a418
---

# Kom i gang

Denne veiledningen får HALPI2-en din i gang på under 30 minutter og dekker også permanent installasjon. Følg trinnene i rekkefølge for et så smidig oppsett som mulig – begynn med et oppsett på skrivebordet for å kontrollere at alt virker, og gå deretter videre til permanent installasjon.

## Sikkerhet og forholdsregler ved håndtering

!!! warning "Før du begynner"
    - Kontroller at strømmen er koblet fra det elektriske anlegget før du kobler til noe
    - Bruk egnede sikringer (3–5 A) for strømtilkoblinger
    - Håndter enheten forsiktig – den er robust, men fall eller støt kan skade interne komponenter
    - Kontroller at polariteten er riktig når du kobler til strømkabler
    - Unngå statiske utladninger – jord deg selv og unngå å gni katter og ravgjenstander før du berører interne komponenter

## Dette trenger du

Fra HALPI2-pakken:

- HALPI2-enhet med ferdig montert CM5 og NVMe SSD
- Strømkabel med E7T-kontakt (2 m lang)

Valgfritt tilbehør (følger med i salgspakken):

- Et par DC-plugger (barrel), 5,5 × 2,1 mm, ved bruk av en vanlig 12 V-strømadapter av «wall wart»-typen
- Raspberry Pi WiFi/Bluetooth-antenne (kreves hvis WiFi brukes ved det første oppsettet)

Ekstra utstyr (følger ikke med):

- 12 V- eller 24 V-strømkilde
- En egen datamaskin for oppsett uten skjerm (hvis du ikke bruker en tilkoblet skjerm)
- Nettverkskabel (valgfritt, for kablet tilkobling)
- Skjerm med HDMI-inngang (valgfritt)
- USB-tastatur og mus (valgfritt, for direkte tilgang)

!!! tip "Hurtigtips"
    Nettverksutstyr som rutere og WiFi-aksesspunkter bruker gjerne en 12 V-strømadapter som kan brukes til å forsyne HALPI2. Let i haugen med gammelt utstyr!

## Oppsett på skrivebordet

Vi anbefaler at du prøver HALPI2 på et skrivebord eller en arbeidsbenk før du installerer den permanent. Det første oppsettet kan gjøres enten uten skjerm (headless) over en nettverksforbindelse, eller med tilkoblet skjerm, tastatur og mus. Et oppsett uten skjerm kan gjøres enten med en kablet ethernetforbindelse eller med WiFi-aksesspunktet til HALPI2.

### Trinn 1: Koble til nødvendig utstyr

#### For det første oppsettet:

1. **Nettverksforbindelse (kreves ved installasjon uten skjerm):**
    - Koble til ethernetkabelen
    - Koble til WiFi/Bluetooth-antennen

2. **Skjermtilkobling (valgfritt):**
    - Koble til en HDMI-skjerm for direkte tilgang
    - USB-tastatur og mus hvis du bruker skjerm

![Kontakter på frontpanelet](./front-panel-connectors.jpg)
*Kontakter på frontpanelet*

### Trinn 2: NMEA 2000-tilkobling (valgfritt)

Hvis du installerer HALPI2 direkte i en båt eller har en NMEA 2000-installasjon tilgjengelig på skrivebordet, kan du allerede nå koble enheten til NMEA 2000-nettverket.

Et [NMEA 2000-nettverk](https://docs.hatlabs.fi/nmea2000/) består av en backbone-kabel som alle enheter kobles til med T-koblinger og stikkledninger. Sett en T-kobling på backbonen i NMEA 2000-nettverket. Koble NMEA 2000 micro-kontakten på HALPI2 til T-koblingen med en NMEA 2000-stikkledning.

### Trinn 3: Strømtilkobling

!!! tip "Om strømforsyning via NMEA 2000"
    HALPI2 kan også forsynes med strøm over NMEA 2000-bussen. Se [Strømtilkobling via NMEA 2000-bussen](#strmtilkobling-via-nmea-2000-bussen) i avsnittet om permanent installasjon nedenfor.

Til oppsettet på skrivebordet bruker vi den medfølgende E7T-strømkabelen. Koble ledningsendene på strømkabelen til hun-DC-pluggen slik:

- **Rød ledning = pluss (+)**
- **Svart ledning = minus (-)**

![E7T til DC-plugg](./e7t-barrel.jpg)
*Et eksempel på kablingen mellom E7T og DC-pluggen*

Koble en vanlig 12 V- eller 24 V-strømadapter til DC-pluggen. Kontroller at strømadapteren er dimensjonert for minst 1 A, slik HALPI2 krever.

!!! warning "Advarsel"
    Fordi DC-pluggen med skrueklemmer mangler strekkavlastning, bør den bare brukes til midlertidige installasjoner. Et utilsiktet drag i kabelen kan løsne den og blottlegge ledningene.

## Første oppstart

HALPI2 leveres med [HaLOS](https://docs.halos.fi), en containerbasert Linux-distribusjon med et webadministrert grensesnitt utviklet for maritime og industrielle bruksområder. Hvis du foretrekker et annet operativsystem, for eksempel OpenPlotter eller Raspberry Pi OS, se [Programvareveiledningen](../user-guide/software.md).

!!! info "HaLOS-dokumentasjon"
    Denne veiledningen dekker HALPI2-maskinvaren og den første oppstarten. Alt om operativsystemet – oppsett ved første oppstart, nettverk, apper, sertifikater og daglig bruk – finnes i **[HaLOS-dokumentasjonen](https://docs.halos.fi)**. Ha den for hånden mens du arbeider deg gjennom trinnene nedenfor.

**Slå på HALPI2** ved å koble til strømadapteren hvis du ikke allerede har gjort det. Etter noen sekunder
begynner LED-raden å fylles med røde lys, som viser at superkondensatorene lades. LED-ene blir gule når systemet starter opp, og til slutt grønne når operativsystemet kjører og HALPI-daemonen er koblet til kontrolleren.

Hvis du har en skjerm tilkoblet, skal du se oppstartsbildet til Raspberry Pi OS, og til slutt kommer et grafisk skrivebord fram.

!!! tip "Tips"
    Mønstrene for status-LED-ene er dokumentert i [driftsveiledningen](../user-guide/operation.md).

### Tilgang til HALPI2 uten skjerm

Hvis du ikke har en skjerm tilkoblet, kan du nå HALPI2 via WiFi-aksesspunktet eller en ethernetforbindelse. HaLOS gir et webbasert grensesnitt – ingen ekstra programvare er nødvendig[^ssh].

[^ssh]: SSH er også tilgjengelig på HaLOS-systembilder uten skjerm (aktivert som standard). På Desktop-varianter aktiverer du SSH med `raspi-config`. Standard påloggingsinformasjon: brukernavn `pi`, passord `halos`.

Vent først til LED-ene blir grønne, som viser at systemet har startet helt opp. Følg deretter disse trinnene:

**Alternativ 1 – Koble til via WiFi-aksesspunktet:** HaLOS oppretter et WiFi-aksesspunkt som heter `Halos-XXXX` (unikt per enhet) med passordet `halos1234`. Koble datamaskinen din til dette nettverket.

Aksesspunktet har ingen egen internettforbindelse, så neste trinn er å peke HALPI2 mot et WiFi-nettverk som har det (nødvendig for å laste ned containerappene ved første oppstart):

1. Åpne Cockpit på `https://halos.local:9090/` og logg på (brukernavn `pi`, passord `halos`).
2. Gå til **Networking** og klikk på **WiFi (wlan0)**.
3. Vent til listen over tilgjengelige nettverk kommer fram, og klikk så på nettverket ditt.
4. Skriv inn passordet og klikk på **Add**.

HALPI2 holder aksesspunktet `Halos-XXXX` oppe mens den kobler seg til nettverket ditt, så datamaskinen din kan falle av aksesspunktet et kort øyeblikk og koble seg til igjen av seg selv.

**Alternativ 2 – Koble til med kablet ethernet:** Hvis du har koblet HALPI2 til nettverket ditt med ethernet, får den automatisk en IP-adresse via DHCP.

Når du er tilkoblet, åpner du en nettleser og går til:

- **Dashboard:** `https://halos.local/` – hoveddashbordet i Homarr med lenker til alle installerte applikasjoner
- **Systemadministrasjon:** `https://halos.local:9090/` – Cockpit for systemstyring, oppdateringer og containerapper

!!! note "Advarsel om SSL-sertifikat"
    Første gang du åpner dashbordet eller Cockpit, viser nettleseren en advarsel om at forbindelsen ikke er sikker («Not secure»). HaLOS signerer webtjenestene sine med en sertifikatutsteder (CA) som enheten genererer selv, og nettleseren din stoler ikke på den CA-en ennå. Godta advarselen for å gå videre inntil videre.

    For å bli kvitt advarselen for godt installerer du CA-en til enheten på datamaskinen din én gang – etterpå validerer alle HaLOS-tjenester rent på alle porter. Åpne `https://halos.local/ca/` for et veiledet installasjonsprogram for hver plattform, eller se [Stol på enheten](https://docs.halos.fi/user-guide/trust-the-device/) i HaLOS-dokumentasjonen.

!!! info "Internett kreves ved første oppstart"
    Cockpit-grensesnittet er tilgjengelig med én gang, men hoveddashbordet og de andre containerbaserte applikasjonene trenger en internettforbindelse ved første oppstart for å laste ned containerbildene sine. Koble HALPI2 til internett med ethernet, eller konfigurer WiFi gjennom Cockpit.

### Konfigurasjon ved første oppstart

!!! warning "Advarsel"
    HaLOS leveres med standardpassord som **må** endres under den første oppstarten for å hindre uautorisert tilgang til enheten din.

HaLOS har to sett med påloggingsinformasjon:

| Tilgangstype | Brukernavn | Standardpassord | Brukes til |
|:------------|:---------|:-----------------|:---------|
| SSO (webapper) | `admin` | `halos` | Dashboard, Signal K, Grafana og andre webapplikasjoner |
| System (SSH/Cockpit) | `pi` | `halos` | SSH-tilgang, systemadministrasjon i Cockpit |

#### Endre passord

- **SSO-passord:** Endres via Authelia (som du når fra dashbordet)
- **Systempassord:** Endres via Cockpit (`https://halos.local:9090/`) under innstillingene for brukerkontoen, eller via SSH med `passwd`

Detaljerte instruksjoner for den første oppstarten finner du i [HaLOS-veiledningen Kom i gang](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Bruker du OpenPlotter eller Raspberry Pi OS?"
    Hvis du har flashet et annet operativsystem, se [Programvareveiledningen](../user-guide/software.md#frste-systemkonfigurasjon) for konfigurasjonsinstruksjoner som gjelder det operativsystemet.

### Kontrollere NMEA 2000-tilkoblingen (valgfritt)

NMEA 2000-tilkoblingen kontrolleres enklest ved å se på statusen til Signal K-serveren. På Marine-variantene av HaLOS-systembildet er Signal K ferdig installert og tilgjengelig fra dashbordet på `https://halos.local/`. For HaLOS-systembilder som ikke er maritime, kan Signal K installeres fra Container Apps-butikken i Cockpit.

Åpne Signal K-webgrensesnittet og se på aktiviteten på `can0`-forbindelsen: du skal se at det mottas noe trafikk.

![Aktivitet på tilkoblingene til Signal K-serveren](./sk-n2k-deltas.jpg)

## Slå av enheten

HALPI2 er laget for å slå seg av automatisk når den kobles fra strømforsyningen. Når du trenger å slå av enheten, kutter du rett og slett strømmen, enten med en bryter på det elektriske panelet eller ved å koble fra strømkontakten. Systemet starter da automatisk en programvarestyrt nedstengingssekvens, som sørger for at alle applikasjoner avsluttes på riktig måte og at filsystemet avmonteres trygt.

Hvis du velger å slå av systemet fra skrivebordsgrensesnittet eller med kommandolinjeverktøy (for eksempel kommandoen `shutdown`), starter enheten automatisk igjen etter omtrent 5 sekunder. Denne oppførselen skyldes at strømstyringssystemet oppdager at ekstern strøm fortsatt er tilgjengelig.

Under nedstengingen kan du følge systemstatusen med LED-indikatorene på frontpanelet. Når strømmen først kuttes, dempes de grønne LED-ene for å vise at det er et strømbrudd. Etter 5 sekunder skifter LED-ene til lilla, som gir en tydelig visuell bekreftelse på at enheten holder på å slå seg av. Når nedstengingen er fullført, slukker alle LED-ene.

Nedstengingen tar vanligvis bare noen få sekunder under normale forhold. I noen tilfeller kan enkelte tjenester likevel trenge ekstra tid for å stoppe på riktig måte. Skjer det, kan enheten tømme superkondensatorene nesten helt før den slår seg av. Denne forlengede nedstengingstiden er normal oppførsel og betyr ikke at det er noe galt med systemet.

## Feilsøking av problemer ved oppstart

### Vanlige og uvanlige problemer:

❌ **Ingen strøm / ingen LED-er:**

- Kontroller strømtilkoblingene og polariteten
- Sjekk tilstanden til sikringen
- Kontroller at spenningen er innenfor området 11–32 V

❌ **WiFi-aksesspunktet er ikke synlig:**

- Kontroller at antennen er ordentlig tilkoblet
- Prøv å koble til med en annen enhet
- Kontroller om HALPI2 har startet helt opp (LED-ene skal være grønne)
- Prøv å koble til med ethernet først

❌ **Får ikke tilgang til enheten med `halos.local`:**

- Prøv å bruke den tildelte IP-adressen i stedet (se DHCP-klientlisten i ruteren din)

❌ **Skjerm tilkoblet, men viser ingenting:**

- Kontroller at HDMI-kabelen sitter godt
- Kontroller at skjermen er slått på og satt til riktig inngang
- Prøv en annen HDMI-kabel eller en annen port på skjermen
- Kontroller at HALPI2 er på (LED-ene skal være gule eller grønne)
- Hvis LED-ene blinker i et regnbuemønster, sitter ikke Compute Module 5 riktig. Det kan skyldes transportskade. Følg instruksjonene i [brukerveiledningen](../user-guide/operation.md) for å montere CM5-en på nytt, eller kontakt støtte for hjelp.

❌ **Tilkoblet skjerm viser en feilmelding om «nvme»:**

- Dette betyr at NVMe SSD-en ikke blir oppdaget eller ikke er riktig initialisert. Det kan skyldes transportskade. Følg instruksjonene i [brukerveiledningen](../user-guide/operation.md) for å montere NVMe SSD-en på nytt, eller kontakt støtte for hjelp.

### Slik får du hjelp:

- **Dokumentasjon:** Se de aktuelle kapitlene for detaljert feilsøking
- **Fellesskap:** Bli med i fellesskapsforumene til Hat Labs
- **Støtte:** Kontakt teknisk støtte ved maskinvareproblemer

---

## Permanent installasjon

Når du har kontrollert at alt virker på skrivebordet, følger du disse trinnene for permanent montering og kabling.

### Planlegge installasjonen

!!! tip "Hurtigtips"
    Ta bilder av den eksisterende kablingen før du gjør endringer – det hjelper når du skal feilsøke senere.

Ta deg tid til å planlegge installasjonen. Tenk gjennom:

- **Monteringssted** – tilgjengelighet, beskyttelse, ventilasjon
- **Kabelføring** – korteste strekk, beskyttelse mot skade
- **Strømkilde** – egen kurs eller delt kurs, krav til sikring
- **Nettverksintegrasjon** – NMEA 2000, ethernet, WiFi-dekning
- **Miljøforhold** – temperatur, fuktighet, vibrasjon

#### Nødvendige verktøy og materialer

**Verktøy:**

- Drill med bor
- Skrutrekkersett (PH2 Phillips, stor flat)
- Avisoleringstang og krimptang for strømtilkoblingene
- Multimeter til testing
- Varmepistol eller lighter (for krympestrømpe)

**Materialer (følger ikke med):**

- Monteringsskruer (4 mm eller M4, avhengig av monteringsflaten)
- Egnede sikringer (3–5 A) eller automatsikringer med tilsvarende merkestrøm i det elektriske panelet
- Kabel av marin kvalitet (1,5 mm² eller 16 AWG til strøm, hvis den medfølgende kabelen er for kort)
- Krympestrømpe og kabelsko
- Kabelstrips og monteringsklips

### Montering

#### Valg av plassering

Velg et monteringssted som gir:

!!! tip "Optimale monteringsforhold"
    - **Temperaturområde:** −20 °C … +60 °C omgivelsestemperatur
    - **Ventilasjon:** Tilstrekkelig klaring rundt kabinettet
    - **Beskyttelse:** Unna direkte vannsprut og mekanisk skade
    - **Tilgang:** Enkel tilgang til kontakter og status-LED-er
    - **Bæreevne:** Solid monteringsflate som tåler 2 kg pluss kabler
    - **Plass:** La det være minst 100 mm klaring foran panelkontaktene til kabelhåndtering.

Selv om denne veiledningen tar for seg faste installasjoner, holder det i praksis ofte å sette enheten på en hylle eller et bord, så lenge den står stødig og er beskyttet mot fuktighet og støt.

#### Retningslinjer for omgivelsene

**Maritime installasjoner:**

- Monter over forventet nivå for lensevann
- Unngå steder med direkte sprut eller stående vann
- Ta hensyn til bevegelse og vibrasjon i båten, og sikre alle forbindelser
- Bruk korrosjonsbestandig monteringsmateriell

**Installasjoner i kjøretøy:**

- Beskytt mot motorvarme og vibrasjon
- Sørg for tilstrekkelig ventilasjon i lukkede rom
- Tenk på tilgjengelighet for vedlikehold
- Bruk vibrasjonsbestandig montering

**Industrielle installasjoner:**

- Beskytt mot prosesskjemikalier og ekstreme temperaturer
- Ta hensyn til kilder til elektromagnetisk støy
- Sørg for samsvar med lokale elektroforskrifter
- Planlegg for tilgang ved rutinemessig vedlikehold

#### Monteringsretning

!!! info "Anbefalt orientering"
    **Foretrukket:** Kontaktene vender nedover

    - Reduserer faren for vanninntrengning
    - Gir bedre kabelhåndtering
    - Enklere tilgang for vedlikehold

    **Akseptabelt:** Kontaktene vender sidelengs

    - Sørg for tilstrekkelig drenering
    - Bruk tetninger ved kabelinnføringene

    **Unngå:** Kontaktene vender oppover

    - Øker faren for vanninntrengning
    - Gjør kabelhåndteringen vanskelig

#### Monteringstrinn

##### Trinn 0: Last ned og skriv ut boremalen

Last ned [boremalen for HALPI2](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) og skriv den ut i 100 % skala. Denne malen hjelper deg med å merke av monteringshullene nøyaktig. Hvis du ikke har tilgang til en skriver, kan du også bruke målene i malen til å merke av hullene manuelt, eller bruke selve kabinettet til å merke hullene direkte på monteringsflaten.

[![Boremal](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Trinn 1: Klargjør monteringsflaten

1. **Rengjør monteringsflaten**
2. **Merk av monteringshullene** med den utskrevne malen
3. **Prøvemonter** kabinettet før installasjonen
4. **Forbor hullene** for monteringsskruene

##### Trinn 2: Monter HALPI2

1. **Plasser kabinettet** med kontaktene i foretrukket retning
2. **Skru inn monteringsskruene** – godt til, men ikke overstram

### Permanent strøminstallasjon

#### Valg av strømkilde

**Alternativ 1: Egen strømkontakt**

- Mest pålitelig og fleksibelt
- Støtter full effektkapasitet
- Enklere vedlikehold og feilsøking

**Alternativ 2: Strøm fra NMEA 2000-bussen**

- Forenkler kablingen i maritime installasjoner
- Begrenset til 0,9 A strømuttak
- Krever nøye oppmerksomhet på spenningsfall

#### Konfigurasjon av strømbegrensning

HALPI2 har en innebygd strømbegrenser på inngangen som styrer den første oppladingen av superkondensatorene og beskytter installasjonen mot overstrøm. Strømgrensen kan settes til enten 0,9 A eller 2,5 A, avhengig av strømkilden din og kravene i bruken. Standardinnstillingen på 0,9 A passer til de fleste bruksområder.

Hvis du vil øke oppstartshastigheten i begynnelsen eller trenger å forsyne utstyr med høyt strømforbruk, kan du bytte til innstillingen 2,5 A. Følg trinnene i [brukerveiledningen](../user-guide/operation.md) for å endre innstillingen for strømgrensen.

#### Egen strømtilkobling

##### Klargjøring av kabelen

1. **Legg strømkabelen** fra HALPI2 til strømkilden
2. **La det være servicesløyfer** i begge ender
3. **Beskytt kabelen** mot gnag og skade
4. **Kapp til lengde**, og la det være nok arbeidsrom

##### Tilkobling ved strømkilden

1. **Sørg for ledningsbeskyttelse** ved å sette av en automatsikring på 3–5 A eller montere en linjesikring
2. **Avisoler ledningsendene** til passende lengde
3. **Monter kabelsko** med riktig krimpeteknikk
4. **Koble til strømkilden:**
    - **Rød ledning:** plussterminal (+)
    - **Svart ledning:** minusterminal (-)
5. **Kontroller polariteten** med multimeteret før du slår på spenningen

##### Tilkobling ved HALPI2

E7T-kontakten er ferdig kablet og krever ingen terminering på stedet. Bare koble den til strømkontakten på HALPI2.

#### Strømtilkobling via NMEA 2000-bussen

!!! info "Forutsetninger"
    - Strømbegrensningsbryteren **må** stå på 0,9 A
    - NMEA 2000-nettverket må ha nok strømkapasitet
    - Stikkledningen bør være nær strøminnmatingen for å begrense spenningsfallet

##### Nødvendige komponenter

- NMEA 2000-stikkledning (følger ikke med)
- T-kobling for tilkobling til backbonen (følger ikke med)

##### Installasjonstrinn

1. **Slå av strømmen** til alle NMEA 2000-enheter
2. **Åpne HALPI2-kabinettet** (se [brukerveiledningen](../user-guide/operation.md) for instruksjoner)
3. **Finn strømkontakten på bærekortet**
4. **Koble fra den eksisterende koblingsklemmen**
5. **Koble den interne koblingsklemmen for NMEA 2000-strøm** til strømkontakten på bærekortet
6. **Kontroller at strømgrensen** er satt til 0,9 A
7. **Koble til backbonen** med egnet stikkledning og T-kobling
8. **Test installasjonen** før du lukker kabinettet
9. **Sett kabinettet sammen igjen**

![Strømkabling for NMEA 2000](./n2k-power-conx.jpg)
*For å forsyne HALPI2 med strøm over NMEA 2000 kobler du fra koblingsklemme 1 og setter inn koblingsklemme 2 i stedet.*

### Nettverks- og datatilkoblinger

#### NMEA 2000-datatilkobling

Selv når du bruker en egen strømtilkobling, vil du kanskje ha datatilkobling til NMEA 2000:

1. **Monter en T-kobling** på NMEA 2000-backbonen
2. **Koble en stikkledning** mellom T-koblingen og HALPI2
3. **Kontroller at NMEA 2000-nettverket** er riktig terminert
4. **Test forbindelsen** etter installasjonen

#### Ethernet-tilkobling

For nettverkstilkobling:

1. **Bruk kabel av marin kvalitet** eller kabel som er egnet for omgivelsene
2. **Monter kabelgjennomføringer eller gummigjennomføringer** hvis kabelen går gjennom skott
3. **La det være servicesløyfer** i begge ender
4. **Test forbindelsen** før den endelige installasjonen

#### WiFi/Bluetooth-antenne

1. **Monter antennen** på RP-SMA-kontakten
2. **Plasser den for best mulig dekning** – unna hindringer av metall. I metallskap kan det være nødvendig med en RP-SMA-skjøtekabel med hann- og hunkontakt.
3. **Test signalstyrken** i den endelige plasseringen

### Feilsøking av installasjonsproblemer

#### Strømproblemer

❌ **Ingen indikasjon på strøm:**

- Sjekk tilstanden til sikringen og merkestrømmen
- Kontroller spenningen fra strømkilden (11–32 V)
- Bekreft at polariteten er riktig
- Test gjennomgangen i strømkablene

❌ **Ustabil strømtilførsel:**

- Sjekk at alle forbindelser sitter godt
- Se etter korroderte terminaler
- Kontroller at ledertverrsnittet er stort nok for strømmen

#### Nettverkstilkobling

❌ **Ingen NMEA 2000-kommunikasjon:**

- Kontroller termineringen av nettverket (120 Ω i begge ender)
- Sjekk monteringen av T-koblingen
- Bekreft at stikkledningen er hel
- Test med en enhet du vet fungerer

❌ **Ingen ethernetforbindelse:**

- Test kabelen med en kabeltester
- Kontroller konfigurasjonen av svitsjen eller ruteren
- Se etter konflikter mellom IP-adresser
- Bekreft kabelklassen (minst Cat5e)

#### Problemer med omgivelsene

❌ **Fuktinntrengning:**

- Kontroller tilstanden til alle tetninger
- Kontroller retningen på kontaktene
- Sjekk kabelinnføringene
- Vurder ekstra beskyttelse

❌ **Overoppheting:**

- Flytt enheten bort fra varmekilder
- Se etter hindringer for luftstrømmen rundt kabinettet

### Sikkerhet og samsvar

#### Elektrisk sikkerhet

- **Bruk egnede sikringer** som beskyttelse mot overstrøm
- **Sørg for riktig jording** etter lokale forskrifter
- **Beskytt mot kortslutning** med riktig kabelføring

#### Maritime installasjoner

- **Følg lokale standarder eller ABYC-standarder** for elektriske installasjoner
- **Bruk komponenter av marin kvalitet** overalt

#### Industrielle installasjoner

- **Følg lokale elektroforskrifter**
- **Sørg for riktig EMI/RFI-beskyttelse**
- **Dokumenter installasjonen** etter kravene på stedet

## Neste steg

Når HALPI2-en din er i gang:

1. **Utforsk [brukerveiledningen](../user-guide/operation.md)** for detaljerte driftsinstruksjoner
2. **Se gjennom vanlige bruksområder** for oppsett tilpasset bruken
3. **Ta en titt på den tekniske referansen** for avanserte konfigurasjonsmuligheter
4. **Bli med i fellesskapet** for tips, triks og støtte

---
translated_from: a51e1cfe53d070c073a563641f9301fd3383a418
---

# Kom godt i gang

Denne vejledning får din HALPI2 op at køre på under 30 minutter og dækker også den permanente installation. Følg trinnene i rækkefølge for den nemmeste opsætning — start med en opsætning på skrivebordet for at kontrollere, at alt virker, og gå derefter videre til den permanente installation.

## Sikkerhed og håndtering

!!! warning "Før du begynder"
    - Sørg for, at strømmen er afbrudt i dit elsystem, før du laver tilslutninger
    - Brug passende sikringer (3–5 A) til strømtilslutninger
    - Håndtér enheden forsigtigt — den er robust, men fald og stød kan beskadige interne komponenter
    - Kontrollér polariteten, når du tilslutter strømkabler
    - Undgå statiske udladninger — jord dig selv, og lad være med at gnide katte og ravgenstande, før du rører ved interne komponenter

## Det skal du bruge

Fra din HALPI2-pakke:

- HALPI2-enhed med formonteret CM5 og NVMe SSD
- Strømkabel med E7T-stik (længde 2 m)

Valgfrit tilbehør (følger med i salgspakken):

- Par af DC-jackstik (barrel) (5,5 × 2,1 mm), hvis du bruger en almindelig 12 V-netadapter
- Raspberry Pi-antenne til WiFi og Bluetooth (påkrævet, hvis WiFi bruges til den første opsætning)

Yderligere udstyr (medfølger ikke):

- 12 V- eller 24 V-strømkilde
- En separat computer til opsætning uden skærm (headless), hvis du ikke tilslutter en skærm
- Netværkskabel (valgfrit, til kablet forbindelse)
- Skærm med HDMI-indgang (valgfrit)
- USB-tastatur og -mus (valgfrit, til direkte adgang)

!!! tip "Hurtigt tip"
    Netværksudstyr som routere og WiFi-adgangspunkter bruger ofte en 12 V-strømforsyning, som kan forsyne HALPI2. Kig i bunken af gammelt udstyr efter en!

## Opsætning på skrivebordet

Vi anbefaler, at du prøver HALPI2 på et skrivebord eller en arbejdsbænk, før du installerer den permanent. Den første opsætning kan foretages enten uden skærm (headless) via en netværksforbindelse eller med tilsluttet skærm, tastatur og mus. En opsætning uden skærm kan bruge enten en kablet ethernetforbindelse eller HALPI2's WiFi-adgangspunkt.

### Trin 1: Tilslut nødvendige perifere enheder

#### Til den første opsætning:

1. **Netværksforbindelse (påkrævet ved installation uden skærm):**
    - Tilslut et ethernetkabel
    - Tilslut WiFi-/Bluetooth-antennen

2. **Skærmtilslutning (valgfrit):**
    - Tilslut en HDMI-skærm for direkte adgang
    - USB-tastatur og -mus, hvis du bruger skærm

![Frontpanelets stik](./front-panel-connectors.jpg)
*Frontpanelets stik*

### Trin 2: NMEA 2000-tilslutning (valgfrit)

Hvis du installerer HALPI2 direkte i en båd eller har en NMEA 2000-opstilling på skrivebordet, kan du allerede nu slutte den til NMEA 2000-netværket.

Et [NMEA 2000-netværk](https://docs.hatlabs.fi/nmea2000/) består af et backbone-kabel, som alle enheder tilsluttes via T-stik og dropkabler. Sæt et T-stik på NMEA 2000-netværkets backbone. Slut HALPI2's NMEA 2000-Micro-stik til T-stikket med et NMEA 2000-dropkabel.

### Trin 3: Strømtilslutning

!!! tip "Om forsyning via NMEA 2000"
    HALPI2 kan også forsynes via NMEA 2000-bussen. Se [Strømtilslutning via NMEA 2000-bussen](#strmtilslutning-via-nmea-2000-bussen) i afsnittet om permanent installation nedenfor.

Til opsætningen på skrivebordet bruger vi det medfølgende E7T-strømkabel. Slut strømkablets ledere til DC-jackstikket (hunstik) sådan her:

- **Rød leder = plus (+)**
- **Sort leder = minus (-)**

![E7T til DC-jackstik](./e7t-barrel.jpg)
*Et eksempel på ledningsføringen fra E7T til DC-jackstikket*

Sæt en almindelig 12 V- eller 24 V-strømforsyning i DC-jackstikket. Sørg for, at strømforsyningen kan levere mindst 1 A, så den kan dække HALPI2's behov.

!!! warning "Advarsel"
    DC-jackstikket med skrueklemmer har ingen trækaflastning og bør derfor kun bruges til midlertidige installationer. Et uheldigt ryk i kablet kan løsne lederne og blotlægge dem.

## Første opstart

HALPI2 leveres med [HaLOS](https://docs.halos.fi), en containerbaseret Linux-distribution med en webadministreret grænseflade, der er udviklet til marine og industrielle anvendelser. Hvis du foretrækker et andet styresystem som OpenPlotter eller Raspberry Pi OS, kan du se [Softwarevejledningen](../user-guide/software.md).

!!! info "HaLOS-dokumentationen"
    Denne vejledning dækker HALPI2's hardware og den første opstart. Alt om styresystemet — opsætning ved første opstart, netværk, apps, certifikater og daglig brug — findes i **[HaLOS-dokumentationen](https://docs.halos.fi)**. Hav den ved hånden, mens du gennemgår trinnene nedenfor.

**Tænd for HALPI2** ved at tilslutte strømforsyningen, hvis du ikke allerede har gjort det. Efter et par sekunder
begynder LED-bjælken at fyldes op med rødt lys, hvilket viser, at superkondensatorerne oplader. LED'erne bliver gule, når systemet starter, og til sidst grønne, når styresystemet kører, og HALPI-dæmonen har forbindelse til controlleren.

Hvis du har en skærm tilsluttet, ser du Raspberry Pi OS-startskærmen, og til sidst kommer et grafisk skrivebord frem.

!!! tip "Tip"
    Status-LED'ernes mønstre er beskrevet i [Systemdrift](../user-guide/operation.md).

### Adgang til HALPI2 uden skærm

Hvis du ikke har en skærm tilsluttet, kan du få adgang til HALPI2 via dens WiFi-adgangspunkt eller en ethernetforbindelse. HaLOS har en webbaseret grænseflade — der er ikke brug for yderligere software[^ssh].

[^ssh]: SSH er også tilgængelig på HaLOS-images uden skærm (aktiveret som standard). På Desktop-varianterne aktiverer du SSH via `raspi-config`. Standardloginoplysninger: brugernavn `pi`, adgangskode `halos`.

Vent først, til LED'erne bliver grønne, hvilket betyder, at systemet er startet helt op. Følg derefter disse trin:

**Mulighed 1 — forbindelse via WiFi-adgangspunktet:** HaLOS opretter et WiFi-adgangspunkt med navnet `Halos-XXXX` (unikt for hver enhed) og adgangskoden `halos1234`. Slut din computer til dette netværk.

Adgangspunktet har ingen internetforbindelse af sig selv, så næste trin er at pege HALPI2 mod et WiFi-netværk, der har en (nødvendigt for at hente containerapps ved første opstart):

1. Åbn Cockpit på `https://halos.local:9090/`, og log ind (brugernavn `pi`, adgangskode `halos`).
2. Gå til **Networking**, og klik på **WiFi (wlan0)**.
3. Vent, til listen over tilgængelige netværk vises, og klik derefter på dit netværk.
4. Indtast adgangskoden, og klik på **Add**.

HALPI2 holder adgangspunktet `Halos-XXXX` oppe, mens den kobler sig på dit netværk, så din computer kan miste forbindelsen til adgangspunktet et kort øjeblik og selv oprette den igen.

**Mulighed 2 — forbindelse via kablet ethernet:** Hvis du har sluttet HALPI2 til dit netværk via ethernet, får den automatisk en IP-adresse via DHCP.

Når forbindelsen er oprettet, skal du åbne en browser og gå til:

- **Dashboard:** `https://halos.local/` — det primære Homarr-dashboard med links til alle installerede applikationer
- **Systemadministration:** `https://halos.local:9090/` — Cockpit til systemstyring, opdateringer og containerapps

!!! note "Advarsel om SSL-certifikat"
    Første gang du åbner dashboardet eller Cockpit, viser din browser advarslen »Not secure«. HaLOS signerer sine webtjenester med en certifikatmyndighed (CA), som enheden selv genererer, og din browser stoler ikke på den CA endnu. Accepter advarslen for at komme videre indtil videre.

    Du fjerner advarslen permanent ved at installere enhedens CA på din computer én gang — derefter validerer alle HaLOS-tjenester rent på alle porte. Åbn `https://halos.local/ca/` for at få en guidet installation til din platform, eller se [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) i HaLOS-dokumentationen.

!!! info "Internetforbindelse kræves ved første opstart"
    Cockpit-grænsefladen er tilgængelig med det samme, men det primære dashboard og de øvrige containerbaserede applikationer kræver en internetforbindelse ved første opstart for at kunne hente deres containerimages. Slut HALPI2 til internettet via ethernet, eller konfigurer WiFi i Cockpit.

### Konfiguration ved første opstart

!!! warning "Advarsel"
    HaLOS leveres med standardadgangskoder, som **skal** ændres ved den første opstart for at forhindre uautoriseret adgang til din enhed.

HaLOS har to sæt loginoplysninger:

| Adgangstype | Brugernavn | Standardadgangskode | Bruges til |
|:------------|:---------|:-----------------|:---------|
| SSO (webapps) | `admin` | `halos` | Dashboard, Signal K, Grafana og andre webapplikationer |
| System (SSH/Cockpit) | `pi` | `halos` | SSH-adgang, systemadministration i Cockpit |

#### Ændring af adgangskoder

- **SSO-adgangskode:** Ændres via Authelia (som du når fra dashboardet)
- **Systemadgangskode:** Ændres via Cockpit (`https://halos.local:9090/`) under indstillingerne for brugerkontoen eller via SSH med `passwd`

Du finder detaljerede anvisninger til den første opstart i [HaLOS' Kom godt i gang-vejledning](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Bruger du OpenPlotter eller Raspberry Pi OS?"
    Hvis du har flashet et andet styresystem, kan du se [Softwarevejledningen](../user-guide/software.md#indledende-systemkonfiguration) for konfigurationsanvisninger til det pågældende styresystem.

### Kontrol af NMEA 2000-forbindelsen (valgfrit)

NMEA 2000-forbindelsen kontrolleres nemmest ved at se på status for Signal K-serveren. På HaLOS Marine-imagevarianterne er Signal K forudinstalleret og tilgængelig fra dashboardet på `https://halos.local/`. På HaLOS-images uden marint indhold kan Signal K installeres fra Container Apps-butikken i Cockpit.

Åbn Signal K-webgrænsefladen, og hold øje med aktiviteten på forbindelsen `can0`: der bør være noget trafik, som bliver modtaget.

![Aktivitet på Signal K-serverens forbindelser](./sk-n2k-deltas.jpg)

## Sådan lukker du enheden ned

HALPI2 er lavet til at lukke ned automatisk, når strømforsyningen afbrydes. Når du vil lukke enheden ned, afbryder du blot strømmen — enten med en kontakt på eltavlen eller ved at trække strømstikket ud. Systemet starter automatisk en softwarestyret nedlukning, så alle applikationer lukker korrekt, og filsystemet afmonteres sikkert.

Hvis du vælger at lukke systemet ned fra skrivebordsgrænsefladen eller med kommandolinjeværktøjer (for eksempel kommandoen `shutdown`), genstarter enheden automatisk efter cirka 5 sekunder. Det skyldes, at strømstyringen registrerer, at der stadig er ekstern strøm til rådighed.

Under nedlukningen kan du følge systemets tilstand på LED-indikatorerne i frontpanelet. Når strømmen afbrydes, dæmpes de grønne LED'er for at vise en strømafbrydelse. Efter 5 sekunder skifter LED'erne til violet, hvilket tydeligt viser, at enheden er ved at lukke ned. Når nedlukningen er gennemført, slukker alle LED'er.

Nedlukningen tager under normale forhold kun få sekunder. I nogle tilfælde har bestemte tjenester dog brug for længere tid til at stoppe korrekt. Sker det, kan enheden nå at aflade superkondensatorerne næsten helt, før den lukker ned. Den længere nedlukningstid er normal og er ikke tegn på en fejl i systemet.

## Fejlfinding ved den første opsætning

### Almindelige og mindre almindelige problemer:

❌ **Ingen strøm/ingen LED'er:**

- Kontrollér strømtilslutninger og polaritet
- Kontrollér sikringens tilstand
- Sørg for, at spændingen ligger inden for området 11–32 V

❌ **WiFi-adgangspunktet er ikke synligt:**

- Sørg for, at antennen sidder ordentligt fast
- Prøv at oprette forbindelse fra en anden enhed
- Kontrollér, om HALPI2 er startet helt op (LED'erne skal være grønne)
- Prøv først at oprette forbindelse via ethernet

❌ **Enheden kan ikke nås på `halos.local`:**

- Prøv i stedet den tildelte IP-adresse (se DHCP-klientlisten i din router)

❌ **Skærmen er tilsluttet, men viser ingenting:**

- Sørg for, at HDMI-kablet sidder ordentligt fast
- Sørg for, at skærmen er tændt og indstillet til den rigtige indgang
- Prøv et andet HDMI-kabel eller en anden port på skærmen
- Kontrollér, at HALPI2 er tændt (LED'erne skal være gule eller grønne)
- Hvis LED'erne blinker i et regnbuemønster, sidder Compute Module 5 ikke ordentligt i sit stik. Det kan skyldes en transportskade. Følg anvisningerne i [Brugervejledningen](../user-guide/operation.md) for at genmontere CM5, eller kontakt support for at få hjælp.

❌ **Den tilsluttede skærm viser en fejlmeddelelse om »nvme«:**

- Det betyder, at NVMe SSD'en ikke registreres eller ikke initialiseres korrekt. Det kan skyldes en transportskade. Følg anvisningerne i [Brugervejledningen](../user-guide/operation.md) for at genmontere NVMe SSD'en, eller kontakt support for at få hjælp.

### Sådan får du hjælp:

- **Dokumentation:** Se de enkelte afsnit for detaljeret fejlfinding
- **Fællesskab:** Deltag i Hat Labs' brugerfora
- **Support:** Kontakt teknisk support ved hardwareproblemer

---

## Permanent installation

Når du har kontrolleret, at alt virker på skrivebordet, følger du disse trin til permanent montering og kabling.

### Planlægning af installationen

!!! tip "Hurtigt tip"
    Tag billeder af den eksisterende kabling, før du ændrer noget — det hjælper ved senere fejlfinding.

Brug tid på at planlægge installationen. Overvej:

- **Monteringssted** — tilgængelighed, beskyttelse, ventilation
- **Kabelføring** — korteste træk, beskyttelse mod skader
- **Strømkilde** — egen kreds eller delt kreds, krav til afsikring
- **Netværksintegration** — NMEA 2000, ethernet, WiFi-dækning
- **Miljøforhold** — temperatur, fugt, vibrationer

#### Nødvendigt værktøj og materialer

**Værktøj:**

- Boremaskine med bor
- Skruetrækkersæt (PH2 stjerne, stor flad)
- Afisoleringstang og krimptang til strømtilslutningerne
- Multimeter til måling
- Varmepistol eller lighter (til krympeflex)

**Materialer (medfølger ikke):**

- Monteringsskruer (4 mm eller M4, afhængigt af monteringsfladen)
- Passende sikringer (3–5 A) eller automatsikringer med tilsvarende mærkning i eltavlen
- Marinegodkendt ledning (1,5 mm² eller 16 AWG til strøm, hvis det medfølgende kabel er for kort)
- Krympeflex og kabelsko
- Kabelbindere og monteringsklips

### Montering

#### Valg af placering

Vælg et monteringssted, der giver:

!!! tip "Optimale monteringsforhold"
    - **Temperaturområde:** −20 °C … +60 °C omgivelsestemperatur
    - **Ventilation:** Tilstrækkelig afstand omkring kabinettet
    - **Beskyttelse:** Væk fra direkte vandsprøjt og mekanisk påvirkning
    - **Adgang:** Nem adgang til stik og status-LED'er
    - **Bæreevne:** Solid monteringsflade, der kan bære 2 kg plus kabler
    - **Plads:** Afsæt mindst 100 mm fri plads foran panelstikkene til kabelføring.

Selvom denne vejledning handler om faste installationer, er det i praksis ofte nok at stille enheden på en hylde eller et bord, så længe den står stabilt og er beskyttet mod fugt og stød.

#### Retningslinjer for omgivelserne

**Marine installationer:**

- Monter over det forventede lænsevandsniveau
- Undgå steder med direkte vandsprøjt eller stillestående vand
- Tag højde for bådens bevægelser og vibrationer, og fastgør alle forbindelser
- Brug korrosionsbestandige monteringsbeslag

**Automotive-installationer:**

- Beskyt mod motorvarme og vibrationer
- Sørg for tilstrækkelig ventilation i lukkede rum
- Tænk på tilgængeligheden ved vedligeholdelse
- Brug en vibrationsbestandig montering

**Industrielle installationer:**

- Beskyt mod proceskemikalier og ekstreme temperaturer
- Tag højde for kilder til elektromagnetisk støj
- Sørg for overensstemmelse med de lokale elregler
- Planlæg adgang til rutinemæssig vedligeholdelse

#### Monteringsretning

!!! info "Anbefalet retning"
    **Foretrukket:** Stikkene vender nedad

    - Mindsker risikoen for vandindtrængning
    - Giver bedre kabelføring
    - Nemmere adgang ved vedligeholdelse

    **Acceptabelt:** Stikkene vender til siden

    - Sørg for tilstrækkeligt afløb
    - Brug tætninger ved kabelindføringerne

    **Undgå:** Stikkene vender opad

    - Øger risikoen for vandindtrængning
    - Gør kabelføringen besværlig

#### Monteringstrin

##### Trin 0: Hent og udskriv boreskabelonen

Hent [HALPI2-boreskabelonen](./HALPI2_enclosure_1B_Drill_Template_v2.pdf), og udskriv den i 100 % skala. Skabelonen hjælper dig med at afsætte monteringshullerne nøjagtigt. Har du ikke adgang til en printer, kan du i stedet bruge målene fra skabelonen til at afsætte hullerne manuelt eller bruge selve kabinettet til at markere hullerne direkte på monteringsfladen.

[![Boreskabelon](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Trin 1: Klargør monteringsfladen

1. **Rengør monteringsfladen**
2. **Afsæt monteringshullerne** med den udskrevne skabelon
3. **Prøvemonter** kabinettet før installationen
4. **Bor styrehuller** til monteringsskruerne

##### Trin 2: Monter HALPI2

1. **Placer kabinettet** med stikkene i den foretrukne retning
2. **Skru monteringsskruerne i** — fast, men uden at overspænde

### Permanent strømtilslutning

#### Valg af strømkilde

**Mulighed 1: Eget strømstik**

- Mest driftssikkert og fleksibelt
- Understøtter fuld effekt
- Nemmere vedligeholdelse og fejlfinding

**Mulighed 2: Busforsyning fra NMEA 2000**

- Forenkler kablingen i marine installationer
- Begrænset til et strømforbrug på 0,9 A
- Kræver, at du er opmærksom på spændingsfald

#### Konfiguration af strømbegrænsningen

HALPI2 har en indbygget strømbegrænser på indgangen, som styrer den indledende opladning af superkondensatorerne og beskytter installationen mod overstrøm. Strømgrænsen kan sættes til enten 0,9 A eller 2,5 A, afhængigt af din strømkilde og anvendelsens krav. Standardindstillingen på 0,9 A passer til de fleste anvendelser.

Hvis du vil have enheden hurtigere op at køre eller skal forsyne perifere enheder med et stort strømforbrug, kan du skifte til indstillingen 2,5 A. Følg trinnene i [Brugervejledningen](../user-guide/operation.md) for at ændre strømgrænsen.

#### Egen strømtilslutning

##### Klargøring af kablet

1. **Før strømkablet** fra HALPI2 til strømkilden
2. **Afsæt servicesløjfer** i begge ender
3. **Beskyt kablet** mod skamfiling og skader
4. **Afkort til længde**, og lad der være rigelig arbejdsplads

##### Tilslutning ved strømkilden

1. **Beskyt ledningen** ved at afsætte en automatsikring på 3–5 A eller montere en ledningssikring
2. **Afisoler ledningsenderne** i passende længde
3. **Monter kabelsko** med korrekt krimpning
4. **Slut til strømkilden:**
    - **Rød leder:** plusklemme (+)
    - **Sort leder:** minusklemme (-)
5. **Kontrollér polariteten** med et multimeter, før du tænder for spændingen

##### Tilslutning ved HALPI2

E7T-stikket er formonteret på kablet og kræver ingen terminering på stedet. Sæt det blot i HALPI2's strømtilslutning.

#### Strømtilslutning via NMEA 2000-bussen

!!! info "Forudsætninger"
    - Strømbegrænsningskontakten **skal** stå på 0,9 A
    - NMEA 2000-netværket skal kunne levere strøm nok
    - Dropkablet bør sidde tæt på strømindføringen for at minimere spændingsfaldet

##### Nødvendige dele

- NMEA 2000-dropkabel (medfølger ikke)
- T-stik til tilslutning på backbone (medfølger ikke)

##### Installationstrin

1. **Sluk** for alle NMEA 2000-enheder
2. **Åbn HALPI2's kabinet** (se [Brugervejledningen](../user-guide/operation.md) for anvisninger)
3. **Find strømtilslutningen på bærekortet**
4. **Træk den eksisterende klemrække ud**
5. **Sæt den interne NMEA 2000-strømklemrække** i strømtilslutningen på bærekortet
6. **Kontrollér, at strømgrænsen** er sat til 0,9 A
7. **Slut til backbone** med et passende dropkabel og T-stik
8. **Test installationen**, før du lukker kabinettet
9. **Saml kabinettet igen**

![Strømkabling til NMEA 2000](./n2k-power-conx.jpg)
*For at forsyne HALPI2 via NMEA 2000 skal du trække klemrække 1 ud og sætte klemrække 2 i stedet.*

### Netværks- og dataforbindelser

#### NMEA 2000-dataforbindelse

Selv når du bruger en egen strømtilslutning, vil du måske også have dataforbindelse til NMEA 2000:

1. **Monter et T-stik** på NMEA 2000-netværkets backbone
2. **Tilslut et dropkabel** mellem T-stikket og HALPI2
3. **Kontrollér, at NMEA 2000-netværket** er korrekt termineret
4. **Test forbindelsen** efter installationen

#### Ethernetforbindelse

Sådan får du netværksforbindelse:

1. **Brug marinegodkendt kabel** eller kabel, der passer til miljøet
2. **Monter kabelforskruninger eller gennemføringstyller**, hvis kablet føres gennem skotter
3. **Afsæt servicesløjfer** i begge ender
4. **Test forbindelsen**, før installationen afsluttes

#### WiFi-/Bluetooth-antenne

1. **Monter antennen** på RP-SMA-stikket
2. **Placer den for at få bedst mulig dækning** — væk fra metalgenstande. I metalskabe kan et RP-SMA-forlængerkabel med han- og hunstik være nødvendigt.
3. **Test signalstyrken** i den endelige placering

### Fejlfinding ved installationen

#### Problemer med strømmen

❌ **Ingen strømindikation:**

- Kontrollér sikringens tilstand og mærkning
- Kontrollér strømkildens spænding (11–32 V)
- Bekræft, at polariteten er rigtig
- Mål gennemgang i strømkablerne

❌ **Ustabil strømforsyning:**

- Kontrollér, at alle forbindelser sidder stramt
- Efterse klemmerne for tæring
- Kontrollér, at ledertværsnittet passer til strømmen

#### Netværksforbindelse

❌ **Ingen kommunikation på NMEA 2000:**

- Kontrollér netværkets terminering (120 Ω i begge ender)
- Kontrollér monteringen af T-stikket
- Bekræft, at dropkablet er helt
- Test med en enhed, du ved virker

❌ **Ingen ethernetforbindelse:**

- Test kablet med en kabeltester
- Kontrollér konfigurationen af switch/router
- Se efter konflikter mellem IP-adresser
- Bekræft kablets klasse (mindst Cat5e)

#### Problemer med omgivelserne

❌ **Fugtindtrængning:**

- Efterse alle tætningers tilstand
- Kontrollér stikkenes retning
- Kontrollér kabelindføringerne
- Overvej yderligere beskyttelse

❌ **Overophedning:**

- Flyt enheden væk fra varmekilder
- Se efter blokeret luftstrøm omkring kabinettet

### Sikkerhed og overensstemmelse

#### Elsikkerhed

- **Brug passende sikringer** til beskyttelse mod overstrøm
- **Sørg for korrekt jordforbindelse** efter de lokale regler
- **Beskyt mod kortslutning** med korrekt kabelføring

#### Marine installationer

- **Følg de lokale standarder eller ABYC-standarderne** for elinstallationer
- **Brug marinegodkendte komponenter** hele vejen igennem

#### Industrielle installationer

- **Overhold de lokale elregler**
- **Sørg for korrekt beskyttelse mod EMI/RFI**
- **Dokumentér installationen** efter anlæggets krav

## Næste skridt

Når din HALPI2 kører:

1. **Udforsk [Brugervejledningen](../user-guide/operation.md)** for detaljerede anvisninger til betjeningen
2. **Læs Almindelige anvendelsestilfælde** for opsætning til bestemte anvendelser
3. **Se Teknisk reference** for avancerede konfigurationsmuligheder
4. **Deltag i fællesskabet** for at få tip, tricks og support

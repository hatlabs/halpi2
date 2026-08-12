---
translated_from: 6e5802b5be19c03e5a1ca6cf292d8785a9f37601
---

# Kom igång

Den här guiden får din HALPI2 i gång på under 30 minuter och går även igenom den permanenta installationen. Följ stegen i ordning för smidigast möjliga uppsättning — börja med en uppsättning på skrivbordet för att kontrollera att allt fungerar, och gå sedan vidare till den permanenta installationen.

## Säkerhet och hantering

!!! warning "Innan du börjar"
    - Se till att strömmen är bortkopplad från elsystemet innan du gör anslutningar
    - Använd lämpliga säkringar (3–5 A) för strömanslutningar
    - Hantera enheten varsamt — den är robust, men fall och slag kan skada interna komponenter
    - Kontrollera polariteten när du ansluter strömkablar
    - Undvik statiska urladdningar — jorda dig själv och avstå från att gnida katter och bärnstensföremål innan du rör vid interna komponenter

## Det här behöver du

Ur HALPI2-förpackningen:

- HALPI2-enhet med förmonterad CM5 och NVMe SSD
- Strömkabel med E7T-kontakt (2 m)

Tillval (ingår i försäljningspaketet):

- Par av DC-hålkontakter (5,5 × 2,1 mm), vid användning av en vanlig 12 V-nätadapter
- Raspberry Pi WiFi/Bluetooth-antenn (krävs om WiFi används vid den första uppsättningen)

Övrigt (ingår ej):

- 12 V- eller 24 V-strömkälla
- En separat dator för uppsättning utan skärm (om du inte ansluter en skärm)
- Nätverkskabel (valfritt, för trådbunden anslutning)
- Skärm med HDMI-ingång (valfritt)
- USB-tangentbord och mus (valfritt, för direkt åtkomst)

!!! tip "Snabbtips"
    Nätverksutrustning som routrar och WiFi-accesspunkter använder ofta en 12 V-nätadapter som går att använda till HALPI2. Leta i högen med gammal hårdvara!

## Uppsättning på skrivbordet

Vi rekommenderar att du provar HALPI2 på ett skrivbord eller en arbetsbänk innan du installerar den permanent. Den första uppsättningen kan göras antingen utan skärm (headless) över en nätverksanslutning, eller med ansluten skärm, tangentbord och mus. En uppsättning utan skärm kan använda antingen trådbunden ethernet eller HALPI2:s WiFi-accesspunkt.

### Steg 1: Anslut nödvändiga kringenheter

#### För den första uppsättningen:

1. **Nätverksanslutning (krävs vid installation utan skärm):**
    - Anslut en ethernetkabel
    - Anslut WiFi/Bluetooth-antennen

2. **Skärmanslutning (valfritt):**
    - Anslut en HDMI-skärm för direkt åtkomst
    - USB-tangentbord och mus om du använder skärm

![Frontpanelens kontakter](./front-panel-connectors.jpg)
*Frontpanelens kontakter*

### Steg 2: NMEA 2000-anslutning (valfritt)

Om du installerar HALPI2 direkt i en båt eller har en NMEA 2000-installation på skrivbordet kan du ansluta enheten till NMEA 2000-nätverket redan nu.

Ett [NMEA 2000-nätverk](https://docs.hatlabs.fi/nmea2000/) består av en backbone-kabel som alla enheter ansluts till med T-kopplingar och stickledningar. Sätt en T-koppling på nätverkets backbone. Anslut HALPI2:s Micro-C-kontakt till T-kopplingen med en NMEA 2000-stickledning.

### Steg 3: Strömanslutning

!!! tip "Om matning via NMEA 2000"
    HALPI2 kan även matas från NMEA 2000-bussen. Se [Strömanslutning via NMEA 2000-bussen](#stromanslutning-via-nmea-2000-bussen) i avsnittet om permanent installation nedan.

För uppsättningen på skrivbordet använder vi den medföljande E7T-strömkabeln. Anslut kabelns ledarändar till hålkontakten (hona) så här:

- **Röd ledare = plus (+)**
- **Svart ledare = minus (-)**

![E7T till hålkontakt](./e7t-barrel.jpg)
*Ett exempel på kablaget mellan E7T och hålkontakten*

Anslut en vanlig 12 V- eller 24 V-nätadapter till hålkontakten. Kontrollera att adaptern klarar minst 1 A, vilket HALPI2 kräver.

!!! warning "Varning"
    Eftersom skruvplintens hålkontakt saknar dragavlastning bör den bara användas vid tillfälliga installationer. Ett ryck i kabeln kan lossa och blottlägga ledarna.

## Första start

HALPI2 levereras med [HaLOS](https://docs.halos.fi), en containerbaserad Linux-distribution med webbaserat gränssnitt, avsedd för marina och industriella tillämpningar. Om du föredrar ett annat operativsystem, som OpenPlotter eller Raspberry Pi OS, se [Programvaruguiden](../user-guide/software.md).

!!! info "HaLOS dokumentation"
    Den här guiden behandlar HALPI2:s hårdvara och den första påslagningen. Allt som rör operativsystemet — uppsättning vid första start, nätverk, appar, certifikat och den dagliga användningen — finns i **[HaLOS dokumentation](https://docs.halos.fi)**. Ha den till hands när du går igenom stegen nedan.

**Slå på HALPI2** genom att ansluta nätadaptern, om du inte redan gjort det. Efter några sekunder börjar LED-raden fyllas med rött ljus, vilket visar att superkondensatorerna laddas. Lysdioderna blir gula när systemet startar och slutligen gröna när operativsystemet körs och HALPI-daemonen har kontakt med styrkretsen.

Om du har en skärm ansluten ser du Raspberry Pi OS startbild och till sist ett grafiskt skrivbord.

!!! tip "Tips"
    Statuslysdiodernas mönster beskrivs i [Daglig användning](../user-guide/operation.md#status-ledar).

### Åtkomst till HALPI2 utan skärm

Om du inte har någon skärm ansluten når du HALPI2 via dess WiFi-accesspunkt eller en ethernetanslutning. HaLOS har ett webbaserat gränssnitt — ingen ytterligare programvara behövs[^ssh].

[^ssh]: SSH finns också på HaLOS-avbilder utan skärm (aktiverat som standard). I Desktop-varianterna aktiverar du SSH med `raspi-config`. Standarduppgifter: användarnamn `pi`, lösenord `halos`.

Vänta först tills lysdioderna blir gröna, vilket betyder att systemet har startat färdigt. Fortsätt sedan så här:

**Alternativ 1 — anslutning via WiFi-accesspunkten:** HaLOS skapar en WiFi-accesspunkt med namnet `Halos-XXXX` (unikt per enhet) och lösenordet `halos1234`. Anslut din dator till det nätverket.

Accesspunkten har ingen egen internetanslutning, så nästa steg är att peka ut ett WiFi-nätverk som har det (behövs för att hämta containerapparna vid första start):

1. Öppna Cockpit på `https://halos.local:9090/` och logga in (användarnamn `pi`, lösenord `halos`).
2. Gå till **Networking** och klicka på **WiFi (wlan0)**.
3. Vänta tills listan över tillgängliga nätverk visas och klicka på ditt nätverk.
4. Ange lösenordet och klicka på **Add**.

HALPI2 håller accesspunkten `Halos-XXXX` uppe medan den ansluter till ditt nätverk, så din dator kan tappa kontakten med accesspunkten en kort stund och sedan ansluta igen av sig själv.

**Alternativ 2 — anslutning via trådbunden ethernet:** om du har anslutit HALPI2 till ditt nätverk med ethernet får den automatiskt en IP-adress via DHCP.

När anslutningen är på plats öppnar du en webbläsare och går till:

- **Instrumentpanel:** `https://halos.local/` — Homarr-instrumentpanelen med länkar till alla installerade appar
- **Systemadministration:** `https://halos.local:9090/` — Cockpit för systemhantering, uppdateringar och containerappar

!!! note "Varning om SSL-certifikat"
    Första gången du öppnar instrumentpanelen eller Cockpit visar webbläsaren varningen ”Inte säker”. HaLOS signerar sina webbtjänster med en certifikatutfärdare (CA) som enheten själv skapar, och din webbläsare litar inte på den ännu. Godta varningen för att fortsätta tills vidare.

    För att bli av med varningen permanent installerar du enhetens CA på din dator en gång — därefter validerar alla HaLOS-tjänster rent på alla portar. Öppna `https://halos.local/ca/` för ett guidat installationsprogram per plattform, eller se [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) i HaLOS dokumentation.

!!! info "Internet krävs vid första start"
    Cockpit-gränssnittet är tillgängligt direkt, men instrumentpanelen och övriga containerbaserade appar kräver en internetanslutning vid första start för att hämta sina containeravbilder. Anslut HALPI2 till internet via ethernet, eller konfigurera WiFi via Cockpit.

### Konfiguration vid första start

!!! warning "Varning"
    HaLOS levereras med standardlösenord som **måste** bytas vid första start, för att hindra obehörig åtkomst till din enhet.

HaLOS har två uppsättningar inloggningsuppgifter:

| Typ av åtkomst | Användarnamn | Standardlösenord | Används till |
|:---------------|:-------------|:-----------------|:-------------|
| SSO (webbappar) | `admin` | `halos` | Instrumentpanelen, Signal K, Grafana och andra webbappar |
| System (SSH/Cockpit) | `pi` | `halos` | SSH-åtkomst, systemadministration i Cockpit |

#### Att byta lösenord

- **SSO-lösenordet:** byts via Authelia (nås från instrumentpanelen)
- **Systemlösenordet:** byts via Cockpit (`https://halos.local:9090/`) under användarkontots inställningar, eller via SSH med `passwd`

Utförliga anvisningar för första start finns i [HaLOS guide Kom igång](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Använder du OpenPlotter eller Raspberry Pi OS?"
    Om du har flashat ett annat operativsystem, se [Programvaruguiden](../user-guide/software.md#forsta-konfigurationen-av-systemet) för operativsystemsspecifika anvisningar.

### Kontrollera NMEA 2000-anslutningen (valfritt)

Enklast kontrollerar du NMEA 2000-anslutningen genom att titta på Signal K-serverns status. I HaLOS Marine-avbilderna är Signal K förinstallerad och nås från instrumentpanelen på `https://halos.local/`. I HaLOS-avbilder som inte är marina kan Signal K installeras från Container Apps-butiken i Cockpit.

Öppna Signal K:s webbgränssnitt och titta på aktiviteten för anslutningen `can0`: du bör se att en del trafik tas emot.

![Anslutningsaktivitet i Signal K-servern](./sk-n2k-deltas.jpg)

## Att stänga av enheten

HALPI2 är konstruerad för att stänga av sig automatiskt när strömförsörjningen bryts. När du behöver stänga av enheten bryter du helt enkelt strömmen, antingen med en brytare på elpanelen eller genom att dra ur strömkontakten. Systemet påbörjar då automatiskt en avstängning i programvaran, så att alla program stängs korrekt och filsystemet avmonteras säkert.

Under avstängningen dämpas lysdioderna först (spänningsbortfall upptäckt), lyser violett medan avstängningen pågår och släcks när den är klar. Avstängningens beteende — inklusive den valfria automatiska omstarten efter en avstängning via programvaran — beskrivs i [Daglig användning](../user-guide/operation.md#stanga-av-systemet).

## Felsökning vid uppstart

### Vanliga och ovanliga problem:

❌ **Ingen ström / inga lysdioder:**

- Kontrollera strömanslutningarna och polariteten
- Kontrollera säkringen
- Se till att spänningen ligger inom 10–32 V

❌ **WiFi-accesspunkten syns inte:**

- Se till att antennen är ordentligt ansluten
- Prova att ansluta med en annan enhet
- Kontrollera att HALPI2 har startat färdigt (lysdioderna ska vara gröna)
- Prova att ansluta via ethernet först

❌ **Enheten går inte att nå på `halos.local`:**

- Prova den tilldelade IP-adressen i stället (se routerns lista över DHCP-klienter)

❌ **Skärmen är ansluten men visar ingenting:**

- Se till att HDMI-kabeln sitter ordentligt
- Se till att skärmen är påslagen och står på rätt ingång
- Prova en annan HDMI-kabel eller en annan port på skärmen
- Kontrollera att HALPI2 är på (lysdioderna ska vara gula eller gröna)
- Om lysdioderna blinkar i ett regnbågsmönster sitter Compute Module 5 inte ordentligt. Det kan bero på transportskada. Följ anvisningarna i [Hårdvaruguiden](../user-guide/hardware.md#byte-av-compute-module-5) för att sätta tillbaka CM5, eller kontakta supporten.

❌ **Den anslutna skärmen visar ett felmeddelande om ”nvme”:**

- Det betyder att NVMe SSD-enheten inte hittas eller inte initieras korrekt. Det kan bero på transportskada. Följ anvisningarna i [Hårdvaruguiden](../user-guide/hardware.md#byte-av-nvme-ssd) för att sätta tillbaka SSD-enheten, eller kontakta supporten.

### Att få hjälp:

- **Dokumentation:** se de enskilda avsnitten för utförlig felsökning
- **Gemenskapen:** gå med i Hat Labs diskussionsforum
- **Support:** kontakta den tekniska supporten vid hårdvaruproblem

---

## Permanent installation

När du har kontrollerat att allt fungerar på skrivbordet följer du de här stegen för permanent montering och kablage.

### Att planera installationen

!!! tip "Snabbtips"
    Ta foton av det befintliga kablaget innan du ändrar något — det hjälper vid senare felsökning.

Ta dig tid att planera installationen. Tänk på:

- **Monteringsplats** — åtkomlighet, skydd, ventilation
- **Kabeldragning** — kortast möjliga sträckor, skydd mot skador
- **Strömkälla** — egen krets eller delad, krav på säkring
- **Nätverksintegration** — NMEA 2000, ethernet, WiFi-täckning
- **Miljöfaktorer** — temperatur, fukt, vibrationer

#### Verktyg och material som behövs

**Verktyg:**

- Borrmaskin med borr
- Skruvmejselsats (PH2 Phillips, stor spårmejsel)
- Avisoleringstång och krimptång för strömanslutningarna
- Multimeter för mätning
- Varmluftspistol eller tändare (för krympslang)

**Material (ingår ej):**

- Monteringsskruvar (4 mm eller M4, beroende på monteringsytan)
- Lämpliga säkringar (3–5 A) eller automatsäkringar med motsvarande märkning på elpanelen
- Marin kabel (1,5 mm² eller 16 AWG för matningen, om den medföljande kabeln är för kort)
- Krympslang och kabelskor
- Buntband och kabelklamrar

### Montering

#### Val av plats

Välj en monteringsplats som ger:

!!! tip "Optimala monteringsförhållanden"
    - **Temperaturområde:** -20 °C till +60 °C omgivningstemperatur
    - **Ventilation:** tillräckligt fritt utrymme runt kapslingen
    - **Skydd:** undan direkt vattenstänk och mekaniska skador
    - **Åtkomst:** lätt att nå kontakter och statuslysdioder
    - **Bärighet:** ett stadigt underlag som bär 2 kg plus kablar
    - **Utrymme:** minst 100 mm fritt framför panelkontakterna för kabeldragningen

Även om den här guiden inriktar sig på fasta installationer räcker det i praktiken ofta att ställa enheten på en hylla eller ett bord, förutsatt att den står stadigt och är skyddad mot fukt och slag.

#### Riktlinjer för miljön

**Marina installationer:**

- Montera ovanför förväntad nivå för slagvatten
- Undvik ytor med direkt stänk eller stående vatten
- Ta hänsyn till båtens rörelser och vibrationer, och säkra alla anslutningar
- Använd korrosionsbeständiga infästningar

**Fordonsinstallationer:**

- Skydda mot motorvärme och vibrationer
- Se till att ventilationen räcker i slutna utrymmen
- Tänk på åtkomsten vid underhåll
- Använd vibrationståliga infästningar

**Industriella installationer:**

- Skydda mot processkemikalier och extrema temperaturer
- Tänk på källor till elektromagnetiska störningar
- Se till att lokala elföreskrifter följs
- Planera för åtkomst vid rutinunderhåll

#### Monteringsriktning

!!! info "Rekommenderad riktning"
    **Att föredra:** kontakterna nedåt

    - Minskar risken för vatteninträngning
    - Ger snyggare kabeldragning
    - Enklare åtkomst vid underhåll

    **Godtagbart:** kontakterna åt sidan

    - Se till att vatten kan rinna av
    - Använd tätningar vid kabelinföringarna

    **Undvik:** kontakterna uppåt

    - Ökar risken för vatteninträngning
    - Försvårar kabeldragningen

#### Monteringssteg

##### Steg 0: Hämta och skriv ut borrmallen

Hämta [HALPI2:s borrmall](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) och skriv ut den i skala 100 %. Med mallen märker du ut fästhålen exakt. Om du inte har tillgång till en skrivare kan du i stället använda måtten i mallen för att märka ut hålen för hand, eller använda själva kapslingen för att märka ut dem direkt på underlaget.

[![Borrmall](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Steg 1: Förbered monteringsytan

1. **Rengör monteringsytan**
2. **Märk ut fästhålen** med den utskrivna mallen
3. **Provmontera** kapslingen före installationen
4. **Förborra hålen** för monteringsskruvarna

##### Steg 2: Montera HALPI2

1. **Placera kapslingen** med kontakterna i önskad riktning
2. **Dra i monteringsskruvarna** — stadigt men utan att dra åt för hårt

### Permanent strömanslutning

#### Val av strömkälla

**Alternativ 1: egen strömkontakt**

- Mest tillförlitligt och flexibelt
- Ger full effektkapacitet
- Enklare underhåll och felsökning

**Alternativ 2: matning från NMEA 2000-bussen**

- Förenklar kablaget i marina installationer
- Begränsad till 0,9 A strömuttag
- Kräver noggrann uppmärksamhet på spänningsfallet

#### Konfiguration av strömbegränsningen

HALPI2 har en inbyggd strömbegränsare på ingången som sköter den inledande laddningen av superkondensatorerna och skyddar installationen mot överström. Begränsningen kan ställas till antingen 0,9 A eller 2,5 A, beroende på strömkälla och tillämpningens krav. Standardinställningen 0,9 A passar de flesta tillämpningar.

Om du vill att starten ska gå fortare, eller behöver mata strömtörstiga kringenheter, kan du byta till inställningen 2,5 A. Följ stegen i [Hårdvaruguiden](../user-guide/hardware.md#konfiguration-av-strombegransningen) för att ändra strömbegränsningen.

#### Egen strömanslutning

##### Förbereda kabeln

1. **Dra strömkabeln** från HALPI2 till strömkällan
2. **Lämna servicelängor** i båda ändar
3. **Skydda kabeln** mot skavning och skador
4. **Kapa till rätt längd** och lämna tillräckligt arbetsutrymme

##### Anslutning vid strömkällan

1. **Skydda ledningen** genom att avsätta en automatsäkring på 3–5 A eller montera en säkring i serie
2. **Avisolera ledarändarna** till lämplig längd
3. **Montera kabelskor** med rätt krimpteknik
4. **Anslut till strömkällan:**
    - **Röd ledare:** plusanslutning (+)
    - **Svart ledare:** minusanslutning (-)
5. **Kontrollera polariteten** med multimeter innan du kopplar på spänningen

##### Anslutning vid HALPI2

E7T-kontakten är färdigkopplad och kräver ingen montering på plats. Anslut den bara till HALPI2:s strömuttag.

#### Strömanslutning via NMEA 2000-bussen

!!! info "Förutsättningar"
    - Omkopplaren för strömbegränsning **måste** stå på 0,9 A
    - NMEA 2000-nätverket måste ha tillräcklig effektkapacitet
    - Stickledningen bör sitta nära matningspunkten för att minska spänningsfallet

##### Komponenter som behövs

- NMEA 2000-stickledning (ingår ej)
- T-koppling för anslutning till backbone (ingår ej)

##### Installationssteg

1. **Stäng av** alla NMEA 2000-enheter
2. **Öppna HALPI2:s kapsling** (se [Hårdvaruguiden](../user-guide/hardware.md#atkomst-till-kapslingen) för anvisningar)
3. **Leta upp bärkortets strömkontakt**
4. **Dra ur den befintliga kopplingsplinten**
5. **Anslut den interna NMEA 2000-kopplingsplinten för ström** till bärkortets strömkontakt
6. **Kontrollera att strömbegränsningen** står på 0,9 A
7. **Anslut till nätverkets backbone** med lämplig stickledning och T-koppling
8. **Provkör installationen** innan du stänger kapslingen
9. **Montera ihop kapslingen**

![Kablage för matning via NMEA 2000](./n2k-power-conx.jpg)
*För att mata HALPI2 via NMEA 2000, dra ur kopplingsplint 1 och ersätt den med kopplingsplint 2.*

### Nätverks- och dataanslutningar

#### NMEA 2000-dataanslutning

Även med en egen strömanslutning kan du vilja ha NMEA 2000-data:

1. **Montera en T-koppling** på NMEA 2000-nätverkets backbone
2. **Anslut en stickledning** mellan T-kopplingen och HALPI2
3. **Kontrollera termineringen** av NMEA 2000-nätverket
4. **Provkör anslutningen** efter installationen

#### Ethernetanslutning

För nätverksanslutning:

1. **Använd marin** eller på annat sätt miljöklassad kabel
2. **Montera kabelgenomföringar eller kabelgummin** om kabeln dras genom skott
3. **Lämna servicelängor** i båda ändar
4. **Provkör anslutningen** före den slutliga installationen

#### WiFi/Bluetooth-antenn

1. **Montera antennen** på RP-SMA-kontakten
2. **Placera den för bästa täckning** — undan metallhinder. I metallskåp kan en förlängningskabel med RP-SMA hane till hona behövas.
3. **Mät signalstyrkan** i den slutliga placeringen

### Felsökning vid installation

#### Strömproblem

❌ **Ingen strömindikering:**

- Kontrollera säkringens skick och märkning
- Kontrollera strömkällans spänning (10–32 V)
- Bekräfta rätt polaritet
- Mät genomgången i strömkablarna

❌ **Glappande ström:**

- Kontrollera att alla anslutningar sitter åt
- Leta efter korroderade anslutningar
- Kontrollera att ledararean räcker för strömmen

#### Nätverksanslutning

❌ **Ingen NMEA 2000-kommunikation:**

- Kontrollera nätverkets terminering (120 Ω i båda ändar)
- Kontrollera T-kopplingens montering
- Kontrollera stickledningens skick
- Prova med en enhet som du vet fungerar

❌ **Ingen ethernetanslutning:**

- Testa kabeln med en kabeltestare
- Kontrollera switchens eller routerns konfiguration
- Leta efter IP-adresskonflikter
- Kontrollera kabelns klassning (minst Cat5e)

#### Miljöproblem

❌ **Fuktinträngning:**

- Kontrollera alla tätningar
- Kontrollera kontakternas riktning
- Kontrollera kabelinföringarna
- Överväg ytterligare skydd

❌ **Överhettning:**

- Flytta enheten bort från värmekällor
- Kontrollera att luftflödet runt kapslingen inte är blockerat

### Säkerhet och regelefterlevnad

#### Elsäkerhet

- **Använd lämpliga säkringar** som överströmsskydd
- **Se till att jordningen är korrekt** enligt lokala föreskrifter
- **Skydda mot kortslutning** med genomtänkt kabeldragning

#### Marina installationer

- **Följ lokala standarder eller ABYC** för elinstallationer
- **Använd marina komponenter** genomgående

#### Industriella installationer

- **Följ lokala elföreskrifter**
- **Se till att EMI/RFI-skyddet** är tillräckligt
- **Dokumentera installationen** enligt anläggningens krav

## Nästa steg

När din HALPI2 är i gång:

1. **Läs [Daglig användning](../user-guide/operation.md)** för att lära dig vad lysdioderna betyder och hur avstängningen fungerar
2. **Utforska [Programvaruguiden](../user-guide/software.md)** för uppdateringar, fjärråtkomst och kommandot `halpi`
3. **Titta i den tekniska referensen** för detaljerade specifikationer
4. **Gå med i gemenskapen** för tips, knep och stöd

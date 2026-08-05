---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Systemdrift

## Status-LED-indikatorer

HALPI2 har fem RGB-LED-er som gir visuell tilbakemelding om systemstatus og strømforhold.

### Hurtigreferanse for LED-status

| LED-mønster | Farge | Betydning |
|-------------|-------|---------|
| LED 5 lyser fast | Rød | Strøm på, venter på lading |
| Gradvis fylling | Rød | Superkondensatorene lades |
| Regnbue + fargesyklus | Flerfarget | CM5 startet ikke |
| Spenningssøyle | Gul | Drift i solomodus |
| Spenningssøyle | Grønn | Drift i samspillsmodus |
| Spenningssøyle | Oransje | Reservestrøm aktiv (solo) |
| Spenningssøyle | Mørkegrønn | Reservestrøm aktiv (samspill) |
| Alle blinker | Rød | Overspenning i superkondensatorene |
| Alle lyser fast | Rød | Watchdog-tidsavbrudd |
| Spenningssøyle | Lilla | Nedstenging pågår |
| Alle lyser fast | Blå | Nedstenging til ventemodus pågår |
| Alle lyser fast | Svak rød | Ventemodus |
| Alle av | — | Systemet av |

### Spenningsindikering for superkondensatorene

Under drift fungerer LED-ene som en spenningsindikator som viser ladenivået i superkondensatorene:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Strømstyring og nedstengingsprosedyrer

HALPI2 har en strømforsyning som er laget for å tåle spenningstopper, forstyrrelser og kortvarige avbrudd.

### Oversikt over strømsystemet

Strømstyringssystemet i HALPI2 består av:

- **Strømforsyning med bredt inngangsområde** (11–32 VDC inngang med beskyttelse opp til 100 VDC)
- **Reservesystem med superkondensatorer** for kontrollert nedstenging ved strømbortfall
- **Strømbegrensning** (0,9 A eller 2,5 A, valgbart)
- **Deteksjon av strømbortfall** og automatisk start av nedstenging
- **Overvåking av inngangsspenning og -strøm**

Systemet virker i to moduser: solomodus (solo mode) og samspillsmodus (co-op mode).

### Drift i solomodus

Solomodus gir grunnleggende selvstendig drift når HALPI-daemonen ikke kjører. Kontrolleren virker på egen hånd, uten kommunikasjon med programvaren.

#### Egenskaper ved solomodus

- **Krever ingen kommunikasjon med programvaren**
- **Grunnleggende beskyttelse mot strømbortfall** – overvåker inngangsspenningen og reagerer på strømbortfall
- **Automatisk nedstenging via simulerte trykk på strømknappen**
- **Begrensede muligheter for overvåking og konfigurasjon**

#### Strømbortfall og nedstenging i solomodus

**Deteksjon av strømbortfall:**
Kontrolleren overvåker inngangsspenningen og oppdager strømbortfall. En strømbruddstimer (standard 5 sekunder) hindrer nedstenging ved korte avbrudd.

**Automatisk nedstengingssekvens:**

1. **Kontrolleren oppdager strømbortfall**
2. **Strømbruddstimeren starter** for å skille forstyrrelser fra virkelig strømbortfall
3. **Simulerte trykk på strømknappen** – kontrolleren sender dobbelttrykk på strømknappen til Compute Module
4. **Operativsystemet reagerer** og starter kontrollert nedstenging
5. **Superkondensatorene opprettholder strømmen** (vanligvis 30–60 sekunder tilgjengelig)
6. **Tidsavbruddsbeskyttelse på 60 sekunder** – tvungen utkobling hvis kontrollert nedstenging mislykkes
7. **Systemet forblir av** til strømmen kommer tilbake
8. **Automatisk omstart** når strømmen er gjenopprettet

**Manuell nedstenging i solomodus:**

- Vanlig nedstenging av operativsystemet skjer
- Systemet starter automatisk igjen etter 5 sekunder hvis inngangsstrømmen fortsatt er tilgjengelig
- For varig nedstenging kobler du fra inngangsstrømmen etter at kontrollert nedstenging er startet

#### Når solomodus er aktiv

Solomodus inntreffer:

- Under første oppstart før HALPI-daemonen starter
- Hvis HALPI-daemonen ikke klarer å starte eller er deaktivert
- På operativsystemer som ikke støttes og mangler daemonen
- Når daemonen har krasjet eller ikke lenger svarer

!!! tip "Pålitelighet i solomodus"
    Solomodus gir nødvendig grunnbeskyttelse, men er mindre pålitelig enn samspillsmodus. Kontrolleren er avhengig av simulerte knappetrykk for å be om nedstenging, og det virker kanskje ikke hvis systemet har låst seg.

### Drift i samspillsmodus

Samspillsmodus gir full strømstyringsfunksjonalitet når HALPI-daemonen kjører og kommuniserer med kontrolleren.

#### Funksjoner i samspillsmodus

- **Direkte kommunikasjon med programvaren** – sanntids datautveksling mellom kontrolleren og daemonen
- **Beskyttelse med watchdog-timer** – tidsavbrudd på 30 sekunder sikrer stabil drift
- **Konfigurerbar nedstengingsatferd** – tidsforløp og kommandoer kan tilpasses
- **Overvåking i sanntid** – omfattende overvåking av strømparametrene
- **Avanserte konfigurasjonsmuligheter**

#### Strømbortfall og nedstenging i samspillsmodus

**Deteksjon av strømbortfall:**
Kontrolleren overvåker inngangsstrømmen og melder hendelser direkte til HALPI-daemonen. Den konfigurerbare strømbruddstimeren (standard 5 sekunder) gjør at korte strømavbrudd ikke starter nedstenging.

**Automatisk nedstengingssekvens:**

1. **Kontrolleren oppdager strømbortfall** og melder fra til HALPI-daemonen
2. **Vurdering av strømbruddstimeren** – daemonen vurderer om strømbortfallet overskrider grensen
3. **Utføring av nedstengingskommando** – daemonen kjører nedstengingskommandoen (standard: `/sbin/poweroff`)
4. **Kontrollert nedstenging av operativsystemet** – programmer avsluttes og filsystemene avmonteres trygt
5. **Reservestrøm fra superkondensatorene** gir energi gjennom hele nedstengingen
6. **Kontrolleren følger med på fullføringen** – den registrerer når Compute Module slås av
7. **5 V-skinnen deaktiveres** når nedstengingen er fullført
8. **Systemet forblir av** til inngangsstrømmen kommer tilbake
9. **Styring av omstart** – avhengig av konfigurasjonen starter systemet automatisk igjen eller forblir av

**Manuell nedstenging i samspillsmodus:**

- Vanlig kontrollert nedstenging skjer når den startes fra programvaren
- Systemet starter automatisk igjen etter 5 sekunder hvis inngangsstrømmen fortsatt er tilgjengelig
- For å hindre automatisk omstart kobler du fra strømmen eller setter `auto_restart` til `false`

#### Watchdog-beskyttelse

Samspillsmodus omfatter beskyttelse med watchdog-timer:

- **Kommunikasjonstidsavbrudd på 30 sekunder** – daemonen må kommunisere jevnlig med kontrolleren
- **Automatisk gjenoppretting** – systemet starter på nytt hvis kommunikasjonen stopper
- **Beskyttelse mot programvarefeil** – sikrer gjenoppretting etter krasj i daemonen eller hengt system
- **«Mating av watchdogen»** – daemonen sender jevnlige statusoppdateringer som nullstiller timeren

#### Når samspillsmodus er aktiv

Samspillsmodus inntreffer når:

- HALPI-daemonen kjører og er i orden
- Kommunikasjonen mellom daemonen og kontrolleren er opprettet
- Systemet kjører på et operativsystem som støttes
- Full overvåking og styring av systemet er tilgjengelig

!!! info "Kontrollere samspillsmodus"
    Sjekk statusen til daemonen: `systemctl status halpid`

    Vis kontrollerens tilstand: `halpi status`

    Mer informasjon om `halpi`-kommandoen finner du i [programvareveiledningen](./software.md#halpi-daemonen-halpid).

### Reservestrøm og kondensatorsystem

Begge modusene er avhengige av reservesystemet med superkondensatorer for å sikre kontrollert nedstenging:

**Varighet på reservestrømmen:**

- Superkondensatorene gir 30–60 sekunder med reservestrøm
- Varigheten avhenger av systembelastningen og tilkoblede eksterne enheter
- Tilstrekkelig tid til trygg lukking av filsystemet og avslutning av prosesser
- Ikke laget for fortsatt drift under lange strømavbrudd

**Ladeegenskaper:**

- Ladetid: 25 sekunder med strømgrensen 0,9 A
- Ladetid: 9 sekunder med strømgrensen 2,5 A
- Ladeforløpet vises visuelt gjennom LED-progresjonen (rødt fyllemønster)

!!! warning "Begrensning i beskyttelsen mot strømbortfall"
    Superkondensatorsystemet er laget for kontrollert nedstenging, ikke for fortsatt drift. Ikke stol på det ved lengre strømavbrudd.

### Hensyn ved manuell nedstenging

HALPI2 prioriterer automatisk drift og gjenoppretting, og det påvirker hvordan manuell nedstenging virker.

#### Automatisk omstart

Som standard starter HALPI2 igjen etter manuell nedstenging så lenge inngangsstrømmen er tilgjengelig:

- Manuell nedstenging gir vanlig nedstenging av operativsystemet
- En venteperiode på 5 sekunder følger etter at nedstengingen er fullført
- Systemet starter automatisk igjen for å opprettholde driftstilgjengeligheten
- Dette sikrer gjenoppretting etter utilsiktede nedstenginger

#### Metoder for tilsiktet nedstenging

For varig nedstenging bruker du en av disse fremgangsmåtene:

**Frakobling av strømmen:**

1. Start kontrollert nedstenging fra programvaren
2. Vent til nedstengingen er fullført (LED-ene slukker)
3. Koble fra inngangsstrømmen for å hindre automatisk omstart

**Konfigurasjonsmetoden:**

1. Deaktiver automatisk omstart: `halpi config set auto_restart false`
2. Start nedstengingen fra programvaren
3. Systemet forblir av etter at nedstengingen er fullført

**Ventemodus (fremtidig):**
!!! info "Funksjonsstatus"
    Ventemodus er planlagt for kommende firmwareutgivelser. Den vil gjøre det mulig å slå av Compute Module mens HALPI2-kontrolleren forblir aktiv og venter på oppvekkingshendelser.

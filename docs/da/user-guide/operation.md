---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Systemdrift

## Status-LED-indikatorer

HALPI2 har fem RGB-LED'er, der giver visuel tilbagemelding om systemets status og strømforhold.

### Hurtig oversigt over LED-status

| LED-mønster | Farve | Betydning |
|-------------|-------|---------|
| LED 5 lyser konstant | Rød | Strøm tilsluttet, venter på opladning |
| Gradvis udfyldning | Rød | Superkondensatorerne oplader |
| Regnbue + farvecyklus | Flere | CM5 kunne ikke starte |
| Spændingssøjle | Gul | Drift i Solo-tilstand |
| Spændingssøjle | Grøn | Drift i Co-op-tilstand |
| Spændingssøjle | Orange | Backupstrøm aktiv (solo) |
| Spændingssøjle | Mørkegrøn | Backupstrøm aktiv (co-op) |
| Alle blinker | Rød | Overspænding på superkondensatorerne |
| Alle lyser konstant | Rød | Watchdog-timeout |
| Spændingssøjle | Lilla | Nedlukning i gang |
| Alle lyser konstant | Blå | Nedlukning til standby i gang |
| Alle lyser konstant | Svagt rød | Standby |
| Alle slukket | — | Systemet er slukket |

### Spændingsvisning for superkondensatorerne

Under drift fungerer LED'erne som en spændingsindikator, der viser superkondensatorernes ladeniveau:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Strømstyring og nedlukningsprocedurer

HALPI2 har en strømforsyning, der er konstrueret til at klare spændingsspidser, korte spændingsudfald og kortvarige afbrydelser.

### Oversigt over strømsystemet

HALPI2's strømstyringssystem består af:

- **Strømforsyning med bredt indgangsområde** (11–32 V DC indgang med beskyttelse op til 100 V DC)
- **Backupsystem med superkondensatorer** til kontrolleret nedlukning ved strømsvigt
- **Strømbegrænsning** (0,9 A eller 2,5 A, som du selv vælger)
- **Registrering af strømsvigt** og automatisk igangsætning af nedlukning
- **Overvågning af indgangsspænding og -strøm**

Systemet kører i to tilstande: Solo-tilstand og Co-op-tilstand.

### Drift i Solo-tilstand

Solo-tilstand giver grundlæggende selvstændig drift, når HALPI-dæmonen ikke kører. Controlleren arbejder uafhængigt uden kommunikation med softwaren.

#### Kendetegn ved Solo-tilstand

- **Ingen kommunikation med software er nødvendig**
- **Grundlæggende beskyttelse mod strømsvigt** – overvåger indgangsspændingen og reagerer på strømsvigt
- **Automatisk nedlukning via simulerede tryk på tænd/sluk-knappen**
- **Begrænsede muligheder for overvågning og konfiguration**

#### Strømsvigt og nedlukning i Solo-tilstand

**Registrering af strømsvigt:**
Controlleren overvåger indgangsspændingen og registrerer strømsvigt. En strømafbrydelsestimer (standard 5 sekunder) forhindrer nedlukning ved korte afbrydelser.

**Automatisk nedlukningsforløb:**

1. **Controlleren registrerer strømsvigt**
2. **Strømafbrydelsestimeren aktiveres** for at skelne korte udfald fra reelt strømsvigt
3. **Simulerede tryk på tænd/sluk-knappen** – controlleren sender et dobbelttryk på tænd/sluk-knappen til Compute Module
4. **Styresystemet reagerer** og påbegynder en kontrolleret nedlukning
5. **Superkondensatorerne opretholder forsyningen** (typisk 30–60 sekunder til rådighed)
6. **Timeoutbeskyttelse på 60 sekunder** – tvungen slukning, hvis den kontrollerede nedlukning mislykkes
7. **Systemet forbliver slukket**, indtil strømmen vender tilbage
8. **Automatisk genstart**, når strømmen er retableret

**Manuel nedlukning i Solo-tilstand:**

- Der sker en normal nedlukning af styresystemet
- Systemet genstarter automatisk efter 5 sekunder, hvis der stadig er strøm på indgangen
- Hvis systemet skal forblive slukket, skal du frakoble indgangsstrømmen, efter at den kontrollerede nedlukning er sat i gang

#### Hvornår Solo-tilstand er aktiv

Solo-tilstand optræder:

- Under den første opstart, før HALPI-dæmonen starter
- Hvis HALPI-dæmonen ikke kan starte eller er deaktiveret
- På styresystemer uden understøttelse, hvor dæmonen ikke findes
- Når dæmonen er gået ned eller ikke svarer

!!! tip "Driftssikkerhed i Solo-tilstand"
    Solo-tilstand giver den nødvendige grundbeskyttelse, men er mindre driftssikker end Co-op-tilstand. Controlleren er afhængig af simulerede knaptryk for at bede om nedlukning, og det virker måske ikke, hvis systemet er frosset.

### Drift i Co-op-tilstand

Co-op-tilstand giver fuld funktionalitet til strømstyring, når HALPI-dæmonen kører og kommunikerer med controlleren.

#### Funktioner i Co-op-tilstand

- **Direkte kommunikation med softwaren** – udveksling af data i realtid mellem controller og dæmon
- **Beskyttelse med watchdog-timer** – et timeout på 30 sekunder sikrer systemets stabilitet
- **Konfigurerbar nedlukningsadfærd** – tidsforløb og kommandoer kan tilpasses
- **Overvågning i realtid** – omfattende overvågning af strømparametre
- **Avancerede konfigurationsmuligheder**

#### Strømsvigt og nedlukning i Co-op-tilstand

**Registrering af strømsvigt:**
Controlleren overvåger den tilførte strøm og melder hændelser direkte til HALPI-dæmonen. Den konfigurerbare strømafbrydelsestimer (standard 5 sekunder) tillader korte strømafbrydelser, uden at nedlukningen sættes i gang.

**Automatisk nedlukningsforløb:**

1. **Controlleren registrerer strømsvigt** og melder det til HALPI-dæmonen
2. **Vurdering med strømafbrydelsestimeren** – dæmonen vurderer, om strømsvigtet overstiger tærsklen
3. **Udførelse af nedlukningskommandoen** – dæmonen kører nedlukningskommandoen (standard: `/sbin/poweroff`)
4. **Kontrolleret nedlukning af styresystemet** – programmer lukkes, og filsystemer afmonteres sikkert
5. **Backupstrøm fra superkondensatorerne** leverer energi under hele nedlukningen
6. **Controlleren følger forløbet** – den holder øje med, hvornår Compute Module slukker
7. **5 V-skinnen deaktiveres**, når nedlukningen er gennemført
8. **Systemet forbliver slukket**, indtil den tilførte strøm vender tilbage
9. **Styring af genstart** – afhængigt af konfigurationen genstarter systemet automatisk eller forbliver slukket

**Manuel nedlukning i Co-op-tilstand:**

- Der sker en normal kontrolleret nedlukning, når den sættes i gang via softwaren
- Systemet genstarter automatisk efter 5 sekunder, hvis der stadig er strøm på indgangen
- Hvis du vil forhindre automatisk genstart, skal du frakoble strømmen eller sætte `auto_restart` til `false`

#### Watchdog-beskyttelse

Co-op-tilstand omfatter beskyttelse med en watchdog-timer:

- **Kommunikationstimeout på 30 sekunder** – dæmonen skal kommunikere regelmæssigt med controlleren
- **Automatisk genopretning** – systemet genstarter, hvis kommunikationen ophører
- **Beskyttelse mod softwarefejl** – sikrer genopretning, hvis dæmonen går ned, eller systemet hænger
- **»Fodring af watchdoggen«** – dæmonen sender regelmæssige statusopdateringer, der nulstiller timeren

#### Hvornår Co-op-tilstand er aktiv

Co-op-tilstand optræder, når:

- HALPI-dæmonen kører og fungerer korrekt
- Der er etableret kommunikation mellem dæmonen og controlleren
- Systemet kører på et understøttet styresystem
- Alle funktioner til overvågning og styring af systemet er til rådighed

!!! info "Sådan kontrollerer du Co-op-tilstand"
    Kontrollér dæmonens status: `systemctl status halpid`

    Se controllerens tilstand: `halpi status`

    Du kan læse mere om kommandoen `halpi` i [Softwarevejledningen](./software.md#halpi-dmonen-halpid).

### Backupstrøm og kondensatorsystem

Begge tilstande er afhængige af backupsystemet med superkondensatorer for at kunne lukke kontrolleret ned:

**Backupstrømmens varighed:**

- Superkondensatorerne leverer 30–60 sekunders backupstrøm
- Varigheden afhænger af systemets belastning og de tilsluttede periferienheder
- Tilstrækkelig tid til at lukke filsystemet sikkert og afslutte processerne
- Ikke beregnet til fortsat drift under længerevarende afbrydelser

**Opladningsegenskaber:**

- Opladningstid: 25 sekunder ved en strømgrænse på 0,9 A
- Opladningstid: 9 sekunder ved en strømgrænse på 2,5 A
- Opladningens forløb vises visuelt gennem LED-forløbet (rødt udfyldningsmønster)

!!! warning "Begrænsning i beskyttelsen mod strømsvigt"
    Systemet med superkondensatorer er beregnet til kontrolleret nedlukning, ikke til fortsat drift. Stol ikke på det ved længerevarende strømafbrydelser.

### Overvejelser ved manuel nedlukning

HALPI2 prioriterer automatisk drift og genopretning, og det påvirker adfærden ved manuel nedlukning.

#### Adfærd ved automatisk genstart

Som standard genstarter HALPI2 efter en manuel nedlukning, hvis der stadig er strøm på indgangen:

- En manuel nedlukning giver en normal nedlukning af styresystemet
- Der følger en henstandsperiode på 5 sekunder, når nedlukningen er gennemført
- Systemet genstarter automatisk for at opretholde driften
- Det sikrer genopretning efter utilsigtede nedlukninger

#### Metoder til bevidst nedlukning

Hvis systemet skal forblive slukket, kan du bruge en af disse fremgangsmåder:

**Metode med frakobling af strømmen:**

1. Sæt en kontrolleret nedlukning i gang via softwaren
2. Vent, til nedlukningen er gennemført (LED'erne slukker)
3. Frakobl indgangsstrømmen for at forhindre automatisk genstart

**Metode med konfiguration:**

1. Deaktivér automatisk genstart: `halpi config set auto_restart false`
2. Sæt nedlukningen i gang via softwaren
3. Systemet forbliver slukket, når nedlukningen er gennemført

**Standby-tilstand (kommende):**
!!! info "Funktionens status"
    Standby-tilstand er planlagt til kommende firmwareudgivelser. Den vil gøre det muligt at slukke Compute Module, mens HALPI2-controlleren forbliver aktiv og venter på opvækningshændelser.

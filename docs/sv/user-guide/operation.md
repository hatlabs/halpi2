# Systemdrift

## Status-LED:ar

HALPI2 har fem RGB-lysdioder som visar systemets och strömförsörjningens tillstånd.

### Snabbguide till lysdioderna

| LED-mönster | Färg | Betydelse |
|-------------|------|-----------|
| LED 5 lyser fast | Röd | Spänning på, väntar på laddning |
| Successiv fyllning | Röd | Superkondensatorerna laddas |
| Regnbåge med färgväxling | Flerfärgad | CM5 startade inte |
| Spänningsstapel | Gul | Drift i sololäge |
| Spänningsstapel | Grön | Drift i co-op-läge |
| Spänningsstapel | Orange | Backupström aktiv (solo) |
| Spänningsstapel | Mörkgrön | Backupström aktiv (co-op) |
| Alla blinkar | Röd | Överspänning i superkondensatorerna |
| Alla lyser fast | Röd | Watchdog löste ut |
| Spänningsstapel | Violett | Avstängning pågår |
| Alla lyser fast | Blå | Övergång till vänteläge pågår |
| Alla lyser fast | Dämpad röd | Vänteläge |
| Alla släckta | — | Systemet avstängt |

### Spänningsindikering för superkondensatorerna

Under drift fungerar lysdioderna som spänningsmätare och visar superkondensatorernas laddningsnivå:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Strömhantering och avstängning

HALPI2 har en strömförsörjning som är konstruerad för att klara spänningstoppar, störningar och korta avbrott.

### Översikt över strömförsörjningen

HALPI2:s strömhantering består av:

- **En strömförsörjning med brett område** (ingång 11–32 V DC, skydd upp till 100 V DC)
- **Backup med superkondensatorer** för kontrollerad avstängning vid spänningsbortfall
- **Strömbegränsning** (0,9 A eller 2,5 A, valbart)
- **Detektering av spänningsbortfall** och automatisk start av avstängningen
- **Övervakning av inspänning och inström**

Systemet arbetar i två lägen: sololäge och co-op-läge.

### Sololäge

Sololäget ger en grundläggande självständig drift när HALPI-daemonen inte körs. Styrkretsen arbetar på egen hand, utan kontakt med programvaran.

#### Sololägets egenskaper

- **Kräver ingen kommunikation med programvaran**
- **Grundläggande skydd mot spänningsbortfall** — övervakar inspänningen och reagerar på avbrott
- **Automatisk avstängning via simulerade tryck på strömknappen**
- **Begränsade möjligheter till övervakning och konfiguration**

#### Spänningsbortfall och avstängning i sololäge

**Detektering av spänningsbortfall:**
Styrkretsen övervakar inspänningen och upptäcker avbrott. En avbrottstimer (5 sekunder som standard) hindrar avstängning vid korta störningar.

**Automatisk avstängningssekvens:**

1. **Styrkretsen upptäcker spänningsbortfallet**
2. **Avbrottstimern startar**, för att skilja en kort störning från ett verkligt bortfall
3. **Simulerade tryck på strömknappen** — styrkretsen skickar ett dubbeltryck till Compute Module
4. **Operativsystemet reagerar** och påbörjar en kontrollerad avstängning
5. **Superkondensatorerna håller uppe spänningen** (normalt 30 till 60 sekunder)
6. **Skydd med 60 sekunders tidsgräns** — framtvingad avstängning om den kontrollerade avstängningen misslyckas
7. **Systemet förblir avstängt** tills spänningen återvänder
8. **Automatisk omstart** när spänningen är tillbaka

**Manuell avstängning i sololäge:**

- Operativsystemet stängs av på vanligt sätt
- Systemet startar om automatiskt efter 5 sekunder om inspänningen fortfarande finns
- För permanent avstängning kopplar du bort inspänningen efter att ha startat den kontrollerade avstängningen

#### När sololäget är aktivt

Sololäget gäller:

- allra först vid start, innan HALPI-daemonen har startat;
- om HALPI-daemonen inte startar eller är avstängd;
- på operativsystem som saknar daemonen;
- när daemonen har kraschat eller slutat svara.

!!! tip "Solulägets tillförlitlighet"
    Sololäget ger ett nödvändigt skydd men är mindre tillförlitligt än co-op-läget. Styrkretsen begär avstängning med simulerade knapptryck, vilket kanske inte fungerar om systemet har hängt sig.

### Co-op-läge

Co-op-läget ger full strömhantering när HALPI-daemonen körs och kommunicerar med styrkretsen.

#### Co-op-lägets funktioner

- **Direkt kommunikation med programvaran** — utbyte av data i realtid mellan styrkrets och daemon
- **Skydd med watchdog** — en tidsgräns på 30 sekunder säkerställer systemets stabilitet
- **Konfigurerbart avstängningsbeteende** — tider och kommandon går att justera
- **Övervakning i realtid** — omfattande uppföljning av strömförsörjningens värden
- **Avancerade konfigurationsmöjligheter**

#### Spänningsbortfall och avstängning i co-op-läge

**Detektering av spänningsbortfall:**
Styrkretsen övervakar inspänningen och rapporterar händelser direkt till HALPI-daemonen. Den konfigurerbara avbrottstimern (5 sekunder som standard) tillåter korta avbrott utan att avstängningen startar.

**Automatisk avstängningssekvens:**

1. **Styrkretsen upptäcker spänningsbortfallet** och meddelar HALPI-daemonen
2. **Bedömning av avbrottstimern** — daemonen avgör om avbrottet överskrider tröskeln
3. **Avstängningskommandot körs** — daemonen kör det inställda kommandot (som standard `/sbin/poweroff`)
4. **Kontrollerad avstängning av operativsystemet** — program avslutas och filsystem avmonteras säkert
5. **Backupströmmen från superkondensatorerna** räcker under hela avstängningen
6. **Styrkretsen följer förloppet** — den märker när Compute Module stängs av
7. **5 V-skenan stängs av** när avstängningen är klar
8. **Systemet förblir avstängt** tills inspänningen återvänder
9. **Hantering av omstart** — beroende på konfigurationen startar systemet om automatiskt eller förblir avstängt

**Manuell avstängning i co-op-läge:**

- En avstängning som startas från programvaran sker kontrollerat
- Systemet startar om automatiskt efter 5 sekunder om inspänningen fortfarande finns
- För att förhindra automatisk omstart kopplar du bort spänningen eller sätter `auto_restart` till `false`

#### Skydd med watchdog

Co-op-läget innehåller en watchdog:

- **Kommunikationsgräns på 30 sekunder** — daemonen måste höra av sig till styrkretsen regelbundet
- **Automatisk återhämtning** — systemet startar om om kommunikationen upphör
- **Skydd mot programvarufel** — säkerställer återhämtning efter att daemonen kraschat eller systemet hängt sig
- **”Mata watchdogen”** — daemonen skickar regelbundna statusmeddelanden som nollställer timern

#### När co-op-läget är aktivt

Co-op-läget gäller när:

- HALPI-daemonen körs och fungerar normalt;
- kommunikationen mellan daemon och styrkrets är upprättad;
- systemet kör ett operativsystem som stöds;
- alla övervaknings- och styrfunktioner är tillgängliga.

!!! info "Kontrollera co-op-läget"
    Daemonens status: `systemctl status halpid`

    Styrkretsens tillstånd: `halpi status`

    Mer om kommandot `halpi` finns i [Programvaruguiden](./software.md#halpi-daemon-halpid).

### Backupström och kondensatorsystem

Båda lägena bygger på superkondensatorerna för att säkra en kontrollerad avstängning:

**Backupströmmens varaktighet:**

- Superkondensatorerna ger 30 till 60 sekunders backuptid
- Tiden beror på systemets belastning och anslutna kringenheter
- Den räcker för att stänga filsystemet och avsluta processer säkert
- Den är inte avsedd för fortsatt drift under längre avbrott

**Laddningsegenskaper:**

- Laddningstid: 25 sekunder vid strömbegränsning 0,9 A
- Laddningstid: 9 sekunder vid strömbegränsning 2,5 A
- Laddningsförloppet syns genom att lysdioderna fylls (rött fyllningsmönster)

!!! warning "Begränsning i skyddet mot spänningsbortfall"
    Systemet med superkondensatorer är avsett för kontrollerad avstängning, inte för fortsatt drift. Lita inte på det vid längre strömavbrott.

### Att tänka på vid manuell avstängning

HALPI2 prioriterar automatisk drift och återhämtning, vilket påverkar hur en manuell avstängning beter sig.

#### Automatisk omstart

Som standard startar HALPI2 om efter en manuell avstängning om inspänningen fortfarande finns:

- En manuell avstängning stänger av operativsystemet på vanligt sätt
- Efter avslutad avstängning följer en väntetid på 5 sekunder
- Systemet startar om automatiskt för att förbli tillgängligt
- Det säkerställer återhämtning efter en avstängning av misstag

#### Så stänger du av enheten permanent

Det finns två sätt:

**Koppla bort spänningen:**

1. Starta en kontrollerad avstängning från programvaran
2. Vänta tills avstängningen är klar (lysdioderna släcks)
3. Koppla bort inspänningen för att förhindra automatisk omstart

**Ändra konfigurationen:**

1. Stäng av automatisk omstart: `halpi config set auto_restart false`
2. Starta avstängningen från programvaran
3. Systemet förblir avstängt efter avslutad avstängning

**Vänteläge (kommande):**

!!! info "Funktionens status"
    Vänteläget planeras till kommande firmwareversioner. Det kommer att göra det möjligt att stänga av Compute Module medan HALPI2:s styrkrets förblir aktiv och väntar på väckningshändelser.

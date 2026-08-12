---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Bärkortets styrkrets

HALPI2:s bärkort har en RP2040-mikrokontroller som hanterar strömmen, övervakar systemet och styr frontpanelens lysdioder. Styrkretsen arbetar oberoende av Compute Module: den är i drift från det ögonblick inspänningen ansluts, innan operativsystemet har startat och efter att det har stängts av. Compute Module kommunicerar med den över I2C (buss 1, adress `0x6d`) genom [HALPI-daemonen](../user-guide/software.md#kommandoradsverktyget-halpi).

Den här sidan beskriver styrkretsens driftlägen, tillståndsövergångar och konfiguration. Den dokumenterar firmwareversion 3.3.x. För den dagliga användningen behöver inget av detta läsas — se i stället [Daglig användning](../user-guide/operation.md).

## Driftlägen

Styrkretsen arbetar i ett av två lägen, beroende på om HALPI-daemonen kommunicerar med den.

### Co-op-läge

Co-op-läget är det normala driftläget. Det är aktivt när HALPI-daemonen (`halpid`) körs och kommunicerar med styrkretsen. Den förinstallerade HaLOS-avbilden och alla Hat Labs OS-avbilder innehåller daemonen.

I co-op-läget:

- Styrkretsen och daemonen utbyter data i realtid: spänningar, ström, temperaturer och tillstånd.
- Spänningsbortfall meddelas daemonen, som startar en kontrollerad avstängning av operativsystemet.
- Watchdog-timern skyddar mot att operativsystemet hänger sig (se [Skydd med watchdog](#skydd-med-watchdog)).
- Konfigurationen kan läsas och ändras med kommandoradsverktyget `halpi`.

### Sololäge

Sololäget är reservläget. Styrkretsen går in i det när det inte finns någon kommunikation med daemonen:

- under starten, innan daemonen har startat
- om daemonen inte är installerad, är avstängd eller har kraschat
- på operativsystem utan HALPI2-stöd

I sololäget skyddar styrkretsen fortfarande mot spänningsbortfall, men med en trubbigare mekanism: den begär avstängning genom att simulera tryck på strömknappen, och den kan inte avgöra om operativsystemet faktiskt slutförde avstängningen kontrollerat.

!!! tip "Sololägets tillförlitlighet"
    Sololäget ger ett nödvändigt skydd men är mindre tillförlitligt än co-op-läget. Simulerade knapptryck fungerar inte om operativsystemet har hängt sig. Om du kör ett eget operativsystem, installera HALPI-daemonen — se [Andra Debian-distributioner](../software-development/ubuntu-installation.md).

## Spänningsbortfall och avstängningssekvenser

Styrkretsen övervakar inspänningen kontinuerligt. Inspänningen betraktas som borta när den faller under 9,0 V. En avbrottstimer (5 sekunder som standard) skiljer korta störningar från verkliga avbrott: superkondensatorerna överbryggar glappet, och om strömmen kommer tillbaka inom timerns tid händer inget mer.

### Avstängningssekvens i co-op-läge

1. Daemonen upptäcker spänningsbortfallet ur styrkretsens spänningsmätningar.
2. Daemonen väntar tills avbrottstidsgränsen (5 sekunder som standard) har passerat.
3. Daemonen kör det inställda avstängningskommandot (som standard `/sbin/poweroff`).
4. Operativsystemet stängs av kontrollerat på superkondensatorernas ström.
5. Styrkretsen upptäcker att Compute Module har stängts av och stänger av 5 V-skenan.
6. Om avstängningen inte är klar inom 60 sekunder framtvingar styrkretsen en avstängning.
7. Systemet förblir avstängt tills inspänningen kommer tillbaka, och startar då om automatiskt.

### Avstängningssekvens i sololäge

1. Styrkretsen upptäcker spänningsbortfallet och startar avbrottstimern (5 sekunder som standard).
2. När timern löper ut simulerar styrkretsen ett dubbelt tryck på strömknappen.
3. Operativsystemet reagerar och påbörjar en kontrollerad avstängning på superkondensatorernas ström.
4. Om avstängningen inte är klar inom 60 sekunder framtvingar styrkretsen en avstängning.
5. Systemet förblir avstängt tills inspänningen kommer tillbaka, och startar då om automatiskt.

### Omstartsbeteende efter avstängning via programvara

En avstängning som startas via programvaran medan inspänningen finns kvar (till exempel kommandot `shutdown` eller skrivbordsmenyn) slutar i tillståndet *avstängd*. Vad som händer sedan beror på konfigurationsinställningen `auto_restart`:

- `auto_restart` avstängd (fabriksinställningen på enheter tillverkade sedan början av 2026): systemet förblir avstängt tills inspänningen bryts och återansluts eller en strömknapp trycks in.
- `auto_restart` aktiverad (firmwarens reservvärde, och fabriksinställningen på äldre enheter): styrkretsen startar om systemet efter 5 sekunder, så att ett system utan tillsyn inte blir stående avstängt på grund av ett avstängningskommando av misstag.

Ändra inställningen med `halpi config set auto_restart <true|false>`.

Ett tryck på strömknappen, eller att inspänningen bryts och återansluts, startar alltid om systemet, oavsett inställningen av `auto_restart`.

## Skydd med watchdog

I co-op-läget skyddar en watchdog-timer mot att operativsystemet hänger sig:

- Daemonen måste mata styrkretsens watchdog med jämna mellanrum.
- Om ingen matning kommer inom watchdog-tidsgränsen (10 sekunder som standard) anser styrkretsen att värddatorn inte längre svarar, visar larmmönstret på lysdioderna (alla lyser fast rött) och bryter och återansluter strömmen till Compute Module för att återställa systemet.
- Tidsgränsen kan konfigureras med `halpi config set watchdog_timeout <seconds>`.

## Vänteläge

Vänteläget stänger av Compute Module medan styrkretsen förblir aktiv och väntar på en schemalagd väckning:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Under övergången lyser alla lysdioder fast blått; i vänteläget lyser de dämpat rött. Styrkretsen startar om systemet vid den schemalagda tidpunkten, vid ett tryck på strömknappen eller efter att inspänningen brutits och återanslutits.

## Status-LED-referens

De fem RGB-lysdioderna på frontpanelen speglar styrkretsens tillstånd. Den här tabellen är den auktoritativa mappningen från styrkretsens tillstånd till LED-mönster; sidan [Daglig användning](../user-guide/operation.md#status-ledar) visar en förenklad version.

| Styrkretsens tillstånd | LED-mönster |
|:-----------------------|:------------|
| PowerOff (ingen användbar inspänning; styrkretsen går på restladdning) | LED 5 lyser fast rött |
| OffCharging | Röd stapel som fylls medan superkondensatorerna laddas |
| SystemStartup | Regnbågssvep, därefter en cykel av fasta färger |
| OperationalSolo | Gul laddningsstapel |
| OperationalCoOp | Grön laddningsstapel |
| BlackoutSolo | Orange laddningsstapel |
| BlackoutCoOp | Mörkgrön laddningsstapel |
| BlackoutShutdown, ManualShutdown | Violett laddningsstapel |
| PoweredDownBlackout, PoweredDownManual | Alla släckta |
| HostUnresponsive (watchdog-timeout) | Alla lyser fast rött |
| EnteringStandby | Alla lyser fast blått |
| Standby | Alla lyser dämpat rött |
| Överspänningslarm för superkondensatorerna | Alla lysdioder blinkar rött |

I laddningsstapelmönstren motsvarar varje tänd lysdiod en volt av superkondensatorernas spänning:

| LED | Spänningsområde |
|:----|:----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Konfigurationsparametrar

Konfigurationen lagras i styrkretsens flashminne och överlever att strömmen bryts. Läs och ändra den med `halpi config` — se [Programvaruguiden](../user-guide/software.md#hantering-av-konfigurationen).

| Parameter | Standardvärde | Beskrivning |
|:----------|:--------------|:------------|
| `auto_restart` | `false` på nuvarande enheter (sätts vid produktionstestet); firmwarens reservvärde `true` | Starta om automatiskt 5 s efter en avstängning via programvara medan inspänning finns |
| `watchdog_timeout` | 10 s | Watchdog-tidsgräns i co-op-läget |
| `power_on_threshold` | 8,0 V | Superkondensatorspänning som krävs innan Compute Module slås på |
| `solo_power_off_threshold` | 5,5 V | Superkondensatorspänning vid vilken styrkretsen framtvingar avstängning i sololäget |
| `solo_depleting_timeout` | 5 s | Sololägets avbrottstimer |
| `led_brightness` | 48 | Ljusstyrka för frontpanelens lysdioder (0–255) |

Avbrottstimern och avstängningskommandot i co-op-läget är daemoninställningar och konfigureras i `/etc/halpid/halpid.conf` (`blackout-time-limit`, standard 5 s; `poweroff`, standard `/sbin/poweroff`).

!!! quote "Relaterad information"
    - **Daglig användning:** se [Daglig användning](../user-guide/operation.md)
    - **Strömförsörjningens detaljer:** se [Strömförsörjningen i detalj](./power-supply.md)
    - **Firmwareuppdateringar:** se [Programvaruguiden](../user-guide/software.md#firmwareuppdateringar)
    - **Firmwarens källkod och I2C-protokoll:** se [HALPI2-firmware-repositoriet](https://github.com/hatlabs/HALPI2-firmware)

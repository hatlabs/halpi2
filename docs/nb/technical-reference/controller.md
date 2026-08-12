---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Bærekortets mikrokontroller

HALPI2-bærekortet har en RP2040-mikrokontroller som styrer strømmen, overvåker systemet og kontrollerer LED-ene på frontpanelet. Kontrolleren kjører uavhengig av Compute Module: den er i drift fra det øyeblikket inngangsstrøm kobles til, før operativsystemet starter opp og etter at det har stengt ned. Compute Module kommuniserer med den over I2C (buss 1, adresse `0x6d`) gjennom [HALPI-daemonen](../user-guide/software.md#halpi-kommandolinjeverktyet).

Denne siden beskriver kontrollerens driftsmoduser, tilstandsoverganger og konfigurasjon. Den dokumenterer firmwareversjon 3.3.x. For daglig bruk er ingenting av dette nødvendig lesning – se heller [Daglig bruk](../user-guide/operation.md).

## Driftsmoduser

Kontrolleren opererer i én av to moduser, avhengig av om HALPI-daemonen kommuniserer med den.

### Samspillsmodus

Samspillsmodus (co-op mode) er den normale driftsmodusen. Den er aktiv når HALPI-daemonen (`halpid`) kjører og kommuniserer med kontrolleren. Det forhåndsinstallerte HaLOS-systembildet og alle operativsystembilder fra Hat Labs inkluderer daemonen.

I samspillsmodus:

- Kontrolleren og daemonen utveksler sanntidsdata: spenninger, strøm, temperaturer og tilstand.
- Strømbortfall meldes til daemonen, som starter en kontrollert nedstenging av operativsystemet.
- Watchdog-timeren beskytter mot at operativsystemet henger (se [Watchdog-beskyttelse](#watchdog-beskyttelse)).
- Konfigurasjonen kan leses og endres med kommandolinjeverktøyet `halpi`.

### Solomodus

Solomodus (solo mode) er reservemodusen. Kontrolleren går inn i den når det ikke er noen kommunikasjon med daemonen:

- under oppstart, før daemonen starter
- hvis daemonen ikke er installert, er deaktivert eller har krasjet
- på operativsystemer uten HALPI2-støtte

I solomodus beskytter kontrolleren fortsatt mot strømbortfall, men med en grovere mekanisme: den ber om nedstenging ved å simulere trykk på strømknappen, og den kan ikke vite om operativsystemet faktisk fullførte nedstengingen kontrollert.

!!! tip "Pålitelighet i solomodus"
    Solomodus gir nødvendig grunnbeskyttelse, men er mindre pålitelig enn samspillsmodus. Simulerte knappetrykk virker ikke hvis operativsystemet har låst seg. Hvis du kjører et eget operativsystem, bør du installere HALPI-daemonen – se [Andre Debian-distribusjoner](../software-development/ubuntu-installation.md).

## Strømbortfall og nedstengingssekvenser

Kontrolleren overvåker inngangsspenningen kontinuerlig. Inngangsstrømmen regnes som tapt når inngangsspenningen faller under 9,0 V. En strømbruddstimer (standard 5 sekunder) skiller korte forstyrrelser fra virkelige strømbrudd: superkondensatorene dekker gapet, og hvis strømmen kommer tilbake innenfor timerperioden, skjer det ikke noe mer.

### Nedstengingssekvens i samspillsmodus

1. Daemonen oppdager strømbortfallet ut fra kontrollerens spenningsmålinger.
2. Daemonen venter til tidsgrensen for strømbrudd (standard 5 sekunder) er passert.
3. Daemonen kjører den konfigurerte nedstengingskommandoen (standard `/sbin/poweroff`).
4. Operativsystemet stenger kontrollert ned på strøm fra superkondensatorene.
5. Kontrolleren registrerer at Compute Module har slått seg av, og deaktiverer 5 V-skinnen.
6. Hvis nedstengingen ikke er fullført innen 60 sekunder, tvinger kontrolleren strømmen av.
7. Systemet forblir av til inngangsstrømmen kommer tilbake, og starter deretter automatisk igjen.

### Nedstengingssekvens i solomodus

1. Kontrolleren oppdager strømbortfallet og starter strømbruddstimeren (standard 5 sekunder).
2. Når timeren løper ut, simulerer kontrolleren et dobbelttrykk på strømknappen.
3. Operativsystemet reagerer og begynner en kontrollert nedstenging på strøm fra superkondensatorene.
4. Hvis nedstengingen ikke er fullført innen 60 sekunder, tvinger kontrolleren strømmen av.
5. Systemet forblir av til inngangsstrømmen kommer tilbake, og starter deretter automatisk igjen.

### Omstart etter nedstenging fra programvaren

En nedstenging startet gjennom programvaren mens inngangsstrømmen fortsatt er tilgjengelig (for eksempel med kommandoen `shutdown` eller fra skrivebordsmenyen), ender i tilstanden *powered down* (avslått). Hva som skjer videre, avhenger av konfigurasjonsinnstillingen `auto_restart`:

- `auto_restart` deaktivert (fabrikkinnstillingen på enheter produsert fra tidlig i 2026): systemet forblir av til inngangsstrømmen kobles ut og inn igjen eller en strømknapp trykkes.
- `auto_restart` aktivert (reserveverdien i firmwaren, og fabrikkinnstillingen på tidligere enheter): kontrolleren starter systemet igjen etter 5 sekunder, slik at et system uten tilsyn ikke blir stående avslått på grunn av en utilsiktet nedstengingskommando.

Endre innstillingen med `halpi config set auto_restart <true|false>`.

Et trykk på strømknappen eller ut- og innkobling av inngangsstrømmen starter alltid systemet igjen, uavhengig av innstillingen `auto_restart`.

## Watchdog-beskyttelse

I samspillsmodus beskytter en watchdog-timer mot at operativsystemet henger:

- Daemonen må mate watchdogen i kontrolleren med jevne mellomrom.
- Hvis ingen mating kommer innenfor watchdog-tidsavbruddet (standard 10 sekunder), regner kontrolleren verten som ikke-svarende, viser varselmønsteret på LED-ene (alle LED-er lyser fast rødt) og slår strømmen til Compute Module av og på for å gjenopprette driften.
- Tidsavbruddet kan konfigureres med `halpi config set watchdog_timeout <seconds>`.

## Ventemodus

Ventemodus (standby) slår av Compute Module mens kontrolleren forblir aktiv og venter på en planlagt oppvekking:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Under overgangen lyser alle LED-ene fast blått; i ventemodus lyser de svakt rødt. Kontrolleren starter systemet igjen på det planlagte tidspunktet, ved et trykk på strømknappen eller etter ut- og innkobling av inngangsstrømmen.

## Status-LED-referanse

De fem RGB-LED-ene på frontpanelet gjenspeiler kontrollerens tilstand. Denne tabellen er den autoritative tilordningen fra kontrollertilstander til LED-mønstre; siden [Daglig bruk](../user-guide/operation.md#status-led-indikatorer) presenterer en forenklet utgave.

| Kontrollertilstand | LED-mønster |
|:-------------------|:------------|
| PowerOff (ingen brukbar inngangsstrøm; kontrolleren kjører på restlading) | LED 5 lyser fast rødt |
| OffCharging | Rød søyle som fylles mens superkondensatorene lades |
| SystemStartup | Regnbuesveip, deretter en syklus med ensfargede lys |
| OperationalSolo | Gul ladenivåsøyle |
| OperationalCoOp | Grønn ladenivåsøyle |
| BlackoutSolo | Oransje ladenivåsøyle |
| BlackoutCoOp | Mørkegrønn ladenivåsøyle |
| BlackoutShutdown, ManualShutdown | Lilla ladenivåsøyle |
| PoweredDownBlackout, PoweredDownManual | Alle av |
| HostUnresponsive (watchdog-tidsavbrudd) | Alle lyser fast rødt |
| EnteringStandby | Alle lyser fast blått |
| Standby | Alle lyser svakt rødt |
| Overspenningsalarm for superkondensatorene | Alle LED-er blinker rødt |

I ladenivåsøylene representerer hver tent LED én volt superkondensatorspenning:

| LED | Spenningsområde |
|:----|:----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Konfigurasjonsparametere

Konfigurasjonen lagres i kontrollerens flashminne og beholdes når strømmen kobles ut og inn. Les og endre den med `halpi config` – se [programvareveiledningen](../user-guide/software.md#konfigurasjonsstyring).

| Parameter | Standard | Beskrivelse |
|:----------|:---------|:------------|
| `auto_restart` | `false` på nåværende enheter (settes under produksjonstesten); reserveverdi i firmwaren `true` | Start automatisk igjen 5 s etter en nedstenging fra programvaren mens inngangsstrøm er til stede |
| `watchdog_timeout` | 10 s | Watchdog-tidsavbrudd i samspillsmodus |
| `power_on_threshold` | 8,0 V | Superkondensatorspenningen som kreves før Compute Module slås på |
| `solo_power_off_threshold` | 5,5 V | Superkondensatorspenningen der kontrolleren tvinger strømmen av i solomodus |
| `solo_depleting_timeout` | 5 s | Strømbruddstimeren i solomodus |
| `led_brightness` | 48 | Lysstyrken på LED-ene på frontpanelet (0–255) |

Strømbruddstimeren og nedstengingskommandoen i samspillsmodus er innstillinger i daemonen og konfigureres i `/etc/halpid/halpid.conf` (`blackout-time-limit`, standard 5 s; `poweroff`, standard `/sbin/poweroff`).

!!! quote "Relatert informasjon"
    - **Hverdagsbruk:** Se [Daglig bruk](../user-guide/operation.md)
    - **Detaljer om strømsystemet:** Se [Strømforsyningen i detalj](./power-supply.md)
    - **Firmware-oppdateringer:** Se [programvareveiledningen](../user-guide/software.md#firmware-oppdateringer)
    - **Firmware-kildekoden og I2C-protokollen:** Se [HALPI2-firmware-repositoriet](https://github.com/hatlabs/HALPI2-firmware)

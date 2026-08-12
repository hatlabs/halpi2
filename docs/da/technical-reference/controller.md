---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Bærekortets controller

HALPI2-bærekortet har en RP2040-mikrocontroller, der styrer strømmen, overvåger systemet og styrer LED'erne på frontpanelet. Controlleren kører uafhængigt af Compute Module: Den arbejder, fra det øjeblik indgangsstrømmen tilsluttes, før styresystemet starter op og efter, at det er lukket ned. Compute Module kommunikerer med den over I2C (bus 1, adresse `0x6d`) gennem [HALPI-dæmonen](../user-guide/software.md#halpi-kommandolinjevrktjet).

Denne side beskriver controllerens driftstilstande, tilstandsovergange og konfiguration. Den dokumenterer firmwareversion 3.3.x. Til daglig brug behøver du ikke at læse noget af det — se i stedet [Daglig brug](../user-guide/operation.md).

## Driftstilstande

Controlleren arbejder i én af to tilstande, afhængigt af om HALPI-dæmonen kommunikerer med den.

### Co-op-tilstand

Co-op-tilstand er den normale driftstilstand. Den er aktiv, når HALPI-dæmonen (`halpid`) kører og kommunikerer med controlleren. Det forudinstallerede HaLOS-image og alle Hat Labs' OS-images indeholder dæmonen.

I Co-op-tilstand:

- Controlleren og dæmonen udveksler data i realtid: spændinger, strøm, temperaturer og tilstand.
- Strømsvigt meldes til dæmonen, som sætter en kontrolleret nedlukning af styresystemet i gang.
- Watchdog-timeren beskytter mod, at styresystemet hænger (se [Watchdog-beskyttelse](#watchdog-beskyttelse)).
- Konfigurationen kan læses og ændres med kommandolinjeværktøjet `halpi`.

### Solo-tilstand

Solo-tilstand er reservetilstanden. Controlleren går i den, når der ikke er kommunikation med dæmonen:

- under opstart, før dæmonen starter
- hvis dæmonen ikke er installeret, er deaktiveret eller er gået ned
- på styresystemer uden HALPI2-understøttelse

I Solo-tilstand beskytter controlleren stadig mod strømsvigt, men med en mere primitiv mekanisme: Den beder om nedlukning ved at simulere tryk på tænd/sluk-knappen, og den kan ikke se, om styresystemet faktisk gennemførte nedlukningen kontrolleret.

!!! tip "Driftssikkerhed i Solo-tilstand"
    Solo-tilstand giver den nødvendige grundbeskyttelse, men er mindre driftssikker end Co-op-tilstand. Simulerede knaptryk virker ikke, hvis styresystemet er frosset. Hvis du kører dit eget styresystem, skal du installere HALPI-dæmonen — se [Andre Debian-distributioner](../software-development/ubuntu-installation.md).

## Strømsvigt og nedlukningsforløb

Controlleren overvåger indgangsspændingen løbende. Indgangsstrømmen betragtes som væk, når indgangsspændingen falder under 9,0 V. En strømafbrydelsestimer (standard 5 sekunder) skelner korte udfald fra reelle afbrydelser: Superkondensatorerne dækker hullet, og hvis strømmen vender tilbage inden for timerens periode, sker der ikke mere.

### Nedlukningsforløb i Co-op-tilstand

1. Dæmonen registrerer strømsvigtet ud fra controllerens spændingsmålinger.
2. Dæmonen venter, til strømafbrydelsestimerens grænse (standard 5 sekunder) er passeret.
3. Dæmonen kører den konfigurerede nedlukningskommando (standard `/sbin/poweroff`).
4. Styresystemet lukker kontrolleret ned på strøm fra superkondensatorerne.
5. Controlleren registrerer, at Compute Module er slukket, og deaktiverer 5 V-skinnen.
6. Hvis nedlukningen ikke er gennemført inden for 60 sekunder, gennemtvinger controlleren slukningen.
7. Systemet forbliver slukket, indtil indgangsstrømmen vender tilbage, og genstarter derefter automatisk.

### Nedlukningsforløb i Solo-tilstand

1. Controlleren registrerer strømsvigtet og starter strømafbrydelsestimeren (standard 5 sekunder).
2. Når timeren udløber, simulerer controlleren et dobbelttryk på tænd/sluk-knappen.
3. Styresystemet reagerer og påbegynder en kontrolleret nedlukning på strøm fra superkondensatorerne.
4. Hvis nedlukningen ikke er gennemført inden for 60 sekunder, gennemtvinger controlleren slukningen.
5. Systemet forbliver slukket, indtil indgangsstrømmen vender tilbage, og genstarter derefter automatisk.

### Genstartsadfærd efter en softwarenedlukning

En nedlukning, der sættes i gang via software, mens indgangsstrømmen stadig er til rådighed (for eksempel med kommandoen `shutdown` eller skrivebordsmenuen), ender i tilstanden *powered down* (slukket). Hvad der derefter sker, afhænger af konfigurationsindstillingen `auto_restart`:

- `auto_restart` deaktiveret (fabriksindstillingen på enheder produceret siden starten af 2026): Systemet forbliver slukket, indtil indgangsstrømmen har været afbrudt og tilsluttet igen, eller der trykkes på en tænd/sluk-knap.
- `auto_restart` aktiveret (firmwarens reserveindstilling og fabriksindstillingen på ældre enheder): Controlleren genstarter systemet efter 5 sekunder, så et system uden opsyn ikke forbliver slukket på grund af en utilsigtet nedlukning.

Skift indstillingen med `halpi config set auto_restart <true|false>`.

Et tryk på tænd/sluk-knappen eller en afbrydelse og gentilslutning af indgangsstrømmen genstarter altid systemet, uanset indstillingen af `auto_restart`.

## Watchdog-beskyttelse

I Co-op-tilstand beskytter en watchdog-timer mod, at styresystemet hænger:

- Dæmonen skal fodre watchdoggen med jævne mellemrum.
- Hvis der ikke kommer en fodring inden for watchdog-timeoutet (standard 10 sekunder), betragter controlleren værten som ikke-svarende, viser alarmmønsteret på LED'erne (alle lyser konstant rødt) og slukker og tænder Compute Module igen for at genoprette driften.
- Timeoutet kan konfigureres med `halpi config set watchdog_timeout <seconds>`.

## Standby

Standby slukker Compute Module, mens controlleren forbliver aktiv og venter på en planlagt opvækning:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Under overgangen lyser alle LED'er konstant blåt; i standby lyser de svagt rødt. Controlleren genstarter systemet på det planlagte tidspunkt, ved et tryk på tænd/sluk-knappen eller efter, at indgangsstrømmen har været afbrudt og tilsluttet igen.

## Status-LED-reference

De fem RGB-LED'er på frontpanelet afspejler controllerens tilstand. Denne tabel er den autoritative oversigt over sammenhængen mellem controllertilstande og LED-mønstre; siden [Daglig brug](../user-guide/operation.md#status-led-indikatorer) viser en forenklet udgave.

| Controllertilstand | LED-mønster |
|:-------------------|:------------|
| PowerOff (ingen brugbar indgangsstrøm; controlleren kører på restladning) | LED 5 lyser konstant rødt |
| OffCharging | Rød søjle, der fyldes op, mens superkondensatorerne oplader |
| SystemStartup | Regnbueforløb og derefter en cyklus af faste farver |
| OperationalSolo | Gul ladeniveausøjle |
| OperationalCoOp | Grøn ladeniveausøjle |
| BlackoutSolo | Orange ladeniveausøjle |
| BlackoutCoOp | Mørkegrøn ladeniveausøjle |
| BlackoutShutdown, ManualShutdown | Lilla ladeniveausøjle |
| PoweredDownBlackout, PoweredDownManual | Alle slukket |
| HostUnresponsive (watchdog-timeout) | Alle lyser konstant rødt |
| EnteringStandby | Alle lyser konstant blåt |
| Standby | Alle lyser svagt rødt |
| Alarm for overspænding på superkondensatorerne | Alle LED'er blinker rødt |

I ladeniveausøjlerne repræsenterer hver tændt LED én volt superkondensatorspænding:

| LED | Spændingsområde |
|:----|:----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Konfigurationsparametre

Konfigurationen gemmes i controllerens flashhukommelse og bevares, når strømmen slukkes og tændes igen. Læs og skift den med `halpi config` — se [Softwarevejledningen](../user-guide/software.md#konfigurationsstyring).

| Parameter | Standard | Beskrivelse |
|:----------|:---------|:------------|
| `auto_restart` | `false` på aktuelle enheder (sættes ved produktionstesten); firmwarens reserveindstilling er `true` | Genstart automatisk 5 s efter en softwarenedlukning, mens der er indgangsstrøm |
| `watchdog_timeout` | 10 s | Watchdog-timeout i Co-op-tilstand |
| `power_on_threshold` | 8,0 V | Den superkondensatorspænding, der kræves, før Compute Module tændes |
| `solo_power_off_threshold` | 5,5 V | Den superkondensatorspænding, hvor controlleren gennemtvinger slukning i Solo-tilstand |
| `solo_depleting_timeout` | 5 s | Strømafbrydelsestimeren i Solo-tilstand |
| `led_brightness` | 48 | Lysstyrke for LED'erne på frontpanelet (0–255) |

Strømafbrydelsestimeren og nedlukningskommandoen i Co-op-tilstand er dæmonindstillinger, som konfigureres i `/etc/halpid/halpid.conf` (`blackout-time-limit`, standard 5 s; `poweroff`, standard `/sbin/poweroff`).

!!! quote "Relaterede oplysninger"
    - **Hverdagsbrug:** Se [Daglig brug](../user-guide/operation.md)
    - **Detaljer om strømsystemet:** Se [Strømforsyningen i detaljer](./power-supply.md)
    - **Firmwareopdateringer:** Se [Softwarevejledningen](../user-guide/software.md#firmwareopdateringer)
    - **Firmwarekildekode og I2C-protokol:** Se [HALPI2-firmware-repositoriet](https://github.com/hatlabs/HALPI2-firmware)

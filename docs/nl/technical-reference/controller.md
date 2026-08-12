---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Controller van het carrierboard

Het HALPI2-carrierboard bevat een RP2040-microcontroller die de voeding beheert, het systeem bewaakt en de leds op het frontpaneel aanstuurt. De controller werkt onafhankelijk van de Compute Module: hij is actief vanaf het moment dat er ingangsspanning wordt aangesloten, voordat het besturingssysteem opstart en nadat het is afgesloten. De Compute Module communiceert met hem via I2C (bus 1, adres `0x6d`), via de [HALPI-daemon](../user-guide/software.md#halpi-opdrachtregelgereedschap).

Deze pagina beschrijft de bedrijfsmodi, de toestandsovergangen en de configuratie van de controller. Ze documenteert firmwareversie 3.3.x. Voor het dagelijks gebruik is niets hiervan verplichte lectuur — zie in plaats daarvan [Dagelijks gebruik](../user-guide/operation.md).

## Bedrijfsmodi

De controller werkt in een van twee modi, afhankelijk van of de HALPI-daemon met hem communiceert.

### Co-opmodus

De co-opmodus is de normale bedrijfsmodus. Hij is actief wanneer de HALPI-daemon (`halpid`) draait en met de controller communiceert. Het voorgeïnstalleerde HaLOS-image en alle besturingssysteemimages van Hat Labs bevatten de daemon.

In de co-opmodus:

- De controller en de daemon wisselen realtime gegevens uit: spanningen, stroom, temperaturen en toestand.
- Spanningsuitval wordt aan de daemon gemeld, die een gecontroleerde afsluiting van het besturingssysteem start.
- De watchdogtimer beschermt tegen het vastlopen van het besturingssysteem (zie [Beveiliging met de watchdog](#beveiliging-met-de-watchdog)).
- De configuratie kan worden gelezen en gewijzigd met het opdrachtregelgereedschap `halpi`.

### Solomodus

De solomodus is de terugvalmodus. De controller gaat erin over wanneer er geen communicatie met de daemon is:

- tijdens het opstarten, voordat de daemon start
- als de daemon niet is geïnstalleerd, is uitgeschakeld of is vastgelopen
- op besturingssystemen zonder HALPI2-ondersteuning

In de solomodus beschermt de controller nog steeds tegen spanningsuitval, maar met een botter mechanisme: hij vraagt het afsluiten aan met gesimuleerde drukken op de aan/uit-knop, en hij kan niet vaststellen of het besturingssysteem het afsluiten daadwerkelijk gecontroleerd heeft voltooid.

!!! tip "Betrouwbaarheid van de solomodus"
    De solomodus biedt essentiële bescherming, maar is minder betrouwbaar dan de co-opmodus. Gesimuleerde drukken op de knop werken niet als het besturingssysteem is vastgelopen. Draait u een eigen besturingssysteem, installeer dan de HALPI-daemon — zie [Andere Debian-distributies](../software-development/ubuntu-installation.md).

## Spanningsuitval en afsluitprocedures

De controller bewaakt de ingangsspanning continu. De ingangsvoeding geldt als weggevallen wanneer de ingangsspanning onder 9,0 V zakt. Een blackouttimer (standaard 5 seconden) onderscheidt korte storingen van echte stroomuitval: de supercondensatoren overbruggen de onderbreking, en keert de spanning binnen de timerperiode terug, dan gebeurt er verder niets.

### Afsluitprocedure in de co-opmodus

1. De daemon detecteert de spanningsuitval aan de spanningsmetingen van de controller.
2. De daemon wacht tot de blackouttijdslimiet (standaard 5 seconden) is verstreken.
3. De daemon voert de geconfigureerde afsluitopdracht uit (standaard `/sbin/poweroff`).
4. Het besturingssysteem sluit gecontroleerd af op de spanning van de supercondensatoren.
5. De controller detecteert dat de Compute Module is uitgeschakeld en schakelt de 5 V-rail uit.
6. Is het afsluiten niet binnen 60 seconden voltooid, dan schakelt de controller de spanning geforceerd uit.
7. Het systeem blijft uit tot de ingangsspanning terugkeert en start dan automatisch opnieuw op.

### Afsluitprocedure in de solomodus

1. De controller detecteert de spanningsuitval en start de blackouttimer (standaard 5 seconden).
2. Zodra de timer afloopt, simuleert de controller een dubbele druk op de aan/uit-knop.
3. Het besturingssysteem reageert en begint een gecontroleerde afsluiting op de spanning van de supercondensatoren.
4. Is het afsluiten niet binnen 60 seconden voltooid, dan schakelt de controller de spanning geforceerd uit.
5. Het systeem blijft uit tot de ingangsspanning terugkeert en start dan automatisch opnieuw op.

### Herstartgedrag na afsluiten via software

Een afsluiting die via software wordt gestart terwijl er ingangsspanning beschikbaar blijft (bijvoorbeeld met de opdracht `shutdown` of via het menu van de grafische werkomgeving), eindigt in de toestand *powered down* (uitgeschakeld). Wat er daarna gebeurt, hangt af van de configuratie-instelling `auto_restart`:

- `auto_restart` uitgeschakeld (de fabrieksinstelling op apparaten die sinds begin 2026 zijn geproduceerd): het systeem blijft uit tot de ingangsspanning uit en weer aan wordt gezet of er op een aan/uit-knop wordt gedrukt.
- `auto_restart` ingeschakeld (de terugvalwaarde van de firmware, en de fabrieksinstelling op eerdere apparaten): de controller start het systeem na 5 seconden opnieuw, zodat een systeem zonder toezicht niet uit blijft staan door een per ongeluk gegeven afsluitopdracht.

Wijzig de instelling met `halpi config set auto_restart <true|false>`.

Een druk op de aan/uit-knop of het uit- en weer inschakelen van de ingangsspanning start het systeem altijd opnieuw, ongeacht de instelling van `auto_restart`.

## Beveiliging met de watchdog

In de co-opmodus beschermt een watchdogtimer tegen het vastlopen van het besturingssysteem:

- De daemon moet de watchdog van de controller met regelmatige tussenpozen voeden.
- Blijft dat signaal binnen de watchdog-time-out (standaard 10 seconden) uit, dan beschouwt de controller de host als niet-reagerend, toont hij het alarmpatroon (alle leds continu rood) en schakelt hij de Compute Module uit en weer in om te herstellen.
- De time-out is instelbaar met `halpi config set watchdog_timeout <seconds>`.

## Standby

In standby wordt de Compute Module uitgeschakeld terwijl de controller actief blijft en op een gepland wekmoment wacht:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Tijdens de overgang tonen alle leds continu blauw; in standby tonen ze gedempt rood. De controller start het systeem opnieuw op het geplande tijdstip, bij een druk op de aan/uit-knop of nadat de ingangsspanning uit en weer aan is gezet.

## Referentie van de statusleds

De vijf RGB-leds op het frontpaneel weerspiegelen de toestand van de controller. Deze tabel is de gezaghebbende toewijzing van controllertoestanden aan ledpatronen; de pagina [Dagelijks gebruik](../user-guide/operation.md#statusleds) geeft een vereenvoudigde versie.

| Controllertoestand | Ledpatroon |
|:-------------------|:-----------|
| PowerOff (geen bruikbare ingangsspanning; de controller draait op restlading) | Led 5 continu rood |
| OffCharging | Rode balk die vol loopt terwijl de supercondensatoren opladen |
| SystemStartup | Lopende regenboog, daarna een cyclus van effen kleuren |
| OperationalSolo | Gele laadniveaubalk |
| OperationalCoOp | Groene laadniveaubalk |
| BlackoutSolo | Oranje laadniveaubalk |
| BlackoutCoOp | Donkergroene laadniveaubalk |
| BlackoutShutdown, ManualShutdown | Paarse laadniveaubalk |
| PoweredDownBlackout, PoweredDownManual | Alle uit |
| HostUnresponsive (watchdog-time-out) | Alle continu rood |
| EnteringStandby | Alle continu blauw |
| Standby | Alle gedempt rood |
| Overspanningsalarm van de supercondensatoren | Alle leds knipperen rood |

Bij de laadniveaubalkpatronen staat elke brandende led voor één volt supercondensatorspanning:

| Led | Spanningsbereik |
|:----|:----------------|
| Led 1 | 5,0–6,0 V |
| Led 2 | 6,0–7,0 V |
| Led 3 | 7,0–8,0 V |
| Led 4 | 8,0–9,0 V |
| Led 5 | 9,0–10,0 V |

## Configuratieparameters

De configuratie wordt opgeslagen in het flashgeheugen van de controller en blijft bewaard bij het uit- en inschakelen. Lees en wijzig de configuratie met `halpi config` — zie de [Softwarehandleiding](../user-guide/software.md#configuratiebeheer).

| Parameter | Standaardwaarde | Beschrijving |
|:----------|:----------------|:-------------|
| `auto_restart` | `false` op huidige apparaten (ingesteld bij de productietest); terugvalwaarde van de firmware `true` | Automatisch herstarten 5 s na een afsluiting via software terwijl er ingangsspanning aanwezig is |
| `watchdog_timeout` | 10 s | Watchdog-time-out in de co-opmodus |
| `power_on_threshold` | 8,0 V | Supercondensatorspanning die vereist is voordat de Compute Module wordt ingeschakeld |
| `solo_power_off_threshold` | 5,5 V | Supercondensatorspanning waarbij de controller in de solomodus de spanning geforceerd uitschakelt |
| `solo_depleting_timeout` | 5 s | Blackouttimer in de solomodus |
| `led_brightness` | 48 | Helderheid van de leds op het frontpaneel (0–255) |

De blackouttimer en de afsluitopdracht van de co-opmodus zijn instellingen van de daemon en worden geconfigureerd in `/etc/halpid/halpid.conf` (`blackout-time-limit`, standaard 5 s; `poweroff`, standaard `/sbin/poweroff`).

!!! quote "Gerelateerde informatie"
    - **Dagelijks gebruik:** zie [Dagelijks gebruik](../user-guide/operation.md)
    - **Details van het voedingssysteem:** zie [De voeding in detail](./power-supply.md)
    - **Firmware-updates:** zie [Softwarehandleiding](../user-guide/software.md#firmware-updates)
    - **Firmwarebroncode en I2C-protocol:** zie de [HALPI2-firmware-repository](https://github.com/hatlabs/HALPI2-firmware)

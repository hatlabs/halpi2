---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Bediening van het systeem

## Statusleds

De HALPI2 heeft vijf RGB-leds die visuele terugkoppeling geven over de systeemstatus en de toestand van de voeding.

### Ledstatussen in het kort

| Ledpatroon | Kleur | Betekenis |
|-------------|-------|---------|
| Led 5 continu | Rood | Spanning aanwezig, wacht op lading |
| Oplopende vulling | Rood | Supercondensatoren laden op |
| Regenboog + kleurencyclus | Meerkleurig | CM5 is niet gestart |
| Spanningsbalk | Geel | Werking in de solomodus |
| Spanningsbalk | Groen | Werking in de co-opmodus |
| Spanningsbalk | Oranje | Backupvoeding actief (solo) |
| Spanningsbalk | Donkergroen | Backupvoeding actief (co-op) |
| Alle knipperen | Rood | Overspanning op de supercondensatoren |
| Alle continu | Rood | Watchdog-time-out |
| Spanningsbalk | Paars | Bezig met afsluiten |
| Alle continu | Blauw | Bezig met afsluiten naar standby |
| Alle continu | Gedempt rood | Standby |
| Alle uit | — | Systeem uit |

### Spanningsindicatie van de supercondensatoren

Tijdens bedrijf werken de leds als spanningsindicator en tonen ze het laadniveau van de supercondensatoren:

- **Led 1**: 5,0–6,0 V
- **Led 2**: 6,0–7,0 V
- **Led 3**: 7,0–8,0 V
- **Led 4**: 8,0–9,0 V
- **Led 5**: 9,0–10,0 V

## Energiebeheer en afsluitprocedures

De HALPI2 heeft een voeding die bestand is tegen spanningspieken, storingen en kortdurende uitval.

### Overzicht van het voedingssysteem

Het energiebeheersysteem van de HALPI2 bestaat uit:

- **Voeding met een breed ingangsbereik** (ingang 11–32 V DC, beveiligd tot 100 V DC)
- **Backupsysteem met supercondensatoren** voor gecontroleerd afsluiten bij spanningsuitval
- **Stroombegrenzing** (instelbaar op 0,9 A of 2,5 A)
- **Detectie van spanningsuitval** en automatisch starten van het afsluiten
- **Bewaking van ingangsspanning en -stroom**

Het systeem werkt in twee modi: de solomodus en de co-opmodus.

### Werking in de solomodus

De solomodus biedt eenvoudige, zelfstandige werking wanneer de HALPI-daemon niet draait. De controller werkt dan onafhankelijk, zonder communicatie met de software.

#### Kenmerken van de solomodus

- **Geen communicatie met software nodig**
- **Basisbeveiliging tegen spanningsuitval** — bewaakt de ingangsspanning en reageert op spanningsuitval
- **Automatisch afsluiten via gesimuleerde drukken op de aan/uit-knop**
- **Beperkte mogelijkheden voor bewaking en configuratie**

#### Spanningsuitval en afsluiten in de solomodus

**Detectie van spanningsuitval:**
De controller bewaakt de ingangsspanning en detecteert spanningsuitval. Een blackouttimer (standaard 5 seconden) voorkomt dat het systeem bij korte onderbrekingen afsluit.

**Automatische afsluitprocedure:**

1. **De controller detecteert spanningsuitval**
2. **De blackouttimer start** om storingen van echte spanningsuitval te onderscheiden
3. **Gesimuleerde drukken op de aan/uit-knop** — de controller stuurt een dubbele druk op de aan/uit-knop naar de Compute Module
4. **Het besturingssysteem reageert** en begint met gecontroleerd afsluiten
5. **De supercondensatoren houden de spanning in stand** (doorgaans 30–60 seconden beschikbaar)
6. **Time-outbeveiliging van 60 seconden** — de spanning wordt geforceerd uitgeschakeld als het gecontroleerd afsluiten mislukt
7. **Het systeem blijft uit** tot de spanning terugkeert
8. **Automatische herstart** zodra de spanning is hersteld

**Handmatig afsluiten in de solomodus:**

- Het besturingssysteem sluit normaal af
- Het systeem start na 5 seconden automatisch opnieuw op als er ingangsspanning aanwezig blijft
- Wilt u het systeem definitief uitschakelen, koppel dan de ingangsspanning los nadat u het gecontroleerd afsluiten hebt gestart

#### Wanneer de solomodus actief is

De solomodus treedt op:

- Tijdens de eerste fase van de start, voordat de HALPI-daemon draait
- Als de HALPI-daemon niet start of is uitgeschakeld
- Op niet-ondersteunde besturingssystemen zonder de daemon
- Wanneer de daemon is vastgelopen of niet meer reageert

!!! tip "Betrouwbaarheid van de solomodus"
    De solomodus biedt essentiële bescherming, maar is minder betrouwbaar dan de co-opmodus. De controller vraagt het afsluiten aan met gesimuleerde drukken op de knop, wat mogelijk niet werkt als het systeem is vastgelopen.

### Werking in de co-opmodus

De co-opmodus biedt volledig energiebeheer wanneer de HALPI-daemon draait en met de controller communiceert.

#### Mogelijkheden van de co-opmodus

- **Rechtstreekse communicatie met de software** — gegevensuitwisseling in realtime tussen controller en daemon
- **Beveiliging met een watchdogtimer** — een time-out van 30 seconden waarborgt de stabiliteit van het systeem
- **Instelbaar afsluitgedrag** — tijden en opdrachten zijn aan te passen
- **Bewaking in realtime** — uitgebreide bewaking van de voedingsparameters
- **Uitgebreide configuratiemogelijkheden**

#### Spanningsuitval en afsluiten in de co-opmodus

**Detectie van spanningsuitval:**
De controller bewaakt de ingangsspanning en meldt gebeurtenissen rechtstreeks aan de HALPI-daemon. Dankzij de instelbare blackouttimer (standaard 5 seconden) leiden korte spanningsonderbrekingen niet tot afsluiten.

**Automatische afsluitprocedure:**

1. **De controller detecteert spanningsuitval** en meldt dit aan de HALPI-daemon
2. **Beoordeling door de blackouttimer** — de daemon bepaalt of de spanningsuitval de drempelwaarde overschrijdt
3. **Uitvoeren van de afsluitopdracht** — de daemon voert de afsluitopdracht uit (standaard: `/sbin/poweroff`)
4. **Gecontroleerd afsluiten van het besturingssysteem** — applicaties worden gesloten en bestandssystemen veilig ontkoppeld
5. **Backupvoeding uit de supercondensatoren** levert energie gedurende het hele afsluiten
6. **De controller bewaakt de voltooiing** — hij volgt wanneer de Compute Module uitschakelt
7. **De 5 V-rail wordt uitgeschakeld** zodra het afsluiten voltooid is
8. **Het systeem blijft uit** tot de ingangsspanning terugkeert
9. **Beheer van de herstart** — afhankelijk van de configuratie start het systeem automatisch opnieuw op of blijft het uit

**Handmatig afsluiten in de co-opmodus:**

- Wordt het afsluiten via software gestart, dan verloopt het gecontroleerd volgens de standaardprocedure
- Het systeem start na 5 seconden automatisch opnieuw op als er ingangsspanning aanwezig blijft
- Wilt u de automatische herstart voorkomen, koppel dan de voeding los of zet `auto_restart` op `false`

#### Beveiliging met de watchdog

De co-opmodus omvat een beveiliging met een watchdogtimer:

- **Communicatietime-out van 30 seconden** — de daemon moet regelmatig met de controller communiceren
- **Automatisch herstel** — het systeem start opnieuw op als de communicatie stopt
- **Bescherming tegen softwarestoringen** — waarborgt herstel na het vastlopen van de daemon of van het systeem
- **“De watchdog voeden”** — de daemon stuurt regelmatig statusupdates om de timer terug te zetten

#### Wanneer de co-opmodus actief is

De co-opmodus treedt op wanneer:

- De HALPI-daemon draait en goed functioneert
- De communicatie tussen daemon en controller tot stand is gekomen
- Het systeem op een ondersteund besturingssysteem draait
- Alle mogelijkheden voor systeembewaking en -besturing beschikbaar zijn

!!! info "De co-opmodus controleren"
    Status van de daemon opvragen: `systemctl status halpid`

    Toestand van de controller bekijken: `halpi status`

    Meer informatie over de opdracht `halpi` vindt u in de [Softwarehandleiding](./software.md#halpi-daemon-halpid).

### Backupvoeding en het condensatorsysteem

In beide modi zorgt het backupsysteem met supercondensatoren voor bescherming bij gecontroleerd afsluiten:

**Duur van de backupvoeding:**

- De supercondensatoren leveren 30–60 seconden backupvoeding
- De duur hangt af van de systeembelasting en de aangesloten randapparatuur
- Voldoende tijd om het bestandssysteem veilig te ontkoppelen en processen te beëindigen
- Niet bedoeld om de werking bij langdurige uitval voort te zetten

**Laadeigenschappen:**

- Laadtijd: 25 seconden bij een stroombegrenzing van 0,9 A
- Laadtijd: 9 seconden bij een stroombegrenzing van 2,5 A
- De laadvoortgang is zichtbaar aan de oplopende leds (rood vulpatroon)

!!! warning "Beperking van de beveiliging tegen spanningsuitval"
    Het systeem met supercondensatoren is bedoeld voor gecontroleerd afsluiten, niet om de werking voort te zetten. Vertrouw er niet op bij langdurige stroomuitval.

### Aandachtspunten bij handmatig afsluiten

De HALPI2 is gericht op geautomatiseerde werking en automatisch herstel, wat gevolgen heeft voor het handmatig afsluiten.

#### Gedrag bij automatische herstart

Standaard start de HALPI2 na handmatig afsluiten opnieuw op zolang er ingangsspanning aanwezig blijft:

- Handmatig afsluiten verloopt als een normale afsluiting van het besturingssysteem
- Na het voltooide afsluiten volgt een wachttijd van 5 seconden
- Het systeem start automatisch opnieuw op om beschikbaar te blijven
- Zo herstelt het systeem zich na een onbedoelde afsluiting

#### Methoden om bewust af te sluiten

Gebruik voor een definitieve afsluiting een van deze methoden:

**Methode met loskoppelen van de voeding:**

1. Start het gecontroleerd afsluiten via de software
2. Wacht tot het afsluiten voltooid is (de leds gaan uit)
3. Koppel de ingangsspanning los om automatische herstart te voorkomen

**Methode via de configuratie:**

1. Schakel de automatische herstart uit: `halpi config set auto_restart false`
2. Start het afsluiten via de software
3. Het systeem blijft uit nadat het afsluiten voltooid is

**Standbymodus (toekomstig):**
!!! info "Status van de functie"
    De standbymodus is gepland voor toekomstige firmwareversies. Daarmee kan de Compute Module worden uitgeschakeld terwijl de HALPI2-controller actief blijft en op wekgebeurtenissen wacht.

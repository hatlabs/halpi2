---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Dagelijks gebruik

De HALPI2 is ontworpen voor gebruik zonder toezicht. Op het voorgeïnstalleerde HaLOS-image — of op elk besturingssysteem waarop de [HALPI-daemon](./software.md#halpi-opdrachtregelgereedschap) is geïnstalleerd — verloopt het energiebeheer automatisch: het apparaat laadt de supercondensatoren van de backupvoeding op, overbrugt korte spanningsdips, sluit het besturingssysteem veilig af wanneer de spanning wegvalt en start weer op zodra de spanning terugkeert. Voor dit alles is geen handeling van de gebruiker nodig.

## Inschakelen

De HALPI2 heeft geen aan/uit-knop op de behuizing: hij start zodra er ingangsspanning wordt aangesloten. (Op het carrierboard kan een externe aan/uit-knop worden aangesloten — zie [Externe knoppen](./interfaces.md#externe-knoppen).) De ledbalk loopt eerst vol met rood terwijl de supercondensatoren opladen (enkele seconden tot een halve minuut, afhankelijk van de [instelling van de stroombegrenzing](./hardware.md#instelling-van-de-stroombegrenzing)). Daarna tonen de leds een korte regenboog- en kleurencyclusanimatie terwijl de Compute Module start, tonen ze een gele balk terwijl het besturingssysteem opstart, en worden ze groen zodra het besturingssysteem draait en de HALPI-daemon verbinding heeft.

## Afsluiten

Om de HALPI2 af te sluiten schakelt u de ingangsspanning uit — bijvoorbeeld met een schakelaar op het elektrisch paneel. Het systeem detecteert de spanningsuitval, sluit het besturingssysteem gecontroleerd af op de spanning van de supercondensatoren en blijft daarna uit. De leds tonen een paarse balk zolang het afsluiten loopt en gaan uit zodra het voltooid is.

U kunt ook via software afsluiten — via het menu van de grafische werkomgeving, de opdracht `shutdown` of `halpi shutdown`. Het systeem schakelt dan uit en blijft uit tot de ingangsspanning uit en weer aan wordt gezet (of tot er, indien aanwezig, op een [externe aan/uit-knop](./interfaces.md#externe-knoppen) wordt gedrukt).

Optioneel kan de controller het systeem ongeveer 5 seconden na een afsluiting via software automatisch opnieuw starten zolang de ingangsspanning aangesloten blijft, zodat een per ongeluk gegeven afsluitopdracht een fysiek moeilijk bereikbare installatie nooit onbereikbaar maakt. Schakel dit in met `halpi config set auto_restart true`; de instelling blijft in de controller bewaard. Apparaten die vóór begin 2026 zijn geproduceerd, werden met dit gedrag ingeschakeld geleverd — controleer uw apparaat met `halpi config get auto_restart`.

Het systeem kan ook in standby worden gezet, waarbij het uitschakelt en op een gepland tijdstip weer ontwaakt — zie de referentie [Controller van het carrierboard](../technical-reference/controller.md#standby).

## Statusleds

De vijf leds op het frontpaneel tonen wat het systeem doet:

| Ledpatroon | Betekenis |
|:-----------|:----------|
| Rode balk die vol loopt | Supercondensatoren laden op vóór het starten — wachten |
| Regenboog en wisselende kleuren | Compute Module start op. Herhaalt het patroon zich zonder voortgang, dan is de module niet gestart — zie [Probleemoplossing](./troubleshooting.md#regenboogkleurige-leds) |
| Gele balk | Systeem draait, HALPI-daemon niet verbonden — kort tijdens het opstarten is dat normaal. Houdt het aan, zie [Probleemoplossing](./troubleshooting.md#leds-blijven-geel) |
| Groene balk | Normale werking |
| Oranje of donkergroene balk | Ingangsspanning weggevallen, systeem draait op de backupvoeding — het afsluiten volgt, tenzij de spanning binnen enkele seconden terugkeert |
| Paarse balk | Bezig met afsluiten |
| Alle continu rood | Besturingssysteem reageert niet — de controller start het automatisch opnieuw |
| Alle knipperen rood | Storing in de supercondensatoren — neem contact op met de ondersteuning |
| Alle continu blauw | Bezig met overgaan naar standby |
| Alle gedempt rood | Standby |
| Alle uit | Uitgeschakeld |

Bij de balkpatronen toont het aantal brandende leds het laadniveau van de supercondensatoren. De exacte spanningsvensters en de volledige toewijzing van toestanden staan in de referentie [Controller van het carrierboard](../technical-reference/controller.md#referentie-van-de-statusleds).

De helderheid van de leds is instelbaar — zie [Ledbesturing](./software.md#ledbesturing). Met de uitbreiding [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights) kunnen de leds ook worden ingezet als weergave voor systeemwaarden en maritieme gegevens (netwerkactiviteit, tankniveaus, NMEA 2000- en Signal K-waarden).

## Bij spanningsuitval

Er hoeft niets te gebeuren. Korte dips en storingen — standaard tot 5 seconden — worden overbrugd door de supercondensatoren en de werking gaat ongestoord verder. Bij een langere stroomuitval sluit het systeem zichzelf gecontroleerd af op de 30–60 seconden backupvoeding die de supercondensatoren vasthouden. Zodra de ingangsspanning terugkeert, start het systeem automatisch weer op.

!!! warning "Geen UPS"
    De supercondensatoren zijn er om storingen te overbruggen en een veilige afsluiting van spanning te voorzien. Voor doorwerken tijdens langdurige stroomuitval is een externe noodstroomvoorziening (UPS) vereist.

## De systeemstatus controleren

Een groene ledbalk betekent dat het systeem in orde is. Voor details toont de opdracht `halpi` de toestand van de controller, de spanningen, de stroom en de temperaturen:

```bash
halpi status
```

Ziet iets er niet goed uit, zie dan [Probleemoplossing](./troubleshooting.md) en de [Softwarehandleiding](./software.md#halpi-opdrachtregelgereedschap).

## Werken zonder de daemon

Op besturingssystemen zonder de HALPI-daemon valt de controller terug op een basisbeveiligingsmodus: hij detecteert nog steeds spanningsuitval en vraagt het afsluiten aan, maar doet dat met gesimuleerde drukken op de aan/uit-knop — wat mislukt als het systeem is vastgelopen — en bewaking en configuratie zijn niet beschikbaar. Draait u een eigen besturingssysteem, installeer dan de daemon; zie [Andere Debian-distributies](../software-development/ubuntu-installation.md). Hoe de twee modi werken staat beschreven in de referentie [Controller van het carrierboard](../technical-reference/controller.md#bedrijfsmodi).

!!! quote "Gerelateerde informatie"
    - **Hoe het energiebeheer intern werkt:** zie [Controller van het carrierboard](../technical-reference/controller.md)
    - **Details van het voedingssysteem:** zie [De voeding in detail](../technical-reference/power-supply.md)
    - **De opdracht `halpi` en de daemon:** zie [Softwarehandleiding](./software.md)
    - **Problemen:** zie [Probleemoplossing](./troubleshooting.md)

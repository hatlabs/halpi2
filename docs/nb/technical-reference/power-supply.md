---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Strømforsyningen i detalj

Strømforsyningen i HALPI2 er laget for de ustabile elektriske miljøene i båter og kjøretøy: den tåler spenningstopper og forstyrrelser, begrenser startstrømmen og lagrer nok energi til å stenge systemet trygt ned når inngangsstrømmen blir borte.

De elektriske spesifikasjonene finner du i [maskinvarereferansen](./hardware.md). Tilstandsmaskinen som handler ut fra målingene som beskrives her, finner du i referansen [Bærekortets mikrokontroller](./controller.md).

## Inngangstrinnet

Det nominelle inngangsområdet er 10–32 V DC og dekker både 12 V- og 24 V-systemer. Inngangstrinnet er beskyttet mot omvendt polaritet og mot kortvarige overspenninger på opptil 100 V, slik som «load dump» fra dynamoen.

### Strømbegrensning

En strømbegrenser på inngangen styrer den største strømmen som trekkes fra kilden, valgbar mellom 0,9 A og 2,5 A med en bryter på bærekortet. Grensen har to formål:

- Den begrenser startstrømmen når de utladede superkondensatorene begynner å lade ved påslag.
- Den holder det samlede forbruket innenfor strømbudsjettet til kilden – innstillingen 0,9 A (LEN 18) gjør HALPI2 trygg å forsyne fra en NMEA 2000-buss.

Standardinnstillingen er 0,9 A. Velg 2,5 A når systemet forsyner eksterne enheter med høyt strømforbruk, eller når raskere oppstart er ønskelig. Hvor bryteren sitter, og hvordan du endrer innstillingen, er beskrevet i [maskinvareveiledningen](../user-guide/hardware.md#konfigurasjon-av-strmbegrensning).

## Reservestrøm fra superkondensatorene

En bank med superkondensatorer gir reserveenergi til kontrollerte nedstenginger. I motsetning til en batteribasert UPS slites ikke superkondensatorer ut, de virker over hele temperaturområdet, og de lades på sekunder – mot at energireserven er mye mindre.

### Lading

Superkondensatorene lades så lenge inngangsstrøm er til stede. Fra tom tilstand tar ladingen omtrent:

- 25 sekunder med strømgrensen 0,9 A
- 9 sekunder med strømgrensen 2,5 A

LED-ene på frontpanelet viser ladeforløpet som en rød søyle som fylles opp. Compute Module slås på når superkondensatorspenningen når innkoblingsterskelen (standard 8,0 V).

### Varighet på reservestrømmen

Når inngangsstrømmen blir borte, bærer superkondensatorene hele systemlasten. De gir 30–60 sekunder driftstid, avhengig av systembelastningen og tilkoblede eksterne enheter – nok til en kontrollert nedstenging av operativsystemet med god margin.

!!! warning "Ikke en UPS"
    Superkondensatorsystemet er laget for å dekke forstyrrelser og gi strøm til en trygg nedstenging. Det er ikke laget for fortsatt drift gjennom lengre strømbrudd.

## Deteksjon av strømbortfall

Kontrolleren måler inngangsspenningen kontinuerlig og regner inngangsstrømmen som tapt når spenningen faller under 9,0 V. En strømbruddstimer (standard 5 sekunder) holder nedstengingen tilbake ved korte avbrudd: superkondensatorene dekker gapet, og driften fortsetter uforstyrret hvis strømmen kommer tilbake i tide. Lengre strømbrudd utløser de automatiske nedstengingssekvensene som er beskrevet i referansen [Bærekortets mikrokontroller](./controller.md#strmbortfall-og-nedstengingssekvenser).

## Overvåking

Kontrolleren måler inngangsspenning, inngangsstrøm og superkondensatorspenning og gjør verdiene tilgjengelige gjennom HALPI-daemonen:

```bash
halpi status
```

Verdiene er også tilgjengelige programmatisk gjennom REST API-et til daemonen – se [programvareveiledningen](../user-guide/software.md#rest-api-tilgang).

!!! quote "Relatert informasjon"
    - **Elektriske spesifikasjoner:** Se [Maskinvarereferanse](./hardware.md)
    - **Tilstandsmaskinen og nedstengingssekvensene:** Se [Bærekortets mikrokontroller](./controller.md)
    - **Strømoppførsel i daglig bruk:** Se [Daglig bruk](../user-guide/operation.md)

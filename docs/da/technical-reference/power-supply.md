---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Strømforsyningen i detaljer

HALPI2's strømforsyning er designet til de ustabile elektriske miljøer på både og i køretøjer: Den tåler spændingsspidser og korte spændingsudfald, begrænser indkoblingsstrømmen og rummer nok lagret energi til at lukke systemet sikkert ned, når indgangsstrømmen forsvinder.

De elektriske specifikationer findes i [Hardwarereferencen](./hardware.md). Tilstandsmaskinen, der handler på de målinger, som beskrives her, er dokumenteret i referencen [Bærekortets controller](./controller.md).

## Indgangstrin

Det nominelle indgangsområde er 10–32 V DC, hvilket dækker både 12 V- og 24 V-systemer. Indgangstrinnet er beskyttet mod omvendt polaritet og mod kortvarige overspændinger på op til 100 V, for eksempel load dumps fra generatoren.

### Strømbegrænsning

En strømbegrænser på indgangen styrer den maksimale strøm, der trækkes fra forsyningen; grænsen kan vælges mellem 0,9 A og 2,5 A med en kontakt på bærekortet. Den tjener to formål:

- Den begrænser indkoblingsstrømmen, når de afladede superkondensatorer begynder at oplade, i det øjeblik strømmen tilsluttes.
- Den holder det samlede forbrug inden for kildens effektbudget — indstillingen 0,9 A (LEN 18) gør det sikkert at forsyne HALPI2 fra en NMEA 2000-bus.

Standardindstillingen er 0,9 A. Vælg 2,5 A, når systemet forsyner strømkrævende perifere enheder, eller når du ønsker en hurtigere opstart. Kontaktens placering og fremgangsmåden for at ændre indstillingen er beskrevet i [Hardwarevejledningen](../user-guide/hardware.md#konfiguration-af-strmbegrnsning).

## Superkondensatorbackup

En bank af superkondensatorer leverer backupenergi til kontrollerede nedlukninger. I modsætning til en batteribaseret UPS slides superkondensatorer ikke op, de fungerer i hele temperaturområdet, og de oplades på sekunder — til gengæld er energireserven meget mindre.

### Opladning

Superkondensatorerne oplades, når der er indgangsstrøm. Fra helt afladet tilstand tager opladningen cirka:

- 25 sekunder ved strømgrænsen 0,9 A
- 9 sekunder ved strømgrænsen 2,5 A

LED'erne på frontpanelet viser opladningens forløb som en rød søjle, der fyldes op. Compute Module tændes, når superkondensatorspændingen når tærsklen for tænding (standard 8,0 V).

### Backupvarighed

Når indgangsstrømmen forsvinder, bærer superkondensatorerne hele systemets belastning. De giver 30–60 sekunders driftstid afhængigt af systemets belastning og de tilsluttede perifere enheder — nok til en kontrolleret nedlukning af styresystemet med margin.

!!! warning "Ikke en UPS"
    Systemet med superkondensatorer er designet til at dække korte udfald og levere strøm til en sikker nedlukning. Det er ikke designet til fortsat drift under længerevarende strømafbrydelser.

## Registrering af strømsvigt

Controlleren måler indgangsspændingen løbende og betragter indgangsstrømmen som væk, når spændingen falder under 9,0 V. En strømafbrydelsestimer (standard 5 sekunder) undertrykker nedlukning ved korte afbrydelser: Superkondensatorerne dækker hullet, og driften fortsætter uforstyrret, hvis strømmen når at vende tilbage. Længere afbrydelser udløser de automatiske nedlukningsforløb, der er beskrevet i referencen [Bærekortets controller](./controller.md#strmsvigt-og-nedlukningsforlb).

## Overvågning

Controlleren måler indgangsspænding, indgangsstrøm og superkondensatorspænding og stiller værdierne til rådighed gennem HALPI-dæmonen:

```bash
halpi status
```

Værdierne er også tilgængelige programmatisk gennem dæmonens REST-API — se [Softwarevejledningen](../user-guide/software.md#adgang-til-rest-apiet).

!!! quote "Relaterede oplysninger"
    - **Elektriske specifikationer:** Se [Hardwarereferencen](./hardware.md)
    - **Tilstandsmaskine og nedlukningsforløb:** Se [Bærekortets controller](./controller.md)
    - **Strømadfærd i dagligdagen:** Se [Daglig brug](../user-guide/operation.md)

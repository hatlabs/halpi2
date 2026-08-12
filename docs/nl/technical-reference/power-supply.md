---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# De voeding in detail

De voeding van de HALPI2 is ontworpen voor de instabiele elektrische omgeving van boten en voertuigen: ze verdraagt spanningspieken en storingen, begrenst de inschakelstroom en levert genoeg opgeslagen energie om het systeem veilig af te sluiten wanneer de ingangsspanning wegvalt.

Zie voor de elektrische specificaties de [Hardwarereferentie](./hardware.md). Zie voor de toestandsmachine die op de hier beschreven metingen reageert de referentie [Controller van het carrierboard](./controller.md).

## Ingangstrap

Het nominale ingangsbereik is 10–32 V DC en dekt zowel 12 V- als 24 V-systemen. De ingangstrap is beveiligd tegen omgekeerde polariteit en tegen kortstondige overspanningen tot 100 V, zoals load dumps van een dynamo.

### Stroombegrenzing

Een stroombegrenzer aan de ingang bepaalt de maximale stroom die uit de voedingsbron wordt getrokken, met een schakelaar op het carrierboard instelbaar op 0,9 A of 2,5 A. De begrenzing dient twee doelen:

- Hij begrenst de inschakelstroom wanneer de ontladen supercondensatoren bij het inschakelen beginnen op te laden.
- Hij houdt de totale stroomafname binnen het vermogensbudget van de bron — met de instelling 0,9 A (LEN 18) kan de HALPI2 veilig vanuit een NMEA 2000-bus worden gevoed.

De standaardinstelling is 0,9 A. Kies 2,5 A wanneer het systeem randapparatuur met een hoge stroomafname voedt of wanneer sneller opstarten gewenst is. De plaats van de schakelaar en de procedure voor het wijzigen staan beschreven in de [Hardwarehandleiding](../user-guide/hardware.md#instelling-van-de-stroombegrenzing).

## Backup met supercondensatoren

Een bank supercondensatoren levert backupenergie voor gecontroleerd afsluiten. Anders dan bij een UPS op batterijen slijten supercondensatoren niet, werken ze over het volledige temperatuurbereik en laden ze in seconden op — met als prijs een veel kleinere energiereserve.

### Opladen

De supercondensatoren laden op zodra er ingangsspanning aanwezig is. Vanuit lege toestand duurt het opladen ongeveer:

- 25 seconden bij de stroombegrenzing van 0,9 A
- 9 seconden bij de stroombegrenzing van 2,5 A

De leds op het frontpaneel tonen de laadvoortgang als een rode balk die vol loopt. De Compute Module wordt ingeschakeld zodra de supercondensatorspanning de inschakeldrempel bereikt (standaard 8,0 V).

### Duur van de backupvoeding

Valt de ingangsspanning weg, dan dragen de supercondensatoren de volledige systeembelasting. Ze leveren 30–60 seconden bedrijfstijd, afhankelijk van de systeembelasting en de aangesloten randapparatuur — genoeg voor een gecontroleerde afsluiting van het besturingssysteem, met marge.

!!! warning "Geen UPS"
    Het systeem met supercondensatoren is ontworpen om storingen te overbruggen en een veilige afsluiting van spanning te voorzien. Het is niet ontworpen om de werking tijdens langdurige stroomuitval voort te zetten.

## Detectie van spanningsuitval

De controller meet de ingangsspanning continu en beschouwt de ingangsvoeding als weggevallen wanneer de spanning onder 9,0 V zakt. Een blackouttimer (standaard 5 seconden) onderdrukt het afsluiten bij korte onderbrekingen: de supercondensatoren overbruggen de onderbreking en de werking gaat ongestoord verder als de spanning op tijd terugkeert. Langere stroomuitval activeert de automatische afsluitprocedures die in de referentie [Controller van het carrierboard](./controller.md#spanningsuitval-en-afsluitprocedures) staan beschreven.

## Bewaking

De controller meet de ingangsspanning, de ingangsstroom en de supercondensatorspanning en stelt ze beschikbaar via de HALPI-daemon:

```bash
halpi status
```

De waarden zijn ook programmatisch beschikbaar via de REST API van de daemon — zie de [Softwarehandleiding](../user-guide/software.md#rest-api-toegang).

!!! quote "Gerelateerde informatie"
    - **Elektrische specificaties:** zie [Hardwarereferentie](./hardware.md)
    - **Toestandsmachine en afsluitprocedures:** zie [Controller van het carrierboard](./controller.md)
    - **Voedingsgedrag in het dagelijks gebruik:** zie [Dagelijks gebruik](../user-guide/operation.md)

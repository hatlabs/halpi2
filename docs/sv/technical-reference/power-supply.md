---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Strömförsörjningen i detalj

HALPI2:s strömförsörjning är konstruerad för de instabila elmiljöerna i båtar och fordon: den tål spänningstoppar och korta störningar, begränsar inkopplingsströmmen och lagrar tillräckligt med energi för att stänga av systemet säkert när inspänningen försvinner.

De elektriska specifikationerna finns i [Hårdvarureferensen](./hardware.md). Tillståndsmaskinen som agerar på mätningarna som beskrivs här behandlas i referensen [Bärkortets styrkrets](./controller.md).

## Ingångssteget

Det nominella inspänningsområdet är 10–32 V DC, vilket täcker både 12 V- och 24 V-system. Ingångssteget är skyddat mot omkastad polaritet och mot transienta överspänningar på upp till 100 V, till exempel load dump-pulser från generatorn.

### Strömbegränsning

En strömbegränsare på ingången styr den maximala ström som dras från källan, valbar mellan 0,9 A och 2,5 A med en omkopplare på bärkortet. Begränsningen har två syften:

- Den begränsar inkopplingsströmmen när de urladdade superkondensatorerna börjar laddas vid påslag.
- Den håller det totala strömuttaget inom källans effektbudget — inställningen 0,9 A (LEN 18) gör HALPI2 säker att mata från en NMEA 2000-buss.

Standardinställningen är 0,9 A. Välj 2,5 A när systemet matar strömtörstiga kringenheter eller när en snabbare start önskas. Omkopplarens placering och hur du ändrar inställningen beskrivs i [Hårdvaruguiden](../user-guide/hardware.md#konfiguration-av-strombegransningen).

## Backup med superkondensatorer

En bank av superkondensatorer ger backupenergi för kontrollerade avstängningar. Till skillnad från en batteribaserad UPS slits superkondensatorer inte ut, fungerar i hela temperaturområdet och laddas på några sekunder — till priset av en mycket mindre energireserv.

### Laddning

Superkondensatorerna laddas så länge inspänning finns. Från tomma tar laddningen ungefär:

- 25 sekunder vid strömbegränsningen 0,9 A
- 9 sekunder vid strömbegränsningen 2,5 A

Frontpanelens lysdioder visar laddningsförloppet som en röd stapel som fylls. Compute Module slås på när superkondensatorernas spänning når påslagströskeln (8,0 V som standard).

### Backuptid

När inspänningen försvinner bär superkondensatorerna hela systemlasten. De ger 30–60 sekunders drifttid, beroende på systemets belastning och anslutna kringenheter — tillräckligt för en kontrollerad avstängning av operativsystemet med marginal.

!!! warning "Inte en UPS"
    Superkondensatorsystemet är konstruerat för att överbrygga korta störningar och driva en säker avstängning. Det är inte avsett för fortsatt drift under längre avbrott.

## Detektering av spänningsbortfall

Styrkretsen mäter inspänningen kontinuerligt och betraktar inspänningen som borta när spänningen faller under 9,0 V. En avbrottstimer (5 sekunder som standard) håller tillbaka avstängningen vid korta avbrott: superkondensatorerna överbryggar glappet, och driften fortsätter ostörd om strömmen kommer tillbaka i tid. Längre avbrott utlöser de automatiska avstängningssekvenser som beskrivs i referensen [Bärkortets styrkrets](./controller.md#spanningsbortfall-och-avstangningssekvenser).

## Övervakning

Styrkretsen mäter inspänning, inström och superkondensatorspänning och exponerar värdena genom HALPI-daemonen:

```bash
halpi status
```

Värdena är också tillgängliga programmatiskt via daemonens REST-API — se [Programvaruguiden](../user-guide/software.md#atkomst-via-rest-apiet).

!!! quote "Relaterad information"
    - **Elektriska specifikationer:** se [Hårdvarureferens](./hardware.md)
    - **Tillståndsmaskin och avstängningssekvenser:** se [Bärkortets styrkrets](./controller.md)
    - **Strömhanteringen i vardagen:** se [Daglig användning](../user-guide/operation.md)

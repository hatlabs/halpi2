---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Daglig bruk

HALPI2 er laget for drift uten tilsyn. På det forhåndsinstallerte HaLOS-systembildet – eller ethvert operativsystem med [HALPI-daemonen](./software.md#halpi-kommandolinjeverktyet) installert – er strømstyringen automatisk: enheten lader opp superkondensatorene som gir reservestrøm, rir av spenningsforstyrrelser, stenger operativsystemet trygt ned når strømmen blir borte, og starter opp igjen når strømmen kommer tilbake. Ingenting av dette krever at brukeren gjør noe.

## Slå på

HALPI2 har ingen strømknapp på kabinettet: den starter når inngangsstrøm kobles til. (En ekstern strømknapp kan kobles til bærekortet – se [Eksterne knapper](./interfaces.md#eksterne-knapper).) LED-raden fylles først opp med rødt mens superkondensatorene lades (fra noen sekunder til et halvt minutt, avhengig av [innstillingen for strømgrensen](./hardware.md#konfigurasjon-av-strmbegrensning)). Deretter spiller LED-ene en kort animasjon med regnbue og fargesyklus mens Compute Module starter, viser en gul søyle mens operativsystemet starter opp, og blir grønne når operativsystemet kjører og HALPI-daemonen har koblet seg til.

## Slå av

For å slå av HALPI2 kutter du inngangsstrømmen – for eksempel med en bryter på det elektriske panelet. Systemet oppdager strømbortfallet, stenger operativsystemet kontrollert ned på strøm fra superkondensatorene og forblir av. LED-ene viser en lilla søyle mens nedstengingen pågår, og slukker når den er fullført.

Du kan også slå av gjennom programvaren – fra skrivebordsmenyen, med kommandoen `shutdown` eller med `halpi shutdown`. Systemet slår seg da av og forblir av til inngangsstrømmen kobles ut og inn igjen (eller til en [ekstern strømknapp](./interfaces.md#eksterne-knapper) trykkes, hvis en slik er montert).

Som et tilvalg kan kontrolleren starte systemet automatisk igjen omtrent 5 sekunder etter en nedstenging fra programvaren så lenge inngangsstrømmen fortsatt er tilkoblet, slik at en utilsiktet nedstengingskommando aldri lar en installasjon som er vanskelig å nå fysisk, bli stående avslått. Aktiver det med `halpi config set auto_restart true`; innstillingen lagres varig i kontrolleren. Enheter produsert før tidlig i 2026 ble levert med denne oppførselen aktivert – sjekk din egen med `halpi config get auto_restart`.

Systemet kan også settes i ventemodus, der det slår seg av og våkner igjen på et planlagt tidspunkt – se referansen [Bærekortets mikrokontroller](../technical-reference/controller.md#ventemodus).

## Status-LED-indikatorer

De fem LED-ene på frontpanelet viser hva systemet gjør:

| LED-mønster | Betydning |
|:------------|:----------|
| Rød søyle som fylles opp | Superkondensatorene lades før oppstart – vent |
| Regnbue og skiftende farger | Compute Module starter opp. Hvis mønsteret gjentar seg uten framgang, startet ikke modulen – se [Feilsøking](./troubleshooting.md#regnbue-led-er) |
| Gul søyle | Systemet kjører, HALPI-daemonen er ikke tilkoblet – normalt en kort stund under oppstart. Hvis det vedvarer, se [Feilsøking](./troubleshooting.md#led-ene-blir-staende-gule) |
| Grønn søyle | Normal drift |
| Oransje eller mørkegrønn søyle | Inngangsstrømmen er borte, systemet kjører på reservestrøm – nedstenging følger hvis ikke strømmen kommer tilbake i løpet av sekunder |
| Lilla søyle | Nedstenging pågår |
| Alle lyser fast rødt | Operativsystemet svarer ikke – kontrolleren starter det på nytt automatisk |
| Alle blinker rødt | Feil på superkondensatorene – kontakt støtte |
| Alle lyser fast blått | Går inn i ventemodus |
| Alle lyser svakt rødt | Ventemodus |
| Alle av | Slått av |

I søylemønstrene viser antallet tente LED-er ladenivået i superkondensatorene. De nøyaktige spenningsintervallene og den fullstendige tilordningen av tilstander finner du i referansen [Bærekortets mikrokontroller](../technical-reference/controller.md#status-led-referanse).

LED-lysstyrken kan justeres – se [LED-styring](./software.md#led-styring). LED-ene kan også brukes som visning for systemmålinger og maritime data (nettverksaktivitet, tanknivåer, NMEA 2000- og Signal K-verdier) med tillegget [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights).

## Ved strømbortfall

Ingenting trenger å gjøres. Korte fall og forstyrrelser – opptil 5 sekunder som standard – dekkes av superkondensatorene, og driften fortsetter uforstyrret. Ved et lengre strømbrudd stenger systemet seg selv kontrollert ned på de 30–60 sekundene med reservestrøm som superkondensatorene holder. Når inngangsstrømmen kommer tilbake, starter systemet opp igjen automatisk.

!!! warning "Ikke en UPS"
    Superkondensatorene finnes for å dekke forstyrrelser og gi strøm til en trygg nedstenging. For fortsatt drift gjennom lengre strømbrudd kreves en ekstern avbruddsfri strømforsyning (UPS).

## Kontrollere systemtilstanden

En grønn LED-søyle betyr at systemet er i orden. For detaljer viser `halpi`-kommandoen kontrollerens tilstand, spenninger, strøm og temperaturer:

```bash
halpi status
```

Hvis noe ser galt ut, se [Feilsøking](./troubleshooting.md) og [programvareveiledningen](./software.md#halpi-kommandolinjeverktyet).

## Drift uten daemonen

På operativsystemer uten HALPI-daemonen faller kontrolleren tilbake til en grunnleggende beskyttelsesmodus: den oppdager fortsatt strømbortfall og ber om nedstenging, men gjør det ved å simulere trykk på strømknappen – noe som mislykkes hvis systemet har låst seg – og overvåking og konfigurasjon er utilgjengelige. Hvis du kjører et eget operativsystem, bør du installere daemonen; se [Andre Debian-distribusjoner](../software-development/ubuntu-installation.md). Hvordan de to modusene virker, er beskrevet i referansen [Bærekortets mikrokontroller](../technical-reference/controller.md#driftsmoduser).

!!! quote "Relatert informasjon"
    - **Hvordan strømstyringen virker internt:** Se [Bærekortets mikrokontroller](../technical-reference/controller.md)
    - **Detaljer om strømsystemet:** Se [Strømforsyningen i detalj](../technical-reference/power-supply.md)
    - **`halpi`-kommandoen og daemonen:** Se [Programvareveiledning](./software.md)
    - **Problemer:** Se [Feilsøking](./troubleshooting.md)

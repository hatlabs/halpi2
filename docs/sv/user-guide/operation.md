---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Daglig användning

HALPI2 är konstruerad för drift utan tillsyn. Med den förinstallerade HaLOS-avbilden — eller vilket operativsystem som helst med [HALPI-daemonen](./software.md#kommandoradsverktyget-halpi) installerad — är strömhanteringen automatisk: enheten laddar sina superkondensatorer för backup, rider ut korta spänningsstörningar, stänger av operativsystemet säkert när strömmen försvinner och startar igen när strömmen kommer tillbaka. Inget av detta kräver någon åtgärd från användaren.

## Slå på systemet

HALPI2 har ingen strömknapp på kapslingen: den startar så snart inspänning ansluts. (En extern strömknapp kan anslutas till bärkortet — se [Externa knappar](./interfaces.md#externa-knappar).) LED-raden fylls först med rött medan superkondensatorerna laddas (några sekunder till en halv minut, beroende på [inställningen av strömbegränsningen](./hardware.md#konfiguration-av-strombegransningen)). Därefter spelar lysdioderna upp en kort regnbågs- och färgväxlingsanimation medan Compute Module startar, visar en gul stapel medan operativsystemet startar och blir gröna när operativsystemet är i gång och HALPI-daemonen har anslutit.

## Stänga av systemet

Stäng av HALPI2 genom att bryta inspänningen — till exempel med en brytare på elpanelen. Systemet upptäcker spänningsbortfallet, stänger av operativsystemet kontrollerat på superkondensatorernas ström och förblir avstängt. Lysdioderna visar en violett stapel medan avstängningen pågår och släcks när den är klar.

Du kan också stänga av via programvaran — skrivbordsmenyn, kommandot `shutdown` eller `halpi shutdown`. Systemet stängs då av och förblir avstängt tills inspänningen bryts och återansluts (eller tills en [extern strömknapp](./interfaces.md#externa-knappar), om en sådan finns, trycks in).

Som tillval kan styrkretsen starta om systemet automatiskt ungefär 5 sekunder efter en avstängning via programvaran medan inspänningen fortfarande är ansluten, så att ett avstängningskommando av misstag aldrig lämnar en fysiskt svåråtkomlig installation strandad. Aktivera funktionen med `halpi config set auto_restart true`; inställningen sparas i styrkretsen. Enheter tillverkade före början av 2026 levererades med beteendet aktiverat — kontrollera din enhet med `halpi config get auto_restart`.

Systemet kan också försättas i vänteläge, där det stänger av sig och vaknar igen vid en schemalagd tidpunkt — se referensen [Bärkortets styrkrets](../technical-reference/controller.md#vantelage).

## Status-LED:ar

De fem lysdioderna på frontpanelen visar vad systemet gör:

| LED-mönster | Betydelse |
|:------------|:----------|
| Röd stapel som fylls | Superkondensatorerna laddas före start — vänta |
| Regnbåge och växlande färger | Compute Module startar. Om mönstret upprepas utan att något händer startade modulen inte — se [Felsökning](./troubleshooting.md#regnbagsfargade-lysdioder) |
| Gul stapel | Systemet kör, HALPI-daemonen har inte anslutit — normalt en kort stund under starten. Om det består, se [Felsökning](./troubleshooting.md#lysdioderna-forblir-gula) |
| Grön stapel | Normal drift |
| Orange eller mörkgrön stapel | Inspänningen borta, drift på backupström — avstängning följer om inte strömmen kommer tillbaka inom några sekunder |
| Violett stapel | Avstängning pågår |
| Alla lyser fast rött | Operativsystemet svarar inte — styrkretsen startar om det automatiskt |
| Alla blinkar rött | Fel på superkondensatorerna — kontakta supporten |
| Alla lyser fast blått | Övergång till vänteläge |
| Alla lyser dämpat rött | Vänteläge |
| Alla släckta | Avstängt |

I stapelmönstren visar antalet tända lysdioder superkondensatorernas laddningsnivå. De exakta spänningsfönstren och den fullständiga tillståndstabellen finns i referensen [Bärkortets styrkrets](../technical-reference/controller.md#status-led-referens).

Lysdiodernas ljusstyrka kan justeras — se [Styrning av lysdioderna](./software.md#styrning-av-lysdioderna). Lysdioderna kan också användas som display för systemmätvärden och marina data (nätverksaktivitet, tanknivåer, NMEA 2000- och Signal K-värden) med tillägget [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights).

## Vid spänningsbortfall

Ingenting behöver göras. Korta dippar och störningar — upp till 5 sekunder som standard — överbryggas av superkondensatorerna, och driften fortsätter ostörd. Vid ett längre avbrott stänger systemet av sig självt kontrollerat på de 30–60 sekunder av backupström som superkondensatorerna rymmer. När inspänningen kommer tillbaka startar systemet igen automatiskt.

!!! warning "Inte en UPS"
    Superkondensatorerna finns för att överbrygga korta störningar och driva en säker avstängning. För fortsatt drift under längre avbrott krävs en extern avbrottsfri strömförsörjning (UPS).

## Kontrollera systemets tillstånd

En grön LED-stapel betyder att systemet mår bra. För detaljer visar kommandot `halpi` styrkretsens tillstånd, spänningar, ström och temperaturer:

```bash
halpi status
```

Om något ser fel ut, se [Felsökning](./troubleshooting.md) och [Programvaruguiden](./software.md#kommandoradsverktyget-halpi).

## Drift utan daemonen

På operativsystem utan HALPI-daemonen faller styrkretsen tillbaka till ett grundläggande skyddsläge: den upptäcker fortfarande spänningsbortfall och begär en avstängning, men genom att simulera tryck på strömknappen — vilket misslyckas om systemet har hängt sig — och övervakning och konfiguration är inte tillgängliga. Om du kör ett eget operativsystem, installera daemonen; se [Andra Debian-distributioner](../software-development/ubuntu-installation.md). Hur de två lägena fungerar beskrivs i referensen [Bärkortets styrkrets](../technical-reference/controller.md#driftlagen).

!!! quote "Relaterad information"
    - **Hur strömhanteringen fungerar internt:** se [Bärkortets styrkrets](../technical-reference/controller.md)
    - **Strömförsörjningens detaljer:** se [Strömförsörjningen i detalj](../technical-reference/power-supply.md)
    - **Kommandot `halpi` och daemonen:** se [Programvaruguiden](./software.md)
    - **Problem:** se [Felsökning](./troubleshooting.md)

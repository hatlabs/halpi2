---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Daglig brug

HALPI2 er designet til drift uden opsyn. På det forudinstallerede HaLOS-image — eller på ethvert styresystem med [HALPI-dæmonen](./software.md#halpi-kommandolinjevrktjet) installeret — er strømstyringen automatisk: Enheden oplader superkondensatorerne, der fungerer som backup, klarer korte spændingsudfald, lukker styresystemet sikkert ned ved strømsvigt og starter op igen, når strømmen vender tilbage. Intet af dette kræver, at du foretager dig noget.

## Opstart

HALPI2 har ingen tænd/sluk-knap på kabinettet: Den starter, så snart der tilsluttes indgangsstrøm. (En ekstern tænd/sluk-knap kan tilsluttes bærekortet — se [Eksterne knapper](./interfaces.md#eksterne-knapper).) LED-søjlen fyldes først op med rødt, mens superkondensatorerne oplader (fra få sekunder til et halvt minut afhængigt af [indstillingen af strømgrænsen](./hardware.md#konfiguration-af-strmbegrnsning)). Derefter viser LED'erne en kort animation med regnbue og skiftende farver, mens Compute Module starter, en gul søjle, mens styresystemet starter op, og de bliver grønne, når styresystemet kører, og HALPI-dæmonen har forbundet sig.

## Nedlukning

Du lukker HALPI2 ned ved at afbryde indgangsstrømmen — for eksempel med en afbryder på eltavlen. Systemet registrerer strømsvigtet, lukker styresystemet kontrolleret ned på strøm fra superkondensatorerne og forbliver slukket. LED'erne viser en lilla søjle, mens nedlukningen kører, og slukker, når den er gennemført.

Du kan også lukke ned via software — skrivebordsmenuen, kommandoen `shutdown` eller `halpi shutdown`. Systemet slukker derefter og forbliver slukket, indtil indgangsstrømmen har været afbrudt og tilsluttet igen (eller der trykkes på en [ekstern tænd/sluk-knap](./interfaces.md#eksterne-knapper), hvis en sådan er monteret).

Controlleren kan desuden genstarte systemet automatisk cirka 5 sekunder efter en softwarenedlukning, mens indgangsstrømmen stadig er tilsluttet, så en utilsigtet nedlukningskommando aldrig efterlader en fysisk svært tilgængelig installation slukket. Slå det til med `halpi config set auto_restart true`; indstillingen gemmes i controlleren. Enheder produceret før starten af 2026 blev leveret med denne adfærd slået til — kontrollér din med `halpi config get auto_restart`.

Systemet kan også sættes i standby, hvor det slukker og vågner igen på et planlagt tidspunkt — se referencen [Bærekortets controller](../technical-reference/controller.md#standby).

## Status-LED-indikatorer

De fem LED'er på frontpanelet viser, hvad systemet er i gang med:

| LED-mønster | Betydning |
|:------------|:----------|
| Rød søjle, der fyldes op | Superkondensatorerne oplader før opstart — vent |
| Regnbue og skiftende farver | Compute Module starter. Hvis mønsteret gentager sig uden fremskridt, kunne modulet ikke starte — se [Fejlfinding](./troubleshooting.md#regnbue-leder) |
| Gul søjle | Systemet kører, HALPI-dæmonen er ikke forbundet — normalt i kort tid under opstart. Hvis det varer ved, se [Fejlfinding](./troubleshooting.md#lederne-bliver-ved-med-at-vre-gule) |
| Grøn søjle | Normal drift |
| Orange eller mørkegrøn søjle | Indgangsstrømmen er væk, systemet kører på backup — nedlukning følger, medmindre strømmen vender tilbage inden for få sekunder |
| Lilla søjle | Nedlukning i gang |
| Alle lyser konstant rødt | Styresystemet svarer ikke — controlleren genstarter det automatisk |
| Alle blinker rødt | Fejl i superkondensatorerne — kontakt support |
| Alle lyser konstant blåt | På vej i standby |
| Alle lyser svagt rødt | Standby |
| Alle slukket | Slukket |

I søjlemønstrene viser antallet af tændte LED'er superkondensatorernes ladeniveau. De præcise spændingsintervaller og den fulde tilstandsoversigt findes i referencen [Bærekortets controller](../technical-reference/controller.md#status-led-reference).

LED'ernes lysstyrke kan justeres — se [LED-styring](./software.md#led-styring). LED'erne kan også bruges som display for systemmålinger og marinedata (netværksaktivitet, tankniveauer, NMEA 2000- og Signal K-værdier) med tilføjelsen [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights).

## Ved strømsvigt

Du behøver ikke at foretage dig noget. Korte dyk og udfald — som standard op til 5 sekunder — dækkes af superkondensatorerne, og driften fortsætter uforstyrret. Ved en længere afbrydelse lukker systemet sig selv kontrolleret ned på de 30–60 sekunders backupstrøm, som superkondensatorerne rummer. Når indgangsstrømmen vender tilbage, starter systemet automatisk op igen.

!!! warning "Ikke en UPS"
    Superkondensatorerne er der for at dække korte udfald og levere strøm til en sikker nedlukning. Fortsat drift under længerevarende strømafbrydelser kræver en ekstern UPS (nødstrømsforsyning).

## Kontrol af systemets tilstand

En grøn LED-søjle betyder, at systemet har det godt. Vil du have detaljer, viser kommandoen `halpi` controllerens tilstand, spændinger, strøm og temperaturer:

```bash
halpi status
```

Hvis noget ser forkert ud, se [Fejlfinding](./troubleshooting.md) og [Softwarevejledningen](./software.md#halpi-kommandolinjevrktjet).

## Drift uden dæmonen

På styresystemer uden HALPI-dæmonen falder controlleren tilbage til en grundlæggende beskyttelsestilstand: Den registrerer stadig strømsvigt og beder om nedlukning, men ved at simulere tryk på tænd/sluk-knappen — hvilket ikke virker, hvis systemet er frosset — og overvågning og konfiguration er ikke til rådighed. Hvis du kører dit eget styresystem, skal du installere dæmonen; se [Andre Debian-distributioner](../software-development/ubuntu-installation.md). Hvordan de to tilstande fungerer, er beskrevet i referencen [Bærekortets controller](../technical-reference/controller.md#driftstilstande).

!!! quote "Relaterede oplysninger"
    - **Sådan fungerer strømstyringen internt:** Se [Bærekortets controller](../technical-reference/controller.md)
    - **Detaljer om strømsystemet:** Se [Strømforsyningen i detaljer](../technical-reference/power-supply.md)
    - **Kommandoen `halpi` og dæmonen:** Se [Softwarevejledningen](./software.md)
    - **Problemer:** Se [Fejlfinding](./troubleshooting.md)

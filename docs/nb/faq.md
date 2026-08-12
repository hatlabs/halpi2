---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Ofte stilte spørsmål

## Hvorfor starter HALPI2 igjen etter at jeg har slått den av?

Enheten din har automatisk omstart aktivert: med `auto_restart` satt til `true` starter kontrolleren systemet igjen omtrent 5 sekunder etter en nedstenging fra programvaren så lenge inngangsstrøm er tilkoblet. Enheter produsert før tidlig i 2026 ble levert slik; nåværende enheter leveres med funksjonen deaktivert. Slå den av med `halpi config set auto_restart false` – eller behold den, siden den sørger for at et system uten tilsyn ikke blir stående avslått etter en utilsiktet nedstengingskommando. Med funksjonen aktivert slår du av permanent ved å kutte inngangsstrømmen. Se [Slå av](user-guide/operation.md#sla-av).

## Hvordan slår jeg av HALPI2?

Kutt inngangsstrømmen. Systemet oppdager strømbortfallet og stenger kontrollert ned på strøm fra superkondensatorene – dette er den tiltenkte måten å slå det av på. Se [Slå av](user-guide/operation.md#sla-av).

## Må jeg gjøre noe når strømmen går?

Nei. Korte forstyrrelser dekkes av superkondensatorene, lengre strømbrudd utløser en automatisk trygg nedstenging, og systemet starter igjen av seg selv når strømmen kommer tilbake. Se [Ved strømbortfall](user-guide/operation.md#ved-strmbortfall).

## Hvor lenge varer reservestrømmen?

Superkondensatorene gir 30–60 sekunder, avhengig av systembelastningen. Det er nok til en trygg nedstenging med god margin, men HALPI2 er ikke en UPS – den fortsetter ikke å kjøre gjennom lengre strømbrudd. Se [Strømforsyningen i detalj](technical-reference/power-supply.md).

## Kan HALPI2 stå på døgnet rundt?

Ja. HALPI2 er laget for kontinuerlig drift uten tilsyn, og strømstyringen forutsetter det: systemet henter seg inn igjen etter strømbortfall og etter at operativsystemet har hengt seg, uten at brukeren trenger å gripe inn.

## Hva betyr det at LED-ene blir stående gule?

En gul søyle betyr at systemet kjører, men at HALPI-daemonen ikke har koblet seg til – normalt en kort stund under oppstart. En vedvarende gul søyle betyr at operativsystemet ikke starter opp, eller at daemonen ikke er installert. Se [Feilsøking](user-guide/troubleshooting.md#led-ene-blir-staende-gule).

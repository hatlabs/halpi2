---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Vanliga frågor

## Varför startar HALPI2 om efter att jag stängt av den?

Din enhet har automatisk omstart aktiverad: med `auto_restart` satt till `true` startar styrkretsen om systemet ungefär 5 sekunder efter en avstängning via programvaran medan inspänningen är ansluten. Enheter tillverkade före början av 2026 levererades så; nuvarande enheter levereras med funktionen avstängd. Stäng av den med `halpi config set auto_restart false` — eller behåll den, eftersom den ser till att ett system utan tillsyn inte blir stående avstängt efter ett avstängningskommando av misstag. Med funktionen aktiverad stänger du av permanent genom att bryta inspänningen. Se [Stänga av systemet](user-guide/operation.md#stanga-av-systemet).

## Hur stänger jag av HALPI2?

Bryt inspänningen. Systemet upptäcker spänningsbortfallet och stänger av sig kontrollerat på superkondensatorernas ström — det är det avsedda sättet att stänga av. Se [Stänga av systemet](user-guide/operation.md#stanga-av-systemet).

## Behöver jag göra något när strömmen försvinner?

Nej. Korta störningar överbryggas av superkondensatorerna, längre avbrott utlöser en automatisk säker avstängning, och systemet startar om av sig självt när strömmen kommer tillbaka. Se [Vid spänningsbortfall](user-guide/operation.md#vid-spanningsbortfall).

## Hur länge räcker backupströmmen?

Superkondensatorerna ger 30–60 sekunder, beroende på systemets belastning. Det räcker för en säker avstängning med marginal, men HALPI2 är ingen UPS — den fortsätter inte att köra genom längre avbrott. Se [Strömförsörjningen i detalj](technical-reference/power-supply.md).

## Kan HALPI2 vara påslagen dygnet runt?

Ja. HALPI2 är konstruerad för kontinuerlig drift utan tillsyn, och strömhanteringen förutsätter det: systemet återhämtar sig från spänningsbortfall och operativsystemshängningar utan att användaren behöver ingripa.

## Vad betyder det när lysdioderna förblir gula?

En gul stapel betyder att systemet kör men att HALPI-daemonen inte har anslutit — normalt en kort stund under starten. En gul stapel som består betyder att operativsystemet inte startar eller att daemonen inte är installerad. Se [Felsökning](user-guide/troubleshooting.md#lysdioderna-forblir-gula).

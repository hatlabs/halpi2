---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Ofte stillede spørgsmål

## Hvorfor genstarter HALPI2, efter at jeg har lukket den ned?

Din enhed har automatisk genstart slået til: Med `auto_restart` sat til `true` genstarter controlleren systemet cirka 5 sekunder efter en softwarenedlukning, mens der er indgangsstrøm tilsluttet. Enheder produceret før starten af 2026 blev leveret sådan; aktuelle enheder leveres med funktionen slået fra. Slå den fra med `halpi config set auto_restart false` — eller behold den, for den sikrer, at et system uden opsyn ikke forbliver slukket efter en utilsigtet nedlukningskommando. Med funktionen slået til lukker du permanent ned ved at afbryde indgangsstrømmen. Se [Nedlukning](user-guide/operation.md#nedlukning).

## Hvordan slukker jeg HALPI2?

Afbryd indgangsstrømmen. Systemet registrerer strømsvigtet og lukker kontrolleret ned på strøm fra superkondensatorerne — det er den måde, enheden er designet til at blive slukket på. Se [Nedlukning](user-guide/operation.md#nedlukning).

## Skal jeg gøre noget, når strømmen går?

Nej. Korte udfald dækkes af superkondensatorerne, længere afbrydelser udløser en automatisk sikker nedlukning, og systemet genstarter af sig selv, når strømmen vender tilbage. Se [Ved strømsvigt](user-guide/operation.md#ved-strmsvigt).

## Hvor længe holder backupstrømmen?

Superkondensatorerne giver 30–60 sekunder afhængigt af systemets belastning. Det er nok til en sikker nedlukning med margin, men HALPI2 er ikke en UPS — den kører ikke videre under længerevarende strømafbrydelser. Se [Strømforsyningen i detaljer](technical-reference/power-supply.md).

## Kan HALPI2 være tændt døgnet rundt?

Ja. HALPI2 er designet til kontinuerlig drift uden opsyn, og strømstyringen forudsætter det: Systemet genopretter sig selv efter strømsvigt, og efter at styresystemet er hængt, uden at brugeren skal gribe ind.

## Hvad betyder det, når LED'erne bliver ved med at være gule?

En gul søjle betyder, at systemet kører, men at HALPI-dæmonen ikke har forbundet sig — det er normalt i kort tid under opstart. En vedvarende gul søjle betyder, at styresystemet ikke starter op, eller at dæmonen ikke er installeret. Se [Fejlfinding](user-guide/troubleshooting.md#lederne-bliver-ved-med-at-vre-gule).

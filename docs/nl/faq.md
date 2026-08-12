---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Veelgestelde vragen

## Waarom start de HALPI2 opnieuw op nadat ik hem heb afgesloten?

Op uw apparaat staat de automatische herstart aan: met `auto_restart` op `true` start de controller het systeem ongeveer 5 seconden na een afsluiting via software opnieuw op zolang er ingangsspanning is aangesloten. Apparaten die vóór begin 2026 zijn geproduceerd, werden zo geleverd; huidige apparaten worden met deze functie uitgeschakeld geleverd. Schakel de functie uit met `halpi config set auto_restart false` — of houd haar aan, want zo blijft een systeem zonder toezicht niet uit staan na een per ongeluk gegeven afsluitopdracht. Staat de functie aan, sluit dan definitief af door de ingangsspanning uit te schakelen. Zie [Afsluiten](user-guide/operation.md#afsluiten).

## Hoe schakel ik de HALPI2 uit?

Schakel de ingangsspanning uit. Het systeem detecteert de spanningsuitval en sluit gecontroleerd af op de spanning van de supercondensatoren — zo is het uitschakelen bedoeld. Zie [Afsluiten](user-guide/operation.md#afsluiten).

## Moet ik iets doen wanneer de stroom uitvalt?

Nee. Korte storingen worden overbrugd door de supercondensatoren, langere stroomuitval activeert een automatische veilige afsluiting en het systeem start vanzelf opnieuw op zodra de spanning terugkeert. Zie [Bij spanningsuitval](user-guide/operation.md#bij-spanningsuitval).

## Hoe lang gaat de backupvoeding mee?

De supercondensatoren leveren 30–60 seconden, afhankelijk van de systeembelasting. Dat is genoeg voor een veilige afsluiting met marge, maar de HALPI2 is geen UPS — hij blijft niet doorwerken tijdens langdurige stroomuitval. Zie [De voeding in detail](technical-reference/power-supply.md).

## Kan de HALPI2 dag en nacht aan blijven staan?

Ja. De HALPI2 is ontworpen voor continu gebruik zonder toezicht en het energiebeheer gaat daarvan uit: het systeem herstelt zich van spanningsuitval en van het vastlopen van het besturingssysteem zonder tussenkomst van de gebruiker.

## Wat betekent het wanneer de leds geel blijven?

Een gele balk betekent dat het systeem draait maar dat de HALPI-daemon geen verbinding heeft — kort tijdens het opstarten is dat normaal. Een aanhoudend gele balk betekent dat het besturingssysteem niet opstart of dat de daemon niet is geïnstalleerd. Zie [Probleemoplossing](user-guide/troubleshooting.md#leds-blijven-geel).

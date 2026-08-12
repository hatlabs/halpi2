---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# FAQ

## Warum startet der HALPI2 nach dem Herunterfahren neu?

Bei Ihrem Gerät ist der automatische Neustart aktiviert: Steht `auto_restart` auf `true`, startet der Controller das System etwa 5 Sekunden nach einem Herunterfahren per Software neu, solange die Eingangsspannung anliegt. Geräte aus der Produktion vor Anfang 2026 wurden so ausgeliefert; aktuelle Geräte kommen mit deaktiviertem Verhalten. Schalten Sie es mit `halpi config set auto_restart false` ab — oder behalten Sie es bei, denn es stellt sicher, dass ein unbeaufsichtigtes System nach einem versehentlichen Shutdown-Befehl nicht ausgeschaltet bleibt. Ist es aktiviert, schalten Sie das Gerät dauerhaft ab, indem Sie die Eingangsspannung trennen. Siehe [Herunterfahren](user-guide/operation.md#herunterfahren).

## Wie schalte ich den HALPI2 aus?

Trennen Sie die Eingangsspannung. Das System erkennt den Spannungsausfall und fährt mit der Energie der Superkondensatoren geordnet herunter — das ist der vorgesehene Weg, das Gerät auszuschalten. Siehe [Herunterfahren](user-guide/operation.md#herunterfahren).

## Muss ich etwas tun, wenn der Strom ausfällt?

Nein. Kurze Störimpulse überbrücken die Superkondensatoren, längere Ausfälle lösen ein automatisches sicheres Herunterfahren aus, und das System startet von selbst neu, wenn die Spannung zurückkehrt. Siehe [Bei Spannungsausfall](user-guide/operation.md#bei-spannungsausfall).

## Wie lange hält die Pufferung?

Die Superkondensatoren liefern 30–60 Sekunden, abhängig von der Systemlast. Das genügt für ein sicheres Herunterfahren mit Reserve, aber der HALPI2 ist keine USV — bei längeren Stromausfällen läuft er nicht weiter. Siehe [Stromversorgung im Detail](technical-reference/power-supply.md).

## Kann der HALPI2 rund um die Uhr eingeschaltet bleiben?

Ja. Der HALPI2 ist für den unbeaufsichtigten Dauerbetrieb ausgelegt, und seine Energieverwaltung setzt das voraus: Das System erholt sich ohne Zutun des Anwenders von Spannungsausfällen und von einem hängenden Betriebssystem.

## Was bedeutet es, wenn die LEDs gelb bleiben?

Ein gelber Balken bedeutet, dass das System läuft, der HALPI-Daemon aber nicht verbunden ist — beim Start für kurze Zeit normal. Ein dauerhaft gelber Balken bedeutet, dass das Betriebssystem nicht startet oder der Daemon nicht installiert ist. Siehe [Fehlersuche](user-guide/troubleshooting.md#die-leds-bleiben-gelb).

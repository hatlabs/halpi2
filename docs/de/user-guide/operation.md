---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Täglicher Betrieb

Der HALPI2 ist für den unbeaufsichtigten Betrieb ausgelegt. Mit dem vorinstallierten HaLOS-Image — oder jedem Betriebssystem mit installiertem [HALPI-Daemon](./software.md#kommandozeilenwerkzeug-halpi) — läuft die Energieverwaltung automatisch: Das Gerät lädt seine Puffer-Superkondensatoren, überbrückt Spannungseinbrüche, fährt das Betriebssystem bei Spannungsausfall sicher herunter und startet wieder, sobald die Spannung zurückkehrt. Nichts davon erfordert ein Eingreifen des Anwenders.

## Einschalten

Der HALPI2 hat keine Ein-/Aus-Taste am Gehäuse: Er startet, sobald die Eingangsspannung anliegt. (Ein externer Power-Taster lässt sich an die Trägerplatine anschließen — siehe [Externe Taster](./interfaces.md#externe-taster).) Die LED-Leiste füllt sich zunächst mit Rot, während die Superkondensatoren laden (einige Sekunden bis eine halbe Minute, abhängig von der [Einstellung der Strombegrenzung](./hardware.md#einstellung-der-strombegrenzung)). Danach zeigen die LEDs eine kurze Regenbogen- und Farbwechselanimation, während das Compute Module startet, einen gelben Balken, während das Betriebssystem hochfährt, und wechseln zu Grün, sobald das Betriebssystem läuft und der HALPI-Daemon verbunden ist.

## Herunterfahren

Um den HALPI2 auszuschalten, trennen Sie die Eingangsspannung — zum Beispiel über einen Schalter am Schaltpaneel. Das System erkennt den Spannungsausfall, fährt das Betriebssystem mit der Energie der Superkondensatoren geordnet herunter und bleibt aus. Die LEDs zeigen während des Herunterfahrens einen violetten Balken und erlöschen, wenn es abgeschlossen ist.

Sie können das System auch aus der Software herunterfahren — über das Desktop-Menü, den Befehl `shutdown` oder `halpi shutdown`. Das Gerät schaltet dann ab und bleibt aus, bis die Eingangsspannung getrennt und wieder verbunden wird (oder ein [externer Power-Taster](./interfaces.md#externe-taster), falls vorhanden, gedrückt wird).

Optional kann der Controller das System etwa 5 Sekunden nach einem Herunterfahren per Software automatisch neu starten, solange die Eingangsspannung anliegt — ein versehentlicher Shutdown-Befehl legt so keine Installation still, die räumlich schwer zugänglich ist. Aktivieren Sie das Verhalten mit `halpi config set auto_restart true`; die Einstellung bleibt im Controller gespeichert. Geräte aus der Produktion vor Anfang 2026 wurden mit aktiviertem Verhalten ausgeliefert — prüfen Sie Ihr Gerät mit `halpi config get auto_restart`.

Das System lässt sich auch in den Standby versetzen: Es schaltet ab und wacht zu einem festgelegten Zeitpunkt wieder auf — siehe die Referenz [Controller der Trägerplatine](../technical-reference/controller.md#standby).

## Status-LEDs

Die fünf LEDs an der Frontplatte zeigen, was das System gerade tut:

| LED-Muster | Bedeutung |
|:-----------|:----------|
| Roter Balken füllt sich | Superkondensatoren laden vor dem Start — abwarten |
| Regenbogen und wechselnde Farben | Das Compute Module startet. Wiederholt sich das Muster ohne Fortschritt, ist der Start fehlgeschlagen — siehe [Fehlersuche](./troubleshooting.md#regenbogenfarbene-leds) |
| Gelber Balken | System läuft, HALPI-Daemon nicht verbunden — beim Start für kurze Zeit normal. Bleibt der Zustand bestehen, siehe [Fehlersuche](./troubleshooting.md#die-leds-bleiben-gelb) |
| Grüner Balken | Normalbetrieb |
| Oranger oder dunkelgrüner Balken | Eingangsspannung ausgefallen, Betrieb auf Pufferenergie — das Herunterfahren folgt, wenn die Spannung nicht binnen Sekunden zurückkehrt |
| Violetter Balken | System fährt herunter |
| Alle dauerhaft rot | Betriebssystem reagiert nicht — der Controller startet es automatisch neu |
| Alle blinken rot | Fehler der Superkondensatoren — wenden Sie sich an den Support |
| Alle dauerhaft blau | Wechsel in den Standby |
| Alle gedimmt rot | Standby |
| Alle aus | Ausgeschaltet |

Bei den Balkenmustern zeigt die Zahl der leuchtenden LEDs den Ladezustand der Superkondensatoren. Die genauen Spannungsfenster und die vollständige Zuordnung der Zustände stehen in der Referenz [Controller der Trägerplatine](../technical-reference/controller.md#status-led-referenz).

Die Helligkeit der LEDs lässt sich anpassen — siehe [Steuerung der LEDs](./software.md#steuerung-der-leds). Mit der Erweiterung [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights) lassen sich die LEDs auch als Anzeige für Systemwerte und Schiffsdaten nutzen (Netzwerkaktivität, Tankfüllstände, NMEA-2000- und Signal-K-Werte).

## Bei Spannungsausfall

Sie müssen nichts tun. Kurze Einbrüche und Störimpulse — standardmäßig bis zu 5 Sekunden — überbrücken die Superkondensatoren, und der Betrieb läuft ungestört weiter. Bei einem längeren Ausfall fährt sich das System mit den 30–60 Sekunden Pufferenergie der Superkondensatoren geordnet herunter. Kehrt die Eingangsspannung zurück, startet das System automatisch neu.

!!! warning "Keine USV"
    Die Superkondensatoren sind dazu da, Störimpulse zu überbrücken und ein sicheres Herunterfahren zu versorgen. Für den Weiterbetrieb bei längeren Stromausfällen ist eine externe unterbrechungsfreie Stromversorgung (USV) erforderlich.

## Systemzustand prüfen

Ein grüner LED-Balken bedeutet, dass das System in Ordnung ist. Für Einzelheiten zeigt der Befehl `halpi` den Zustand des Controllers, Spannungen, Stromaufnahme und Temperaturen:

```bash
halpi status
```

Sieht etwas nicht richtig aus, siehe [Fehlersuche](./troubleshooting.md) und das [Software-Handbuch](./software.md#kommandozeilenwerkzeug-halpi).

## Betrieb ohne den Daemon

Auf Betriebssystemen ohne den HALPI-Daemon fällt der Controller in einen einfachen Schutzmodus zurück: Er erkennt Spannungsausfälle weiterhin und fordert das Herunterfahren an, allerdings über simulierte Betätigungen der Ein-/Aus-Taste — was bei einem eingefrorenen System fehlschlägt — und Überwachung wie Konfiguration stehen nicht zur Verfügung. Wenn Sie ein eigenes Betriebssystem einsetzen, installieren Sie den Daemon; siehe [Andere Debian-Distributionen](../software-development/ubuntu-installation.md). Wie die beiden Betriebsarten arbeiten, beschreibt die Referenz [Controller der Trägerplatine](../technical-reference/controller.md#betriebsarten).

!!! quote "Weiterführende Informationen"
    - **So arbeitet die Energieverwaltung intern:** siehe [Controller der Trägerplatine](../technical-reference/controller.md)
    - **Einzelheiten zur Stromversorgung:** siehe [Stromversorgung im Detail](../technical-reference/power-supply.md)
    - **Der Befehl `halpi` und der Daemon:** siehe [Software-Handbuch](./software.md)
    - **Probleme:** siehe [Fehlersuche](./troubleshooting.md)

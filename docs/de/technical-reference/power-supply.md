---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Stromversorgung im Detail

Die Stromversorgung des HALPI2 ist für die instabilen elektrischen Umgebungen von Booten und Fahrzeugen ausgelegt: Sie verkraftet Spannungsspitzen und Störimpulse, begrenzt den Einschaltstrom und speichert genug Energie, um das System bei einem Spannungsausfall sicher herunterzufahren.

Die elektrischen Spezifikationen stehen in der [Hardware-Referenz](./hardware.md). Den Zustandsautomaten, der auf die hier beschriebenen Messwerte reagiert, beschreibt die Referenz [Controller der Trägerplatine](./controller.md).

## Eingangsstufe

Der nominelle Eingangsbereich beträgt 10–32 V DC und deckt 12-V- wie 24-V-Systeme ab. Die Eingangsstufe ist gegen Verpolung und gegen transiente Überspannungen bis 100 V geschützt, etwa den Lastabwurf (Load Dump) einer Lichtmaschine.

### Strombegrenzung

Eine Eingangsstrombegrenzung steuert den maximalen Strom, der aus der Quelle gezogen wird — wählbar zwischen 0,9 A und 2,5 A über einen Schalter auf der Trägerplatine. Die Begrenzung erfüllt zwei Zwecke:

- Sie begrenzt den Einschaltstrom, wenn die entladenen Superkondensatoren beim Einschalten zu laden beginnen.
- Sie hält die Gesamtaufnahme innerhalb des Leistungsbudgets der Quelle — mit der Einstellung 0,9 A (LEN 18) lässt sich der HALPI2 gefahrlos aus einem NMEA-2000-Bus versorgen.

Die Standardeinstellung ist 0,9 A. Wählen Sie 2,5 A, wenn das System Peripheriegeräte mit hohem Strombedarf versorgt oder ein schnellerer Start gewünscht ist. Lage des Schalters und Vorgehen beim Umstellen beschreibt das [Hardware-Handbuch](../user-guide/hardware.md#einstellung-der-strombegrenzung).

## Pufferung durch Superkondensatoren

Eine Superkondensatorbank liefert die Pufferenergie für geordnetes Herunterfahren. Anders als eine batteriegestützte USV verschleißen Superkondensatoren nicht, arbeiten über den gesamten Temperaturbereich und laden in Sekunden — um den Preis einer deutlich kleineren Energiereserve.

### Laden

Die Superkondensatoren laden, sobald Eingangsspannung anliegt. Aus dem entladenen Zustand dauert das Laden etwa:

- 25 Sekunden bei einer Strombegrenzung von 0,9 A
- 9 Sekunden bei einer Strombegrenzung von 2,5 A

Die LEDs an der Frontplatte zeigen den Ladefortschritt als roten Balken, der sich füllt. Das Compute Module wird eingeschaltet, sobald die Superkondensator-Spannung die Einschaltschwelle erreicht (standardmäßig 8,0 V).

### Dauer der Pufferung

Fällt die Eingangsspannung aus, tragen die Superkondensatoren die gesamte Systemlast. Sie liefern 30–60 Sekunden Laufzeit, abhängig von Systemlast und angeschlossenen Peripheriegeräten — genug für ein geordnetes Herunterfahren des Betriebssystems mit Reserve.

!!! warning "Keine USV"
    Das System aus Superkondensatoren ist dafür ausgelegt, Störimpulse zu überbrücken und ein sicheres Herunterfahren zu versorgen. Für den Weiterbetrieb bei längeren Stromausfällen ist es nicht gedacht.

## Erkennung von Spannungsausfällen

Der Controller misst die Eingangsspannung fortlaufend und wertet die Eingangsspannung als ausgefallen, wenn sie unter 9,0 V fällt. Ein Ausfallzeitgeber (standardmäßig 5 Sekunden) unterdrückt das Herunterfahren bei kurzen Unterbrechungen: Die Superkondensatoren überbrücken die Lücke, und der Betrieb läuft ungestört weiter, wenn die Spannung rechtzeitig zurückkehrt. Längere Ausfälle lösen die automatischen Abläufe des Herunterfahrens aus, die in der Referenz [Controller der Trägerplatine](./controller.md#spannungsausfall-und-herunterfahren) beschrieben sind.

## Überwachung

Der Controller misst Eingangsspannung, Eingangsstrom und Superkondensator-Spannung und stellt die Werte über den HALPI-Daemon bereit:

```bash
halpi status
```

Die Werte sind auch programmatisch über die REST-API des Daemons abrufbar — siehe das [Software-Handbuch](../user-guide/software.md#zugriff-uber-die-rest-api).

!!! quote "Weiterführende Informationen"
    - **Elektrische Spezifikationen:** siehe [Hardware-Referenz](./hardware.md)
    - **Zustandsautomat und Abläufe des Herunterfahrens:** siehe [Controller der Trägerplatine](./controller.md)
    - **Alltägliches Verhalten der Stromversorgung:** siehe [Täglicher Betrieb](../user-guide/operation.md)

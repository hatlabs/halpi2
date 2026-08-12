---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Controller der Trägerplatine

Die Trägerplatine des HALPI2 enthält einen RP2040-Mikrocontroller, der die Stromversorgung verwaltet, das System überwacht und die LEDs an der Frontplatte steuert. Der Controller arbeitet unabhängig vom Compute Module: Er läuft vom Anlegen der Eingangsspannung an, bevor das Betriebssystem startet und nachdem es heruntergefahren ist. Das Compute Module kommuniziert mit ihm über I2C (Bus 1, Adresse `0x6d`), vermittelt durch den [HALPI-Daemon](../user-guide/software.md#kommandozeilenwerkzeug-halpi).

Diese Seite beschreibt die Betriebsarten, Zustandsübergänge und Konfiguration des Controllers. Sie dokumentiert die Firmware-Version 3.3.x. Für den Alltag ist nichts davon Pflichtlektüre — siehe stattdessen [Täglicher Betrieb](../user-guide/operation.md).

## Betriebsarten

Der Controller arbeitet in einer von zwei Betriebsarten, je nachdem, ob der HALPI-Daemon mit ihm kommuniziert.

### Co-op-Modus

Der Co-op-Modus ist die normale Betriebsart. Er ist aktiv, wenn der HALPI-Daemon (`halpid`) läuft und mit dem Controller kommuniziert. Das vorinstallierte HaLOS-Image und alle Betriebssystem-Images von Hat Labs enthalten den Daemon.

Im Co-op-Modus:

- Controller und Daemon tauschen Daten in Echtzeit aus: Spannungen, Stromaufnahme, Temperaturen und Zustand.
- Spannungsausfälle werden dem Daemon gemeldet, der ein geordnetes Herunterfahren des Betriebssystems einleitet.
- Der Watchdog schützt vor einem hängenden Betriebssystem (siehe [Schutz durch Watchdog](#schutz-durch-watchdog)).
- Die Konfiguration lässt sich mit dem Kommandozeilenwerkzeug `halpi` lesen und ändern.

### Solo-Modus

Der Solo-Modus ist die Rückfallebene. Der Controller wechselt in ihn, wenn keine Kommunikation mit dem Daemon besteht:

- während des Starts, bevor der Daemon läuft
- wenn der Daemon nicht installiert, deaktiviert oder abgestürzt ist
- auf Betriebssystemen ohne HALPI2-Unterstützung

Auch im Solo-Modus schützt der Controller vor Spannungsausfällen, allerdings mit einem gröberen Mechanismus: Er fordert das Herunterfahren über simulierte Betätigungen der Ein-/Aus-Taste an und kann nicht erkennen, ob das Betriebssystem das Herunterfahren tatsächlich geordnet abgeschlossen hat.

!!! tip "Zuverlässigkeit des Solo-Modus"
    Der Solo-Modus bietet einen unverzichtbaren Schutz, ist aber weniger zuverlässig als der Co-op-Modus. Simulierte Tastenbetätigungen wirken nicht, wenn das Betriebssystem eingefroren ist. Wenn Sie ein eigenes Betriebssystem einsetzen, installieren Sie den HALPI-Daemon — siehe [Andere Debian-Distributionen](../software-development/ubuntu-installation.md).

## Spannungsausfall und Herunterfahren

Der Controller überwacht die Eingangsspannung fortlaufend. Fällt sie unter 9,0 V, gilt die Eingangsspannung als ausgefallen. Ein Ausfallzeitgeber (standardmäßig 5 Sekunden) unterscheidet kurze Störimpulse von echten Ausfällen: Die Superkondensatoren überbrücken die Lücke, und kehrt die Spannung innerhalb der Frist zurück, passiert nichts weiter.

### Ablauf des Herunterfahrens im Co-op-Modus

1. Der Daemon erkennt den Spannungsausfall an den Spannungsmesswerten des Controllers.
2. Der Daemon wartet den Ablauf des Ausfallzeitgebers ab (standardmäßig 5 Sekunden).
3. Der Daemon führt den konfigurierten Abschaltbefehl aus (standardmäßig `/sbin/poweroff`).
4. Das Betriebssystem fährt mit der Energie der Superkondensatoren geordnet herunter.
5. Der Controller erkennt, dass das Compute Module abgeschaltet hat, und schaltet die 5-V-Schiene ab.
6. Ist das Herunterfahren nicht innerhalb von 60 Sekunden abgeschlossen, erzwingt der Controller das Abschalten.
7. Das System bleibt ausgeschaltet, bis die Eingangsspannung zurückkehrt, und startet dann automatisch neu.

### Ablauf des Herunterfahrens im Solo-Modus

1. Der Controller erkennt den Spannungsausfall und startet den Ausfallzeitgeber (standardmäßig 5 Sekunden).
2. Nach Ablauf des Zeitgebers simuliert der Controller einen Doppeldruck der Ein-/Aus-Taste.
3. Das Betriebssystem reagiert und beginnt, mit der Energie der Superkondensatoren geordnet herunterzufahren.
4. Ist das Herunterfahren nicht innerhalb von 60 Sekunden abgeschlossen, erzwingt der Controller das Abschalten.
5. Das System bleibt ausgeschaltet, bis die Eingangsspannung zurückkehrt, und startet dann automatisch neu.

### Neustartverhalten nach einem Herunterfahren per Software

Ein per Software ausgelöstes Herunterfahren bei weiterhin anliegender Eingangsspannung (etwa über den Befehl `shutdown` oder das Desktop-Menü) endet im Zustand *ausgeschaltet*. Was danach geschieht, hängt von der Konfigurationseinstellung `auto_restart` ab:

- `auto_restart` deaktiviert (Werkseinstellung bei Geräten aus der Produktion seit Anfang 2026): Das System bleibt aus, bis die Eingangsspannung getrennt und wieder verbunden oder ein Power-Taster gedrückt wird.
- `auto_restart` aktiviert (Rückfallwert der Firmware und Werkseinstellung früherer Geräte): Der Controller startet das System nach 5 Sekunden neu, damit ein unbeaufsichtigtes System nicht wegen eines versehentlichen Shutdown-Befehls ausgeschaltet bleibt.

Ändern Sie die Einstellung mit `halpi config set auto_restart <true|false>`.

Ein Druck auf den Power-Taster oder das Trennen und Wiederverbinden der Eingangsspannung startet das System immer neu, unabhängig von der Einstellung `auto_restart`.

## Schutz durch Watchdog

Im Co-op-Modus schützt ein Watchdog vor einem hängenden Betriebssystem:

- Der Daemon muss dem Controller in regelmäßigen Abständen ein Watchdog-Signal senden.
- Bleibt das Signal länger als das Watchdog-Zeitlimit aus (standardmäßig 10 Sekunden), betrachtet der Controller den Host als nicht mehr ansprechbar, zeigt das Alarmmuster der LEDs (alle LEDs dauerhaft rot) und schaltet das Compute Module zur Wiederherstellung aus und wieder ein.
- Das Zeitlimit ist konfigurierbar mit `halpi config set watchdog_timeout <seconds>`.

## Standby

Im Standby ist das Compute Module abgeschaltet, während der Controller aktiv bleibt und auf einen geplanten Weckzeitpunkt wartet:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Während des Übergangs leuchten alle LEDs dauerhaft blau; im Standby leuchten sie gedimmt rot. Der Controller startet das System zum geplanten Zeitpunkt, bei einem Druck auf den Power-Taster oder nach dem Trennen und Wiederverbinden der Eingangsspannung neu.

## Status-LED-Referenz

Die fünf RGB-LEDs an der Frontplatte spiegeln den Zustand des Controllers wider. Diese Tabelle ist die maßgebliche Zuordnung der Controller-Zustände zu den LED-Mustern; die Seite [Täglicher Betrieb](../user-guide/operation.md#status-leds) zeigt eine vereinfachte Fassung.

| Controller-Zustand | LED-Muster |
|:-------------------|:-----------|
| PowerOff (keine nutzbare Eingangsspannung; der Controller läuft auf Restladung) | LED 5 dauerhaft rot |
| OffCharging | Roter Balken füllt sich, während die Superkondensatoren laden |
| SystemStartup | Regenbogenlauf, dann ein Durchlauf einfarbiger Farben |
| OperationalSolo | Gelber Ladezustandsbalken |
| OperationalCoOp | Grüner Ladezustandsbalken |
| BlackoutSolo | Oranger Ladezustandsbalken |
| BlackoutCoOp | Dunkelgrüner Ladezustandsbalken |
| BlackoutShutdown, ManualShutdown | Violetter Ladezustandsbalken |
| PoweredDownBlackout, PoweredDownManual | Alle aus |
| HostUnresponsive (Watchdog-Zeitüberschreitung) | Alle dauerhaft rot |
| EnteringStandby | Alle dauerhaft blau |
| Standby | Alle gedimmt rot |
| Überspannungsalarm der Superkondensatoren | Alle LEDs blinken rot |

Bei den Ladezustandsbalken steht jede leuchtende LED für ein Volt Superkondensator-Spannung:

| LED | Spannungsbereich |
|:----|:-----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Konfigurationsparameter

Die Konfiguration liegt im Flash-Speicher des Controllers und übersteht das Trennen der Versorgung. Lesen und ändern Sie sie mit `halpi config` — siehe das [Software-Handbuch](../user-guide/software.md#verwaltung-der-konfiguration).

| Parameter | Standardwert | Beschreibung |
|:----------|:-------------|:-------------|
| `auto_restart` | `false` bei aktuellen Geräten (beim Produktionstest gesetzt); Rückfallwert der Firmware `true` | Automatischer Neustart 5 s nach einem Herunterfahren per Software bei anliegender Eingangsspannung |
| `watchdog_timeout` | 10 s | Watchdog-Zeitlimit im Co-op-Modus |
| `power_on_threshold` | 8,0 V | Superkondensator-Spannung, die vor dem Einschalten des Compute Module erreicht sein muss |
| `solo_power_off_threshold` | 5,5 V | Superkondensator-Spannung, bei der der Controller im Solo-Modus das Abschalten erzwingt |
| `solo_depleting_timeout` | 5 s | Ausfallzeitgeber des Solo-Modus |
| `led_brightness` | 48 | Helligkeit der LEDs an der Frontplatte (0–255) |

Der Ausfallzeitgeber des Co-op-Modus und der Abschaltbefehl sind Einstellungen des Daemons und werden in `/etc/halpid/halpid.conf` konfiguriert (`blackout-time-limit`, standardmäßig 5 s; `poweroff`, standardmäßig `/sbin/poweroff`).

!!! quote "Weiterführende Informationen"
    - **Alltäglicher Gebrauch:** siehe [Täglicher Betrieb](../user-guide/operation.md)
    - **Einzelheiten zur Stromversorgung:** siehe [Stromversorgung im Detail](./power-supply.md)
    - **Firmware-Aktualisierungen:** siehe [Software-Handbuch](../user-guide/software.md#firmware-aktualisierungen)
    - **Firmware-Quelltext und I2C-Protokoll:** siehe das [HALPI2-firmware-Repository](https://github.com/hatlabs/HALPI2-firmware)

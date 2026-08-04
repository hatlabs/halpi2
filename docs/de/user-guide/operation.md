---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Systembetrieb

## Status-LEDs

Der HALPI2 verfügt über fünf RGB-LEDs, die den Zustand des Systems und der Stromversorgung sichtbar machen.

### LED-Kurzübersicht

| LED-Muster | Farbe | Bedeutung |
|------------|-------|-----------|
| LED 5 dauerhaft | Rot | Eingeschaltet, wartet auf Ladung |
| Fortschreitendes Füllen | Rot | Superkondensatoren laden |
| Regenbogen mit Farbwechsel | Mehrfarbig | Das CM5 ist nicht gestartet |
| Spannungsbalken | Gelb | Betrieb im Solo-Modus |
| Spannungsbalken | Grün | Betrieb im Co-op-Modus |
| Spannungsbalken | Orange | Pufferbetrieb aktiv (Solo) |
| Spannungsbalken | Dunkelgrün | Pufferbetrieb aktiv (Co-op) |
| Alle blinkend | Rot | Überspannung der Superkondensatoren |
| Alle dauerhaft | Rot | Watchdog-Zeitüberschreitung |
| Spannungsbalken | Violett | Herunterfahren läuft |
| Alle dauerhaft | Blau | Wechsel in den Standby läuft |
| Alle dauerhaft | Gedimmtes Rot | Standby |
| Alle aus | — | System ausgeschaltet |

### Spannungsanzeige der Superkondensatoren

Im Betrieb dienen die LEDs als Spannungsanzeige und zeigen den Ladezustand der Superkondensatoren:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Energieverwaltung und Herunterfahren

Der HALPI2 besitzt eine Stromversorgung, die Spannungsspitzen, Störimpulse und kurze Ausfälle verkraftet.

### Überblick über die Stromversorgung

Die Energieverwaltung des HALPI2 besteht aus:

- **Einer Stromversorgung mit weitem Bereich** (Eingang 11–32 V DC, Schutz bis 100 V DC)
- **Einer Pufferung durch Superkondensatoren** für geordnetes Herunterfahren bei Spannungsausfall
- **Einer Strombegrenzung** (0,9 A oder 2,5 A wählbar)
- **Der Erkennung von Spannungsausfällen** und dem automatischen Auslösen des Herunterfahrens
- **Der Überwachung von Eingangsspannung und -strom**

Das System arbeitet in zwei Betriebsarten: dem Solo-Modus und dem Co-op-Modus.

### Solo-Modus

Der Solo-Modus bietet einen einfachen autonomen Betrieb, wenn der HALPI-Daemon nicht läuft. Der Controller arbeitet eigenständig, ohne Kommunikation mit der Software.

#### Merkmale des Solo-Modus

- **Keine Kommunikation mit der Software erforderlich**
- **Grundlegender Schutz vor Spannungsausfall** — überwacht die Eingangsspannung und reagiert auf Ausfälle
- **Automatisches Herunterfahren über simulierte Betätigungen der Ein-/Aus-Taste**
- **Eingeschränkte Überwachungs- und Konfigurationsmöglichkeiten**

#### Spannungsausfall und Herunterfahren im Solo-Modus

**Erkennung des Spannungsausfalls:**
Der Controller überwacht die Eingangsspannung und erkennt Ausfälle. Ein Ausfallzeitgeber (standardmäßig 5 Sekunden) verhindert ein Herunterfahren bei kurzen Unterbrechungen.

**Ablauf des automatischen Herunterfahrens:**

1. **Der Controller erkennt den Spannungsausfall**
2. **Der Ausfallzeitgeber startet**, um Störimpulse von einem echten Ausfall zu unterscheiden
3. **Simulierte Tastenbetätigungen** — der Controller sendet einen Doppeldruck an das Compute Module
4. **Das Betriebssystem reagiert** und beginnt das geordnete Herunterfahren
5. **Die Superkondensatoren halten die Versorgung aufrecht** (in der Regel 30 bis 60 Sekunden)
6. **Schutz durch 60-Sekunden-Zeitüberschreitung** — erzwungenes Abschalten, falls das geordnete Herunterfahren scheitert
7. **Das System bleibt ausgeschaltet**, bis die Spannung zurückkehrt
8. **Automatischer Neustart**, sobald die Spannung wieder anliegt

**Manuelles Herunterfahren im Solo-Modus:**

- Das Betriebssystem fährt normal herunter
- Das System startet nach 5 Sekunden automatisch neu, wenn die Eingangsspannung weiterhin anliegt
- Für ein dauerhaftes Abschalten trennen Sie die Eingangsspannung, nachdem Sie das geordnete Herunterfahren ausgelöst haben

#### Wann der Solo-Modus aktiv ist

Der Solo-Modus gilt:

- ganz zu Beginn des Starts, bevor der HALPI-Daemon läuft;
- wenn der HALPI-Daemon nicht startet oder deaktiviert ist;
- auf nicht unterstützten Betriebssystemen ohne den Daemon;
- wenn der Daemon abgestürzt ist oder nicht mehr reagiert.

!!! tip "Zuverlässigkeit des Solo-Modus"
    Der Solo-Modus bietet einen unverzichtbaren Schutz, ist aber weniger zuverlässig als der Co-op-Modus. Der Controller fordert das Herunterfahren über simulierte Tastenbetätigungen an, was bei einem eingefrorenen System möglicherweise nicht wirkt.

### Co-op-Modus

Der Co-op-Modus bietet die vollständige Energieverwaltung, wenn der HALPI-Daemon läuft und mit dem Controller kommuniziert.

#### Funktionen des Co-op-Modus

- **Direkte Kommunikation mit der Software** — Datenaustausch zwischen Controller und Daemon in Echtzeit
- **Schutz durch Watchdog** — eine Zeitüberschreitung von 30 Sekunden sichert die Systemstabilität
- **Konfigurierbares Verhalten beim Herunterfahren** — Zeiten und Befehle anpassbar
- **Überwachung in Echtzeit** — umfassende Erfassung der Versorgungsparameter
- **Erweiterte Konfigurationsmöglichkeiten**

#### Spannungsausfall und Herunterfahren im Co-op-Modus

**Erkennung des Spannungsausfalls:**
Der Controller überwacht die Eingangsspannung und meldet Ereignisse direkt an den HALPI-Daemon. Der konfigurierbare Ausfallzeitgeber (standardmäßig 5 Sekunden) lässt kurze Unterbrechungen zu, ohne das Herunterfahren auszulösen.

**Ablauf des automatischen Herunterfahrens:**

1. **Der Controller erkennt den Spannungsausfall** und meldet ihn dem HALPI-Daemon
2. **Auswertung des Ausfallzeitgebers** — der Daemon prüft, ob der Ausfall den Schwellwert überschreitet
3. **Ausführung des Abschaltbefehls** — der Daemon führt den konfigurierten Befehl aus (standardmäßig `/sbin/poweroff`)
4. **Geordnetes Herunterfahren des Betriebssystems** — Anwendungen werden geschlossen und Dateisysteme sicher ausgehängt
5. **Die Pufferung durch Superkondensatoren** liefert während des gesamten Vorgangs Energie
6. **Der Controller verfolgt den Abschluss** — er erkennt, wann das Compute Module abschaltet
7. **Die 5-V-Schiene wird abgeschaltet**, sobald das Herunterfahren beendet ist
8. **Das System bleibt ausgeschaltet**, bis die Eingangsspannung zurückkehrt
9. **Steuerung des Neustarts** — je nach Konfiguration startet das System automatisch neu oder bleibt aus

**Manuelles Herunterfahren im Co-op-Modus:**

- Ein aus der Software ausgelöstes Herunterfahren verläuft geordnet
- Das System startet nach 5 Sekunden automatisch neu, wenn die Eingangsspannung weiterhin anliegt
- Um den automatischen Neustart zu verhindern, trennen Sie die Spannung oder setzen Sie `auto_restart` auf `false`

#### Schutz durch Watchdog

Der Co-op-Modus enthält einen Watchdog:

- **Kommunikations-Zeitüberschreitung von 30 Sekunden** — der Daemon muss sich regelmäßig beim Controller melden
- **Automatische Wiederherstellung** — das System startet neu, wenn die Kommunikation abreißt
- **Schutz vor Softwarefehlern** — sichert die Wiederherstellung nach einem Absturz des Daemons oder einem Systemstillstand
- **„Füttern des Watchdogs“** — der Daemon sendet regelmäßig Statusmeldungen, die den Zeitgeber zurücksetzen

#### Wann der Co-op-Modus aktiv ist

Der Co-op-Modus gilt, wenn:

- der HALPI-Daemon läuft und einwandfrei arbeitet;
- die Verbindung zwischen Daemon und Controller besteht;
- das System ein unterstütztes Betriebssystem verwendet;
- alle Überwachungs- und Steuerungsfunktionen zur Verfügung stehen.

!!! info "Co-op-Modus prüfen"
    Status des Daemons: `systemctl status halpid`

    Zustand des Controllers: `halpi status`

    Weitere Angaben zum Befehl `halpi` finden Sie im [Software-Handbuch](./software.md#halpi-daemon-halpid).

### Pufferung und Kondensatorsystem

Beide Betriebsarten stützen sich auf die Superkondensatoren, um ein geordnetes Herunterfahren zu sichern:

**Dauer der Pufferung:**

- Die Superkondensatoren liefern 30 bis 60 Sekunden Pufferzeit
- Die Dauer hängt von der Systemlast und den angeschlossenen Peripheriegeräten ab
- Sie genügt, um das Dateisystem sicher zu schließen und Prozesse zu beenden
- Sie ist nicht dafür ausgelegt, den Betrieb bei längeren Ausfällen fortzusetzen

**Ladeverhalten:**

- Ladezeit: 25 Sekunden bei einer Strombegrenzung von 0,9 A
- Ladezeit: 9 Sekunden bei einer Strombegrenzung von 2,5 A
- Der Ladefortschritt ist am Füllen der LEDs zu erkennen (rotes Füllmuster)

!!! warning "Grenzen des Ausfallschutzes"
    Das System aus Superkondensatoren ist für ein geordnetes Herunterfahren ausgelegt, nicht für den Weiterbetrieb. Verlassen Sie sich bei längeren Stromausfällen nicht darauf.

### Hinweise zum manuellen Herunterfahren

Der HALPI2 ist auf automatischen Betrieb und automatische Wiederherstellung ausgelegt, was sich auf das Verhalten beim manuellen Herunterfahren auswirkt.

#### Automatischer Neustart

Standardmäßig startet der HALPI2 nach einem manuellen Herunterfahren neu, solange die Eingangsspannung anliegt:

- Ein manuelles Herunterfahren beendet das Betriebssystem normal
- Nach dem Abschluss folgt eine Wartezeit von 5 Sekunden
- Das System startet automatisch neu, um verfügbar zu bleiben
- So ist die Wiederherstellung nach einem versehentlichen Abschalten gesichert

#### So schalten Sie das Gerät dauerhaft ab

Dafür gibt es zwei Wege:

**Spannung trennen:**

1. Lösen Sie aus der Software ein geordnetes Herunterfahren aus
2. Warten Sie, bis der Vorgang abgeschlossen ist (die LEDs erlöschen)
3. Trennen Sie die Eingangsspannung, um den automatischen Neustart zu verhindern

**Konfiguration ändern:**

1. Deaktivieren Sie den automatischen Neustart: `halpi config set auto_restart false`
2. Lösen Sie das Herunterfahren aus der Software aus
3. Das System bleibt nach dem Abschluss ausgeschaltet

**Standby-Modus (geplant):**

!!! info "Stand der Funktion"
    Der Standby-Modus ist für künftige Firmware-Versionen vorgesehen. Er wird es erlauben, das Compute Module abzuschalten, während der Controller des HALPI2 aktiv bleibt und auf Weckereignisse wartet.

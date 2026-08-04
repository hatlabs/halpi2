# Schnittstellen und Konnektivität

## CAN FD / NMEA 2000

Der HALPI2 besitzt eine vollständig galvanisch getrennte [CAN-FD](https://en.wikipedia.org/wiki/CAN_FD)-Schnittstelle, die sowohl [NMEA-2000](https://en.wikipedia.org/wiki/NMEA_2000)-Netzwerke auf Schiffen als auch Anwendungen in Fahrzeugen und Industrie unterstützt. Sie bietet eine schnelle Datenübertragung mit vollständiger elektrischer Trennung und damit hoher Störfestigkeit.

### Spezifikationen der Schnittstelle

Die CAN-FD-Schnittstelle unterstützt sowohl das klassische CAN- als auch das CAN-FD-Protokoll. Im NMEA-2000-Einsatz arbeitet sie im gewöhnlichen CAN-Modus mit der genormten Datenrate von 250 kbit/s. In Fahrzeug- und Industrieanwendungen kann sie die vollen CAN-FD-Fähigkeiten mit Datenraten bis 8 Mbit/s nutzen.

An der Frontplatte sitzt ein Micro-C-Anschluss, der mit üblicher NMEA-2000-Verkabelung und den zugehörigen Bauteilen kompatibel ist. So lässt sich das Gerät mit handelsüblichen T-Stücken und Stichleitungen direkt in bestehende Bordnetzwerke einbinden.

### Stromversorgung und Netzwerklast

Wie stark der HALPI2 das NMEA-2000-Netzwerk belastet, hängt von der gewählten Stromversorgung ab. In der Standardkonfiguration mit externer Versorgung über den E7T-Anschluss entnimmt das Gerät dem NMEA-2000-Netzwerk keine Leistung; seine Lastkennzahl (LEN) beträgt daher 0.

Bei Versorgung über den NMEA-2000-Bus muss die Stromaufnahme durch die interne Strombegrenzung auf 0,9 A begrenzt werden. Das entspricht einem LEN-Wert von 18. Schließen Sie das Gerät in diesem Fall nahe an der Einspeisung an den Backbone an, um den Spannungsabfall gering zu halten und einen zuverlässigen Betrieb zu sichern.

### Konfiguration der Hardware

Die Trägerplatine enthält einen Abschlusswiderstand von 120 Ω, der sich über einen Jumper zuschalten lässt. In NMEA-2000-Anwendungen sollte am Gerät kein Abschluss gesetzt werden, da die Norm dies nicht zulässt. In Fahrzeug- und Industrieanwendungen mit Punkt-zu-Punkt-Verbindung kann der Jumper dagegen gesetzt werden.

Für Diagnose und Fehlersuche besitzt die Trägerplatine eigene RX- und TX-LEDs, die den Netzwerkverkehr anzeigen. Sie geben unmittelbare Rückmeldung über Senden und Empfangen und erleichtern so das Eingrenzen von Verbindungsproblemen.

### Einbindung ins Netzwerk

Die Verbindung mit einem NMEA-2000-Netzwerk erfolgt über ein handelsübliches T-Stück (nicht im Lieferumfang) am Backbone sowie eine Stichleitung vom T-Stück zum Micro-C-Anschluss des HALPI2.

### Softwareintegration

Die CAN-Schnittstelle fügt sich über das SocketCAN-Framework nahtlos in Linux ein und erscheint als Netzwerkgerät `can0`. Dank dieser Standardschnittstelle lassen sich die üblichen CAN-Werkzeuge von Linux für Überwachung und Diagnose nutzen. Die Netzwerkschnittstelle ist in allen Systemabbildern des HALPI2 vorkonfiguriert (HaLOS, OpenPlotter und Raspberry Pi OS).

Die Anbindung an den Signal-K-Server steht in den HaLOS-Marine-Abbildern und in OpenPlotter zur Verfügung: Sie erkennen die CAN-Schnittstelle automatisch und nutzen sie zur Verarbeitung der NMEA-2000-Daten. In den nicht maritimen HaLOS-Abbildern lässt sich Signal K über den Container-Apps-Store in Cockpit installieren. Der Signal-K-Server dekodiert die PGNs und stellt die Netzwerkdaten in Echtzeit über eine Weboberfläche bereit.

### Fehlersuche

Die Fehlersuche im Netzwerk beginnt bei den RX/TX-LEDs auf der Trägerplatine. Im Normalbetrieb blinken sie im Takt des Netzwerkverkehrs. Fehlende RX-Aktivität kann auf Verkabelungsprobleme oder einen falschen Abschluss hindeuten, fehlende TX-Aktivität auf Konflikte im Netzwerk oder die Verkabelung.

Mit dem Linux-Befehl `candump` lässt sich der CAN-Bus direkt auf der Kommandozeile beobachten. Das Werkzeug zeigt alle Nachrichten auf dem Bus im Detail und erlaubt eine gründliche Diagnose. In der einfachsten Form:

```bash
candump can0
```

Damit werden alle eingehenden CAN-Rohnachrichten in Echtzeit angezeigt.

Das Dashboard des Signal-K-Servers bietet weitere Überwachungsmöglichkeiten. Es zeigt die NMEA-2000-Datenraten der CAN-Schnittstelle in Echtzeit, und mit dem Datenbrowser lassen sich die dekodierten NMEA-2000-Daten einsehen.

!!! quote "Weiterführende Informationen"
    - **Konfiguration der Stromversorgung:** siehe [Erste Schritte](../getting-started/getting-started.md#permanent-power-installation)
    - **Softwareeinrichtung:** siehe [Software-Handbuch](./software.md)
    - **Fehlersuche im Netzwerk:** siehe [Fehlersuche](./troubleshooting.md)


## RS-485 (NMEA 0183)

Der HALPI2 besitzt eine galvanisch getrennte [RS-485](https://en.wikipedia.org/wiki/RS-485)-Schnittstelle für die serielle Kommunikation mit [NMEA-0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422]-Netzwerken auf Schiffen und in Industrieanwendungen.

[^rs422]: Streng genommen verwendet NMEA 0183 die Norm RS-422, doch RS-485 ist abwärtskompatibel, sodass der HALPI2 mit RS-422- wie mit RS-485-Geräten kommunizieren kann.

### Spezifikationen der Schnittstelle

Der RS-485-Transceiver arbeitet mit bis zu 10 Mbit/s, typische NMEA-0183-Anwendungen nutzen jedoch die üblichen Baudraten von 4800 oder 38400 bit/s. Die Schnittstelle ist galvanisch getrennt und entspricht der NMEA-0183-Spezifikation; sie schützt den HALPI2 vor Masseschleifen und den elektrischen Störungen, die im maritimen Umfeld häufig auftreten.

Sie ist intern mit UART 4 des Raspberry Pi verbunden und erscheint unter Linux als `/dev/ttyAMA4`. Auf dieses gewöhnliche serielle Gerät kann jede Anwendung zugreifen, die serielle Kommunikation unterstützt, darunter der Signal-K-Server, OpenCPN und eigene Programme.

### Konfiguration der Hardware

Die Trägerplatine besitzt eigene RX- und TX-LEDs, die den Datenverkehr der RS-485-Schnittstelle anzeigen. Sie geben während Installation und Fehlersuche unmittelbare Rückmeldung und machen leicht überprüfbar, ob Daten korrekt gesendet und empfangen werden.

Als allgemeine RS-485-Schnittstelle lässt sich das Gerät auf automatische oder manuelle Sendefreigabe einstellen. Im manuellen Modus steuert ein GPIO-Pin das Freigabesignal, sodass die Software bestimmt, wann die Schnittstelle sendet und wann sie empfängt. Das ist bei Anwendungen mit mehreren Sendern erforderlich, bei denen die Schnittstelle im Ruhezustand rezessiv bleiben muss. Im Automatikmodus aktiviert die Hardware das Freigabesignal beim Senden selbst, was Aufbauten mit einem einzelnen Sender vereinfacht.

Darüber hinaus unterstützt die RS-485-Schnittstelle den Halbduplex-Betrieb, sodass sie über dasselbe Aderpaar senden und empfangen kann.

Die Schnittstelle lässt sich auch vollständig per Hardwarekonfiguration abschalten, wenn UART 4 für andere Zwecke benötigt wird.

### Verkabelung und Anschluss

Die RS-485-Schnittstelle benötigt eine Kabelverschraubung oder einen Frontplattenstecker, den der Anwender selbst beschafft. Eine gute Wahl ist [ein SP13-Frontplattenstecker mit Anschlusslitze](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). Die Schnittstelle ist abwärtskompatibel zur RS-422-Signalisierung des NMEA 0183 und unterstützt sowohl RS-485-Netzwerke mit mehreren Sendern als auch RS-422-Netzwerke mit einem Sender und mehreren Empfängern. Sie verwendet symmetrische Differenzpaare mit der Bezeichnung TX+/TX- und RX+/RX-.

### Softwareintegration

In allen HALPI2-Abbildern ist die RS-485-Schnittstelle einsatzbereit vorkonfiguriert. In den HaLOS-Marine-Abbildern und in OpenPlotter erkennt der Signal-K-Server die Schnittstelle automatisch und empfängt die übertragenen NMEA-0183-Daten.

Für eigene Anwendungen verhält sich die Schnittstelle wie eine gewöhnliche serielle Schnittstelle unter Linux. Anwendungen können `/dev/ttyAMA4` öffnen und Baudrate, Datenbits, Stoppbits und Parität nach den Anforderungen des angeschlossenen Geräts einstellen. Programme in Python, Node.js und C/C++ greifen mit den üblichen Bibliotheken für serielle Kommunikation darauf zu.

### Typische Anwendungen

Auf Schiffen wird an die RS-485-Schnittstelle typischerweise ein GPS-Empfänger, ein Echolot, ein Windmessgerät, ein AIS-Transponder oder ein anderes Gerät mit NMEA-0183-Protokoll angeschlossen. In der Industrie können speicherprogrammierbare Steuerungen, Sensoren und andere Automatisierungsgeräte angebunden werden, die Modbus RTU oder andere RS-485-Protokolle verwenden.

Die hohe Übertragungsrate erlaubt auch untypische Anwendungen wie die schnelle Erfassung von Sensordaten oder eigene Übertragungsprotokolle, wodurch sich der HALPI2 für Forschungsschiffe und spezialisierte Überwachungsaufgaben eignet.

!!! quote "Weiterführende Informationen"
    - **Softwarekonfiguration:** siehe [Software-Handbuch](./software.md)
    - **Fehlersuche:** siehe [Fehlersuche](./troubleshooting.md)


## GNSS (GPS)

Der HALPI2 unterstützt GNSS-Empfänger-HATs an UART0 (`/dev/ttyAMA0`). Jeder GNSS-Empfänger an diesem Anschluss arbeitet ohne weitere Einrichtung mit gpsd zusammen.

Für u-blox-Empfänger (etwa den Max-M8Q) bringen die HaLOS-Marine-Abbilder zusätzlich eine automatische, auf den maritimen Einsatz abgestimmte Konfiguration mit.

### Automatische Konfiguration (u-blox-Empfänger)

In den HaLOS-Marine-Abbildern erkennt und konfiguriert ein systemd-Dienst (`configure-ublox-marine`) u-blox-Empfänger bei jedem Start automatisch:

| Parameter | Wert |
|:----------|:-----|
| Baudrate | 115200 bit/s (Werkseinstellung: 9600) |
| Aktualisierungsrate | 10 Hz (100 ms) |
| Dynamisches Modell | Sea (auf den maritimen Einsatz abgestimmt) |

Die Konfiguration läuft bei jedem Start, weil u-blox-Module mit ROM (etwa das MAX-M8Q) keinen Flash-Speicher besitzen. Die Einstellungen liegen im batteriegepufferten RAM (BBR), das verloren gehen kann, wenn die Pufferspannung unterbrochen wird — etwa wenn das Gerät längere Zeit ohne Strom ist. Die erneute Konfiguration läuft unbemerkt ab und verlängert den Start von gpsd um etwa 2 Sekunden.

Wird kein Empfänger erkannt, beendet sich der Dienst stillschweigend. Ein neu eingebauter GNSS-HAT wird beim nächsten Neustart automatisch konfiguriert.

### Zugriff auf die Daten

Die GPS-Daten stellt [gpsd](https://gpsd.io/) auf TCP-Port 2947 bereit. In den HaLOS-Marine-Abbildern verbindet sich Signal K automatisch mit gpsd — eine weitere Konfiguration ist nicht nötig.

Für die Diagnose stehen die üblichen Kommandozeilenwerkzeuge von gpsd bereit:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Abbilder außer HaLOS

Unter Raspberry Pi OS oder anderen Betriebssystemen installieren und konfigurieren Sie gpsd von Hand:

```bash
sudo apt install gpsd gpsd-clients
```

Setzen Sie in `/etc/default/gpsd` den Eintrag `DEVICES="/dev/ttyAMA0"` und starten Sie den Dienst neu. Der Empfänger arbeitet mit seinen Werkseinstellungen (9600 bit/s, 1 Hz), solange er nicht mit `ubxtool` aus dem Paket `gpsd-clients` konfiguriert wurde.

!!! quote "Weiterführende Informationen"
    - **gpsd unter HaLOS:** siehe [GPS-Dokumentation von HaLOS](https://docs.halos.fi/user-guide/gps/)
    - **Softwareeinrichtung:** siehe [Software-Handbuch](./software.md)


## Ethernet

Der HALPI2 besitzt eine Gigabit-Ethernet-Schnittstelle für eine schnelle Netzwerkanbindung zur Datenübertragung, für den Fernzugriff und zur Einbindung in Bordnetzwerke. Der Ethernet-Anschluss auf der Trägerplatine ist eine gewöhnliche RJ45-Buchse. Sie ist auf einen Frontplattenanschluss herausgeführt, an den ein externes Ethernet-Kabel angeschlossen wird.

## USB

Der HALPI2 besitzt insgesamt vier USB-3.0-Anschlüsse vom Typ A für die schnelle Anbindung unterschiedlichster Peripheriegeräte. Ein Anschluss führt direkt zur USB-3.0-Schnittstelle des CM5, die drei übrigen laufen über einen USB-3-Hub auf der Platine. In der Standardkonfiguration sind zwei Anschlüsse auf die Frontplatte herausgeführt, zwei stehen auf der Trägerplatine für interne Verbindungen bereit.

## HDMI

Der HALPI2 besitzt zwei HDMI-2.0-Anschlüsse (HDMI0 und HDMI1) für die Videoausgabe. Auf der Trägerplatine sind beide als FFC-Anschlüsse (flexibles Flachkabel) ausgeführt und über eigens gefertigte FFC-Kabel auf die Frontplatte geführt. Die Anschlüsse an der Frontplatte sind gewöhnliche HDMI-Buchsen vom Typ A.

Die HDMI-Ausgabe des HALPI2 unterstützt zuverlässig zwei Full-HD-Videoströme (1080p). Eine 4K-Ausgabe kann funktionieren, wird aber nicht zugesichert.

## MIPI (CSI/DSI)

Die Trägerplatine besitzt zwei MIPI-CSI/DSI-Anschlüsse für Kameras und Displays. Es handelt sich um 22-polige FFC-Anschlüsse (flexibles Flachkabel) im Raster 0,5 mm. Mit neueren Raspberry-Pi-kompatiblen Kameras und Displays sollten sie ohne Anpassung funktionieren.

Aus Gründen der Dichtigkeit sollten FFC-Kabel ausschließlich für interne Verbindungen verwendet werden.

## Externe Taster

Die Trägerplatine des HALPI2 besitzt eine 2×3-polige Stiftleiste für den Anschluss externer Taster. Das Gehäuse enthält keine eingebauten Taster, sodass Anwender Platzierung und Bauform frei wählen können.

### Belegung des Tasteranschlusses

Die Trägerplatine besitzt eine 6-polige Stiftleiste mit drei beschrifteten Tasterfunktionen:

| Beschriftung | Funktion | Beschreibung |
|:-------------|:---------|:-------------|
| Reset | Reset des Controllers | Hardware-Reset (RUN-Pin des RP2040) |
| Power | Stromversorgung des Raspberry Pi | Ein-/Aus-Taste des CM5 (Eingang PWR_BUT) |
| User | Vom Benutzer konfigurierbar | Benutzerdefiniertes Ereignis (noch nicht umgesetzt) |

Jeder Taster belegt zwei Pins: einen für das Signal, einen für die Masse. Verwenden Sie Taster mit Schließerkontakt (NO), die den Signalpin beim Drücken mit Masse verbinden.

### Funktionen der Taster

**Reset-Taster:**
Der Reset-Taster löst einen Hardware-Reset aus, indem er den RUN-Pin des RP2040 auf Masse zieht. Das setzt das gesamte System zurück: Controller, CM5 und alle angeschlossenen Peripheriegeräte. Besonders nützlich ist er in Notfällen, wenn das Herunterfahren per Software fehlgeschlagen ist und das System nicht mehr reagiert.

**Power-Taster:**
Der Power-Taster ist direkt mit dem Eingang der Ein-/Aus-Taste des CM5 verbunden und verhält sich genau wie die Taste eines Raspberry Pi 5. Ein Doppelklick fordert ein geordnetes Herunterfahren an: Das Betriebssystem schließt die Anwendungen ordnungsgemäß und hängt die Dateisysteme aus, bevor abgeschaltet wird. Ein langer Druck erzwingt das sofortige Abschalten und sollte nur verwendet werden, wenn das System nicht mehr reagiert.

**User-Taster:**
Die Funktion des Benutzertasters wartet noch auf ihre Umsetzung in der Software und wird in künftigen Firmware-Versionen frei konfigurierbar sein. Danach ist der Taster für eigene Aktionen und anwendungsspezifische Auslöser vorgesehen, deren Verhalten der Anwender selbst festlegt.

### Einbau der Taster

#### Direkte Montage am Gehäuse

Für die direkte Montage am HALPI2-Gehäuse nutzen Sie die bereits vorhandenen Bohrungen mit 6 mm oder 13 mm. Entfernen Sie zunächst die entsprechenden Blindstopfen und setzen Sie einen wasserdichten Taster passend zum Bohrungsdurchmesser ein. Verbinden Sie ihn über ein geeignetes Kabel mit der Stiftleiste der Trägerplatine und achten Sie auf eine ordentliche Zugentlastung sowie eine wetterfeste Abdichtung an der Gehäusedurchführung.

#### Montage an einem abgesetzten Bedienfeld

Bei der Montage an einem abgesetzten Bedienfeld wählen Sie einen gut erreichbaren Ort, der die Wetterfestigkeit erhält. Verwenden Sie an den Kabeleinführungen Kabelverschraubungen und schließen Sie die Taster über ein Verlängerungskabel mit Leitern von 22 bis 26 AWG an; die Gesamtlänge sollte unter 3 Metern bleiben, um die Signalqualität zu erhalten. In feuchten oder rauen Umgebungen verwenden Sie an den Verbindungsstellen wasserdichte Stecker, um einen dauerhaft zuverlässigen Betrieb zu sichern.

#### Anschluss

Alle Tasteranschlüsse an der Trägerplatine sollten Buchsenleisten im Raster 2,54 mm verwenden. Achten Sie auf die richtige Ausrichtung der Pins und eine feste Verbindung, um Kontaktprobleme im Betrieb zu vermeiden.

!!! quote "Weiterführende Informationen"
    - **Energieverwaltung:** siehe [Energieverwaltung und Herunterfahren](./operation.md#power-management-and-shutdown-procedures)
    - **Zugang zur Hardware:** siehe [Hardware-Handbuch](./hardware.md)

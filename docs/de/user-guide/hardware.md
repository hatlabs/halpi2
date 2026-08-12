---
translated_from: 9b11eb34bb5624df50aa731a000eca6df6dcbc8a
---

# Hardware-Handbuch

## Zugang zum Gehäuse

Der HALPI2 steckt in einem pulverbeschichteten Gehäuse aus Aluminium-Druckguss mit vorgebohrten Öffnungen für die Frontplattenanschlüsse. Wenn Arbeiten im Inneren oder Wartungen anstehen, öffnen Sie es nach den folgenden Verfahren.

### Gehäuse öffnen

Stellen Sie zunächst sicher, dass das Gerät vollständig ausgeschaltet und von allen Stromkabeln getrennt ist. Der Deckel ist mit vier Senkkopfschrauben M4×10 mit PH2-Antrieb befestigt. Lösen Sie diese mit einem PH2-Schraubendreher und nehmen Sie den Deckel ab.

### Wieder zusammenbauen

Prüfen Sie vor dem Schließen des Gehäuses, ob alle internen Verbindungen fest sitzen. Führen Sie die Kabel sorgfältig, ohne sie zu quetschen oder scharf zu knicken.

Flexible Flachkabel (FFC) lassen sich leicht versehentlich verkehrt herum einstecken. Prüfen Sie die Richtung anhand der Contacts-Pfeile im Bestückungsdruck.

Achten Sie besonders auf die Deckeldichtung und prüfen Sie sie auf Beschädigungen, Verschmutzungen oder Verrutschen, die die Wetterfestigkeit beeinträchtigen könnten.

Setzen Sie die vier M4×10-Deckelschrauben mit dem PH2-Schraubendreher wieder ein. Nicht zu fest anziehen.


## Frontplattenanschlüsse

### Standardkonfiguration

Der HALPI2 wird mit einer Standardbestückung der Anschlüsse ausgeliefert, die für die meisten Anwendungen passt. Sie umfasst:

- **E7T-Stromanschluss**
- **NMEA-2000-Micro-Anschluss**
- **Gigabit-Ethernet RJ45**
- **HDMI-Ausgang**
- **2× USB 3.0 Type-A**
- **3× PG7-Kabelverschraubungspositionen** (mit Blindstopfen)
- **2× RP-SMA-Antennenpositionen** (mit Blindstopfen)
- **Druckausgleichsstopfen**

![Frontplattenanschlüsse und Blindstopfen](./front-panel-connectors-all.jpg)
*Frontplattenanschlüsse und Blindstopfen. Grün markierte Anschlüsse gehören zur Standardkonfiguration. Die gelben Positionen sind Blindstopfen, die sich bei Bedarf durch Anschlüsse ersetzen lassen. Die rote Position ist der Druckausgleichsstopfen, der nicht entfernt werden darf.*

### Andere Anschlussvarianten

Wenn Sie andere Anschlusstypen benötigen, lässt sich die Bestückung der Frontplatte ändern:

#### Anschlüsse ausbauen

!!! warning "Wichtig"
    Arbeiten Sie an den Anschlüssen nur, wenn das Gerät ausgeschaltet und von allen Quellen getrennt ist.

    Kunststoffgewinde können durch zu festes Anziehen beschädigt werden. Verwenden Sie handelsübliche Sechskantnüsse, ziehen Sie aber nur handfest an.

1. **Passende Nussgröße verwenden:**
    - Große Anschlüsse: Nuss 26 mm
    - M6-Nylonschrauben: Nuss 10 mm
    - RP-SMA-Anschlüsse: Nuss 8 mm
    - PG7-Positionen: großer Schlitzschraubendreher, Nuss 17 mm

2. **Vorsichtig ausbauen** — Kunststoffgewinde können durch zu festes Anziehen beschädigt werden

3. **Ausgebaute Teile aufbewahren** für eine spätere Verwendung

#### Neue Anschlüsse einbauen

1. **Nur seewasserfeste** oder für die Umgebung geeignete Anschlüsse verwenden
2. **Auf gute Abdichtung achten** — innen ist ein breiter Flansch erforderlich
3. **Nur handfest anziehen** — Kunststoffgewinde nicht überdrehen
4. **Probeweise einsetzen**, bevor Sie endgültig montieren

## Innerer Aufbau

- Die Trägerplatine des HALPI2 ist die Hauptplatine des Rechners: Sie nimmt auf ihrer Unterseite das Compute Module 5 (CM5) auf und stellt Energieverwaltung, Anzeigen und die Anschlüsse aller Schnittstellen bereit.

### Funktionsbereiche der Trägerplatine

Die wichtigsten Funktionsbereiche der Trägerplatine zeigt das folgende Bild.

![Aufbau der Trägerplatine, Oberseite](./carrier-board-top-layout.jpg)
*Aufbau der Oberseite der Trägerplatine mit den wichtigsten Funktionsbereichen.*

### Anschlüsse der Trägerplatine

Die Funktionen sind über eine Reihe von Anschlüssen auf der Platine zugänglich, die das folgende Bild zeigt.

![Anschlüsse der Trägerplatine, Oberseite](./carrier-board-top-conx.jpg)
*Anschlüsse der Trägerplatine, Oberseite.*

Nachstehend die Anschlüsse der Oberseite.

| Kennung | Beschreibung |
|:--------|:-------------|
| **a1** | Stromanschluss (Typ Phoenix MC, Raster 3,81 mm) |
| **a2** | Schalter für die Eingangsstrombegrenzung (0,9 A oder 2,5 A) |
| **a3** | Jumper zur Spannungssteuerung. Überbrücken Sie die Pins „3.3V off“, um die 3,3-V-Schiene zwangsweise abzuschalten. Überbrücken Sie die Pins „5V on“, um die 5-V-Schiene zwangsweise einzuschalten. **Hinweis:** Auf Platinen der Version 0.4.0 sind die Anschlüsse **a3** und **c2** anders angeordnet. |
| **b1** | Ethernet-Anschluss (RJ45) |
| **c1** | USB-Anschluss des Controllers. Dient dem Flashen der Firmware des Mikrocontrollers RP2040. |
| **c2** | Jumper-Stiftleiste MCU USB BOOT. Überbrücken Sie die Pins, um den RP2040 in den USB-Startmodus zu versetzen. |
| **c3** | Debug-Stiftleiste des Controllers |
| **c4** | Unbestückte GPIO-Stiftleiste des Controllers |
| **c5** | Tasterleisten. Für den Anschluss der Taster Power, Reset und User. |
| **c6** | Ein-/Aus-Taste. Zum Ein- und Ausschalten des Compute Module 5. |
| **d1** | 40-polige GPIO-Stiftleiste des Raspberry Pi |
| **e1** | MIPI0-Anschluss für Kamera oder Display |
| **e2** | MIPI1-Anschluss für Kamera oder Display |
| **f1** | HDMI0-Anschluss |
| **f2** | HDMI1-Anschluss |
| **g1** | M.2-Anschluss für NVMe-SSD |
| **h1** | CAN-FD-Schnittstelle (Typ Phoenix MC, Raster 3,81 mm) |
| **h2** | CAN-Abschluss-Jumper. Überbrücken Sie die Pins, um den Abschlusswiderstand des CAN-FD-Busses zuzuschalten. |
| **i1** | RS-485-Schnittstelle (Typ Phoenix MC, Raster 3,81 mm) |
| **i2** | Jumper für den Automatik-/Handbetrieb des RS-485. |
| **i4** | Jumper XRS-485 RX Enable. Überbrücken Sie die Pins, um den RS-485-Empfang zu aktivieren. |
| **j1** | USB-Boot-Anschluss des Compute Module. Dient dem Flashen der Firmware des Compute Module 5. |
| **j2** | Wahlschalter für den Startmodus des Compute Module. „Normal“ für den normalen Betrieb, „Abnormal“ für den USB-Startmodus. In Stellung „Abnormal“ leuchtet eine Warn-LED. |
| **m1** | USB3-Anschluss 0. Direkt mit dem CM5 verbunden. |
| **m2** | USB3-Anschluss 1-0. Mit dem USB3-Hub der Platine verbunden. |
| **m3** | USB3-Anschluss 1-1. Mit dem USB3-Hub der Platine verbunden. |
| **m4** | USB3-Anschluss 1-2. Mit dem USB3-Hub der Platine verbunden. |
| **n1** | CR2032-Batteriehalter für die Echtzeituhr (RTC) |
| **q1** | Lüfteranschluss des CM5. Der Lüfter kann die Luftzirkulation im Gehäuse verbessern. Beim Standardgehäuse wird er nicht benötigt. |

![Anschlüsse der Trägerplatine, Unterseite](./carrier-board-bottom-conx.jpg)
*Anschlüsse der Trägerplatine, Unterseite.*

Nachstehend die Anschlüsse der Unterseite.

| Kennung | Beschreibung |
|:--------|:-------------|
| **p1** | Anschluss des Compute Module 5. |
| **q1** | Lüfteranschluss des CM5, alternative Position. Hier lässt sich bei einem eigenen Gehäuse ein Prozessorlüfter über dem CM5-Modul anschließen. **Hinweis:** Die Anschlüsse **q1** und **q2** sind parallel geschaltet und dürfen nicht gleichzeitig verwendet werden. |

Der Anschluss für die WLAN- und Bluetooth-Antenne sitzt schließlich auf dem Compute Module 5 selbst. Das folgende Bild zeigt ihn.

![Anschluss der WLAN-Antenne](./cm5-top-conx.jpg)
*U.FL-Antennenanschluss auf dem Compute Module 5.*

| Kennung | Beschreibung |
|:--------|:-------------|
| **r1** | U.FL-Anschluss für die WLAN- und Bluetooth-Antenne. |

### Blinkenlights

Die Trägerplatine besitzt mehrere Status-LEDs zur Systemüberwachung.

![Status-LEDs der Trägerplatine](./carrier-board-top-leds.jpg)
*Status-LEDs der Trägerplatine und ihre Farben.*

Die Status-LEDs geben Auskunft über Stromversorgung und Aktivität des Systems. Nachstehend die Übersicht.

| Kennung | Farbe | Beschreibung |
|---------|:------|:-------------|
| **1** | RGB | Fünf RGB-LEDs. Sie zeigen Zustand und Aktivität des Systems an der Frontplatte an. |
| **2** | Rot | Betriebsanzeigen der 3,3-V- und 5-V-Schienen. Sie zeigen den Zustand der jeweiligen Spannungsschiene. |
| **3** | Gelb | Anzeige der Ethernet-Geschwindigkeit. Leuchtet, wenn der Ethernet-Anschluss eine Verbindung mit 100/1000 Mbit/s ausgehandelt hat. |
| **4** | Grün | Anzeige der Ethernet-Aktivität. Blinkt bei Netzwerkverkehr am Ethernet-Anschluss. |
| **5** | Blau | Anzeige der SSD-Aktivität. Blinkt bei Lese- und Schreibzugriffen auf die M.2-NVMe-SSD. |
| **6** | Rot | Anzeige des Pi-Betriebszustands. Leuchtet, wenn das System versorgt, aber heruntergefahren ist. |
| **7** | Grün | Anzeige der Pi-Aktivität. Blinkt bei Aktivität des Raspberry Pi. |
| **8** | Bernstein | Warnung „Abnormal Boot Mode“. Leuchtet, wenn der USB-Startmodus-Schalter auf „Abnormal“ steht. Das Gerät ist dann auf das Flashen über den USB-Boot-Anschluss eingestellt und startet nicht normal. |
| **9** | Grün | CAN-TX/RX-LEDs. Sie blinken beim Empfangen (RX) oder Senden (TX) von Daten auf der CAN-Schnittstelle. |
| **10** | Grün | RS-485-TX/RX-LEDs. Sie blinken beim Empfangen (RX) oder Senden (TX) von Daten auf der RS-485-Schnittstelle. |

Die Muster der RGB-LEDs sind unter [Täglicher Betrieb](./operation.md#status-leds) beschrieben.

## Einstellung der Strombegrenzung

Die Trägerplatine besitzt einen Schalter für die Strombegrenzung, mit dem der maximale Strom für die Peripherie festgelegt wird. Seine Lage finden Sie als Schalter **a2** im Bild des Abschnitts [Anschlüsse der Trägerplatine](#anschlusse-der-tragerplatine).

!!! info "Einstellungen der Strombegrenzung"
    **0,9 A (Standard):**

    - Zwingend bei Versorgung über den NMEA-2000-Bus
    - Für den Grundbetrieb ausreichend

    **2,5 A:**

    - Für Peripheriegeräte mit hohem Strombedarf
    - Schnelleres Laden der Superkondensatoren
    - Nur mit eigener Stromversorgung

Zum Ändern der Einstellung schalten Sie den HALPI2 vollständig aus und nehmen den Gehäusedeckel nach dem Verfahren im Abschnitt Zugang zum Gehäuse ab. Suchen Sie den Schalter für die Strombegrenzung auf der Trägerplatine und bringen Sie ihn in die gewünschte Stellung (0,9 A oder 2,5 A). Bauen Sie das Gehäuse anschließend wieder zusammen und achten Sie darauf, dass alle Verbindungen fest sitzen.

## HATs verwenden

### Kompatibilität von HATs

Der HALPI2 unterstützt über seine 40-polige GPIO-Stiftleiste die üblichen Raspberry-Pi-HATs und bleibt dabei elektrisch wie mechanisch vollständig kompatibel zur HAT-Spezifikation von Raspberry Pi. Die Trägerplatine bietet dieselbe GPIO-Belegung wie ein gewöhnlicher Raspberry Pi, sodass die meisten für Raspberry Pi 4 und 5 entwickelten HATs ohne Änderung funktionieren. Das gilt sowohl für offizielle Raspberry-Pi-HATs als auch für Erweiterungskarten von Drittanbietern, die dem HAT-Standard folgen.

### Räumliche Grenzen

Das Gehäuse des HALPI2 bietet 45 mm freie Höhe über der Trägerplatine, genug für bis zu zwei gestapelte HATs. Links neben dem eingezeichneten HAT-Bereich sitzen die Superkondensatoren, was den Platz für HATs einschränkt, die über die Standardabmessungen von 65 × 56 mm hinausgehen. Achten Sie besonders auf HATs mit seitlichen Anschlüssen: Anschlüsse nach „Süden“ oder „Osten“ sind in der Regel unproblematisch, nach „Westen“ gerichtete können mit den Superkondensatoren kollidieren.

### Konflikte bei GPIO-Pins

Mehrere GPIO-Pins werden von den integrierten Schnittstellen des HALPI2 belegt und müssen bei der Auswahl eines HAT berücksichtigt werden. Die folgende Tabelle führt die belegten Pins und ihre Funktionen auf:

| GPIO-Nummer | Funktion | Schnittstelle | Hinweise |
|-------------|----------|---------------|----------|
| GPIO 2 | I2C SDA | System-I2C | Teilbar; Adresse 0x6d reserviert |
| GPIO 3 | I2C SCL | System-I2C | Teilbar; Adresse 0x6d reserviert |
| GPIO 6 | SPI CS | CAN FD | Eigenes Chip-Select für den CAN-Controller |
| GPIO 9 | SPI MISO | CAN FD | Gemeinsamer SPI0-Bus |
| GPIO 10 | SPI MOSI | CAN FD | Gemeinsamer SPI0-Bus |
| GPIO 11 | SPI SCK | CAN FD | Gemeinsamer SPI0-Bus |
| GPIO 12 | UART TX | RS-485 | Senden von UART4 |
| GPIO 13 | UART RX | RS-485 | Empfangen von UART4 |
| GPIO 24 | RS-485 EN | RS-485 | Freigabesignal (nur im Handbetrieb) |
| GPIO 26 | CAN INT | CAN FD | Interruptleitung des CAN-Controllers |

### Gemeinsame Nutzung von Schnittstellen und Konflikte

Der I2C-Bus an GPIO 2 und 3 lässt sich mit HAT-Geräten teilen, da I2C mehrere Geräte an einem Bus zulässt. HATs dürfen jedoch nicht die I2C-Adresse 0x6d verwenden, die dem Systemcontroller des HALPI2 vorbehalten ist. Die meisten I2C-HATs arbeiten ohne Probleme, prüfen Sie aber vor dem Einbau die verwendeten Adressen.

Der SPI0-Bus der CAN-FD-Schnittstelle lässt sich unter Umständen mit anderen SPI-Geräten teilen, da der HALPI2 eigene Pins für Chip-Select (GPIO 6) und Interrupt (GPIO 26) verwendet. HATs, die SPI0 mit den Standard-Chip-Select-Pins (GPIO 7 oder GPIO 8) nutzen, können neben der CAN-Schnittstelle bestehen, benötigen aber möglicherweise eine zusätzliche Konfiguration per Device-Tree-Overlay.

### Integrierte Schnittstellen deaktivieren

Benötigt ein HAT Pins exklusiv, die von den integrierten Schnittstellen des HALPI2 belegt sind, lassen sich diese durch Änderungen an der Hardware abschalten. Die CAN-FD-Schnittstelle wird vollständig frei, wenn Sie den Lötjumper GPIO6-CAN.CS auf der Unterseite der Trägerplatine entfernen. Damit wird der CAN-Controller vom SPI-Bus getrennt und die Pins GPIO 6, 9, 10, 11 und 26 stehen dem HAT zur Verfügung.

Die RS-485-Schnittstelle lässt sich abschalten, indem Sie den Jumper RX Enable (i4) auf der Trägerplatine entfernen. Der RS-485-Empfänger empfängt dann keine Daten mehr und GPIO 12 und 13 werden frei. Wird keine manuelle Sendefreigabe benötigt, lässt sich auch GPIO 24 anderweitig nutzen, indem Sie den Jumper für Automatik-/Handbetrieb des RS-485 (i2) auf Automatik stellen.

### Einbau

Schalten Sie zu Beginn das System aus und trennen Sie alle Stromquellen. Nehmen Sie den Gehäusedeckel nach dem Verfahren im Abschnitt Zugang zum Gehäuse ab.

Trägerplatinen ab Version 0.5.0 besitzen an den vier HAT-Befestigungspunkten bereits Gewindeeinsätze M2.5, was den Einbau vereinfacht. Bei älteren Platinen der Version 0.4.0 müssen die M2.5-Muttern von Hand gesetzt werden; dafür ist die Trägerplatine vorübergehend auszubauen — ohne dass zwingend alle Kabel getrennt werden müssen.

Für viele gängige HATs eignen sich Abstandsbolzen von 15 mm; messen Sie jedoch die Höhe der Buchsenleiste des HAT, um den richtigen Abstand zu ermitteln. Der Sockel der Stiftleiste ist 2,5 mm hoch; addieren Sie diesen Wert zur Höhe der Buchsenleiste, um die nötige Länge des Abstandsbolzens zu bestimmen.

Schrauben Sie die Abstandsbolzen in die Befestigungslöcher oder sichern Sie sie bei Platinen der Version 0.4.0 von unten mit Muttern. Richten Sie den HAT an der 40-poligen GPIO-Stiftleiste aus, prüfen Sie die Lage aller Pins und drücken Sie den Anschluss dann gleichmäßig auf. Der HAT sollte parallel zur Trägerplatine sitzen, ohne sichtbaren Spalt am GPIO-Anschluss.

Befestigen Sie den HAT mit M2.5-Schrauben oder weiteren Abstandsbolzen durch seine Befestigungslöcher. Diese Schrauben gehören nicht zum Lieferumfang des HALPI2 und müssen separat beschafft werden. Ziehen Sie sie nur so weit an, dass der HAT sicher sitzt, ohne die Leiterplatte zu verbiegen.

### Kabelführung

Besitzt der HAT Anschlüsse, die von außen zugänglich sein müssen, sollten Sie passende Frontplattenanschlüsse in den freien PG7-Kabelverschraubungspositionen einbauen. So bleibt der Schutz des Gehäuses erhalten und die Anschlüsse sind dennoch bequem erreichbar.

### Ausbau

Der Ausbau eines HAT erfolgt in umgekehrter Reihenfolge. Schalten Sie das System vollständig aus und trennen Sie alle Stromquellen, bevor Sie das Gehäuse öffnen. Entfernen Sie die M2.5-Befestigungsschrauben und heben Sie den HAT gerade nach oben von der GPIO-Stiftleiste ab; vermeiden Sie seitliche Kräfte, die die Pins verbiegen könnten.

Sitzt der HAT fest, prüfen Sie zunächst, ob eine Schraube oder ein Kabel übersehen wurde, bevor Sie stärker ziehen. Manche HATs mit stramm sitzenden Anschlüssen lassen sich durch leichtes Wippen beim Ziehen lösen. Wippen Sie in Nord-Süd-Richtung; ein Wippen in Ost-West-Richtung kann die Pins verbiegen, sobald sich der Anschluss plötzlich löst.

### Softwarekonfiguration

Nach dem Einbau kann der HAT eine Softwarekonfiguration benötigen. Viele HATs bringen Device-Tree-Overlays mit, die in der Raspberry-Pi-Konfiguration aktiviert werden müssen. Ergänzen Sie in `/boot/firmware/config.txt` die in der Dokumentation Ihres HAT angegebenen `dtoverlay`-Zeilen.

!!! quote "Weiterführende Informationen"
    - **GPIO-Belegung:** siehe [Hardware-Referenz](../technical-reference/hardware.md)
    - **Softwarekonfiguration:** siehe [Software-Handbuch](./software.md)
    - **Änderungen am Gehäuse:** siehe [Andere Anschlussvarianten](#andere-anschlussvarianten)

## NVMe-SSD austauschen

### Kompatibilität von SSDs

Der HALPI2 unterstützt NVMe-SSDs im Format M.2 2230 bis 2280 in der üblichen einseitigen Bauform. Kürzere 2230-Laufwerke dürfen wegen des größeren Freiraums an dieser Position auch beidseitig bestückt sein; längere Laufwerke müssen einseitig sein, um auf die Trägerplatine zu passen.

Die Kompatibilität lässt sich nur für SSDs von Hat Labs und offizielle Raspberry-Pi-SSDs zusichern. Ziehen Sie ein Laufwerk eines Drittanbieters in Betracht, prüfen Sie vor dem Kauf anhand von Anwenderberichten und Kompatibilitätslisten, ob es mit dem Raspberry Pi 5 zusammenarbeitet. Typische Probleme bei inkompatiblen Laufwerken sind eine zu hohe Leistungsaufnahme, Überhitzung sowie Startfehler oder Systeminstabilität.

### Neue SSD vorbereiten

Vor dem Einbau einer neuen SSD in den HALPI2 sollte das Betriebssystem darauf geflasht werden. Zwar lässt sich die SSD auch nach dem Einbau über den USB-Boot-Anschluss des CM5 (j1) flashen, ein externer USB-NVMe-Adapter ist jedoch einfacher und schneller. Das Flash-Verfahren ist im [Software-Handbuch](./software.md) beschrieben.

### Die 3,3-V-Systemspannung abschalten

Die Superkondensatoren können die 3,3-V-Schiene der Trägerplatine nach dem Trennen der Hauptversorgung noch geraume Zeit unter Spannung halten. Da die SSD aus dieser Schiene versorgt wird, muss sie abgeschaltet werden, damit die SSD vor dem Aus- oder Einbau sicher spannungsfrei ist.

Schalten Sie zunächst den HALPI2 aus und trennen Sie die Stromversorgung. Öffnen Sie das Gehäuse nach dem Verfahren im Abschnitt Zugang zum Gehäuse.

Suchen Sie den Jumper „3.3V off“ auf der Trägerplatine. Seine Lage hängt von der Platinenversion ab. Auf Platinen der Version 0.4.0 sitzt er unmittelbar neben den Superkondensatoren, auf deren „Südseite“. Ab Version 0.5.0 finden Sie die Stiftleiste „Pow.Ctrl“ „östlich“ der Superkondensatoren; die Pins „3.3V off“ sind die beiden oberen.

Setzen Sie den Jumper so, dass die Pins „3.3V off“ überbrückt sind. Damit wird die 3,3-V-Schiene abgeschaltet, erkennbar am Erlöschen der LEDs.

### Ausbau

Der M.2-Steckplatz liegt an der „Südkante“ der Trägerplatine. Den mit **g1** gekennzeichneten M.2-Anschluss finden Sie im Bild des Abschnitts [Anschlüsse der Trägerplatine](#anschlusse-der-tragerplatine).

Entfernen Sie die M2.5-Befestigungsschraube mit einem PH1-Schraubendreher. Nach dem Lösen der Schraube stellt sich die SSD schräg auf. Heben Sie das Laufwerk am Befestigungsende vorsichtig an und ziehen Sie es mit leichten Bewegungen aus dem M.2-Anschluss. Fassen Sie die SSD an den Kanten an, um Bauteile und Anschlüsse nicht zu beschädigen.

### Einbau

Setzen Sie die vorbereitete SSD in einem Winkel von etwa 30 Grad in den M.2-Anschluss ein und achten Sie darauf, dass die Kerbe der SSD zur Codierung des Anschlusses passt. Das Laufwerk sollte ohne Kraftaufwand hineingleiten. Drücken Sie das Befestigungsende anschließend flach auf den Abstandsbolzen.

Sichern Sie die SSD mit der M2.5-Schraube und einem PH1-Schraubendreher. Ziehen Sie die Schraube nur so weit an, dass das Laufwerk fest sitzt. Die SSD muss völlig plan liegen, ohne sichtbare Biegung.

Sobald die SSD sitzt, entfernen Sie den Jumper von den Pins „3.3V off“, um die 3,3-V-Schiene wieder zu aktivieren. Bewahren Sie den Jumper für den späteren Gebrauch auf der Stiftleiste auf.

Bauen Sie das Gehäuse wie im Abschnitt Zugang zum Gehäuse beschrieben wieder zusammen. Für die Softwarekonfiguration und die Fehlersuche siehe das [Software-Handbuch](./software.md).

!!! quote "Weiterführende Informationen"
    - **Systemabbilder:** siehe [Software-Handbuch](./software.md)
    - **Startvorgänge:** siehe [Täglicher Betrieb](./operation.md#einschalten)
    - **Zugang zur Hardware:** siehe [Zugang zum Gehäuse](#zugang-zum-gehause)

## Compute Module 5 austauschen

### Voraussetzungen

Der Austausch des Compute Module 5 erfordert Sorgfalt, da die Platine-zu-Platine-Anschlüsse empfindlich sind. Das CM5 verwendet zwei hochpolige Anschlüsse, die bei zu großer Kraft oder falscher Technik leicht beschädigt werden. Bauen Sie ein vorhandenes Modul nur aus, wenn es unbedingt nötig ist, etwa weil es beschädigt ist oder ersetzt werden soll. Schäden an den Befestigungsanschlüssen des Compute Module — am CM5 wie an der Trägerplatine — fallen nicht unter die Garantie.

Halten Sie vor Beginn Wärmeleitpads für die Wärmeübertragung bereit. Die Standardbestückung verwendet ein 1 mm dickes Pad auf dem SoC und 2 mm dicke Pads auf dem RP1-Chip und den internen Bauteilen der Stromversorgung. Vorhandene Pads lassen sich wiederverwenden, sofern sie unbeschädigt und sauber sind.

### Zugang zum Compute Module

Schalten Sie den HALPI2 aus und trennen Sie die Stromquelle. Nehmen Sie den Gehäusedeckel nach dem Verfahren im Abschnitt Zugang zum Gehäuse ab. Da das CM5 auf der Unterseite der Trägerplatine sitzt, muss diese zuerst aus dem Gehäuse ausgebaut werden. An der Trägerplatine hängen zahlreiche Kabel; fotografieren Sie die Verbindungen vor dem Weiterarbeiten.

Trennen Sie alle Kabel, die das Anheben der Trägerplatine verhindern. Entfernen Sie deren Befestigungsschrauben und nehmen Sie die Platine aus dem Gehäuse.

### Vorhandenes Modul ausbauen

!!! danger "Achtung"
    Wird das CM5-Modul nacheinander an je einem Anschluss gelöst, können die Verwindungskräfte den Anschluss vom Modul abreißen. Dieser Schaden fällt nicht unter die Garantie.

Das CM5 ist über zwei Platine-zu-Platine-Anschlüsse befestigt, die vorsichtig behandelt werden müssen. Verwenden Sie dafür niemals Metallwerkzeuge — sie können die Anschlüsse oder benachbarte SMD-Bauteile beschädigen. Nutzen Sie ein Öffnungswerkzeug aus Holz oder Kunststoff, ein Gitarrenplektrum oder ein vergleichbares nicht leitendes Hilfsmittel.

Setzen Sie das Werkzeug mittig an der linken Schmalseite des CM5-Moduls an, zwischen Modul und Trägerplatine. Drücken Sie die Ecken der rechten Seite fest nach unten. Hebeln Sie mit möglichst geringer Kraft vorsichtig nach oben — das Modul sollte sich mit einem leichten Klicken lösen, wobei sich beide Anschlüsse gleichzeitig trennen.

![Ausbau des CM5-Moduls](./unmount-cm5.jpg)
*Bauen Sie das CM5-Modul aus, indem Sie die Ecken der rechten Kante nach unten drücken und gleichzeitig mittig an der linken Kante nach oben hebeln. Beide Anschlüsse sollten sich gleichzeitig lösen.*

### Neues Modul einbauen

Richten Sie das neue CM5-Modul an den Anschlüssen der Trägerplatine aus und nutzen Sie die Umrandung im Bestückungsdruck als Hilfe. Bei richtiger Ausrichtung deckt sich die aufgedruckte Umrandung genau mit den Abmessungen des CM5.

Drücken Sie das ausgerichtete Modul dann an den Anschlussstellen beider Schmalseiten sanft und gleichmäßig an. Sie spüren, wie die Anschlüsse mit einem leisen Klicken einrasten. Drücken Sie fest, vermeiden Sie aber ein Durchbiegen der Trägerplatine — stützen Sie sie nötigenfalls von unten. Beide Anschlüsse müssen vollständig sitzen, damit das Gerät einwandfrei arbeitet.

Bringen Sie anschließend die Wärmeleitpads auf dem CM5-Modul an: ein 1-mm-Pad auf dem Haupt-SoC, 2-mm-Pads auf dem RP1-Chip und den Bauteilen der Stromversorgung. Achten Sie bei wiederverwendeten Pads darauf, dass sie sauber und richtig platziert sind.

![Platzierung der Wärmeleitpads auf dem CM5](./cm5-thermal-pads-annotated.jpg)
*Platzierung der Wärmeleitpads auf dem Compute Module 5. Verwenden Sie ein 1 mm dickes Pad auf dem SoC (Mitte) und 2 mm dicke Pads auf dem RP1 und den Bauteilen der Stromversorgung. Form und Größe der Pads können abweichen.*

### Anschluss der Antenne

Verbinden Sie vor dem Wiedereinbau der Trägerplatine das U.FL-Antennenkabel mit dem Antennenanschluss des CM5. Nach dem Einbau der Platine ist dieser Anschluss nicht mehr erreichbar. Der U.FL-Anschluss verlangt eine genaue Ausrichtung und festen Druck; bei vollständigem Einrasten spüren Sie ein deutliches Klicken. Achten Sie darauf, die Hülse des Anschlusses beim Aufsetzen nicht zu verbiegen.

### Endmontage

Prüfen Sie den Einbau: Beide Anschlüsse müssen vollständig sitzen und das Modul muss ohne Spalt flach auf der Trägerplatine liegen. Die Wärmeleitpads müssen die wärmeerzeugenden Bauteile berühren.

Setzen Sie die Trägerplatine zurück ins Gehäuse und achten Sie darauf, dass die Wärmeleitpads des CM5 mit den entsprechenden Wärmeableitflächen im Gehäuseboden fluchten. Setzen Sie alle Befestigungsschrauben wieder ein und schließen Sie die zuvor getrennten Kabel an.

Schließen Sie die Montage nach dem üblichen Verfahren zum Schließen des Gehäuses ab. Beim ersten Start sollte das System das neue CM5 automatisch erkennen.

!!! warning "Warnung zu den Anschlüssen"
    Die Platine-zu-Platine-Anschlüsse sind die empfindlichsten Bauteile bei diesem Vorgang. Verwenden Sie niemals Metallwerkzeuge in ihrer Nähe, wenden Sie beim Aus- und Einbau ausschließlich senkrechte Kräfte an und prüfen Sie die Ausrichtung, bevor Sie drücken. Beschädigte Anschlüsse machen in der Regel den Austausch der Trägerplatine erforderlich.

!!! quote "Weiterführende Informationen"
    - **Einrichtung nach dem Austausch:** siehe [Software-Handbuch](./software.md)
    - **Fehlersuche beim Start:** siehe [Fehlersuche](./troubleshooting.md)
    - **Wärmemanagement:** siehe [Hardware-Referenz](../technical-reference/hardware.md)

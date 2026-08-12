---
translated_from: 6e5802b5be19c03e5a1ca6cf292d8785a9f37601
---

# Erste Schritte

Dieses Handbuch bringt Ihren HALPI2 in weniger als 30 Minuten zum Laufen und behandelt auch den festen Einbau. Halten Sie die Reihenfolge ein, damit die Inbetriebnahme reibungslos verläuft: Beginnen Sie mit einem Aufbau auf dem Tisch, prüfen Sie, dass alles funktioniert, und gehen Sie erst dann zum festen Einbau über.

## Sicherheit und Umgang

!!! warning "Bevor Sie beginnen"
    - Stellen Sie sicher, dass Ihre elektrische Anlage spannungsfrei ist, bevor Sie Verbindungen herstellen
    - Verwenden Sie passende Sicherungen (3–5 A) für die Stromanschlüsse
    - Gehen Sie sorgsam mit dem Gerät um — trotz robuster Bauweise können Stürze oder Stöße die Bauteile im Inneren beschädigen
    - Prüfen Sie beim Anschließen der Stromkabel die richtige Polarität
    - Vermeiden Sie elektrostatische Entladungen — erden Sie sich und reiben Sie weder Katzen noch Bernstein, bevor Sie Bauteile im Inneren berühren

## Was Sie benötigen

Aus der Verpackung des HALPI2:

- Das HALPI2-Gerät mit vorinstalliertem CM5 und NVMe-SSD
- Ein Stromkabel mit E7T-Stecker (2 m)

Optionale Teile (im Verkaufspaket enthalten):

- Ein Paar DC-Hohlstecker (5,5 × 2,1 mm), falls Sie ein handelsübliches 12-V-Steckernetzteil verwenden
- Die WLAN-/Bluetooth-Antenne von Raspberry Pi (erforderlich, wenn die Ersteinrichtung über WLAN erfolgt)

Zusätzlich benötigt (nicht enthalten):

- Eine Stromquelle mit 12 V oder 24 V
- Ein weiterer Rechner für die Einrichtung ohne Bildschirm (falls kein Bildschirm angeschlossen wird)
- Ein Netzwerkkabel (optional, für eine kabelgebundene Verbindung)
- Ein Bildschirm mit HDMI-Eingang (optional)
- USB-Tastatur und -Maus (optional, für den direkten Zugriff)

!!! tip "Tipp"
    Netzwerkgeräte wie Router oder WLAN-Access-Points verwenden meist ein 12-V-Netzteil, das sich auch für den HALPI2 eignet. Sehen Sie in Ihrem Fundus alter Geräte nach!

## Aufbau auf dem Tisch

Wir empfehlen, den HALPI2 vor dem festen Einbau auf einem Schreibtisch oder einer Werkbank auszuprobieren. Die Ersteinrichtung kann entweder ohne Bildschirm (headless) über eine Netzwerkverbindung oder mit angeschlossenem Bildschirm, Tastatur und Maus erfolgen. Ohne Bildschirm gelingt sie über eine kabelgebundene Ethernet-Verbindung oder über den WLAN-Access-Point des HALPI2.

### Schritt 1: Notwendige Peripherie anschließen

#### Für die Ersteinrichtung:

1. **Netzwerkverbindung (bei Installation ohne Bildschirm erforderlich):**
    - Schließen Sie das Ethernet-Kabel an
    - Schließen Sie die WLAN-/Bluetooth-Antenne an

2. **Bildschirmanschluss (optional):**
    - Schließen Sie für den direkten Zugriff einen HDMI-Bildschirm an
    - USB-Tastatur und -Maus, falls Sie einen Bildschirm verwenden

![Frontplattenanschlüsse](./front-panel-connectors.jpg)
*Frontplattenanschlüsse*

### Schritt 2: NMEA-2000-Anschluss (optional)

Wenn Sie den HALPI2 direkt auf einem Boot einbauen oder einen NMEA-2000-Aufbau auf dem Tisch haben, können Sie ihn bereits jetzt an das NMEA-2000-Netzwerk anschließen.

Ein [NMEA-2000-Netzwerk](https://docs.hatlabs.fi/nmea2000/) besteht aus einem Backbone-Kabel, an das alle Geräte über T-Stücke und Stichleitungen angeschlossen werden. Setzen Sie ein T-Stück in den Backbone des NMEA-2000-Netzwerks. Verbinden Sie den NMEA-2000-Micro-Anschluss des HALPI2 über eine NMEA-2000-Stichleitung mit diesem T-Stück.

### Schritt 3: Stromanschluss

!!! tip "Hinweis zur Versorgung über NMEA 2000"
    Der HALPI2 lässt sich auch über den NMEA-2000-Bus versorgen. Siehe [Versorgung über den NMEA-2000-Bus](#versorgung-uber-den-nmea-2000-bus) weiter unten im Abschnitt Fester Einbau.

Für den Aufbau auf dem Tisch verwenden wir das mitgelieferte E7T-Stromkabel. Verbinden Sie die Aderenden des Stromkabels wie folgt mit dem Hohlstecker (Buchse):

- **Rote Ader = Pluspol (+)**
- **Schwarze Ader = Minuspol (−)**

![Vom E7T-Stecker zum Hohlstecker](./e7t-barrel.jpg)
*Beispiel für die Verdrahtung zwischen E7T-Stecker und Hohlstecker*

Stecken Sie ein handelsübliches 12-V- oder 24-V-Netzteil in den Hohlstecker. Achten Sie darauf, dass es für mindestens 1 A ausgelegt ist, um den Bedarf des HALPI2 zu decken.

!!! warning "Warnung"
    Da eine Zugentlastung fehlt, sollte der Hohlstecker mit Schraubklemmen nur für vorübergehende Aufbauten verwendet werden. Versehentliches Ziehen am Kabel kann die Adern lösen und blank legen.

## Erster Start

Der HALPI2 wird mit [HaLOS](https://docs.halos.fi) ausgeliefert, einer containerbasierten Linux-Distribution mit Weboberfläche für maritime und industrielle Anwendungen. Wenn Sie ein anderes Betriebssystem wie OpenPlotter oder Raspberry Pi OS bevorzugen, siehe das [Software-Handbuch](../user-guide/software.md).

!!! info "HaLOS-Dokumentation"
    Dieses Handbuch behandelt die HALPI2-Hardware und das erste Einschalten. Alles zum Betriebssystem — Einrichtung beim ersten Start, Netzwerk, Anwendungen, Zertifikate und der tägliche Betrieb — steht in der **[HaLOS-Dokumentation](https://docs.halos.fi)**. Halten Sie sie beim Durchgehen der folgenden Schritte bereit.

**Schalten Sie den HALPI2 ein**, indem Sie das Netzteil anschließen, falls noch nicht geschehen. Nach wenigen Sekunden sollte sich die LED-Leiste mit roten Lichtern füllen — die Superkondensatoren laden. Die LEDs wechseln zu Gelb, sobald das System startet, und schließlich zu Grün, wenn das Betriebssystem läuft und der HALPI-Daemon mit dem Controller verbunden ist.

Ist ein Bildschirm angeschlossen, sehen Sie den Startbildschirm von Raspberry Pi OS und anschließend eine grafische Oberfläche.

!!! tip "Tipp"
    Die Muster der Status-LEDs sind unter [Täglicher Betrieb](../user-guide/operation.md#status-leds) beschrieben.

### Zugriff auf den HALPI2 ohne Bildschirm

Ohne angeschlossenen Bildschirm erreichen Sie den HALPI2 über seinen WLAN-Access-Point oder eine Ethernet-Verbindung. HaLOS bietet eine Weboberfläche — weitere Software ist nicht nötig[^ssh].

[^ssh]: SSH steht auch auf HaLOS-Abbildern ohne Bildschirm zur Verfügung (standardmäßig aktiviert). Auf den Desktop-Varianten aktivieren Sie SSH mit `raspi-config`. Standardzugangsdaten: Benutzername `pi`, Passwort `halos`.

Warten Sie zunächst, bis die LEDs grün leuchten — dann ist das System vollständig gestartet. Gehen Sie anschließend so vor:

**Variante 1 — Verbindung über den WLAN-Access-Point:** HaLOS richtet einen WLAN-Access-Point mit dem Namen `Halos-XXXX` (je Gerät verschieden) und dem Passwort `halos1234` ein. Verbinden Sie Ihren Rechner mit diesem Netz.

Der Access Point hat selbst keinen Internetzugang. Im nächsten Schritt weisen Sie den HALPI2 daher einem WLAN mit Internetzugang zu; das wird benötigt, um beim ersten Start die Container-Anwendungen herunterzuladen:

1. Öffnen Sie Cockpit unter `https://halos.local:9090/` und melden Sie sich an (Benutzername `pi`, Passwort `halos`).
2. Wechseln Sie zu **Networking** und klicken Sie auf **WiFi (wlan0)**.
3. Warten Sie, bis die Liste der verfügbaren Netze erscheint, und klicken Sie auf Ihr Netz.
4. Geben Sie das Passwort ein und klicken Sie auf **Add**.

Der HALPI2 hält den Access Point `Halos-XXXX` aufrecht, während er Ihrem Netz beitritt; Ihr Rechner kann daher kurz die Verbindung verlieren und sich anschließend selbst wieder verbinden.

**Variante 2 — Verbindung über kabelgebundenes Ethernet:** Haben Sie den HALPI2 per Ethernet mit Ihrem Netz verbunden, erhält er seine IP-Adresse automatisch per DHCP.

Öffnen Sie nach dem Verbinden einen Browser und rufen Sie auf:

- **Dashboard:** `https://halos.local/` — das Homarr-Dashboard mit Verweisen auf alle installierten Anwendungen
- **Systemverwaltung:** `https://halos.local:9090/` — Cockpit für Systemverwaltung, Aktualisierungen und Container-Anwendungen

!!! note "Warnung zum SSL-Zertifikat"
    Beim ersten Aufruf des Dashboards oder von Cockpit zeigt Ihr Browser eine Warnung („Nicht sicher“). HaLOS signiert seine Webdienste mit einer Zertifizierungsstelle (CA), die es selbst auf dem Gerät erzeugt, und Ihr Browser vertraut dieser CA noch nicht. Bestätigen Sie die Warnung, um vorerst fortzufahren.

    Damit die Warnung dauerhaft verschwindet, installieren Sie die CA des Geräts einmalig auf Ihrem Rechner — danach werden alle HaLOS-Dienste an allen Ports einwandfrei geprüft. Öffnen Sie `https://halos.local/ca/` für eine geführte, plattformabhängige Installation, oder lesen Sie [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) in der HaLOS-Dokumentation.

!!! info "Internetverbindung beim ersten Start erforderlich"
    Cockpit steht sofort zur Verfügung, das Haupt-Dashboard und die übrigen containerbasierten Anwendungen benötigen beim ersten Start jedoch eine Internetverbindung, um ihre Container-Images herunterzuladen. Verbinden Sie den HALPI2 per Ethernet mit dem Internet oder richten Sie das WLAN über Cockpit ein.

### Konfiguration beim ersten Start

!!! warning "Warnung"
    HaLOS wird mit Standardpasswörtern ausgeliefert, die beim ersten Start unbedingt geändert werden **müssen**, damit niemand unbefugt auf Ihr Gerät zugreifen kann.

HaLOS kennt zwei Sätze von Zugangsdaten:

| Zugangsart | Benutzername | Standardpasswort | Verwendet für |
|:-----------|:-------------|:-----------------|:--------------|
| SSO (Webanwendungen) | `admin` | `halos` | Dashboard, Signal K, Grafana und weitere Webanwendungen |
| System (SSH/Cockpit) | `pi` | `halos` | SSH-Zugang, Systemverwaltung in Cockpit |

#### Passwörter ändern

- **SSO-Passwort:** über Authelia ändern (vom Dashboard aus erreichbar)
- **Systempasswort:** in Cockpit (`https://halos.local:9090/`) in den Einstellungen des Benutzerkontos ändern, oder per SSH mit `passwd`

Ausführliche Hinweise zum ersten Start finden Sie im [HaLOS-Handbuch für den Einstieg](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Sie verwenden OpenPlotter oder Raspberry Pi OS?"
    Haben Sie ein anderes Betriebssystem geflasht, finden Sie die systemabhängigen Konfigurationshinweise im [Software-Handbuch](../user-guide/software.md#erste-konfiguration-des-systems).

### NMEA-2000-Verbindung prüfen (optional)

Am einfachsten prüfen Sie die NMEA-2000-Anbindung über den Status des Signal-K-Servers. In den HaLOS-Marine-Abbildern ist Signal K vorinstalliert und über das Dashboard unter `https://halos.local/` erreichbar. In den nicht maritimen HaLOS-Abbildern lässt sich Signal K über den Container-Apps-Store in Cockpit installieren.

Öffnen Sie die Weboberfläche von Signal K und beobachten Sie die Aktivität der Verbindung `can0`: Es sollte eingehender Datenverkehr zu sehen sein.

![Verbindungsaktivität des Signal-K-Servers](./sk-n2k-deltas.jpg)

## Das Gerät ausschalten

Der HALPI2 ist so ausgelegt, dass er sich beim Trennen von der Stromversorgung automatisch abschaltet. Wenn Sie das Gerät ausschalten möchten, trennen Sie einfach die Spannung — entweder über einen Schalter am Schaltpaneel oder durch Abziehen des Stromsteckers. Das System leitet dann selbstständig ein geordnetes Herunterfahren ein, sodass alle Anwendungen ordnungsgemäß geschlossen und das Dateisystem sicher ausgehängt wird.

Während des Herunterfahrens dimmen die LEDs zunächst (Spannungsausfall erkannt), leuchten violett, solange das Herunterfahren läuft, und erlöschen, wenn es abgeschlossen ist. Das Verhalten beim Herunterfahren — einschließlich des optionalen automatischen Neustarts nach einem Herunterfahren per Software — beschreibt [Täglicher Betrieb](../user-guide/operation.md#herunterfahren).

## Fehlersuche bei der Inbetriebnahme

### Häufige und weniger häufige Probleme

❌ **Keine Spannung, keine LEDs:**

- Prüfen Sie die Stromanschlüsse und die Polarität
- Kontrollieren Sie den Zustand der Sicherung
- Stellen Sie sicher, dass die Spannung zwischen 10 und 32 V liegt

❌ **Der WLAN-Access-Point ist nicht sichtbar:**

- Prüfen Sie, ob die Antenne richtig angeschlossen ist
- Versuchen Sie es mit einem anderen Gerät
- Prüfen Sie, ob der HALPI2 vollständig gestartet ist (die LEDs sollten grün leuchten)
- Versuchen Sie zunächst eine Verbindung über Ethernet

❌ **Das Gerät ist unter `halos.local` nicht erreichbar:**

- Verwenden Sie stattdessen die zugewiesene IP-Adresse (siehe die DHCP-Client-Liste Ihres Routers)

❌ **Ein Bildschirm ist angeschlossen, zeigt aber nichts an:**

- Prüfen Sie, ob das HDMI-Kabel fest sitzt
- Prüfen Sie, ob der Bildschirm eingeschaltet und auf den richtigen Eingang gestellt ist
- Versuchen Sie ein anderes HDMI-Kabel oder einen anderen Anschluss am Bildschirm
- Vergewissern Sie sich, dass der HALPI2 eingeschaltet ist (die LEDs sollten gelb oder grün leuchten)
- Blinken die LEDs in einem Regenbogenmuster, sitzt das Compute Module 5 nicht richtig auf der Trägerplatine. Ursache kann ein Transportschaden sein. Setzen Sie das CM5 nach der Anleitung im [Hardware-Handbuch](../user-guide/hardware.md#compute-module-5-austauschen) neu ein oder wenden Sie sich an den Support.

❌ **Der angeschlossene Bildschirm zeigt eine Fehlermeldung mit „nvme“:**

- Das bedeutet, dass die NVMe-SSD nicht erkannt oder nicht richtig initialisiert wird. Ursache kann ein Transportschaden sein. Setzen Sie die NVMe-SSD nach der Anleitung im [Hardware-Handbuch](../user-guide/hardware.md#nvme-ssd-austauschen) neu ein oder wenden Sie sich an den Support.

### Wo Sie Hilfe finden

- **Dokumentation:** Ausführliche Hinweise zur Fehlersuche stehen in den jeweiligen Abschnitten
- **Community:** Treten Sie den Community-Foren von Hat Labs bei
- **Support:** Wenden Sie sich bei Hardwareproblemen an den technischen Support

---

## Fester Einbau

Wenn auf dem Tisch alles funktioniert, gehen Sie für die feste Montage und Verkabelung nach den folgenden Schritten vor.

### Den Einbau planen

!!! tip "Tipp"
    Fotografieren Sie die vorhandene Verkabelung, bevor Sie etwas verändern — das hilft bei einer späteren Fehlersuche sehr.

Nehmen Sie sich Zeit für die Planung. Bedenken Sie:

- **Den Montageort** — Zugänglichkeit, Schutz, Belüftung
- **Die Kabelführung** — kurze Wege, Schutz vor Beschädigung
- **Die Stromquelle** — eigener oder gemeinsamer Stromkreis, Absicherung
- **Die Netzwerkanbindung** — NMEA 2000, Ethernet, WLAN-Abdeckung
- **Die Umgebungsbedingungen** — Temperatur, Feuchtigkeit, Vibration

#### Benötigte Werkzeuge und Materialien

**Werkzeuge:**

- Bohrmaschine mit Bohrern
- Schraubendrehersatz (PH2 Kreuzschlitz, großer Schlitz)
- Abisolierzange und Crimpzange für die Stromanschlüsse
- Multimeter zum Messen
- Heißluftpistole oder Feuerzeug (für Schrumpfschlauch)

**Materialien (nicht enthalten):**

- Befestigungsschrauben (4 mm oder M4, je nach Montagefläche)
- Passende Sicherungen (3–5 A) oder entsprechend ausgelegte Leitungsschutzschalter im Schaltpaneel
- Seewasserfeste Leitung (1,5 mm² oder 16 AWG für die Stromversorgung, falls das mitgelieferte Kabel zu kurz ist)
- Schrumpfschlauch und Kabelschuhe
- Kabelbinder und Befestigungsschellen

### Montage

#### Wahl des Montageorts

Wählen Sie einen Montageort, der Folgendes bietet:

!!! tip "Ideale Montagebedingungen"
    - **Temperaturbereich:** Umgebungstemperatur −20 °C … +60 °C
    - **Belüftung:** ausreichend Freiraum rund um das Gehäuse
    - **Schutz:** außerhalb von direktem Spritzwasser und mechanischer Beschädigung
    - **Zugänglichkeit:** leichter Zugang zu Anschlüssen und Status-LEDs
    - **Tragfähigkeit:** feste Montagefläche für 2 kg zuzüglich Kabel
    - **Platz:** mindestens 100 mm Freiraum vor den Frontplattenanschlüssen für die Kabelführung

Auch wenn dieses Handbuch feste Installationen behandelt, genügt es in der Praxis oft, das Gerät auf ein Regal oder einen Tisch zu stellen, sofern der Platz stabil und vor Feuchtigkeit und Stößen geschützt ist.

#### Hinweise zur Umgebung

**Einbau auf Schiffen:**

- Montieren Sie das Gerät oberhalb des zu erwartenden Bilgenwasserstands
- Meiden Sie Bereiche mit direktem Spritzwasser oder stehendem Wasser
- Berücksichtigen Sie Bewegung und Vibration des Schiffs und sichern Sie alle Verbindungen
- Verwenden Sie korrosionsbeständiges Befestigungsmaterial

**Einbau in Fahrzeugen:**

- Schützen Sie das Gerät vor Motorwärme und Vibration
- Sorgen Sie in geschlossenen Räumen für ausreichende Belüftung
- Berücksichtigen Sie die Zugänglichkeit für Wartungsarbeiten
- Verwenden Sie eine vibrationsfeste Befestigung

**Industrieller Einbau:**

- Schützen Sie das Gerät vor Prozesschemikalien und extremen Temperaturen
- Berücksichtigen Sie Quellen elektromagnetischer Störungen
- Stellen Sie die Einhaltung der örtlichen Elektrovorschriften sicher
- Planen Sie den Zugang für die regelmäßige Wartung ein

#### Montagerichtung

!!! info "Empfohlene Ausrichtung"
    **Bevorzugt:** Anschlüsse nach unten

    - Verringert das Risiko eindringenden Wassers
    - Erleichtert die Kabelführung
    - Erleichtert die Wartung

    **Vertretbar:** Anschlüsse zur Seite

    - Sorgen Sie für ausreichenden Wasserablauf
    - Verwenden Sie Dichtungen an den Kabeleinführungen

    **Vermeiden:** Anschlüsse nach oben

    - Erhöht das Risiko eindringenden Wassers
    - Erschwert die Kabelführung

#### Montageschritte

##### Schritt 0: Bohrschablone herunterladen und ausdrucken

Laden Sie die [HALPI2-Bohrschablone](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) herunter und drucken Sie sie im Maßstab 100 % aus. Mit ihr markieren Sie die Befestigungslöcher genau. Steht kein Drucker zur Verfügung, können Sie die Löcher auch anhand der Maße der Schablone von Hand anzeichnen oder das Gehäuse selbst als Vorlage auf der Montagefläche verwenden.

[![Bohrschablone](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Schritt 1: Montagefläche vorbereiten

1. **Reinigen Sie die Montagefläche**
2. **Markieren Sie die Befestigungslöcher** mit der ausgedruckten Schablone
3. **Setzen Sie das Gehäuse probeweise auf**, bevor Sie montieren
4. **Bohren Sie Vorbohrungen** für die Befestigungsschrauben

##### Schritt 2: HALPI2 montieren

1. **Setzen Sie das Gehäuse** mit den Anschlüssen in der gewünschten Ausrichtung an
2. **Ziehen Sie die Befestigungsschrauben an** — fest, aber nicht überdreht

### Feste Installation der Stromversorgung

#### Wahl der Stromquelle

**Variante 1: eigener Stromanschluss**

- Am zuverlässigsten und flexibelsten
- Erlaubt die volle Leistungsaufnahme
- Erleichtert Wartung und Fehlersuche

**Variante 2: Versorgung über den NMEA-2000-Bus**

- Vereinfacht die Verkabelung bei Einbauten auf Schiffen
- Auf 0,9 A Stromaufnahme begrenzt
- Erfordert besondere Aufmerksamkeit beim Spannungsabfall

#### Einstellung der Strombegrenzung

Der HALPI2 besitzt eine eingebaute Eingangsstrombegrenzung, die das anfängliche Laden der Superkondensatoren steuert und die Installation vor Überstrom schützt. Die Begrenzung lässt sich je nach Stromquelle und Anwendung auf 0,9 A oder 2,5 A einstellen. Die Standardeinstellung von 0,9 A passt für die meisten Anwendungen.

Um den Startvorgang zu beschleunigen oder Peripheriegeräte mit hohem Strombedarf zu versorgen, können Sie auf 2,5 A umstellen. Gehen Sie dabei nach der Anleitung im [Hardware-Handbuch](../user-guide/hardware.md#einstellung-der-strombegrenzung) vor.

#### Eigener Stromanschluss

##### Kabel vorbereiten

1. **Verlegen Sie das Stromkabel** vom HALPI2 zur Stromquelle
2. **Lassen Sie Serviceschlaufen** an beiden Enden
3. **Schützen Sie das Kabel** vor Scheuern und Beschädigung
4. **Kürzen Sie es auf Länge** und lassen Sie ausreichend Arbeitsspielraum

##### Anschluss an der Stromquelle

1. **Sichern Sie die Leitung ab**, indem Sie einen Leitungsschutzschalter mit 3–5 A vorsehen oder eine Leitungssicherung einbauen
2. **Isolieren Sie die Aderenden ab** auf passende Länge
3. **Bringen Sie die Kabelschuhe an** mit sauberer Crimptechnik
4. **Schließen Sie an die Stromquelle an:**
    - **Rote Ader:** Plusklemme (+)
    - **Schwarze Ader:** Minusklemme (−)
5. **Prüfen Sie die Polarität** mit dem Multimeter, bevor Sie die Spannung einschalten

##### Anschluss am HALPI2

Der E7T-Stecker ist vorkonfektioniert und muss vor Ort nicht angeschlossen werden. Stecken Sie ihn einfach in die Strombuchse des HALPI2.

#### Versorgung über den NMEA-2000-Bus

!!! info "Voraussetzungen"
    - Der Schalter der Strombegrenzung **muss** auf 0,9 A stehen
    - Das NMEA-2000-Netzwerk muss genügend Leistung bereitstellen
    - Die Stichleitung sollte nahe an der Einspeisung liegen, um den Spannungsabfall gering zu halten

##### Benötigte Teile

- NMEA-2000-Stichleitung (nicht enthalten)
- T-Stück für die Einbindung in den Backbone (nicht enthalten)

##### Einbauschritte

1. **Schalten Sie** alle NMEA-2000-Geräte **spannungsfrei**
2. **Öffnen Sie das Gehäuse des HALPI2** (Anleitung im [Hardware-Handbuch](../user-guide/hardware.md#zugang-zum-gehause))
3. **Suchen Sie den Stromanschluss der Trägerplatine**
4. **Ziehen Sie den vorhandenen Klemmenblock ab**
5. **Schließen Sie den internen NMEA-2000-Stromklemmenblock** an den Stromanschluss der Trägerplatine an
6. **Prüfen Sie, dass die Strombegrenzung** auf 0,9 A steht
7. **Verbinden Sie mit dem Backbone** über eine passende Stichleitung und ein T-Stück
8. **Testen Sie den Aufbau**, bevor Sie das Gehäuse schließen
9. **Bauen Sie das Gehäuse wieder zusammen**

![Verdrahtung der NMEA-2000-Versorgung](./n2k-power-conx.jpg)
*Um den HALPI2 über NMEA 2000 zu versorgen, ziehen Sie Klemmenblock 1 ab und ersetzen ihn durch Klemmenblock 2.*

### Netzwerk- und Datenverbindungen

#### NMEA-2000-Datenverbindung

Auch bei eigener Stromversorgung möchten Sie unter Umständen eine NMEA-2000-Datenverbindung:

1. **Setzen Sie ein T-Stück** in den NMEA-2000-Backbone
2. **Verbinden Sie eine Stichleitung** zwischen T-Stück und HALPI2
3. **Prüfen Sie den korrekten Abschluss** des NMEA-2000-Netzwerks
4. **Testen Sie die Verbindung** nach dem Einbau

#### Ethernet-Verbindung

Für die Netzwerkanbindung:

1. **Verwenden Sie seewasserfeste** oder für die Umgebung geeignete Kabel
2. **Setzen Sie Kabelverschraubungen oder Tüllen ein**, wenn das Kabel durch ein Schott geführt wird
3. **Lassen Sie Serviceschlaufen** an beiden Enden
4. **Testen Sie die Verbindung** vor dem endgültigen Einbau

#### WLAN-/Bluetooth-Antenne

1. **Montieren Sie die Antenne** am RP-SMA-Anschluss
2. **Richten Sie sie für die beste Abdeckung aus** — abseits metallischer Hindernisse. In Metallschränken kann ein RP-SMA-Verlängerungskabel (Stecker auf Buchse) nötig sein.
3. **Prüfen Sie die Signalstärke** an der endgültigen Position

### Fehlersuche beim Einbau

#### Probleme mit der Stromversorgung

❌ **Keine Betriebsanzeige:**

- Prüfen Sie Zustand und Nennwert der Sicherung
- Prüfen Sie die Spannung der Stromquelle (10–32 V)
- Bestätigen Sie die richtige Polarität
- Prüfen Sie die Durchgängigkeit der Stromkabel

❌ **Aussetzende Stromversorgung:**

- Prüfen Sie den festen Sitz aller Verbindungen
- Suchen Sie nach korrodierten Klemmen
- Prüfen Sie, ob der Leiterquerschnitt für den Strom ausreicht

#### Netzwerkverbindung

❌ **Keine NMEA-2000-Kommunikation:**

- Prüfen Sie den Netzwerkabschluss (120 Ω an beiden Enden)
- Prüfen Sie den Einbau des T-Stücks
- Prüfen Sie die Stichleitung auf Unversehrtheit
- Testen Sie mit einem als funktionsfähig bekannten Gerät

❌ **Keine Ethernet-Verbindung:**

- Prüfen Sie das Kabel mit einem Kabeltester
- Prüfen Sie die Konfiguration von Switch oder Router
- Suchen Sie nach Konflikten bei den IP-Adressen
- Prüfen Sie die Kabelkategorie (mindestens Cat5e)

#### Umgebungsbedingte Probleme

❌ **Eindringende Feuchtigkeit:**

- Prüfen Sie den Zustand aller Dichtungen
- Prüfen Sie die Ausrichtung der Anschlüsse
- Prüfen Sie die Kabeleinführungen
- Erwägen Sie zusätzlichen Schutz

❌ **Überhitzung:**

- Bringen Sie das Gerät weiter von Wärmequellen weg
- Prüfen Sie, ob die Luftzirkulation um das Gehäuse behindert wird

### Sicherheit und Konformität

#### Elektrische Sicherheit

- **Verwenden Sie passende Sicherungen** zum Schutz vor Überstrom
- **Sorgen Sie für eine ordnungsgemäße Erdung** gemäß den örtlichen Vorschriften
- **Schützen Sie vor Kurzschlüssen** durch sorgfältige Kabelführung

#### Einbau auf Schiffen

- **Befolgen Sie die örtlichen Vorschriften oder die ABYC-Normen** für elektrische Installationen
- **Verwenden Sie durchgängig seewasserfeste Bauteile**

#### Industrieller Einbau

- **Halten Sie die örtlichen Elektrovorschriften ein**
- **Sorgen Sie für ausreichenden EMI-/RFI-Schutz**
- **Dokumentieren Sie den Einbau** gemäß den Anforderungen des Betriebs

## Nächste Schritte

Sobald Ihr HALPI2 läuft:

1. **Lesen Sie [Täglicher Betrieb](../user-guide/operation.md)**, um zu erfahren, was die LEDs bedeuten und wie das Herunterfahren funktioniert
2. **Erkunden Sie das [Software-Handbuch](../user-guide/software.md)** für Aktualisierungen, Fernzugriff und den Befehl `halpi`
3. **Werfen Sie einen Blick in die Technische Referenz** für ausführliche Spezifikationen
4. **Treten Sie der Community bei** für Tipps, Kniffe und Unterstützung

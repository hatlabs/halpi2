---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Software-Handbuch

## Systemabbilder

Hat Labs stellt fertige Abbilder für den HALPI2 bereit. Alle enthalten die für die HALPI2-Hardware nötige Konfiguration und Anpassungen: CAN (NMEA 2000) als Netzwerkgerät `can0`, RS-485 (NMEA 0183) als `/dev/ttyAMA4` sowie das Paket `halpi2-firmware`.

### HaLOS (Standard)

[HaLOS](https://docs.halos.fi) ist eine containerbasierte Linux-Distribution für maritime und industrielle Anwendungen. Sie bietet eine Weboberfläche für Systemverwaltung, Anwendungsverwaltung und Überwachung — ohne Bildschirm, Tastatur oder VNC.

**Varianten des Abbilds:**

| Abbild | Beschreibung |
|:-------|:-------------|
| Halos-HALPI2 | Basisabbild ohne Bildschirm, mit Cockpit und Containerverwaltung |
| Halos-HALPI2-Desktop | Basisabbild mit Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Ohne Bildschirm, mit maritimen Anwendungen (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Desktop mit maritimen Anwendungen |

Die HaLOS-Abbilder finden Sie auf der [HaLOS-Releaseseite](https://github.com/halos-org/halos-pi-gen/releases/latest). Ausführliche Dokumentation steht auf [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter ist ein auf Raspberry Pi OS aufbauendes Abbild mit Erweiterungen für maritime Anwendungen. Es bietet eine klassische Desktop-Umgebung mit VNC-Fernzugriff und bringt Signal K und OpenCPN vorinstalliert mit.

Wenn Sie den HALPI2 ohne Bildschirm, Tastatur und Maus betreiben, können Sie sich entweder über ein Ethernet-Kabel oder über den WLAN-Access-Point verbinden (`OpenPlotter`, Passwort `12345678`).

In beiden Fällen erreichen Sie den HALPI2 über VNC oder SSH. Für VNC benötigen Sie den [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) von RealVNC.

Da sowohl der Access Point als auch das Standardbenutzerkonto mit Standardpasswörtern ausgeliefert werden, müssen diese unbedingt sofort nach dem ersten Start geändert werden. Das Vorgehen ist in der [OpenPlotter-Dokumentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html) beschrieben.

Die OpenPlotter-Abbilder finden Sie auf [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS und Raspberry Pi OS Lite

Wenn Sie das gewöhnliche Raspberry Pi OS vorziehen, können Sie das aktuelle Abbild mit HALPI2-Unterstützung aus dem [GitHub-Repository](https://github.com/hatlabs/openplotter-halpi/releases) herunterladen. Flashen Sie das Abbild mit dem Raspberry Pi Imager auf die SSD. Beim Flashen lassen sich Anpassungen vornehmen, etwa der Hostname, die Aktivierung von SSH und die WLAN-Konfiguration.

Verzichten Sie auf diese Anpassungen, benötigen Sie für die Ersteinrichtung einen Bildschirm und eine Tastatur am HALPI2. Beim ersten Start werden Sie nach Benutzername und Passwort gefragt.


## Ein Systemabbild auf die SSD flashen

Für das Flashen eines Systemabbilds auf die NVMe-SSD des HALPI2 gibt es zwei Wege: die SSD ausbauen und einen USB-NVMe-Adapter verwenden, oder direkt am HALPI2 flashen. Der USB-NVMe-Adapter ist der bequemere Weg: Solche Adapter sind online günstig erhältlich und der Ablauf ist unkompliziert.

### Flashen mit einem USB-NVMe-Adapter

Bauen Sie zunächst die NVMe-SSD nach dem im [Hardware-Handbuch](./hardware.md#nvme-ssd-austauschen) beschriebenen Verfahren aus dem HALPI2 aus. Laden Sie anschließend ein HALPI2-kompatibles Abbild herunter — entweder ein [HaLOS-Abbild](https://github.com/halos-org/halos-pi-gen/releases/latest) oder ein [OpenPlotter- bzw. Raspberry-Pi-OS-Abbild](https://github.com/hatlabs/openplotter-halpi/releases) — und achten Sie darauf, das für Ihren Einsatzzweck passende zu wählen.

Setzen Sie die SSD in den USB-NVMe-Adapter ein und schließen Sie ihn an Ihren Rechner an. Flashen Sie das heruntergeladene Abbild mit dem Raspberry Pi Imager auf die NVMe-SSD. Bei einem Raspberry-Pi-OS-Abbild können Sie während des Flashens die Anpassungen des Betriebssystems bearbeiten und übernehmen. Ohne diese Anpassungen benötigen Sie nach der Installation eine USB-Tastatur und eine Maus am HALPI2 für die Ersteinrichtung.

Bei HaLOS-Abbildern dürfen die Anpassungen des Betriebssystems beim Flashen **nicht** übernommen werden. HaLOS wird nach dem Start über seine Weboberfläche konfiguriert.

Ebenso dürfen beim OpenPlotter-Abbild die Anpassungen beim Flashen **nicht** übernommen werden. Die Konfiguration erfolgt nach dem ersten Start mit den Konfigurationswerkzeugen von Raspberry Pi und OpenPlotter.

Ziehen Sie nach dem Flashen den Adapter ab und entnehmen Sie die SSD. Setzen Sie sie nach dem Einbauverfahren des Hardware-Handbuchs wieder in den HALPI2 ein und schließen Sie das Gehäuse gemäß demselben Handbuch.

### Direkt am HALPI2 flashen

Alternativ können Sie das Systemabbild direkt am HALPI2 flashen, ohne die SSD auszubauen. Dieser Weg folgt dem üblichen Flash-Verfahren für Compute Modules, das in der [Raspberry-Pi-Dokumentation](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc) beschrieben ist. Die dortigen Hinweise zur Platine beziehen sich auf das CM5 IO Board, das Vorgehen ist beim HALPI2 aber vergleichbar.

**Voraussetzungen.** Installieren Sie das Werkzeug `rpiboot` aus dem [`usbboot`-Repository](https://github.com/raspberrypi/usbboot) von Raspberry Pi. Unter Linux und macOS übersetzen und installieren Sie es wie in der README des Repositorys beschrieben aus den Quellen; unter Windows installieren Sie den Raspberry Pi Imager oder das eigenständige `rpiboot`-Installationsprogramm, das auf derselben Seite verlinkt ist.

So bereiten Sie den HALPI2 für das Flashen über USB vor:

1. Schalten Sie das System vollständig aus und öffnen Sie den Gehäusedeckel nach dem Verfahren im [Hardware-Handbuch](./hardware.md#zugang-zum-gehause).
2. Suchen Sie den mit „USB Boot“ beschrifteten USB-C-Anschluss rechts neben der HAT-Umrandung auf der Trägerplatine und stellen Sie den benachbarten Startmodus-Schalter auf „Abnormal“. (Eine LED-Rückmeldung gibt es noch nicht — das Gerät ist stromlos.)
3. Verbinden Sie Ihren Rechner über ein USB-Kabel mit dem USB-Boot-Anschluss des HALPI2 und schalten Sie das Gerät wieder ein. Neben dem Startmodus-Schalter leuchtet nun eine bernsteinfarbene LED und bestätigt den USB-Startmodus.
4. Führen Sie auf Ihrem Rechner `rpiboot` aus. Das Werkzeug erkennt den HALPI2 und lädt die Massenspeicher-Firmware; der HALPI2 erscheint danach als USB-Massenspeicher.
5. Sobald `rpiboot` durchgelaufen ist und der Massenspeicher erscheint, stellen Sie den Startmodus-Schalter zurück auf „Normal“. Das unterbricht den Flash-Vorgang nicht und sorgt dafür, dass der HALPI2 nach dem nächsten Aus- und Einschalten normal vom frisch geflashten Abbild startet. Bleibt der Schalter auf „Abnormal“, geht das Gerät beim nächsten Start erneut in den USB-Startmodus, statt das neue System zu starten.
6. Flashen Sie das Systemabbild mit dem Raspberry Pi Imager (oder einem anderen Werkzeug, das auf ein Blockgerät schreiben kann) auf den neuen Massenspeicher.
7. Ziehen Sie nach dem Flashen das USB-Kabel ab, schalten Sie den HALPI2 aus und wieder ein und schließen Sie das Gehäuse.

!!! tip "Neustarten ohne Abziehen des Netzsteckers"
    Bei bereits geöffnetem Gehäuse ist der schnellste Weg, den HALPI2 neu zu starten, die beiden unteren Pins der Tasterleiste neben der USB-C-Buchse kurz zu überbrücken. Beide Pins gleichzeitig mit dem Metallgehäuse eines USB-C-Steckers zu berühren funktioniert gut und ist ungefährlich.

## Erste Konfiguration des Systems

Nach dem erstmaligen Flashen und Starten des HALPI2 sind einige Schritte nötig, um einen sicheren und ordnungsgemäßen Betrieb zu gewährleisten.

### Konfiguration von HaLOS

HaLOS wird vollständig über seine Weboberfläche konfiguriert. Nach dem ersten Start erreichen Sie Cockpit unter `https://halos.local:9090/` und das Dashboard unter `https://halos.local/`. Ändern Sie die Standardpasswörter sofort — Einzelheiten im Handbuch [Erste Schritte](../getting-started/getting-started.md#konfiguration-beim-ersten-start) und in der [HaLOS-Dokumentation](https://docs.halos.fi/getting-started/first-boot/).

### Konfiguration von OpenPlotter

Beim OpenPlotter-Abbild startet das System mit Standardpasswörtern für den WLAN-Access-Point und das Standardbenutzerkonto. Aus Sicherheitsgründen müssen diese Passwörter unbedingt sofort nach dem ersten Start geändert werden.

Das Ändern der Passwörter und die Ersteinrichtung sind im Handbuch [Erste Schritte](../getting-started/getting-started.md#konfiguration-beim-ersten-start) und in der [OpenPlotter-Dokumentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html) beschrieben.

### Konfiguration von Raspberry Pi OS

Wenn Sie das gewöhnliche Raspberry Pi OS statt OpenPlotter gewählt haben, folgen Sie dem üblichen Einrichtungsablauf von Raspberry Pi, der beim ersten Start erscheint. Der Assistent führt Sie durch das Anlegen von Benutzerkonten, das Setzen von Passwörtern, die WLAN-Konfiguration und das Aktivieren wichtiger Dienste wie SSH für den Fernzugriff.

Bei der Ersteinrichtung sollten Sie außerdem Zeitzone, Tastaturbelegung und weitere regionale Einstellungen passend zu Ihrer Umgebung wählen. Das Konfigurationswerkzeug von Raspberry Pi (`raspi-config`) bietet Zugang zu weiteren Systemeinstellungen, die sich nach der Ersteinrichtung anpassen lassen.

## Fernzugriff

Der HALPI2 unterstützt mehrere Wege des Fernzugriffs, sodass sich das System überwachen und steuern lässt, ohne physisch am Gerät zu sein. Das ist besonders wertvoll, wenn der HALPI2 ohne Bildschirm an schwer zugänglicher Stelle eingebaut ist.

### Webzugriff (HaLOS)

HaLOS bietet eine vollständige Weboberfläche zur Verwaltung, ohne zusätzliche Software:

- **Dashboard** (`https://halos.local/`): Das Homarr-Dashboard führt zu allen installierten Anwendungen, darunter Signal K, Grafana und weitere maritime Anwendungen.
- **Cockpit** (`https://halos.local:9090/`): Systemverwaltung mit Terminalzugang, Softwareaktualisierungen, Netzwerkkonfiguration und Verwaltung der Container-Anwendungen.

### SSH (Secure Shell)

SSH bietet einen sicheren Kommandozeilenzugang zum HALPI2, über den Sie Befehle ausführen, Dateien übertragen und das System aus der Ferne verwalten können. SSH ist auf HaLOS-Abbildern ohne Bildschirm und auf OpenPlotter standardmäßig aktiviert. Auf den HaLOS-Desktop-Varianten und unter Raspberry Pi OS aktivieren Sie es mit `raspi-config`.

Für die Verbindung genügt ein SSH-Client, etwa das eingebaute Terminal unter macOS und Linux oder ein Programm wie PuTTY unter Windows. Der grundlegende Befehl lautet:

```bash
ssh username@halpi2-ip-address
```

SSH-Verbindungen sind verschlüsselt und sicher und eignen sich bei sorgfältig eingerichteter Authentifizierung auch für öffentliche Netze. Sie benötigen zudem sehr wenig Bandbreite und sind damit ideal für den Fernzugriff über langsame Verbindungen mit hoher Latenz.

### VNC (Virtual Network Computing)

!!! note
    VNC betrifft ausschließlich die Abbilder OpenPlotter und Raspberry Pi OS Desktop. HaLOS setzt stattdessen auf den Webzugriff — siehe oben.

VNC bietet den Fernzugriff auf die grafische Oberfläche des HALPI2, sodass Sie den Desktop bedienen können, als säßen Sie davor. Auf OpenPlotter-Abbildern ist VNC vorinstalliert und vorkonfiguriert. Bei einer Raspberry-Pi-OS-Installation aktivieren Sie es mit dem Konfigurationswerkzeug `raspi-config`.

Für den Fernzugriff auf den Desktop verwenden Sie den [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) von RealVNC, der für Windows, macOS, Linux, iOS und Android verfügbar ist. VNC funktioniert gut in lokalen Netzen und ohne Internetverbindung und eignet sich damit für Bordinstallationen, in denen die Internetanbindung eingeschränkt oder gar nicht vorhanden ist.

Für den Fernzugriff über das Internet benötigt VNC zusätzliche Netzwerkeinstellungen wie eine Portweiterleitung oder ein VPN, da das Protokoll Firewalls und NAT-Geräte nicht von sich aus durchdringt.

### Raspberry Pi Connect

Raspberry Pi Connect bietet einen modernen, webbasierten Fernzugriff auf den Desktop: Sie verbinden sich mit einem gewöhnlichen Browser, ohne zusätzliche Software zu installieren. Der Dienst arbeitet automatisch durch Firewalls und NAT hindurch und eignet sich damit besonders für den Fernzugriff über das Internet ohne aufwendige Netzwerkkonfiguration.

Anders als VNC übernimmt Raspberry Pi Connect die Netzwerkfeinheiten selbst und ermöglicht einen unkomplizierten Zugriff von überall dort, wo eine Internetverbindung besteht. Er setzt allerdings voraus, dass der HALPI2 selbst durchgehend mit dem Internet verbunden ist.

## Softwareaktualisierungen

Regelmäßige Aktualisierungen werden empfohlen, um Leistung und Sicherheit des Systems zu erhalten.

### Aktualisierungen unter HaLOS

Unter HaLOS werden Systempakete (einschließlich der HALPI2-Firmware) über Cockpit oder auf der Kommandozeile mit `apt` aktualisiert. Containerbasierte Anwendungen (Signal K, Grafana und andere) aktualisieren Sie über die Container-Apps-Oberfläche in Cockpit, die nach neuen Container-Image-Versionen sucht.

### Aktualisierungen auf der Kommandozeile (alle Abbilder)

Der zuverlässigste Weg führt über die Kommandozeile. Öffnen Sie ein Terminal und führen Sie aus:

```bash
sudo apt update
sudo apt upgrade
```

Der erste Befehl (`apt update`) bringt die Paketdatenbank auf den neuesten Stand, der zweite (`apt upgrade`) lädt alle verfügbaren Aktualisierungen herunter und installiert sie. Dabei werden alle installierten Pakete aktualisiert, einschließlich des Raspberry-Pi-OS-Grundsystems, der OpenPlotter-Komponenten und der HALPI2-spezifischen Software.

Während der Aktualisierung werden Sie möglicherweise gebeten, die Installation bestimmter Pakete oder den Neustart von Diensten zu bestätigen. In der Regel können Sie zustimmen, sofern Sie keinen besonderen Grund dagegen haben.

### Grafische Aktualisierungen

Wer eine grafische Oberfläche bevorzugt, erhält im Desktop einen Hinweis, sobald Aktualisierungen verfügbar sind. In der oberen rechten Ecke der Taskleiste erscheint dann ein Download-Symbol. Ein Klick darauf öffnet die Aktualisierungsverwaltung, in der sich die verfügbaren Aktualisierungen durchsehen und installieren lassen.

## Firmware-Aktualisierungen

Die Controller-Firmware des HALPI2 wird über den üblichen Aktualisierungsablauf von Raspberry Pi OS auf den neuesten Stand gebracht — nahtlos und integriert. Regelmäßige Firmware-Aktualisierungen sind wichtig für die Leistung, für neue Funktionen und für die Kompatibilität mit sich weiterentwickelnder Software.

### Automatische Firmware-Aktualisierungen

Firmware-Aktualisierungen werden über den gewöhnlichen Systemaktualisierungsmechanismus als Debian-Pakete aus einer APT-Paketquelle verteilt. Zum Suchen und Installieren öffnen Sie ein Terminal und führen aus:

```bash
sudo apt update
sudo apt upgrade
```

Steht neue HALPI2-Firmware bereit, wird sie im Zuge der Aktualisierung automatisch heruntergeladen und installiert. Das System weist Sie darauf hin, wenn Firmware-Aktualisierungen enthalten sind.

Nach der Aktualisierung des Firmware-Pakets muss das System ordnungsgemäß neu gestartet werden, damit die Änderungen wirksam werden. Verwenden Sie den Abschaltbefehl, um ein vollständiges Aus- und Einschalten sicherzustellen:

```bash
sudo shutdown -h now
```

**Wichtig:** Ein bloßer Neustart genügt für Firmware-Aktualisierungen nicht. Erforderlich ist ein vollständiges Herunterfahren mit anschließendem Start, denn erst dann startet der Controller neu und übernimmt die neue Firmware. Die Controller-Firmware wird ausschließlich beim Einschaltvorgang aktualisiert.

### Sicherungsmechanismen der Firmware

Der HALPI2 besitzt eingebaute Schutzmechanismen gegen beschädigte Firmware. Wird das Gerät innerhalb von 30 Sekunden nach einer Firmware-Aktualisierung erneut gestartet, kehrt das System automatisch zur vorherigen Firmware-Version zurück. Das schützt vor problematischen Aktualisierungen, die den normalen Betrieb verhindern könnten.

### Firmware von Hand installieren

Für erfahrene Anwender oder bestimmte Fälle der Fehlersuche lässt sich die Firmware mit dem Kommandozeilenwerkzeug HALPI von Hand installieren. Die Firmware-Dateien liegen im Verzeichnis `/usr/share/halpi2-firmware/` und lassen sich direkt flashen:

```bash
halpi flash <firmware_file>.bin
```

### Automatische Firmware-Aktualisierungen deaktivieren

Wer bei einer bestimmten Firmware-Version bleiben möchte, kann die automatischen Aktualisierungen abschalten. Bearbeiten Sie dazu die Konfigurationsdatei des HALPI2:

```bash
sudo nano /etc/halpid/firmware.conf
```

Suchen Sie die Einstellung `AUTO_FLASH_ON_INSTALL` und setzen Sie sie auf `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Speichern Sie die Datei und verlassen Sie den Editor. Der HALPI2 flasht danach im gewöhnlichen Aktualisierungsablauf keine neue Firmware mehr automatisch; der Zeitpunkt liegt vollständig in Ihrer Hand. Firmware-Aktualisierungen lassen sich weiterhin mit `halpi flash` von Hand einspielen.


## Kommandozeilenwerkzeug HALPI

Die Softwareschnittstelle des HALPI2 besteht aus dem Dienst `halpid` und dem Kommandozeilenwerkzeug `halpi`. Gemeinsam ermöglichen sie Überwachung, Konfiguration und Steuerung des Systems.

### HALPI-Daemon (`halpid`)

Der HALPI-Daemon läuft als Systemdienst und stellt die Verbindung zwischen Betriebssystem und HALPI2-Controller her. Er ermöglicht den Co-op-Modus mit vollem Umfang an Überwachung und Energieverwaltung.

#### Verwaltung des Dienstes

Der Daemon wird über systemd gesteuert:

```bash
# Check daemon status
systemctl status halpid

# Start the daemon
sudo systemctl start halpid

# Stop the daemon
sudo systemctl stop halpid

# Enable auto-start at boot
sudo systemctl enable halpid

# Disable auto-start
sudo systemctl disable halpid

# View daemon logs
journalctl -u halpid -f
```

#### Konfiguration

Die Konfiguration des Daemons liegt in `/etc/halpid/halpid.conf`. Zum Bearbeiten:

```bash
sudo nano /etc/halpid/halpid.conf
```

Änderungen erfordern einen Neustart des Daemons:

```bash
sudo systemctl restart halpid
```

### Kommandozeilenwerkzeug HALPI (`halpi`)

Der Befehl `halpi` bietet direkten Zugriff auf die Funktionen des Controllers und den Systemzustand. Er kommuniziert mit dem Daemon, um Befehle auszuführen und Angaben über Betriebszustand, Konfiguration und Hardwarewerte des HALPI2 abzurufen.

#### Systemzustand und Überwachung

Die Hauptaufgabe des Kommandozeilenwerkzeugs ist es, einen umfassenden Systemzustand auszugeben: Hardwarewerte, Betriebszustand und Überwachungsdaten in Echtzeit.

Systemzustand anzeigen:

```bash
# Display comprehensive system status
halpi status
```

Der Befehl liefert einen vollständigen Überblick über den aktuellen Betriebszustand des HALPI2, einschließlich Spannungen, Stromaufnahme, Temperaturen und Controller-Status:

```
$ halpi status
 hardware_version               N/A
 firmware_version             3.1.0
 state              OperationalCoOp
 5v_output_enabled             True
 watchdog_enabled              True
 watchdog_timeout              10.0  s
 watchdog_elapsed               0.0  s
 V_in                          12.2  V
 I_in                          0.38  A
 V_supercap                   10.27  V
 T_mcu                         43.3  °C
 T_pcb                         35.2  °C
```

Möchten Sie nur einen einzelnen Wert verfolgen, rufen Sie ihn so ab:

```bash
# Show controller firmware version
halpi get firmware_version
```

Für Skripte eignet sich die REST-Schnittstelle besser, die im Abschnitt [Zugriff über die REST-API](#zugriff-uber-die-rest-api) beschrieben ist.

#### Verwaltung der Konfiguration

Mit dem Kommandozeilenwerkzeug HALPI lassen sich die aktuellen Einstellungen einsehen und die Betriebsparameter ändern.

Aktuelle Konfiguration anzeigen:

```bash
# Show current configuration
halpi config
```

Damit werden alle konfigurierbaren Parameter und ihre aktuellen Werte ausgegeben:

```
$ halpi config
 Key                       Value
 watchdog_timeout           10.0
 power_on_threshold          8.0
 solo_power_off_threshold    5.5
 led_brightness               40
 auto_restart               True
 solo_depleting_timeout      5.0
```

#### Steuerung der LEDs

Eine der am häufigsten angepassten Einstellungen ist die Helligkeit der LEDs, die sich an die Umgebung und die eigenen Vorlieben anpassen lässt.

Beispielbefehle zur Helligkeitssteuerung:

```bash
# Get current LED brightness (0-255)
halpi config get led_brightness

# Set LED brightness to low level for night operation
halpi config set led_brightness 40

# Set moderate brightness
halpi config set led_brightness 64

# Turn LEDs off completely
halpi config set led_brightness 0

# Maximum brightness for daylight operation
halpi config set led_brightness 255
```

Die Helligkeit nimmt Werte von 0 (vollständig aus) bis 255 (maximale Helligkeit) an und erlaubt damit eine feine Abstimmung der LEDs an der Frontplatte.

#### Energieverwaltung

Das Kommandozeilenwerkzeug HALPI stellt die nötigen Funktionen zur Energieverwaltung für einen sicheren Betrieb bereit.

Beispiele:

```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

Der Abschaltbefehl sorgt für ein sicheres Herunterfahren: Das Betriebssystem schließt die Anwendungen und hängt die Dateisysteme ordnungsgemäß aus, bevor der Controller die Spannung abschaltet.

#### Zugriff über die REST-API

Für erfahrene Anwender und eigene Programme stellt der HALPI-Daemon zusätzlich eine REST-Schnittstelle über einen Unix-Socket bereit. Sie erlaubt einen schnelleren programmatischen Zugriff auf die Systemdaten:

Einige Anwendungsbeispiele:

```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

Die REST-Schnittstelle ist besonders für Überwachungsanwendungen, Systeme zur Datenaufzeichnung oder andere Software nützlich, die in Echtzeit auf den Zustand des HALPI2 zugreifen muss.

Die vollständige Beschreibung der REST-API finden Sie im Kapitel [Softwareentwicklung: HALPI2-Daemon](../software-development/daemon.md).

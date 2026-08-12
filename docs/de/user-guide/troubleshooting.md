---
translated_from: 232aac811fb62f4cc46a1955e832ea282dc92332
---

# Fehlersuche

Diese Seite behandelt häufige Probleme beim Betrieb des HALPI2 und deren Behebung.

## Probleme mit Stromversorgung und Start

### Das System schaltet sich nicht ein

**Symptome:** keine LED-Aktivität, keine Reaktion nach dem Anschließen der Stromversorgung.

1. Prüfen Sie mit einem Multimeter am E7T-Anschluss, ob die Eingangsspannung im zulässigen Bereich liegt (10–32 V DC).
2. Kontrollieren Sie die Anschlüsse des Stromkabels — der E7T-Stecker muss vollständig eingesteckt sein.
3. Bei Versorgung über den NMEA-2000-Bus: prüfen Sie, ob die Strombegrenzung auf 0,9 A eingestellt ist und das Netzwerk genügend Strom liefern kann.
4. Öffnen Sie das Gehäuse und suchen Sie nach sichtbaren Schäden oder losen internen Verbindungen.

### Regenbogenfarbene LEDs

**Symptome:** die LEDs durchlaufen ein Regenbogenmuster und erreichen keinen stabilen Zustand.

Das Regenbogenmuster bedeutet, dass der Controller eingeschaltet ist, das CM5 aber nicht erkannt wird. Mögliche Ursachen:

- Das Compute Module ist nicht eingebaut oder sitzt nicht richtig.
- Das Compute Module ist defekt.
- Ein angeschlossenes Gerät speist Fremdspannungen ein, die den Start des CM5 verhindern — trennen Sie versuchsweise das HDMI-Kabel.

1. Trennen Sie alle HDMI-Bildschirme und starten Sie neu, um Fremdspannungen auszuschließen.
2. Besteht das Problem weiter, öffnen Sie das Gehäuse und prüfen Sie, ob das CM5-Modul vollständig in seinem Anschluss sitzt — dafür muss die Trägerplatine ausgebaut werden.

### Die LEDs bleiben gelb

**Symptome:** die LEDs wechseln von Rot (Laden) zu Gelb (eingeschaltet), erreichen aber nie Grün.

Gelb bedeutet, dass der Controller das CM5 eingeschaltet hat und auf die Antwort des Daemons wartet. Bleiben die LEDs gelb, startet entweder das Betriebssystem nicht oder der HALPI-Daemon ist nicht installiert.

1. Prüfen Sie, ob der Startmodus-Schalter auf „Normal“ steht — die gelbe LED daneben leuchtet, wenn er auf „Abnormal“ (USB-Start) steht.
2. Schließen Sie einen Bildschirm über HDMI an, um Startfehler oder die Anmeldeaufforderung zu sehen.
3. Prüfen Sie, ob die NVMe-SSD richtig im M.2-Steckplatz sitzt.
4. Startet das Betriebssystem einwandfrei, prüfen Sie, ob der Daemon installiert ist: `systemctl status halpid`
5. Ist der Daemon installiert, läuft aber nicht, sehen Sie in seinen Protokollen nach: `journalctl -u halpid -e`

### Das System schaltet sich unerwartet ab

**Symptome:** das System schaltet ohne Zutun ab, obwohl die externe Stromversorgung angeschlossen ist.

1. Prüfen Sie die Stabilität der Eingangsspannung — kurze Einbrüche unter den Schwellwert lösen den Ausfallzeitgeber aus. Beobachten Sie `V_in` in Echtzeit mit `halpi status`.
2. Untersuchen Sie das Stromkabel auf lose Verbindungen oder beschädigte Leiter, die zu Wackelkontakten führen können.
3. Bei Versorgung über den NMEA-2000-Bus: prüfen Sie, ob die Netzwerkspannung unter Last stabil bleibt. Andere Geräte mit hohem Strombedarf können Spannungseinbrüche verursachen.

## Firmware-Aktualisierung fehlgeschlagen oder zurückgesetzt

Startet das System innerhalb von 30 Sekunden nach einer Firmware-Aktualisierung neu, kehrt die Firmware zur Sicherheit automatisch zur vorherigen Version zurück.

1. Prüfen Sie die aktuelle Firmware-Version: `halpi get firmware_version`
2. Wiederholen Sie die Aktualisierung: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Fahren Sie nach der Installation sauber herunter: `sudo shutdown -h now`
4. Warten Sie das vollständige Abschalten ab, bevor Sie erneut einschalten — lassen Sie mindestens 30 Sekunden verstreichen, damit der Rücksetzmechanismus nicht auslöst.

## Probleme mit Netzwerk und Schnittstellen

### Keine NMEA-2000-Daten

**Symptome:** `candump can0` gibt nichts aus, oder Signal K empfängt keine Daten.

1. Prüfen Sie den Zustand der CAN-Schnittstelle:
    ```bash
    ip link show can0
    ```
    Die Schnittstelle sollte `UP` sein. Steht dort `DOWN`, aktivieren Sie sie:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Beobachten Sie die RX-LED auf der Trägerplatine — sie blinkt, wenn Daten im Netzwerk anliegen. Bleibt sie dunkel:
    - prüfen Sie den Anschluss des Micro-C-Kabels und die Lage des T-Stücks;
    - stellen Sie sicher, dass das NMEA-2000-Netzwerk versorgt wird und andere Geräte senden;
    - vergewissern Sie sich, dass der Abschlusswiderstands-Jumper (120 Ω) in NMEA-2000-Netzwerken **nicht** gesetzt ist.

3. Blinkt die RX-LED, `candump` zeigt aber nichts, liegt das Problem in der Software. Prüfen Sie die Konfiguration der CAN-Schnittstelle:
    ```bash
    ip -details link show can0
    ```

4. Suchen Sie nach Fehlern auf dem CAN-Bus:
    ```bash
    ip -statistics link show can0
    ```
    Hohe Fehlerzähler deuten auf Verkabelungsprobleme, eine falsche Baudrate oder Buskonflikte hin.

### Keine NMEA-0183-Daten über RS-485

**Symptome:** keine Daten an `/dev/ttyAMA4`, oder das angeschlossene Gerät antwortet nicht.

1. Öffnen Sie das Gehäuse und beobachten Sie die LEDs der RS-485-Schnittstelle — die RX-LED blinkt beim Empfang von Daten.
2. Prüfen Sie, ob die serielle Schnittstelle vorhanden und zugänglich ist:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Kontrollieren Sie die Polarität der Verdrahtung — RS-485 nutzt eine differentielle Übertragung über die Leitungen A und B. Vertauschte A- und B-Anschlüsse verhindern jede Kommunikation.

### Die Ethernet-Verbindung kommt nicht zustande

1. Prüfen Sie das Ethernet-Kabel und den RJ45-Stecker. Versuchen Sie es mit einem anderen Kabel.
2. Öffnen Sie das Gehäuse und beobachten Sie die Ethernet-LEDs für den Verbindungszustand.
3. Prüfen Sie den Verbindungszustand: `ip link show eth0`
4. Besteht die Verbindung, fehlt aber eine IP-Adresse, prüfen Sie DHCP: `sudo dhclient eth0`
5. Bei fester IP-Konfiguration prüfen Sie die Einstellungen in `/etc/network/interfaces` oder im NetworkManager.

## Probleme mit dem Betriebssystem

### Keine SSH-Verbindung zum Gerät möglich

1. Prüfen Sie, ob SSH aktiviert ist: `sudo systemctl status ssh`
2. Prüfen Sie die Netzwerkverbindung — antwortet das Gerät auf einen Ping?
3. SSH ist auf HaLOS-Images ohne Bildschirm und auf OpenPlotter standardmäßig aktiviert. Auf den HaLOS-Desktop-Varianten und unter Raspberry Pi OS aktivieren Sie SSH mit `raspi-config`.

### Das System ist langsam oder friert ein

1. Prüfen Sie die Prozessortemperatur — extreme Umgebungstemperaturen können zu einer thermischen Drosselung führen. Verwenden Sie:
    ```bash
    vcgencmd measure_temp
    ```
    Temperaturen über 80 °C weisen auf ein Wärmeproblem hin. Senken Sie die Umgebungstemperatur oder verbessern Sie die Luftzirkulation um das Gehäuse.

2. Prüfen Sie die Speicherauslastung: `free -h`
3. Prüfen Sie den Speicherplatz: `df -h` — eine volle NVMe-SSD führt zu erheblichen Leistungseinbußen.
4. Suchen Sie nach außer Kontrolle geratenen Prozessen: `top` oder `htop`

### Die Uhr geht nach einem Spannungsausfall falsch

Der HALPI2 besitzt eine Echtzeituhr (RTC) mit Pufferbatterie, die die Zeit bei Stromausfällen hält. Setzt sich die Uhr zurück:

1. Prüfen Sie die RTC-Batterie — sie kann getauscht werden müssen, wenn das Gerät längere Zeit ohne Spannung war.
2. Prüfen Sie die NTP-Synchronisierung, sobald das Netzwerk verfügbar ist: `timedatectl status`
3. Stellen Sie die Zeit bei Bedarf von Hand: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Diagnose über die LEDs

An den LED-Mustern lässt sich der Systemzustand rasch ablesen:

| Symptom | LED-Muster | Wahrscheinliche Ursache |
|:--------|:-----------|:------------------------|
| System startet nicht | Keine LEDs | Keine Eingangsspannung oder Hardwarefehler |
| Hängt beim Start | Rotes fortschreitendes Füllen | Superkondensatoren laden noch — abwarten |
| Hängt beim Start | Regenbogenmuster | CM5 nicht erkannt — Sitz des Moduls prüfen und Bildschirme trennen |
| Bleibt gelb | Gelber Balken | Betriebssystem startet nicht oder Daemon nicht installiert |
| Unerwartetes Abschalten | Oranger oder dunkelgrüner Balken, dann violett | Eingangsspannung ausgefallen, Herunterfahren auf Pufferenergie — Eingangsspannung prüfen |
| System startet von selbst neu | Alle LEDs dauerhaft rot vor dem Neustart | Watchdog-Zeitüberschreitung — das Betriebssystem reagierte nicht mehr, und der Controller hat es neu gestartet |
| Fehler | Alle LEDs blinken rot | Überspannung der Superkondensatoren — wenden Sie sich an den Support |

!!! quote "Weiterführende Informationen"
    - **LED-Muster:** siehe [Status-LEDs](./operation.md#status-leds)
    - **Verhalten bei Spannungsausfall:** siehe [Bei Spannungsausfall](./operation.md#bei-spannungsausfall)
    - **Verwaltung des Daemons:** siehe [Software-Handbuch](./software.md#halpi-daemon-halpid)
    - **Einzelheiten zur CAN-Schnittstelle:** siehe [Schnittstellen und Konnektivität](./interfaces.md#can-fd-nmea-2000)
    - **Einzelheiten zur RS-485-Schnittstelle:** siehe [Schnittstellen und Konnektivität](./interfaces.md#rs-485-nmea-0183)

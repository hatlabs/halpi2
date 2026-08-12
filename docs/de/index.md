---
translated_from: 14cb3c2c516710194d6d97569111c8626e6fc6ea
---

# Einführung

Der HALPI2 ist ein einsatzbereiter Bordcomputer auf Basis des Raspberry Pi Compute Module 5 (CM5). Er bietet einen umfassenden Funktionsumfang, der sich gut für den Einsatz auf Schiffen, in Fahrzeugen und in vielen industriellen Anwendungen eignet.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Link zum Shop"
    Den HALPI2 erhalten Sie im [Hat-Labs-Onlineshop](https://shop.hatlabs.fi/products/halpi2-computer).

## Was ist der HALPI2?

Der HALPI2 steht für die neueste Generation robuster eingebetteter Rechentechnik: Er verbindet die Leistung und das Ökosystem des Raspberry Pi mit Funktionen für anspruchsvolle Umgebungen. Anders als übliche Einplatinencomputer ist der HALPI2 von Grund auf für den Dauerbetrieb unter harten Bedingungen ausgelegt, dort wo Zuverlässigkeit entscheidend ist.

Das System vereint ein Raspberry Pi Compute Module 5 mit einer eigens entwickelten Trägerplatine, untergebracht in einem wasserdichten Aluminiumgehäuse, das zugleich als Kühlkörper dient. Diese Bauweise liefert die Rechenleistung moderner Anwendungen und behält dabei die Robustheit, die der Einsatz auf See und in der Industrie verlangt.

## Wichtigste Merkmale

### Merkmale des Gehäuses

- **Wasserdichtes Aluminiumgehäuse (IP65)**, Maße 200 × 130 × 60 mm
- **Standardanschlüsse** für Stromversorgung, NMEA 2000, Gigabit-Ethernet, HDMI, 2× USB 3.0 und WLAN-/Bluetooth-Antenne
- **Flexible Anschlussmöglichkeiten**: 3× PG7-Kabelverschraubung oder wasserdichte SP13-Stecker
- **Externe Antennen**: Aussparungen für 2 zusätzliche SMA-Anschlüsse
- **Für Wandmontage ausgelegt**, Anschlüsse für eine einfache Installation angeordnet

![Anschlussanordnung des HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Merkmale der Hardware

- **Weiter Eingangsspannungsbereich** von 10 bis 32 V DC, Schutz bis 100 V DC
- **Intelligente Strombegrenzung**: maximaler Eingangsstrom 0,9 oder 2,5 A, vom Benutzer wählbar
- **Zwei Arten der Stromversorgung**: direkter Anschluss mit 12 V/24 V oder Versorgung über den NMEA-2000-Bus mit 12 V
- **Pufferung durch Superkondensatoren** für Störfestigkeit und geordnetes Herunterfahren bei Spannungsausfall
- **Fortschrittliche Energieverwaltung** mit automatischer Erkennung von Spannungsausfällen
- **Passive Kühlung**: das CM5 hat direkten Kontakt zum Gehäuse
- **Schneller Massenspeicher** über eine handelsübliche M.2-NVMe-SSD-Schnittstelle
- **Erweiterbarkeit** über die 40-polige GPIO-Stiftleiste des Raspberry Pi
- **Vielfältige Ein- und Ausgänge**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, Gigabit-Ethernet
- **Schnittstellen für den Schiffsbereich**: CAN FD (NMEA 2000) und RS-485 (NMEA 0183)
- **Echtzeituhr** mit Pufferbatterie für eine genaue Zeitführung
- **Sichtbare Statusanzeige** über fünf RGB-LEDs
- **Bedienung** über konfigurierbare Tastenanschlüsse

![Innenansicht des HALPI2](./halpi2-interior.jpg)
*Innenansicht des HALPI2 mit Trägerplatine und den verschiedenen Anschlüssen.*

### Merkmale der Software

- **Vorkonfigurierte Systemabbilder** für den sofortigen Einsatz: [HaLOS](https://docs.halos.fi) (Standard), OpenPlotter, Raspberry Pi OS und Raspberry Pi OS Lite
- **Umfassende Überwachung** von Spannung, Strom und Temperatur
- **Unauffällige Firmware-Aktualisierungen** über die I2C-Schnittstelle

## Einsatzbereiche

### Anwendungen auf See

- **Navigationssysteme** mit Kartenplottern und GPS-Anbindung
- **Datenaufzeichnung** für Motorwerte, Umweltsensoren und Schiffsleistung
- **Signal-K-Server** für die einheitliche Verwaltung der Bordsdaten
- **Universeller Bordrechner** für Internetzugang und Kommunikation
- **Fehlersuche in NMEA-2000-Netzwerken** für eine höhere Systemzuverlässigkeit

### Industrielle Anwendungen

- **Prozessüberwachung** und Steuerungssysteme
- **Umweltmesstechnik** und Datenerfassung
- **Fernüberwachungsstationen**
- **Automatisierung und Steuerung von Anlagen**
- **Systeme zur vorausschauenden Wartung**

### Anwendungen im Fahrzeug

- **Systeme zum Flottenmanagement**
- **Telematik** und Fahrzeugortung
- **Infotainmentsysteme im Fahrzeug**
- **Diagnose- und Überwachungsplattformen**

## Lieferumfang

Die Verpackung des HALPI2 enthält:

- **Das HALPI2-Gerät** mit vorinstalliertem Compute Module 5 und NVMe-SSD (sofern nicht ohne bestellt)
- **Ein Stromkabel** mit E7T-Stecker (kompatibel mit Amphenol LTW Ceres Mini), Länge 2 m
- **Einen E7T-Kabelstecker** für eigene Installationen
- **Ein Paar DC-Hohlstecker** (5,5 × 2,1 mm) für handelsübliche 12-V- und 24-V-Netzteile
- **Eine Raspberry-Pi-Antenne** für WLAN und Bluetooth
- **3 PG7-Kabelverschraubungen** für zusätzliche Schnittstellen
- **Eine Kurzanleitung und die Garantieunterlagen**

![Inhalt der Zubehörtasche des HALPI2](./goodie-bag-contents.jpg)

Separat erhältliches Zubehör:

- **NMEA-2000-Stichleitung** für die Versorgung über den Bus
- **Verschiedene Steckersätze** für eigene Installationen

## So nutzen Sie diese Dokumentation

Diese Dokumentation richtet sich sowohl an Endanwender, die praktische Anleitungen suchen, als auch an Entwickler, die ausführliche technische Angaben benötigen.

### Für Endanwender

- Beginnen Sie mit **Erste Schritte** für Inbetriebnahme und Installation
- Lesen Sie **Täglicher Betrieb** für den Alltag: Bedeutung der LEDs, Herunterfahren, Verhalten bei Spannungsausfall
- Ziehen Sie die **Fehlersuche** heran, wenn Probleme auftreten

### Für Entwickler

- Lesen Sie die **Technische Referenz** für ausführliche Spezifikationen
- Studieren Sie die Abschnitte zur **Softwareentwicklung** für eigene Anwendungen
- Sehen Sie sich die **Konstruktionsdateien** für die Integrationsplanung an

### Konventionen dieser Dokumentation

- 💡 **Tipp**-Kästen geben Abkürzungen für häufige Aufgaben
- ⚠️ **Warnung** und **Achtung** heben wichtige Sicherheitshinweise hervor
- 🔧 **Technische Details** vertiefen die Umsetzung
- 📖 **Querverweise** verbinden zusammengehörende Themen in der gesamten Dokumentation

Ob Sie Ihren ersten Bordcomputer einrichten oder eine eigene Industrielösung entwickeln — diese Dokumentation begleitet Sie durch jeden Schritt.

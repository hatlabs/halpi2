---
translated_from: fc7ea79249b080c0f717303d066b9f6ea6d64795
---

# Konstruktionsdateien und Schaltpläne

Diese Seite stellt die Schaltpläne und die mechanischen Konstruktionsdateien des HALPI2 bereit.

Die Elektronik des HALPI2 wird mit KiCad entworfen. Die Konstruktionsdateien sind im [GitHub-Repository](https://github.com/hatlabs/HALPI2-hardware) verfügbar. Zu jeder veröffentlichten Version gibt es dort ein entsprechendes Tag.

Die Schaltpläne stehen unten der Einfachheit halber als PDF bereit. Die Layoutdaten der Leiterplatte sind ausschließlich im GitHub-Repository verfügbar.

Mechanische Konstruktionsdateien gibt es vorerst nur für das Gehäuse. Der Entwurf wurde mit Autocad Fusion erstellt, die Exportdateien im STEP-Format lassen sich jedoch mit den meisten CAD-Programmen öffnen.

## Version 0.6.1

Eine Korrekturversion mit Verbesserungen bei Signalintegrität und Masseführung, die während der Produktionstests festgestellt wurden.

Änderungen:

- Taktoszillator für NVMe SUSCLK ergänzt, behebt Kompatibilitätsprobleme mit bestimmten NVMe-SSDs
- Fehlende Kondensatoren an den RX-Differenzpaaren des USB3-Hubs ergänzt
- Masseanbindung an jedem Befestigungspunkt vorgesehen

### Konstruktionsdateien

- KiCad-Konstruktionsdateien: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Schaltplan (PDF): [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Version 0.6.0

Die dritte Produktionsversion des HALPI2 mit weiteren kleineren Korrekturen an der Trägerplatine. Der Funktionsumfang der Platine entspricht dem der Version 0.5.0.

Änderungen:

- Der 3,3-V-Ausgang wird nun vom Controller geschaltet statt dauerhaft aktiv zu sein
- Testpunkte für bessere Produktionstests ergänzt
- HDMI-, MIPI- und USB3-Schnittstellen für bessere Signalintegrität neu geroutet
- Die FFC-Anschlüsse auf der Platine liegen nun waagerecht
- Stabilität des 10-V-Abwärtswandlers verbessert — er pfeift unter keinen Umständen mehr
- Symmetrierschaltung der Superkondensatoren mit einem einzigen Vierfach-Operationsverstärker neu aufgebaut
- Footprints einiger Bauteile geändert, um die Verfügbarkeit zu verbessern

### Konstruktionsdateien

- KiCad-Konstruktionsdateien: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Schaltplan (PDF): [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Version 0.5.0

Die zweite Produktionsversion des HALPI2 mit kleineren Korrekturen an der Trägerplatine. Die Funktion der Platine entspricht der Version 0.4.0.

Änderungen:

- Kleinere Fehler im Bestückungsdruck behoben
- 3,3-V-Kupferflächen auf der Unterseite neben den Befestigungsstrukturen entfernt
- Einpressmuttern für die einfachere Montage von HATs ergänzt
- Einpressmuttern für die sicherere Befestigung des Compute Module ergänzt
- Jumper-Stiftleisten für bessere mechanische Festigkeit wieder in Durchsteckmontage (THT) ausgeführt
- Eigene +5-V-Betriebsanzeige ergänzt
- Symmetrierung der Superkondensatoren gelockert
- Jumper-Stiftleisten für bessere Bedienbarkeit neu angeordnet

### Konstruktionsdateien

- KiCad-Konstruktionsdateien: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Schaltplan (PDF): [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- 3D-Modell des Gehäuses: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (identisch mit Version 0.4.0)

## Version 0.4.0

Die erste öffentliche Version des HALPI2.

### Konstruktionsdateien

- KiCad-Konstruktionsdateien: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Schaltplan (PDF): [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- 3D-Modell des Gehäuses: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

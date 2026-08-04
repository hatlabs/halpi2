---
translated_from: 930b506809e4abe2b54e4fea058658a9d6d94461
---

# Bekannte Fehler

Auf dieser Seite sind die bekannten Hardwareprobleme der verschiedenen HALPI2-Versionen aufgeführt.

## Geräte der Version 0.4.0

#### Stromspitze beim Einschalten

Wird das Gerät mit vollständig entladenen Superkondensatoren eingeschaltet, kann der Einschaltstrom für einen kurzen Moment 1,1 A erreichen. Damit erfüllt das Gerät nominell die NMEA-2000-Anforderung eines maximalen Eingangsstroms von 1 A nicht.

Der höhere Anfangsstrom entsteht durch ein schwer zu fassendes Zusammenspiel zwischen den Analogeingängen des Mikrocontrollers RP2040 und der Strombegrenzungsschaltung.

#### Kupferfläche unter den Montagestegen

Eine 3,3-V-Versorgungsfläche auf der Unterseite der Leiterplatte reicht über die Montagestege hinaus. In einigen Gehäusen weisen diese Stege noch scharfe Gussgrate auf (Aluminiumreste aus dem Gießvorgang). Durchdringt die Kante eines Grats den Lötstopplack der Leiterplatte, kann sie einen Kurzschluss zur 3,3-V-Fläche verursachen und das Einschalten des Geräts verhindern.

Das Problem lässt sich beheben, indem PVC-Isolierband auf die Montagestege geklebt wird.

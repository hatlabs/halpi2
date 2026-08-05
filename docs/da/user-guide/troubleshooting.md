# Fejlfinding

Denne side gennemgår almindelige problemer, du kan støde på, når du bruger HALPI2, og hvordan du løser dem.

## Problemer med strøm og opstart

### Systemet tænder ikke

**Symptomer:** Ingen LED-aktivitet, ingen livstegn efter tilslutning af strøm.

1. Kontrollér med et multimeter ved E7T-stikket, at indgangsspændingen ligger inden for området (11–32 V DC).
2. Kontrollér strømkablets tilslutninger — sørg for, at E7T-stikket sidder helt i bund.
3. Hvis du bruger busforsyning fra NMEA 2000, skal du kontrollere, at strømbegrænseren er indstillet til 0,9 A, og at netværket kan levere strøm nok.
4. Åbn kabinettet, og se efter synlige skader eller løse interne forbindelser.

### Regnbue-LED'er

**Symptomer:** LED'erne kører et regnbuemønster igennem og når aldrig en stabil tilstand.

Regnbuemønsteret betyder, at controlleren er tændt, men at CM5 ikke registreres. Det kan ske, hvis:

- Compute Module ikke er monteret eller ikke sidder ordentligt.
- Compute Module er defekt.
- En tilsluttet enhed sender vildfarne spændinger ind, der forhindrer CM5 i at starte — prøv at frakoble HDMI-kablet.

1. Frakobl alle HDMI-skærme, og genstart for at udelukke forstyrrelser fra vildfarne spændinger.
2. Hvis problemet fortsætter, skal du åbne kabinettet og kontrollere, at CM5-modulet sidder helt i bund i sit stik — det kræver, at bærekortet afmonteres.

### LED'erne bliver ved med at være gule

**Symptomer:** LED'erne går fra rød (opladning) til gul (tændt), men når aldrig grøn.

Den gule tilstand betyder, at controlleren har tændt for CM5 og venter på svar fra dæmonen (baggrundstjenesten). Hvis LED'erne bliver ved med at være gule, er styresystemet enten ikke ved at starte, eller også er HALPI-dæmonen ikke installeret.

1. Kontrollér, at kontakten til boot-tilstand står i positionen Normal — den gule indikator-LED ved siden af kontakten lyser, når boot-tilstanden er sat til Abnormal (USB-boot).
2. Tilslut en skærm via HDMI for at se, om der er opstartsfejl eller en loginprompt.
3. Kontrollér, at NVMe SSD'en sidder korrekt i sin M.2-slot.
4. Hvis styresystemet starter korrekt, skal du kontrollere, at dæmonen er installeret: `systemctl status halpid`
5. Hvis dæmonen er installeret, men ikke kører, skal du se dens logfiler: `journalctl -u halpid -e`

### Systemet lukker ned uventet

**Symptomer:** Systemet slukker uden brugerens indgriben, selvom den eksterne strømforsyning er tilsluttet.

1. Kontrollér, at indgangsspændingen er stabil — korte spændingsdyk under grænsen udløser strømafbrydelsestimeren. Brug `halpi status` til at følge `V_in` i realtid.
2. Efterse strømkablet for løse forbindelser eller beskadigede ledere, der kan give periodisk kontaktsvigt.
3. Hvis du bruger busforsyning fra NMEA 2000, skal du kontrollere, at netværksspændingen forbliver stabil under belastning. Andre enheder med stort strømforbrug på netværket kan give spændingsfald.

## Firmwareopdatering mislykkedes eller blev rullet tilbage

Hvis systemet genstarter inden for 30 sekunder efter en firmwareopdatering, ruller firmwaren automatisk tilbage til den forrige version som en sikkerhedsforanstaltning.

1. Kontrollér den aktuelle firmwareversion: `halpi get firmware_version`
2. Prøv opdateringen igen: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Udfør en ren nedlukning, når opdateringen er installeret: `sudo shutdown -h now`
4. Vent, til systemet er helt slukket, før du tilslutter strømmen igen — lad der gå mindst 30 sekunder før næste genstart, så tilbagerulningsmekanismen ikke udløses.

## Problemer med netværk og grænseflader

### Ingen NMEA 2000-data

**Symptomer:** `candump can0` viser intet output, eller Signal K modtager ikke data.

1. Kontrollér CAN-grænsefladens status:
    ```bash
    ip link show can0
    ```
    Grænsefladen bør vise `UP`. Hvis den viser `DOWN`, skal du aktivere den:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Kontrollér RX-LED'en på bærekortet — den bør blinke, når der er data på netværket. Hvis RX-LED'en er inaktiv:
    - Kontrollér Micro-C-kablets tilslutning og T-stikkets placering.
    - Kontrollér, at NMEA 2000-netværket har strøm, og at andre enheder sender.
    - Sørg for, at termineringsjumperen på 120 Ω **ikke** er aktiveret på NMEA 2000-netværk.

3. Hvis RX-LED'en blinker, men `candump` intet viser, ligger problemet i softwaren. Kontrollér konfigurationen af CAN-grænsefladen:
    ```bash
    ip -details link show can0
    ```

4. Se efter fejl på CAN-bussen:
    ```bash
    ip -statistics link show can0
    ```
    Høje fejltal tyder på problemer med kablingen, forkert baudrate eller konflikter på bussen.

### Ingen NMEA 0183-data på RS-485

**Symptomer:** Ingen data på `/dev/ttyAMA4`, eller den tilsluttede enhed svarer ikke.

1. Åbn kabinettet, og kontrollér LED'erne for RS-485-grænsefladen — RX-LED'en bør blinke, når der modtages data.
2. Kontrollér, at den serielle port findes og er tilgængelig:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Kontrollér ledningernes polaritet — RS-485 bruger differentiel signalering med A/B-linjer. Ombyttede A- og B-forbindelser forhindrer al kommunikation.

### Ethernetforbindelsen bliver ikke etableret

1. Kontrollér ethernetkablet og RJ45-stikket. Prøv et andet kabel.
2. Åbn kabinettet, og kontrollér ethernet-LED'erne for forbindelsesstatus.
3. Kontrollér forbindelsens status: `ip link show eth0`
4. Hvis forbindelsen er oppe, men der ikke er nogen IP-adresse, skal du kontrollere DHCP: `sudo dhclient eth0`
5. Ved statiske IP-konfigurationer skal du kontrollere indstillingerne i `/etc/network/interfaces` eller NetworkManager.

## Problemer med styresystemet

### Kan ikke oprette SSH-forbindelse til enheden

1. Kontrollér, at SSH er aktiveret: `sudo systemctl status ssh`
2. Kontrollér netværksforbindelsen — kan du pinge enheden?
3. SSH er aktiveret som standard på HaLOS-images uden skærm (headless) og på OpenPlotter. På HaLOS Desktop-varianter og Raspberry Pi OS kan SSH aktiveres via `raspi-config`.

### Systemet er langsomt eller fryser

1. Kontrollér CPU-temperaturen — ekstreme omgivelsestemperaturer kan give termisk nedregulering. Brug:
    ```bash
    vcgencmd measure_temp
    ```
    Temperaturer over 80 °C tyder på et termisk problem. Prøv at sænke omgivelsestemperaturen eller forbedre luftcirkulationen omkring kabinettet.

2. Kontrollér hukommelsesforbruget: `free -h`
3. Kontrollér diskforbruget: `df -h` — en fuld NVMe SSD giver alvorlige ydelsesproblemer.
4. Se efter processer, der er løbet løbsk: `top` eller `htop`

### Uret er forkert efter strømsvigt

HALPI2 har et realtidsur (RTC) med backupbatteri, som holder tiden under strømafbrydelser. Hvis uret nulstilles:

1. Kontrollér RTC-batteriet — det skal måske udskiftes, hvis systemet har været uden strøm i længere tid.
2. Kontrollér NTP-synkroniseringen, når netværket er tilgængeligt: `timedatectl status`
3. Indstil om nødvendigt tiden manuelt: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## LED-diagnostik

Brug LED-mønstrene til hurtigt at fastslå systemets tilstand:

| Symptom | LED-mønster | Sandsynlig årsag |
|:--------|:------------|:-----------------|
| Systemet starter ikke | Ingen LED'er | Ingen indgangsstrøm eller hardwarefejl |
| Hænger under opstart | Rød, gradvis udfyldning | Superkondensatoren oplader stadig — vent |
| Hænger under opstart | Regnbuemønster | CM5 ikke registreret — kontrollér modulets montering, og frakobl skærme |
| Bliver ved med at være gul | Konstant gul | Styresystemet starter ikke, eller dæmonen er ikke installeret |
| Uventet nedlukning | Rullende grøn/gul | Strømsvigt registreret — kontrollér den tilførte strøm |
| Overspænding | LED 1 blinker rødt | Indgangsspændingen er for høj (>32 V) |
| Fejl | Alle LED'er blinker rødt | Hardwarefejl — kontakt producenten |

!!! quote "Relaterede oplysninger"
    - **LED-mønstre:** Se [Status-LED-indikatorer](./operation.md#status-led-indicators)
    - **Strømstyring:** Se [Strømstyring og nedlukningsprocedurer](./operation.md#power-management-and-shutdown-procedures)
    - **Håndtering af dæmonen:** Se [Softwarevejledning](./software.md#halpi-daemon-halpid)
    - **Detaljer om CAN-grænsefladen:** Se [Grænseflader og forbindelser](./interfaces.md#can-fd-nmea-2000)
    - **Detaljer om RS-485-grænsefladen:** Se [Grænseflader og forbindelser](./interfaces.md#rs-485-nmea-0183)

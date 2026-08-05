---
translated_from: 35a84e7f96c0891201c8a8248bf146139684b772
---

# Feilsøking

Denne siden tar for seg vanlige problemer du kan møte når du bruker HALPI2, og hvordan du løser dem.

## Problemer med strøm og oppstart

### Systemet slår seg ikke på

**Symptomer:** Ingen LED-aktivitet, ingen tegn til liv etter at strømmen er koblet til.

1. Kontroller med et multimeter ved E7T-kontakten at inngangsspenningen er innenfor området (11–32 VDC).
2. Sjekk tilkoblingene til strømkabelen – pass på at E7T-kontakten er skjøvet helt inn.
3. Hvis du bruker strøm fra NMEA 2000-bussen, kontroller at strømbegrensningen er satt til 0,9 A, og at nettverket kan levere nok strøm.
4. Åpne kabinettet og se etter synlige skader eller løse interne forbindelser.

### Regnbue-LED-er

**Symptomer:** LED-ene går gjennom et regnbuemønster og kommer aldri videre til en stabil tilstand.

Regnbuemønsteret betyr at kontrolleren har slått seg på, men at CM5 ikke blir funnet. Det kan skje hvis:

- Compute Module ikke er installert eller ikke sitter riktig.
- Compute Module er defekt.
- En tilkoblet enhet sender inn uønskede spenninger som hindrer CM5 i å starte – prøv å koble fra HDMI-kabelen.

1. Koble fra eventuelle HDMI-skjermer og start på nytt for å utelukke forstyrrelser fra uønskede spenninger.
2. Hvis problemet vedvarer, åpner du kabinettet og kontrollerer at CM5-modulen sitter helt inne i kontakten sin – dette krever at bærekortet demonteres.

### LED-ene blir stående gule

**Symptomer:** LED-ene går fra rødt (lading) til gult (slått på), men når aldri grønt.

Den gule tilstanden betyr at kontrolleren har gitt strøm til CM5 og venter på svar fra daemonen. Blir LED-ene stående gule, starter enten ikke operativsystemet opp, eller så er ikke HALPI-daemonen installert.

1. Kontroller at bryteren for oppstartsmodus står i «Normal»-stilling – den gule varsel-LED-en ved siden av bryteren lyser når oppstartsmodus er satt til «Abnormal» (USB-oppstart).
2. Koble til en skjerm via HDMI for å se etter oppstartsfeil eller en påloggingsledetekst.
3. Kontroller at NVMe SSD-en sitter riktig i M.2-sporet.
4. Hvis operativsystemet starter opp som det skal, kontroller at daemonen er installert: `systemctl status halpid`
5. Hvis daemonen er installert, men ikke kjører, sjekk loggene: `journalctl -u halpid -e`

### Systemet slår seg av uventet

**Symptomer:** Systemet slår seg av uten at brukeren gjør noe, selv om ekstern strøm er tilkoblet.

1. Kontroller om inngangsspenningen er stabil – korte spenningsfall under terskelen utløser strømbruddstimeren. Bruk `halpi status` til å følge `V_in` i sanntid.
2. Undersøk strømkabelen for løse forbindelser eller skadde ledere som kan gi ustabil kontakt.
3. Hvis du bruker strøm fra NMEA 2000-bussen, kontroller at nettverksspenningen holder seg stabil under belastning. Andre enheter med høyt strømforbruk på nettverket kan gi spenningsfall.

## Firmware-oppdateringen mislyktes eller ble rullet tilbake

Hvis systemet startes på nytt innen 30 sekunder etter en firmware-oppdatering, ruller firmwaren automatisk tilbake til den forrige versjonen som en sikkerhetsmekanisme.

1. Sjekk gjeldende firmwareversjon: `halpi get firmware_version`
2. Prøv oppdateringen på nytt: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Når oppdateringen er installert, gjør du en ren nedstenging: `sudo shutdown -h now`
4. Vent til systemet er helt avslått før du kobler til igjen – la det gå minst 30 sekunder før neste omstart, slik at tilbakerullingsmekanismen ikke utløses.

## Problemer med nettverk og grensesnitt

### Ingen NMEA 2000-data

**Symptomer:** `candump can0` gir ingen utdata, eller Signal K mottar ikke data.

1. Sjekk statusen til CAN-grensesnittet:
    ```bash
    ip link show can0
    ```
    Grensesnittet skal vise `UP`. Hvis det viser `DOWN`, aktiverer du det:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Sjekk RX-LED-en på bærekortet – den skal blinke når det er data på nettverket. Hvis RX-LED-en er inaktiv:
    - Kontroller tilkoblingen av Micro-C-kabelen og plasseringen av T-koblingen.
    - Sjekk at NMEA 2000-nettverket har strøm, og at andre enheter sender.
    - Pass på at termineringsjumperen på 120 Ω **ikke** er aktivert for NMEA 2000-nettverk.

3. Hvis RX-LED-en blinker, men `candump` ikke viser noe, ligger problemet i programvaren. Kontroller konfigurasjonen av CAN-grensesnittet:
    ```bash
    ip -details link show can0
    ```

4. Se etter feil på CAN-bussen:
    ```bash
    ip -statistics link show can0
    ```
    Høye feiltall tyder på problemer med kablingen, feil baudrate eller konflikt på bussen.

### Ingen NMEA 0183-data på RS-485

**Symptomer:** Ingen data på `/dev/ttyAMA4`, eller den tilkoblede enheten svarer ikke.

1. Åpne kabinettet og sjekk LED-ene for RS-485-grensesnittet – RX-LED-en skal blinke når det mottas data.
2. Kontroller at serieporten finnes og er tilgjengelig:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Sjekk polariteten i kablingen – RS-485 bruker differensiell signalering med A/B-linjer. Byttes A og B om, blir kommunikasjon umulig.

### Ingen Ethernet-forbindelse

1. Sjekk Ethernet-kabelen og RJ45-kontakten. Prøv en annen kabel.
2. Åpne kabinettet og sjekk Ethernet-LED-ene for forbindelsesstatus.
3. Kontroller forbindelsesstatusen: `ip link show eth0`
4. Hvis forbindelsen er oppe, men det ikke finnes noen IP-adresse, sjekk DHCP: `sudo dhclient eth0`
5. For oppsett med statisk IP kontrollerer du innstillingene i `/etc/network/interfaces` eller NetworkManager.

## Problemer med operativsystemet

### Kan ikke koble til enheten med SSH

1. Kontroller at SSH er aktivert: `sudo systemctl status ssh`
2. Sjekk nettverksforbindelsen – får du svar når du pinger enheten?
3. SSH er aktivert som standard på HaLOS-systembilder uten skjerm og på OpenPlotter. På HaLOS Desktop-varianter og på Raspberry Pi OS kan SSH aktiveres med `raspi-config`.

### Systemet går tregt eller henger

1. Sjekk CPU-temperaturen – ekstreme omgivelsestemperaturer kan føre til termisk struping. Bruk:
    ```bash
    vcgencmd measure_temp
    ```
    Temperaturer over 80 °C tyder på et varmeproblem. Prøv å senke omgivelsestemperaturen eller bedre luftstrømmen rundt kabinettet.

2. Sjekk minnebruken: `free -h`
3. Sjekk diskbruken: `df -h` – en full NVMe SSD gir alvorlige ytelsesproblemer.
4. Se etter prosesser som løper løpsk: `top` eller `htop`

### Klokken er feil etter strømbortfall

HALPI2 har en sanntidsklokke (RTC) med reservebatteri som holder tiden ved strømbrudd. Hvis klokken nullstilles:

1. Sjekk RTC-batteriet – det kan trenge utskifting hvis systemet har vært uten strøm over lengre tid.
2. Kontroller NTP-synkroniseringen når nettverket er tilgjengelig: `timedatectl status`
3. Still klokken manuelt om nødvendig: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## LED-diagnostikk

Bruk LED-mønstrene til å stille rask diagnose på systemtilstanden:

| Symptom | LED-mønster | Sannsynlig årsak |
|:--------|:------------|:-------------|
| Systemet starter ikke | Ingen LED-er | Ingen inngangsstrøm eller maskinvarefeil |
| Henger under oppstart | Gradvis rød fylling | Superkondensatorene lades fortsatt – vent |
| Henger under oppstart | Regnbuemønster | CM5 ikke funnet – kontroller at modulen sitter riktig, og koble fra skjermer |
| Blir stående gul | Lyser fast gult | Operativsystemet starter ikke, eller daemonen er ikke installert |
| Uventet nedstenging | Rullende grønt/gult | Strømbortfall oppdaget – kontroller inngangsstrømmen |
| Overspenning | LED 1 blinker rødt | Inngangsspenningen er for høy (>32 V) |
| Feil | Alle LED-er blinker rødt | Maskinvarefeil – kontakt produsenten |

!!! quote "Relatert informasjon"
    - **LED-mønstre:** Se [Status-LED-indikatorer](./operation.md#status-led-indikatorer)
    - **Strømstyring:** Se [Strømstyring og nedstengingsprosedyrer](./operation.md#strmstyring-og-nedstengingsprosedyrer)
    - **Styring av daemonen:** Se [Programvareveiledning](./software.md#halpi-daemonen-halpid)
    - **Detaljer om CAN-grensesnittet:** Se [Grensesnitt og tilkoblingsmuligheter](./interfaces.md#can-fd-nmea-2000)
    - **Detaljer om RS-485-grensesnittet:** Se [Grensesnitt og tilkoblingsmuligheter](./interfaces.md#rs-485-nmea-0183)

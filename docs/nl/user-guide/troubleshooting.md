---
translated_from: 35a84e7f96c0891201c8a8248bf146139684b772
---

# Probleemoplossing

Deze pagina behandelt veelvoorkomende problemen bij het gebruik van de HALPI2 en hoe u ze verhelpt.

## Problemen met voeding en opstarten

### Systeem gaat niet aan

**Symptomen:** geen ledactiviteit, geen enkel teken van leven nadat de voeding is aangesloten.

1. Controleer met een multimeter aan de E7T-connector of de ingangsspanning binnen het bereik ligt (11–32 V DC).
2. Controleer de aansluitingen van de voedingskabel — zorg dat de E7T-connector volledig is ingestoken.
3. Gebruikt u busvoeding via NMEA 2000, controleer dan of de stroombegrenzer op 0,9 A staat en of het netwerk voldoende stroom kan leveren.
4. Open de behuizing en kijk of er zichtbare schade of losse interne verbindingen zijn.

### Regenboogkleurige leds

**Symptomen:** de leds doorlopen een regenboogpatroon en komen nooit in een vaste toestand.

Het regenboogpatroon betekent dat de controller is ingeschakeld maar dat de CM5 niet wordt gedetecteerd. Dit kan gebeuren als:

- De Compute Module niet is geïnstalleerd of niet goed is geplaatst.
- De Compute Module defect is.
- Een aangesloten apparaat zwerfspanningen injecteert die het opstarten van de CM5 verhinderen — probeer de HDMI-kabel los te koppelen.

1. Koppel alle HDMI-beeldschermen los en start opnieuw op om storing door zwerfspanning uit te sluiten.
2. Blijft het probleem bestaan, open dan de behuizing en controleer of de CM5-module volledig in de connector is geplaatst — hiervoor moet het carrierboard worden gedemonteerd.

### Leds blijven geel

**Symptomen:** de leds gaan van rood (opladen) naar geel (ingeschakeld), maar worden nooit groen.

De gele toestand betekent dat de controller de CM5 heeft ingeschakeld en wacht op antwoord van de daemon. Blijven de leds geel, dan start het besturingssysteem niet op of is de HALPI-daemon niet geïnstalleerd.

1. Controleer of de opstartmodusschakelaar in de stand `Normal` staat — de gele indicatieled naast de schakelaar brandt wanneer de opstartmodus op `Abnormal` (USB-boot) staat.
2. Sluit een beeldscherm aan via HDMI om te kijken of er opstartfouten of een inlogprompt zijn.
3. Controleer of de NVMe SSD goed in het M.2-slot is geplaatst.
4. Start het besturingssysteem wel goed op, controleer dan of de daemon is geïnstalleerd: `systemctl status halpid`
5. Is de daemon geïnstalleerd maar draait hij niet, bekijk dan de logs: `journalctl -u halpid -e`

### Systeem sluit onverwacht af

**Symptomen:** het systeem schakelt zichzelf uit zonder tussenkomst van de gebruiker, terwijl er externe voeding is aangesloten.

1. Controleer de stabiliteit van de ingangsspanning — korte spanningsdips onder de drempelwaarde starten de blackouttimer. Gebruik `halpi status` om `V_in` in realtime te volgen.
2. Inspecteer de voedingskabel op losse verbindingen of beschadigde aders die een onderbroken contact kunnen veroorzaken.
3. Gebruikt u busvoeding via NMEA 2000, controleer dan of de netwerkspanning onder belasting stabiel blijft. Andere verbruikers met een hoge stroomafname op het netwerk kunnen spanningsval veroorzaken.

## Firmware-update mislukt of teruggedraaid

Start het systeem na een firmware-update binnen 30 seconden opnieuw op, dan draait de firmware zichzelf uit veiligheidsoverwegingen automatisch terug naar de vorige versie.

1. Controleer de huidige firmwareversie: `halpi get firmware_version`
2. Voer de update opnieuw uit: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Sluit het systeem na het installeren van de update netjes af: `sudo shutdown -h now`
4. Wacht tot het systeem volledig is uitgeschakeld voordat u de voeding weer aansluit — laat minstens 30 seconden verstrijken voor de volgende herstart, zodat het terugdraaimechanisme niet wordt geactiveerd.

## Problemen met netwerk en interfaces

### Geen NMEA 2000-gegevens

**Symptomen:** `candump can0` geeft geen uitvoer, of Signal K ontvangt geen gegevens.

1. Controleer de status van de CAN-interface:
    ```bash
    ip link show can0
    ```
    De interface hoort `UP` te tonen. Toont ze `DOWN`, breng ze dan omhoog:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Controleer de RX-led op het carrierboard — die hoort te knipperen wanneer er gegevens op het netwerk staan. Is de RX-led inactief:
    - Controleer de aansluiting van de Micro-C-kabel en de plaatsing van het T-stuk.
    - Controleer of het NMEA 2000-netwerk spanning heeft en of andere apparaten zenden.
    - Zorg dat de jumper voor de 120 Ω-afsluitweerstand **niet** is ingeschakeld voor NMEA 2000-netwerken.

3. Knippert de RX-led wel maar toont `candump` niets, dan zit het probleem in de software. Controleer de configuratie van de CAN-interface:
    ```bash
    ip -details link show can0
    ```

4. Controleer op fouten op de CAN-bus:
    ```bash
    ip -statistics link show can0
    ```
    Hoge fouttellers wijzen op bekabelingsproblemen, een onjuiste baudrate of conflicten op de bus.

### Geen NMEA 0183-gegevens op RS-485

**Symptomen:** geen gegevens op `/dev/ttyAMA4`, of het aangesloten apparaat reageert niet.

1. Open de behuizing en controleer de leds van de RS-485-interface — de RX-led hoort te knipperen wanneer er gegevens binnenkomen.
2. Controleer of de seriële poort bestaat en toegankelijk is:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Controleer de polariteit van de bedrading — RS-485 werkt met differentiële signalen over de A/B-lijnen. Verwisselde A- en B-aansluitingen maken communicatie onmogelijk.

### Geen ethernetverbinding

1. Controleer de ethernetkabel en de RJ45-connector. Probeer een andere kabel.
2. Open de behuizing en controleer de ethernetleds op de verbindingsstatus.
3. Controleer de verbindingsstatus: `ip link show eth0`
4. Is de verbinding actief maar is er geen IP-adres, controleer dan DHCP: `sudo dhclient eth0`
5. Bij een vaste IP-configuratie controleert u de instellingen in `/etc/network/interfaces` of in NetworkManager.

## Problemen met het besturingssysteem

### Geen SSH-verbinding met het apparaat mogelijk

1. Controleer of SSH is ingeschakeld: `sudo systemctl status ssh`
2. Controleer de netwerkverbinding — kunt u het apparaat pingen?
3. SSH staat standaard aan op de HaLOS-images zonder beeldscherm (headless) en op OpenPlotter. Op de HaLOS Desktop-varianten en op Raspberry Pi OS kunt u SSH inschakelen via `raspi-config`.

### Systeem is traag of loopt vast

1. Controleer de temperatuur van de processor — bij extreme omgevingstemperaturen kan het systeem terugschakelen om oververhitting te voorkomen. Gebruik:
    ```bash
    vcgencmd measure_temp
    ```
    Temperaturen boven 80 °C wijzen op een warmteprobleem. Verlaag de omgevingstemperatuur of zorg voor betere luchtstroming rond de behuizing.

2. Controleer het geheugengebruik: `free -h`
3. Controleer het schijfgebruik: `df -h` — een volle NVMe SSD veroorzaakt ernstige prestatieproblemen.
4. Controleer of er processen op hol zijn geslagen: `top` of `htop`

### Klok loopt niet goed na spanningsuitval

De HALPI2 heeft een realtimeklok (RTC) met backupbatterij die de tijd bijhoudt tijdens stroomuitval. Als de klok wordt teruggezet:

1. Controleer de RTC-batterij — die kan aan vervanging toe zijn als het systeem lange tijd zonder spanning heeft gestaan.
2. Controleer de NTP-synchronisatie zodra er netwerk beschikbaar is: `timedatectl status`
3. Stel de tijd zo nodig handmatig in: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Leddiagnose

Aan de hand van de ledpatronen stelt u de systeemtoestand snel vast:

| Symptoom | Ledpatroon | Waarschijnlijke oorzaak |
|:---------|:-----------|:------------------------|
| Systeem start niet | Geen leds | Geen ingangsspanning of hardwarefout |
| Blijft hangen tijdens het opstarten | Rode balk die vol loopt | Supercondensator laadt nog op — wachten |
| Blijft hangen tijdens het opstarten | Regenboogpatroon | CM5 niet gedetecteerd — controleer de plaatsing van de module en koppel beeldschermen los |
| Blijft geel | Continu geel | Besturingssysteem start niet op of daemon niet geïnstalleerd |
| Onverwacht afsluiten | Lopend groen/geel | Spanningsuitval gedetecteerd — controleer de ingangsspanning |
| Overspanning | Led 1 knippert rood | Ingangsspanning te hoog (> 32 V) |
| Storing | Alle leds knipperen rood | Hardwarefout — neem contact op met de fabrikant |

!!! quote "Gerelateerde informatie"
    - **Ledpatronen:** zie [Statusleds](./operation.md#statusleds)
    - **Energiebeheer:** zie [Energiebeheer en afsluitprocedures](./operation.md#energiebeheer-en-afsluitprocedures)
    - **Beheer van de daemon:** zie [Softwarehandleiding](./software.md#halpi-daemon-halpid)
    - **Details over de CAN-interface:** zie [Interfaces en connectiviteit](./interfaces.md#can-fd-nmea-2000)
    - **Details over de RS-485-interface:** zie [Interfaces en connectiviteit](./interfaces.md#rs-485-nmea-0183)

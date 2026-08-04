---
translated_from: 35a84e7f96c0891201c8a8248bf146139684b772
---

# Felsökning

Den här sidan tar upp vanliga problem du kan stöta på när du använder HALPI2, och hur du löser dem.

## Problem med ström och start

### Systemet startar inte

**Symtom:** ingen aktivitet i lysdioderna, inga livstecken efter att strömmen anslutits.

1. Kontrollera med en multimeter vid E7T-kontakten att inspänningen ligger inom området (11–32 V DC).
2. Kontrollera strömkabelns anslutningar — se till att E7T-kontakten är helt intryckt.
3. Om du matar enheten från NMEA 2000-bussen, kontrollera att strömbegränsningen är inställd på 0,9 A och att nätverket kan leverera tillräckligt med ström.
4. Öppna kapslingen och leta efter synliga skador eller lösa interna anslutningar.

### Regnbågsfärgade lysdioder

**Symtom:** lysdioderna löper genom ett regnbågsmönster och når aldrig ett stabilt läge.

Regnbågsmönstret betyder att styrkretsen har fått spänning men att CM5 inte hittas. Det kan bero på att:

- Compute Module inte är monterad eller inte sitter ordentligt.
- Compute Module är trasig.
- En ansluten enhet matar in läckspänningar som hindrar CM5 från att starta — prova att koppla bort HDMI-kabeln.

1. Koppla bort alla HDMI-skärmar och starta om för att utesluta läckspänningar.
2. Om problemet kvarstår, öppna kapslingen och kontrollera att CM5-modulen sitter helt i sin kontakt — det kräver att bärkortet demonteras.

### Lysdioderna förblir gula

**Symtom:** lysdioderna går från rött (laddning) till gult (spänning på) men blir aldrig gröna.

Gult betyder att styrkretsen har slagit på CM5 och väntar på svar från daemonen. Om lysdioderna förblir gula startar antingen inte operativsystemet, eller så är HALPI-daemonen inte installerad.

1. Kontrollera att startlägesomkopplaren står i läget ”Normal” — den gula indikeringslysdioden bredvid tänds när läget är ”Abnormal” (USB-start).
2. Anslut en skärm via HDMI för att se startfel eller inloggningsprompten.
3. Kontrollera att NVMe SSD-enheten sitter ordentligt i sin M.2-plats.
4. Om operativsystemet startar som det ska, kontrollera att daemonen är installerad: `systemctl status halpid`
5. Om daemonen är installerad men inte körs, titta i dess loggar: `journalctl -u halpid -e`

### Systemet stängs av oväntat

**Symtom:** systemet stänger av sig utan åtgärd, trots att den externa strömförsörjningen är ansluten.

1. Kontrollera inspänningens stabilitet — korta dippar under tröskeln utlöser avbrottstimern. Följ `V_in` i realtid med `halpi status`.
2. Undersök strömkabeln efter lösa anslutningar eller skadade ledare som kan ge glappkontakt.
3. Om du matar enheten från NMEA 2000-bussen, kontrollera att nätverkets spänning håller sig stabil under belastning. Andra strömtörstiga enheter på nätverket kan orsaka spänningsfall.

## Firmwareuppdatering misslyckades eller återställdes

Om systemet startar om inom 30 sekunder efter en firmwareuppdatering återgår firmwaren automatiskt till föregående version som säkerhetsåtgärd.

1. Kontrollera nuvarande firmwareversion: `halpi get firmware_version`
2. Gör om uppdateringen: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. När uppdateringen är installerad, stäng av kontrollerat: `sudo shutdown -h now`
4. Vänta tills systemet är helt avstängt innan du kopplar in det igen — låt minst 30 sekunder gå före nästa start så att återställningsmekanismen inte löser ut.

## Problem med nätverk och gränssnitt

### Inga NMEA 2000-data

**Symtom:** `candump can0` visar ingenting, eller Signal K tar inte emot data.

1. Kontrollera CAN-gränssnittets status:
    ```bash
    ip link show can0
    ```
    Gränssnittet ska visa `UP`. Om det visar `DOWN`, aktivera det:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Titta på RX-lysdioden på bärkortet — den ska blinka när det finns trafik på nätverket. Om RX-lysdioden är släckt:
    - kontrollera Micro-C-kabelns anslutning och T-kopplingens placering;
    - se till att NMEA 2000-nätverket har spänning och att andra enheter sänder;
    - kontrollera att bygeln för 120 Ω-terminering **inte** är isatt i NMEA 2000-nätverk.

3. Om RX-lysdioden blinkar men `candump` inte visar något ligger felet i programvaran. Kontrollera CAN-gränssnittets konfiguration:
    ```bash
    ip -details link show can0
    ```

4. Leta efter fel på CAN-bussen:
    ```bash
    ip -statistics link show can0
    ```
    Höga felräknare tyder på kabelproblem, fel överföringshastighet eller konkurrens på bussen.

### Inga NMEA 0183-data på RS-485

**Symtom:** inga data på `/dev/ttyAMA4`, eller den anslutna enheten svarar inte.

1. Öppna kapslingen och titta på RS-485-gränssnittets lysdioder — RX-lysdioden ska blinka när data tas emot.
2. Kontrollera att serieporten finns och är åtkomlig:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Kontrollera kablagets polaritet — RS-485 använder differentiell signalering på ledarna A och B. Om A och B kastats om fungerar ingen kommunikation.

### Ethernet-länken kommer inte upp

1. Kontrollera ethernet-kabeln och RJ45-kontakten. Prova en annan kabel.
2. Öppna kapslingen och titta på ethernet-lysdioderna för att se länkens status.
3. Kontrollera länkens status: `ip link show eth0`
4. Om länken är uppe men ingen IP-adress finns, kontrollera DHCP: `sudo dhclient eth0`
5. Vid fast IP-konfiguration, kontrollera inställningarna i `/etc/network/interfaces` eller i NetworkManager.

## Problem med operativsystemet

### Går inte att ansluta med SSH

1. Kontrollera att SSH är aktiverat: `sudo systemctl status ssh`
2. Kontrollera nätverksanslutningen — svarar enheten på ping?
3. SSH är aktiverat som standard i HaLOS-avbilder utan skärm och i OpenPlotter. I HaLOS Desktop-varianterna och i Raspberry Pi OS aktiverar du SSH med `raspi-config`.

### Systemet är långsamt eller hänger sig

1. Kontrollera processorns temperatur — hög omgivningstemperatur kan orsaka termisk nedvarvning. Använd:
    ```bash
    vcgencmd measure_temp
    ```
    Temperaturer över 80 °C tyder på ett värmeproblem. Sänk omgivningstemperaturen eller förbättra luftcirkulationen runt kapslingen.

2. Kontrollera minnesanvändningen: `free -h`
3. Kontrollera diskutrymmet: `df -h` — en full NVMe SSD ger kraftiga prestandaproblem.
4. Leta efter processer som skenat: `top` eller `htop`

### Klockan går fel efter ett strömavbrott

HALPI2 har en realtidsklocka (RTC) med backupbatteri som håller tiden under strömavbrott. Om klockan nollställs:

1. Kontrollera RTC-batteriet — det kan behöva bytas om enheten har stått utan spänning länge.
2. Kontrollera NTP-synkroniseringen när nätverket är tillgängligt: `timedatectl status`
3. Ställ tiden manuellt vid behov: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Diagnostik med lysdioderna

Lysdiodernas mönster gör det snabbt att avgöra systemets tillstånd:

| Symtom | LED-mönster | Trolig orsak |
|:-------|:------------|:-------------|
| Systemet startar inte | Inga lysdioder | Ingen inspänning eller hårdvarufel |
| Fastnar under start | Röd successiv fyllning | Superkondensatorerna laddas fortfarande — vänta |
| Fastnar under start | Regnbågsmönster | CM5 hittas inte — kontrollera modulens montering och koppla bort skärmar |
| Förblir gul | Fast gul | Operativsystemet startar inte, eller daemonen är inte installerad |
| Oväntad avstängning | Rullande grönt/gult | Spänningsbortfall upptäckt — kontrollera inspänningen |
| Överspänning | LED 1 blinkar rött | Inspänningen för hög (över 32 V) |
| Fel | Alla lysdioder blinkar rött | Hårdvarufel — kontakta tillverkaren |

!!! quote "Relaterad information"
    - **LED-mönster:** se [Status-LED:ar](./operation.md#status-ledar)
    - **Strömhantering:** se [Strömhantering och avstängning](./operation.md#stromhantering-och-avstangning)
    - **Hantering av daemonen:** se [Programvaruguiden](./software.md#halpi-daemon-halpid)
    - **Detaljer om CAN-gränssnittet:** se [Gränssnitt och anslutningar](./interfaces.md#can-fd-nmea-2000)
    - **Detaljer om RS-485-gränssnittet:** se [Gränssnitt och anslutningar](./interfaces.md#rs-485-nmea-0183)

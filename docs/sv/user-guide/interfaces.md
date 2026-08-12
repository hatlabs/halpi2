---
translated_from: 288cabc5149b6610fd3f280bfce455d945b6a356
---

# Gränssnitt och anslutningar

## CAN FD / NMEA 2000

HALPI2 har ett helt isolerat [CAN FD](https://en.wikipedia.org/wiki/CAN_FD)-gränssnitt som fungerar både för marina [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000)-nätverk och för fordons- och industritillämpningar. Gränssnittet ger snabb dataöverföring med fullständig elektrisk isolation och därmed god störningstålighet.

### Gränssnittets specifikationer

CAN FD-gränssnittet stöder både vanligt CAN och CAN FD. I NMEA 2000-bruk arbetar det i vanligt CAN-läge med standardhastigheten 250 kbit/s. I fordons- och industritillämpningar kan det utnyttja CAN FD:s fulla kapacitet med hastigheter upp till 8 Mbit/s.

På frontpanelen sitter en Micro-C-kontakt som är kompatibel med vanligt NMEA 2000-kablage och tillhörande komponenter. Enheten kan därmed anslutas direkt till befintliga marina nätverk med vanliga T-kopplingar och stickledningar.

### Strömförsörjning och belastning av nätverket

Hur mycket HALPI2 belastar NMEA 2000-nätverkets strömförsörjning beror på hur den matas. I standardutförandet, med extern matning via E7T-kontakten, tar enheten ingen ström från NMEA 2000-nätverket, och dess belastningstal (LEN) är därför 0.

När enheten matas från NMEA 2000-bussen måste strömuttaget begränsas till 0,9 A av den interna strömbegränsaren. Det motsvarar ett LEN-värde på 18. Anslut då enheten till nätverkets backbone nära matningspunkten, så att spänningsfallet blir litet och driften tillförlitlig.

### Hårdvarukonfiguration

Bärkortet har ett termineringsmotstånd på 120 Ω som kan kopplas in med en bygel. I NMEA 2000-tillämpningar ska terminering vid enheten undvikas, eftersom standarden inte tillåter det. I fordons- och industritillämpningar med punkt-till-punkt-förbindelse kan bygeln däremot sättas i.

För diagnostik och felsökning har bärkortet egna RX- och TX-lysdioder som visar trafiken på nätverket. De ger omedelbar återkoppling om sändning och mottagning, vilket gör det enklare att ringa in anslutningsproblem.

### Anslutning till nätverket

Anslutningen till ett NMEA 2000-nätverk görs med en vanlig T-koppling (medföljer ej) på nätverkets backbone och en stickledning mellan T-kopplingen och HALPI2:s Micro-C-kontakt.

### Programvaruintegration

CAN-gränssnittet integreras sömlöst i Linux via ramverket SocketCAN och visas som nätverksenheten `can0`. Tack vare detta standardgränssnitt kan du använda Linux vanliga CAN-verktyg för övervakning och diagnostik. Nätverksgränssnittet är förkonfigurerat i alla HALPI2:s systemavbilder (HaLOS, OpenPlotter och Raspberry Pi OS).

Integration med Signal K-servern finns i HaLOS Marine-avbilderna och i OpenPlotter: de hittar CAN-gränssnittet automatiskt och använder det för att behandla NMEA 2000-data. I HaLOS-avbilder som inte är marina kan Signal K installeras från Container Apps-butiken i Cockpit. Signal K-servern avkodar PGN-meddelanden och ger webbaserad åtkomst till nätverkets data i realtid.

### Felsökning

Felsökningen av nätverket börjar med RX/TX-lysdioderna på bärkortet. Vid normal drift blinkar de i takt med trafiken. Utebliven RX-aktivitet kan tyda på kabelproblem eller felaktig terminering, medan utebliven TX-aktivitet kan tyda på konflikter i nätverket eller på kablaget.

Med Linux-kommandot `candump` kan du följa CAN-bussen direkt från kommandoraden. Verktyget visar detaljerad information om alla meddelanden på bussen och möjliggör en grundlig diagnostik. I sin enklaste form:

```bash
candump can0
```

Det visar alla inkommande råa CAN-meddelanden i realtid.

Signal K-serverns instrumentpanel ger ytterligare övervakningsmöjligheter. Den visar NMEA 2000-datahastigheterna från CAN-gränssnittet i realtid, och med databläddraren kan du granska avkodade NMEA 2000-data.

!!! quote "Relaterad information"
    - **Konfiguration av strömförsörjningen:** se [Kom igång](../getting-started/getting-started.md#permanent-stromanslutning)
    - **Uppsättning av programvaran:** se [Programvaruguiden](./software.md)
    - **Felsökning av nätverket:** se [Felsökning](./troubleshooting.md)


## RS-485 (NMEA 0183)

HALPI2 har ett isolerat [RS-485](https://en.wikipedia.org/wiki/RS-485)-gränssnitt för seriell kommunikation med marina [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422]-nätverk och industritillämpningar.

[^rs422]: Strikt sett använder NMEA 0183 standarden RS-422, men RS-485 är bakåtkompatibel, så HALPI2 kan kommunicera med både RS-422- och RS-485-enheter.

### Gränssnittets specifikationer

RS-485-transceivern arbetar i hastigheter upp till 10 Mbit/s, även om typiska NMEA 0183-tillämpningar använder standardhastigheterna 4800 eller 38400 bit/s. Gränssnittet är galvaniskt isolerat och följer NMEA 0183-specifikationen; det skyddar HALPI2 mot jordslingor och de elektriska störningar som är vanliga i marin miljö.

Det är internt kopplat till Raspberry Pi:s UART 4 och visas i Linux som `/dev/ttyAMA4`. Den här vanliga serieporten kan användas av alla program som stöder seriell kommunikation, däribland Signal K-servern, OpenCPN och egna program.

### Hårdvarukonfiguration

Bärkortet har egna RX- och TX-lysdioder som visar trafiken på RS-485-gränssnittet. De ger omedelbar återkoppling under installation och felsökning och gör det enkelt att se att data sänds och tas emot korrekt.

Som allmänt RS-485-gränssnitt kan enheten ställas in på automatisk eller manuell sändningsaktivering. I manuellt läge styr ett GPIO-stift aktiveringssignalen, så att programvaran avgör när gränssnittet sänder och när det tar emot. Det behövs i tillämpningar med flera sändare, där gränssnittet måste vara passivt när det inte sänder. I automatiskt läge aktiverar hårdvaran signalen själv när data sänds, vilket förenklar uppsättningar med en enda sändare.

RS-485-gränssnittet stöder dessutom halv duplex, så att det kan både sända och ta emot på samma ledarpar.

Gränssnittet kan också stängas av helt genom hårdvarukonfiguration, om UART 4 behövs till något annat.

### Kablage och anslutning

RS-485-gränssnittet kräver en kabelgenomföring eller en panelkontakt, som användaren själv skaffar. Ett bra alternativ är [en SP13-panelkontakt med ledning](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). Gränssnittet är bakåtkompatibelt med RS-422-signaleringen i NMEA 0183 och stöder både RS-485-nätverk med flera sändare och RS-422-nätverk med en sändare och flera mottagare. Det använder balanserade differentialpar, märkta TX+/TX- och RX+/RX-.

### Programvaruintegration

I alla HALPI2-avbilder är RS-485-gränssnittet färdigt att använda. I HaLOS Marine-avbilderna och i OpenPlotter hittar Signal K-servern gränssnittet automatiskt och tar emot de NMEA 0183-data som sänds.

I egna tillämpningar beter sig gränssnittet som en vanlig serieport i Linux. Program kan öppna `/dev/ttyAMA4` och ställa in hastighet, databitar, stoppbitar och paritet enligt den anslutna utrustningens krav. Program i Python, Node.js och C/C++ når gränssnittet med vanliga bibliotek för seriell kommunikation.

### Vanliga tillämpningar

Ombord ansluts RS-485-gränssnittet vanligen till GPS-mottagare, ekolod, vindmätare, AIS-transpondrar eller andra enheter som använder NMEA 0183. I industrin kan det anslutas till programmerbara styrsystem, sensorer och annan automationsutrustning som använder Modbus RTU eller andra RS-485-protokoll.

Den höga hastigheten möjliggör också mindre vanliga användningar, som snabb insamling av sensordata eller egna överföringsprotokoll, vilket gör HALPI2 lämplig för forskningsfartyg och specialiserade övervakningsuppgifter.

!!! quote "Relaterad information"
    - **Konfiguration av programvaran:** se [Programvaruguiden](./software.md)
    - **Felsökning:** se [Felsökning](./troubleshooting.md)


## GNSS (GPS)

HALPI2 stöder GNSS-mottagare i form av HAT-kort anslutna till UART0 (`/dev/ttyAMA0`). Alla GNSS-mottagare på den porten fungerar med gpsd direkt.

För u-blox-mottagare (till exempel Max-M8Q) ger HaLOS Marine-avbilderna dessutom en automatisk konfiguration anpassad för marint bruk.

### Automatisk konfiguration (u-blox-mottagare)

I HaLOS Marine-avbilderna hittar och konfigurerar en systemd-tjänst (`configure-ublox-marine`) u-blox-mottagare automatiskt vid varje start:

| Parameter | Värde |
|:----------|:------|
| Hastighet | 115200 bit/s (fabriksvärde: 9600) |
| Uppdateringsfrekvens | 10 Hz (100 ms) |
| Dynamisk modell | Sea (anpassad för marint bruk) |

Konfigurationen körs vid varje start, eftersom ROM-baserade u-blox-moduler (som MAX-M8Q) saknar flashminne. Inställningarna sparas i batteribackat RAM (BBR), som kan tömmas när backupspänningen bryts — till exempel när enheten stått utan ström en längre tid. Omkonfigurationen sker obemärkt och förlänger gpsd:s start med ungefär 2 sekunder.

Om ingen mottagare hittas avslutas tjänsten utan meddelande. Ett nyinstallerat GNSS-HAT-kort konfigureras automatiskt vid nästa omstart.

### Åtkomst till data

GPS-data tillhandahålls av [gpsd](https://gpsd.io/) på TCP-port 2947. I HaLOS Marine-avbilderna ansluter Signal K automatiskt till gpsd — ingen ytterligare konfiguration behövs.

För diagnostik finns gpsd:s vanliga kommandoradsverktyg:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Andra avbilder än HaLOS

I Raspberry Pi OS eller andra operativsystem installerar och konfigurerar du gpsd för hand:

```bash
sudo apt install gpsd gpsd-clients
```

Redigera `/etc/default/gpsd` och sätt `DEVICES="/dev/ttyAMA0"`, och starta sedan om tjänsten. Mottagaren arbetar med sina fabriksinställningar (9600 bit/s, 1 Hz) tills den konfigurerats med `ubxtool` från paketet `gpsd-clients`.

!!! quote "Relaterad information"
    - **gpsd i HaLOS:** se [HaLOS GPS-dokumentation](https://docs.halos.fi/user-guide/gps/)
    - **Uppsättning av programvaran:** se [Programvaruguiden](./software.md)


## Ethernet

HALPI2 har ett gigabit-ethernetgränssnitt som ger snabb nätverksanslutning för dataöverföring, fjärråtkomst och anslutning till nätverk ombord. Ethernetporten på bärkortet är en vanlig RJ45-kontakt. Den är utförd till en panelkontakt dit en extern ethernetkabel kan anslutas.

## USB

HALPI2 har totalt fyra USB 3.0-portar av typ A för snabb anslutning av olika kringenheter. En port går direkt till CM5:ns USB 3.0-gränssnitt, medan de tre övriga går via en USB 3-hubb på kortet. I standardutförandet är två portar utförda till frontpanelen och två finns på bärkortet för interna anslutningar.

## HDMI

HALPI2 har två HDMI 2.0-portar (HDMI0 och HDMI1) för videoutgång. På bärkortet finns FFC-kontakter (böjlig flatkabel) för båda portarna. De är utförda till frontpanelen med specialtillverkade FFC-kablar. Kontakterna på frontpanelen är vanliga HDMI Type A-kontakter.

HALPI2:s HDMI-utgång klarar tillförlitligt två Full HD-videoströmmar (1080p). 4K-utgång kan fungera, men garanteras inte.

## MIPI (CSI/DSI)

Bärkortet har två MIPI CSI/DSI-kontakter för kameror och skärmar. Kontakterna är 22-poliga FFC-kontakter (böjlig flatkabel) med delningen 0,5 mm. De ska fungera som de är med nyare Raspberry Pi-kompatibla kameror och skärmar.

Av täthetsskäl bör FFC-kablar bara användas för interna anslutningar.

## Externa knappar

HALPI2:s bärkort har en 2×3-polig stiftlist för anslutning av externa knappar. Kapslingen har inga inbyggda knappar, vilket låter användaren välja placering och typ efter egna behov.

### Knappanslutningens stiftläge

Bärkortet har en 6-polig stiftlist med tre märkta knappfunktioner:

| Märkning | Funktion | Beskrivning |
|:---------|:---------|:------------|
| Reset | Reset av styrkretsen | Hårdvarureset (RP2040:s RUN-stift) |
| Power | Raspberry Pi:s strömknapp | CM5:ns strömknapp (ingången PWR_BUT) |
| User | Konfigurerbar av användaren | Användardefinierad händelse (ännu inte implementerad) |

Varje knapp använder två stift: ett för signalen och ett för jord. Använd slutande (NO) momentana tryckknappar som förbinder signalstiftet med jord när de trycks in.

### Knapparnas funktioner

**Reset-knappen:**
Reset-knappen utför en hårdvarureset genom att dra RP2040:s RUN-stift mot jord. Det återställer hela systemet: styrkretsen, CM5 och alla anslutna kringenheter. Knappen är särskilt användbar i nödlägen, när avstängning via programvaran har misslyckats och systemet inte längre svarar.

**Power-knappen:**
Power-knappen är kopplad direkt till CM5:ns strömknappsingång och fungerar precis som knappen på en Raspberry Pi 5. Ett dubbelklick begär en kontrollerad avstängning, så att operativsystemet hinner stänga program och avmontera filsystem innan spänningen bryts. Ett långt tryck tvingar fram omedelbar avstängning och bör bara användas när systemet inte svarar.

**User-knappen:**
Användarknappens funktion väntar fortfarande på implementation i programvaran och blir konfigurerbar i kommande firmwareversioner. När den är på plats är knappen avsedd för egna åtgärder och tillämpningsspecifika utlösare, där användaren själv bestämmer beteendet.

### Montering av knappar

#### Direkt montering i kapslingen

För direkt montering i HALPI2:s kapsling använder du de färdiga hålen på 6 mm eller 13 mm. Ta först bort motsvarande blindpluggar och montera en vattentät knapp som passar hålets diameter. Anslut knappen till bärkortets stiftlist med en lämplig kabel och se till att dragavlastningen och tätningen vid genomföringen blir ordentlig.

#### Montering på en separat panel

När knapparna monteras på en separat manöverpanel väljer du en plats som är lätt att nå och som behåller väderbeständigheten. Använd kabelgenomföringar vid kabelinföringarna och anslut knapparna med en förlängningskabel med ledare på 22–26 AWG. Håll den totala kabellängden under 3 meter för att bevara signalkvaliteten. I fuktiga eller tuffa miljöer använder du vattentäta kontakter vid skarvarna för att säkra en tillförlitlig drift över tid.

#### Anslutning

Alla knappanslutningar till bärkortet bör använda honkontakter med delningen 2,54 mm. Se till att stiften ligger rätt och att anslutningen sitter stadigt, så att kontaktproblem inte uppstår under drift.

!!! quote "Relaterad information"
    - **Strömhantering:** se [Bärkortets styrkrets](../technical-reference/controller.md)
    - **Åtkomst till hårdvaran:** se [Hårdvaruguiden](./hardware.md)

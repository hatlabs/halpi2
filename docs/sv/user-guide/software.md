---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Programvaruguide

## Systemavbilder

Hat Labs tillhandahåller färdiga avbilder för HALPI2. Alla innehåller den konfiguration och de anpassningar HALPI2-hårdvaran kräver: CAN (NMEA 2000) som nätverksenheten `can0`, RS-485 (NMEA 0183) som `/dev/ttyAMA4` samt paketet `halpi2-firmware`.

### HaLOS (standard)

[HaLOS](https://docs.halos.fi) är en containerbaserad Linux-distribution avsedd för marina och industriella tillämpningar. Den erbjuder ett webbgränssnitt för systemadministration, apphantering och övervakning — utan skärm, tangentbord eller VNC.

**Varianter av avbilden:**

| Avbild | Beskrivning |
|:-------|:------------|
| Halos-HALPI2 | Basavbild utan skärm, med Cockpit och containerhantering |
| Halos-HALPI2-Desktop | Basavbild med Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Utan skärm, med marina appar (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Skrivbord med marina appar |

Hämta HaLOS-avbilderna från [HaLOS releasesida](https://github.com/halos-org/halos-pi-gen/releases/latest). Utförlig dokumentation finns på [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter är en avbild baserad på Raspberry Pi OS med tillägg för marina tillämpningar. Den ger en klassisk skrivbordsmiljö med VNC-fjärråtkomst och har Signal K och OpenCPN förinstallerade.

Om du inte använder skärm, tangentbord och mus med HALPI2 kan du ansluta antingen med en ethernetkabel eller via WiFi-accesspunkten (`OpenPlotter`, lösenord `12345678`).

I båda fallen når du HALPI2-datorn med VNC eller SSH. För VNC behöver du RealVNC:s [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).

Eftersom både accesspunkten och standardanvändaren har standardlösenord är det nödvändigt att byta dem omedelbart efter första start. Hur det går till beskrivs i [OpenPlotters dokumentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Hämta OpenPlotter-avbilderna från [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS och Raspberry Pi OS Lite

Om du föredrar vanliga Raspberry Pi OS kan du hämta den senaste avbilden med HALPI2-stöd från [GitHub-repositoriet](https://github.com/hatlabs/openplotter-halpi/releases). Flasha avbilden till SSD-enheten med Raspberry Pi Imager. Under flashningen kan du göra anpassningar, som att sätta värdnamn, aktivera SSH och ställa in WiFi.

Om du hoppar över anpassningarna behöver du en skärm och ett tangentbord anslutna till HALPI2 för den första konfigurationen. Vid första start får du ange användarnamn och lösenord.


## Flasha en systemavbild till SSD-enheten

Det finns två sätt att flasha en systemavbild till HALPI2:s NVMe SSD: ta ut SSD-enheten och använda en USB-NVMe-adapter, eller flasha direkt på HALPI2. USB-NVMe-adaptern rekommenderas för enkelhetens skull — sådana adaptrar finns billigt på nätet och förfarandet är okomplicerat.

### Flasha med en USB-NVMe-adapter

Börja med att ta ut NVMe SSD-enheten ur HALPI2 enligt anvisningen i [Hårdvaruguiden](./hardware.md#byte-av-nvme-ssd). Hämta sedan en HALPI2-kompatibel avbild — antingen en [HaLOS-avbild](https://github.com/halos-org/halos-pi-gen/releases/latest) eller en [OpenPlotter- eller Raspberry Pi OS-avbild](https://github.com/hatlabs/openplotter-halpi/releases) — och se till att välja den som passar din användning.

Sätt in SSD-enheten i USB-NVMe-adaptern och anslut den till din dator. Flasha den hämtade avbilden till NVMe SSD-enheten med Raspberry Pi Imager. Om du flashar en Raspberry Pi OS-avbild kan du redigera och tillämpa systemets anpassningsinställningar under flashningen. Utan dessa anpassningar behöver du ett USB-tangentbord och en mus anslutna till HALPI2 för den första konfigurationen efter installationen.

När du använder HaLOS-avbilder ska anpassningsinställningarna **inte** tillämpas under flashningen. HaLOS konfigureras efter start via sitt webbgränssnitt.

På samma sätt ska anpassningsinställningarna **inte** tillämpas för OpenPlotter-avbilden. Konfigurationen görs efter första start med Raspberry Pi:s och OpenPlotters egna verktyg.

När flashningen är klar kopplar du bort adaptern och tar ut SSD-enheten. Sätt tillbaka den i HALPI2 enligt monteringsanvisningen i Hårdvaruguiden och stäng kapslingen enligt samma guide.

### Flasha direkt på HALPI2

Alternativt kan du flasha systemavbilden direkt på HALPI2 utan att ta ut SSD-enheten. Detta följer det vanliga förfarandet för att flasha en Compute Module, som beskrivs i [Raspberry Pi:s dokumentation](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Anvisningarna där gäller kortet CM5 IO Board, men förfarandet är likartat på HALPI2.

**Förutsättningar.** Installera verktyget `rpiboot` från Raspberry Pi:s [`usbboot`-repositorium](https://github.com/raspberrypi/usbboot). På Linux och macOS bygger och installerar du det från källkoden enligt repositoriets README; på Windows installerar du Raspberry Pi Imager eller det fristående installationsprogrammet för `rpiboot` som är länkat från samma sida.

Så förbereder du HALPI2 för flashning via USB:

1. Stäng av systemet helt och öppna kapslingens lock enligt anvisningen i [Hårdvaruguiden](./hardware.md#atkomst-till-kapslingen).
2. Leta upp USB-C-kontakten märkt ”USB Boot” till höger om HAT-området på bärkortet och ställ startlägesomkopplaren bredvid i läget ”Abnormal”. (Någon lysdiodåterkoppling finns ännu inte — enheten är spänningslös.)
3. Anslut en USB-kabel mellan din dator och USB Boot-kontakten på HALPI2 och slå på enheten igen. En bärnstensfärgad lysdiod tänds nu bredvid omkopplaren och bekräftar USB-startläget.
4. Kör `rpiboot` på din dator. Verktyget hittar HALPI2 och läser in masslagringsfirmwaren, varefter HALPI2 visas som en USB-masslagringsenhet.
5. När `rpiboot` är klart och masslagringsenheten dyker upp ställer du tillbaka startlägesomkopplaren i läget ”Normal”. Det avbryter inte flashningen och gör att HALPI2 startar normalt från den nyss flashade avbilden efter nästa strömcykel. Om omkopplaren står kvar på ”Abnormal” går enheten in i USB-startläge igen vid nästa start i stället för att starta det nya systemet.
6. Flasha systemavbilden med Raspberry Pi Imager (eller ett annat verktyg som kan skriva till en blockenhet) till den nya masslagringsenheten.
7. När flashningen är klar kopplar du bort USB-kabeln, bryter och återansluter strömmen till HALPI2 och stänger kapslingen.

!!! tip "Starta om utan att dra ur strömmen"
    När kapslingen redan är öppen är det snabbaste sättet att starta om HALPI2 att kortvarigt kortsluta de två nedersta stiften på knappanslutningen bredvid USB-C-uttaget. Att röra vid båda stiften samtidigt med metallhöljet på en USB-C-kontakt fungerar bra och är ofarligt.

## Första konfigurationen av systemet

När HALPI2 har flashats och startats för första gången krävs några steg för säker och korrekt drift.

### Konfiguration av HaLOS

HaLOS konfigureras helt via sitt webbgränssnitt. Efter första start når du Cockpit på `https://halos.local:9090/` och instrumentpanelen på `https://halos.local/`. Byt standardlösenorden omedelbart — se guiden [Kom igång](../getting-started/getting-started.md#konfiguration-vid-forsta-start) och [HaLOS dokumentation](https://docs.halos.fi/getting-started/first-boot/).

### Konfiguration av OpenPlotter

Med OpenPlotter-avbilden startar systemet med standardlösenord både för WiFi-accesspunkten och för standardanvändarkontot. Av säkerhetsskäl är det nödvändigt att byta dem omedelbart efter första start.

Byte av lösenord och den första konfigurationen beskrivs i guiden [Kom igång](../getting-started/getting-started.md#konfiguration-vid-forsta-start) och i [OpenPlotters dokumentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Konfiguration av Raspberry Pi OS

Om du har valt vanliga Raspberry Pi OS i stället för OpenPlotter följer du Raspberry Pi:s vanliga konfigurationsflöde som visas vid första start. Guiden hjälper dig att skapa användarkonton, sätta lösenord, ställa in WiFi och aktivera nödvändiga tjänster som SSH för fjärråtkomst.

Under den första konfigurationen bör du också ställa in tidszon, tangentbordslayout och andra regionala inställningar så att de passar din miljö. Raspberry Pi:s konfigurationsverktyg (`raspi-config`) ger tillgång till fler systeminställningar som kan ändras efteråt.

## Fjärråtkomst

HALPI2 stöder flera sätt att komma åt systemet på distans, så att du kan övervaka och styra det utan fysisk åtkomst till enheten. Det är särskilt värdefullt när HALPI2 är monterad utan skärm på ett svåråtkomligt ställe.

### Webbåtkomst (HaLOS)

HaLOS ger ett komplett webbaserat administrationsgränssnitt utan extra programvara:

- **Instrumentpanel** (`https://halos.local/`): Homarr-instrumentpanelen ger tillgång till alla installerade appar, däribland Signal K, Grafana och andra marina appar.
- **Cockpit** (`https://halos.local:9090/`): systemadministration med terminalåtkomst, programvaruuppdateringar, nätverkskonfiguration och hantering av containerappar.

### SSH (Secure Shell)

SSH ger säker kommandoradsåtkomst till HALPI2, så att du kan köra kommandon, överföra filer och sköta systemadministration på distans. SSH är aktiverat som standard i HaLOS-avbilder utan skärm och i OpenPlotter. I HaLOS Desktop-varianterna och i Raspberry Pi OS aktiverar du det med `raspi-config`.

För att ansluta med SSH använder du en SSH-klient, till exempel den inbyggda terminalen i macOS och Linux eller ett program som PuTTY i Windows. Grundkommandot är:

```bash
ssh username@halpi2-ip-address
```

SSH-anslutningar är krypterade och säkra, och lämpar sig därför även för publika nät när autentiseringen är rätt uppsatt. De kräver dessutom mycket lite bandbredd, vilket gör dem idealiska för fjärråtkomst över långsamma förbindelser med hög fördröjning.

### VNC (Virtual Network Computing)

!!! note
    VNC gäller endast avbilderna OpenPlotter och Raspberry Pi OS Desktop. HaLOS använder webbåtkomst i stället — se ovan.

VNC ger fjärråtkomst till HALPI2:s grafiska gränssnitt, så att du kan använda skrivbordet som om du satt vid enheten. VNC är förinstallerat och förkonfigurerat i OpenPlotter-avbilderna. I en Raspberry Pi OS-installation aktiverar du det med konfigurationsverktyget `raspi-config`.

För att nå HALPI2:s skrivbord på distans använder du RealVNC:s [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/), som finns för Windows, macOS, Linux, iOS och Android. VNC fungerar bra i lokala nät och utan internetuppkoppling, vilket gör det lämpligt för båtinstallationer där internet kan vara begränsat eller saknas.

För fjärråtkomst över internet kräver VNC extra nätverkskonfiguration, som portvidarebefordran eller VPN, eftersom protokollet inte i sig tar sig igenom brandväggar och NAT-enheter.

### Raspberry Pi Connect

Raspberry Pi Connect erbjuder ett modernt webbaserat sätt att nå skrivbordet på distans: du ansluter med en vanlig webbläsare, utan att installera någon extra programvara. Tjänsten tar sig automatiskt igenom brandväggar och NAT, vilket gör den särskilt lämplig för fjärråtkomst över internet utan komplicerad nätverkskonfiguration.

Till skillnad från VNC sköter Raspberry Pi Connect nätverksdetaljerna själv och ger enkel åtkomst varhelst det finns internet. Den kräver dock att HALPI2 själv har en aktiv internetuppkoppling.

## Programvaruuppdateringar

Regelbundna uppdateringar rekommenderas för att bevara systemets prestanda och säkerhet.

### Uppdateringar i HaLOS

I HaLOS uppdateras systempaketen (inklusive HALPI2:s firmware) via Cockpit eller från kommandoraden med `apt`. Containerbaserade appar (Signal K, Grafana med flera) uppdateras via Container Apps-vyn i Cockpit, som letar efter nya versioner av containeravbilderna.

### Uppdateringar från kommandoraden (alla avbilder)

Det mest tillförlitliga sättet är kommandoraden. Öppna en terminal och kör:

```bash
sudo apt update
sudo apt upgrade
```

Det första kommandot (`apt update`) uppdaterar paketdatabasen med de senaste tillgängliga versionerna, och det andra (`apt upgrade`) hämtar och installerar alla tillgängliga uppdateringar. Det uppdaterar samtliga installerade paket, inklusive grundsystemet Raspberry Pi OS, OpenPlotters komponenter och HALPI2:s egen programvara.

Under uppdateringen kan du bli ombedd att bekräfta installationen av vissa paket eller omstart av tjänster. Det är i regel säkert att godta, om du inte har särskilda skäl att avstå.

### Grafiska uppdateringar

För dig som föredrar ett grafiskt gränssnitt visar skrivbordet en avisering när uppdateringar finns. En nedladdningsikon dyker upp i aktivitetsfältets övre högra hörn när uppdateringar är redo att installeras. Ett klick på ikonen öppnar uppdateringshanteraren, där du kan gå igenom och installera de tillgängliga uppdateringarna.

## Firmwareuppdateringar

HALPI2:s styrkretsfirmware uppdateras via Raspberry Pi OS vanliga uppdateringsflöde, vilket gör det till en integrerad och friktionsfri åtgärd. Regelbundna firmwareuppdateringar är viktiga för prestanda, för nya funktioner och för kompatibiliteten med programvara som utvecklas.

### Automatiska firmwareuppdateringar

Firmwareuppdateringar distribueras via det vanliga systemuppdateringsflödet, som Debian-paket i ett APT-paketförråd. För att söka efter och installera dem öppnar du en terminal och kör:

```bash
sudo apt update
sudo apt upgrade
```

När ny HALPI2-firmware finns hämtas och installeras den automatiskt som en del av uppdateringen. Systemet meddelar dig om firmwareuppdateringar ingår bland de tillgängliga paketen.

När firmwarepaketet har uppdaterats måste systemet startas om på rätt sätt för att ändringarna ska träda i kraft. Använd avstängningskommandot för att säkerställa en fullständig strömcykel:

```bash
sudo shutdown -h now
```

**Viktigt:** En vanlig omstart räcker inte för firmwareuppdateringar. En fullständig avstängning följd av start krävs, eftersom det är då styrkretsen startar om och tar den nya firmwaren i bruk. Styrkretsens firmware uppdateras bara vid påslagning.

### Firmwarens säkerhetsfunktioner

HALPI2 har inbyggda skydd mot skadad firmware. Om enheten startas om inom 30 sekunder efter en firmwareuppdatering återgår systemet automatiskt till den föregående firmwareversionen. Det skyddar mot problematiska uppdateringar som annars kunde hindra normal drift.

### Installera firmware manuellt

För erfarna användare eller i vissa felsökningssituationer kan firmwaren installeras manuellt med kommandoradsverktyget HALPI. Firmwarefilerna ligger i katalogen `/usr/share/halpi2-firmware/` och kan flashas direkt:

```bash
halpi flash <firmware_file>.bin
```

### Stänga av automatiska firmwareuppdateringar

Ibland vill man stanna kvar på en viss firmwareversion och stänga av de automatiska uppdateringarna. Det gör du genom att redigera HALPI2:s konfigurationsfil:

```bash
sudo nano /etc/halpid/firmware.conf
```

Leta upp inställningen `AUTO_FLASH_ON_INSTALL` och sätt den till `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Spara filen och avsluta redigeraren. HALPI2 flashar då inte längre ny firmware automatiskt vid vanliga uppdateringar, och du bestämmer själv när det ska ske. Firmwareuppdateringar kan fortfarande installeras manuellt med `halpi flash`.


## Kommandoradsverktyget HALPI

HALPI2:s programvarugränssnitt består av tjänsten `halpid` och kommandoradsverktyget `halpi`. Tillsammans ger de övervakning, konfiguration och styrning av systemet.

### HALPI-daemon (`halpid`)

HALPI-daemonen körs som en systemtjänst och sköter kommunikationen mellan operativsystemet och HALPI2:s styrkrets. Den möjliggör co-op-läget med full övervakning och strömhantering.

#### Hantering av tjänsten

Daemonen styrs via systemd:

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

Daemonens konfiguration ligger i `/etc/halpid/halpid.conf`. För att redigera den:

```bash
sudo nano /etc/halpid/halpid.conf
```

Ändringar kräver att daemonen startas om:

```bash
sudo systemctl restart halpid
```

### Kommandoradsverktyget HALPI (`halpi`)

Kommandot `halpi` ger direkt tillgång till styrkretsens funktioner och systemets tillstånd. Det kommunicerar med daemonen för att köra kommandon och hämta uppgifter om HALPI2:s driftstillstånd, konfiguration och hårdvaruvärden.

#### Systemtillstånd och övervakning

Kommandoradsverktygets huvuduppgift är att ge en heltäckande bild av systemets tillstånd: hårdvaruvärden, driftstillstånd och övervakningsdata i realtid.

Visa systemets tillstånd:

```bash
# Display comprehensive system status
halpi status
```

Kommandot ger en fullständig översikt över HALPI2:s aktuella driftstillstånd, inklusive spänningar, strömförbrukning, temperaturer och styrkretsens status:

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

Om du bara vill följa ett enskilt värde hämtar du det så här:

```bash
# Show controller firmware version
halpi get firmware_version
```

För skript är REST-gränssnittet lämpligare; det beskrivs i avsnittet [Åtkomst via REST-API:et](#atkomst-via-rest-apiet).

#### Hantering av konfigurationen

Med kommandoradsverktyget HALPI kan du se de aktuella inställningarna och ändra driftsparametrarna.

Visa nuvarande konfiguration:

```bash
# Show current configuration
halpi config
```

Det visar alla konfigurerbara parametrar och deras aktuella värden:

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

#### Styrning av lysdioderna

En av de inställningar som ändras oftast är lysdiodernas ljusstyrka, som går att anpassa till miljön och egna önskemål.

Exempel på kommandon för ljusstyrkan:

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

Ljusstyrkan tar värden från 0 (helt släckt) till 255 (maximal ljusstyrka), vilket ger en fin justering av lysdioderna på frontpanelen.

#### Strömhantering

Kommandoradsverktyget HALPI ger de strömhanteringsfunktioner som behövs för säker drift.

Exempel:

```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

Avstängningskommandot ser till att systemet stängs av säkert: operativsystemet hinner stänga program och avmontera filsystem innan styrkretsen bryter spänningen.

#### Åtkomst via REST-API:et

För erfarna användare och egna program erbjuder HALPI-daemonen även ett REST-gränssnitt via en Unix-socket. Det ger snabbare programmatisk åtkomst till systemets data:

Några användningsexempel:

```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

REST-gränssnittet är särskilt användbart för övervakningsprogram, system för datalagring eller annan programvara som behöver läsa HALPI2:s tillstånd i realtid.

Den fullständiga beskrivningen av REST-API:et finns i kapitlet [Programvaruutveckling: HALPI2-daemon](../software-development/daemon.md).

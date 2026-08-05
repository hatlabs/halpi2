---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Softwarehandleiding

## Systeemimages

Hat Labs levert kant-en-klare images voor de HALPI2. Alle images bevatten de benodigde configuratie en aanpassingen voor de HALPI2-hardware, waaronder CAN (NMEA 2000) als netwerkapparaat `can0`, RS-485 (NMEA 0183) als `/dev/ttyAMA4` en het pakket `halpi2-firmware`.

### HaLOS (standaard)

[HaLOS](https://docs.halos.fi) is een containergebaseerde Linux-distributie voor maritieme en industriële toepassingen. Het biedt een webinterface voor systeembeheer, applicatiebeheer en bewaking — zonder beeldscherm, toetsenbord of VNC.

**Imagevarianten:**

| Image | Beschrijving |
|:------|:------------|
| Halos-HALPI2 | Basisimage zonder beeldscherm (headless), met Cockpit en containerbeheer |
| Halos-HALPI2-Desktop | Basisimage met Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Zonder beeldscherm, met maritieme apps (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Desktop met maritieme apps |

Download HaLOS-images van de [releasepagina van HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest). Zie voor uitgebreide documentatie [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter is een image op basis van Raspberry Pi OS met uitbreidingen voor maritieme toepassingen. Het biedt een traditionele desktopomgeving met VNC-toegang op afstand en wordt geleverd met Signal K en OpenCPN voorgeïnstalleerd.

Als u de HALPI2 zonder beeldscherm, toetsenbord en muis gebruikt, kunt u verbinding maken met de computer via een ethernetkabel of via het wifi-accesspoint (`OpenPlotter`, wachtwoord `12345678`).

In beide gevallen kunt u de HALPI2-computer benaderen met VNC of SSH. Om VNC te gebruiken moet u [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) van RealVNC downloaden.

Omdat zowel het accesspoint als de standaardgebruiker met standaardwachtwoorden worden geleverd, is het absoluut noodzakelijk dat de wachtwoorden onmiddellijk na de eerste start worden gewijzigd. De procedure staat beschreven in de [OpenPlotter-documentatie](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Download OpenPlotter-images van [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS en Raspberry Pi OS Lite

Als u liever het standaard Raspberry Pi OS gebruikt, kunt u het nieuwste image
met HALPI2-ondersteuning downloaden van [de GitHub-repository](https://github.com/hatlabs/openplotter-halpi/releases).
Flash het image met Raspberry Pi Imager naar de SSD. Tijdens het flashen kunt u
aanpassingen toepassen, zoals het instellen van de hostnaam, het inschakelen van
SSH en het configureren van wifi.

Als u ervoor kiest geen aanpassingen toe te passen, moet er een beeldscherm en
toetsenbord op de HALPI2 zijn aangesloten om de eerste installatie te voltooien.
Bij de eerste start wordt om een gebruikersnaam en wachtwoord gevraagd.


## Een systeemimage naar de SSD flashen

Er zijn twee methoden beschikbaar om een systeemimage naar de NVMe SSD van de HALPI2 te flashen: de SSD verwijderen en een USB-NVMe-adapter gebruiken, of rechtstreeks op de HALPI2-unit flashen. De methode met de USB-NVMe-adapter wordt aanbevolen vanwege het gemak: dergelijke adapters zijn online tegen lage kosten verkrijgbaar en bieden een eenvoudig flashproces.

### Flashen met een USB-NVMe-adapter

Om het image met de USB-NVMe-adaptermethode te flashen, verwijdert u eerst de NVMe SSD uit de HALPI2-unit volgens de procedure in de [Hardwarehandleiding](./hardware.md#de-nvme-ssd-vervangen). Download vervolgens een HALPI2-compatibel image — een [HaLOS-image](https://github.com/halos-org/halos-pi-gen/releases/latest) of een [OpenPlotter- of Raspberry Pi OS-image](https://github.com/hatlabs/openplotter-halpi/releases) — en let erop dat u het juiste image voor het beoogde gebruik kiest.

Plaats de SSD in de USB-NVMe-adapter en sluit deze aan op uw computer. Gebruik Raspberry Pi Imager om het gedownloade image naar de NVMe SSD te flashen. Als u een Raspberry Pi OS-image flasht, kunt u tijdens het flashen desgewenst de aanpassingsinstellingen van het besturingssysteem bewerken en toepassen. Worden er geen aangepaste instellingen toegepast, dan zijn er na de installatie een USB-toetsenbord en een USB-muis op de HALPI2 nodig voor de eerste installatie.

Bij HaLOS-images mogen de aanpassingsinstellingen van het besturingssysteem tijdens het flashen **niet** worden toegepast. HaLOS wordt na het opstarten via de webinterface geconfigureerd.

Hetzelfde geldt voor het OpenPlotter-image: de aanpassingsinstellingen van het besturingssysteem mogen tijdens het flashen **niet** worden toegepast. De configuratie gebeurt in plaats daarvan na de eerste start met de configuratiegereedschappen van Raspberry Pi en OpenPlotter.

Zodra het flashen voltooid is, koppelt u de adapter los en verwijdert u de SSD. Plaats de SSD terug in de HALPI2-unit volgens de installatieprocedure in de Hardwarehandleiding en monteer daarna de behuizing weer volgens dezelfde handleiding.

### Rechtstreeks op de HALPI2 flashen

Het systeemimage kan ook rechtstreeks op de HALPI2 worden geflasht, zonder de SSD te verwijderen. Deze methode volgt de standaard flashprocedure voor de Compute Module, zoals beschreven in de [Raspberry Pi-documentatie](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). De instructies voor de boardopstelling daar zijn geschreven voor het CM5 IO Board, maar het proces is vergelijkbaar voor de HALPI2.

**Vereisten.** Installeer het gereedschap `rpiboot` uit de [`usbboot`-repository](https://github.com/raspberrypi/usbboot) van Raspberry Pi. Bouw en installeer het op Linux en macOS vanaf de broncode, zoals beschreven in de README van de repository; installeer op Windows de Raspberry Pi Imager of het losse installatieprogramma voor `rpiboot` waarnaar op dezelfde pagina wordt verwezen.

De HALPI2 voorbereiden op flashen via USB:

1. Schakel het systeem volledig uit en open het deksel van de behuizing volgens de procedure in de [Hardwarehandleiding](./hardware.md#toegang-tot-de-behuizing).
2. Zoek de USB-C-connector met het opschrift “USB Boot” rechts van de HAT-omtrek op het carrierboard en zet de bootmodusschakelaar ernaast in de stand “Abnormal”. (Er is nog geen terugkoppeling via leds — het apparaat is spanningsloos.)
3. Sluit een USB-kabel aan tussen uw computer en de USB-bootconnector op de HALPI2 en schakel het apparaat weer in. Een amberkleurige led naast de bootmodusschakelaar gaat nu branden, wat bevestigt dat de HALPI2 in de USB-bootmodus staat.
4. Voer op uw computer `rpiboot` uit. Het gereedschap detecteert de HALPI2 en laadt de firmware voor de massaopslag-gadget; daarna verschijnt de HALPI2 als USB-massaopslagapparaat.
5. Zodra `rpiboot` is geslaagd en het massaopslagapparaat verschijnt, zet u de bootmodusschakelaar terug in de stand “Normal”. Dit onderbreekt de flashsessie niet en zorgt ervoor dat de HALPI2 na de volgende in- en uitschakelcyclus normaal opstart vanaf het pas geflashte image. Blijft de schakelaar in de stand “Abnormal” staan, dan gaat het apparaat bij de volgende start opnieuw in de USB-bootmodus in plaats van het nieuwe besturingssysteem te starten.
6. Flash het systeemimage met Raspberry Pi Imager (of met een ander gereedschap dat naar een blockdevice kan schrijven), met het nieuwe massaopslagapparaat als doel.
7. Koppel na het flashen de USB-kabel los, schakel de HALPI2 uit en weer in en sluit de behuizing.

!!! tip "In- en uitschakelen zonder de stekker los te nemen"
    Met de behuizing al open is de snelste manier om de HALPI2 opnieuw op te starten het kortsluiten van de twee onderste pinnen van de Button Headers naast de USB-C-aansluiting. Beide pinnen tegelijk aanraken met de metalen behuizing van een USB-C-kabelconnector werkt goed en is veilig.

## Eerste systeemconfiguratie

Nadat u de HALPI2 met succes hebt geflasht en voor het eerst hebt opgestart, zijn er enkele configuratiestappen nodig om een veilige en correcte werking van het systeem te waarborgen.

### HaLOS-configuratie

HaLOS wordt volledig via de webinterface geconfigureerd. Open na de eerste start Cockpit op `https://halos.local:9090/` en het dashboard op `https://halos.local/`. Wijzig de standaardwachtwoorden onmiddellijk — zie de handleiding [Aan de slag](../getting-started/getting-started.md#configuratie-bij-de-eerste-start) en de [HaLOS-documentatie](https://docs.halos.fi/getting-started/first-boot/) voor details.

### OpenPlotter-configuratie

Bij het OpenPlotter-image start het systeem op met standaardwachtwoorden voor zowel het wifi-accesspoint als het standaard gebruikersaccount. Om veiligheidsredenen is het absoluut noodzakelijk dat deze wachtwoorden onmiddellijk na de eerste start worden gewijzigd.

De procedure voor het wijzigen van de wachtwoorden en de eerste configuratie staan beschreven in de handleiding [Aan de slag](../getting-started/getting-started.md#configuratie-bij-de-eerste-start) en in de [OpenPlotter-documentatie](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Raspberry Pi OS-configuratie

Als u ervoor hebt gekozen het standaard Raspberry Pi OS te gebruiken in plaats van OpenPlotter, volgt u de standaard installatieprocedure van Raspberry Pi die bij de eerste start wordt getoond. Deze installatiewizard leidt u door het aanmaken van gebruikersaccounts, het instellen van wachtwoorden, het configureren van wifi-verbindingen en het inschakelen van essentiële diensten zoals SSH voor toegang op afstand.

Tijdens de eerste installatie wilt u mogelijk ook de tijdzone, de toetsenbordindeling en andere regionale voorkeuren instellen die bij uw gebruiksomgeving passen. Het configuratiegereedschap van Raspberry Pi (`raspi-config`) geeft toegang tot aanvullende systeeminstellingen die na de eerste installatie kunnen worden aangepast.

## Toegang op afstand

De HALPI2 ondersteunt meerdere methoden voor toegang op afstand, waarmee u het systeem kunt bewaken en bedienen zonder fysieke toegang tot het apparaat. Dat is vooral waardevol bij installaties waarbij de HALPI2 zonder beeldscherm op een moeilijk bereikbare plaats is gemonteerd.

### Webgebaseerde toegang (HaLOS)

HaLOS biedt een volledige webgebaseerde beheerinterface waarvoor geen extra software nodig is:

- **Dashboard** (`https://halos.local/`): het Homarr-dashboard geeft toegang tot alle geïnstalleerde applicaties, waaronder Signal K, Grafana en andere maritieme apps.
- **Cockpit** (`https://halos.local:9090/`): systeembeheer met onder meer terminaltoegang, software-updates, netwerkconfiguratie en beheer van containerapps.

### SSH (Secure Shell)

SSH biedt beveiligde toegang tot de opdrachtregel van het HALPI2-systeem, waarmee u opdrachten kunt uitvoeren, bestanden kunt overdragen en systeembeheertaken op afstand kunt uitvoeren. SSH staat standaard aan op de HaLOS-images zonder beeldscherm en op OpenPlotter. Op de HaLOS Desktop-varianten en op Raspberry Pi OS kan SSH worden ingeschakeld met `raspi-config`.

Gebruik voor een SSH-verbinding een SSH-client, zoals de ingebouwde terminal op macOS- en Linux-systemen of een applicatie als PuTTY op Windows. De basisopdracht voor de verbinding is:

```bash
ssh username@halpi2-ip-address
```

SSH-verbindingen zijn versleuteld en veilig, waardoor ze bij een goede configuratie met sterke authenticatie ook over openbare netwerken bruikbaar zijn. Bovendien vergt SSH zeer weinig bandbreedte, wat het ideaal maakt voor toegang op afstand over trage verbindingen met een hoge latentie.

### VNC (Virtual Network Computing)

!!! note
    VNC is alleen van toepassing op de OpenPlotter- en Raspberry Pi OS Desktop-images. HaLOS gebruikt in plaats daarvan webgebaseerde toegang — zie hierboven.

VNC biedt toegang op afstand tot de grafische omgeving van de HALPI2, zodat u met de desktopomgeving kunt werken alsof u fysiek bij het apparaat aanwezig bent. Op OpenPlotter-images is VNC voorgeïnstalleerd en voorgeconfigureerd. Bij installaties van Raspberry Pi OS kan VNC worden ingeschakeld met het configuratiegereedschap `raspi-config`.

Gebruik voor toegang op afstand tot de HALPI2-desktop de applicatie [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) van RealVNC, die beschikbaar is voor Windows, macOS, Linux, iOS en Android. VNC werkt goed op lokale netwerken en in offlineomgevingen, wat het ideaal maakt voor installaties aan boord waar de internetverbinding beperkt of niet beschikbaar is.

Voor toegang op afstand via internet vereist VNC aanvullende netwerkconfiguratie, zoals port forwarding of een VPN, omdat het protocol firewalls en NAT-apparaten niet uit zichzelf passeert.

### Raspberry Pi Connect

Raspberry Pi Connect biedt een moderne, webgebaseerde manier van desktoptoegang op afstand: u verbindt met de HALPI2-desktop via een gewone webbrowser, zonder extra software te installeren. Deze dienst werkt automatisch door firewall- en NAT-configuraties heen, wat hem bijzonder geschikt maakt voor toegang op afstand via internet zonder ingewikkelde netwerkinstellingen.

Anders dan VNC handelt Raspberry Pi Connect de netwerkcomplexiteit automatisch af en biedt zo naadloze toegang vanaf elke plek met een internetverbinding. Wel vereist de dienst dat de HALPI2 zelf een actieve internetverbinding heeft.

## Software-updates

Regelmatige updates worden aanbevolen om de prestaties en de veiligheid van het systeem op peil te houden.

### HaLOS-updates

Op HaLOS worden systeempakketten (inclusief de HALPI2-firmware) bijgewerkt via Cockpit of vanaf de opdrachtregel met `apt`. Containergebaseerde applicaties (Signal K, Grafana enzovoort) worden bijgewerkt via de Container Apps-interface van Cockpit, die controleert op nieuwe versies van containerimages.

### Updates via de opdrachtregel (alle images)

De betrouwbaarste manier om het systeem bij te werken is via de opdrachtregel. Open een terminalvenster en voer de volgende opdrachten uit om het systeem bij te werken:

```bash
sudo apt update
sudo apt upgrade
```

De eerste opdracht (`apt update`) ververst de pakketdatabase met de nieuwste beschikbare versies; de tweede opdracht (`apt upgrade`) downloadt en installeert alle beschikbare updates. Dit proces werkt alle geïnstalleerde pakketten bij, inclusief het onderliggende Raspberry Pi OS, de OpenPlotter-onderdelen en de HALPI2-specifieke software.

Tijdens het bijwerken wordt u mogelijk gevraagd de installatie van bepaalde pakketten te bevestigen of diensten opnieuw te starten. Het is doorgaans veilig om daarmee in te stemmen, tenzij u specifieke redenen hebt om dat niet te doen.

### Grafische updates

Voor wie liever een grafische interface gebruikt, geeft de desktopomgeving een visuele melding wanneer er updates beschikbaar zijn. Er verschijnt dan een downloadpictogram rechtsboven in de taakbalk van het bureaublad. Door op dit pictogram te klikken opent u het updatebeheer, dat een gebruiksvriendelijke interface biedt om beschikbare updates te bekijken en te installeren.

## Firmware-updates

De controllerfirmware van de HALPI2 kan worden bijgewerkt via het standaard updateproces van Raspberry Pi OS, wat een naadloze en geïntegreerde aanpak biedt om de firmware actueel te houden. Regelmatige firmware-updates zijn belangrijk voor optimale prestaties, toegang tot nieuwe functies en compatibiliteit met de zich ontwikkelende softwareonderdelen.

### Automatische firmware-updates

Firmware-updates worden geleverd via het standaard mechanisme voor systeemupdates: Debian-pakketten in een APT-repository. Open een terminalvenster en voer de volgende opdrachten uit om te controleren op firmware-updates en deze te installeren:

```bash
sudo apt update
sudo apt upgrade
```

Wanneer er nieuwe HALPI2-firmware beschikbaar is, wordt deze automatisch gedownload en geïnstalleerd als onderdeel van het upgradeproces. Het systeem meldt het wanneer er firmware-updates bij de beschikbare pakketten zitten.

Nadat het firmwarepakket is bijgewerkt, is het essentieel om het systeem op de juiste manier opnieuw te starten om de firmwarewijzigingen toe te passen. Gebruik de shutdown-opdracht om een volledige in- en uitschakelcyclus te garanderen:

```bash
sudo shutdown -h now
```

**Belangrijk:** het systeem alleen opnieuw opstarten is niet voldoende voor firmware-updates. Een volledige afsluiting en herstart is nodig, omdat de controller daardoor opnieuw start en de nieuwe firmware toepast. De controllerfirmware wordt uitsluitend tijdens de inschakelsequentie bijgewerkt.

### Veiligheidsvoorzieningen van de firmware

De HALPI2 heeft ingebouwde veiligheidsmechanismen die beschermen tegen beschadigde firmware. Wordt het apparaat binnen 30 seconden na het toepassen van een firmware-update opnieuw gestart, dan valt het systeem automatisch terug op de vorige firmwareversie. Deze voorziening beschermt tegen problematische firmware-updates die de normale werking zouden kunnen verhinderen.

### Firmware handmatig installeren

Voor gevorderde gebruikers of specifieke probleemsituaties kan de firmware handmatig worden geïnstalleerd met het HALPI-opdrachtregelgereedschap. Firmwarebestanden staan in de map `/usr/share/halpi2-firmware/` en kunnen rechtstreeks worden geflasht met:

```bash
halpi flash <firmware_file>.bin
```

### Automatische firmware-updates uitschakelen

Sommige gebruikers willen automatische firmware-updates uitschakelen om op een bepaalde firmwareversie te blijven. Dat kan door het configuratiebestand van de HALPI2 te bewerken:

```bash
sudo nano /etc/halpid/firmware.conf
```

Zoek de instelling `AUTO_FLASH_ON_INSTALL` op en wijzig deze in `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Sla het bestand op en sluit de editor. Deze configuratiewijziging voorkomt dat de HALPI2 tijdens het standaard updateproces automatisch nieuwe firmware flasht, waarmee u volledige controle hebt over het moment waarop firmware-updates worden toegepast. Handmatig installeren van firmware-updates met de opdracht `halpi flash` blijft desgewenst gewoon mogelijk.


## HALPI-opdrachtregelgereedschap

De software-interface van de HALPI2 bestaat uit de daemon `halpid` en het opdrachtregelgereedschap `halpi`. Samen bieden zij systeembewaking, configuratie en besturing.

### HALPI-daemon (`halpid`)

De HALPI-daemon draait als systeemdienst en verzorgt de communicatie tussen het besturingssysteem en de HALPI2-controller. Hij maakt werking in de co-opmodus mogelijk, met volledige bewaking en energiebeheer.

#### Dienstbeheer

De daemon wordt beheerd via systemd:

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

#### Configuratie

De configuratie van de daemon staat in `/etc/halpid/halpid.conf`. Gebruik het volgende om de configuratie te bewerken:

```bash
sudo nano /etc/halpid/halpid.conf
```

Configuratiewijzigingen vereisen een herstart van de daemon:

```bash
sudo systemctl restart halpid
```

### HALPI-opdrachtregelgereedschap (`halpi`)

De opdracht `halpi` geeft rechtstreeks toegang tot de controllerfuncties en de systeemstatus. Hij communiceert met de daemon om opdrachten uit te voeren en informatie op te vragen over de bedrijfstoestand, de configuratie en de hardwareparameters van de HALPI2.

#### Systeemstatus en bewaking

De belangrijkste functie van het HALPI-opdrachtregelgereedschap is het geven van uitgebreide informatie over de systeemstatus. Daaronder vallen hardwareparameters, de bedrijfstoestand en realtime bewakingsgegevens.

De systeemstatus weergeven:
```bash
# Display comprehensive system status
halpi status
```

Deze opdracht geeft een volledig overzicht van de huidige bedrijfstoestand van de HALPI2, inclusief spanningsniveaus, stroomverbruik, temperatuurmetingen en controllerstatus:

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

Wilt u slechts één specifieke waarde bewaken, dan kunt u die als volgt opvragen:

```bash
# Show controller firmware version
halpi get firmware_version
```

Voor scripts kunt u beter de REST API gebruiken, zoals beschreven in het onderdeel [REST API-toegang](#rest-api-toegang).

#### Configuratiebeheer

Het HALPI-opdrachtregelgereedschap biedt uitgebreide mogelijkheden voor configuratiebeheer, waarmee u de huidige instellingen kunt bekijken en bedrijfsparameters kunt wijzigen.

De huidige configuratie bekijken:
```bash
# Show current configuration
halpi config
```

Dit toont alle instelbare parameters en hun huidige waarden:

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

#### Ledbesturing

Een van de vaakst aangepaste instellingen is de ledhelderheid, die kan worden afgestemd op verschillende gebruiksomgevingen en persoonlijke voorkeuren.

Voorbeeldopdrachten voor het beheren van de ledhelderheid:
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

De ledhelderheid accepteert waarden van 0 (volledig uit) tot 255 (maximale helderheid), wat nauwkeurige controle geeft over de led-indicatoren op het frontpaneel.

#### Energiebeheer

Het HALPI-opdrachtregelgereedschap biedt de essentiële functies voor energiebeheer die nodig zijn voor een veilige werking van het systeem.

Voorbeelden van opdrachten voor energiebeheer:
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

De shutdown-opdracht zorgt ervoor dat het systeem veilig wordt uitgeschakeld, zodat het besturingssysteem applicaties kan sluiten en bestandssystemen correct kan ontkoppelen voordat de controller de spanning wegneemt.

#### REST API-toegang

Voor gevorderde gebruikers en eigen toepassingen biedt de HALPI-daemon ook een REST API die bereikbaar is via een Unix-domainsocket. Dat maakt snellere programmatische toegang tot systeemgegevens mogelijk:

Hieronder staan enkele gebruiksvoorbeelden:
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

De REST API is vooral nuttig voor bewakingstoepassingen, systemen voor dataregistratie of integratie met andere software die realtime toegang nodig heeft tot de statusinformatie van de HALPI2.

De volledige REST API-documentatie staat in het hoofdstuk [Softwareontwikkeling: daemon](../software-development/daemon.md).

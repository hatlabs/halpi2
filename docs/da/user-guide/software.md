---
translated_from: 14a7c45fdb780582813fb147c7e6e5c28f41ae7b
---

# Softwarevejledning

## Styresystemimages

Hat Labs leverer færdigbyggede images til HALPI2. Alle images indeholder den konfiguration og de tilpasninger, HALPI2-hardwaren kræver, herunder CAN (NMEA 2000) som netværksenheden `can0`, RS-485 (NMEA 0183) som `/dev/ttyAMA4` og pakken `halpi2-firmware`.

### HaLOS (standard)

[HaLOS](https://docs.halos.fi) er en containerbaseret Linux-distribution udviklet til marine og industrielle anvendelser. Den giver en webstyret grænseflade til systemadministration, applikationshåndtering og overvågning — der kræves hverken skærm, tastatur eller VNC.

**Imagevarianter:**

| Image | Beskrivelse |
|:------|:------------|
| Halos-HALPI2 | Basisimage uden skærm (headless) med Cockpit og containerhåndtering |
| Halos-HALPI2-Desktop | Basisimage med Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Uden skærm, med marineapplikationer (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Desktop med marineapplikationer |

Hent HaLOS-images fra [HaLOS' udgivelsesside](https://github.com/halos-org/halos-pi-gen/releases/latest). Detaljeret dokumentation findes på [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter er et image baseret på Raspberry Pi OS med tilføjelser til marine anvendelser. Det giver et traditionelt skrivebordsmiljø med fjernadgang via VNC og leveres med Signal K og OpenCPN forudinstalleret.

Hvis du ikke bruger skærm, tastatur og mus sammen med HALPI2, kan du forbinde dig til computeren enten med et ethernetkabel eller via WiFi-adgangspunktet (`OpenPlotter`, adgangskode `12345678`).

Med begge muligheder kan du tilgå HALPI2-computeren via VNC eller SSH. For at bruge VNC skal du hente RealVNC's [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).

Da både adgangspunktet og standardbrugeren leveres med standardadgangskoder, er det bydende nødvendigt, at adgangskoderne ændres umiddelbart efter den første opstart. Fremgangsmåden er beskrevet i [OpenPlotter-dokumentationen](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Hent OpenPlotter-images fra [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS og Raspberry Pi OS Lite

Hvis du foretrækker at bruge standardudgaven af Raspberry Pi OS, kan du hente
det nyeste image med HALPI2-understøttelse fra [GitHub-repositoriet](https://github.com/hatlabs/openplotter-halpi/releases).
Flash imaget til SSD-disken med Raspberry Pi Imager. Under flashningen kan du
anvende tilpasninger som at angive værtsnavn, aktivere SSH og konfigurere WiFi.

Hvis du vælger ikke at anvende tilpasninger, skal du have en skærm og et
tastatur tilsluttet HALPI2 for at gennemføre den indledende opsætning. Du bliver
bedt om at angive et brugernavn og en adgangskode ved den første opstart.


## Flashning af et styresystemimage til SSD'en

Der er to metoder til at flashe et styresystemimage til HALPI2's NVMe SSD: at tage SSD'en ud og bruge en USB-NVMe-adapter, eller at flashe direkte på HALPI2-enheden. Metoden med USB-NVMe-adapter anbefales, fordi den er bekvem og nem — adapterne fås billigt på nettet og giver en ligetil flashningsproces.

### Flashning med en USB-NVMe-adapter

For at flashe imaget med USB-NVMe-adapteren skal du begynde med at tage NVMe SSD'en ud af HALPI2-enheden efter fremgangsmåden i [Hardwarevejledningen](./hardware.md#udskiftning-af-nvme-ssden). Hent derefter et HALPI2-kompatibelt image — enten et [HaLOS-image](https://github.com/halos-org/halos-pi-gen/releases/latest) eller et [OpenPlotter-/Raspberry Pi OS-image](https://github.com/hatlabs/openplotter-halpi/releases) — og sørg for at vælge det image, der passer til din anvendelse.

Sæt SSD'en i USB-NVMe-adapteren, og forbind den til din computer. Brug Raspberry Pi Imager til at flashe det hentede image til NVMe SSD'en. Hvis du flasher et Raspberry Pi OS-image, kan du redigere og anvende tilpasninger af styresystemet efter behov under flashningen. Hvis der ikke anvendes egne indstillinger, skal du dog have et USB-tastatur og en USB-mus tilsluttet HALPI2 til den indledende opsætning efter installationen.

Ved HaLOS-images bør tilpasninger af styresystemet **ikke** anvendes under flashningen. HaLOS konfigureres efter opstart via sin webgrænseflade.

På samme måde bør tilpasninger af styresystemet **ikke** anvendes under flashningen, når du bruger OpenPlotter-imaget. Konfigurationen sker i stedet efter den første opstart med konfigurationsværktøjerne til Raspberry Pi og OpenPlotter.

Når flashningen er færdig, skal du frakoble adapteren og tage SSD'en ud. Sæt SSD'en tilbage i HALPI2-enheden efter installationsproceduren i Hardwarevejledningen, og saml derefter kabinettet igen efter samme vejledning.

### Flashning direkte på HALPI2

Alternativt kan du flashe styresystemimaget direkte på HALPI2 uden at tage SSD'en ud. Denne metode følger standardproceduren for flashning af en Compute Module, som den er beskrevet i [Raspberry Pi-dokumentationen](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Vejledningen til kortopsætningen på den side er skrevet til CM5 IO Board, men processen er tilsvarende på HALPI2.

**Forudsætninger.** Installer værktøjet `rpiboot` fra Raspberry Pi's [`usbboot`-repositorium](https://github.com/raspberrypi/usbboot). På Linux og macOS bygger og installerer du det fra kildekoden som beskrevet i repositoriets README; på Windows installerer du Raspberry Pi Imager eller det selvstændige `rpiboot`-installationsprogram, der er linket til fra samme side.

Sådan gør du HALPI2 klar til USB-flashning:

1. Sluk systemet helt, og åbn kabinetlåget efter fremgangsmåden i [Hardwarevejledningen](./hardware.md#adgang-til-kabinettet).
2. Find USB-C-stikket, der er mærket »USB Boot«. Det sidder til højre for HAT-omridset på bærekortet. Stil derefter den tilstødende kontakt til boot-tilstand over i positionen »Abnormal«. (Der er endnu ingen tilbagemelding fra LED'erne — enheden er uden strøm.)
3. Forbind et USB-kabel mellem din computer og USB Boot-stikket på HALPI2, og tænd derefter enheden igen. En gul LED ved siden af kontakten til boot-tilstand lyser nu og bekræfter, at HALPI2 er i USB-boot-tilstand.
4. Kør `rpiboot` på din computer. Værktøjet registrerer HALPI2 og indlæser firmwaren til masselagerenheden; HALPI2 optræder derefter som en USB-masselagerenhed.
5. Når `rpiboot` er lykkedes, og masselagerenheden er dukket op, skal du stille kontakten til boot-tilstand tilbage i positionen »Normal«. Det afbryder ikke flashningen, og det sikrer, at HALPI2 starter normalt fra det nyflashede image, næste gang du slukker og tænder. Hvis kontakten bliver stående i »Abnormal«, går enheden i USB-boot-tilstand igen ved næste opstart i stedet for at starte det nye styresystem.
6. Flash styresystemimaget med Raspberry Pi Imager (eller et andet værktøj, der kan skrive til en blokenhed), med den nye masselagerenhed som mål.
7. Når flashningen er færdig, skal du frakoble USB-kablet, slukke og tænde HALPI2 igen og lukke kabinettet.

!!! tip "Slukning og tænding uden at trække stikket ud"
    Når kabinettet allerede er åbent, er den hurtigste måde at genstarte HALPI2 på at kortslutte de to nederste ben på knapstiklisten ved siden af USB-C-stikket et kort øjeblik. At røre ved begge ben samtidig med metalkappen på et USB-C-kabelstik fungerer godt og er ufarligt.

## Indledende systemkonfiguration

Når du har flashet og startet din HALPI2 for første gang, kræves der flere konfigurationstrin for at sikre en sikker og korrekt drift af systemet.

### Konfiguration af HaLOS

HaLOS konfigureres udelukkende via sin webgrænseflade. Efter den første opstart kan du tilgå Cockpit på `https://halos.local:9090/` og dashboardet på `https://halos.local/`. Skift standardadgangskoderne med det samme — se vejledningen [Kom godt i gang](../getting-started/getting-started.md#konfiguration-ved-frste-opstart) og [HaLOS-dokumentationen](https://docs.halos.fi/getting-started/first-boot/) for detaljer.

### Konfiguration af OpenPlotter

Når du bruger OpenPlotter-imaget, starter systemet med standardadgangskoder til både WiFi-adgangspunktet og standardbrugerkontoen. Af sikkerhedshensyn er det bydende nødvendigt, at disse adgangskoder ændres umiddelbart efter den første opstart.

Skift af adgangskoder og den indledende konfiguration er beskrevet i vejledningen [Kom godt i gang](../getting-started/getting-started.md#konfiguration-ved-frste-opstart) og i [OpenPlotter-dokumentationen](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Konfiguration af Raspberry Pi OS

Hvis du har valgt at bruge standardudgaven af Raspberry Pi OS i stedet for OpenPlotter, skal du følge den almindelige opsætningsproces for Raspberry Pi, som vises ved den første opstart. Denne opsætningsguide fører dig gennem oprettelse af brugerkonti, valg af adgangskoder, konfiguration af WiFi-forbindelser og aktivering af nødvendige tjenester som SSH til fjernadgang.

Under den indledende opsætning vil du måske også indstille tidszone, tastaturlayout og andre regionale indstillinger, så de passer til dine omgivelser. Konfigurationsværktøjet til Raspberry Pi (`raspi-config`) giver adgang til flere systemindstillinger, som kan justeres, når den indledende opsætning er gennemført.

## Fjernadgang

HALPI2 understøtter flere former for fjernadgang, så du kan overvåge og styre systemet uden fysisk adgang til enheden. Det er især værdifuldt i installationer, hvor HALPI2 er monteret uden skærm på svært tilgængelige steder.

### Webbaseret adgang (HaLOS)

HaLOS har en komplet webbaseret administrationsgrænseflade, og der kræves ingen ekstra software:

- **Dashboard** (`https://halos.local/`): Homarr-dashboardet giver adgang til alle installerede applikationer, herunder Signal K, Grafana og andre marineapplikationer.
- **Cockpit** (`https://halos.local:9090/`): Systemadministration med terminaladgang, softwareopdateringer, netværkskonfiguration og håndtering af containerapps.

### SSH (Secure Shell)

SSH giver sikker kommandolinjeadgang til HALPI2-systemet, så du kan køre kommandoer, overføre filer og udføre systemadministration på afstand. SSH er aktiveret som standard på HaLOS-images uden skærm og på OpenPlotter. På HaLOS Desktop-varianter og Raspberry Pi OS kan SSH aktiveres via `raspi-config`.

For at oprette forbindelse via SSH skal du bruge en SSH-klient, for eksempel den indbyggede terminal på macOS og Linux eller programmer som PuTTY på Windows. Den grundlæggende kommando til at oprette forbindelse er:

```bash
ssh username@halpi2-ip-address
```

SSH-forbindelser er krypterede og sikre, hvilket gør dem egnede til brug over offentlige netværk, når de er sat op med stærk godkendelse. Desuden kræver de meget lidt båndbredde, hvilket gør dem ideelle til fjernadgang over langsomme forbindelser med høj forsinkelse.

### VNC (Virtual Network Computing)

!!! note
    VNC gælder kun for OpenPlotter- og Raspberry Pi OS Desktop-images. HaLOS bruger webbaseret adgang i stedet — se ovenfor.

VNC giver fjernadgang til HALPI2's grafiske skrivebord, så du kan arbejde i skrivebordsmiljøet, som var du fysisk til stede ved enheden. VNC er forudinstalleret og forudkonfigureret på OpenPlotter-images. På installationer med Raspberry Pi OS kan VNC aktiveres med konfigurationsværktøjet `raspi-config`.

For at forbinde dig til HALPI2's skrivebord på afstand skal du bruge RealVNC's [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/), som findes til Windows, macOS, Linux, iOS og Android. VNC fungerer godt på lokale netværk og i offlinemiljøer, hvilket gør det ideelt til bådinstallationer, hvor internetforbindelsen kan være begrænset eller helt fraværende.

Ved fjernadgang over internettet kræver VNC ekstra netværkskonfiguration som portviderestilling eller opsætning af VPN, fordi protokollen ikke i sig selv passerer firewalls og NAT-enheder.

### Raspberry Pi Connect

Raspberry Pi Connect er en moderne, webbaseret måde at få fjernadgang til skrivebordet på: du forbinder dig til HALPI2's skrivebord med en almindelig browser, uden at der skal installeres ekstra software. Tjenesten arbejder automatisk gennem firewall- og NAT-opsætninger, hvilket gør den særligt velegnet til fjernadgang over internettet uden kompliceret netværksopsætning.

I modsætning til VNC håndterer Raspberry Pi Connect selv de netværksmæssige forviklinger og giver gnidningsfri adgang alle steder fra, hvor der er internetforbindelse. Til gengæld kræver den, at HALPI2 selv har en aktiv internetforbindelse.

## Softwareopdateringer

Regelmæssige opdateringer anbefales for at bevare optimal ydeevne og sikkerhed i systemet.

### Opdatering af HaLOS

På HaLOS opdateres systempakker (herunder HALPI2-firmwaren) via Cockpit eller fra kommandolinjen med `apt`. Containerbaserede applikationer (Signal K, Grafana osv.) opdateres via Cockpits grænseflade Container Apps, som ser efter nye versioner af containerimages.

### Opdatering fra kommandolinjen (alle images)

Den mest pålidelige måde at opdatere systemet på er via kommandolinjen. Åbn et terminalvindue, og kør følgende kommandoer for at opdatere systemet:

```bash
sudo apt update
sudo apt upgrade
```

Den første kommando (`apt update`) opdaterer pakkedatabasen med de nyeste tilgængelige versioner, mens den anden kommando (`apt upgrade`) henter og installerer alle tilgængelige opdateringer. Denne proces opdaterer alle installerede pakker, herunder Raspberry Pi OS-grundsystemet, OpenPlotter-komponenterne og HALPI2-specifik software.

Under opdateringen kan du blive bedt om at bekræfte installationen af bestemte pakker eller genstart af tjenester. Det er som regel sikkert at acceptere disse forespørgsler, medmindre du har særlige grunde til at afvise dem.

### Grafisk opdatering

Foretrækker du en grafisk grænseflade, giver skrivebordsmiljøet visuel besked, når der er opdateringer. Et download-ikon dukker op i øverste højre hjørne af skrivebordets proceslinje, når opdateringer er klar til installation. Klikker du på ikonet, åbnes opdateringshåndteringen, som giver en brugervenlig grænseflade til at gennemgå og installere de tilgængelige opdateringer.

## Firmwareopdateringer

Firmwaren i HALPI2's controller kan opdateres med den almindelige opdateringsproces i Raspberry Pi OS, hvilket giver en gnidningsfri og integreret måde at holde firmwaren opdateret på. Regelmæssige firmwareopdateringer er vigtige for at sikre optimal ydeevne, få adgang til nye funktioner og bevare kompatibiliteten med de softwarekomponenter, der udvikler sig løbende.

### Automatiske firmwareopdateringer

Firmwareopdateringer leveres gennem den almindelige mekanisme til systemopdatering, altså Debian-pakker i et APT-pakkearkiv. Åbn et terminalvindue, og kør følgende kommandoer for at se efter og installere firmwareopdateringer:

```bash
sudo apt update
sudo apt upgrade
```

Når der er ny HALPI2-firmware, hentes og installeres den automatisk som en del af opgraderingen. Systemet giver dig besked, hvis der er firmwareopdateringer blandt de tilgængelige pakker.

Når firmwarepakken er opdateret, er det afgørende, at systemet genstartes korrekt, så firmwareændringerne træder i kraft. Brug nedlukningskommandoen for at sikre, at strømmen bliver afbrudt helt:

```bash
sudo shutdown -h now
```

**Vigtigt:** Det er ikke nok blot at genstarte systemet ved en firmwareopdatering. Der kræves en fuldstændig nedlukning og efterfølgende start, fordi det er dét, der får controlleren til at genstarte og tage den nye firmware i brug. Firmwaren i controlleren opdateres kun under opstartssekvensen.

### Sikkerhedsfunktioner i firmwaren

HALPI2 har indbyggede sikkerhedsmekanismer, der beskytter mod ødelagt firmware. Hvis enheden genstartes igen inden for 30 sekunder efter en firmwareopdatering, ruller systemet automatisk tilbage til den forrige firmwareversion. Funktionen beskytter mod problematiske firmwareopdateringer, der ellers kunne forhindre normal drift.

### Manuel installation af firmware

Til erfarne brugere og bestemte fejlfindingssituationer kan firmwaren installeres manuelt med HALPI-kommandolinjeværktøjet. Firmwarefilerne ligger i mappen `/usr/share/halpi2-firmware/` og kan flashes direkte med:

```bash
halpi flash <firmware_file>.bin
```

### Deaktivering af automatiske firmwareopdateringer

Nogle brugere ønsker måske at deaktivere automatiske firmwareopdateringer for at blive på en bestemt firmwareversion. Det gøres ved at redigere HALPI2's konfigurationsfil:

```bash
sudo nano /etc/halpid/firmware.conf
```

Find indstillingen `AUTO_FLASH_ON_INSTALL`, og sæt den til `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Gem filen, og afslut editoren. Denne ændring forhindrer HALPI2 i automatisk at flashe ny firmware under den almindelige opdateringsproces, så du selv bestemmer, hvornår firmwareopdateringer tages i brug. Du kan stadig installere firmwareopdateringer manuelt med kommandoen `halpi flash`, når du ønsker det.


## HALPI-kommandolinjeværktøjet

HALPI2's softwaregrænseflade består af dæmontjenesten `halpid` (baggrundstjenesten) og kommandolinjeværktøjet `halpi`. Tilsammen giver de mulighed for overvågning, konfiguration og styring af systemet.

### HALPI-dæmonen (`halpid`)

HALPI-dæmonen kører som en systemtjeneste og står for kommunikationen mellem styresystemet og HALPI2's controller. Med dæmonen kørende får controlleren fuld overvågning, konfiguration og koordinering af kontrolleret nedlukning — se referencen [Bærekortets controller](../technical-reference/controller.md#driftstilstande) for, hvordan controlleren opfører sig med og uden den.

#### Håndtering af tjenesten

Dæmonen håndteres via systemd:

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

Dæmonens konfiguration ligger i `/etc/halpid/halpid.conf`. Rediger konfigurationen med:

```bash
sudo nano /etc/halpid/halpid.conf
```

Ændringer i konfigurationen kræver, at dæmonen genstartes:

```bash
sudo systemctl restart halpid
```

### HALPI-kommandolinjeværktøjet (`halpi`)

Kommandoen `halpi` giver direkte adgang til controllerens funktioner og til systemets status. Den kommunikerer med dæmonen for at udføre kommandoer og hente oplysninger om HALPI2's driftstilstand, konfiguration og hardwareparametre.

#### Systemstatus og overvågning

Kommandolinjeværktøjet HALPI's vigtigste funktion er at give fyldestgørende oplysninger om systemets status. Det omfatter hardwareparametre, driftstilstand og overvågningsdata i realtid.

Visning af systemets status:
```bash
# Display comprehensive system status
halpi status
```

Denne kommando giver et komplet overblik over HALPI2's aktuelle driftstilstand, herunder spændingsniveauer, strømforbrug, temperaturmålinger og controllerens status:

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

Vil du kun følge en enkelt værdi, kan den hentes sådan her:

```bash
# Show controller firmware version
halpi get firmware_version
```

Til scripting er det bedre at bruge REST-API'et, som beskrevet i afsnittet [Adgang til REST-API'et](#adgang-til-rest-apiet).

#### Konfigurationsstyring

Kommandolinjeværktøjet HALPI har fyldestgørende funktioner til konfigurationsstyring, så du kan se de aktuelle indstillinger og ændre driftsparametre.

Visning af den aktuelle konfiguration:
```bash
# Show current configuration
halpi config
```

Dette viser alle konfigurerbare parametre og deres aktuelle værdier:

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

#### LED-styring

En af de indstillinger, der oftest justeres, er LED-lysstyrken, som kan tilpasses forskellige driftsmiljøer og personlige præferencer.

Eksempler på kommandoer til styring af LED-lysstyrken:
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

LED-lysstyrken accepterer værdier fra 0 (helt slukket) til 255 (maksimal lysstyrke), hvilket giver finmasket kontrol over status-LED'erne på frontpanelet.

#### Strømstyring

Kommandolinjeværktøjet HALPI stiller de nødvendige funktioner til strømstyring til rådighed for sikker drift af systemet.

Eksempler på kommandoer til strømstyring:
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode, waking up after a delay (seconds) or at a given time
halpi shutdown --standby --time 3600
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Nedlukningskommandoen sikrer, at systemet lukker sikkert ned, så styresystemet kan afslutte programmer og afmontere filsystemer ordentligt, før controlleren afbryder strømmen.

#### Adgang til REST-API'et

Til erfarne brugere og egne applikationer stiller HALPI-dæmonen desuden et REST-API til rådighed via en Unix-domænesocket. Det giver hurtigere programmatisk adgang til systemets data:

Se nogle eksempler på brugen herunder:
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

REST-API'et er især nyttigt til overvågningsprogrammer, systemer til datalogning eller integration med anden software, der har brug for adgang til HALPI2's statusoplysninger i realtid.

Den fulde dokumentation af REST-API'et findes i kapitlet [Softwareudvikling: HALPI2-dæmonen](../software-development/daemon.md).

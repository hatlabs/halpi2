# Programvareveiledning

## Operativsystembilder

Hat Labs tilbyr ferdigbygde systembilder for HALPI2. Alle systembilder inneholder nødvendig konfigurasjon og tilpasning for HALPI2-maskinvaren, inkludert CAN (NMEA 2000) som nettverksenheten `can0`, RS-485 (NMEA 0183) som `/dev/ttyAMA4`, og pakken `halpi2-firmware`.

### HaLOS (standard)

[HaLOS](https://docs.halos.fi) er en containerbasert Linux-distribusjon utviklet for maritime og industrielle bruksområder. Den gir et webadministrert grensesnitt for systemadministrasjon, applikasjonsstyring og overvåking – uten behov for skjerm, tastatur eller VNC.

**Varianter av systembildet:**

| Systembilde | Beskrivelse |
|:------|:------------|
| Halos-HALPI2 | Basisbilde uten skjerm (headless) med Cockpit og containerstyring |
| Halos-HALPI2-Desktop | Basisbilde med Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Uten skjerm, med maritime apper (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Desktop med maritime apper |

Last ned HaLOS-systembilder fra [utgivelsessiden for HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest). Se [docs.halos.fi](https://docs.halos.fi) for detaljert dokumentasjon.

### OpenPlotter

OpenPlotter er et systembilde basert på Raspberry Pi OS med tillegg for maritime bruksområder. Det gir et tradisjonelt skrivebordsmiljø med VNC-fjerntilgang, og leveres med Signal K og OpenCPN ferdig installert.

Hvis du ikke bruker skjerm, tastatur og mus sammen med HALPI2, kan du koble deg til datamaskinen enten med en Ethernet-kabel eller via WiFi-aksesspunktet (`OpenPlotter`, passord `12345678`).

Med begge deler kan du nå HALPI2-datamaskinen med VNC eller SSH. Du må laste ned RealVNCs [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) for å bruke VNC.

Ettersom både aksesspunktet og standardbrukeren leveres med standardpassord, er det helt nødvendig at passordene endres umiddelbart etter første oppstart. Prosessen er beskrevet i [OpenPlotter-dokumentasjonen](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Last ned OpenPlotter-systembilder fra [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS og Raspberry Pi OS Lite

Hvis du foretrekker å bruke standard Raspberry Pi OS, kan du laste ned det nyeste
systembildet med HALPI2-støtte fra [GitHub-repositoriet](https://github.com/hatlabs/openplotter-halpi/releases).
Flash systembildet til SSD-disken med Raspberry Pi Imager. Under flashingen kan
du bruke tilpasninger som å angi vertsnavn, aktivere SSH og konfigurere WiFi.

Hvis du velger å ikke bruke tilpasninger, må du ha en skjerm og et tastatur
koblet til HALPI2 for å fullføre det første oppsettet. Du blir bedt om å oppgi
brukernavn og passord ved første oppstart.


## Flashe et operativsystembilde til SSD

Det finnes to metoder for å flashe et operativsystembilde til NVMe SSD-en i HALPI2: å ta ut SSD-en og bruke en USB-NVMe-adapter, eller å flashe direkte på HALPI2-enheten. Metoden med USB-NVMe-adapter anbefales fordi den er praktisk og enkel; slike adaptere fås rimelig på nett og gir en grei flasheprosess.

### Flashe med en USB-NVMe-adapter

For å flashe systembildet med USB-NVMe-adapteren begynner du med å ta NVMe SSD-en ut av HALPI2-enheten slik prosedyren i [Maskinvareveiledningen](./hardware.md#replacing-the-nvme-ssd) beskriver. Deretter laster du ned et HALPI2-kompatibelt systembilde – enten et [HaLOS-systembilde](https://github.com/halos-org/halos-pi-gen/releases/latest) eller et [OpenPlotter- eller Raspberry Pi OS-systembilde](https://github.com/hatlabs/openplotter-halpi/releases) – og passer på å velge riktig systembilde for den bruken du har tenkt deg.

Sett SSD-en inn i USB-NVMe-adapteren og koble den til datamaskinen din. Bruk Raspberry Pi Imager til å flashe det nedlastede systembildet til NVMe SSD-en. Hvis du flasher et Raspberry Pi OS-systembilde, kan du redigere og ta i bruk tilpasningsinnstillinger for operativsystemet etter behov under flashingen. Men hvis du ikke tar i bruk egne innstillinger, trenger du et USB-tastatur og en mus koblet til HALPI2 for det første oppsettet etter installasjonen.

Når du bruker HaLOS-systembilder, skal tilpasningsinnstillinger for operativsystemet **ikke** tas i bruk under flashingen. HaLOS konfigureres etter oppstart via webgrensesnittet sitt.

På samme måte skal tilpasningsinnstillinger for operativsystemet **ikke** tas i bruk under flashingen når du bruker OpenPlotter-systembildet. Konfigurasjonen gjøres i stedet etter første oppstart med konfigurasjonsverktøyene til Raspberry Pi og OpenPlotter.

Når flashingen er ferdig, kobler du fra adapteren og tar ut SSD-en. Sett SSD-en tilbake i HALPI2-enheten slik installasjonsprosedyren i Maskinvareveiledningen beskriver, og monter så kabinettet sammen igjen etter samme veiledning.

### Flashe direkte på HALPI2

Alternativt kan du flashe operativsystembildet direkte på HALPI2 uten å ta ut SSD-en. Denne metoden følger standardprosedyren for flashing av Compute Module, slik den er dokumentert i [Raspberry Pi-dokumentasjonen](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Instruksjonene for kortoppsett der er skrevet for CM5 IO Board, men prosessen er tilsvarende for HALPI2.

**Forutsetninger.** Installer verktøyet `rpiboot` fra Raspberry Pi-repositoriet [`usbboot`](https://github.com/raspberrypi/usbboot). På Linux og macOS bygger og installerer du det fra kildekoden slik README-filen i repoet beskriver; på Windows installerer du Raspberry Pi Imager eller det frittstående `rpiboot`-installasjonsprogrammet som er lenket fra samme side.

Slik gjør du HALPI2 klar for USB-flashing:

1. Slå av systemet helt og åpne kabinettlokket slik prosedyren i [Maskinvareveiledningen](./hardware.md#enclosure-access) beskriver.
2. Finn USB-C-kontakten merket «USB Boot» til høyre for HAT-omrisset på bærekortet, og sett den tilstøtende bryteren for oppstartsmodus i «Abnormal»-stilling. (Det finnes ingen LED-tilbakemelding ennå – enheten er uten strøm.)
3. Koble en USB-kabel mellom datamaskinen din og USB Boot-kontakten på HALPI2, og slå så enheten på igjen. En ravgul LED ved siden av bryteren for oppstartsmodus lyser nå og bekrefter at HALPI2 er i USB-oppstartsmodus.
4. Kjør `rpiboot` på datamaskinen din. Den oppdager HALPI2 og laster inn firmwaren for masselagringsenheten; HALPI2 vises deretter som en USB-masselagringsenhet.
5. Når `rpiboot` er ferdig og masselagringsenheten vises, setter du bryteren for oppstartsmodus tilbake i «Normal»-stilling. Dette avbryter ikke flasheøkten, og det sikrer at HALPI2 starter normalt opp fra det nyflashede systembildet etter neste av- og påslag. Blir bryteren stående i «Abnormal», går enheten inn i USB-oppstartsmodus igjen ved neste oppstart i stedet for å starte det nye operativsystemet.
6. Flash operativsystembildet med Raspberry Pi Imager (eller et annet verktøy som kan skrive til en blokkenhet), med den nye masselagringsenheten som mål.
7. Når flashingen er ferdig, kobler du fra USB-kabelen, slår HALPI2 av og på igjen, og lukker kabinettet.

!!! tip "Av- og påslag uten å trekke ut kabelen"
    Når kabinettet allerede er åpent, er den raskeste måten å starte HALPI2 på nytt å kortslutte de to nederste pinnene på Button Headers ved siden av USB-C-kontakten et kort øyeblikk. Å berøre begge pinnene samtidig med metallhylsen på en USB-C-kabelkontakt fungerer godt og er trygt.

## Første systemkonfigurasjon

Etter at du har flashet og startet opp HALPI2 for første gang, kreves det flere konfigurasjonstrinn for å sikre trygg og riktig drift av systemet.

### HaLOS-konfigurasjon

HaLOS konfigureres i sin helhet via webgrensesnittet. Etter første oppstart når du Cockpit på `https://halos.local:9090/` og dashbordet på `https://halos.local/`. Endre standardpassordene umiddelbart – se veiledningen [Kom i gang](../getting-started/getting-started.md#first-boot-configuration) og [HaLOS-dokumentasjonen](https://docs.halos.fi/getting-started/first-boot/) for detaljer.

### OpenPlotter-konfigurasjon

Når du bruker OpenPlotter-systembildet, starter systemet opp med standardpassord både for WiFi-aksesspunktet og for standardbrukerkontoen. Av sikkerhetsgrunner er det helt nødvendig at disse passordene endres umiddelbart etter første oppstart.

Prosessen for å endre passord og den første konfigurasjonen er beskrevet i veiledningen [Kom i gang](../getting-started/getting-started.md#first-boot-configuration) og i [OpenPlotter-dokumentasjonen](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Raspberry Pi OS-konfigurasjon

Hvis du har valgt å bruke standard Raspberry Pi OS i stedet for OpenPlotter, følger du det vanlige Raspberry Pi-oppsettet som vises ved første oppstart. Denne oppsettsveiviseren leder deg gjennom å opprette brukerkontoer, sette passord, konfigurere WiFi-tilkoblinger og aktivere viktige tjenester som SSH for fjerntilgang.

Under det første oppsettet vil du kanskje også stille inn tidssone, tastaturoppsett og andre regionale innstillinger som passer til driftsmiljøet ditt. Konfigurasjonsverktøyet for Raspberry Pi (`raspi-config`) gir tilgang til flere systeminnstillinger som kan justeres etter at det første oppsettet er fullført.

## Fjerntilgang

HALPI2 støtter flere metoder for fjerntilgang, slik at du kan overvåke og styre systemet uten å ha fysisk tilgang til enheten. Dette er særlig verdifullt i installasjoner der HALPI2 er montert uten skjerm på steder som er vanskelige å nå.

### Webbasert tilgang (HaLOS)

HaLOS gir et komplett webbasert administrasjonsgrensesnitt uten behov for ekstra programvare:

- **Dashboard** (`https://halos.local/`): Homarr-dashbordet gir tilgang til alle installerte applikasjoner, inkludert Signal K, Grafana og andre maritime apper.
- **Cockpit** (`https://halos.local:9090/`): Systemadministrasjon, inkludert terminaltilgang, programvareoppdateringer, nettverkskonfigurasjon og styring av containerapper.

### SSH (Secure Shell)

SSH gir sikker kommandolinjetilgang til HALPI2-systemet, slik at du kan kjøre kommandoer, overføre filer og utføre systemadministrasjon eksternt. SSH er aktivert som standard på HaLOS-systembilder uten skjerm og på OpenPlotter. På HaLOS Desktop-varianter og på Raspberry Pi OS kan SSH aktiveres med `raspi-config`.

For å koble til med SSH bruker du en SSH-klient, for eksempel den innebygde terminalen på macOS og Linux, eller programmer som PuTTY på Windows. Den grunnleggende tilkoblingskommandoen er:

```bash
ssh username@halpi2-ip-address
```

SSH-tilkoblinger er krypterte og sikre, og egner seg derfor for bruk over offentlige nettverk når de er riktig konfigurert med sterk autentisering. SSH krever også svært lite båndbredde, noe som gjør det ideelt for fjerntilgang over trege forbindelser med høy forsinkelse.

### VNC (Virtual Network Computing)

!!! note
    VNC gjelder bare for systembildene OpenPlotter og Raspberry Pi OS Desktop. HaLOS bruker webbasert tilgang i stedet – se ovenfor.

VNC gir fjerntilgang til det grafiske grensesnittet på HALPI2, slik at du kan bruke skrivebordsmiljøet som om du var fysisk til stede ved enheten. VNC er forhåndsinstallert og ferdig konfigurert på OpenPlotter-systembilder. På installasjoner med Raspberry Pi OS kan VNC aktiveres med konfigurasjonsverktøyet `raspi-config`.

For å koble deg til HALPI2-skrivebordet eksternt bruker du RealVNCs [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/), som er tilgjengelig for Windows, macOS, Linux, iOS og Android. VNC fungerer godt på lokale nettverk og i frakoblede miljøer, noe som gjør det ideelt for båtinstallasjoner der internettilgangen kan være begrenset eller mangle helt.

For fjerntilgang over internett krever VNC ekstra nettverkskonfigurasjon, som portviderekobling eller VPN-oppsett, siden protokollen ikke i seg selv passerer brannmurer og NAT-enheter.

### Raspberry Pi Connect

Raspberry Pi Connect gir en moderne, webbasert måte å få tilgang til skrivebordet eksternt på, slik at du kan koble deg til HALPI2-skrivebordet med bare en vanlig nettleser og uten å installere ekstra programvare. Tjenesten fungerer automatisk gjennom brannmur- og NAT-oppsett, og egner seg derfor særlig godt for fjerntilgang over internett uten komplisert nettverksoppsett.

I motsetning til VNC håndterer Raspberry Pi Connect nettverkskompleksiteten automatisk og gir sømløs tilgang fra hvor som helst med internettforbindelse. Til gjengjeld krever tjenesten at HALPI2 selv har en aktiv internettforbindelse for å fungere.

## Programvareoppdateringer

Regelmessige oppdateringer anbefales for å opprettholde optimal systemytelse og sikkerhet.

### HaLOS-oppdateringer

På HaLOS oppdateres systempakker (inkludert HALPI2-firmware) via Cockpit eller fra kommandolinjen med `apt`. Containerbaserte applikasjoner (Signal K, Grafana og så videre) oppdateres gjennom Container Apps-grensesnittet i Cockpit, som ser etter nye versjoner av containerbildene.

### Kommandolinjeoppdateringer (alle systembilder)

Den mest pålitelige måten å oppdatere systemet på er via kommandolinjen. Åpne et terminalvindu og kjør følgende kommandoer for å oppdatere systemet:

```bash
sudo apt update
sudo apt upgrade
```

Den første kommandoen (`apt update`) oppdaterer pakkedatabasen med de nyeste tilgjengelige versjonene, mens den andre kommandoen (`apt upgrade`) laster ned og installerer alle tilgjengelige oppdateringer. Denne prosessen oppdaterer alle installerte pakker, inkludert Raspberry Pi OS-basen, OpenPlotter-komponentene og programvare som er spesifikk for HALPI2.

Under oppdateringen kan du bli bedt om å bekrefte installasjonen av enkelte pakker eller om å starte tjenester på nytt. Det er normalt trygt å godta disse forespørslene, med mindre du har spesielle grunner til å avslå.

### Grafiske oppdateringer

For brukere som foretrekker et grafisk grensesnitt, gir skrivebordsmiljøet et synlig varsel når oppdateringer er tilgjengelige. Et nedlastingsikon dukker opp øverst til høyre på skrivebordets oppgavelinje når oppdateringer er klare til å installeres. Når du klikker på ikonet, åpnes oppdateringsbehandleren, som gir et brukervennlig grensesnitt for å gå gjennom og installere tilgjengelige oppdateringer.

## Firmware-oppdateringer

Kontrollerfirmwaren i HALPI2 kan oppdateres med den vanlige oppdateringsprosessen i Raspberry Pi OS, som gir en sømløs og integrert måte å holde firmwaren oppdatert på. Regelmessige firmware-oppdateringer er viktige for å sikre optimal ytelse, få tilgang til nye funksjoner og opprettholde kompatibilitet med programvarekomponenter i stadig utvikling.

### Automatiske firmware-oppdateringer

Firmware-oppdateringer leveres gjennom den vanlige mekanismen for systemoppdatering, som Debian-pakker i et APT-repositorium. For å se etter og installere firmware-oppdateringer åpner du et terminalvindu og kjører følgende kommandoer:

```bash
sudo apt update
sudo apt upgrade
```

Når ny HALPI2-firmware er tilgjengelig, lastes den automatisk ned og installeres som en del av oppgraderingen. Systemet varsler deg hvis firmware-oppdateringer er med blant de tilgjengelige pakkene.

Etter at oppdateringen av firmware-pakken er fullført, er det avgjørende at systemet startes på nytt på riktig måte for at firmware-endringene skal tre i kraft. Bruk kommandoen for nedstenging for å sikre en fullstendig av- og påslagssyklus:

```bash
sudo shutdown -h now
```

**Viktig:** Det holder ikke bare å starte systemet på nytt når firmwaren skal oppdateres. Fullstendig nedstenging og oppstart kreves, fordi det lar kontrolleren starte på nytt og ta i bruk den nye firmwaren. Kontrollerfirmwaren oppdateres bare under påslagssekvensen.

### Sikkerhetsfunksjoner for firmware

HALPI2 har innebygde sikkerhetsmekanismer som beskytter mot ødelagt firmware. Hvis enheten startes på nytt igjen innen 30 sekunder etter at en firmware-oppdatering er tatt i bruk, ruller systemet automatisk tilbake til den forrige firmwareversjonen. Denne funksjonen gir beskyttelse mot problematiske firmware-oppdateringer som kan hindre normal drift.

### Manuell installasjon av firmware

For avanserte brukere eller spesielle feilsøkingssituasjoner kan firmware installeres manuelt med HALPI-kommandolinjeverktøyet. Firmware-filene ligger i katalogen `/usr/share/halpi2-firmware/` og kan flashes direkte med:

```bash
halpi flash <firmware_file>.bin
```

### Slå av automatiske firmware-oppdateringer

Noen brukere vil kanskje slå av automatiske firmware-oppdateringer for å beholde en bestemt firmwareversjon. Det gjør du ved å redigere konfigurasjonsfilen til HALPI2:

```bash
sudo nano /etc/halpid/firmware.conf
```

Finn innstillingen `AUTO_FLASH_ON_INSTALL` og endre den til `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Lagre filen og avslutt redigeringsprogrammet. Denne endringen i konfigurasjonen hindrer HALPI2 i å flashe ny firmware automatisk under den vanlige oppdateringsprosessen, og gir deg full kontroll over når firmware-oppdateringer tas i bruk. Du kan fortsatt installere firmware-oppdateringer manuelt med kommandoen `halpi flash` når du ønsker det.


## HALPI-kommandolinjeverktøyet

Programvaregrensesnittet til HALPI2 består av daemon-tjenesten `halpid` og kommandolinjeverktøyet `halpi`. Sammen gir de systemovervåking, konfigurasjon og styring.

### HALPI-daemonen (`halpid`)

HALPI-daemonen kjører som en systemtjeneste og sørger for kommunikasjonen mellom operativsystemet og HALPI2-kontrolleren. Den gjør drift i samspillsmodus (co-op mode) mulig, med full overvåking og strømstyring.

#### Tjenestestyring

Daemonen styres gjennom systemd:

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

#### Konfigurasjon

Konfigurasjonen til daemonen ligger i `/etc/halpid/halpid.conf`. Bruk denne kommandoen for å redigere konfigurasjonen:

```bash
sudo nano /etc/halpid/halpid.conf
```

Endringer i konfigurasjonen krever at daemonen startes på nytt:

```bash
sudo systemctl restart halpid
```

### HALPI-kommandolinjeverktøyet (`halpi`)

Kommandoen `halpi` gir direkte tilgang til kontrollerfunksjoner og systemstatus. Den kommuniserer med daemonen for å kjøre kommandoer og hente informasjon om driftstilstanden, konfigurasjonen og maskinvareparametrene til HALPI2.

#### Systemstatus og overvåking

Hovedoppgaven til HALPI-kommandolinjeverktøyet er å gi utfyllende informasjon om systemstatus. Det omfatter maskinvareparametere, driftstilstand og overvåkingsdata i sanntid.

Vise systemstatus:
```bash
# Display comprehensive system status
halpi status
```

Denne kommandoen gir en fullstendig oversikt over den aktuelle driftstilstanden til HALPI2, inkludert spenningsnivåer, strømforbruk, temperaturavlesninger og kontrollerstatus:

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

Hvis du bare vil følge med på én bestemt verdi, kan den hentes slik:

```bash
# Show controller firmware version
halpi get firmware_version
```

For skripting er det bedre å bruke REST API-et i stedet, slik det er beskrevet i avsnittet [REST API-tilgang](#rest-api-access).

#### Konfigurasjonsstyring

HALPI-kommandolinjeverktøyet har omfattende funksjoner for konfigurasjonsstyring, slik at du kan se gjeldende innstillinger og endre driftsparametere.

Vise gjeldende konfigurasjon:
```bash
# Show current configuration
halpi config
```

Dette viser alle konfigurerbare parametere og verdiene de har nå:

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

En av innstillingene som justeres oftest, er LED-lysstyrken, som kan tilpasses ulike driftsmiljøer og brukerpreferanser.

Eksempler på kommandoer for styring av LED-lysstyrken:
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

LED-lysstyrken godtar verdier fra 0 (helt av) til 255 (maksimal lysstyrke), noe som gir finjustert kontroll over LED-indikatorene på frontpanelet.

#### Strømstyring

HALPI-kommandolinjeverktøyet har viktige strømstyringsfunksjoner for trygg drift av systemet.

Eksempler på strømstyringskommandoer:
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

Kommandoen for nedstenging sørger for at systemet slås av trygt, slik at operativsystemet rekker å lukke applikasjoner og avmontere filsystemene på riktig måte før kontrolleren kutter strømmen.

#### REST API-tilgang

For avanserte brukere og egne applikasjoner tilbyr HALPI-daemonen også et REST API-grensesnitt som er tilgjengelig via en Unix domain socket. Det gir raskere programmatisk tilgang til systemdata:

Nedenfor finner du noen brukseksempler:
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

REST API-et er særlig nyttig for overvåkingsapplikasjoner, systemer for datalogging eller integrasjon med annen programvare som trenger sanntidstilgang til statusinformasjon fra HALPI2.

Fullstendig dokumentasjon av REST API-et finnes i kapittelet [Programvareutvikling: Daemon](../software-development/daemon.md).

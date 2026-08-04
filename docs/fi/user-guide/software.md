# Ohjelmisto-opas

## Käyttöjärjestelmän levykuvat

Hat Labs tarjoaa HALPI2:lle valmiit levykuvat. Kaikissa levykuvissa on HALPI2:n laitteiston vaatimat asetukset ja muutokset, kuten CAN (NMEA 2000) verkkolaitteena `can0`, RS-485 (NMEA 0183) laitteena `/dev/ttyAMA4` sekä `halpi2-firmware`-paketti.

### HaLOS (oletus)

[HaLOS](https://docs.halos.fi) on konttipohjainen Linux-jakelu, joka on suunniteltu vene- ja teollisuuskäyttöön. Sitä hallitaan selainkäyttöliittymästä — näyttöä, näppäimistöä tai VNC:tä ei tarvita.

**Levykuvan versiot:**

| Levykuva | Kuvaus |
|:---------|:-------|
| Halos-HALPI2 | Näytötön perusversio, mukana Cockpit ja konttien hallinta |
| Halos-HALPI2-Desktop | Perusversio ja Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Näytötön versio venesovelluksineen (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Työpöytäversio venesovelluksineen |

Lataa HaLOS-levykuvat [HaLOSin julkaisusivulta](https://github.com/halos-org/halos-pi-gen/releases/latest). Tarkemmat ohjeet löytyvät osoitteesta [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter on Raspberry Pi OS -pohjainen levykuva, johon on lisätty venesovelluksia. Se tarjoaa perinteisen työpöytäympäristön ja VNC-etäyhteyden, ja siinä on valmiiksi asennettuna Signal K ja OpenCPN.

Jos et käytä HALPI2:n kanssa näyttöä, näppäimistöä ja hiirtä, voit ottaa yhteyden joko ethernet-kaapelilla tai WiFi-tukiaseman kautta (`OpenPlotter`, salasana `12345678`).

Kummallakin tavalla HALPI2-tietokoneeseen pääsee VNC:llä tai SSH:lla. VNC:n käyttöön tarvitset RealVNC:n [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) -sovelluksen.

Koska sekä tukiasemassa että oletuskäyttäjällä on oletussalasanat, salasanat on ehdottomasti vaihdettava heti ensikäynnistyksen jälkeen. Menettely on kuvattu [OpenPlotterin dokumentaatiossa](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Lataa OpenPlotter-levykuvat [GitHubista](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS ja Raspberry Pi OS Lite

Jos haluat käyttää tavallista Raspberry Pi OS:ää, voit ladata uusimman HALPI2:ta tukevan levykuvan [GitHub-repositoriosta](https://github.com/hatlabs/openplotter-halpi/releases). Flashaa levykuva SSD-levylle Raspberry Pi Imagerilla. Flashauksen yhteydessä voit tehdä muutoksia, kuten asettaa laitteen nimen, ottaa SSH:n käyttöön ja määrittää WiFin.

Jos et tee näitä muutoksia, tarvitset HALPI2:een kytketyn näytön ja näppäimistön alkuasetusten tekemiseen. Ensikäynnistyksessä sinulta kysytään käyttäjätunnusta ja salasanaa.


## Käyttöjärjestelmän flashaus SSD:lle

Käyttöjärjestelmän levykuvan voi flashata HALPI2:n NVMe SSD:lle kahdella tavalla: irrottamalla SSD:n ja käyttämällä USB-NVMe-sovitinta, tai flashaamalla suoraan HALPI2-laitteella. USB-NVMe-sovitinta suositellaan helppouden vuoksi: sovittimia saa verkosta edullisesti ja flashaus on suoraviivaista.

### Flashaus USB-NVMe-sovittimella

Aloita irrottamalla NVMe SSD HALPI2-laitteesta [Laitteisto-oppaan](./hardware.md#nvme-ssdn-vaihtaminen) ohjeen mukaan. Lataa seuraavaksi HALPI2:n kanssa yhteensopiva levykuva — joko [HaLOS-levykuva](https://github.com/halos-org/halos-pi-gen/releases/latest) tai [OpenPlotter- tai Raspberry Pi OS -levykuva](https://github.com/hatlabs/openplotter-halpi/releases) — ja varmista että valitset käyttötarkoitukseesi sopivan levykuvan.

Aseta SSD USB-NVMe-sovittimeen ja kytke se tietokoneeseesi. Flashaa ladattu levykuva NVMe SSD:lle Raspberry Pi Imagerilla. Jos flashaat Raspberry Pi OS -levykuvaa, voit muokata ja ottaa käyttöön käyttöjärjestelmän mukautusasetukset flashauksen aikana. Jos et tee mukautuksia, tarvitset HALPI2:een kytketyn USB-näppäimistön ja -hiiren asennuksen jälkeisiin alkuasetuksiin.

HaLOS-levykuvia käytettäessä mukautusasetuksia **ei** tule ottaa käyttöön flashauksen aikana. HaLOS määritetään käynnistyksen jälkeen selainkäyttöliittymästä.

Samoin OpenPlotter-levykuvaa käytettäessä mukautusasetuksia **ei** tule ottaa käyttöön flashauksen aikana. Asetukset tehdään ensikäynnistyksen jälkeen Raspberry Pi:n ja OpenPlotterin omilla työkaluilla.

Kun flashaus on valmis, irrota sovitin ja poista SSD. Aseta SSD takaisin HALPI2-laitteeseen Laitteisto-oppaan asennusohjeen mukaan ja kokoa kotelo saman oppaan mukaisesti.

### Flashaus suoraan HALPI2:lla

Vaihtoehtoisesti voit flashata käyttöjärjestelmän suoraan HALPI2:lla ilman SSD:n irrottamista. Tämä noudattaa tavallista Compute Modulen flashausmenettelyä, joka on kuvattu [Raspberry Pi:n dokumentaatiossa](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Siellä olevat kortin asetusohjeet on kirjoitettu CM5 IO Boardille, mutta menettely on HALPI2:lla samankaltainen.

**Esivalmistelut.** Asenna `rpiboot`-työkalu Raspberry Pi:n [`usbboot`-repositoriosta](https://github.com/raspberrypi/usbboot). Linuxilla ja macOS:llä käännä ja asenna se lähdekoodista repon README-ohjeen mukaan; Windowsilla asenna Raspberry Pi Imager tai erillinen `rpiboot`-asennusohjelma, joka löytyy samalta sivulta.

HALPI2:n valmistelu USB-flashausta varten:

1. Sammuta järjestelmä kokonaan ja avaa kotelon kansi [Laitteisto-oppaan](./hardware.md#kotelon-kasittely) ohjeen mukaan.
2. Paikanna emolevyltä HAT-alueen oikealta puolelta USB-C-liitin, jossa on merkintä "USB Boot", ja käännä sen vieressä oleva käynnistystilan kytkin "Abnormal"-asentoon. (LED-palautetta ei vielä ole, koska laitteessa ei ole virtaa.)
3. Kytke USB-kaapeli tietokoneesi ja HALPI2:n USB Boot -liittimen välille, ja kytke laitteeseen virta. Käynnistystilan kytkimen vieressä syttyy nyt keltainen LED, mikä vahvistaa HALPI2:n olevan USB-käynnistystilassa.
4. Aja tietokoneellasi `rpiboot`. Se tunnistaa HALPI2:n ja lataa massamuistilaitteen firmwaren, minkä jälkeen HALPI2 näkyy USB-massamuistilaitteena.
5. Kun `rpiboot` on onnistunut ja massamuistilaite näkyy, käännä käynnistystilan kytkin takaisin "Normal"-asentoon. Tämä ei keskeytä flashausta, ja se varmistaa että HALPI2 käynnistyy normaalisti juuri flashatusta levykuvasta seuraavan virrankatkaisun jälkeen. Jos kytkin jää "Abnormal"-asentoon, laite menee seuraavalla käynnistyksellä uudelleen USB-käynnistystilaan sen sijaan että käynnistäisi uuden käyttöjärjestelmän.
6. Flashaa käyttöjärjestelmän levykuva Raspberry Pi Imagerilla (tai millä tahansa työkalulla, joka osaa kirjoittaa lohkolaitteelle) uudelle massamuistilaitteelle.
7. Kun flashaus on valmis, irrota USB-kaapeli, katkaise ja kytke HALPI2:n virta ja sulje kotelo.

!!! tip "Uudelleenkäynnistys ilman virtajohdon irrottamista"
    Kun kotelo on jo auki, nopein tapa käynnistää HALPI2 uudelleen on oikosulkea hetkeksi USB-C-liittimen vieressä olevan painikeliittimen kaksi alinta nastaa. Molempien nastojen koskettaminen samanaikaisesti USB-C-kaapelin liittimen metallikuorella toimii hyvin ja on turvallista.

## Järjestelmän alkuasetukset

Kun HALPI2 on flashattu ja käynnistetty ensimmäistä kertaa, järjestelmä on määritettävä muutamin askelin turvallista ja asianmukaista käyttöä varten.

### HaLOSin asetukset

HaLOS määritetään kokonaan selainkäyttöliittymästä. Ensikäynnistyksen jälkeen Cockpit löytyy osoitteesta `https://halos.local:9090/` ja koontinäyttö osoitteesta `https://halos.local/`. Vaihda oletussalasanat heti — tarkemmat ohjeet ovat [Aloitusoppaassa](../getting-started/getting-started.md#ensikaynnistyksen-asetukset) ja [HaLOSin dokumentaatiossa](https://docs.halos.fi/getting-started/first-boot/).

### OpenPlotterin asetukset

OpenPlotter-levykuvaa käytettäessä sekä WiFi-tukiasemalla että oletuskäyttäjällä on oletussalasanat. Tietoturvasyistä nämä salasanat on ehdottomasti vaihdettava heti ensikäynnistyksen jälkeen.

Salasanojen vaihto ja alkuasetukset on kuvattu [Aloitusoppaassa](../getting-started/getting-started.md#ensikaynnistyksen-asetukset) ja [OpenPlotterin dokumentaatiossa](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Raspberry Pi OS:n asetukset

Jos olet valinnut tavallisen Raspberry Pi OS:n OpenPlotterin sijaan, seuraa ensikäynnistyksessä avautuvaa Raspberry Pi:n vakioasennusta. Ohjattu asennus opastaa käyttäjätilien luomisessa, salasanojen asettamisessa, WiFi-yhteyksien määrittämisessä ja tarpeellisten palveluiden, kuten etäkäytön SSH:n, käyttöönotossa.

Alkuasetusten yhteydessä kannattaa määrittää myös aikavyöhyke, näppäimistöasettelu ja muut alueelliset asetukset käyttöympäristöä vastaaviksi. Raspberry Pi:n asetustyökalu (`raspi-config`) tarjoaa pääsyn muihin järjestelmäasetuksiin, joita voi säätää alkuasetusten jälkeen.

## Etäkäyttö

HALPI2:ta voi käyttää etänä useilla tavoilla, jolloin järjestelmää voi valvoa ja ohjata ilman fyysistä pääsyä laitteelle. Tämä on erityisen arvokasta asennuksissa, joissa HALPI2 on ilman näyttöä hankalasti tavoitettavassa paikassa.

### Selainkäyttö (HaLOS)

HaLOS tarjoaa täyden selainpohjaisen hallintakäyttöliittymän ilman lisäohjelmistoja:

- **Koontinäyttö** (`https://halos.local/`): Homarr-koontinäytöltä pääsee kaikkiin asennettuihin sovelluksiin, kuten Signal K:hon, Grafanaan ja muihin venesovelluksiin.
- **Cockpit** (`https://halos.local:9090/`): järjestelmänhallinta, mukaan lukien pääte, ohjelmistopäivitykset, verkkoasetukset ja konttisovellusten hallinta.

### SSH (Secure Shell)

SSH tarjoaa suojatun komentoriviyhteyden HALPI2-järjestelmään, jolloin voit ajaa komentoja, siirtää tiedostoja ja hoitaa järjestelmänhallintaa etänä. SSH on oletuksena käytössä näytöttömissä HaLOS-levykuvissa ja OpenPlotterissa. HaLOSin Desktop-versioissa ja Raspberry Pi OS:ssä SSH otetaan käyttöön `raspi-config`-työkalulla.

SSH-yhteyteen käy mikä tahansa SSH-asiakasohjelma, kuten macOS:n ja Linuxin sisäänrakennettu pääte tai Windowsin PuTTY. Perusmuotoinen yhteyskomento on:

```bash
ssh username@halpi2-ip-address
```

SSH-yhteydet ovat salattuja ja turvallisia, joten ne soveltuvat käytettäviksi myös julkisissa verkoissa, kun tunnistautuminen on määritetty kunnolla. SSH tarvitsee myös hyvin vähän kaistaa, mikä tekee siitä ihanteellisen hitaiden ja viiveisten yhteyksien yli.

### VNC (Virtual Network Computing)

!!! note
    VNC koskee vain OpenPlotter- ja Raspberry Pi OS Desktop -levykuvia. HaLOS käyttää sen sijaan selainkäyttöä — katso yllä.

VNC tarjoaa etätyöpöytäyhteyden HALPI2:n graafiseen käyttöliittymään, jolloin työpöytää voi käyttää kuin olisi paikan päällä. VNC on valmiiksi asennettuna ja määritettynä OpenPlotter-levykuvissa. Raspberry Pi OS -asennuksissa VNC otetaan käyttöön `raspi-config`-työkalulla.

Etätyöpöytäyhteyteen käy RealVNC:n [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) -sovellus, joka on saatavilla Windowsille, macOS:lle, Linuxille, iOS:lle ja Androidille. VNC toimii hyvin paikallisverkoissa ja ilman internetyhteyttä, mikä tekee siitä ihanteellisen veneasennuksiin, joissa internetyhteys voi olla rajallinen tai puuttua kokonaan.

Internetin yli käytettäessä VNC vaatii lisäasetuksia, kuten porttiohjauksen tai VPN:n, koska protokolla ei sellaisenaan läpäise palomuureja ja NAT-laitteita.

### Raspberry Pi Connect

Raspberry Pi Connect tarjoaa nykyaikaisen selainpohjaisen etätyöpöytäyhteyden: HALPI2:n työpöytään voi ottaa yhteyden pelkällä selaimella ilman lisäohjelmistoja. Palvelu toimii automaattisesti palomuurien ja NAT-asetusten läpi, joten se sopii erityisen hyvin etäkäyttöön internetin yli ilman monimutkaisia verkkoasetuksia.

Toisin kuin VNC, Raspberry Pi Connect hoitaa verkon mutkat automaattisesti ja tarjoaa vaivattoman yhteyden mistä tahansa internetyhteyden päästä. Se kuitenkin edellyttää, että HALPI2:lla itsellään on toimiva internetyhteys.

## Ohjelmistopäivitykset

Säännölliset päivitykset ovat suositeltavia järjestelmän suorituskyvyn ja tietoturvan ylläpitämiseksi.

### HaLOSin päivitykset

HaLOSissa järjestelmäpaketit (mukaan lukien HALPI2:n firmware) päivitetään Cockpitista tai komentoriviltä `apt`-työkalulla. Konttipohjaiset sovellukset (Signal K, Grafana ja muut) päivitetään Cockpitin Container Apps -näkymästä, joka tarkistaa uudet konttikuvien versiot.

### Komentoriviltä tehtävät päivitykset (kaikki levykuvat)

Luotettavin tapa päivittää järjestelmä on komentorivi. Avaa pääteikkuna ja aja seuraavat komennot:

```bash
sudo apt update
sudo apt upgrade
```

Ensimmäinen komento (`apt update`) päivittää pakettitietokannan uusimpiin saatavilla oleviin versioihin, ja toinen (`apt upgrade`) lataa ja asentaa kaikki saatavilla olevat päivitykset. Tämä päivittää kaikki asennetut paketit, mukaan lukien Raspberry Pi OS:n perusjärjestelmän, OpenPlotterin osat ja HALPI2:n oman ohjelmiston.

Päivityksen aikana sinulta voidaan kysyä vahvistusta joidenkin pakettien asennukseen tai palveluiden uudelleenkäynnistykseen. Näihin voi yleensä vastata myöntävästi, ellei sinulla ole erityistä syytä kieltäytyä.

### Graafiset päivitykset

Graafista käyttöliittymää suosiville työpöytäympäristö näyttää ilmoituksen, kun päivityksiä on saatavilla. Työpöydän tehtäväpalkin oikeaan yläkulmaan ilmestyy latauskuvake, kun päivitykset ovat asennettavissa. Kuvakkeen napsauttaminen avaa päivitystenhallinnan, jossa päivitykset voi käydä läpi ja asentaa.

## Firmware-päivitykset

HALPI2:n ohjaimen firmware päivitetään Raspberry Pi OS:n tavallisella päivitysmenettelyllä, mikä pitää firmwaren ajan tasalla vaivattomasti. Säännölliset firmware-päivitykset ovat tärkeitä suorituskyvyn, uusien ominaisuuksien ja ohjelmistoyhteensopivuuden kannalta.

### Automaattiset firmware-päivitykset

Firmware-päivitykset jaetaan tavallisen järjestelmäpäivityksen kautta Debian-paketteina APT-pakettivarastosta. Tarkista ja asenna firmware-päivitykset avaamalla pääteikkuna ja ajamalla:

```bash
sudo apt update
sudo apt upgrade
```

Kun uusi HALPI2:n firmware on saatavilla, se ladataan ja asennetaan automaattisesti päivityksen yhteydessä. Järjestelmä ilmoittaa, jos saatavilla olevissa paketeissa on firmware-päivityksiä.

Firmware-paketin päivityksen jälkeen järjestelmä on käynnistettävä oikealla tavalla uudelleen, jotta muutokset tulevat voimaan. Käytä sammutuskomentoa varmistaaksesi täyden virrankatkaisun:

```bash
sudo shutdown -h now
```

**Tärkeää:** Pelkkä uudelleenkäynnistys ei riitä firmware-päivitykselle. Täysi sammutus ja käynnistys tarvitaan, koska vasta silloin ohjain käynnistyy uudelleen ja ottaa uuden firmwaren käyttöön. Ohjaimen firmware päivittyy vain virran kytkemisen yhteydessä.

### Firmwaren turvaominaisuudet

HALPI2:ssa on sisäänrakennetut suojaukset firmwaren vioittumista vastaan. Jos laite käynnistetään uudelleen 30 sekunnin kuluessa firmware-päivityksestä, järjestelmä palaa automaattisesti edelliseen firmware-versioon. Tämä suojaa ongelmallisilta firmware-päivityksiltä, jotka voisivat estää normaalin toiminnan.

### Firmwaren asennus käsin

Edistyneemmille käyttäjille ja tietyissä vianetsintätilanteissa firmwaren voi asentaa käsin HALPI-komentorivityökalulla. Firmware-tiedostot ovat hakemistossa `/usr/share/halpi2-firmware/`, ja ne voi flashata suoraan:

```bash
halpi flash <firmware_file>.bin
```

### Automaattisten firmware-päivitysten poistaminen käytöstä

Joskus halutaan pysyä tietyssä firmware-versiossa ja poistaa automaattiset päivitykset käytöstä. Tämä onnistuu muokkaamalla HALPI2:n asetustiedostoa:

```bash
sudo nano /etc/halpid/firmware.conf
```

Etsi asetus `AUTO_FLASH_ON_INSTALL` ja muuta sen arvoksi `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Tallenna tiedosto ja poistu editorista. Tämän jälkeen HALPI2 ei enää flashaa uutta firmwarea automaattisesti tavallisen päivityksen yhteydessä, joten päivitysten ajankohta on täysin sinun hallinnassasi. Firmware-päivitykset voi edelleen asentaa käsin `halpi flash` -komennolla.


## HALPI-komentorivityökalu

HALPI2:n ohjelmistorajapinta koostuu `halpid`-daemonpalvelusta ja `halpi`-komentorivityökalusta. Yhdessä ne mahdollistavat järjestelmän valvonnan, asetukset ja ohjauksen.

### HALPI-daemon (`halpid`)

HALPI-daemon toimii järjestelmäpalveluna ja välittää tietoa käyttöjärjestelmän ja HALPI2:n ohjaimen välillä. Se mahdollistaa co-op-tilan, jossa valvonta ja virranhallinta ovat täysimääräisesti käytössä.

#### Palvelun hallinta

Daemonia hallitaan systemd:llä:

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

#### Asetukset

Daemonin asetukset ovat tiedostossa `/etc/halpid/halpid.conf`. Muokkaa asetuksia komennolla:

```bash
sudo nano /etc/halpid/halpid.conf
```

Asetusmuutokset vaativat daemonin uudelleenkäynnistyksen:

```bash
sudo systemctl restart halpid
```

### HALPI-komentorivityökalu (`halpi`)

`halpi`-komento antaa suoran pääsyn ohjaimen toimintoihin ja järjestelmän tilaan. Se keskustelee daemonin kanssa suorittaakseen komentoja ja hakeakseen tietoa HALPI2:n toimintatilasta, asetuksista ja laitteiston mittausarvoista.

#### Järjestelmän tila ja valvonta

HALPI-komentorivityökalun tärkein tehtävä on näyttää kattava tilatieto järjestelmästä. Siihen kuuluvat laitteiston mittausarvot, toimintatila ja reaaliaikainen seuranta.

Järjestelmän tilan näyttäminen:

```bash
# Display comprehensive system status
halpi status
```

Komento antaa täyden yleiskuvan HALPI2:n toimintatilasta, mukaan lukien jännitteet, virrankulutuksen, lämpötilat ja ohjaimen tilan:

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

Jos haluat seurata vain yhtä arvoa, sen voi hakea näin:

```bash
# Show controller firmware version
halpi get firmware_version
```

Skriptejä varten kannattaa käyttää REST-rajapintaa, joka on kuvattu kohdassa [REST API -rajapinta](#rest-api-rajapinta).

#### Asetusten hallinta

HALPI-komentorivityökalulla voi tarkastella nykyisiä asetuksia ja muuttaa toimintaparametreja.

Nykyisten asetusten tarkastelu:

```bash
# Show current configuration
halpi config
```

Tämä näyttää kaikki säädettävät parametrit ja niiden nykyiset arvot:

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

#### LEDien ohjaus

Yksi useimmin säädetyistä asetuksista on LEDien kirkkaus, jonka voi sovittaa käyttöympäristöön ja omiin mieltymyksiin.

Esimerkkikomentoja LEDien kirkkauden hallintaan:

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

LEDien kirkkaus hyväksyy arvot väliltä 0 (täysin pois) ja 255 (suurin kirkkaus), joten etupaneelin merkkivaloja voi säätää tarkasti.

#### Virranhallinta

HALPI-komentorivityökalu tarjoaa tarpeelliset virranhallintatoiminnot järjestelmän turvalliseen käyttöön.

Esimerkkejä virranhallinnan komennoista:

```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

Sammutuskomento varmistaa, että järjestelmä sammuu turvallisesti: käyttöjärjestelmä ehtii sulkea sovellukset ja irrottaa tiedostojärjestelmät ennen kuin ohjain katkaisee virran.

#### REST API -rajapinta

Edistyneemmille käyttäjille ja omille sovelluksille HALPI-daemon tarjoaa myös REST-rajapinnan Unix-soketin kautta. Se antaa nopeamman ohjelmallisen pääsyn järjestelmän tietoihin:

Alla muutama käyttöesimerkki:

```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

REST-rajapinta on erityisen hyödyllinen valvontasovelluksille, tiedonkeruujärjestelmille ja muille ohjelmistoille, jotka tarvitsevat reaaliaikaisen pääsyn HALPI2:n tilatietoihin.

REST-rajapinnan täydellinen kuvaus on luvussa [Ohjelmistokehitys: HALPI2-daemon](../software-development/daemon.md).

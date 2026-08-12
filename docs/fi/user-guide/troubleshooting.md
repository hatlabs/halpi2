---
translated_from: 232aac811fb62f4cc46a1955e832ea282dc92332
---

# Vianetsintä

Tällä sivulla käydään läpi tavallisia HALPI2:n käytössä vastaan tulevia ongelmia ja niiden ratkaisut.

## Virransyötön ja käynnistyksen ongelmat

### Järjestelmä ei käynnisty

**Oireet:** LEDit eivät reagoi, eikä laitteessa näy elonmerkkejä virran kytkemisen jälkeen.

1. Varmista yleismittarilla E7T-liittimestä, että syöttöjännite on sallitulla alueella (10–32 V DC).
2. Tarkista virtakaapelin kytkennät — varmista että E7T-liitin on kunnolla pohjassa.
3. Jos käytät virransyöttöä NMEA 2000 -väylästä, varmista että virranrajoitus on 0,9 A ja että verkko pystyy syöttämään riittävästi virtaa.
4. Avaa kotelo ja tarkista, näkyykö vaurioita tai löysiä sisäisiä liitoksia.

### Sateenkaari-LEDit

**Oireet:** LEDit kiertävät sateenkaarikuviota eivätkä koskaan asetu vakaaseen tilaan.

Sateenkaarikuvio tarkoittaa, että ohjaimeen on kytkeytynyt virta mutta CM5:tä ei havaita. Näin voi käydä jos:

- Compute Module -moduulia ei ole asennettu tai se ei ole kunnolla paikallaan.
- Compute Module on viallinen.
- Kytketty laite syöttää harhajännitteitä, jotka estävät CM5:n käynnistymisen — kokeile irrottaa HDMI-kaapeli.

1. Irrota kaikki HDMI-näytöt ja käynnistä uudelleen sulkeaksesi pois harhajännitteiden häiriön.
2. Jos ongelma jatkuu, avaa kotelo ja varmista että CM5-moduuli on kunnolla liittimessään — tämä edellyttää emolevyn irrottamista.

### LEDit jäävät keltaisiksi

**Oireet:** LEDit etenevät punaisesta (lataus) keltaiseen (virta kytketty) mutta eivät koskaan muutu vihreiksi.

Keltainen tila tarkoittaa, että ohjain on kytkenyt virran CM5:lle ja odottaa daemonin vastausta. Jos LEDit jäävät keltaisiksi, joko käyttöjärjestelmä ei käynnisty tai HALPI-daemonia ei ole asennettu.

1. Tarkista että käynnistystilan kytkin on "Normal"-asennossa — kytkimen vieressä oleva keltainen merkkivalo palaa, kun käynnistystila on "Abnormal" (USB-käynnistys).
2. Kytke näyttö HDMI:llä nähdäksesi käynnistysvirheet tai kirjautumiskehotteen.
3. Varmista että NVMe SSD on kunnolla M.2-paikassaan.
4. Jos käyttöjärjestelmä käynnistyy normaalisti, tarkista että daemon on asennettu: `systemctl status halpid`
5. Jos daemon on asennettu mutta ei käynnissä, tarkista sen lokit: `journalctl -u halpid -e`

### Järjestelmä sammuu odottamatta

**Oireet:** Järjestelmä sammuu ilman käyttäjän toimia, vaikka ulkoinen virransyöttö on kytkettynä.

1. Tarkista syöttöjännitteen vakaus — lyhyetkin notkahdukset raja-arvon alle käynnistävät katkoajastimen. Seuraa `V_in`-arvoa reaaliajassa komennolla `halpi status`.
2. Tarkista virtakaapeli löysien liitosten ja vaurioituneiden johtimien varalta — ne voivat aiheuttaa katkeilevan kosketuksen.
3. Jos käytät virransyöttöä NMEA 2000 -väylästä, varmista että verkon jännite pysyy vakaana kuormitettuna. Muut paljon virtaa ottavat laitteet voivat aiheuttaa jännitehäviöitä.

## Firmware-päivitys epäonnistui tai peruuntui

Jos järjestelmä käynnistyy uudelleen 30 sekunnin kuluessa firmware-päivityksen jälkeen, firmware palautuu turvatoimena automaattisesti edelliseen versioon.

1. Tarkista nykyinen firmware-versio: `halpi get firmware_version`
2. Yritä päivitystä uudelleen: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Kun päivitys on asennettu, sammuta järjestelmä hallitusti: `sudo shutdown -h now`
4. Odota että järjestelmä on sammunut kokonaan ennen virran kytkemistä — anna vähintään 30 sekuntia ennen seuraavaa käynnistystä, jotta palautusmekanismi ei laukea.

## Verkko- ja liitäntäongelmat

### NMEA 2000 -dataa ei tule

**Oireet:** `candump can0` ei tulosta mitään, tai Signal K ei saa dataa.

1. Tarkista CAN-liitännän tila:
    ```bash
    ip link show can0
    ```
    Liitännän pitäisi näkyä tilassa `UP`. Jos se on `DOWN`, nosta se ylös:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Tarkista emolevyn RX-LED — sen pitäisi vilkkua, kun verkossa on liikennettä. Jos RX-LED ei vilku:
    - Varmista Micro-C-kaapelin kytkentä ja T-liittimen sijainti.
    - Tarkista että NMEA 2000 -verkossa on jännite ja että muut laitteet lähettävät.
    - Varmista että 120 Ω:n päätevastusjumpperi **ei** ole kytkettynä NMEA 2000 -verkoissa.

3. Jos RX-LED vilkkuu mutta `candump` ei näytä mitään, vika on ohjelmistossa. Tarkista CAN-liitännän asetukset:
    ```bash
    ip -details link show can0
    ```

4. Tarkista CAN-väylän virheet:
    ```bash
    ip -statistics link show can0
    ```
    Suuret virhemäärät viittaavat johdotusongelmiin, väärään tiedonsiirtonopeuteen tai väyläkilpailuun.

### RS-485:llä ei tule NMEA 0183 -dataa

**Oireet:** `/dev/ttyAMA4`-portissa ei näy dataa, tai kytketty laite ei vastaa.

1. Avaa kotelo ja tarkista RS-485-liitännän LEDit — RX-LEDin pitäisi vilkkua, kun dataa saapuu.
2. Varmista että sarjaportti on olemassa ja käytettävissä:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Tarkista johdotuksen napaisuus — RS-485 käyttää differentiaalista signalointia A- ja B-linjoilla. Keskenään vaihdetut A- ja B-kytkennät estävät tiedonsiirron.

### Ethernet-yhteys ei muodostu

1. Tarkista ethernet-kaapeli ja RJ45-liitin. Kokeile toista kaapelia.
2. Avaa kotelo ja tarkista ethernet-LEDeistä yhteyden tila.
3. Varmista yhteyden tila: `ip link show eth0`
4. Jos yhteys on ylhäällä mutta IP-osoitetta ei ole, tarkista DHCP: `sudo dhclient eth0`
5. Kiinteillä IP-asetuksilla tarkista asetukset tiedostosta `/etc/network/interfaces` tai NetworkManagerista.

## Käyttöjärjestelmän ongelmat

### Laitteeseen ei saa SSH-yhteyttä

1. Varmista että SSH on käytössä: `sudo systemctl status ssh`
2. Tarkista verkkoyhteys — vastaako laite ping-kutsuun?
3. SSH on oletuksena käytössä näytöttömissä HaLOS-levykuvissa ja OpenPlotterissa. HaLOSin Desktop-versioissa ja Raspberry Pi OS:ssä SSH otetaan käyttöön `raspi-config`-työkalulla.

### Järjestelmä on hidas tai jumittuu

1. Tarkista suorittimen lämpötila — korkea ympäristön lämpötila voi aiheuttaa lämpörajoituksen. Käytä komentoa:
    ```bash
    vcgencmd measure_temp
    ```
    Yli 80 °C:n lämpötilat kertovat lämpöongelmasta. Yritä laskea ympäristön lämpötilaa tai parantaa ilmankiertoa kotelon ympärillä.

2. Tarkista muistin käyttö: `free -h`
3. Tarkista levytila: `df -h` — täynnä oleva NVMe SSD aiheuttaa vakavia suorituskykyongelmia.
4. Tarkista karanneet prosessit: `top` tai `htop`

### Kello on väärässä sähkökatkon jälkeen

HALPI2:ssa on reaaliaikakello (RTC) ja varaparisto, jotka ylläpitävät aikaa sähkökatkojen aikana. Jos kello nollautuu:

1. Tarkista RTC-paristo — se voi vaatia vaihtoa, jos laite on ollut pitkään ilman virtaa.
2. Varmista NTP-synkronointi, kun verkkoyhteys on käytettävissä: `timedatectl status`
3. Aseta aika tarvittaessa käsin: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## LED-diagnostiikka

LED-kuvioista näkee järjestelmän tilan nopeasti:

| Oire | LED-kuvio | Todennäköinen syy |
|:-----|:----------|:------------------|
| Järjestelmä ei käynnisty | Ei LEDejä | Ei syöttöjännitettä tai laitevika |
| Jumissa käynnistyksessä | Punainen täyttyvä rivi | Superkondensaattorit latautuvat vielä — odota |
| Jumissa käynnistyksessä | Sateenkaarikuvio | CM5:tä ei havaita — tarkista moduulin paikallaanolo ja irrota näytöt |
| Jää keltaiseksi | Keltainen palkki | Käyttöjärjestelmä ei käynnisty tai daemonia ei ole asennettu |
| Odottamaton sammutus | Oranssi tai tummanvihreä palkki, sitten violetti | Syöttöjännite menetetty, sammutus varavirralla — tarkista syöttöjännite |
| Järjestelmä käynnistyy itsestään uudelleen | Kaikki LEDit palavat punaisina ennen uudelleenkäynnistystä | Vahtikoiran aikakatkaisu — käyttöjärjestelmä lakkasi vastaamasta ja ohjain käynnisti sen uudelleen |
| Vika | Kaikki LEDit vilkkuvat punaisina | Superkondensaattorien ylijännite — ota yhteyttä tukeen |

!!! quote "Aiheeseen liittyvää"
    - **LED-kuviot:** katso [Tila-LEDit](./operation.md#tila-ledit)
    - **Toiminta sähkökatkoissa:** katso [Kun virransyöttö katkeaa](./operation.md#kun-virransyotto-katkeaa)
    - **Daemonin hallinta:** katso [Ohjelmisto-opas](./software.md#halpi-daemon-halpid)
    - **CAN-liitännän tiedot:** katso [Liitännät ja tiedonsiirto](./interfaces.md#can-fd-nmea-2000)
    - **RS-485-liitännän tiedot:** katso [Liitännät ja tiedonsiirto](./interfaces.md#rs-485-nmea-0183)

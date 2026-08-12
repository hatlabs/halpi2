---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Emolevyn ohjain

HALPI2:n emolevyllä on RP2040-mikro-ohjain, joka hallitsee virransyöttöä, valvoo järjestelmää ja ohjaa etupaneelin LEDejä. Ohjain toimii Compute Modulesta riippumatta: se on toiminnassa siitä hetkestä, kun syöttöjännite kytketään — ennen käyttöjärjestelmän käynnistymistä ja sen sammumisen jälkeen. Compute Module keskustelee ohjaimen kanssa I2C-väylän kautta (väylä 1, osoite `0x6d`) [HALPI-daemonin](../user-guide/software.md#halpi-komentorivityokalu) välityksellä.

Tällä sivulla kuvataan ohjaimen toimintatilat, tilasiirtymät ja asetukset. Sivu dokumentoi firmware-version 3.3.x. Päivittäisessä käytössä mitään tästä ei tarvitse lukea — katso sen sijaan [Päivittäinen käyttö](../user-guide/operation.md).

## Toimintatilat

Ohjain toimii kahdessa tilassa sen mukaan, onko HALPI-daemon yhteydessä siihen.

### Co-op-tila

Co-op-tila on normaali toimintatila. Se on käytössä, kun HALPI-daemon (`halpid`) on käynnissä ja yhteydessä ohjaimeen. Esiasennettu HaLOS-levykuva ja kaikki Hat Labsin käyttöjärjestelmälevykuvat sisältävät daemonin.

Co-op-tilassa:

- Ohjain ja daemon vaihtavat tietoa reaaliajassa: jännitteet, virran, lämpötilat ja tilan.
- Jännitteen menetykset välitetään daemonille, joka käynnistää käyttöjärjestelmän hallitun sammutuksen.
- Vahtikoira-ajastin suojaa käyttöjärjestelmän jumiutumiselta (katso [Vahtikoirasuojaus](#vahtikoirasuojaus)).
- Asetuksia voi lukea ja muuttaa `halpi`-komentorivityökalulla.

### Solo-tila

Solo-tila on varatila. Ohjain siirtyy siihen, kun daemon-yhteyttä ei ole:

- käynnistyksen aikana, ennen kuin daemon on käynnistynyt
- jos daemonia ei ole asennettu, se on poistettu käytöstä tai se on kaatunut
- käyttöjärjestelmissä, joissa ei ole HALPI2-tukea

Solo-tilassa ohjain suojaa edelleen jännitteen menetykseltä, mutta karkeammalla mekanismilla: se pyytää sammutusta simuloimalla virtapainikkeen painalluksia, eikä se voi tietää, saiko käyttöjärjestelmä sammutuksen vietyä hallitusti loppuun.

!!! tip "Solo-tilan luotettavuus"
    Solo-tila tarjoaa välttämättömän suojauksen, mutta on co-op-tilaa epävarmempi. Simuloidut painikkeen painallukset eivät toimi, jos käyttöjärjestelmä on jumissa. Jos käytät omaa käyttöjärjestelmää, asenna HALPI-daemon — katso [Muut Debian-jakelut](../software-development/ubuntu-installation.md).

## Jännitteen menetys ja sammutusjärjestykset

Ohjain valvoo syöttöjännitettä jatkuvasti. Syöttöjännite katsotaan menetetyksi, kun se laskee alle 9,0 V:n. Katkoajastin (oletuksena 5 sekuntia) erottaa lyhyet häiriöt todellisista katkoista: superkondensaattorit siltaavat katkon, ja jos virta palaa ajastimen kuluessa, mitään muuta ei tapahdu.

### Sammutusjärjestys co-op-tilassa

1. Daemon havaitsee jännitteen menetyksen ohjaimen jännitemittauksista.
2. Daemon odottaa, että katkoajan raja (oletuksena 5 sekuntia) ylittyy.
3. Daemon suorittaa asetetun sammutuskomennon (oletuksena `/sbin/poweroff`).
4. Käyttöjärjestelmä sammuu hallitusti superkondensaattorien virralla.
5. Ohjain havaitsee Compute Modulen sammuneen ja katkaisee 5 V:n jännitteen.
6. Jos sammutus ei valmistu 60 sekunnissa, ohjain katkaisee virran pakolla.
7. Järjestelmä pysyy pois päältä, kunnes syöttöjännite palaa, ja käynnistyy sitten automaattisesti uudelleen.

### Sammutusjärjestys solo-tilassa

1. Ohjain havaitsee jännitteen menetyksen ja käynnistää katkoajastimen (oletuksena 5 sekuntia).
2. Kun ajastin umpeutuu, ohjain simuloi virtapainikkeen kaksoispainalluksen.
3. Käyttöjärjestelmä reagoi ja aloittaa hallitun sammutuksen superkondensaattorien virralla.
4. Jos sammutus ei valmistu 60 sekunnissa, ohjain katkaisee virran pakolla.
5. Järjestelmä pysyy pois päältä, kunnes syöttöjännite palaa, ja käynnistyy sitten automaattisesti uudelleen.

### Uudelleenkäynnistys ohjelmallisen sammutuksen jälkeen

Ohjelmallisesti käynnistetty sammutus syöttöjännitteen ollessa kytkettynä (esimerkiksi `shutdown`-komennolla tai työpöydän valikosta) päättyy *sammutettu*-tilaan. Jatko riippuu `auto_restart`-asetuksesta:

- `auto_restart` pois käytöstä (tehdasasetus vuoden 2026 alusta alkaen valmistetuissa laitteissa): järjestelmä pysyy pois päältä, kunnes syöttöjännite katkaistaan ja kytketään uudelleen tai virtapainiketta painetaan.
- `auto_restart` käytössä (firmwaren oletusarvo ja tehdasasetus aiemmissa laitteissa): ohjain käynnistää järjestelmän uudelleen 5 sekunnin kuluttua, jotta valvomaton järjestelmä ei jää pois päältä vahingossa annetun sammutuskomennon takia.

Muuta asetusta komennolla `halpi config set auto_restart <true|false>`.

Virtapainikkeen painallus tai syöttöjännitteen katkaisu ja uudelleenkytkentä käynnistää järjestelmän aina `auto_restart`-asetuksesta riippumatta.

## Vahtikoirasuojaus

Co-op-tilassa vahtikoira-ajastin (watchdog) suojaa käyttöjärjestelmän jumiutumiselta:

- Daemonin on lähetettävä ohjaimelle vahtikoiraviesti säännöllisin väliajoin.
- Jos viestiä ei saavu vahtikoiran aikakatkaisun kuluessa (oletuksena 10 sekuntia), ohjain toteaa isäntäjärjestelmän vastaamattomaksi, näyttää hälytyskuvion (kaikki LEDit palavat punaisina) ja katkaisee ja kytkee Compute Modulen virran palauttaakseen järjestelmän toimintaan.
- Aikakatkaisun voi asettaa komennolla `halpi config set watchdog_timeout <seconds>`.

## Valmiustila

Valmiustilassa Compute Modulen virta katkaistaan, mutta ohjain jää toimintaan odottamaan ajastettua herätystä:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Siirtymän aikana kaikki LEDit palavat sinisinä; valmiustilassa ne palavat himmeän punaisina. Ohjain käynnistää järjestelmän ajastettuna ajankohtana, virtapainikkeen painalluksesta tai kun syöttöjännite katkaistaan ja kytketään uudelleen.

## Tila-LEDien kuviot

Etupaneelin viisi RGB-LEDiä heijastavat ohjaimen tilaa. Tämä taulukko on ohjaimen tilojen ja LED-kuvioiden virallinen vastaavuus; [Päivittäinen käyttö](../user-guide/operation.md#tila-ledit) -sivulla on yksinkertaistettu versio.

| Ohjaimen tila | LED-kuvio |
|:--------------|:----------|
| PowerOff (ei käyttökelpoista syöttöjännitettä; ohjain toimii jäännösvarauksella) | LED 5 palaa punaisena |
| OffCharging | Punainen palkki täyttyy superkondensaattorien latautuessa |
| SystemStartup | Sateenkaaripyyhkäisy, sitten tasaisten värien kierto |
| OperationalSolo | Keltainen varaustasopalkki |
| OperationalCoOp | Vihreä varaustasopalkki |
| BlackoutSolo | Oranssi varaustasopalkki |
| BlackoutCoOp | Tummanvihreä varaustasopalkki |
| BlackoutShutdown, ManualShutdown | Violetti varaustasopalkki |
| PoweredDownBlackout, PoweredDownManual | Kaikki sammuneet |
| HostUnresponsive (vahtikoiran aikakatkaisu) | Kaikki palavat punaisina |
| EnteringStandby | Kaikki palavat sinisinä |
| Standby | Kaikki himmeän punaisina |
| Superkondensaattorien ylijännitehälytys | Kaikki LEDit vilkkuvat punaisina |

Varaustasopalkkien kuvioissa kukin palava LED vastaa yhtä volttia superkondensaattorien jännitettä:

| LED | Jännitealue |
|:----|:------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Asetusparametrit

Asetukset tallennetaan ohjaimen flash-muistiin, ja ne säilyvät virtakatkojen yli. Lue ja muuta niitä `halpi config` -komennolla — katso [Ohjelmisto-opas](../user-guide/software.md#asetusten-hallinta).

| Parametri | Oletusarvo | Kuvaus |
|:----------|:-----------|:-------|
| `auto_restart` | `false` nykyisissä laitteissa (asetetaan tuotantotestissä); firmwaren oletusarvo `true` | Käynnistä automaattisesti uudelleen 5 s ohjelmallisen sammutuksen jälkeen, kun syöttöjännite on kytkettynä |
| `watchdog_timeout` | 10 s | Co-op-tilan vahtikoiran aikakatkaisu |
| `power_on_threshold` | 8,0 V | Superkondensaattorien jännite, joka vaaditaan ennen Compute Modulen käynnistämistä |
| `solo_power_off_threshold` | 5,5 V | Superkondensaattorien jännite, jossa ohjain katkaisee virran pakolla solo-tilassa |
| `solo_depleting_timeout` | 5 s | Solo-tilan katkoajastin |
| `led_brightness` | 48 | Etupaneelin LEDien kirkkaus (0–255) |

Co-op-tilan katkoajastin ja sammutuskomento ovat daemonin asetuksia, jotka määritellään tiedostossa `/etc/halpid/halpid.conf` (`blackout-time-limit`, oletuksena 5 s; `poweroff`, oletuksena `/sbin/poweroff`).

!!! quote "Aiheeseen liittyvää"
    - **Päivittäinen käyttö:** katso [Päivittäinen käyttö](../user-guide/operation.md)
    - **Virransyöttöjärjestelmän tiedot:** katso [Virtalähde tarkemmin](./power-supply.md)
    - **Firmware-päivitykset:** katso [Ohjelmisto-opas](../user-guide/software.md#firmware-paivitykset)
    - **Firmwaren lähdekoodi ja I2C-protokolla:** katso [HALPI2-firmware-repositorio](https://github.com/hatlabs/HALPI2-firmware)

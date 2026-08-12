---
translated_from: 14cb3c2c516710194d6d97569111c8626e6fc6ea
---

# Johdanto

HALPI2 on käyttövalmis venetietokone, joka perustuu Raspberry Pi Compute Module 5 -moduuliin (CM5). Siinä on kattava valikoima ominaisuuksia, jotka sopivat hyvin vene-, ajoneuvo- ja moniin teollisuussovelluksiin.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Linkki verkkokauppaan"
    Osta HALPI2 [Hat Labsin verkkokaupasta](https://shop.hatlabs.fi/products/halpi2-computer).

## Mikä HALPI2 on?

HALPI2 edustaa kestäväksi rakennetun sulautetun tietotekniikan uusinta sukupolvea: se yhdistää Raspberry Pi:n suorituskyvyn ja ekosysteemin vaativiin ympäristöihin suunniteltuihin erikoisominaisuuksiin. Toisin kuin tavalliset yhden piirilevyn tietokoneet, HALPI2 on suunniteltu alusta asti jatkuvaan käyttöön olosuhteissa, joissa luotettavuus on ratkaisevaa.

Järjestelmä yhdistää Raspberry Pi Compute Module 5 -moduulin ja räätälöidyn emolevyn vesitiiviiseen alumiinikoteloon, joka toimii samalla jäähdytyselementtinä. Ratkaisu tarjoaa nykyaikaisten sovellusten vaatiman laskentatehon ja säilyttää silti vene- ja teollisuuskäytön edellyttämän kestävyyden.

## Tärkeimmät ominaisuudet

### Kotelon ominaisuudet

- **Vesitiivis (IP65) alumiinikotelo**, koko 200×130×60 mm
- **Vakioliittimet**: virransyöttö, NMEA 2000, gigabit-ethernet, HDMI, 2× USB 3.0 sekä WiFi/Bluetooth-antenni
- **Joustavat liitäntävaihtoehdot**: 3× PG7-läpivientiholkki tai vesitiiviit SP13-liittimet
- **Ulkoisten antennien tuki**: aukot kahdelle ylimääräiselle SMA-liittimelle
- **Seinäkiinnitykseen suunniteltu rakenne**, jossa liittimet on sijoitettu asennuksen kannalta kätevästi

![HALPI2:n liitinsijoittelu](./user-guide/front-panel-connectors-all.jpg)

### Laitteiston ominaisuudet

- **Laaja syöttöjännitealue** 10–32 V DC, suojaus 100 V DC asti
- **Älykäs virranrajoitus**: suurin syöttövirta 0,9 tai 2,5 A, käyttäjän valittavissa
- **Kaksi virransyöttötapaa**: suora 12 V:n tai 24 V:n liitäntä tai 12 V:n syöttö NMEA 2000 -väylästä
- **Superkondensaattorivarmennus** häiriönsietoa ja hallittua sammutusta varten jännitteen katketessa
- **Kehittynyt virranhallinta**, joka tunnistaa jännitteen menetyksen automaattisesti
- **Passiivinen jäähdytys**: CM5 on suorassa kosketuksessa koteloon
- **Nopea massamuisti** vakiomuotoisen M.2 NVMe SSD -liitännän kautta
- **Laajennettavuus** vakiomuotoisen 40-nastaisen Raspberry Pi GPIO-liittimen kautta
- **Monipuoliset I/O-liitännät**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, gigabit-ethernet
- **Veneilyyn suunnatut liitännät**: CAN FD (NMEA 2000) ja RS-485 (NMEA 0183)
- **Reaaliaikakello** ja varaparisto tarkkaa ajanpitoa varten
- **Näkyvä tilatieto** viiden RGB-LEDin avulla
- **Käyttäjän ohjaus** konfiguroitavien painikeliittimien kautta

![Näkymä HALPI2:n sisälle](./halpi2-interior.jpg)
*Näkymä HALPI2:n sisälle: emolevy ja eri liittimet.*

### Ohjelmiston ominaisuudet

- **Valmiiksi määritellyt käyttöjärjestelmän levykuvat** heti käyttöönotettaviksi: [HaLOS](https://docs.halos.fi) (oletus), OpenPlotter, Raspberry Pi OS ja Raspberry Pi OS Lite
- **Kattava valvonta**: jännite, virta ja lämpötila
- **Huomaamattomat firmware-päivitykset** I2C-väylän kautta

## Käyttökohteet

### Venesovellukset

- **Navigointijärjestelmät**, joissa on karttaplotteri ja GPS-integraatio
- **Tiedonkeruu** moottorin mittaustiedoista, ympäristöantureista ja aluksen suorituskyvystä
- **Signal K -palvelimet** veneen tietojen yhtenäiseen hallintaan
- **Yleiskäyttöinen tietokone veneessä** internetyhteyttä ja viestintää varten
- **NMEA 2000 -verkon vianetsintä** järjestelmän luotettavuuden parantamiseksi

### Teollisuussovellukset

- **Prosessivalvonta** ja ohjausjärjestelmät
- **Ympäristön mittaus** ja tiedonkeruu
- **Etävalvonta-asemat**
- **Laitteiden automaatio** ja ohjaus
- **Ennakoivan kunnossapidon** järjestelmät

### Ajoneuvosovellukset

- **Kalustonhallintajärjestelmät**
- **Telematiikka** ja ajoneuvojen seuranta
- **Ajoneuvon viihde- ja tietojärjestelmät**
- **Diagnostiikka- ja valvonta-alustat**

## Pakkauksen sisältö

HALPI2-pakkaus sisältää:

- **HALPI2-laitteen**, jossa on valmiiksi asennettuna Compute Module 5 ja NVMe SSD (ellei tilattu ilman)
- **Virtakaapelin** E7T-liittimellä (yhteensopiva Amphenol LTW Ceres Mini -liittimen kanssa), pituus 2 m
- **E7T-kaapeliliittimen** räätälöityihin asennuksiin
- **DC-pyöröliitinparin** (5,5 × 2,1 mm) tavallisia 12 V:n ja 24 V:n virtalähteitä varten
- **Raspberry Pi -antennin** WiFi- ja Bluetooth-yhteyksiä varten
- **Kolme PG7-läpivientiholkkia** lisäliitäntöjä varten
- **Pika-aloitusoppaan ja takuuasiakirjat**

![HALPI2:n tarvikepussin sisältö](./goodie-bag-contents.jpg)

Erikseen saatavat lisätarvikkeet:

- **NMEA 2000 -haarakaapeli** väyläsyöttöä käyttäviin asennuksiin
- **Erilaiset liitinsarjat** räätälöityihin asennuksiin

## Näin käytät tätä dokumentaatiota

Dokumentaatio on jäsennelty palvelemaan sekä käytännön ohjeita etsiviä loppukäyttäjiä että yksityiskohtaista teknistä tietoa tarvitsevia kehittäjiä.

### Loppukäyttäjälle

- Aloita **Aloitusoppaasta**, joka käy läpi käyttöönoton ja asennuksen
- Lue **Päivittäinen käyttö** -sivulta päivittäisen käytön perusteet: LEDien merkitykset, sammutus ja toiminta sähkökatkoissa
- Katso **Vianetsintä**, jos ongelmia ilmenee

### Kehittäjälle

- Tutustu **Teknisiin tietoihin** yksityiskohtaisten määritysten osalta
- Perehdy **Ohjelmistokehitys**-osioihin räätälöityjä sovelluksia varten
- Tarkastele **Suunnittelutiedostoja** integraation suunnittelussa

### Dokumentaation merkinnät

- 💡 **Vinkkilaatikot** tarjoavat oikoteitä tavallisiin tehtäviin
- ⚠️ **Varoitukset** ja **huomautukset** nostavat esiin tärkeää turvallisuustietoa
- 🔧 **Tekniset yksityiskohdat** -osiot tarjoavat syvällistä toteutustietoa
- 📖 **Ristiviittaukset** yhdistävät toisiinsa liittyvät aiheet läpi dokumentaation

Olitpa ottamassa käyttöön ensimmäistä venetietokonettasi tai kehittämässä räätälöityä teollisuusratkaisua, tämä dokumentaatio opastaa sinut HALPI2:n käytön jokaisessa vaiheessa.

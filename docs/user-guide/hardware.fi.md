# Laitteisto-opas

## Kotelon käsittely

HALPI2:n kotelo on jauhemaalattua painevalettua alumiinia, ja siinä on valmiit reiät paneeliliittimille. Kun kotelon sisälle on päästävä muutoksia tai huoltoa varten, toimi alla olevien ohjeiden mukaan.

### Kotelon avaaminen

Varmista ensin, että laitteessa ei ole virtaa ja virtakaapelit on irrotettu. Kansi on kiinnitetty neljällä uppokantaisella M4×10-ruuvilla, joissa on PH2-kanta. Irrota ruuvit PH2-ruuvimeisselillä ja nosta kansi pois.

### Kokoaminen

Ennen kotelon sulkemista varmista, että kaikki sisäiset liitokset ovat tukevasti paikallaan. Reititä kaapelit huolellisesti niin, etteivät ne jää puristuksiin tai taivu jyrkästi.

Taipuisat litteät kaapelit (FFC) on helppo kytkeä vahingossa väärin päin. Tarkista oikea suunta silkkipainon Contacts-nuolista.

Kiinnitä erityistä huomiota kannen tiivisteeseen: tarkista ettei siinä ole vaurioita, roskia tai siirtymiä, jotka heikentäisivät kotelon säänkestävyyttä.

Kiinnitä kannen neljä M4×10-ruuvia takaisin PH2-ruuvimeisselillä. Älä ylikiristä.


## Paneeliliittimet

### Vakiokokoonpano

HALPI2 toimitetaan vakioliitinkokoonpanolla, joka sopii useimpiin käyttökohteisiin. Oletuskokoonpanoon kuuluvat:

- **E7T-virtaliitin**
- **NMEA 2000 -microliitin**
- **Gigabit-ethernet RJ45**
- **HDMI-lähtö**
- **2× USB 3.0 Type-A**
- **3× PG7-läpivientipaikkaa** (umpitulpilla)
- **2× RP-SMA-antennipaikkaa** (umpitulpilla)
- **Tasausventtiili** paineentasausta varten

![Etupaneelin liittimet ja umpitulpat](./front-panel-connectors-all.jpg)
*Etupaneelin liittimet ja umpitulpat. Vihreällä merkityt liittimet kuuluvat vakiokokoonpanoon. Keltaiset paikat ovat umpitulppia, jotka voi tarvittaessa korvata liittimillä. Punainen paikka on tasausventtiili, jota ei saa poistaa.*

### Muut liitinvaihtoehdot

Jos tarvitset toisenlaisia liittimiä, paneelikokoonpanoa voi muuttaa:

#### Liittimien irrottaminen

!!! warning "Tärkeää"
    Muuta liittimiä vain kun laitteessa ei ole virtaa ja se on irrotettu kaikista lähteistä.

    Muovikierteet voivat vaurioitua ylikiristettäessä. Käytä tavallisia kuusiohylsyjä, mutta kiristä vain sormivoimin.

1. **Käytä oikean kokoista hylsyä:**
   - Suuret liittimet: 26 mm:n hylsy
   - M6-nailonpultit: 10 mm:n hylsy
   - RP-SMA-liittimet: 8 mm:n hylsy
   - PG7-paikat: iso talttapäämeisseli, 17 mm:n hylsy

2. **Irrota varoen** — muovikierteet voivat vaurioitua ylikiristettäessä

3. **Säilytä irrotetut osat** myöhempää käyttöä varten

#### Uusien liittimien asentaminen

1. **Käytä vain merikäyttöön hyväksyttyjä** tai muuten olosuhteisiin sopivia liittimiä
2. **Varmista kunnollinen tiivistys** — sisäpuolelle tarvitaan leveä laippa
3. **Kiristä vain sormivoimin** — älä ylikiristä muovikierteitä
4. **Sovita paikalleen** ennen lopullista asennusta

## Sisäinen rakenne

- HALPI2:n emolevy on tietokoneen pääkortti, jonka alapuolella on Compute Module 5 (CM5) ja joka hoitaa virranhallinnan, merkkivalot ja kaikkien liitäntöjen kytkennät.

### Emolevyn toiminnalliset alueet

Emolevyn tärkeimmät toiminnalliset alueet näkyvät alla olevassa kuvassa.

![Emolevyn yläpuolen rakenne](./carrier-board-top-layout.jpg)
*Emolevyn yläpuolen rakenne ja keskeiset toiminnalliset alueet.*

### Emolevyn liittimet

Toiminnot ovat käytettävissä kortilla olevien liittimien kautta, jotka näkyvät alla olevassa kuvassa.

![Emolevyn liittimet, yläpuoli](./carrier-board-top-conx.jpg)
*Emolevyn liittimet, yläpuoli.*

Alla on luettelo yläpuolen liittimistä.

| Merkintä | Kuvaus |
|:---------|:-------|
| **a1** | Virtaliitin (Phoenix MC -tyyppi, 3,81 mm:n jako) |
| **a2** | Syöttövirran rajoituskytkin (0,9 A tai 2,5 A) |
| **a3** | Virranohjausjumpperi. Oikosulje 3.3V off -nastat pakottaaksesi 3,3 V:n jännitteen pois. Oikosulje 5V on -nastat pakottaaksesi 5 V:n jännitteen päälle. **Huom:** Version 0.4.0 korteilla liittimet **a3** ja **c2** on järjestetty toisin. |
| **b1** | Ethernet-portti (RJ45) |
| **c1** | Ohjaimen USB-portti. Käytetään RP2040-mikro-ohjaimen firmwaren flashaukseen. |
| **c2** | MCU USB BOOT -jumpperiliitin. Oikosulje nastat asettaaksesi RP2040:n USB-käynnistystilaan. |
| **c3** | Ohjaimen vianetsintäliitin |
| **c4** | Juottamaton ohjaimen GPIO-liitin |
| **c5** | Painikeliittimet. Käytetään Power-, Reset- ja User-painikkeiden kytkemiseen. |
| **c6** | Virtapainike. Käytetään Compute Module 5:n käynnistämiseen ja sammuttamiseen. |
| **d1** | Raspberry Pi:n 40-nastainen GPIO-liitin |
| **e1** | MIPI0-liitin kameralle tai näytölle |
| **e2** | MIPI1-liitin kameralle tai näytölle |
| **f1** | HDMI0-liitin |
| **f2** | HDMI1-liitin |
| **g1** | M.2 NVMe SSD -liitin |
| **h1** | CAN FD -liitäntä (Phoenix MC -tyyppi, 3,81 mm:n jako) |
| **h2** | CAN-päätevastusjumpperi. Oikosulje nastat kytkeäksesi CAN FD -väylän päätevastuksen. |
| **i1** | RS-485-liitäntä (Phoenix MC -tyyppi, 3,81 mm:n jako) |
| **i2** | RS-485:n automaatti-/käsiohjausjumpperi. |
| **i4** | XRS-485 RX Enable -jumpperi. Oikosulje nastat ottaaksesi RS-485-vastaanoton käyttöön. |
| **j1** | Compute Modulen USB Boot -liitin. Käytetään Compute Module 5:n firmwaren flashaukseen. |
| **j2** | Compute Modulen käynnistystilan valintakytkin. Aseta "Normal" normaaliin käyttöön ja "Abnormal" USB-käynnistystilaan. Varoitus-LED syttyy, kun kytkin on "Abnormal"-asennossa. |
| **m1** | USB3-liitin 0. Kytketty suoraan CM5:een. |
| **m2** | USB3-liitin 1-0. Kytketty kortin USB3-hubiin. |
| **m3** | USB3-liitin 1-1. Kytketty kortin USB3-hubiin. |
| **m4** | USB3-liitin 1-2. Kytketty kortin USB3-hubiin. |
| **n1** | CR2032-paristopidike reaaliaikakellolle (RTC) |
| **q1** | CM5:n tuuletinliitin. Tuulettimella voi parantaa ilmankiertoa kotelon sisällä. Vakiokotelossa sitä ei tarvita. |

![Emolevyn liittimet, alapuoli](./carrier-board-bottom-conx.jpg)
*Emolevyn liittimet, alapuoli.*

Alla on luettelo alapuolen liittimistä.

| Merkintä | Kuvaus |
|:---------|:-------|
| **p1** | Compute Module 5 -liitin. |
| **q1** | CM5:n tuuletinliitin, vaihtoehtoinen paikka. Tähän voi kytkeä suorittimen tuulettimen CM5-moduulin päälle, kun käytetään räätälöityä koteloa. **Huom:** Liittimet **q1** ja **q2** on kytketty rinnan, eikä niitä saa käyttää yhtä aikaa. |

Lopuksi: WiFi- ja Bluetooth-antennin liitin on itse Compute Module 5:llä. Se näkyy alla olevassa kuvassa.

![WiFi-antennin liitin](./cm5-top-conx.jpg)
*U.FL-antenniliitin Compute Module 5:llä.*

| Merkintä | Kuvaus |
|:---------|:-------|
| **r1** | U.FL-liitin WiFi- ja Bluetooth-antennille. |

### Blinkenlights

Emolevyllä on useita tila-LEDejä järjestelmän seurantaan.

![Emolevyn tila-LEDit](./carrier-board-top-leds.jpg)
*Emolevyn tila-LEDit ja niiden värit.*

Tila-LEDit kertovat järjestelmän virransyötön ja toiminnan tilasta. Alla on luettelo tila-LEDeistä.

| Merkintä | Väri | Kuvaus |
|----------|:-----|:-------|
| **1** | RGB | Viisi RGB-LEDiä. Nämä LEDit näyttävät järjestelmän tilan ja toiminnan etupaneelissa. |
| **2** | Punainen | 3,3 V:n ja 5 V:n jännitteiden merkkivalot. Kertovat kyseisten jännitteiden tilan. |
| **3** | Keltainen | Ethernetin nopeusnäyttö. Palaa, kun ethernet-portti on neuvotellut 100/1000 Mbit/s yhteyden. |
| **4** | Vihreä | Ethernetin toimintanäyttö. Vilkkuu, kun ethernet-portissa on liikennettä. |
| **5** | Sininen | SSD:n toimintanäyttö. Vilkkuu, kun M.2 NVMe SSD:llä on luku- tai kirjoitustoimintaa. |
| **6** | Punainen | Pi:n virtatilan näyttö. Palaa, kun järjestelmässä on virta mutta se on sammutettu. |
| **7** | Vihreä | Pi:n toimintanäyttö. Vilkkuu, kun Raspberry Pi:llä on toimintaa. |
| **8** | Keltainen | Abnormal-käynnistystilan varoitus. Palaa, kun USB-käynnistystilan kytkin on "Abnormal"-asennossa. Tämä kertoo, että laite on asetettu flashattavaksi USB Boot -liittimen kautta eikä käynnisty normaalisti. |
| **9** | Vihreä | CAN TX/RX -LEDit. Vilkkuvat, kun CAN-liitännässä vastaanotetaan (RX) tai lähetetään (TX) dataa. |
| **10** | Vihreä | RS-485 TX/RX -LEDit. Vilkkuvat, kun RS-485-liitännässä vastaanotetaan (RX) tai lähetetään (TX) dataa. |

RGB-LEDien kuviot on kuvattu [Järjestelmän käyttö](./operation.md#tila-ledit) -sivulla.

## Virranrajoituksen asetus

Emolevyllä on virranrajoituskytkin, jolla asetetaan oheislaitteille syötettävä enimmäisvirta. Kytkimen paikan löydät kohdan [Emolevyn liittimet](#emolevyn-liittimet) kuvasta merkinnällä **a2**.

!!! info "Virranrajoituksen asetukset"
    **0,9 A (oletus):**

    - Pakollinen NMEA 2000 -väyläsyötössä
    - Riittää perustason käyttöön

    **2,5 A:**

    - Paljon virtaa kuluttaville oheislaitteille
    - Nopeampi superkondensaattorien lataus
    - Vain oman virtaliitännän kanssa

Muuta virranrajoitusta sammuttamalla HALPI2 kokonaan ja irrottamalla kotelon kansi Kotelon käsittely -osion ohjeen mukaan. Paikanna virranrajoituskytkin emolevyltä ja siirrä se haluttuun asentoon (0,9 A tai 2,5 A). Kun asetus on muutettu, kokoa kotelo ja varmista että kaikki liitokset pysyvät tukevina.

## HATtien käyttö

### HATtien yhteensopivuus

HALPI2 tukee tavallisia Raspberry Pi -HATteja 40-nastaisen GPIO-liittimensä kautta ja on täysin sähköisesti ja mekaanisesti yhteensopiva Raspberry Pi:n HAT-määrittelyn kanssa. Emolevyn GPIO-nastajärjestys on sama kuin tavallisessa Raspberry Pi:ssä, joten useimmat Raspberry Pi 4:lle ja 5:lle suunnitellut HATit toimivat ilman muutoksia. Yhteensopivuus koskee sekä virallisia Raspberry Pi -HATteja että HAT-standardia noudattavia kolmannen osapuolen laajennuskortteja.

### Fyysiset rajoitteet

HALPI2:n kotelossa on 45 mm vapaata korkeutta emolevyn yläpuolella, mikä riittää enintään kahdelle päällekkäiselle HATille. HAT-alueen vasemmalla puolella ovat superkondensaattorit, mikä rajoittaa tilaa HATeilta, jotka ylittävät vakiokoon 65 × 56 mm. Kiinnitä erityistä huomiota HATteihin, joissa on liittimiä sivuilla. "Etelään" tai "itään" osoittavat liittimet ovat yleensä kunnossa, mutta "länteen" osoittavat voivat osua superkondensaattoreihin.

### GPIO-nastojen ristiriidat

HALPI2:n sisäiset liitännät käyttävät useita GPIO-nastoja, mikä on otettava huomioon HATteja valittaessa. Alla olevassa taulukossa on varatut GPIO-nastat ja niiden toiminnot:

| GPIO-numero | Toiminto | Liitäntä | Huomiot |
|-------------|----------|----------|---------|
| GPIO 2 | I2C SDA | Järjestelmän I2C | Voidaan jakaa; osoite 0x6d varattu |
| GPIO 3 | I2C SCL | Järjestelmän I2C | Voidaan jakaa; osoite 0x6d varattu |
| GPIO 6 | SPI CS | CAN FD | Oma piirinvalinta CAN-ohjaimelle |
| GPIO 9 | SPI MISO | CAN FD | Jaettu SPI0-väylä |
| GPIO 10 | SPI MOSI | CAN FD | Jaettu SPI0-väylä |
| GPIO 11 | SPI SCK | CAN FD | Jaettu SPI0-väylä |
| GPIO 12 | UART TX | RS-485 | UART4:n lähetys |
| GPIO 13 | UART RX | RS-485 | UART4:n vastaanotto |
| GPIO 24 | RS-485 EN | RS-485 | Enable-signaali (vain käsiohjaustilassa) |
| GPIO 26 | CAN INT | CAN FD | CAN-ohjaimen keskeytyslinja |

### Liitäntöjen jakaminen ja ristiriidat

GPIO 2:n ja 3:n I2C-väylän voi jakaa HAT-laitteiden kanssa, koska I2C tukee useita laitteita samalla väylällä. HATit eivät kuitenkaan saa käyttää I2C-osoitetta 0x6d, joka on varattu HALPI2:n järjestelmäohjaimelle. Useimmat I2C-HATit toimivat ongelmitta, mutta tarkista käytetyt I2C-osoitteet ennen asennusta.

CAN FD -liitännän käyttämän SPI0-väylän voi mahdollisesti jakaa muiden SPI-laitteiden kanssa, koska HALPI2 käyttää omaa piirinvalinta- (GPIO 6) ja keskeytysnastaa (GPIO 26). HATit, jotka käyttävät SPI0:aa vakiopiirinvalintanastoilla (GPIO 7 tai GPIO 8), voivat toimia CAN-liitännän rinnalla, mutta ne voivat vaatia lisämäärittelyjä device tree -overlayhin.

### Sisäisten liitäntöjen poistaminen käytöstä

Jos HAT tarvitsee yksinoikeudella nastoja, jotka HALPI2:n sisäiset liitännät varaavat, nämä liitännät voi poistaa käytöstä laitteistomuutoksilla. CAN FD -liitännän saa kokonaan vapautettua poistamalla emolevyn alapuolella olevan GPIO6-CAN.CS-juotosjumpperin. Muutos irrottaa CAN-ohjaimen SPI-väylästä ja vapauttaa GPIO 6:n, 9:n, 10:n, 11:n ja 26:n HATin käyttöön.

RS-485-liitännän saa pois käytöstä poistamalla emolevyn RX Enable -jumpperin (i4). Tämä estää RS-485-lähetinvastaanotinta vastaanottamasta dataa ja vapauttaa GPIO 12:n ja 13:n muuhun käyttöön. Jos lähetyksen käsiohjausta ei tarvita, myös GPIO 24:n voi ottaa muuhun käyttöön asettamalla RS-485:n automaatti-/käsiohjausjumpperin (i2) automaattitilaan.

### Asennus

Aloita sammuttamalla järjestelmä ja irrottamalla kaikki virtalähteet. Irrota kotelon kansi Kotelon käsittely -osion ohjeen mukaan.

Versiosta 0.5.0 alkaen emolevyillä on valmiiksi asennetut M2.5-kierreholkit HATin neljässä kiinnityskohdassa, mikä helpottaa asennusta. Vanhemmilla version 0.4.0 korteilla M2.5-mutterit on asennettava käsin. Muttereiden asentamiseksi emolevy on irrotettava väliaikaisesti. Tämä onnistuu ilman kaikkien kaapeleiden irrottamista.

Monille tavallisille HATeille 15 mm:n välikkeet sopivat, mutta mittaa HATin naarasliittimen korkeus varmistaaksesi oikean välin. Urosliittimen jalusta on 2,5 mm korkea, joten lisää tämä naarasliittimen korkeuteen määrittääksesi tarvittavan välikkeen pituuden.

Kierrä välikkeet kiinnitysreikiin tai kiinnitä ne muttereilla alapuolelta version 0.4.0 korteilla. Kohdista HAT 40-nastaisen GPIO-liittimen kanssa ja varmista että kaikki nastat ovat oikeilla paikoillaan, ennen kuin painat liitintä paikalleen tasaisella voimalla. HATin tulisi asettua emolevyn suuntaisesti niin, ettei GPIO-liitokseen jää näkyvää rakoa.

Kiinnitä HAT M2.5-ruuveilla tai lisävälikkeillä HATin kiinnitysreikien läpi välikkeisiin. Nämä ruuvit eivät sisälly HALPI2:n toimitukseen, vaan ne on hankittava erikseen. Kiristä ruuvit juuri niin paljon, että HAT pysyy paikallaan piirilevyn taipumatta.

### Kaapelointi

Jos HATissa on ulkoisia liittimiä, joihin on päästävä käsiksi kotelon ulkopuolelta, harkitse sopivien paneeliliittimien asentamista vapaisiin PG7-läpivientipaikkoihin. Näin kotelon suojaus säilyy ja liittimiin pääsee silti kätevästi käsiksi.

### Irrotus

HAT irrotetaan asennuksen vastakkaisessa järjestyksessä. Sammuta järjestelmä kokonaan ja irrota kaikki virtalähteet ennen kotelon avaamista. Irrota M2.5-kiinnitysruuvit ja nosta HAT varovasti suoraan ylös GPIO-liittimestä välttäen sivusuuntaista voimaa, joka voisi taivuttaa liittimen nastoja.

Jos HAT tuntuu juuttuneen, tarkista jäikö jokin kiinnitysosa tai kaapeli huomaamatta ennen kuin käytät enemmän voimaa. Jotkin tiukkaliittimiset HATit voivat vaatia varovaista keinuttamista ylöspäin vedettäessä. Keinuta HATtia pohjois–etelä-suunnassa; itä–länsi-suuntainen keinutus voi taivuttaa liittimen nastoja, kun liitin yhtäkkiä irtoaa.

### Ohjelmistoasetukset

Laitteistoasennuksen jälkeen HAT voi vaatia ohjelmistoasetuksia toimiakseen. Monissa HATeissa on device tree -overlayt, jotka on otettava käyttöön Raspberry Pi:n asetuksissa. Muokkaa tiedostoa `/boot/firmware/config.txt` ja lisää HATin dokumentaatiossa mainitut `dtoverlay`-rivit.

!!! quote "Aiheeseen liittyvää"
    - **GPIO-nastajärjestys:** katso [Laitteiston tekniset tiedot](../technical-reference/hardware.md)
    - **Ohjelmiston asetukset:** katso [Lisäasetukset](../software-development/advanced-config.md)
    - **Kotelon muutokset:** katso [Muut liitinvaihtoehdot](#muut-liitinvaihtoehdot)

## NVMe SSD:n vaihtaminen

### SSD-yhteensopivuus

HALPI2 tukee M.2 2230–2280 -kokoisia NVMe SSD -levyjä vakiomuotoisena yksipuolisena versiona. Lyhyemmät 2230-levyt voivat olla kaksipuolisia, koska kyseisessä kiinnityskohdassa on enemmän tilaa, mutta pidempien levyjen on oltava yksipuolisia mahtuakseen emolevylle.

Yhteensopivuus voidaan taata vain Hat Labsin toimittamille ja virallisille Raspberry Pi -SSD-levyille. Jos harkitset kolmannen osapuolen levyä, tarkista ennen ostoa sen yhteensopivuus Raspberry Pi 5:n kanssa käyttäjäraporteista ja yhteensopivuuslistoista. Yhteensopimattomilla levyillä tavallisia ongelmia ovat liiallinen virrankulutus, ylikuumeneminen sekä käynnistysvirheet tai järjestelmän epävakaus.

### Uuden SSD:n valmistelu

Ennen uuden SSD:n asentamista HALPI2:een sille kannattaa flashata käyttöjärjestelmä. SSD:n voi flashata myös asennuksen jälkeen CM5:n USB Boot -liittimen (j1) kautta, mutta ulkoinen USB–NVMe-sovitin on helpompi ja nopeampi. Flashaus on kuvattu [Ohjelmisto-oppaassa](./software.md).

### Järjestelmän 3,3 V:n jännitteen katkaisu

Superkondensaattorit voivat pitää emolevyn 3,3 V:n jännitteen päällä pitkäänkin sen jälkeen, kun päävirta on katkaistu. Koska SSD saa virtansa 3,3 V:n jännitteestä, tämä jännite on katkaistava, jotta SSD on varmasti jännitteetön irrotuksen tai asennuksen aikana.

Aloita sammuttamalla HALPI2 ja irrottamalla virtalähde. Avaa kotelo Kotelon käsittely -osion ohjeen mukaan.

Paikanna emolevyltä "3.3V off" -jumpperi. Sen sijainti vaihtelee kortin version mukaan. Version 0.4.0 korteilla jumpperi on aivan superkondensaattorien vieressä niiden "eteläpuolella". Versiosta 0.5.0 alkaen etsi "Pow.Ctrl"-liitin superkondensaattorien "itäpuolelta". "3.3V off" -nastat ovat liittimen kaksi ylintä nastaa.

Siirrä jumpperi oikosulkemaan "3.3V off" -nastat. Tämä katkaisee 3,3 V:n jännitteen, minkä huomaa LEDien sammumisesta.

### Irrotus

M.2-paikka on emolevyn eteläreunassa. Paikanna **g1**-merkinnällä varustettu M.2-liitin kohdan [Emolevyn liittimet](#emolevyn-liittimet) kuvasta.

Irrota M2.5-kiinnitysruuvi PH1-ruuvimeisselillä. Kun ruuvi on irti, SSD ponnahtaa vinoon asentoon. Nosta levyä varovasti kiinnityspäästä ja vedä se ulos M.2-liittimestä pienin liikkein. Käsittele SSD:tä reunoista, jotta komponentit tai liittimet eivät vaurioidu.

### Asennus

Työnnä valmisteltu SSD M.2-liittimeen noin 30 asteen kulmassa ja varmista, että SSD:n lovi osuu liittimen avaimeen. Levyn pitäisi liukua paikalleen ilman voimaa. Kun se on pohjassa, paina SSD:n kiinnityspää alas välikettä vasten.

Kiinnitä SSD M2.5-ruuvilla PH1-ruuvimeisselillä. Kiristä ruuvi juuri niin paljon, että levy pysyy tukevasti paikallaan. SSD:n tulisi olla täysin suorassa ilman näkyvää taipumaa.

Kun SSD on paikallaan, poista jumpperi "3.3V off" -nastoilta palauttaaksesi 3,3 V:n jännitteen. Säilytä jumpperi liittimessä myöhempää käyttöä varten.

Kokoa kotelo Kotelon käsittely -osion ohjeen mukaan. Ohjelmiston asetuksista ja vianetsinnästä kerrotaan [Ohjelmisto-oppaassa](./software.md).

!!! quote "Aiheeseen liittyvää"
    - **Käyttöjärjestelmän levykuvat:** katso [Ohjelmisto-opas](./software.md)
    - **Käynnistys:** katso [Järjestelmän käyttö](./operation.md)
    - **Kotelon avaaminen:** katso [Kotelon käsittely](#kotelon-kasittely)

## Compute Module 5:n vaihtaminen

### Esivalmistelut

Compute Module 5:n vaihtaminen vaatii huolellisuutta, koska kortti-korttiliittimet ovat herkkiä. CM5 käyttää kahta tiheää liitintä, jotka vaurioituvat helposti liiallisesta voimasta tai väärästä tekniikasta. Irrota asennettu moduuli vain jos se on välttämätöntä, esimerkiksi jos moduuli on vaurioitunut tai se halutaan päivittää. Takuu ei kata Compute Modulen kiinnitysliittimien vaurioita CM5:llä eikä emolevyllä.

Varaa ennen aloittamista lämmönjohtotyynyt lämmönsiirtoa varten. Vakiokokoonpanossa käytetään 1 mm:n tyynyä SoC-piirin päällä ja 2 mm:n tyynyjä RP1-piirin ja sisäisen virransyötön komponenttien päällä. Vanhat lämmönjohtotyynyt voi käyttää uudelleen, jos ne ovat ehjiä ja puhtaita.

### Compute Moduleen käsiksi pääsy

Sammuta HALPI2 ja irrota virtalähde. Irrota kotelon kansi Kotelon käsittely -osion ohjeen mukaan. CM5 on emolevyn alapuolella, joten emolevy on ensin irrotettava kotelosta. Emolevylle tulee useita kaapeleita, joten kannattaa ottaa muutama valokuva kytkennöistä ennen jatkamista.

Irrota kaapelit, jotka estävät emolevyn nostamisen. Irrota emolevyn kiinnitysruuvit ja nosta kortti pois kotelosta.

### Vanhan moduulin irrotus

!!! danger "Varoitus"
    Jos CM5-moduuli irrotetaan yksi liitin kerrallaan, vääntövoimat voivat repiä liittimen irti CM5-moduulista. Takuu ei kata tätä vauriota.

CM5 on kiinni kahdella kortti-korttiliittimellä, jotka vaativat varovaista käsittelyä. Älä koskaan käytä metallityökaluja, sillä ne voivat vaurioittaa liittimiä tai lähellä olevia pintaliitoskomponentteja. Käytä puista tai muovista avausvälinettä, kitaraplektraa tai vastaavaa sähköä johtamatonta työkalua.

Aseta työkalu CM5-moduulin vasemman lyhyen reunan keskelle, moduulin ja emolevyn väliin. Paina oikean reunan kulmia tukevasti alas. Vipua varovasti ylöspäin mahdollisimman pienellä voimalla — moduulin pitäisi irrota kevyellä napsahduksella niin, että molemmat liittimet irtoavat yhtä aikaa.

![CM5-moduulin irrotus](./unmount-cm5.jpg)
*Irrota CM5-moduuli painamalla oikean reunan kulmia alas ja vipuamalla samalla ylöspäin vasemman reunan keskeltä. Molempien liittimien pitäisi irrota yhtä aikaa.*

### Uuden moduulin asennus

Kohdista uusi CM5-moduuli emolevyn liittimiin käyttäen apuna emolevyn silkkipainon ääriviivaa. Emolevylle painetun moduulin ääriviivan pitäisi vastata CM5:n mittoja tarkasti, kun moduuli on oikein päin.

Kun moduuli on kohdistettu, paina tasaisesti ja varovasti liittimien kohdalta moduulin molemmilta lyhyiltä reunoilta. Liittimien kiinnittymisen tuntee hienoisena napsahduksena. Paina tukevasti mutta vältä emolevyn taivuttamista — tue korttia tarvittaessa alapuolelta. Molempien liittimien on oltava täysin pohjassa, jotta laite toimii oikein.

Lisää sitten lämmönjohtotyynyt CM5-moduulin päälle. Tyynyt sijoitetaan näin: 1 mm:n tyyny pää-SoC:n päälle ja 2 mm:n tyynyt RP1-piirin ja virransyötön komponenttien päälle. Jos käytät vanhoja tyynyjä uudelleen, varmista että ne ovat puhtaita ja oikein paikoillaan.

![Lämmönjohtotyynyjen sijoitus CM5:llä](./cm5-thermal-pads-annotated.jpg)
*Lämmönjohtotyynyjen sijoitus Compute Module 5:llä. Käytä 1 mm:n tyynyä SoC:n päällä (keskellä) ja 2 mm:n tyynyjä RP1:n ja virransyötön komponenttien päällä. Tyynyjen todelliset muodot ja koot voivat vaihdella.*

### Antennin kytkentä

Kytke U.FL-antennikaapeli CM5:n antenniliittimeen ennen emolevyn takaisin asentamista. Tähän liittimeen ei pääse käsiksi enää sen jälkeen, kun emolevy on paikallaan. U.FL-liitin vaatii tarkan kohdistuksen ja tukevan painalluksen. Kun liitin on kunnolla paikallaan, tuntuu selvä napsahdus. Varo taivuttamasta liittimen kuorta asennuksen aikana.

### Loppukokoonpano

Tarkista asennus: molempien liittimien on oltava täysin pohjassa ja moduulin tulee olla suorassa emolevyä vasten ilman rakoja. Lämmönjohtotyynyjen tulee koskettaa moduulin lämpöä tuottavia komponentteja.

Aseta emolevy takaisin koteloon niin, että CM5:n lämmönjohtotyynyt osuvat kotelon pohjan vastaaviin lämmönsiirtoalueisiin. Kiinnitä kaikki emolevyn kiinnitysruuvit ja kytke takaisin ne kaapelit, jotka irrotit.

Kokoa laite loppuun tavallisen kotelon sulkemisohjeen mukaan. Ensimmäisellä käynnistyksellä järjestelmän pitäisi tunnistaa uusi CM5 automaattisesti.

!!! warning "Varoitus liittimistä"
    Kortti-korttiliittimet ovat tämän työvaiheen herkimmät osat. Älä koskaan käytä metallityökaluja liittimien lähellä, käytä irrotuksessa ja asennuksessa vain pystysuoraa voimaa, ja varmista täydellinen kohdistus ennen painamista. Vaurioituneet liittimet edellyttävät yleensä emolevyn vaihtoa.

!!! quote "Aiheeseen liittyvää"
    - **Järjestelmän käyttöönotto vaihdon jälkeen:** katso [Ohjelmisto-opas](./software.md)
    - **Käynnistyksen vianetsintä:** katso [Vianetsintä](./troubleshooting.md)
    - **Lämmönhallinta:** katso [Laitteiston tekniset tiedot](../technical-reference/hardware.md)

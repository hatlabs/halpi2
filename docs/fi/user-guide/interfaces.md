---
translated_from: da8aa35c462e57bc7c0b00d50046a1df518e97dd
---

# Liitännät ja tiedonsiirto

## CAN FD / NMEA 2000

HALPI2:ssa on täysin erotettu [CAN FD](https://en.wikipedia.org/wiki/CAN_FD) -liitäntä, joka soveltuu sekä veneiden [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) -verkkoihin että ajoneuvo- ja teollisuuskäyttöön. Liitäntä tarjoaa nopean tiedonsiirron ja täyden sähköisen erotuksen häiriönsiedon vuoksi.

### Liitännän tekniset tiedot

CAN FD -liitäntä tukee sekä tavallista CAN- että CAN FD -protokollaa. NMEA 2000 -käytössä liitäntä toimii tavallisessa CAN-tilassa vakionopeudella 250 kbit/s. Ajoneuvo- ja teollisuuskäytössä liitäntä voi hyödyntää CAN FD:n koko suorituskykyä jopa 8 Mbit/s nopeuteen asti.

Etupaneelissa on Micro-C-liitin, joka on yhteensopiva vakiomuotoisen NMEA 2000 -kaapeloinnin ja -osien kanssa. Näin laite liitetään suoraan olemassa oleviin veneverkkoihin tavallisilla T-liittimillä ja haarakaapeleilla.

### Virransyötön asetukset ja verkon kuormitus

HALPI2:n vaikutus NMEA 2000 -verkon tehonsyöttöön riippuu valitusta virransyöttötavasta. Vakiokokoonpanossa, jossa virta tulee ulkoisesti E7T-liittimen kautta, laite ei tarvitse tehoa NMEA 2000 -verkosta, joten sen kuormaekvivalenttiluku (LEN) on 0.

Kun laite syötetään NMEA 2000 -väylästä, sen virranotto on rajoitettava sisäisellä virranrajoittimella 0,9 A:iin. Tämä vastaa LEN-lukua 18. NMEA 2000 -syöttöä käytettäessä laite kannattaa liittää runkokaapeliin lähelle syöttökaapelia, jotta jännitehäviö jää pieneksi ja toiminta on luotettavaa.

### Laitteistoasetukset

Emolevyllä on 120 Ω:n päätevastus, jonka voi kytkeä jumpperilla. NMEA 2000 -käytössä laitteen omaa päätevastusta ei tule käyttää, koska standardi ei salli sitä. Ajoneuvo- ja teollisuuskäytössä, jossa liikennöidään kahden pisteen välillä, jumpperin voi asettaa päätevastuksen kytkevään asentoon.

Verkon vianetsintää varten emolevyllä on omat RX- ja TX-LEDit, jotka kertovat verkon liikenteestä. LEDit antavat välittömän näkyvän palautteen lähetyksestä ja vastaanotosta, mikä helpottaa yhteysongelmien selvittämistä.

### Verkkoon asentaminen

Liittäminen NMEA 2000 -verkkoon tehdään runkokaapeliin asennettavalla vakiomuotoisella T-liittimellä (ei sisälly toimitukseen) sekä haarakaapelilla, joka yhdistää T-liittimen HALPI2:n Micro-C-liittimeen.

### Ohjelmistointegraatio

CAN-liitäntä toimii Linuxissa SocketCAN-kehyksen kautta ja näkyy verkkolaitteena `can0`. Tämän vakiorajapinnan ansiosta voi käyttää tavallisia Linuxin CAN-työkaluja valvontaan ja vianetsintään. Verkkoliitäntä on valmiiksi määritetty kaikissa HALPI2:n käyttöjärjestelmälevykuvissa (HaLOS, OpenPlotter ja Raspberry Pi OS).

Signal K -palvelinintegraatio on käytettävissä HaLOSin Marine-levykuvissa ja OpenPlotterissa: ne tunnistavat CAN-liitännän automaattisesti ja käyttävät sitä NMEA 2000 -datan käsittelyyn. Muissa HaLOS-levykuvissa Signal K:n voi asentaa Cockpitin Container Apps -kaupasta. Signal K -palvelin purkaa PGN-sanomat ja tarjoaa selainkäyttöisen pääsyn verkon reaaliaikaiseen dataan.

### Vianetsintä

Verkon vianetsintä alkaa emolevyn RX/TX-LEDeistä. Normaalissa toiminnassa LEDit vilkkuvat verkon liikenteen tahdissa. Puuttuva RX-toiminta voi viitata johdotusongelmiin tai virheelliseen päätevastukseen, kun taas puuttuva TX-toiminta voi kertoa verkon ristiriidoista tai johdotuksesta.

Linuxin `candump`-komennolla voi seurata CAN-väylää suoraan komentoriviltä. Työkalu näyttää yksityiskohtaiset tiedot kaikista väylän sanomista, mikä mahdollistaa perusteellisen vianetsinnän. Yksinkertaisimmillaan voit ajaa:

```bash
candump can0
```

Tämä näyttää kaikki saapuvat raa'at CAN-sanomat reaaliajassa.

Signal K -palvelimen koontinäyttö tarjoaa lisää valvontamahdollisuuksia. Se näyttää NMEA 2000 -datanopeudet CAN-liitännästä reaaliajassa. Datan selaustyökalulla voi tarkastella purettua NMEA 2000 -dataa.

!!! quote "Aiheeseen liittyvää"
    - **Virransyötön asetukset:** katso [Aloitusopas](../getting-started/getting-started.md#kiintea-virransyoton-asennus)
    - **Ohjelmiston käyttöönotto:** katso [Ohjelmisto-opas](./software.md)
    - **Verkon vianetsintä:** katso [Vianetsintä](./troubleshooting.md)


## RS-485 (NMEA 0183)

HALPI2:ssa on erotettu [RS-485](https://en.wikipedia.org/wiki/RS-485) -liitäntä, joka tarjoaa sarjaliikenteen veneiden [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422] -verkkoihin ja teollisuuskäyttöön.

[^rs422]: Teknisesti NMEA 0183 käyttää RS-422-standardia, mutta RS-485 on alaspäin yhteensopiva, joten HALPI2 pystyy liikennöimään sekä RS-422- että RS-485-laitteiden kanssa.

### Liitännän tekniset tiedot

RS-485-lähetinvastaanotin toimii jopa 10 Mbit/s nopeudella, joskin tavallisissa NMEA 0183 -sovelluksissa käytetään vakionopeuksia 4800 tai 38400 bit/s. Liitäntä on galvaanisesti erotettu ja NMEA 0183 -määrittelyn mukainen, mikä suojaa HALPI2:ta maasilmukoilta ja veneympäristölle tyypillisiltä sähköhäiriöiltä.

Liitäntä on kytketty sisäisesti Raspberry Pi:n UART 4:ään ja näkyy Linuxissa laitteena `/dev/ttyAMA4`. Tätä tavallista sarjaporttia voi käyttää mikä tahansa sarjaliikennettä tukeva sovellus, kuten Signal K -palvelin, OpenCPN tai omat sovellukset.

### Laitteistoasetukset

Emolevyllä on omat RX- ja TX-LEDit, jotka kertovat RS-485-liitännän liikenteestä. LEDit antavat välittömän näkyvän palautteen asennuksen ja vianetsinnän aikana, jolloin lähetyksen ja vastaanoton toimivuus on helppo varmistaa.

Yleiskäyttöisenä RS-485-liitäntänä laite voidaan asettaa joko automaattiseen tai käsiohjattuun lähetyksen ohjaustilaan. Käsiohjatussa tilassa GPIO-nasta ohjaa lähetyksen enable-signaalia, jolloin ohjelmisto päättää milloin liitäntä lähettää ja milloin vastaanottaa. Tätä tarvitaan monilähettäjäsovelluksissa, joissa liitännän on oltava vaimeassa tilassa silloin kun se ei lähetä. Automaattitilassa laitteisto aktivoi lähetyksen enable-signaalin datan lähtiessä, mikä yksinkertaistaa yhden lähettäjän kokoonpanoja.

Lisäksi RS-485-liitäntä tukee puoliduplex-tilaa, jolloin se voi sekä lähettää että vastaanottaa samalla johdinparilla.

Liitännän voi myös poistaa kokonaan käytöstä laitteistoasetuksilla, jos UART 4 tarvitaan muuhun tarkoitukseen.

### Johdotus ja liitännät

RS-485-liitäntä vaatii läpivientiholkin tai paneeliliittimen, jonka käyttäjä hankkii itse. Yksi hyvä vaihtoehto on [SP13-paneeliliitin johtimineen](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). Liitäntä on alaspäin yhteensopiva NMEA 0183:ssa käytetyn RS-422-signaloinnin kanssa ja tukee sekä RS-485-monilähettäjäverkkoja että RS-422-verkkoja, joissa on yksi lähettäjä ja useita kuuntelijoita. Se käyttää balansoituja differentiaalipareja, jotka on merkitty TX+/TX- ja RX+/RX-.

### Ohjelmistointegraatio

Kaikissa HALPI2:n levykuvissa RS-485-liitäntä on valmiiksi käyttökunnossa. HaLOSin Marine-levykuvissa ja OpenPlotterissa Signal K -palvelin tunnistaa liitännän automaattisesti ja vastaanottaa sen kautta tulevan NMEA 0183 -datan.

Omissa sovelluksissa liitäntä käyttäytyy tavallisena Linuxin sarjaporttina. Sovellukset voivat avata portin `/dev/ttyAMA4` ja asettaa tiedonsiirtonopeuden, databitit, stop-bitit ja pariteetin kytketyn laitteen vaatimusten mukaan. Python-, Node.js- ja C/C++-sovellukset pääsevät liitäntään tavallisilla sarjaliikennekirjastoilla.

### Yleisiä käyttökohteita

Veneissä RS-485-liitäntään kytketään tyypillisesti GPS-vastaanottimia, kaikuluotaimia, tuulimittareita, AIS-transpondereita tai muita NMEA 0183 -protokollaa käyttäviä laitteita. Teollisuudessa liitäntään voidaan kytkeä ohjelmoitavia logiikoita, antureita ja muita automaatiolaitteita, jotka käyttävät Modbus RTU:ta tai muita RS-485-protokollia.

Liitännän suuri nopeus mahdollistaa myös epätavalliset käyttökohteet, kuten nopean anturidatan keruun tai omat tiedonsiirtoprotokollat. Tämä tekee HALPI2:sta sopivan tutkimusaluksiin ja erikoisvalvontasovelluksiin.

!!! quote "Aiheeseen liittyvää"
    - **Ohjelmiston asetukset:** katso [Ohjelmisto-opas](./software.md)
    - **Vianetsintä:** katso [Vianetsintä](./troubleshooting.md)


## GNSS (GPS)

HALPI2 tukee GNSS-vastaanotin-HATteja, jotka kytketään UART0:aan (`/dev/ttyAMA0`). Mikä tahansa tässä portissa oleva GNSS-vastaanotin toimii gpsd:n kanssa suoraan.

U-blox-vastaanottimille (kuten Max-M8Q) HaLOSin Marine-levykuvat tarjoavat lisäksi automaattiset, veneilyyn optimoidut asetukset.

### Automaattiset asetukset (u-blox-vastaanottimet)

HaLOSin Marine-levykuvissa systemd-palvelu (`configure-ublox-marine`) tunnistaa ja määrittää u-blox-vastaanottimet automaattisesti joka käynnistyksellä:

| Asetus | Arvo |
|:-------|:-----|
| Tiedonsiirtonopeus | 115200 bit/s (tehdasoletus 9600) |
| Päivitysnopeus | 10 Hz (100 ms) |
| Dynaaminen malli | Sea (optimoitu veneilyyn) |

Asetukset tehdään joka käynnistyksellä, koska ROM-pohjaisissa u-blox-moduuleissa (kuten MAX-M8Q) ei ole flash-muistia. Asetukset tallentuvat paristovarmennettuun RAM-muistiin (BBR), joka voi tyhjentyä varapariston jännitteen katketessa — esimerkiksi jos laite on pitkään ilman virtaa. Uudelleenmäärittely tapahtuu huomaamatta ja pidentää gpsd:n käynnistystä noin kahdella sekunnilla.

Jos vastaanotinta ei löydy, palvelu päättyy ilman ilmoitusta. Vasta asennettu GNSS-HAT määritetään automaattisesti seuraavalla käynnistyksellä.

### Datan käyttö

GPS-datan tarjoaa [gpsd](https://gpsd.io/) TCP-portissa 2947. HaLOSin Marine-levykuvissa Signal K yhdistyy gpsd:hen automaattisesti — muita asetuksia ei tarvita.

Vianetsintään käy gpsd:n vakiokomentorivityökalut:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Muut kuin HaLOS-levykuvat

Raspberry Pi OS:ssä ja muissa käyttöjärjestelmissä gpsd asennetaan ja määritetään käsin:

```bash
sudo apt install gpsd gpsd-clients
```

Muokkaa tiedostoa `/etc/default/gpsd` niin, että `DEVICES="/dev/ttyAMA0"`, ja käynnistä palvelu uudelleen. Vastaanotin toimii tehdasasetuksillaan (9600 bit/s, 1 Hz), ellei sitä määritetä `gpsd-clients`-paketin `ubxtool`-työkalulla.

!!! quote "Aiheeseen liittyvää"
    - **gpsd HaLOSissa:** katso [HaLOSin GPS-dokumentaatio](https://docs.halos.fi/user-guide/gps/)
    - **Ohjelmiston käyttöönotto:** katso [Ohjelmisto-opas](./software.md)


## Ethernet

HALPI2:ssa on gigabit-ethernet-liitäntä, joka tarjoaa nopean verkkoyhteyden tiedonsiirtoon, etäkäyttöön ja veneen verkkoihin liittymiseen. Emolevyn ethernet-portti on tavallinen RJ45-liitin. Se on tuotu paneeliliittimeen, johon voi kytkeä ulkoisen ethernet-kaapelin.

## USB

HALPI2:ssa on yhteensä neljä USB 3.0 Type A -porttia, jotka tarjoavat nopean liitännän monenlaisille oheislaitteille. Yksi portti on kytketty suoraan CM5:n USB 3.0 -liitäntään, ja loput kolme kulkevat kortilla olevan USB 3 -hubin kautta. Vakiokokoonpanossa kaksi porttia on tuotu etupaneeliin ja kaksi on käytettävissä emolevyllä sisäisiin kytkentöihin.

## HDMI

HALPI2:ssa on kaksi HDMI 2.0 -porttia (HDMI0 ja HDMI1) videolähtöä varten. Emolevyllä on molemmille HDMI-porteille FFC-liittimet (taipuisa litteä kaapeli). Ne on tuotu etupaneeliin räätälöidyillä FFC-kaapeleilla. Etupaneelin liittimet ovat tavallisia HDMI Type A -liittimiä.

HALPI2:n HDMI-lähtö tukee luotettavasti kahta Full HD (1080p) -videovirtaa. 4K-lähtö voi toimia, mutta sitä ei taata.

## MIPI (CSI/DSI)

Emolevyllä on kaksi MIPI CSI/DSI -liitintä kameroille ja näytöille. Liittimet ovat 22-napaisia FFC-liittimiä (taipuisa litteä kaapeli), joiden jako on 0,5 mm. Niiden pitäisi toimia sellaisenaan uudempien Raspberry Pi -yhteensopivien kameroiden ja näyttöjen kanssa.

Vesitiiviyden vuoksi FFC-kaapeleita tulisi käyttää vain kotelon sisäisiin kytkentöihin.

## Ulkoiset painikkeet

HALPI2:n emolevyllä on 2×3-nastainen liitin ulkoisten painikkeiden kytkemiseen. Kotelossa ei ole valmiita painikkeita, joten käyttäjä voi valita painikkeiden paikan ja tyypin omien tarpeidensa mukaan.

### Painikeliittimen nastajärjestys

Emolevyllä on 6-napainen liitin, jossa on kolme merkittyä painiketoimintoa:

| Merkintä | Toiminto | Kuvaus |
|:---------|:---------|:-------|
| Reset | Ohjaimen nollaus | Laitteistotason nollaus (RP2040:n RUN-nasta) |
| Power | Raspberry Pi:n virtapainike | CM5:n virtapainike (PWR_BUT-tulo) |
| User | Käyttäjän määritettävissä | Käyttäjän oma tapahtuma (ei vielä toteutettu) |

Kukin painikekytkentä käyttää kahta nastaa: yhtä painikkeen signaalille ja yhtä maalle. Käytä normaalisti auki olevia (NO) hetkellisiä painikkeita, jotka yhdistävät signaalinastan maahan painettaessa.

### Painikkeiden toiminnot

**Reset-painike:**
Reset-painike tekee laitteistotason nollauksen vetämällä RP2040:n RUN-nastan alas. Tämä nollaa koko järjestelmän: ohjaimen, CM5:n ja kaikki kytketyt oheislaitteet. Painike on erityisen hyödyllinen hätätilanteissa, joissa ohjelmistotason sammutus on epäonnistunut ja järjestelmä on lakannut vastaamasta.

**Power-painike:**
Power-painike on kytketty suoraan CM5:n virtapainiketuloon ja toimii samalla tavalla kuin Raspberry Pi 5:n virtapainike. Kaksoisnapautus pyytää järjestelmää sammumaan hallitusti, jolloin käyttöjärjestelmä ehtii sulkea sovellukset ja irrottaa tiedostojärjestelmät ennen virran katkaisua. Pitkä painallus pakottaa välittömän virrankatkaisun, ja sitä tulisi käyttää vain jos järjestelmä ei vastaa.

**User-painike:**
User-painikkeen toiminnallisuus odottaa vielä ohjelmistototeutusta, ja se tulee käyttäjän määritettäväksi tulevissa firmware-julkaisuissa. Toteutuksen jälkeen painike on tarkoitettu omiin toimintoihin ja sovelluskohtaisiin laukaisimiin, jolloin käyttäjä voi määrittää painikkeen käyttäytymisen omien tarpeidensa mukaan.

### Painikkeiden asennus

#### Kiinnitys suoraan koteloon

Kun painike kiinnitetään suoraan HALPI2:n koteloon, käytä kotelossa valmiina olevia 6 mm:n tai 13 mm:n reikiä. Poista ensin niistä umpitulpat ja asenna reiän halkaisijaan sopiva vesitiivis painike. Kytke painike emolevyn liittimeen sopivalla kaapelilla ja varmista kunnollinen vedonpoisto sekä säänkestävä tiivistys kotelon läpiviennissä.

#### Kiinnitys erilliseen paneeliin

Kun painikkeet asennetaan erilliseen ohjauspaneeliin, valitse paikka, johon pääsee helposti käsiksi ja joka säilyttää säänkestävyyden. Käytä kaapelin läpivienneissä läpivientiholkkeja ja kytke painikkeet jatkokaapelilla, jonka johtimet ovat 22–26 AWG. Pidä kaapelin kokonaispituus alle kolmessa metrissä signaalin laadun säilyttämiseksi. Kosteille tai vaativille olosuhteille altistuvissa asennuksissa käytä liitoskohdissa vesitiiviitä liittimiä pitkäaikaisen toiminnan varmistamiseksi.

#### Kytkentä

Kaikissa painikekytkennöissä emolevylle tulisi käyttää naaraspuolisia liittimiä, joiden jako on 2,54 mm. Varmista nastojen oikea kohdistus ja tukeva kytkentä, jotta kontaktiongelmia ei synny käytön aikana.

!!! quote "Aiheeseen liittyvää"
    - **Virranhallinta:** katso [Virranhallinta ja sammutus](./operation.md#virranhallinta-ja-sammutus)
    - **Laitteiston käsittely:** katso [Laitteisto-opas](./hardware.md)

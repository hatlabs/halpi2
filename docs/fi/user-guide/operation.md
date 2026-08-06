---
translated_from: 3ad6bd291105f72d9e440ca46e96fe9fa085e02c
---

# Järjestelmän käyttö

## Tila-LEDit

HALPI2:ssa on viisi RGB-LEDiä, jotka kertovat järjestelmän ja virransyötön tilan.

### LEDien pikaopas

| LED-kuvio | Väri | Merkitys |
|-----------|------|----------|
| LED 5 palaa | Punainen | Virta kytketty, odottaa latausta |
| Täyttyvä rivi | Punainen | Superkondensaattorit latautuvat |
| Sateenkaari ja värikierto | Monivärinen | CM5 ei käynnistynyt |
| Jännitepalkki | Keltainen | Solo-tila käytössä |
| Jännitepalkki | Vihreä | Co-op-tila käytössä |
| Jännitepalkki | Oranssi | Varavirta käytössä (solo) |
| Jännitepalkki | Tummanvihreä | Varavirta käytössä (co-op) |
| Kaikki vilkkuvat | Punainen | Superkondensaattorien ylijännite |
| Kaikki palavat | Punainen | Vahtikoiran aikakatkaisu |
| Jännitepalkki | Violetti | Sammutus käynnissä |
| Kaikki palavat | Sininen | Sammutus valmiustilaan käynnissä |
| Kaikki palavat | Himmeä punainen | Valmiustila |
| Kaikki sammuneet | — | Järjestelmä pois päältä |

### Superkondensaattorien jännitenäyttö

Käytön aikana LEDit toimivat jännitemittarina, joka näyttää superkondensaattorien varaustason:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Virranhallinta ja sammutus

HALPI2:n virtalähde on suunniteltu kestämään jännitepiikkejä, häiriöitä ja lyhyitä katkoja.

### Virransyöttöjärjestelmän yleiskuvaus

HALPI2:n virranhallinta koostuu näistä osista:

- **Laajan jännitealueen virtalähde** (11–32 V DC, suojaus 100 V DC asti)
- **Superkondensaattorivarmennus** hallittuun sammutukseen jännitteen katketessa
- **Virranrajoitus** (valittavissa 0,9 A tai 2,5 A)
- **Jännitteen menetyksen tunnistus** ja automaattinen sammutuksen käynnistys
- **Syöttöjännitteen ja -virran valvonta**

Järjestelmä toimii kahdessa tilassa: solo-tilassa ja co-op-tilassa.

### Solo-tila

Solo-tila tarjoaa perustason itsenäisen toiminnan silloin, kun HALPI-daemon ei ole käynnissä. Ohjain toimii omillaan ilman yhteyttä ohjelmistoon.

#### Solo-tilan ominaisuudet

- **Ei vaadi yhteyttä ohjelmistoon**
- **Perustason suojaus jännitteen menetykseltä** — valvoo syöttöjännitettä ja reagoi katkoon
- **Automaattinen sammutus simuloiduilla virtapainikkeen painalluksilla**
- **Rajalliset valvonta- ja asetusmahdollisuudet**

#### Jännitteen menetys ja sammutus solo-tilassa

**Jännitteen menetyksen tunnistus:**
Ohjain valvoo syöttöjännitettä ja havaitsee katkon. Katkoajastin (oletuksena 5 sekuntia) estää sammutuksen lyhyiden häiriöiden takia.

**Automaattinen sammutusjärjestys:**

1. **Ohjain havaitsee jännitteen menetyksen**
2. **Katkoajastin käynnistyy** erottamaan häiriön todellisesta katkosta
3. **Simuloidut virtapainikkeen painallukset** — ohjain lähettää kaksoispainalluksen Compute Modulelle
4. **Käyttöjärjestelmä reagoi** ja aloittaa hallitun sammutuksen
5. **Superkondensaattorit ylläpitävät virransyöttöä** (tyypillisesti 30–60 sekuntia)
6. **60 sekunnin aikakatkaisusuojaus** — pakotettu virrankatkaisu, jos hallittu sammutus ei onnistu
7. **Järjestelmä pysyy pois päältä**, kunnes virta palaa
8. **Automaattinen uudelleenkäynnistys**, kun virta on palannut

**Käsin tehtävä sammutus solo-tilassa:**

- Käyttöjärjestelmä sammuu normaalisti
- Järjestelmä käynnistyy automaattisesti uudelleen viiden sekunnin kuluttua, jos syöttöjännite on yhä käytettävissä
- Pysyvää sammutusta varten katkaise syöttöjännite hallitun sammutuksen käynnistämisen jälkeen

#### Milloin solo-tila on käytössä

Solo-tila on käytössä näissä tilanteissa:

- Käynnistyksen alkuvaiheessa ennen kuin HALPI-daemon on käynnistynyt
- Jos HALPI-daemon ei käynnisty tai se on poistettu käytöstä
- Käyttöjärjestelmissä, joissa daemonia ei ole
- Kun daemon on kaatunut tai lakannut vastaamasta

!!! tip "Solo-tilan luotettavuus"
    Solo-tila tarjoaa välttämättömän suojauksen, mutta on co-op-tilaa epävarmempi. Ohjain pyytää sammutusta simuloiduilla painikkeen painalluksilla, mikä ei välttämättä toimi jos järjestelmä on jumissa.

### Co-op-tila

Co-op-tila tarjoaa täyden virranhallinnan silloin, kun HALPI-daemon on käynnissä ja keskustelee ohjaimen kanssa.

#### Co-op-tilan ominaisuudet

- **Suora yhteys ohjelmistoon** — ohjain ja daemon vaihtavat tietoa reaaliajassa
- **Vahtikoirasuojaus** — 30 sekunnin aikakatkaisu varmistaa järjestelmän vakauden
- **Muokattava sammutuskäyttäytyminen** — ajastukset ja komennot ovat säädettävissä
- **Reaaliaikainen valvonta** — kattava virransyötön mittaustietojen seuranta
- **Edistyneemmät asetusmahdollisuudet**

#### Jännitteen menetys ja sammutus co-op-tilassa

**Jännitteen menetyksen tunnistus:**
Ohjain valvoo syöttöjännitettä ja välittää tapahtumat suoraan HALPI-daemonille. Säädettävä katkoajastin (oletuksena 5 sekuntia) sallii lyhyet katkot ilman sammutusta.

**Automaattinen sammutusjärjestys:**

1. **Ohjain havaitsee jännitteen menetyksen** ja ilmoittaa siitä HALPI-daemonille
2. **Katkoajastimen arviointi** — daemon arvioi, ylittääkö katko raja-arvon
3. **Sammutuskomennon suoritus** — daemon ajaa sammutuskomennon (oletuksena `/sbin/poweroff`)
4. **Käyttöjärjestelmän hallittu sammutus** — sovellukset sulkeutuvat ja tiedostojärjestelmät irrotetaan turvallisesti
5. **Superkondensaattorien varavirta** riittää koko sammutuksen ajaksi
6. **Ohjain seuraa valmistumista** — se havaitsee, milloin Compute Modulen virta katkeaa
7. **5 V:n jännite katkaistaan**, kun sammutus on valmis
8. **Järjestelmä pysyy pois päältä**, kunnes syöttöjännite palaa
9. **Uudelleenkäynnistyksen hallinta** — asetuksista riippuen järjestelmä käynnistyy automaattisesti tai jää pois päältä

**Käsin tehtävä sammutus co-op-tilassa:**

- Ohjelmistosta käynnistetty sammutus tapahtuu hallitusti
- Järjestelmä käynnistyy automaattisesti uudelleen viiden sekunnin kuluttua, jos syöttöjännite on yhä käytettävissä
- Automaattisen uudelleenkäynnistyksen estämiseksi katkaise virta tai aseta `auto_restart` arvoon `false`

#### Vahtikoirasuojaus

Co-op-tilaan kuuluu vahtikoira-ajastin (watchdog):

- **30 sekunnin aikakatkaisu** — daemonin on oltava säännöllisesti yhteydessä ohjaimeen
- **Automaattinen palautuminen** — järjestelmä käynnistyy uudelleen, jos yhteys katkeaa
- **Suojaus ohjelmistovirheiltä** — varmistaa toipumisen daemonin kaatumisesta tai järjestelmän jumiutumisesta
- **Vahtikoiran ruokkiminen** — daemon lähettää säännöllisiä tilatietoja, jotka nollaavat ajastimen

#### Milloin co-op-tila on käytössä

Co-op-tila on käytössä, kun:

- HALPI-daemon on käynnissä ja toimii normaalisti
- Daemonin ja ohjaimen välinen yhteys on muodostettu
- Järjestelmä käyttää tuettua käyttöjärjestelmää
- Kaikki valvonta- ja ohjaustoiminnot ovat käytettävissä

!!! info "Co-op-tilan tarkistus"
    Tarkista daemonin tila: `systemctl status halpid`

    Katso ohjaimen tila: `halpi status`

    Lisätietoa `halpi`-komennosta on [Ohjelmisto-oppaassa](./software.md#halpi-daemon-halpid).

### Varavirta ja kondensaattorijärjestelmä

Molemmat tilat nojaavat superkondensaattorien varavirtaan hallitun sammutuksen turvaamiseksi:

**Varavirran kesto:**

- Superkondensaattorit antavat varavirtaa 30–60 sekuntia
- Kesto riippuu järjestelmän kuormasta ja kytketyistä oheislaitteista
- Aika riittää tiedostojärjestelmän turvalliseen sulkemiseen ja prosessien lopettamiseen
- Ei ole tarkoitettu käytön jatkamiseen pitkien katkojen aikana

**Latautuminen:**

- Latausaika 25 sekuntia, kun virranrajoitus on 0,9 A
- Latausaika 9 sekuntia, kun virranrajoitus on 2,5 A
- Latauksen eteneminen näkyy LEDien täyttymisenä (punainen täyttökuvio)

!!! warning "Varavirran rajoitus"
    Superkondensaattorijärjestelmä on tarkoitettu hallittuun sammutukseen, ei käytön jatkamiseen. Älä luota siihen pitkissä sähkökatkoissa.

### Huomioita käsin tehtävästä sammutuksesta

HALPI2 painottaa automaattista toimintaa ja toipumista, mikä vaikuttaa käsin tehtävän sammutuksen käyttäytymiseen.

#### Automaattinen uudelleenkäynnistys

Oletuksena HALPI2 käynnistyy uudelleen käsin tehdyn sammutuksen jälkeen, jos syöttöjännite on yhä käytettävissä:

- Käsin tehty sammutus sammuttaa käyttöjärjestelmän normaalisti
- Sammutuksen valmistumisen jälkeen on viiden sekunnin odotusaika
- Järjestelmä käynnistyy automaattisesti uudelleen pysyäkseen käytettävissä
- Tämä varmistaa toipumisen vahingossa tehdyistä sammutuksista

#### Tavat sammuttaa laite pysyvästi

Pysyvään sammutukseen on kaksi tapaa:

**Virran katkaiseminen:**

1. Käynnistä hallittu sammutus ohjelmistosta
2. Odota että sammutus on valmis (LEDit sammuvat)
3. Katkaise syöttöjännite estääksesi automaattisen uudelleenkäynnistyksen

**Asetuksen muuttaminen:**

1. Poista automaattinen uudelleenkäynnistys käytöstä: `halpi config set auto_restart false`
2. Käynnistä sammutus ohjelmistosta
3. Järjestelmä jää pois päältä sammutuksen jälkeen

**Valmiustila (tulossa):**

!!! info "Ominaisuuden tila"
    Valmiustila on suunnitteilla tuleviin firmware-julkaisuihin. Se mahdollistaa Compute Modulen sammuttamisen niin, että HALPI2:n ohjain jää päälle odottamaan herätystapahtumia.

---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Päivittäinen käyttö

HALPI2 on suunniteltu toimimaan ilman valvontaa. Esiasennetulla HaLOS-levykuvalla — tai millä tahansa käyttöjärjestelmällä, johon on asennettu [HALPI-daemon](./software.md#halpi-komentorivityokalu) — virranhallinta on automaattista: laite lataa varavirtana toimivat superkondensaattorinsa, sietää jännitehäiriöt, sammuttaa käyttöjärjestelmän turvallisesti virransyötön katketessa ja käynnistyy uudelleen, kun virta palaa. Mikään tästä ei vaadi käyttäjän toimia.

## Käynnistäminen

HALPI2:n kotelossa ei ole virtapainiketta: laite käynnistyy aina, kun syöttöjännite kytketään. (Emolevylle voi johdottaa ulkoisen virtapainikkeen — katso [Ulkoiset painikkeet](./interfaces.md#ulkoiset-painikkeet).) LED-rivi täyttyy ensin punaisella superkondensaattorien latautuessa (muutamasta sekunnista puoleen minuuttiin [virranrajoituksen asetuksesta](./hardware.md#virranrajoituksen-asetus) riippuen). Sitten LEDit näyttävät lyhyen sateenkaari- ja värikiertoanimaation Compute Modulen käynnistyessä ja keltaisen palkin käyttöjärjestelmän käynnistyessä, ja muuttuvat vihreiksi, kun käyttöjärjestelmä on käynnissä ja HALPI-daemon on muodostanut yhteyden.

## Sammuttaminen

Sammuta HALPI2 katkaisemalla syöttöjännite — esimerkiksi sähkötaulun kytkimestä. Järjestelmä havaitsee jännitteen menetyksen, sammuttaa käyttöjärjestelmän hallitusti superkondensaattorien virralla ja jää pois päältä. LEDit näyttävät violettia palkkia sammutuksen ajan ja sammuvat, kun sammutus on valmis.

Sammuttaa voi myös ohjelmallisesti — työpöydän valikosta, `shutdown`-komennolla tai komennolla `halpi shutdown`. Järjestelmä sammuu ja pysyy pois päältä, kunnes syöttöjännite katkaistaan ja kytketään uudelleen (tai kunnes [ulkoista virtapainiketta](./interfaces.md#ulkoiset-painikkeet), jos sellainen on asennettu, painetaan).

Halutessasi ohjain voi käynnistää järjestelmän automaattisesti uudelleen noin 5 sekunnin kuluttua ohjelmallisesta sammutuksesta, kun syöttöjännite on yhä kytkettynä — näin vahingossa annettu sammutuskomento ei koskaan jätä pois päältä asennusta, johon on hankala päästä käsiksi. Ota toiminto käyttöön komennolla `halpi config set auto_restart true`; asetus säilyy ohjaimen muistissa. Ennen vuoden 2026 alkua valmistetuissa laitteissa toiminto oli toimitettaessa käytössä — tarkista omasi komennolla `halpi config get auto_restart`.

Järjestelmän voi myös asettaa valmiustilaan, jossa se sammuu ja herää uudelleen ajastettuna ajankohtana — katso [Emolevyn ohjain](../technical-reference/controller.md#valmiustila) -sivu.

## Tila-LEDit

Etupaneelin viisi LEDiä kertovat, mitä järjestelmä tekee:

| LED-kuvio | Merkitys |
|:----------|:---------|
| Punaisella täyttyvä palkki | Superkondensaattorit latautuvat ennen käynnistystä — odota |
| Sateenkaari ja kiertävät värit | Compute Module käynnistyy. Jos kuvio toistuu ilman etenemistä, moduuli ei käynnistynyt — katso [Vianetsintä](./troubleshooting.md#sateenkaari-ledit) |
| Keltainen palkki | Järjestelmä käynnissä, HALPI-daemon ei ole yhteydessä — normaalia hetken aikaa käynnistyksen aikana. Jos tila jatkuu, katso [Vianetsintä](./troubleshooting.md#ledit-jaavat-keltaisiksi) |
| Vihreä palkki | Normaali toiminta |
| Oranssi tai tummanvihreä palkki | Syöttöjännite menetetty, toiminta jatkuu varavirralla — sammutus seuraa, ellei virta palaa muutamassa sekunnissa |
| Violetti palkki | Sammutus käynnissä |
| Kaikki palavat punaisina | Käyttöjärjestelmä ei vastaa — ohjain käynnistää sen automaattisesti uudelleen |
| Kaikki vilkkuvat punaisina | Superkondensaattorivika — ota yhteyttä tukeen |
| Kaikki palavat sinisinä | Siirtyminen valmiustilaan |
| Kaikki himmeän punaisina | Valmiustila |
| Kaikki sammuneet | Virta katkaistu |

Palkkikuvioissa palavien LEDien määrä kertoo superkondensaattorien varaustason. Tarkat jännitealueet ja täydellinen tilakartta ovat [Emolevyn ohjain](../technical-reference/controller.md#tila-ledien-kuviot) -sivulla.

LEDien kirkkautta voi säätää — katso [LEDien ohjaus](./software.md#ledien-ohjaus). LEDit voi myös valjastaa näyttämään järjestelmän mittaustietoja ja veneilytietoa (verkkoliikennettä, tankkien pinnankorkeuksia, NMEA 2000- ja Signal K -arvoja) [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights) -lisäosalla.

## Kun virransyöttö katkeaa

Mitään ei tarvitse tehdä. Superkondensaattorit siltaavat lyhyet notkahdukset ja häiriöt — oletuksena enintään 5 sekuntia — ja toiminta jatkuu keskeytyksettä. Pidemmässä katkossa järjestelmä sammuttaa itsensä hallitusti superkondensaattorien 30–60 sekunnin varavirralla. Kun syöttöjännite palaa, järjestelmä käynnistyy automaattisesti uudelleen.

!!! warning "Ei UPS-laite"
    Superkondensaattorien tehtävä on siltata häiriöt ja antaa virta turvalliseen sammutukseen. Pitkien sähkökatkojen yli jatkuvaan käyttöön tarvitaan erillinen UPS-laite (keskeytymätön virransyöttö).

## Järjestelmän kunnon tarkistus

Vihreä LED-palkki tarkoittaa, että järjestelmä voi hyvin. Tarkemmat tiedot — ohjaimen tilan, jännitteet, virran ja lämpötilat — näyttää `halpi`-komento:

```bash
halpi status
```

Jos jokin näyttää olevan vialla, katso [Vianetsintä](./troubleshooting.md) ja [Ohjelmisto-opas](./software.md#halpi-komentorivityokalu).

## Käyttö ilman daemonia

Käyttöjärjestelmissä, joissa HALPI-daemonia ei ole, ohjain siirtyy perustason suojaustilaan: se havaitsee edelleen jännitteen menetyksen ja pyytää sammutusta, mutta simuloiduilla virtapainikkeen painalluksilla — mikä ei toimi, jos järjestelmä on jumissa — eivätkä valvonta ja asetukset ole käytettävissä. Jos käytät omaa käyttöjärjestelmää, asenna daemon; katso [Muut Debian-jakelut](../software-development/ubuntu-installation.md). Tilojen toiminta on kuvattu [Emolevyn ohjain](../technical-reference/controller.md#toimintatilat) -sivulla.

!!! quote "Aiheeseen liittyvää"
    - **Virranhallinnan sisäinen toiminta:** katso [Emolevyn ohjain](../technical-reference/controller.md)
    - **Virransyöttöjärjestelmän tiedot:** katso [Virtalähde tarkemmin](../technical-reference/power-supply.md)
    - **`halpi`-komento ja daemon:** katso [Ohjelmisto-opas](./software.md)
    - **Ongelmatilanteet:** katso [Vianetsintä](./troubleshooting.md)

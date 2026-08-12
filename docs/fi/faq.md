---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# UKK

## Miksi HALPI2 käynnistyy uudelleen, kun sammutan sen?

Laitteessasi on automaattinen uudelleenkäynnistys käytössä: kun `auto_restart` on `true`, ohjain käynnistää järjestelmän uudelleen noin 5 sekunnin kuluttua ohjelmallisesta sammutuksesta, jos syöttöjännite on kytkettynä. Ennen vuoden 2026 alkua valmistetut laitteet toimitettiin asetus käytössä; nykyiset laitteet toimitetaan se poissa käytöstä. Poista toiminto käytöstä komennolla `halpi config set auto_restart false` — tai pidä se, sillä se varmistaa, ettei valvomaton järjestelmä jää pois päältä vahingossa annetun sammutuskomennon jälkeen. Kun toiminto on käytössä, sammuta laite pysyvästi katkaisemalla syöttöjännite. Katso [Sammuttaminen](user-guide/operation.md#sammuttaminen).

## Miten HALPI2 sammutetaan?

Katkaise syöttöjännite. Järjestelmä havaitsee jännitteen menetyksen ja sammuu hallitusti superkondensaattorien virralla — tämä on laitteen suunniteltu sammutustapa. Katso [Sammuttaminen](user-guide/operation.md#sammuttaminen).

## Pitääkö minun tehdä jotain, kun sähköt katkeavat?

Ei. Superkondensaattorit siltaavat lyhyet häiriöt, pidemmät katkot käynnistävät automaattisen turvallisen sammutuksen, ja järjestelmä käynnistyy itsestään uudelleen, kun virta palaa. Katso [Kun virransyöttö katkeaa](user-guide/operation.md#kun-virransyotto-katkeaa).

## Kuinka kauan varavirta kestää?

Superkondensaattorit antavat 30–60 sekuntia järjestelmän kuormasta riippuen. Se riittää turvalliseen sammutukseen marginaalilla, mutta HALPI2 ei ole UPS — se ei jatka toimintaa pitkien katkojen yli. Katso [Virtalähde tarkemmin](technical-reference/power-supply.md).

## Voiko HALPI2 olla päällä vuorokauden ympäri?

Voi. HALPI2 on suunniteltu jatkuvaan valvomattomaan käyttöön, ja sen virranhallinta olettaa sen: järjestelmä toipuu jännitteen menetyksistä ja käyttöjärjestelmän jumiutumisista ilman käyttäjän toimia.

## Mitä tarkoittaa, kun LEDit jäävät keltaisiksi?

Keltainen palkki tarkoittaa, että järjestelmä on käynnissä mutta HALPI-daemon ei ole muodostanut yhteyttä — normaalia hetken aikaa käynnistyksen aikana. Pysyvästi keltainen palkki tarkoittaa, että käyttöjärjestelmä ei käynnisty tai daemonia ei ole asennettu. Katso [Vianetsintä](user-guide/troubleshooting.md#ledit-jaavat-keltaisiksi).

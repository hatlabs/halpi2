---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Virtalähde tarkemmin

HALPI2:n virtalähde on suunniteltu veneiden ja ajoneuvojen epävakaisiin sähköympäristöihin: se sietää jännitepiikit ja häiriöt, rajoittaa kytkentävirtasysäyksen ja varastoi riittävästi energiaa järjestelmän turvalliseen sammuttamiseen, kun syöttöjännite katoaa.

Sähköiset tekniset tiedot ovat [Laitteiston teknisissä tiedoissa](./hardware.md). Tilakone, joka toimii tässä kuvattujen mittausten pohjalta, on kuvattu [Emolevyn ohjain](./controller.md) -sivulla.

## Tuloaste

Nimellinen syöttöjännitealue on 10–32 V DC, mikä kattaa sekä 12 V:n että 24 V:n järjestelmät. Tuloaste on suojattu väärältä napaisuudelta ja enintään 100 V:n hetkellisiltä ylijännitteiltä, kuten laturin kuormanpudotuspiikeiltä (load dump).

### Virranrajoitus

Syöttövirran rajoitin ohjaa virtalähteestä otettavaa enimmäisvirtaa, ja se on valittavissa emolevyn kytkimellä 0,9 A:n ja 2,5 A:n välillä. Rajoituksella on kaksi tehtävää:

- Se rajaa kytkentävirtasysäyksen, kun tyhjät superkondensaattorit alkavat latautua virran kytkeytyessä.
- Se pitää kokonaiskulutuksen virtalähteen tehobudjetissa — 0,9 A:n asetuksella (LEN 18) HALPI2:lle voi turvallisesti syöttää virran NMEA 2000 -väylästä.

Oletusasetus on 0,9 A. Valitse 2,5 A, kun järjestelmä syöttää paljon virtaa kuluttavia oheislaitteita tai kun haluat nopeamman käynnistyksen. Kytkimen sijainti ja asetuksen vaihtamisen vaiheet on kuvattu [Laitteisto-oppaassa](../user-guide/hardware.md#virranrajoituksen-asetus).

## Superkondensaattorivarmennus

Superkondensaattoripankki varastoi energian hallittuja sammutuksia varten. Toisin kuin akkukäyttöinen UPS, superkondensaattorit eivät kulu, toimivat koko lämpötila-alueella ja latautuvat sekunneissa — hintana huomattavasti pienempi energiavarasto.

### Latautuminen

Superkondensaattorit latautuvat aina, kun syöttöjännite on kytkettynä. Tyhjästä lataus kestää noin:

- 25 sekuntia 0,9 A:n virranrajoituksella
- 9 sekuntia 2,5 A:n virranrajoituksella

Etupaneelin LEDit näyttävät latauksen etenemisen punaisella täyttyvänä palkkina. Compute Module käynnistetään, kun superkondensaattorien jännite saavuttaa käynnistysrajan (oletuksena 8,0 V).

### Varavirran kesto

Kun syöttöjännite katoaa, superkondensaattorit kantavat koko järjestelmän kuorman. Ne antavat 30–60 sekuntia käyttöaikaa järjestelmän kuormasta ja kytketyistä oheislaitteista riippuen — riittävästi käyttöjärjestelmän hallittuun sammutukseen marginaalilla.

!!! warning "Ei UPS-laite"
    Superkondensaattorijärjestelmä on suunniteltu siltaamaan häiriöt ja antamaan virta turvalliseen sammutukseen. Sitä ei ole suunniteltu jatkuvaan käyttöön pitkien katkojen yli.

## Jännitteen menetyksen tunnistus

Ohjain mittaa syöttöjännitettä jatkuvasti ja toteaa syöttöjännitteen menetetyksi, kun jännite laskee alle 9,0 V:n. Katkoajastin (oletuksena 5 sekuntia) estää sammutuksen lyhyissä katkoissa: superkondensaattorit siltaavat katkon, ja toiminta jatkuu keskeytyksettä, jos virta palaa ajoissa. Pidemmät katkot käynnistävät automaattiset sammutusjärjestykset, jotka on kuvattu [Emolevyn ohjain](./controller.md#jannitteen-menetys-ja-sammutusjarjestykset) -sivulla.

## Valvonta

Ohjain mittaa syöttöjännitteen, syöttövirran ja superkondensaattorien jännitteen ja tarjoaa ne HALPI-daemonin kautta:

```bash
halpi status
```

Arvot ovat saatavilla myös ohjelmallisesti daemonin REST-rajapinnan kautta — katso [Ohjelmisto-opas](../user-guide/software.md#rest-api-rajapinta).

!!! quote "Aiheeseen liittyvää"
    - **Sähköiset tekniset tiedot:** katso [Laitteiston tekniset tiedot](./hardware.md)
    - **Tilakone ja sammutusjärjestykset:** katso [Emolevyn ohjain](./controller.md)
    - **Virransyötön toiminta päivittäisessä käytössä:** katso [Päivittäinen käyttö](../user-guide/operation.md)

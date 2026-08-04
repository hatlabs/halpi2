# Liitännät ja tiedonsiirto

Tällä sivulla kuvataan, miten CM5:n liitännät on tuotu HALPI2:n emolevylle.
Kortin CAN FD- ja RS-485-porttien päivittäisestä käytöstä kerrotaan
[Liitännät ja tiedonsiirto](../user-guide/interfaces.md) -käyttöoppaassa.

## Sarjaportit (UART)

Compute Module 5 kytkeytyy 40-nastaiseen liittimeen RP1-I/O-ohjaimensa kautta,
joka tuo esiin viisi UARTia (`uart0`–`uart4`). Jokainen UART on johdotettu yhteen
kiinteään GPIO-pariin — toisin kuin aiemmissa Pi-malleissa, nastoja ei voi
vaihtaa toisiin. Kirjautumiskonsoli on erillinen, oma vianetsintä-UART
(`/dev/ttyAMA10`), eikä se ole näiden joukossa.

| UART | TX / RX | Liittimen nastat | Linux-laite | Saatavuus HALPI2:ssa |
|:-----|:--------|:-----------------|:-------------|:---------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Vapaa. Tavanomainen HAT-sarjaportti; käytetään GNSS-HATeissa. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Vapaa. Nämä ovat HAT-tunnisteen EEPROM-nastat (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Vapaa. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | CAN FD -ohjaimen käytössä (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | RS-485:n käytössä. |

### UARTin käyttöönotto

Lisää vastaava `-pi5`-overlay tiedostoon `/boot/firmware/config.txt` ja käynnistä
laite uudelleen:

```
dtoverlay=uart2-pi5
```

`uart0` otetaan käyttöön asetuksella `dtparam=uart0=on`. (CM5:llä firmware ohjaa
tavalliset `uartN`-overlayt niiden `uartN-pi5`-vastineisiin, joten kumpikin nimi
toimii; `-pi5`-muotoa käytetään tässä selkeyden vuoksi.)

Laitteistotason vuonohjaus otetaan käyttöön erikseen `ctsrts`-parametrilla, ja
overlayt voivat ohjata RS-485-lähetinvastaanottimen enable-linjaa suoraan
`rs485`-parametrilla:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS varaa seuraavan GPIO-parin, joka HALPI2:ssa on usein jo käytössä:

| UART | CTS / RTS | Menee päällekkäin |
|:-----|:----------|:------------------|
| `uart1` | GPIO2 / 3 | Järjestelmän I2C-väylä (I2C1) |
| `uart2` | GPIO6 / 7 | CAN FD -piirin valinta (chip select) |
| `uart3` | GPIO10 / 11 | CAN FD:n SPI-väylä |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` on siis käytännössä käyttökelpoinen vain pelkkänä TX/RX-porttina.

### Varatun UARTin vapauttaminen

`uart3` ja `uart4` menevät päällekkäin kortin CAN FD- ja RS-485-liitäntöjen
kanssa:

- **`uart3`** jakaa SPI0-väylän CAN FD -ohjaimen kanssa — GPIO9 on ohjaimen
  datalähtö (SDO). `uart3`:n käyttö edellyttää CAN-liitännän poistamista
  käytöstä sekä laitteistomuutosta, eikä sitä tueta vakiokortilla.
- **`uart4`** on RS-485-portti. Kortin RX-enable-jumpperin poistaminen irrottaa
  RS-485-vastaanottimen GPIO13:sta ja vapauttaa `uart4`:n yleiskäyttöön. RS-485
  ei tällöin ole käytettävissä.

Laitteistotason vaiheet on kuvattu kohdassa
[Sisäisten liitäntöjen poistaminen käytöstä](../user-guide/hardware.md#hattien-kaytto).

### Tarkistus

Varmista uudelleenkäynnistyksen jälkeen, että laitetiedosto on olemassa ja
nastoilla on odotettu toiminto:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

Valittujen nastojen pitäisi ilmoittaa UART-toimintonsa (`a2` UARTeille
`uart1`–`uart4`, `a4` UARTille `uart0`).

## Muut aiheet

- NMEA 2000 -toteutuksen yksityiskohdat
- USB 3.0 -tekniset tiedot ja virranhallinta
- Ethernet ja verkot
- M.2 NVMe -massamuistin vaatimukset

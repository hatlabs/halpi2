---
translated_from: 14cb3c2c516710194d6d97569111c8626e6fc6ea
---

# Innledning

HALPI2 er en ferdig båtdatamaskin basert på Raspberry Pi Compute Module 5 (CM5). Den har et omfattende sett med egenskaper som passer godt til maritime bruksområder, kjøretøy og mange industrielle anvendelser.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Lenke til nettbutikken"
    Kjøp HALPI2 i [nettbutikken til Hat Labs](https://shop.hatlabs.fi/products/halpi2-computer).

## Hva er HALPI2?

HALPI2 er siste generasjon innen robust innebygd databehandling, og kombinerer kraften og økosystemet til Raspberry Pi med spesialiserte egenskaper for krevende miljøer. I motsetning til vanlige enkortsdatamaskiner er HALPI2 konstruert fra bunnen av for drift 24/7 under tøffe forhold der pålitelighet er avgjørende.

Systemet forener en Raspberry Pi Compute Module 5 med et spesialutviklet bærekort, alt sammen i et vanntett aluminiumskabinett som samtidig fungerer som kjøleribbe. Denne konstruksjonen gir regnekraften dagens bruksområder krever, samtidig som robustheten maritim og industriell bruk stiller krav om, beholdes.

## Viktige egenskaper og muligheter

### Egenskaper ved kabinettet

- **Vanntett aluminiumskabinett (IP65)**, størrelse 200 × 130 × 60 mm
- **Standardkontakter** for strøm, NMEA 2000, gigabit Ethernet, HDMI, 2× USB 3.0 og WiFi-/Bluetooth-antenne
- **Fleksible tilkoblingsmuligheter** med valg mellom 3× PG7-kabelgjennomføringer eller vanntette SP13-kontakter
- **Støtte for ekstern antenne** gjennom utsparinger for 2 ekstra SMA-kontakter
- **Konstruert for veggmontering**, med kontaktene plassert for enkel installasjon

![Kontaktplassering på HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Maskinvareegenskaper

- **Bredt inngangsspenningsområde** fra 10 til 32 VDC, med beskyttelse opp til 100 VDC
- **Intelligent strømbegrensning**: største inngangsstrøm 0,9 eller 2,5 A, valgbart av brukeren
- **To strømalternativer**: direkte tilkobling av 12 V/24 V eller 12 V strøm fra NMEA 2000-bussen
- **Reserve med superkondensatorer** for beskyttelse mot forstyrrelser og kontrollert nedstenging ved strømbortfall
- **Avansert strømstyring** med automatisk deteksjon av strømbortfall
- **Passiv kjøling** der CM5 er i direkte kontakt med kabinettet
- **Rask lagring** via standard M.2 NVMe SSD-grensesnitt
- **Utvidelsesmuligheter** gjennom standard 40-pinners GPIO-pinneliste fra Raspberry Pi
- **Omfattende I/O-muligheter**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, gigabit Ethernet
- **Maritime grensesnitt**: CAN FD (NMEA 2000) og RS-485 (NMEA 0183)
- **Sanntidsklokke** med reservebatteri for nøyaktig tidsangivelse
- **Visuell statusindikering** med fem RGB-LED-er
- **Brukerinteraksjon** gjennom konfigurerbare knappepinnelister

![HALPI2 sett innvendig](./halpi2-interior.jpg)
*Innvendig bilde av HALPI2 som viser bærekortet og de ulike kontaktene.*

### Programvareegenskaper

- **Ferdig konfigurerte operativsystembilder** klare til bruk med en gang: [HaLOS](https://docs.halos.fi) (standard), OpenPlotter, Raspberry Pi OS og Raspberry Pi OS Lite
- **Omfattende overvåking** av spenning, strøm og temperatur
- **Transparente firmware-oppdateringer** over I2C-grensesnittet

## Bruksområder

### Maritime bruksområder

- **Navigasjonssystemer** med kartplottere og GPS-integrasjon
- **Datalogging** av motorparametere, miljøsensorer og fartøyets ytelse
- **Signal K-servere** for samlet håndtering av båtdata
- **Generell databehandling om bord** for internettilgang og kommunikasjon
- **Feilsøking av NMEA 2000-nettverk** for bedre systempålitelighet

### Industrielle bruksområder

- **Prosessovervåking** og styresystemer
- **Miljømåling** og datainnsamling
- **Stasjoner for fjernovervåking**
- **Automatisering og styring** av utstyr
- **Systemer for prediktivt vedlikehold**

### Bruksområder i kjøretøy

- **Systemer for flåtestyring**
- **Telematikk** og kjøretøysporing
- **Infotainmentsystemer i kjøretøy**
- **Plattformer for diagnostikk og overvåking**

## Innholdet i esken

HALPI2-pakken inneholder:

- **HALPI2-enheten** med ferdig montert Compute Module 5 og NVMe SSD (med mindre den er bestilt uten)
- **Strømkabel** med E7T-kontakt (kompatibel med Amphenol LTW Ceres Mini), lengde 2 m
- **E7T-kabelplugg** for egne installasjoner
- **Par med DC-plugg (barrel)** på 5,5 × 2,1 mm, til bruk med vanlige 12 V-/24 V-strømforsyninger
- **Raspberry Pi-antenne** for WiFi- og Bluetooth-tilkobling
- **3 stk. PG7-kabelgjennomføringer** for flere grensesnitt
- **Hurtigstartveiledning og garantidokumentasjon** som hjelp til å komme i gang

![Innholdet i tilbehørsposen til HALPI2](./goodie-bag-contents.jpg)

Ekstra tilbehør fås separat:

- **NMEA 2000-stikkledning** for bussdrevne installasjoner
- **Ulike kontaktsett** for egne installasjoner

## Slik bruker du denne dokumentasjonen

Denne dokumentasjonen er bygd opp for å tjene både sluttbrukere som trenger praktisk veiledning, og profesjonelle utviklere som trenger detaljert teknisk informasjon.

### For sluttbrukere

- Begynn med veiledningen **Kom i gang** for oppsett og installasjon
- Les **Daglig bruk** for den daglige bruken: hva LED-ene betyr, nedstenging og oppførsel ved strømbortfall
- Slå opp i **Feilsøking** når det oppstår problemer

### For utviklere

- Se gjennom **Teknisk referanse** for detaljerte spesifikasjoner
- Studer avsnittene under **Programvareutvikling** for egne applikasjoner
- Gå gjennom **Konstruksjonsfiler** for planlegging av integrasjon

### Tips til dokumentasjonen

- 💡 Boksene med **Tips** gir snarveier for vanlige oppgaver
- ⚠️ Varslene **Advarsel** og **Forsiktig** framhever viktig sikkerhetsinformasjon
- 🔧 Avsnittene med **Tekniske detaljer** gir grundig informasjon om implementasjonen
- 📖 **Kryssreferanser** knytter sammen beslektede emner gjennom hele dokumentasjonen

Enten du setter opp din første båtdatamaskin eller utvikler en egen industriell løsning, vil denne dokumentasjonen lede deg gjennom hvert steg av HALPI2-opplevelsen.

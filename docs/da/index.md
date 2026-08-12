---
translated_from: 14cb3c2c516710194d6d97569111c8626e6fc6ea
---

# Introduktion

HALPI2 er en færdig bådcomputer baseret på Raspberry Pi Compute Module 5 (CM5). Den har et omfattende sæt funktioner, som passer godt til marine, automotive og mange industrielle anvendelser.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Link til webshoppen"
    Køb HALPI2 i [Hatlabs' webshop](https://shop.hatlabs.fi/products/halpi2-computer).

## Hvad er HALPI2?

HALPI2 er det nyeste skridt inden for robust indlejret databehandling og kombinerer ydeevnen og økosystemet fra Raspberry Pi med specialiserede funktioner til krævende miljøer. I modsætning til almindelige enkeltkortcomputere er HALPI2 konstrueret fra bunden til drift døgnet rundt under barske forhold, hvor driftssikkerhed er altafgørende.

Systemet integrerer et Raspberry Pi Compute Module 5 med et specialudviklet bærekort, det hele indbygget i et vandtæt aluminiumskabinet, der samtidig fungerer som køleplade. Konstruktionen giver den regnekraft, moderne anvendelser kræver, og bevarer samtidig den robusthed, marin og industriel brug forudsætter.

## Vigtigste funktioner og egenskaber

### Kabinettets egenskaber

- **Vandtæt aluminiumskabinet (IP65)**, størrelse 200×130×60 mm
- **Standardstik** til strøm, NMEA 2000, gigabit-ethernet, HDMI, 2× USB 3.0 og WiFi-/Bluetooth-antenne
- **Fleksible tilslutningsmuligheder** med valg mellem 3× PG7-kabelforskruninger eller vandtætte SP13-stik
- **Understøttelse af eksterne antenner** via udskæringer til 2 ekstra SMA-stik
- **Design til vægmontering** med stikkene placeret, så installationen er nem

![HALPI2's stikplacering](./user-guide/front-panel-connectors-all.jpg)

### Hardwarefunktioner

- **Bredt indgangsspændingsområde** fra 10 til 32 V DC med beskyttelse op til 100 V DC
- **Intelligent strømbegrænsning**: maks. indgangsstrøm 0,9 eller 2,5 A, som du selv vælger
- **To forsyningsmuligheder**: direkte tilslutning af 12 V/24 V eller 12 V-busforsyning via NMEA 2000
- **Superkondensatorbackup** mod korte spændingsudfald og til kontrolleret nedlukning ved strømsvigt
- **Avanceret strømstyring** med automatisk registrering af strømsvigt
- **Passiv køling** med CM5 i direkte kontakt med kabinettet
- **Hurtig lagring** via standard M.2 NVMe SSD-grænseflade
- **Udvidelsesmulighed** via den 40-benede GPIO-stikliste fra Raspberry Pi
- **Rige I/O-muligheder**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, gigabit-ethernet
- **Marinespecifikke grænseflader**: CAN FD (NMEA 2000) og RS-485 (NMEA 0183)
- **Realtidsur** med backupbatteri til nøjagtig tidsangivelse
- **Visuel statusvisning** via fem RGB-LED'er
- **Brugerinteraktion** via konfigurerbare knapstiklister

![HALPI2 set indvendigt](./halpi2-interior.jpg)
*Indvendigt billede af HALPI2 med bærekortet og de forskellige stik.*

### Softwarefunktioner

- **Forudkonfigurerede styresystemimages**, der er klar til brug med det samme: [HaLOS](https://docs.halos.fi) (standard), OpenPlotter, Raspberry Pi OS og Raspberry Pi OS Lite
- **Omfattende overvågning** af spænding, strøm og temperatur
- **Gennemsigtige firmwareopdateringer** via I2C-grænsefladen

## Målanvendelser

### Marine anvendelser

- **Navigationssystemer** med kortplottere og GPS-integration
- **Datalogning** af motorparametre, miljøsensorer og fartøjets ydeevne
- **Signal K-servere** til samlet håndtering af bådens data
- **Almindelig computerbrug om bord** til internetadgang og kommunikation
- **Fejlfinding på NMEA 2000-netværk** for højere driftssikkerhed

### Industrielle anvendelser

- **Procesovervågning** og styresystemer
- **Miljømåling** og dataopsamling
- **Fjernovervågningsstationer**
- **Automatisering af udstyr** og styring
- **Systemer til forudsigende vedligeholdelse**

### Automotive-anvendelser

- **Flådestyringssystemer**
- **Telematik** og sporing af køretøjer
- **Infotainmentsystemer** i køretøjer
- **Platforme til diagnostik og overvågning**

## Hvad er der i æsken

Din HALPI2-pakke indeholder:

- **HALPI2-enhed** med formonteret Compute Module 5 og NVMe SSD (medmindre den er bestilt uden)
- **Strømkabel** med E7T-stik (kompatibelt med Amphenol LTW Ceres Mini), længde 2 m
- **E7T-kabelstik** til egne installationer
- **Par af DC-jackstik (barrel)** (5,5 × 2,1 mm) til brug med almindelige strømforsyninger på 12 V/24 V
- **Raspberry Pi-antenne** til WiFi og Bluetooth
- **3 stk. PG7-kabelforskruninger** til yderligere grænseflader
- **Lynguide og garantidokumentation**, så du kan komme i gang

![Indholdet af HALPI2's tilbehørspose](./goodie-bag-contents.jpg)

Yderligere tilbehør fås separat:

- **NMEA 2000-dropkabel** til busforsynede installationer
- **Forskellige stiksæt** til egne installationer

## Sådan bruger du denne dokumentation

Denne dokumentation henvender sig både til slutbrugere, der søger praktisk vejledning, og til professionelle udviklere, der har brug for detaljerede tekniske oplysninger.

### For slutbrugere

- Start med vejledningen **Kom godt i gang** til opsætning og installation
- Læs **Daglig brug** om hverdagens betjening: LED'ernes betydning, nedlukning og adfærd ved strømsvigt
- Slå op i **Fejlfinding**, når der opstår problemer

### For udviklere

- Gennemgå **Teknisk reference** for detaljerede specifikationer
- Læs afsnittene om **Softwareudvikling**, når du udvikler egne applikationer
- Se **Designfiler** til planlægning af integration

### Tip til dokumentationen

- 💡 **Hurtige tip**-bokse giver genveje til almindelige opgaver
- ⚠️ **Advarsel** og **Forsigtig** fremhæver vigtige sikkerhedsoplysninger
- 🔧 **Tekniske detaljer** giver dybdegående oplysninger om implementeringen
- 📖 **Krydshenvisninger** forbinder beslægtede emner i hele dokumentationen

Uanset om du sætter din første bådcomputer op eller udvikler en specialtilpasset industriel løsning, guider denne dokumentation dig gennem hvert trin af HALPI2-oplevelsen.

---
translated_from: 9741366021074655d667fcf3a93a634f86f3519a
---

# Hårdvaruguide

## Åtkomst till kapslingen

HALPI2 har en pulverlackerad kapsling i pressgjuten aluminium med förborrade hål för panelkontakter. När interna ändringar eller underhåll behövs kommer du åt insidan enligt anvisningarna nedan.

### Öppna kapslingen

För att komma åt de interna komponenterna börjar du med att se till att enheten är helt avstängd och att strömkablarna är bortkopplade. Locket hålls på plats av fyra försänkta M4x10-skruvar med PH2-huvud. Ta bort skruvarna med en PH2-skruvmejsel och lyft av locket.

### Återmontering

Innan du sätter ihop kapslingen igen bör du kontrollera att alla interna anslutningar sitter ordentligt och är rätt monterade. Dra kablarna omsorgsfullt så att de inte kläms eller får skarpa böjar.

Det är lätt att råka koppla in de böjliga flatkablarna (FFC) bakvänt. Kontrollera riktningen mot pilarna märkta ”Contacts” i tryckskiktet.

Var särskilt noga med lockets packning: kontrollera att den inte är skadad, smutsig eller förskjuten, eftersom det skulle försämra kapslingens täthet.

Sätt tillbaka lockets fyra M4x10-skruvar med PH2-skruvmejseln. Dra inte åt för hårt.


## Panelkontakter

### Standardutförande

HALPI2 levereras med ett standardutförande av kontakter som passar de flesta tillämpningar. Standardplaceringen omfattar:

- **E7T-strömkontakt**
- **NMEA 2000 Micro-C-kontakt**
- **Gigabit-ethernet RJ45**
- **HDMI-utgång**
- **2× USB 3.0 typ A**
- **3× platser för PG7-kabelgenomföring** (med blindpluggar)
- **2× platser för RP-SMA-antenn** (med blindpluggar)
- **Andningsplugg** för tryckutjämning

![Frontpanelens kontakter och blindpluggar](./front-panel-connectors-all.jpg)
*Frontpanelens kontakter och blindpluggar. Kontakterna märkta med grönt ingår i standardutförandet. De gula platserna är blindpluggar som vid behov kan ersättas med kontakter. Den röda platsen är andningspluggen, som inte får tas bort.*

### Egna kontaktalternativ

Om du behöver andra kontakttyper kan du ändra panelens utförande:

#### Ta bort kontakter

!!! warning "Viktigt"
    Ändra kontakterna endast när enheten är avstängd och bortkopplad från alla källor.

    Plastgängor skadas lätt om de dras åt för hårt. Använd vanliga hylsnycklar men dra bara åt för hand.

1. **Använd rätt hylsstorlek:**
    - Stora kontakter: 26 mm hylsa
    - M6-nylonbultar: 10 mm hylsa
    - RP-SMA-kontakter: 8 mm hylsa
    - PG7-platser: stor spårskruvmejsel, 17 mm hylsa

2. **Ta bort försiktigt** — plastgängor skadas lätt om de dras åt för hårt

3. **Spara de borttagna delarna** för eventuellt framtida bruk

#### Montera nya kontakter

1. **Använd endast marina** eller på annat sätt miljöklassade kontakter
2. **Se till att tätningen blir god** — en bred fläns krävs på insidan
3. **Dra bara åt för hand** — dra inte åt plastgängorna för hårt
4. **Provmontera** före den slutliga installationen

## Intern layout

- HALPI2:s bärkort är datorns moderkort. Det bär Compute Module 5 (CM5) på undersidan och sköter strömhantering, indikeringar och anslutningar för alla gränssnitt.

### Bärkortets funktionsområden

Bärkortets viktigaste funktionsområden visas i bilden nedan.

![Bärkortets layout, ovansidan](./carrier-board-top-layout.jpg)
*Bärkortets layout på ovansidan, med de viktigaste funktionsområdena.*

### Bärkortets kontakter

Funktionerna nås via ett antal kontakter på kortet, som visas i bilden nedan.

![Bärkortets kontakter, ovansidan](./carrier-board-top-conx.jpg)
*Bärkortets kontakter, ovansidan.*

En förteckning över kontakterna på ovansidan följer nedan.

| Märkning | Beskrivning |
|:---------|:------------|
| **a1** | Strömkontakt (typ Phoenix MC, delning 3,81 mm) |
| **a2** | Omkopplare för strömbegränsning (0,9 A eller 2,5 A) |
| **a3** | Bygel för strömstyrning. Kortslut stiften ”3.3V off” för att tvinga av 3,3 V-skenan. Kortslut stiften ”5V on” för att tvinga på 5 V-skenan. **Obs:** På kort av version 0.4.0 är kontakterna **a3** och **c2** ordnade på ett annat sätt. |
| **b1** | Ethernetport (RJ45) |
| **c1** | Styrkretsens USB-port. Används för att flasha RP2040-mikrokontrollerns firmware. |
| **c2** | Stiftlist för MCU USB BOOT. Kortslut stiften för att sätta RP2040 i USB-startläge. |
| **c3** | Stiftlist för felsökning av styrkretsen |
| **c4** | Obestyckad GPIO-stiftlist för styrkretsen |
| **c5** | Stiftlister för knappar. Används för att ansluta knapparna Power, Reset och User. |
| **c6** | Strömknapp. Används för att slå på och stänga av Compute Module 5. |
| **d1** | Raspberry Pi:s 40-poliga GPIO-stiftlist |
| **e1** | MIPI0-kontakt för kamera eller skärm |
| **e2** | MIPI1-kontakt för kamera eller skärm |
| **f1** | HDMI0-kontakt |
| **f2** | HDMI1-kontakt |
| **g1** | M.2-kontakt för NVMe SSD |
| **h1** | CAN FD-gränssnitt (typ Phoenix MC, delning 3,81 mm) |
| **h2** | Bygel för CAN-terminering. Kortslut stiften för att koppla in termineringsmotståndet på CAN FD-bussen. |
| **i1** | RS-485-gränssnitt (typ Phoenix MC, delning 3,81 mm) |
| **i2** | Bygel för automatisk/manuell aktivering av RS-485. |
| **i4** | Bygel för XRS-485 RX Enable. Kortslut stiften för att aktivera mottagning av RS-485-trafik. |
| **j1** | Kontakt för Compute Module USB Boot. Används för att flasha Compute Module 5:s firmware. |
| **j2** | Omkopplare för Compute Modules startläge. Sätt den i läget ”Normal” för normal drift och i läget ”Abnormal” för USB-startläge. En varningslysdiod tänds när omkopplaren står i läget ”Abnormal”. |
| **m1** | USB3-kontakt 0. Ansluten direkt till CM5. |
| **m2** | USB3-kontakt 1-0. Ansluten till USB3-hubben på kortet. |
| **m3** | USB3-kontakt 1-1. Ansluten till USB3-hubben på kortet. |
| **m4** | USB3-kontakt 1-2. Ansluten till USB3-hubben på kortet. |
| **n1** | CR2032-batterihållare för realtidsklockan (RTC) |
| **q1** | Kontakt för CM5-fläkt. Fläkten kan användas för att förbättra luftcirkulationen inuti kapslingen. Den behövs inte när standardkapslingen används. |

![Bärkortets kontakter, undersidan](./carrier-board-bottom-conx.jpg)
*Bärkortets kontakter, undersidan.*

En förteckning över kontakterna på undersidan följer nedan.

| Märkning | Beskrivning |
|:---------|:------------|
| **p1** | Kontakt för Compute Module 5. |
| **q1** | Kontakt för CM5-fläkt, alternativ placering. Den här stiftlisten kan användas för att ansluta en processorfläkt ovanpå CM5-modulen i en egen kapsling. **Obs:** Kontakterna **q1** och **q2** är parallellkopplade och får inte användas samtidigt. |

Slutligen sitter antennkontakten för WiFi och Bluetooth på själva Compute Module 5. Den visas i bilden nedan.

![Antennkontakt för WiFi](./cm5-top-conx.jpg)
*U.FL-antennkontakten på Compute Module 5.*

| Märkning | Beskrivning |
|:---------|:------------|
| **r1** | U.FL-kontakt för WiFi- och Bluetooth-antennen. |

### Blinkenlights

Bärkortet har flera statuslysdioder för systemövervakning.

![Bärkortets statuslysdioder](./carrier-board-top-leds.jpg)
*Bärkortets statuslysdioder och deras färger.*

Statuslysdioderna ger information om systemets ström- och aktivitetstillstånd. En förteckning över dem följer nedan.

| Märkning | Färg | Beskrivning |
|----------|:-----|:------------|
| **1** | RGB | Fem RGB-lysdioder. De används för att visa systemets tillstånd och aktivitet på frontpanelen. |
| **2** | Röd | Strömlysdioder för 3,3 V- och 5 V-skenorna. De visar strömtillståndet för respektive spänningsskena. |
| **3** | Gul | Indikering av ethernethastighet. Lyser när ethernetporten har förhandlat fram en förbindelse på 100/1000 Mbit/s. |
| **4** | Grön | Indikering av ethernetaktivitet. Blinkar när det finns nätverkstrafik på ethernetporten. |
| **5** | Blå | Indikering av SSD-aktivitet. Blinkar när det finns läs- eller skrivaktivitet på M.2 NVMe SSD-enheten. |
| **6** | Röd | Indikering av Pi:ns strömtillstånd. Lyser när systemet har spänning men är avstängt. |
| **7** | Grön | Indikering av Pi:ns aktivitet. Blinkar när det finns aktivitet på Raspberry Pi:n. |
| **8** | Bärnstensgul | Varning för onormalt startläge. Lyser när omkopplaren för USB-startläge står i läget ”Abnormal”. Det betyder att enheten är inställd för flashning via USB Boot-kontakten och inte startar normalt. |
| **9** | Grön | CAN TX/RX-lysdioder. De blinkar när data tas emot (RX) eller sänds (TX) på CAN-gränssnittet. |
| **10** | Grön | RS-485 TX/RX-lysdioder. De blinkar när data tas emot (RX) eller sänds (TX) på RS-485-gränssnittet. |

RGB-lysdiodernas mönster beskrivs i [Systemdrift](./operation.md#status-ledar).

## Konfiguration av strömbegränsningen

Bärkortet har en omkopplare för strömbegränsning som ställer in den maximala ström som matas ut till kringenheter. Omkopplaren hittar du som **a2** i bilden i avsnittet [Bärkortets kontakter](#barkortets-kontakter).

!!! info "Inställningar för strömbegränsningen"
    **Inställningen 0,9 A (standard):**

    - Obligatorisk vid matning från NMEA 2000-bussen
    - Lämplig för grundläggande drift

    **Inställningen 2,5 A:**

    - För strömtörstiga kringenheter
    - Snabbare laddning av superkondensatorerna
    - Endast med egen strömanslutning

För att ändra strömbegränsningen stänger du först av HALPI2 helt och tar bort kapslingens lock enligt anvisningen i avsnittet Åtkomst till kapslingen. Leta upp omkopplaren för strömbegränsning på bärkortet och ställ den i önskat läge (antingen 0,9 A eller 2,5 A). När inställningen är ändrad monterar du ihop kapslingen igen och kontrollerar att alla anslutningar sitter kvar ordentligt.

## Att använda HAT-kort

### HAT-kompatibilitet

HALPI2 stöder vanliga Raspberry Pi HAT-kort via sin 40-poliga GPIO-stiftlist och är fullt elektriskt och mekaniskt kompatibel med HAT-specifikationen. Bärkortet har samma GPIO-stiftläge som en vanlig Raspberry Pi, vilket gör att de flesta HAT-kort avsedda för Raspberry Pi 4 och 5 fungerar utan ändringar. Kompatibiliteten gäller både officiella Raspberry Pi HAT-kort och tredjepartskort som följer HAT-standarden.

### Fysiska begränsningar

HALPI2:s kapsling ger 45 mm fri höjd ovanför bärkortet, vilket räcker för upp till två staplade HAT-kort. Ytan till vänster om det markerade HAT-området upptas av superkondensatorerna, vilket begränsar utrymmet för kort som sträcker sig utanför standardmåtten 65 mm × 56 mm. Var särskilt uppmärksam på HAT-kort med kontakter i kanten. Kontakter som pekar ”söderut” eller ”österut” går bra, men de som pekar ”västerut” kan komma i vägen för superkondensatorerna.

### Konflikter mellan GPIO-stift

Flera GPIO-stift används av HALPI2:s inbyggda gränssnitt och måste beaktas när du väljer HAT-kort. Tabellen nedan visar de reserverade stiften och deras funktioner:

| GPIO-nummer | Funktion | Gränssnitt | Anmärkningar |
|-------------|----------|------------|--------------|
| GPIO 2 | I2C SDA | Systemets I2C | Kan delas; adressen 0x6d är reserverad |
| GPIO 3 | I2C SCL | Systemets I2C | Kan delas; adressen 0x6d är reserverad |
| GPIO 6 | SPI CS | CAN FD | Egen chip select för CAN-styrkretsen |
| GPIO 9 | SPI MISO | CAN FD | Delad SPI0-buss |
| GPIO 10 | SPI MOSI | CAN FD | Delad SPI0-buss |
| GPIO 11 | SPI SCK | CAN FD | Delad SPI0-buss |
| GPIO 12 | UART TX | RS-485 | UART4 sändning |
| GPIO 13 | UART RX | RS-485 | UART4 mottagning |
| GPIO 24 | RS-485 EN | RS-485 | Aktiveringssignal (endast manuellt läge) |
| GPIO 26 | CAN INT | CAN FD | Avbrottsledning för CAN-styrkretsen |

### Delade gränssnitt och konflikter

I2C-bussen på GPIO 2 och 3 kan delas med HAT-enheter, eftersom I2C stöder flera enheter på samma buss. HAT-kort får dock inte använda I2C-adressen 0x6d, som är reserverad för HALPI2:s systemstyrkrets. De flesta I2C-kort fungerar utan problem, men kontrollera vilka I2C-adresser de använder före installationen.

SPI0-bussen som CAN FD-gränssnittet använder kan i princip delas med andra SPI-enheter, eftersom HALPI2 använder egna stift för chip select (GPIO 6) och avbrott (GPIO 26). HAT-kort som använder SPI0 med de vanliga chip select-stiften (GPIO 7 eller GPIO 8) kan samexistera med CAN-gränssnittet, men kan kräva ytterligare konfiguration med device tree-överlägg.

### Att stänga av inbyggda gränssnitt

Om ett HAT-kort kräver exklusiv tillgång till stift som HALPI2:s inbyggda gränssnitt upptar, kan gränssnitten stängas av med ändringar i hårdvaran. CAN FD-gränssnittet kan frigöras helt genom att lödbygeln GPIO6-CAN.CS på bärkortets undersida tas bort. Ändringen kopplar bort CAN-styrkretsen från SPI-bussen och frigör GPIO 6, 9, 10, 11 och 26 för HAT-bruk.

RS-485-gränssnittet kan stängas av genom att bygeln RX Enable (i4) på bärkortet tas bort. Det hindrar RS-485-transceivern från att ta emot data och frigör GPIO 12 och 13 för andra ändamål. Om manuell styrning av sändningsaktiveringen inte behövs kan även GPIO 24 användas till annat, genom att bygeln för automatisk/manuell aktivering av RS-485 (i2) sätts i automatiskt läge.

### Monteringsanvisning

Börja med att stänga av systemet och koppla bort alla strömkällor. Ta bort kapslingens lock enligt anvisningen i avsnittet Åtkomst till kapslingen.

Bärkort av version 0.5.0 och senare har förmonterade M2.5-gänginsatser på HAT-kortets fyra fästpunkter, vilket förenklar monteringen. På äldre kort av version 0.4.0 måste M2.5-muttrar monteras för hand. För att montera muttrarna måste bärkortet tillfälligt demonteras. Det går att göra utan att koppla bort alla kablar.

För många vanliga HAT-kort passar distanser på 15 mm, men mät honlistens höjd för att säkerställa rätt avstånd. Hanlistens sockel är 2,5 mm hög, så lägg till det till honlistens höjd för att få fram rätt distanslängd.

Skruva i distanserna i fästhålen, eller fäst dem med muttrar underifrån på kort av version 0.4.0. Passa in HAT-kortet mot den 40-poliga GPIO-stiftlisten och kontrollera att alla stift ligger rätt innan du trycker jämnt för att få kontakten på plats. Kortet ska sitta parallellt med bärkortet, utan synlig glipa vid GPIO-anslutningen.

Fäst HAT-kortet med M2.5-skruvar eller ytterligare distanser genom kortets fästhål ned i distanserna. Skruvarna ingår inte i HALPI2 utan måste skaffas separat. Dra åt dem precis så mycket att kortet sitter stadigt, utan att kretskortet böjs.

### Kabeldragning

Om HAT-kortet har externa kontakter som behöver nås utifrån kapslingen bör du montera lämpliga panelkontakter i de lediga PG7-genomföringsplatserna. Då bevaras kapslingens skydd mot väder och vind samtidigt som anslutningen blir enkel att nå.

### Demontering

Demontering av ett HAT-kort följer monteringen i omvänd ordning. Stäng av systemet helt och koppla bort alla strömkällor innan du öppnar kapslingen. Ta bort M2.5-fästskruvarna och lyft kortet rakt upp från GPIO-stiftlisten, utan sidokrafter som kan böja stiften.

Om kortet sitter fast, leta efter förbisedda skruvar eller kablar innan du tar i mer. Vissa HAT-kort med tätt sittande kontakter kan behöva vaggas försiktigt medan du drar uppåt. Vagga kortet i nord-sydlig riktning; att vagga öst-västligt riskerar att böja stiften när kontakten plötsligt släpper.

### Konfiguration av programvaran

Efter monteringen kan HAT-kortet behöva konfigureras i programvaran för att fungera. Många kort levereras med device tree-överlägg som måste aktiveras i Raspberry Pi:ns konfiguration. Redigera `/boot/firmware/config.txt` och lägg till de `dtoverlay`-rader som anges i kortets dokumentation.

!!! quote "Relaterad information"
    - **GPIO-stiftläge:** se [Hårdvarureferens](../technical-reference/hardware.md)
    - **Konfiguration av programvaran:** se [Avancerad konfiguration](../software-development/advanced-config.md)
    - **Ändringar i kapslingen:** se [Egna kontaktalternativ](#egna-kontaktalternativ)

## Byte av NVMe SSD

### SSD-kompatibilitet

HALPI2 stöder M.2 2230–2280 NVMe SSD-enheter i vanligt enkelsidigt utförande. Kortare 2230-enheter kan vara dubbelsidiga tack vare det extra utrymmet vid den fästpunkten, men längre enheter måste vara enkelsidiga för att få plats på bärkortet.

Kompatibiliteten kan bara garanteras för SSD-enheter som levereras av Hat Labs och för officiella Raspberry Pi-enheter. Om du överväger en enhet från tredje part bör du kontrollera dess kompatibilitet med Raspberry Pi 5 före köpet, genom användarrapporter och kompatibilitetslistor på nätet. Vanliga problem med inkompatibla enheter är alltför hög strömförbrukning, överhettning samt startfel eller instabilitet.

### Förbereda den nya SSD-enheten

Innan en ny SSD monteras i HALPI2 bör operativsystemet flashas till enheten. Det går att flasha SSD-enheten efter monteringen via CM5:ns USB Boot-kontakt (j1), men det är enklare och snabbare med en extern USB-NVMe-adapter. Flashningen beskrivs i [Programvaruguiden](./software.md).

### Att stänga av systemets 3,3 V-spänning

Superkondensatorerna kan hålla bärkortets 3,3 V-skena spänningssatt en avsevärd tid efter att huvudströmmen kopplats bort. Eftersom SSD-enheten matas från 3,3 V-skenan måste skenan stängas av, så att enheten säkert är spänningslös före demontering eller montering.

Börja med att stänga av HALPI2 och koppla bort strömförsörjningen. Öppna kapslingen enligt anvisningen i avsnittet Åtkomst till kapslingen.

Leta upp bygeln ”3.3V off” på bärkortet. Placeringen varierar med kortets version. På kort av version 0.4.0 sitter bygeln mycket nära superkondensatorerna, på deras ”södra” sida. På kort av version 0.5.0 och senare hittar du stiftlisten ”Pow.Ctrl” ”öster” om superkondensatorerna. Stiften ”3.3V off” är de två översta på listen.

Flytta bygeln så att stiften ”3.3V off” kortsluts. Det stänger av 3,3 V-skenan, vilket syns genom att lysdioderna slocknar.

### Demontering

M.2-platsen sitter vid bärkortets södra kant. Se bilden i avsnittet [Bärkortets kontakter](#barkortets-kontakter) för att hitta M.2-kontakten märkt **g1**.

Ta bort M2.5-fästskruven med en PH1-skruvmejsel. När skruven är borta fjädrar SSD-enheten upp i vinkel. Lyft enheten försiktigt i fäständen och vicka ut den ur M.2-kontakten. Håll i enhetens kanter för att inte skada komponenter eller kontakter.

### Montering

För in den förberedda SSD-enheten i M.2-kontakten i ungefär 30 graders vinkel och se till att skåran i enheten passar mot kontaktens styrning. Enheten ska glida in mjukt, utan att du behöver ta i. När den sitter helt på plats trycker du ned fäständen tills den ligger plant mot distansen.

Fäst SSD-enheten med M2.5-skruven och en PH1-skruvmejsel. Dra åt precis så mycket att enheten hålls stadigt på plats. Den ska ligga helt plant, utan synlig böj.

När SSD-enheten sitter på plats tar du bort bygeln från stiften ”3.3V off” för att koppla in 3,3 V-skenan igen. Låt bygeln sitta kvar på stiftlisten för framtida bruk.

Montera ihop kapslingen enligt avsnittet Åtkomst till kapslingen.
För konfiguration av programvaran och felsökning, se [Programvaruguiden](./software.md).

!!! quote "Relaterad information"
    - **Systemavbilder:** se [Programvaruguiden](./software.md)
    - **Startförlopp:** se [Systemdrift](./operation.md)
    - **Åtkomst till hårdvaran:** se [Åtkomst till kapslingen](#atkomst-till-kapslingen)

## Byte av Compute Module 5

### Förutsättningar

Byte av Compute Module 5 kräver varsamhet, eftersom kort-till-kort-kontakterna är ömtåliga. CM5 använder två kontakter med hög täthet som lätt skadas av alltför stor kraft eller fel teknik. Demontera en befintlig modul bara när det är absolut nödvändigt, till exempel om den är trasig eller ska uppgraderas. Skador på Compute Modules monteringskontakter — på CM5 eller på bärkortet — täcks inte av garantin.

Innan du börjar bör du ha värmeledande dynor till hands. I standardutförandet används en 1 mm tjock dyna på SoC:n och 2 mm tjocka dynor på RP1-kretsen och den interna strömförsörjningens komponenter. Befintliga dynor kan återanvändas om de är hela och rena.

### Att komma åt Compute Module

Stäng av HALPI2 och koppla bort strömkällan. Ta bort kapslingens lock enligt anvisningen i avsnittet Åtkomst till kapslingen. CM5 sitter på bärkortets undersida, så du måste först demontera bärkortet från kapslingen för att komma åt den. För att hålla reda på de många kablar som är anslutna till bärkortet rekommenderas att du tar några foton av anslutningarna innan du fortsätter.

Koppla bort de kablar som hindrar dig från att lyfta bärkortet. Ta bort bärkortets fästskruvar och lyft ut kortet ur kapslingen.

### Att ta bort den befintliga modulen

!!! danger "Varning"
    Om CM5-modulen lossas en kontakt i taget kan vridkrafterna slita loss kontakten från modulen. Sådana skador täcks inte av garantin.

CM5 hålls fast av två kort-till-kort-kontakter som kräver varsam hantering. Använd aldrig metallverktyg för det här momentet, eftersom de kan skada kontakterna eller närliggande ytmonterade komponenter. Använd en spudger av trä eller plast, ett plektrum eller ett liknande icke ledande verktyg.

Placera verktyget mitt på CM5-modulens vänstra kortsida, mellan modulen och bärkortet. Tryck bestämt nedåt i hörnen på den högra sidan. Bänd försiktigt uppåt med minimal kraft — modulen ska lossna med ett lätt klick och båda kontakterna ska släppa samtidigt.

![Demontering av CM5-modulen](./unmount-cm5.jpg)
*Demontera CM5-modulen genom att trycka nedåt i den högra kantens hörn samtidigt som du bänder uppåt mitt på den vänstra kanten. Båda kontakterna ska släppa samtidigt.*

### Att montera den nya modulen

Passa in den nya CM5-modulen mot bärkortets kontakter med hjälp av konturen i tryckskiktet på bärkortet. Den utritade konturen ska stämma exakt med CM5:ns mått när modulen ligger rätt vänd.

När modulen är inpassad trycker du varsamt och jämnt vid kontaktlägena på båda kortsidorna. Du ska känna hur kontakterna griper med ett svagt klick. Tryck bestämt, men undvik att böja bärkortet — stöd kortet underifrån om det behövs. Båda kontakterna måste sitta helt i för att modulen ska fungera.

Sätt sedan de värmeledande dynorna på CM5-modulen. De ska placeras rätt: en 1 mm dyna på huvud-SoC:n och 2 mm dynor på RP1-kretsen och strömförsörjningens komponenter. Om du återanvänder befintliga dynor, kontrollera att de är rena och rätt placerade.

![Placering av värmeledande dynor på CM5](./cm5-thermal-pads-annotated.jpg)
*Placering av de värmeledande dynorna på Compute Module 5. Använd en 1 mm tjock dyna på SoC:n (i mitten) och 2 mm tjocka dynor på RP1 och strömförsörjningens komponenter. Dynornas verkliga former och storlekar kan variera.*

### Anslutning av antennen

Innan du sätter tillbaka bärkortet ansluter du U.FL-antennkabeln till CM5:ns trådlösa antennkontakt. Den anslutningen går inte att komma åt när bärkortet väl är monterat. U.FL-kontakten kräver noggrann inpassning och ett bestämt tryck för att sitta rätt. Du ska känna ett tydligt knäpp när kontakten är helt på plats. Var försiktig så att du inte böjer kontaktens hölje under monteringen.

### Slutlig montering

Kontrollera monteringen: båda kontakterna ska sitta helt i och modulen ska ligga plant mot bärkortet utan glipor. De värmeledande dynorna ska ha kontakt med modulens värmealstrande komponenter.

Placera bärkortet tillbaka i kapslingen och se till att dynorna på CM5 hamnar mot motsvarande värmeavledande ytor i kapslingens botten. Sätt tillbaka alla bärkortets fästskruvar och återanslut de kablar som kopplades bort vid demonteringen.

Slutför monteringen enligt det vanliga förfarandet för att stänga kapslingen. Vid första start ska systemet känna igen den nya CM5-modulen automatiskt.

!!! warning "Varning för kontakterna"
    Kort-till-kort-kontakterna är de ömtåligaste delarna i det här momentet. Använd aldrig metallverktyg nära kontakterna, använd bara vertikal kraft vid demontering och montering, och kontrollera att inpassningen är perfekt innan du trycker. Skadade kontakter kräver i regel att bärkortet byts.

!!! quote "Relaterad information"
    - **Uppsättning av systemet efter bytet:** se [Programvaruguiden](./software.md)
    - **Felsökning av starten:** se [Felsökning](./troubleshooting.md)
    - **Värmehantering:** se [Hårdvarureferens](../technical-reference/hardware.md)

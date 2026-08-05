---
translated_from: a51e1cfe53d070c073a563641f9301fd3383a418
---

# Guida introduttiva

Questa guida consente di mettere in funzione l’HALPI2 in meno di 30 minuti e comprende anche l’installazione permanente. Seguire questi passaggi nell’ordine indicato per una configurazione senza intoppi: iniziare con una configurazione da tavolo per verificare che tutto funzioni, quindi procedere all’installazione permanente.

## Precauzioni di sicurezza e di manipolazione

!!! warning "Prima di iniziare"
    - Assicurarsi che l’alimentazione sia scollegata dall’impianto elettrico prima di effettuare i collegamenti
    - Utilizzare fusibili adeguati (3–5 A) per i collegamenti di alimentazione
    - Maneggiare l’unità con cura: sebbene sia robusta, cadute o urti possono danneggiare i componenti interni
    - Verificare la corretta polarità durante il collegamento dei cavi di alimentazione
    - Evitare le scariche elettrostatiche: scaricare l’elettricità statica dal proprio corpo ed evitare di strofinare gatti e oggetti d’ambra prima di toccare i componenti interni

## Che cosa serve

Dalla confezione dell’HALPI2:

- Unità HALPI2 con CM5 e unità SSD NVMe preinstallati
- Cavo di alimentazione con connettore E7T (lunghezza 2 m)

Elementi opzionali (inclusi nella confezione di vendita):

- Coppia di connettori cilindrici (barrel) CC da 5,5 × 2,1 mm, per l’uso con un alimentatore standard da 12 V di tipo “wall wart”
- Antenna WiFi/Bluetooth Raspberry Pi (necessaria se si utilizza il WiFi per la configurazione iniziale)

Elementi aggiuntivi (non inclusi):

- Sorgente di alimentazione da 12 V o 24 V
- Un computer separato per la configurazione senza monitor (headless), se non si utilizza un display collegato
- Cavo di rete (opzionale, per la connessione via cavo)
- Display con ingresso HDMI (opzionale)
- Tastiera e mouse USB (opzionali, per l’accesso diretto)

!!! tip "Suggerimento rapido"
    Qualsiasi dispositivo di rete, come un router o un access point WiFi, utilizza in genere un alimentatore da 12 V che può essere impiegato per alimentare l’HALPI2. Vale la pena cercarne uno nella pila di vecchio hardware!

## Configurazione da tavolo

Si consiglia di provare l’HALPI2 su una scrivania o su un banco di lavoro prima di installarlo in modo permanente. La configurazione iniziale può essere eseguita senza monitor (headless) tramite una connessione di rete, oppure con display, tastiera e mouse collegati. Una configurazione senza monitor può essere effettuata tramite una connessione Ethernet via cavo oppure tramite l’access point WiFi dell’HALPI2.

### Passaggio 1: collegare le periferiche essenziali

#### Per la configurazione iniziale:

1. **Connessione di rete (necessaria per l’installazione senza monitor):**
    - Collegare il cavo Ethernet
    - Collegare l’antenna WiFi/Bluetooth

2. **Collegamento del display (opzionale):**
    - Collegare un display HDMI per l’accesso diretto
    - Tastiera e mouse USB se si utilizza un display

![Connettori del pannello frontale](./front-panel-connectors.jpg)
*Connettori del pannello frontale*

### Passaggio 2: collegamento NMEA 2000 (opzionale)

Se l’HALPI2 viene installato direttamente su un’imbarcazione oppure se è disponibile un’installazione NMEA 2000 da tavolo, è già possibile collegarlo alla rete NMEA 2000.

Una [rete NMEA 2000](https://docs.hatlabs.fi/nmea2000/) è costituita da un cavo dorsale al quale tutti i dispositivi si collegano tramite connettori a T e cavi di derivazione. Aggiungere un connettore a T alla dorsale della rete NMEA 2000. Collegare il connettore micro NMEA 2000 dell’HALPI2 al connettore a T utilizzando un cavo di derivazione NMEA 2000.

### Passaggio 3: collegamento dell’alimentazione

!!! tip "Nota sull’alimentazione tramite NMEA 2000"
    L’HALPI2 può essere alimentato anche tramite il bus NMEA 2000. Vedere [Collegamento dell’alimentazione tramite bus NMEA 2000](#collegamento-dellalimentazione-tramite-bus-nmea-2000) nella sezione Installazione permanente più avanti.

Per la configurazione da tavolo si utilizza il cavo di alimentazione E7T in dotazione. Collegare le estremità dei conduttori del cavo di alimentazione alla presa cilindrica femmina come segue:

- **Conduttore rosso = positivo (+)**
- **Conduttore nero = negativo (-)**

![Da E7T a connettore cilindrico](./e7t-barrel.jpg)
*Esempio di cablaggio dal connettore E7T al connettore cilindrico*

Collegare un alimentatore standard da 12 V o 24 V al connettore cilindrico. Assicurarsi che l’alimentatore sia dimensionato per almeno 1 A, in modo da soddisfare i requisiti dell’HALPI2.

!!! warning "Avvertenza"
    In assenza di uno scarico della trazione, il connettore cilindrico con morsetti a vite deve essere utilizzato solo per installazioni temporanee. Una trazione accidentale sul cavo può scollegare i conduttori ed esporli.

## Primo avvio

HALPI2 viene fornito con [HaLOS](https://docs.halos.fi), una distribuzione Linux basata su container con un’interfaccia di gestione web, progettata per applicazioni nautiche e industriali. Se si preferisce un altro sistema operativo, come OpenPlotter o Raspberry Pi OS, vedere la [Guida al software](../user-guide/software.md).

!!! info "Documentazione di HaLOS"
    Questa guida riguarda l’hardware HALPI2 e la prima accensione. Tutto ciò che concerne il sistema operativo — configurazione al primo avvio, rete, applicazioni, certificati e uso quotidiano — si trova nella **[documentazione di HaLOS](https://docs.halos.fi)**. È utile tenerla a portata di mano durante i passaggi descritti di seguito.

**Accendere l’HALPI2** collegando l’alimentatore, se non è già stato fatto. Dopo alcuni secondi,
la barra LED dovrebbe iniziare a riempirsi di luci rosse, a indicare che i supercondensatori si stanno caricando. I LED diventano gialli quando il sistema si sta avviando e infine verdi quando il sistema operativo è in esecuzione e il demone HALPI è connesso al controller.

Se è collegato un display, dovrebbe comparire la schermata iniziale di Raspberry Pi OS e infine il desktop grafico.

!!! tip "Suggerimento"
    Le sequenze dei LED di stato sono documentate nella [Guida al funzionamento](../user-guide/operation.md).

### Accedere all’HALPI2 senza display

Se non è collegato alcun display, è possibile accedere all’HALPI2 tramite il suo access point WiFi o tramite una connessione Ethernet. HaLOS offre un’interfaccia web: non è necessario alcun software aggiuntivo[^ssh].

[^ssh]: SSH è disponibile anche nelle immagini HaLOS senza monitor (abilitato per impostazione predefinita). Nelle varianti Desktop, abilitare SSH tramite `raspi-config`. Credenziali predefinite: nome utente `pi`, password `halos`.

Attendere innanzitutto che i LED diventino verdi, a indicare che il sistema è completamente avviato. Quindi seguire questi passaggi:

**Opzione 1 — connessione tramite access point WiFi:** HaLOS crea un access point WiFi denominato `Halos-XXXX` (univoco per ogni dispositivo) con la password `halos1234`. Collegare il computer a questa rete.

L’access point non dispone di una connessione a internet propria, quindi il passaggio successivo consiste nell’indirizzare l’HALPI2 verso una rete WiFi che ne disponga (necessaria per scaricare le applicazioni in container al primo avvio):

1. Aprire Cockpit all’indirizzo `https://halos.local:9090/` ed effettuare l’accesso (nome utente `pi`, password `halos`).
2. Accedere a **Networking** e fare clic su **WiFi (wlan0)**.
3. Attendere la comparsa dell’elenco delle reti disponibili, quindi fare clic sulla rete desiderata.
4. Inserire la password e fare clic su **Add**.

L’HALPI2 mantiene attivo l’access point `Halos-XXXX` mentre si collega alla rete, per cui il computer potrebbe disconnettersi brevemente dall’access point e riconnettersi da solo.

**Opzione 2 — connessione via cavo Ethernet:** se l’HALPI2 è stato collegato alla rete tramite Ethernet, ottiene automaticamente un indirizzo IP tramite DHCP.

Una volta stabilita la connessione, aprire un browser e accedere a:

- **Dashboard:** `https://halos.local/` — la dashboard principale Homarr, con i collegamenti a tutte le applicazioni installate
- **Amministrazione del sistema:** `https://halos.local:9090/` — Cockpit per la gestione del sistema, gli aggiornamenti e le applicazioni in container

!!! note "Avviso sul certificato SSL"
    Alla prima apertura della dashboard o di Cockpit, il browser mostra un avviso “Not secure”. HaLOS firma i propri servizi web con un’autorità di certificazione (CA) generata sul dispositivo stesso, e il browser non considera ancora attendibile tale CA. Per il momento, accettare l’avviso e proseguire.

    Per eliminare definitivamente l’avviso, installare una sola volta la CA del dispositivo sul computer: da quel momento ogni servizio HaLOS viene validato correttamente su ogni porta. Aprire `https://halos.local/ca/` per un programma di installazione guidato specifico per piattaforma, oppure vedere [Trust the device](https://docs.halos.fi/user-guide/trust-the-device/) nella documentazione di HaLOS.

!!! info "Connessione a internet necessaria al primo avvio"
    L’interfaccia Cockpit è disponibile immediatamente, ma la dashboard principale e le altre applicazioni basate su container richiedono una connessione a internet al primo avvio per scaricare le rispettive immagini del container. Collegare l’HALPI2 a internet tramite Ethernet oppure configurare il WiFi da Cockpit.

### Configurazione al primo avvio

!!! warning "Avvertenza"
    HaLOS è dotato di password predefinite che **devono** essere modificate durante il primo avvio, per impedire accessi non autorizzati al dispositivo.

HaLOS dispone di due set di credenziali:

| Tipo di accesso | Nome utente | Password predefinita | Utilizzato per |
|:------------|:---------|:-----------------|:---------|
| SSO (applicazioni web) | `admin` | `halos` | Dashboard, Signal K, Grafana e altre applicazioni web |
| Sistema (SSH/Cockpit) | `pi` | `halos` | Accesso SSH, amministrazione del sistema con Cockpit |

#### Modifica delle password

- **Password SSO:** modificarla tramite Authelia (accessibile dalla dashboard)
- **Password di sistema:** modificarla tramite Cockpit (`https://halos.local:9090/`) nelle impostazioni dell’account utente, oppure via SSH con `passwd`

Per istruzioni dettagliate sul primo avvio, vedere la [guida introduttiva di HaLOS](https://docs.halos.fi/getting-started/first-boot/).

!!! info "Si utilizza OpenPlotter o Raspberry Pi OS?"
    Se è stato scritto un sistema operativo alternativo, vedere la [Guida al software](../user-guide/software.md#configurazione-iniziale-del-sistema) per le istruzioni di configurazione specifiche del sistema operativo.

### Verifica del collegamento NMEA 2000 (opzionale)

Il modo più semplice per verificare la connettività NMEA 2000 è controllare lo stato del server Signal K. Nelle varianti dell’immagine HaLOS Marine, Signal K è preinstallato e accessibile dalla dashboard all’indirizzo `https://halos.local/`. Per le immagini HaLOS non nautiche, Signal K può essere installato dallo store Container Apps in Cockpit.

Aprire l’interfaccia web di Signal K e osservare l’attività della connessione `can0`: dovrebbe essere visibile del traffico in ricezione.

![Attività delle connessioni del server Signal K](./sk-n2k-deltas.jpg)

## Spegnimento del dispositivo

L’HALPI2 è progettato per spegnersi automaticamente quando viene scollegato dall’alimentazione. Per spegnere il dispositivo è sufficiente togliere l’alimentazione, tramite un interruttore del quadro elettrico oppure scollegando il connettore di alimentazione. Il sistema avvia automaticamente una sequenza di spegnimento software, garantendo che tutte le applicazioni si chiudano correttamente e che il file system venga smontato in sicurezza.

Se si sceglie di spegnere il sistema tramite l’interfaccia desktop o strumenti da riga di comando (come il comando `shutdown`), il dispositivo si riavvia automaticamente dopo circa 5 secondi. Questo comportamento è dovuto al sistema di gestione dell’alimentazione, che rileva la presenza di alimentazione esterna.

Durante lo spegnimento è possibile monitorare lo stato del sistema tramite i LED sul pannello frontale. Quando l’alimentazione viene interrotta, i LED verdi si attenuano per segnalare una condizione di interruzione di corrente. Dopo 5 secondi i LED diventano viola, a indicare chiaramente che il dispositivo si sta spegnendo. Al termine del processo di spegnimento tutti i LED si spengono.

In condizioni normali lo spegnimento richiede in genere solo pochi secondi. In alcuni casi, tuttavia, determinati servizi possono richiedere più tempo per arrestarsi correttamente. In tal caso il dispositivo può scaricare quasi completamente i supercondensatori prima di spegnersi. Questo tempo di spegnimento prolungato è normale e non indica un guasto del sistema.

## Risoluzione dei problemi di configurazione iniziale

### Problemi comuni e meno comuni:

❌ **Assenza di alimentazione o LED spenti:**

- Verificare i collegamenti di alimentazione e la polarità
- Controllare lo stato del fusibile
- Assicurarsi che la tensione rientri nell’intervallo 11–32 V

❌ **Access point WiFi non visibile:**

- Assicurarsi che l’antenna sia collegata correttamente
- Provare a connettersi con un altro dispositivo
- Verificare che l’HALPI2 sia completamente avviato (i LED devono essere verdi)
- Provare prima a connettersi tramite Ethernet

❌ **Impossibile accedere al dispositivo tramite `halos.local`:**

- Provare a utilizzare l’indirizzo IP assegnato (consultare l’elenco dei client DHCP del router)

❌ **Display collegato che non mostra nulla:**

- Assicurarsi che il cavo HDMI sia collegato saldamente
- Assicurarsi che il display sia acceso e impostato sull’ingresso corretto
- Provare un altro cavo HDMI o un’altra porta del display
- Assicurarsi che l’HALPI2 sia acceso (i LED devono essere gialli o verdi)
- Se i LED lampeggiano con una sequenza arcobaleno, il Compute Module 5 non è inserito correttamente. La causa può essere un danno durante il trasporto. Seguire le istruzioni nella [Guida utente](../user-guide/operation.md) per reinserire il CM5 oppure contattare l’assistenza.

❌ **Il display collegato mostra un messaggio di errore relativo a “nvme”:**

- Ciò indica che l’unità SSD NVMe non viene rilevata o non è inizializzata correttamente. La causa può essere un danno durante il trasporto. Seguire le istruzioni nella [Guida utente](../user-guide/operation.md) per reinserire l’unità SSD NVMe oppure contattare l’assistenza.

### Come ottenere assistenza:

- **Documentazione:** consultare le sezioni specifiche per una risoluzione dei problemi dettagliata
- **Comunità:** partecipare ai forum della comunità di Hat Labs
- **Assistenza:** contattare l’assistenza tecnica per i problemi hardware

---

## Installazione permanente

Dopo aver verificato che tutto funzioni sulla scrivania, seguire questi passaggi per il montaggio e il cablaggio definitivi.

### Pianificazione dell’installazione

!!! tip "Suggerimento rapido"
    Fotografare il cablaggio esistente prima di apportare modifiche: sarà utile in caso di successiva risoluzione dei problemi.

Dedicare tempo alla pianificazione dell’installazione. Occorre considerare:

- **Posizione di montaggio** — accessibilità, protezione, ventilazione
- **Posa dei cavi** — percorsi più brevi, protezione dai danni
- **Sorgente di alimentazione** — circuito dedicato o condiviso, requisiti di protezione con fusibili
- **Integrazione di rete** — NMEA 2000, Ethernet, copertura WiFi
- **Fattori ambientali** — temperatura, umidità, vibrazioni

#### Utensili e materiali necessari

**Utensili:**

- Trapano con punte
- Set di cacciaviti (PH2 Phillips, taglio grande)
- Pinza spelafili e pinza crimpatrice per i collegamenti di alimentazione
- Multimetro per le verifiche
- Pistola termica o accendino (per la guaina termorestringente)

**Materiali (non inclusi):**

- Viti di montaggio (4 mm o M4, a seconda della superficie di montaggio)
- Fusibili adeguati (3–5 A) o interruttori automatici del quadro elettrico di portata corrispondente
- Cavo per uso nautico (1,5 mm² o 16 AWG per l’alimentazione, se il cavo in dotazione è troppo corto)
- Guaina termorestringente e capicorda
- Fascette e clip di fissaggio

### Montaggio

#### Scelta della posizione

Scegliere una posizione di montaggio che garantisca:

!!! tip "Condizioni di montaggio ottimali"
    - **Intervallo di temperatura:** da −20 °C a +60 °C di temperatura ambiente
    - **Ventilazione:** spazio libero sufficiente attorno alla custodia
    - **Protezione:** lontano da getti d’acqua diretti e da danni meccanici
    - **Accesso:** facile accesso ai connettori e ai LED di stato
    - **Sostegno:** superficie di montaggio solida, in grado di sostenere 2 kg più i cavi
    - **Spazio:** prevedere almeno 100 mm di spazio libero davanti ai connettori del pannello per la gestione dei cavi.

Anche se questa guida si concentra sulle installazioni fisse, nella pratica è spesso sufficiente collocare il dispositivo su una mensola o su un piano, purché sia stabile e protetto da umidità e urti.

#### Indicazioni ambientali

**Installazioni nautiche:**

- Montare al di sopra del livello previsto dell’acqua di sentina
- Evitare zone soggette a spruzzi diretti o a ristagni d’acqua
- Tenere conto del movimento e delle vibrazioni dell’imbarcazione e fissare saldamente tutti i collegamenti
- Utilizzare minuteria di fissaggio resistente alla corrosione

**Installazioni su veicoli:**

- Proteggere dal calore e dalle vibrazioni del motore
- Garantire una ventilazione adeguata negli spazi chiusi
- Tenere conto dell’accessibilità per la manutenzione
- Utilizzare un montaggio resistente alle vibrazioni

**Installazioni industriali:**

- Proteggere dagli agenti chimici di processo e dalle temperature estreme
- Tenere conto delle sorgenti di interferenza elettromagnetica
- Garantire la conformità alle normative elettriche locali
- Prevedere l’accesso per la manutenzione ordinaria

#### Orientamento di montaggio

!!! info "Orientamento consigliato"
    **Preferito:** connettori rivolti verso il basso

    - Riduce il rischio di infiltrazioni d’acqua
    - Migliora la gestione dei cavi
    - Facilita l’accesso per la manutenzione

    **Accettabile:** connettori rivolti lateralmente

    - Garantire un drenaggio adeguato
    - Utilizzare guarnizioni per gli ingressi dei cavi

    **Da evitare:** connettori rivolti verso l’alto

    - Aumenta il rischio di infiltrazioni d’acqua
    - Rende difficile la gestione dei cavi

#### Fasi di montaggio

##### Passaggio 0: scaricare e stampare la dima di foratura

Scaricare la [dima di foratura HALPI2](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) e stamparla in scala 100%. La dima consente di segnare con precisione i fori di montaggio. Se non è disponibile una stampante, è possibile utilizzare le quote riportate nella dima per segnare i fori manualmente, oppure usare la custodia stessa per tracciare i fori direttamente sulla superficie di montaggio.

[![Dima di foratura](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Passaggio 1: preparare la superficie di montaggio

1. **Pulire la superficie di montaggio**
2. **Segnare i fori di montaggio** utilizzando la dima stampata
3. **Provare il posizionamento** della custodia prima dell’installazione
4. **Praticare i fori pilota** per le viti di montaggio

##### Passaggio 2: installare l’HALPI2

1. **Posizionare la custodia** con i connettori nell’orientamento preferito
2. **Serrare le viti di montaggio** — ben salde, senza serrare eccessivamente

### Installazione permanente dell’alimentazione

#### Scelta della sorgente di alimentazione

**Opzione 1: connettore di alimentazione dedicato**

- La soluzione più affidabile e flessibile
- Supporta la piena capacità di potenza
- Manutenzione e risoluzione dei problemi più semplici

**Opzione 2: alimentazione tramite bus NMEA 2000**

- Semplifica il cablaggio nelle installazioni nautiche
- Limitata a un assorbimento di corrente di 0,9 A
- Richiede particolare attenzione alla caduta di tensione

#### Configurazione della limitazione di corrente

HALPI2 integra un limitatore di corrente in ingresso che gestisce la carica iniziale dei supercondensatori e protegge l’installazione da condizioni di sovracorrente. Il limite di corrente può essere impostato su 0,9 A oppure su 2,5 A, a seconda della sorgente di alimentazione e dei requisiti dell’applicazione. L’impostazione predefinita di 0,9 A è adatta alla maggior parte delle applicazioni.

Per aumentare la velocità di avvio iniziale o per alimentare periferiche ad alto assorbimento, è possibile passare all’impostazione da 2,5 A. Seguire i passaggi descritti nella [Guida utente](../user-guide/operation.md) per modificare l’impostazione del limite di corrente.

#### Collegamento di alimentazione dedicato

##### Preparazione del cavo

1. **Posare il cavo di alimentazione** dall’HALPI2 alla sorgente di alimentazione
2. **Prevedere una riserva di cavo (service loop)** a entrambe le estremità
3. **Proteggere il cavo** da sfregamenti e danni
4. **Tagliare a misura** lasciando spazio di lavoro sufficiente

##### Collegamento alla sorgente di alimentazione

1. **Garantire la protezione del conduttore** dedicando un interruttore automatico da 3–5 A oppure installando un fusibile in linea
2. **Spelare le estremità dei conduttori** per la lunghezza adeguata
3. **Installare i capicorda** con una corretta tecnica di crimpatura
4. **Collegare alla sorgente di alimentazione:**
    - **Conduttore rosso:** morsetto positivo (+)
    - **Conduttore nero:** morsetto negativo (-)
5. **Verificare la polarità** con il multimetro prima di dare tensione

##### Collegamento all’HALPI2

Il connettore E7T è precablato e non richiede alcuna terminazione in campo. È sufficiente inserirlo nella presa di alimentazione dell’HALPI2.

#### Collegamento dell’alimentazione tramite bus NMEA 2000

!!! info "Prerequisiti"
    - Il limitatore di corrente **deve** essere impostato su 0,9 A
    - La rete NMEA 2000 deve disporre di una capacità di alimentazione adeguata
    - Il cavo di derivazione deve trovarsi vicino al punto di alimentazione, per ridurre al minimo la caduta di tensione

##### Componenti necessari

- Cavo di derivazione NMEA 2000 (non incluso)
- Connettore a T per l’integrazione nella dorsale (non incluso)

##### Fasi di installazione

1. **Spegnere** tutti i dispositivi NMEA 2000
2. **Aprire la custodia di HALPI2** (per le istruzioni vedere la [Guida utente](../user-guide/operation.md))
3. **Individuare il connettore di alimentazione della scheda portante (carrier board)**
4. **Scollegare la morsettiera esistente**
5. **Collegare la morsettiera interna di alimentazione NMEA 2000** al connettore di alimentazione della scheda portante
6. **Verificare che il limite di corrente** sia impostato su 0,9 A
7. **Collegare alla dorsale** utilizzando un cavo di derivazione e un connettore a T adeguati
8. **Verificare l’installazione** prima della chiusura definitiva
9. **Rimontare la custodia**

![Cablaggio dell’alimentazione NMEA 2000](./n2k-power-conx.jpg)
*Per alimentare HALPI2 tramite NMEA 2000, scollegare la morsettiera 1 e sostituirla con la morsettiera 2.*

### Collegamenti di rete e dati

#### Collegamento dati NMEA 2000

Anche utilizzando un collegamento di alimentazione dedicato, può essere utile disporre della connettività dati NMEA 2000:

1. **Installare un connettore a T** sulla dorsale NMEA 2000
2. **Collegare il cavo di derivazione** tra il connettore a T e l’HALPI2
3. **Verificare la corretta terminazione** della rete NMEA 2000
4. **Verificare la connettività** dopo l’installazione

#### Collegamento Ethernet

Per la connettività di rete:

1. **Utilizzare un cavo per uso nautico** o comunque adatto all’ambiente di installazione
2. **Installare pressacavi o passacavi** se il percorso attraversa una paratia
3. **Prevedere una riserva di cavo** a entrambe le estremità
4. **Verificare la connettività** prima dell’installazione definitiva

#### Antenna WiFi/Bluetooth

1. **Installare l’antenna** sul connettore RP-SMA
2. **Posizionarla per una copertura ottimale** — lontano da ostacoli metallici. Negli armadi metallici può essere necessaria una prolunga RP-SMA maschio-femmina.
3. **Verificare l’intensità del segnale** nella posizione definitiva

### Risoluzione dei problemi di installazione

#### Problemi di alimentazione

❌ **Nessuna indicazione di alimentazione:**

- Controllare lo stato e la portata del fusibile
- Verificare la tensione della sorgente di alimentazione (11–32 V)
- Confermare la corretta polarità
- Verificare la continuità dei cavi di alimentazione

❌ **Alimentazione intermittente:**

- Controllare il serraggio di tutti i collegamenti
- Verificare la presenza di morsetti corrosi
- Verificare che la sezione del conduttore sia adeguata alla corrente

#### Connettività di rete

❌ **Nessuna comunicazione NMEA 2000:**

- Verificare la terminazione della rete (120 Ω a entrambe le estremità)
- Controllare l’installazione del connettore a T
- Verificare l’integrità del cavo di derivazione
- Provare con un dispositivo sicuramente funzionante

❌ **Nessuna connettività Ethernet:**

- Provare il cavo con un tester per cavi
- Verificare la configurazione dello switch o del router
- Controllare la presenza di conflitti di indirizzi IP
- Verificare la categoria del cavo (almeno Cat5e)

#### Problemi ambientali

❌ **Infiltrazioni di umidità:**

- Ispezionare lo stato di tutte le guarnizioni
- Verificare l’orientamento dei connettori
- Controllare i punti di ingresso dei cavi
- Valutare protezioni aggiuntive

❌ **Surriscaldamento:**

- Allontanare il dispositivo dalle fonti di calore
- Verificare che il flusso d’aria attorno alla custodia non sia ostruito

### Sicurezza e conformità

#### Sicurezza elettrica

- **Utilizzare fusibili adeguati** per la protezione da sovracorrente
- **Garantire una corretta messa a terra** secondo le normative locali
- **Proteggere dai cortocircuiti** con una posa dei cavi corretta

#### Installazioni nautiche

- **Seguire le normative locali o gli standard ABYC** per gli impianti elettrici
- **Utilizzare componenti per uso nautico** in tutto l’impianto

#### Installazioni industriali

- **Rispettare le normative elettriche locali**
- **Garantire un’adeguata protezione** da EMI/RFI
- **Documentare l’installazione** secondo i requisiti dell’impianto

## Passaggi successivi

Una volta che l’HALPI2 è in funzione:

1. **Consultare la [Guida utente](../user-guide/operation.md)** per istruzioni dettagliate sul funzionamento
2. **Esaminare i casi d’uso più comuni** per le configurazioni specifiche per applicazione
3. **Consultare il Riferimento tecnico** per le opzioni di configurazione avanzate
4. **Partecipare alla comunità** per consigli, suggerimenti e assistenza

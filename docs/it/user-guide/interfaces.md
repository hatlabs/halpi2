---
translated_from: da8aa35c462e57bc7c0b00d50046a1df518e97dd
---

# Interfacce e connettività

## CAN FD / NMEA 2000

L’HALPI2 dispone di un’interfaccia [CAN FD](https://en.wikipedia.org/wiki/CAN_FD) completamente isolata, che supporta sia le reti nautiche [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) sia le applicazioni automobilistiche o industriali. L’interfaccia offre una comunicazione dati ad alta velocità con isolamento elettrico completo, per l’immunità ai disturbi.

### Specifiche dell’interfaccia

L’interfaccia CAN FD supporta sia il protocollo CAN standard sia il CAN FD. Nelle applicazioni NMEA 2000 l’interfaccia funziona in modalità CAN normale, alla velocità dati standard di 250 kbit/s. Nelle applicazioni automobilistiche o industriali è possibile sfruttare tutte le capacità del CAN FD, con velocità dati fino a 8 Mbit/s.

Il pannello frontale è dotato di un connettore Micro-C compatibile con i cavi e i componenti NMEA 2000 standard. Ciò consente l’integrazione diretta con le reti nautiche esistenti mediante connettori a T e cavi di derivazione standard.

### Configurazione dell’alimentazione e carico sulla rete

L’impatto dell’HALPI2 sull’alimentazione della rete NMEA 2000 dipende dalla configurazione di alimentazione scelta. Nella configurazione standard, con alimentazione esterna tramite il connettore E7T, il dispositivo non richiede alimentazione dalla rete NMEA 2000 e il suo Load Equivalency Number (LEN) risulta pari a 0.

Se configurato per l’alimentazione dal bus NMEA 2000, l’assorbimento di corrente del dispositivo deve essere limitato a 0,9 A dal limitatore di corrente interno. Ciò corrisponde a un valore LEN di 18. Quando l’HALPI2 viene alimentato tramite NMEA 2000, il dispositivo va collegato alla dorsale della rete in prossimità del cavo di alimentazione, per ridurre al minimo la caduta di tensione e garantire un funzionamento affidabile.

### Configurazione hardware

La scheda portante (carrier board) include una resistenza di terminazione da 120 Ω che può essere attivata tramite un jumper. Nelle applicazioni NMEA 2000 la terminazione sul dispositivo va evitata, poiché lo standard non la consente. Nelle applicazioni automobilistiche o industriali con comunicazione punto-punto, invece, il jumper può essere impostato in modo da attivare la resistenza di terminazione.

Per la diagnostica e la risoluzione dei problemi di rete, la scheda portante dispone di LED RX e TX dedicati che segnalano l’attività della rete. Questi LED offrono un riscontro visivo immediato sulla trasmissione e sulla ricezione dei dati, facilitando la diagnosi dei problemi di connettività.

### Installazione in rete

Il collegamento alle reti NMEA 2000 si effettua con un connettore a T standard (non fornito) installato sulla dorsale della rete e con un cavo di derivazione che collega il connettore a T al connettore Micro-C dell’HALPI2.

### Integrazione software

L’interfaccia CAN si integra senza difficoltà con Linux tramite il framework SocketCAN e compare come dispositivo di rete `can0`. Questa interfaccia standard consente di utilizzare le comuni utility CAN di Linux per il monitoraggio e la diagnostica. L’interfaccia di rete è preconfigurata in tutte le immagini del sistema operativo per HALPI2 (HaLOS, OpenPlotter e Raspberry Pi OS).

L’integrazione con il server Signal K è disponibile nelle varianti dell’immagine HaLOS Marine e in OpenPlotter: l’interfaccia CAN viene rilevata e utilizzata automaticamente per l’elaborazione dei dati NMEA 2000. Nelle immagini HaLOS non nautiche, Signal K può essere installato dallo store Container Apps di Cockpit. Il server Signal K si occupa della decodifica dei PGN e fornisce l’accesso web ai dati di rete in tempo reale.

### Risoluzione dei problemi

La risoluzione dei problemi di rete inizia dai LED RX/TX sulla scheda portante. In condizioni normali i LED mostrano un’attività intermittente corrispondente al traffico di rete. L’assenza di attività RX può indicare problemi di cablaggio o una terminazione non corretta, mentre l’assenza di attività TX può segnalare conflitti di rete o problemi di cablaggio.

Il comando Linux `candump` consente di monitorare il bus CAN direttamente dalla riga di comando. Questo strumento fornisce informazioni dettagliate su tutti i messaggi presenti sul bus e permette una diagnostica approfondita. Nella sua forma più semplice si esegue così:

```bash
candump can0
```

In questo modo vengono visualizzati in tempo reale tutti i messaggi CAN grezzi in ingresso.

La dashboard del server Signal K offre ulteriori funzioni di monitoraggio della rete: mostra in tempo reale le velocità dei dati NMEA 2000 provenienti dall’interfaccia CAN. Lo strumento data browser consente di visualizzare i dati NMEA 2000 decodificati.

!!! quote "Informazioni correlate"
    - **Configurazione dell’alimentazione:** consultare [Guida introduttiva](../getting-started/getting-started.md#installazione-permanente-dellalimentazione)
    - **Configurazione software:** consultare [Guida al software](./software.md)
    - **Risoluzione dei problemi di rete:** consultare [Guida alla risoluzione dei problemi](./troubleshooting.md)


## RS-485 (NMEA 0183)

L’HALPI2 include un’interfaccia [RS-485](https://en.wikipedia.org/wiki/RS-485) isolata che fornisce la comunicazione seriale per le reti nautiche [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422] e per le applicazioni industriali.

[^rs422]: Tecnicamente NMEA 0183 utilizza lo standard RS-422, ma RS-485 è compatibile all’indietro, il che consente all’HALPI2 di comunicare sia con dispositivi RS-422 sia con dispositivi RS-485.

### Specifiche dell’interfaccia

Il ricetrasmettitore RS-485 funziona a velocità fino a 10 Mbit/s, anche se le tipiche applicazioni NMEA 0183 utilizzano le velocità standard di 4800 o 38400 bit/s. L’interfaccia è isolata galvanicamente ed è conforme alla specifica NMEA 0183: protegge l’HALPI2 dagli anelli di massa e dai disturbi elettrici comuni negli ambienti nautici.

L’interfaccia è collegata internamente alla UART 4 del Raspberry Pi e compare come `/dev/ttyAMA4` nel sistema operativo Linux. A questo dispositivo seriale standard può accedere qualsiasi applicazione che supporti la comunicazione seriale, compresi il server Signal K, OpenCPN e applicazioni software personalizzate.

### Configurazione hardware

La scheda portante dispone di LED RX e TX dedicati che segnalano l’attività di comunicazione sull’interfaccia RS-485. Questi LED offrono un riscontro visivo immediato durante l’installazione e la risoluzione dei problemi, rendendo semplice verificare che i dati vengano trasmessi e ricevuti correttamente.

Quando funziona come interfaccia RS-485 generica, il dispositivo può essere configurato in modalità di abilitazione della trasmissione automatica oppure manuale. Nella modalità manuale un pin GPIO controlla il segnale di abilitazione della trasmissione, consentendo al software di gestire quando l’interfaccia è in trasmissione o in ricezione. Questo è necessario nelle applicazioni multi-talker, in cui l’interfaccia deve trovarsi in stato recessivo quando non trasmette. La modalità automatica lascia che sia l’hardware ad attivare il segnale di abilitazione della trasmissione all’invio dei dati, semplificando la configurazione nelle applicazioni single-talker.

Inoltre, l’interfaccia RS-485 supporta una modalità half-duplex, che le consente di trasmettere e ricevere sulla stessa coppia di conduttori.

L’interfaccia può anche essere disattivata completamente tramite la configurazione hardware, se la UART 4 serve per altri scopi.

### Cablaggio e collegamenti

L’interfaccia RS-485 richiede un pressacavo o un connettore da pannello, che deve essere fornito dall’utente. Una buona soluzione è [un connettore da pannello SP13 con pigtail](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). L’interfaccia è compatibile all’indietro con la segnalazione RS-422 utilizzata in NMEA 0183 e supporta sia le reti multi-talker RS-485 sia le reti RS-422 con un solo talker e più listener. Utilizza coppie differenziali bilanciate, contrassegnate TX+/TX- e RX+/RX-.

### Integrazione software

Tutte le immagini per HALPI2 sono preconfigurate con l’interfaccia RS-485 pronta all’uso. Nelle immagini HaLOS Marine e in OpenPlotter il server Signal K rileva automaticamente l’interfaccia e riceve i dati NMEA 0183 trasmessi.

Per le applicazioni personalizzate, l’interfaccia si comporta come una normale porta seriale Linux. Le applicazioni possono aprire `/dev/ttyAMA4` e impostare velocità in baud, bit di dati, bit di stop e parità secondo quanto richiesto dall’apparecchiatura collegata. Le applicazioni Python, Node.js e C/C++ possono accedere facilmente all’interfaccia utilizzando le librerie standard per la comunicazione seriale.

### Applicazioni comuni

Negli ambienti nautici l’interfaccia RS-485 viene collegata tipicamente a ricevitori GPS, ecoscandagli, strumenti del vento, transponder AIS o altri dispositivi che utilizzano il protocollo NMEA 0183. Le applicazioni industriali possono comprendere il collegamento a PLC, sensori e altre apparecchiature di automazione che utilizzano Modbus RTU o altri protocolli RS-485.

L’elevata velocità dell’interfaccia supporta anche applicazioni non standard, come la raccolta di dati da sensori ad alta frequenza o protocolli di comunicazione personalizzati, rendendo l’HALPI2 adatto alle navi da ricerca e alle applicazioni di monitoraggio specializzate.

!!! quote "Informazioni correlate"
    - **Configurazione software:** consultare [Guida al software](./software.md)
    - **Risoluzione dei problemi:** consultare [Guida alla risoluzione dei problemi](./troubleshooting.md)


## GNSS (GPS)

L’HALPI2 supporta gli HAT con ricevitore GNSS collegati alla UART0 (`/dev/ttyAMA0`). Qualsiasi ricevitore GNSS su questa porta funziona con gpsd senza alcuna configurazione.

Per i ricevitori u-blox (come il Max-M8Q), le immagini HaLOS Marine offrono inoltre una configurazione automatica ottimizzata per l’uso nautico.

### Configurazione automatica (ricevitori u-blox)

Nelle immagini HaLOS Marine un servizio systemd (`configure-ublox-marine`) rileva e configura automaticamente i ricevitori u-blox a ogni avvio:

| Parametro | Valore |
|:----------|:------|
| Velocità in baud | 115200 bit/s (impostazione di fabbrica: 9600) |
| Frequenza di aggiornamento | 10 Hz (100 ms) |
| Modello dinamico | Sea (ottimizzato per l’uso nautico) |

La configurazione viene eseguita a ogni avvio perché i moduli u-blox basati su ROM (come il MAX-M8Q) non dispongono di memoria flash. Le impostazioni vengono salvate nella Battery-Backed RAM (BBR), che può essere persa quando l’alimentazione della batteria tampone viene interrotta, ad esempio se il dispositivo resta senza alimentazione per un periodo prolungato. La riconfigurazione è trasparente e aggiunge circa 2 secondi all’avvio di gpsd.

Se non viene rilevato alcun ricevitore, il servizio termina senza segnalazioni. Un HAT GNSS appena installato viene configurato automaticamente al riavvio successivo.

### Accesso ai dati

I dati GPS sono forniti da [gpsd](https://gpsd.io/) sulla porta TCP 2947. Nelle immagini HaLOS Marine, Signal K si collega automaticamente a gpsd: non è necessaria alcuna configurazione aggiuntiva.

Per la diagnostica, utilizzare i normali strumenti da riga di comando di gpsd:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Immagini non HaLOS

Su Raspberry Pi OS o su altri sistemi operativi, installare e configurare gpsd manualmente:

```bash
sudo apt install gpsd gpsd-clients
```

Modificare `/etc/default/gpsd` impostando `DEVICES="/dev/ttyAMA0"` e riavviare il servizio. Il ricevitore funzionerà con le impostazioni di fabbrica (9600 baud, 1 Hz), a meno che non venga configurato con `ubxtool` del pacchetto `gpsd-clients`.

!!! quote "Informazioni correlate"
    - **gpsd su HaLOS:** consultare la [documentazione GPS di HaLOS](https://docs.halos.fi/user-guide/gps/)
    - **Configurazione software:** consultare [Guida al software](./software.md)


## Ethernet

L’HALPI2 include un’interfaccia Gigabit Ethernet che offre connettività di rete ad alta velocità per il trasferimento dei dati, l’accesso remoto e l’integrazione con le reti di bordo. La porta Ethernet sulla scheda portante è un connettore RJ45 standard, portato su un connettore da pannello a cui è possibile collegare un cavo Ethernet esterno.

## USB

L’HALPI2 dispone di quattro porte USB 3.0 Type A integrate, che offrono connettività ad alta velocità per periferiche e dispositivi di vario tipo. Una porta è collegata direttamente all’interfaccia USB 3.0 del CM5, mentre le altre tre passano attraverso un hub USB 3 integrato. Nella configurazione standard due porte sono portate sul pannello frontale, mentre due restano disponibili sulla scheda portante per i collegamenti interni.

## HDMI

L’HALPI2 include due porte HDMI 2.0 (HDMI0 e HDMI1) per l’uscita video. La scheda portante mette a disposizione connettori per cavo piatto flessibile (FFC) per entrambe le porte HDMI, portate sul pannello frontale mediante cavi FFC personalizzati. I connettori del pannello frontale sono normali connettori HDMI Type A.

L’uscita HDMI dell’HALPI2 supporta in modo affidabile due flussi video Full HD (1080p). L’uscita video 4K può funzionare, ma non è garantita.

## MIPI (CSI/DSI)

La scheda portante include due connettori MIPI CSI/DSI per le interfacce di fotocamere e display. Si tratta di connettori FFC (cavo piatto flessibile) a 22 pin con passo 0,5 mm. Dovrebbero funzionare senza modifiche con le fotocamere e i display compatibili Raspberry Pi più recenti.

Per motivi di impermeabilità, l’uso dei cavi FFC va limitato ai soli collegamenti interni.

## Pulsanti esterni

L’HALPI2 mette a disposizione sulla scheda portante un connettore a pettine 2×3 pin per il collegamento di pulsanti esterni. La custodia non include pulsanti integrati: la posizione e il tipo dei pulsanti possono quindi essere personalizzati in base alle esigenze specifiche.

### Piedinatura del connettore dei pulsanti

La scheda portante include un connettore a pettine a 6 pin con tre funzioni di pulsante etichettate:

| Etichetta | Funzione | Descrizione |
|:------|:---------|:------------|
| Reset | Reset del controller | Reset hardware (pin RUN dell’RP2040) |
| Power | Accensione del Raspberry Pi | Pulsante di accensione del CM5 (ingresso PWR_BUT) |
| User | Configurabile dall’utente | Evento definito dall’utente (non ancora implementato) |

Ogni collegamento di pulsante utilizza due pin: uno per il segnale del pulsante e uno per la massa. Utilizzare interruttori momentanei normalmente aperti (NO) che collegano il pin di segnale alla massa quando vengono premuti.

### Funzioni dei pulsanti

**Pulsante Reset:**
Il pulsante di reset esegue un reset del sistema a livello hardware portando a massa il pin RUN dell’RP2040. Questa azione provoca un reset completo del sistema, che coinvolge il controller, il CM5 e tutte le periferiche collegate. Il pulsante di reset è particolarmente utile nelle situazioni di ripristino di emergenza, quando le procedure di spegnimento via software non hanno funzionato e il sistema non risponde più.

**Pulsante Power:**
Il pulsante di accensione è collegato direttamente all’ingresso del pulsante di accensione del CM5 e funziona esattamente come il pulsante di accensione del Raspberry Pi 5. Un doppio clic richiede uno spegnimento controllato del sistema, che consente al sistema operativo di chiudere correttamente le applicazioni e di smontare i file system prima dello spegnimento. Una pressione prolungata forza lo spegnimento immediato e va utilizzata solo quando il sistema non risponde.

**Pulsante User:**
La funzionalità del pulsante utente è attualmente in attesa di implementazione software e offrirà funzioni configurabili dall’utente nelle future versioni del firmware. Una volta implementato, questo pulsante sarà destinato ad azioni personalizzate e a trigger specifici per applicazione, permettendo di definire comportamenti dei pulsanti su misura per le esigenze operative specifiche.

### Installazione dei pulsanti

#### Montaggio diretto sulla custodia

Per il montaggio diretto sulla custodia dell’HALPI2, utilizzare i fori da 6 mm o 13 mm già previsti nel progetto della custodia. Rimuovere innanzitutto i tappi ciechi corrispondenti e installare un gruppo pulsante impermeabile del diametro adatto al foro. Collegare il pulsante al connettore a pettine della scheda portante con un cavo adeguato, curando lo scarico della trazione e la tenuta agli agenti atmosferici nel punto di attraversamento della custodia.

#### Montaggio su pannello esterno

Quando i pulsanti vengono montati su un pannello di comando remoto, scegliere una posizione che offra un accesso comodo mantenendo la tenuta agli agenti atmosferici. Utilizzare pressacavi per i punti di ingresso dei cavi e collegare i pulsanti con una prolunga a conduttori da 22–26 AWG, mantenendo la lunghezza totale del cavo entro 3 metri per preservare l’integrità del segnale. Nelle installazioni esposte all’umidità o ad ambienti gravosi, impiegare connettori impermeabili nei punti di giunzione, per garantire un funzionamento affidabile nel tempo.

#### Collegamento

Tutti i collegamenti dei pulsanti alla scheda portante devono utilizzare connettori femmina a pettine con passo 2,54 mm. Verificare il corretto allineamento dei pin e la solidità del collegamento, per evitare problemi di contatto durante il funzionamento.

!!! quote "Informazioni correlate"
    - **Gestione dell’alimentazione:** consultare [Gestione dell’alimentazione e procedure di spegnimento](./operation.md#gestione-dellalimentazione-e-procedure-di-spegnimento)
    - **Accesso all’hardware:** consultare [Manutenzione dell’hardware](./hardware.md)

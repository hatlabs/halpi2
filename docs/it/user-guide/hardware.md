---
translated_from: 9741366021074655d667fcf3a93a634f86f3519a
---

# Guida all’hardware

## Accesso alla custodia

L’HALPI2 è dotato di una custodia in alluminio pressofuso verniciato a polvere, con fori predisposti per i connettori del pannello. Quando sono necessarie modifiche interne o interventi di manutenzione, si può accedere alla custodia seguendo le procedure descritte di seguito.

### Apertura della custodia

Per accedere ai componenti interni, verificare innanzitutto che l’unità sia completamente spenta e che i cavi di alimentazione siano scollegati. Il coperchio è fissato con quattro viti svasate M4×10 con testa PH2. Rimuovere queste viti con un cacciavite PH2 e togliere il coperchio.

### Rimontaggio

Prima di rimontare la custodia, verificare con calma che tutti i collegamenti interni siano saldi e correttamente inseriti. Disporre i cavi con attenzione per evitare schiacciamenti o pieghe troppo strette.

È facile collegare per errore i cavi piatti flessibili (FFC) al contrario. Osservare le frecce “Contacts” sulla serigrafia per verificare il corretto orientamento.

Prestare particolare attenzione alla guarnizione del coperchio, controllando che non presenti danni, residui o spostamenti che possano compromettere la tenuta della custodia.

Rimontare le quattro viti M4×10 del coperchio con il cacciavite PH2. Non serrare eccessivamente.


## Connettori del pannello

### Configurazione standard

HALPI2 viene fornito con una configurazione di connettori standard adatta alla maggior parte delle applicazioni. La disposizione predefinita comprende:

- **Connettore di alimentazione E7T**
- **Connettore NMEA 2000 micro**
- **Gigabit Ethernet RJ45**
- **Uscita HDMI**
- **2× USB 3.0 Type-A**
- **3× posizioni per pressacavo PG7** (con tappi ciechi)
- **2× posizioni per antenna RP-SMA** (con tappi ciechi)
- **Tappo di compensazione** per l’equalizzazione della pressione

![Connettori e tappi ciechi del pannello frontale](./front-panel-connectors-all.jpg)
*Connettori e tappi ciechi del pannello frontale. I connettori contrassegnati in verde fanno parte della configurazione standard. Le posizioni in giallo sono tappi ciechi che possono essere sostituiti con connettori secondo necessità. La posizione in rosso è il tappo di compensazione, che non deve essere rimosso.*

### Opzioni di connettori personalizzate

Se servono tipi di connettori diversi, è possibile modificare la configurazione del pannello:

#### Rimozione dei connettori

!!! warning "Importante"
    Modificare i connettori solo quando l’unità è spenta e scollegata da tutte le sorgenti.

    Le filettature in plastica possono danneggiarsi con un serraggio eccessivo. Usare normali chiavi a bussola esagonali, serrando però solo a mano.

1. **Usare la chiave a bussola della misura corretta:**
    - Connettori grandi: chiave a bussola da 26 mm
    - Bulloni in nylon M6: chiave a bussola da 10 mm
    - Connettori RP-SMA: chiave a bussola da 8 mm
    - Posizioni PG7: cacciavite a taglio grande, chiave a bussola da 17 mm

2. **Rimuovere con attenzione**: le filettature in plastica possono danneggiarsi con un serraggio eccessivo

3. **Conservare le parti rimosse** per un eventuale uso futuro

#### Installazione di nuovi connettori

1. **Usare esclusivamente connettori per uso nautico** o con grado di protezione adeguato all’ambiente
2. **Garantire una tenuta corretta**: è necessaria una flangia larga sul lato interno
3. **Serrare solo a mano**: non forzare le filettature in plastica
4. **Provare l’accoppiamento** prima dell’installazione definitiva

## Disposizione interna

- La scheda portante (carrier board) dell’HALPI2 è la scheda principale del computer: ospita il Compute Module 5 (CM5) sul lato inferiore e fornisce la gestione dell’alimentazione, le indicazioni luminose e i collegamenti per tutte le interfacce.

### Aree funzionali della scheda portante

Le principali aree funzionali della scheda portante sono illustrate nell’immagine seguente.

![Disposizione della scheda portante, lato superiore](./carrier-board-top-layout.jpg)
*Disposizione del lato superiore della scheda portante, con le principali aree funzionali.*

### Connettori della scheda portante

Le funzionalità sono accessibili attraverso una serie di connettori presenti sulla scheda, mostrati nell’immagine seguente.

![Connettori della scheda portante, lato superiore](./carrier-board-top-conx.jpg)
*Connettori della scheda portante, lato superiore.*

Di seguito è riportato l’elenco dei connettori del lato superiore.

| Etichetta | Descrizione |
|:------|:------------|
| **a1** | Connettore di alimentazione (tipo Phoenix MC, passo 3,81 mm) |
| **a2** | Limitatore di corrente di ingresso (0,9 A o 2,5 A) |
| **a3** | Jumper di controllo dell’alimentazione. Cortocircuitare i pin “3.3V off” per forzare lo spegnimento della linea da 3,3 V. Cortocircuitare i pin “5V on” per forzare l’accensione della linea da 5 V. **NB:** sulle schede versione 0.4.0 i connettori **a3** e **c2** sono disposti diversamente. |
| **b1** | Porta Ethernet (RJ45) |
| **c1** | Porta USB del controller. Utilizzata per flashare il firmware del microcontrollore RP2040. |
| **c2** | Connettore a pettine del jumper USB BOOT dell’MCU. Cortocircuitare i pin per mettere l’RP2040 in modalità USB boot. |
| **c3** | Connettore a pettine per il debug del controller |
| **c4** | Connettore a pettine GPIO del controller, non popolato |
| **c5** | Connettori a pettine dei pulsanti. Utilizzati per collegare i pulsanti Power, Reset e User. |
| **c6** | Pulsante di accensione. Utilizzato per accendere e spegnere il Compute Module 5. |
| **d1** | Connettore GPIO a 40 pin del Raspberry Pi |
| **e1** | Connettore MIPI0 per interfaccia camera o display |
| **e2** | Connettore MIPI1 per interfaccia camera o display |
| **f1** | Connettore HDMI0 |
| **f2** | Connettore HDMI1 |
| **g1** | Connettore per unità SSD NVMe M.2 |
| **h1** | Interfaccia CAN FD (tipo Phoenix MC, passo 3,81 mm) |
| **h2** | Jumper di terminazione CAN. Cortocircuitare i pin per attivare la resistenza di terminazione del bus CAN FD. |
| **i1** | Interfaccia RS-485 (tipo Phoenix MC, passo 3,81 mm) |
| **i2** | Jumper di abilitazione automatica/manuale RS-485. |
| **i4** | Jumper XRS-485 RX Enable. Cortocircuitare i pin per abilitare la ricezione del traffico RS-485. |
| **j1** | Connettore USB Boot del Compute Module. Utilizzato per flashare il firmware del Compute Module 5. |
| **j2** | Selettore della modalità di avvio del Compute Module. Impostare su “Normal” per il funzionamento normale e su “Abnormal” per la modalità USB boot. Quando il selettore è su “Abnormal” si accende un LED di avviso. |
| **m1** | Connettore USB3 0. Collegato direttamente al CM5. |
| **m2** | Connettore USB3 1-0. Collegato all’hub USB3 integrato. |
| **m3** | Connettore USB3 1-1. Collegato all’hub USB3 integrato. |
| **m4** | Connettore USB3 1-2. Collegato all’hub USB3 integrato. |
| **n1** | Portabatteria CR2032 per l’orologio in tempo reale (RTC) |
| **q1** | Connettore della ventola del CM5. La ventola può essere utilizzata per migliorare la circolazione dell’aria all’interno della custodia. Non è necessaria quando si utilizza la custodia standard. |

![Connettori della scheda portante, lato inferiore](./carrier-board-bottom-conx.jpg)
*Connettori della scheda portante, lato inferiore.*

Di seguito è riportato l’elenco dei connettori del lato inferiore.

| Etichetta | Descrizione |
|:------|:------------|
| **p1** | Connettore del Compute Module 5. |
| **q1** | Connettore della ventola del CM5, posizione alternativa. Questo connettore a pettine può essere utilizzato per collegare una ventola per la CPU sopra il modulo CM5 quando si usa una custodia personalizzata. **NB:** i connettori **q1** e **q2** sono collegati in parallelo e non devono essere utilizzati contemporaneamente. |

Infine, il connettore dell’antenna WiFi e Bluetooth si trova sul Compute Module 5 stesso ed è mostrato nell’immagine seguente.

![Connettore dell’antenna WiFi](./cm5-top-conx.jpg)
*Connettore per antenna U.FL sul Compute Module 5.*

| Etichetta | Descrizione |
|:------|:------------|
| **r1** | Connettore U.FL per l’antenna WiFi e Bluetooth. |

### Blinkenlights

La scheda portante è dotata di diversi LED di stato per il monitoraggio del sistema.

![LED di stato della scheda portante](./carrier-board-top-leds.jpg)
*LED di stato della scheda portante e relativi colori.*

I LED di stato forniscono informazioni sullo stato di alimentazione e di attività del sistema. Di seguito è riportato l’elenco dei LED di stato.

| Etichetta | Colore | Descrizione |
|-------|:-------|:------------|
| **1** | RGB   | Cinque LED RGB. Questi LED indicano lo stato e l’attività del sistema sul pannello frontale. |
| **2** | Rosso   | LED di alimentazione per le linee da 3,3 V e 5 V. Indicano lo stato di alimentazione delle rispettive linee di tensione. |
| **3** | Giallo| Indicatore di velocità Ethernet. Acceso quando la porta Ethernet ha negoziato un collegamento a 100/1000 Mbps. |
| **4** | Verde | Indicatore di attività Ethernet. Lampeggia in presenza di traffico di rete sulla porta Ethernet. |
| **5** | Blu | Indicatore di attività dell’unità SSD. Lampeggia in presenza di attività di lettura o scrittura sull’unità SSD NVMe M.2. |
| **6** | Rosso | Indicatore di stato di alimentazione del Pi. Acceso quando il sistema è alimentato ma spento. |
| **7** | Verde | Indicatore di attività del Pi. Lampeggia in presenza di attività sul Raspberry Pi. |
| **8** | Ambra | Avviso di modalità di avvio anomala. Acceso quando il selettore della modalità USB boot è su “Abnormal”. Indica che il dispositivo è impostato per essere flashato tramite il connettore USB Boot e non si avvierà normalmente. |
| **9** | Verde | LED TX/RX del CAN. Lampeggiano quando i dati vengono ricevuti (RX) o trasmessi (TX) sull’interfaccia CAN. |
| **10** | Verde | LED TX/RX dell’RS-485. Lampeggiano quando i dati vengono ricevuti (RX) o trasmessi (TX) sull’interfaccia RS-485. |

Gli schemi di illuminazione dei LED RGB sono documentati nella [Guida al funzionamento](./operation.md#indicatori-led-di-stato).

## Configurazione della limitazione di corrente

La scheda portante è dotata di un limitatore di corrente che permette di configurare la corrente massima fornita alle periferiche. Per individuarlo, fare riferimento alla posizione contrassegnata **a2** nell’immagine della sezione [Connettori della scheda portante](#connettori-della-scheda-portante).

!!! info "Impostazioni del limite di corrente"
    **Impostazione 0,9 A (predefinita):**

    - Obbligatoria per l’alimentazione dal bus NMEA 2000
    - Adatta al funzionamento di base

    **Impostazione 2,5 A:**

    - Per periferiche ad alto assorbimento
    - Ricarica più rapida dei supercondensatori
    - Solo con alimentazione dedicata

Per modificare l’impostazione del limite di corrente, spegnere prima completamente l’HALPI2 e rimuovere il coperchio della custodia seguendo la procedura descritta nella sezione Accesso alla custodia. Individuare il limitatore di corrente sulla scheda portante e spostarlo nella posizione desiderata (0,9 A oppure 2,5 A). Una volta modificata l’impostazione, rimontare la custodia verificando che tutti i collegamenti rimangano saldi.

## Uso degli HAT

### Compatibilità con gli HAT

HALPI2 supporta gli HAT standard per Raspberry Pi tramite il connettore GPIO a 40 pin, mantenendo la piena compatibilità elettrica e meccanica con la specifica HAT del Raspberry Pi. La scheda portante offre la stessa piedinatura GPIO di un Raspberry Pi standard, permettendo alla maggior parte degli HAT progettati per Raspberry Pi 4 e 5 di funzionare senza modifiche. Questa compatibilità riguarda sia gli HAT ufficiali Raspberry Pi sia le schede di espansione di terze parti conformi allo standard HAT.

### Vincoli fisici

La custodia dell’HALPI2 offre 45 mm di spazio verticale sopra la scheda portante, sufficienti per ospitare fino a due HAT impilati. L’area a sinistra dell’area di installazione degli HAT delimitata dal contorno è occupata dai supercondensatori, il che limita lo spazio disponibile per gli HAT che superano l’ingombro standard di 65 × 56 mm. Prestare particolare attenzione agli HAT con connettori laterali. I connettori rivolti verso “south” o “east” non dovrebbero creare problemi, mentre quelli rivolti verso “west” possono interferire con i supercondensatori.

### Conflitti sui pin GPIO

Diversi pin GPIO sono utilizzati dalle interfacce integrate dell’HALPI2 e vanno considerati nella scelta degli HAT compatibili. La tabella seguente riporta i pin GPIO riservati e le relative funzioni:

| Numero GPIO | Funzione | Interfaccia | Note |
|----------|----------|-----------|-------|
| GPIO 2 | I2C SDA | I2C di sistema | Condivisibile; indirizzo 0x6d riservato |
| GPIO 3 | I2C SCL | I2C di sistema | Condivisibile; indirizzo 0x6d riservato |
| GPIO 6 | SPI CS | CAN FD | Chip select personalizzato per il controller CAN |
| GPIO 9 | SPI MISO | CAN FD | Bus SPI0 condiviso |
| GPIO 10 | SPI MOSI | CAN FD | Bus SPI0 condiviso |
| GPIO 11 | SPI SCK | CAN FD | Bus SPI0 condiviso |
| GPIO 12 | UART TX | RS-485 | Trasmissione UART4 |
| GPIO 13 | UART RX | RS-485 | Ricezione UART4 |
| GPIO 24 | RS-485 EN | RS-485 | Segnale di abilitazione (solo in modalità manuale) |
| GPIO 26 | CAN INT | CAN FD | Linea di interrupt per il controller CAN |

### Condivisione delle interfacce e conflitti

Il bus I2C sui GPIO 2 e 3 può essere condiviso con dispositivi HAT, poiché l’I2C supporta più dispositivi sullo stesso bus. Gli HAT non devono però utilizzare l’indirizzo I2C 0x6d, riservato al controller di sistema dell’HALPI2. La maggior parte degli HAT I2C funziona senza problemi, ma è opportuno verificare gli indirizzi I2C utilizzati prima dell’installazione.

Il bus SPI0 usato per l’interfaccia CAN FD può essere condiviso con altri dispositivi SPI, poiché HALPI2 utilizza pin di chip select (GPIO 6) e di interrupt (GPIO 26) personalizzati. Gli HAT che usano SPI0 con i pin di chip select standard (GPIO 7 o GPIO 8) possono coesistere con l’interfaccia CAN, ma possono richiedere una configurazione aggiuntiva tramite device tree overlay.

### Disattivazione delle interfacce integrate

Se un HAT richiede l’uso esclusivo di pin occupati dalle interfacce integrate dell’HALPI2, tali interfacce possono essere disattivate con modifiche hardware. L’interfaccia CAN FD può essere liberata completamente rimuovendo il jumper a saldare GPIO6-CAN.CS situato sul lato inferiore della scheda portante. Questa modifica scollega il controller CAN dal bus SPI e libera i GPIO 6, 9, 10, 11 e 26 per l’uso da parte dell’HAT.

L’interfaccia RS-485 può essere disattivata rimuovendo il jumper RX Enable (i4) sulla scheda portante. In questo modo il transceiver RS-485 non riceve più dati e i GPIO 12 e 13 restano liberi per altri usi. Se non serve il controllo manuale dell’abilitazione alla trasmissione, anche il GPIO 24 può essere riutilizzato impostando in modalità automatica il jumper di abilitazione automatica/manuale RS-485 (i2).

### Procedura di installazione

Iniziare spegnendo il sistema e scollegando tutte le fonti di alimentazione. Rimuovere il coperchio della custodia seguendo la procedura descritta nella sezione Accesso alla custodia.

Le schede portanti dalla versione 0.5.0 in poi hanno inserti filettati M2,5 già installati nelle quattro posizioni di montaggio degli HAT, il che semplifica l’installazione. Le schede precedenti v0.4.0 richiedono l’installazione manuale di dadi M2,5. Per installare i dadi occorre rimuovere temporaneamente la scheda portante. È possibile farlo senza scollegare tutti i cavi.

Per molti HAT diffusi sono adatti distanziali da 15 mm, ma è bene misurare l’altezza del connettore femmina dell’HAT per garantire lo spazio corretto. La base del connettore maschio è alta 2,5 mm: sommare questo valore all’altezza del connettore femmina per determinare la lunghezza necessaria del distanziale.

Avvitare i distanziali nei fori di montaggio oppure, sulle schede v0.4.0, fissarli con dadi dal basso. Allineare l’HAT al connettore GPIO a 40 pin, verificando che tutti i pin siano nella posizione corretta prima di applicare una pressione uniforme per innestare il connettore. L’HAT deve risultare parallelo alla scheda portante, senza spazi visibili in corrispondenza del collegamento GPIO.

Fissare l’HAT con viti M2,5 o con ulteriori distanziali, facendoli passare attraverso i fori di montaggio dell’HAT fino ai distanziali sottostanti. Queste viti non sono incluse con HALPI2 e devono essere procurate separatamente. Serrare le viti quanto basta per fissare l’HAT senza flettere il circuito stampato.

### Gestione dei cavi

Se l’HAT dispone di connettori esterni che devono essere raggiungibili dall’esterno della custodia, valutare l’installazione di connettori da pannello adeguati nelle posizioni disponibili per i pressacavi PG7. In questo modo si mantiene la protezione ambientale della custodia garantendo al tempo stesso un comodo accesso dall’esterno.

### Procedura di rimozione

La rimozione dell’HAT segue la procedura di installazione in ordine inverso. Spegnere completamente il sistema e scollegare tutte le fonti di alimentazione prima di aprire la custodia. Rimuovere le viti di montaggio M2,5 e sollevare con cautela l’HAT dal connettore GPIO tirandolo dritto verso l’alto, evitando qualsiasi forza laterale che potrebbe piegare i pin del connettore.

Se l’HAT sembra bloccato, controllare che non siano rimaste viti o cavi prima di applicare ulteriore forza. Alcuni HAT con connettori molto aderenti possono richiedere un leggero movimento oscillante durante l’estrazione. Oscillare l’HAT in direzione nord-sud: oscillarlo in direzione est-ovest rischia di piegare i pin del connettore quando questo si sgancia improvvisamente.

### Configurazione software

Dopo l’installazione hardware, l’HAT può richiedere una configurazione software per funzionare correttamente. Molti HAT includono device tree overlay che devono essere abilitati nella configurazione del Raspberry Pi. Modificare `/boot/firmware/config.txt` aggiungendo le righe `dtoverlay` indicate nella documentazione dell’HAT.

!!! quote "Informazioni correlate"
    - **Riferimento della piedinatura GPIO:** vedere [Riferimento hardware](../technical-reference/hardware.md)
    - **Configurazione software:** vedere [Configurazione avanzata](../software-development/advanced-config.md)
    - **Modifiche alla custodia:** vedere [Opzioni di connettori personalizzate](#opzioni-di-connettori-personalizzate)

## Sostituzione dell’unità SSD NVMe

### Compatibilità delle unità SSD

HALPI2 supporta unità SSD NVMe M.2 2230–2280 nella configurazione standard a singola faccia. Le unità 2230, più corte, possono essere a doppia faccia grazie allo spazio aggiuntivo disponibile in quella posizione di montaggio, mentre le unità più lunghe devono essere a singola faccia per poter essere alloggiate sulla scheda portante.

La compatibilità può essere garantita solo con le unità SSD fornite da Hat Labs e con le unità SSD ufficiali Raspberry Pi. Se si valuta un’unità di terze parti, verificarne la compatibilità con Raspberry Pi 5 prima dell’acquisto, consultando le segnalazioni degli utenti e gli elenchi di compatibilità disponibili online. I problemi più comuni con le unità non compatibili sono un consumo eccessivo, il surriscaldamento, gli errori di avvio e l’instabilità del sistema.

### Preparazione della nuova unità SSD

Prima di installare una nuova unità SSD nell’HALPI2, occorre scrivere il sistema operativo sull’unità. Sebbene sia possibile farlo dopo l’installazione tramite il connettore USB Boot del CM5 (j1), l’uso di un adattatore esterno da USB a NVMe è più semplice e rapido. La procedura di scrittura è descritta nella [Guida al software](./software.md).

### Disattivazione della tensione di sistema da 3,3 V

I supercondensatori possono mantenere alimentata la linea da 3,3 V della scheda portante per un tempo considerevole dopo lo scollegamento dell’alimentazione principale. Poiché l’unità SSD è alimentata dalla linea da 3,3 V, questa deve essere disattivata per garantire che l’unità sia completamente priva di alimentazione prima della rimozione o dell’installazione.

Iniziare spegnendo l’HALPI2 e scollegando l’alimentazione. Aprire la custodia seguendo la procedura descritta nella sezione Accesso alla custodia.

Individuare il jumper “3.3V off” sulla scheda portante. La posizione varia in base alla versione della scheda. Sulle schede v0.4.0 il jumper si trova molto vicino ai supercondensatori, sul loro lato “south”. Sulle schede v0.5.0 e successive, individuare il connettore a pettine “Pow.Ctrl” sul lato “east” dei supercondensatori. I pin “3.3V off” sono i due più in alto del connettore.

Spostare il jumper in modo da cortocircuitare i pin “3.3V off”. In questo modo la linea da 3,3 V viene disattivata, come segnalato dallo spegnimento dei LED.

### Procedura di rimozione

Lo slot M.2 si trova sul bordo sud della scheda portante. Fare riferimento all’immagine nella sezione [Connettori della scheda portante](#connettori-della-scheda-portante) per individuare il connettore M.2 contrassegnato **g1**.

Con un cacciavite PH1, rimuovere la vite di fissaggio M2,5. Una volta rimossa la vite, l’unità SSD si solleva formando un angolo. Sollevare delicatamente l’unità dal lato di fissaggio ed estrarla dal connettore M.2 con un leggero movimento oscillante. Maneggiare l’unità SSD dai bordi per evitare di danneggiare componenti o connettori.

### Procedura di installazione

Inserire l’unità SSD preparata nel connettore M.2 con un’inclinazione di circa 30 gradi, verificando che la tacca dell’unità sia allineata alla chiave del connettore. L’unità deve scorrere senza sforzo. Una volta inserita completamente, premere verso il basso il lato di fissaggio dell’unità finché non appoggia in piano sul distanziale.

Fissare l’unità SSD con la vite di fissaggio M2,5 usando un cacciavite PH1. Serrare la vite quanto basta per tenere l’unità saldamente in posizione. L’unità SSD deve risultare perfettamente piana, senza pieghe o flessioni visibili.

Una volta installata l’unità SSD, rimuovere il jumper dai pin “3.3V off” per riattivare la linea da 3,3 V. Conservare il jumper sul connettore a pettine per usi futuri.

Rimontare la custodia come descritto nella sezione Accesso alla custodia.
Per la configurazione software o la risoluzione dei problemi, fare riferimento alla [Guida al software](./software.md).

!!! quote "Informazioni correlate"
    - **Immagini di sistema:** vedere [Guida al software](./software.md)
    - **Procedure di avvio:** vedere [Funzionamento del sistema](./operation.md)
    - **Accesso all’hardware:** vedere [Accesso alla custodia](#accesso-alla-custodia)

## Sostituzione del Compute Module 5

### Prerequisiti

La sostituzione del Compute Module 5 richiede una manipolazione attenta, data la delicatezza dei connettori scheda-scheda. Il CM5 utilizza due connettori ad alta densità che possono danneggiarsi facilmente in caso di forza eccessiva o di tecnica scorretta. Rimuovere un modulo esistente solo se strettamente necessario, ad esempio quando il modulo è danneggiato o deve essere sostituito con uno più recente. I danni ai connettori di montaggio del compute module, sul CM5 o sulla scheda portante, non sono coperti da garanzia.

Prima di iniziare, procurarsi i pad termici necessari al trasferimento del calore. La configurazione standard prevede un pad da 1 mm di spessore sul SoC e pad da 2 mm di spessore sul chip RP1 e sui componenti dell’alimentazione interna. I pad termici esistenti possono essere riutilizzati se sono integri e puliti.

### Accesso al Compute Module

Spegnere l’HALPI2 e scollegare la fonte di alimentazione. Rimuovere il coperchio della custodia seguendo la procedura descritta nella sezione Accesso alla custodia. Per accedere al CM5, montato sul lato inferiore della scheda portante, occorre prima rimuovere la scheda portante dalla custodia. Per tenere traccia dei numerosi cavi collegati alla scheda portante, è consigliabile scattare qualche foto dei collegamenti prima di procedere.

Scollegare i cavi che impediscono di sollevare la scheda portante. Rimuovere le viti di fissaggio della scheda portante e sollevare la scheda dalla custodia.

### Rimozione del modulo esistente

!!! danger "Attenzione"
    Se il modulo CM5 viene scollegato un connettore alla volta, le forze di torsione possono strappare il connettore dal modulo CM5. Questo danno non è coperto da garanzia.

Il CM5 è fissato da due connettori scheda-scheda che richiedono una manipolazione attenta. Non usare mai utensili metallici per questa procedura: possono danneggiare i connettori o i componenti a montaggio superficiale vicini. Usare uno spudger in legno o plastica, un plettro da chitarra o un utensile non conduttivo simile.

Posizionare l’utensile al centro del bordo corto di sinistra del modulo CM5, tra il modulo e la scheda portante. Premere con decisione sugli angoli del lato destro. Fare leva delicatamente verso l’alto con il minimo sforzo: il modulo dovrebbe sganciarsi con un leggero clic e i due connettori dovrebbero staccarsi contemporaneamente.

![Rimozione del modulo CM5](./unmount-cm5.jpg)
*Rimuovere il modulo CM5 premendo sugli angoli del bordo destro e facendo leva verso l’alto al centro del bordo sinistro. I due connettori devono staccarsi contemporaneamente.*

### Installazione del nuovo modulo

Allineare il nuovo modulo CM5 ai connettori della scheda portante, usando come guida il contorno serigrafato sulla scheda portante. Il contorno del modulo stampato sulla scheda portante deve corrispondere esattamente alle dimensioni fisiche del CM5 quando l’orientamento è corretto.

Una volta allineato, applicare una pressione delicata e uniforme in corrispondenza dei connettori su entrambi i bordi corti del modulo. Si deve avvertire un leggero clic quando i connettori si innestano. Premere con decisione evitando però di flettere la scheda portante: se necessario, sostenerla da sotto. Entrambi i connettori devono essere completamente inseriti per un funzionamento corretto.

A questo punto, applicare i pad termici sul modulo CM5. I pad termici devono essere posizionati correttamente: pad da 1 mm sul SoC principale e pad da 2 mm sul chip RP1 e sui componenti dell’alimentazione. Se si riutilizzano pad esistenti, verificare che siano puliti e posizionati correttamente.

![Posizionamento dei pad termici sul CM5](./cm5-thermal-pads-annotated.jpg)
*Posizionamento dei pad termici sul Compute Module 5. Usare un pad da 1 mm di spessore sul SoC (al centro) e pad da 2 mm di spessore sul chip RP1 e sui componenti dell’alimentazione. Le forme e le dimensioni effettive dei pad termici possono variare.*

### Collegamento dell’antenna

Prima di rimontare la scheda portante, collegare il cavo dell’antenna U.FL al connettore per antenna wireless del CM5. Questo collegamento è impossibile da raggiungere una volta reinstallata la scheda portante. Il connettore U.FL richiede un allineamento accurato e una pressione decisa per innestarsi correttamente. Si deve avvertire uno scatto netto quando il connettore è completamente inserito. Fare attenzione a non deformare il corpo del connettore durante l’installazione.

### Assemblaggio finale

Controllare l’installazione del modulo per verificare che entrambi i connettori siano completamente inseriti e che il modulo appoggi in piano sulla scheda portante, senza spazi. I pad termici devono essere a contatto con i componenti del modulo che generano calore.

Riposizionare la scheda portante nella custodia, verificando che i pad termici sul CM5 siano allineati alle corrispondenti aree di dissipazione del calore sul fondo della custodia. Rimontare tutte le viti di fissaggio della scheda portante e ricollegare i cavi scollegati durante la rimozione.

Completare il rimontaggio seguendo la procedura standard di chiusura della custodia. Al primo avvio il sistema dovrebbe riconoscere automaticamente il nuovo CM5.

!!! warning "Avvertenza sui connettori"
    I connettori scheda-scheda sono i componenti più fragili di questa procedura. Non usare mai utensili metallici in prossimità dei connettori, applicare solo forza verticale durante la rimozione o l’installazione e verificare il perfetto allineamento prima di esercitare pressione. I connettori danneggiati richiedono in genere la sostituzione della scheda portante.

!!! quote "Informazioni correlate"
    - **Configurazione del sistema dopo la sostituzione:** vedere [Guida al software](./software.md)
    - **Risoluzione dei problemi di avvio:** vedere [Risoluzione dei problemi](./troubleshooting.md)
    - **Gestione termica:** vedere [Riferimento hardware](../technical-reference/hardware.md)

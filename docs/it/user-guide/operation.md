# Funzionamento del sistema

## Indicatori LED di stato

HALPI2 è dotato di cinque LED RGB che forniscono un riscontro visivo sullo stato del sistema e sulle condizioni di alimentazione.

### Riferimento rapido degli stati dei LED

| Schema dei LED | Colore | Significato |
|-------------|-------|---------|
| LED 5 acceso fisso | Rosso | Alimentazione presente, in attesa di carica |
| Riempimento progressivo | Rosso | Carica dei supercondensatori |
| Arcobaleno + ciclo di colori | Multicolore | Avvio del CM5 non riuscito |
| Barra di tensione | Giallo | Funzionamento in modalità Solo |
| Barra di tensione | Verde | Funzionamento in modalità Co-op |
| Barra di tensione | Arancione | Alimentazione di riserva attiva (Solo) |
| Barra di tensione | Verde scuro | Alimentazione di riserva attiva (Co-op) |
| Tutti lampeggianti | Rosso | Sovratensione dei supercondensatori |
| Tutti accesi fissi | Rosso | Timeout del watchdog |
| Barra di tensione | Viola | Spegnimento in corso |
| Tutti accesi fissi | Blu | Spegnimento verso lo standby in corso |
| Tutti accesi fissi | Rosso attenuato | Standby |
| Tutti spenti | — | Sistema spento |

### Indicazione della tensione dei supercondensatori

Durante il funzionamento i LED fungono da indicatore di tensione e mostrano il livello di carica dei supercondensatori:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Gestione dell’alimentazione e procedure di spegnimento

HALPI2 è dotato di un alimentatore progettato per resistere a picchi di tensione, disturbi e brevi interruzioni.

### Panoramica del sistema di alimentazione

Il sistema di gestione dell’alimentazione dell’HALPI2 è costituito da:

- **Alimentatore ad ampio intervallo** (ingresso 11–32 V CC con protezione fino a 100 V CC)
- **Sistema di riserva a supercondensatori** per spegnimenti controllati in caso di mancanza di alimentazione
- **Limitazione di corrente** (selezionabile 0,9 A o 2,5 A)
- **Rilevamento della mancanza di alimentazione** e avvio automatico dello spegnimento
- **Monitoraggio della tensione e della corrente di ingresso**

Il sistema funziona in due modalità: modalità Solo e modalità Co-op.

### Funzionamento in modalità Solo

La modalità Solo garantisce un funzionamento autonomo di base quando il demone HALPI non è in esecuzione. Il controller opera in modo indipendente, senza comunicazione con il software.

#### Caratteristiche della modalità Solo

- **Nessuna comunicazione software necessaria**
- **Protezione di base dalla mancanza di alimentazione**: monitora la tensione di ingresso e reagisce alla mancanza di alimentazione
- **Spegnimento automatico tramite pressioni simulate del pulsante di accensione**
- **Opzioni di monitoraggio e configurazione limitate**

#### Mancanza di alimentazione e spegnimento in modalità Solo

**Rilevamento della mancanza di alimentazione:**
Il controller monitora la tensione di ingresso e rileva la mancanza di alimentazione. Un timer di interruzione di corrente (valore predefinito 5 secondi) impedisce lo spegnimento in caso di brevi interruzioni.

**Sequenza di spegnimento automatico:**

1. **Il controller rileva la mancanza di alimentazione**
2. **Si attiva il timer di interruzione di corrente**, che distingue i disturbi da un’effettiva mancanza di alimentazione
3. **Pressioni simulate del pulsante di accensione**: il controller invia al Compute Module una doppia pressione del pulsante di accensione
4. **Il sistema operativo reagisce** e avvia lo spegnimento controllato
5. **I supercondensatori mantengono l’alimentazione** (in genere 30–60 secondi disponibili)
6. **Protezione con timeout di 60 secondi**: spegnimento forzato se lo spegnimento controllato non riesce
7. **Il sistema resta spento** finché l’alimentazione non torna
8. **Riavvio automatico** al ritorno dell’alimentazione

**Spegnimento manuale in modalità Solo:**

- Avviene il normale spegnimento del sistema operativo
- Il sistema si riavvia automaticamente dopo 5 secondi se l’alimentazione di ingresso è ancora presente
- Per uno spegnimento definitivo, scollegare l’alimentazione di ingresso dopo aver avviato lo spegnimento controllato

#### Quando la modalità Solo è attiva

La modalità Solo si attiva:

- Durante l’avvio iniziale, prima che parta il demone HALPI
- Se il demone HALPI non si avvia o è disabilitato
- Su sistemi operativi non supportati, privi del demone
- Quando il demone si è bloccato o non risponde più

!!! tip "Affidabilità della modalità Solo"
    La modalità Solo offre una protezione essenziale, ma è meno affidabile della modalità Co-op. Il controller si affida a pressioni simulate del pulsante per richiedere lo spegnimento, che potrebbero non funzionare se il sistema è bloccato.

### Funzionamento in modalità Co-op

La modalità Co-op offre tutte le funzioni di gestione dell’alimentazione quando il demone HALPI è in esecuzione e comunica con il controller.

#### Funzioni della modalità Co-op

- **Comunicazione diretta con il software**: scambio di dati in tempo reale tra controller e demone
- **Protezione con timer watchdog**: un timeout di 30 secondi garantisce la stabilità del sistema
- **Comportamento di spegnimento configurabile**: tempi e comandi personalizzabili
- **Monitoraggio in tempo reale**: monitoraggio completo dei parametri di alimentazione
- **Opzioni di configurazione avanzate**

#### Mancanza di alimentazione e spegnimento in modalità Co-op

**Rilevamento della mancanza di alimentazione:**
Il controller monitora l’alimentazione di ingresso e comunica gli eventi direttamente al demone HALPI. Il timer di interruzione di corrente configurabile (valore predefinito 5 secondi) consente brevi interruzioni dell’alimentazione senza avviare lo spegnimento.

**Sequenza di spegnimento automatico:**

1. **Il controller rileva la mancanza di alimentazione** e lo comunica al demone HALPI
2. **Valutazione del timer di interruzione di corrente**: il demone valuta se la mancanza di alimentazione supera la soglia
3. **Esecuzione del comando di spegnimento**: il demone esegue il comando di spegnimento (predefinito: `/sbin/poweroff`)
4. **Spegnimento controllato del sistema operativo**: le applicazioni si chiudono e i file system vengono smontati in sicurezza
5. **L’alimentazione di riserva dei supercondensatori** fornisce energia per tutta la durata dello spegnimento
6. **Il controller monitora il completamento**: rileva quando il Compute Module si spegne
7. **La linea da 5 V viene disattivata** al termine dello spegnimento
8. **Il sistema resta spento** finché non torna l’alimentazione di ingresso
9. **Gestione del riavvio**: in base alla configurazione, il sistema si riavvia automaticamente oppure resta spento

**Spegnimento manuale in modalità Co-op:**

- Quando viene avviato dal software, avviene un normale spegnimento controllato
- Il sistema si riavvia automaticamente dopo 5 secondi se l’alimentazione di ingresso è ancora presente
- Per impedire il riavvio automatico, scollegare l’alimentazione oppure impostare `auto_restart` su `false`

#### Protezione watchdog

La modalità Co-op include la protezione con timer watchdog:

- **Timeout di comunicazione di 30 secondi**: il demone deve comunicare regolarmente con il controller
- **Ripristino automatico**: il sistema si riavvia se la comunicazione si interrompe
- **Protezione dai guasti software**: garantisce il ripristino in caso di blocco del demone o del sistema
- **“Alimentare il watchdog”**: il demone invia aggiornamenti di stato regolari per azzerare il timer

#### Quando la modalità Co-op è attiva

La modalità Co-op si attiva quando:

- Il demone HALPI è in esecuzione e funziona correttamente
- La comunicazione tra demone e controller è stabilita
- Il sistema funziona su un sistema operativo supportato
- Sono disponibili tutte le funzioni di monitoraggio e controllo del sistema

!!! info "Verifica della modalità Co-op"
    Controllare lo stato del demone: `systemctl status halpid`

    Visualizzare lo stato del controller: `halpi status`

    Per ulteriori informazioni sul comando `halpi`, vedere la [Guida al software](./software.md#halpi-daemon-halpid).

### Alimentazione di riserva e sistema di condensatori

Entrambe le modalità si affidano al sistema di riserva a supercondensatori per la protezione tramite spegnimento controllato:

**Durata dell’alimentazione di riserva:**

- I supercondensatori forniscono 30–60 secondi di alimentazione di riserva
- La durata dipende dal carico del sistema e dalle periferiche collegate
- È un tempo sufficiente per chiudere in sicurezza il file system e terminare i processi
- Non è pensata per proseguire il funzionamento durante interruzioni prolungate

**Caratteristiche di carica:**

- Tempo di carica: 25 secondi con limite di corrente di 0,9 A
- Tempo di carica: 9 secondi con limite di corrente di 2,5 A
- L’avanzamento della carica è indicato visivamente dalla progressione dei LED (riempimento rosso)

!!! warning "Limiti della protezione dalla mancanza di alimentazione"
    Il sistema a supercondensatori è progettato per lo spegnimento controllato, non per la continuità di funzionamento. Non farvi affidamento in caso di interruzioni di corrente prolungate.

### Considerazioni sullo spegnimento manuale

HALPI2 privilegia il funzionamento e il ripristino automatici, il che influisce sul comportamento dello spegnimento manuale.

#### Comportamento di riavvio automatico

Per impostazione predefinita, HALPI2 si riavvia dopo uno spegnimento manuale se l’alimentazione di ingresso è ancora presente:

- Lo spegnimento manuale comporta un normale spegnimento del sistema operativo
- Al completamento dello spegnimento segue un periodo di attesa di 5 secondi
- Il sistema si riavvia automaticamente per mantenere la disponibilità operativa
- Questo garantisce il ripristino dopo spegnimenti accidentali

#### Metodi di spegnimento intenzionale

Per uno spegnimento definitivo, utilizzare uno dei metodi seguenti:

**Metodo con scollegamento dell’alimentazione:**

1. Avviare lo spegnimento controllato dal software
2. Attendere il completamento dello spegnimento (i LED si spengono)
3. Scollegare l’alimentazione di ingresso per impedire il riavvio automatico

**Metodo con configurazione:**

1. Disattivare il riavvio automatico: `halpi config set auto_restart false`
2. Avviare lo spegnimento dal software
3. Il sistema resta spento al termine dello spegnimento

**Modalità standby (in futuro):**
!!! info "Stato della funzione"
    La modalità standby è prevista per versioni future del firmware. Consentirà di spegnere il Compute Module mantenendo attivo il controller dell’HALPI2, in attesa di eventi di riattivazione.

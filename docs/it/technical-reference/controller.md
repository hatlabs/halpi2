---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Controller della scheda portante

La scheda portante (carrier board) dell’HALPI2 include un microcontrollore RP2040 che gestisce l’alimentazione, monitora il sistema e controlla i LED del pannello frontale. Il controller funziona indipendentemente dal Compute Module: è attivo dal momento in cui viene collegata l’alimentazione di ingresso, prima che il sistema operativo si avvii e dopo che si è spento. Il Compute Module comunica con esso tramite I2C (bus 1, indirizzo `0x6d`) attraverso il [demone HALPI](../user-guide/software.md#strumento-da-riga-di-comando-halpi).

Questa pagina descrive le modalità di funzionamento, le transizioni di stato e la configurazione del controller. Documenta la versione 3.3.x del firmware. Per l’uso di tutti i giorni non è necessario leggere nulla di tutto questo — vedere invece [Uso quotidiano](../user-guide/operation.md).

## Modalità di funzionamento

Il controller funziona in una di due modalità, a seconda che il demone HALPI stia comunicando con esso oppure no.

### Modalità Co-op

La modalità Co-op è la modalità di funzionamento normale. È attiva quando il demone HALPI (`halpid`) è in esecuzione e comunica con il controller. L’immagine HaLOS preinstallata e tutte le immagini dei sistemi operativi di Hat Labs includono il demone.

In modalità Co-op:

- Il controller e il demone si scambiano dati in tempo reale: tensioni, corrente, temperature e stato.
- Gli eventi di mancanza di alimentazione vengono comunicati al demone, che avvia uno spegnimento controllato del sistema operativo.
- Il timer del watchdog protegge dai blocchi del sistema operativo (vedere [Protezione tramite watchdog](#protezione-tramite-watchdog)).
- La configurazione può essere letta e modificata con lo strumento da riga di comando `halpi`.

### Modalità Solo

La modalità Solo è la modalità di ripiego. Il controller vi entra quando non c’è comunicazione con il demone:

- durante l’avvio, prima della partenza del demone
- se il demone non è installato, è stato disabilitato o si è arrestato in modo anomalo
- sui sistemi operativi privi di supporto per HALPI2

In modalità Solo il controller protegge comunque dalla mancanza di alimentazione, ma con un meccanismo più rudimentale: richiede lo spegnimento simulando pressioni del pulsante di accensione e non può sapere se il sistema operativo ha davvero completato lo spegnimento in modo controllato.

!!! tip "Affidabilità della modalità Solo"
    La modalità Solo offre una protezione essenziale, ma è meno affidabile della modalità Co-op. Le pressioni simulate del pulsante non funzionano se il sistema operativo è bloccato. Se si utilizza un sistema operativo personalizzato, installare il demone HALPI — vedere [Altre distribuzioni Debian](../software-development/ubuntu-installation.md).

## Mancanza di alimentazione e sequenze di spegnimento

Il controller monitora continuamente la tensione di ingresso. L’alimentazione di ingresso è considerata assente quando la tensione di ingresso scende sotto 9,0 V. Un timer di interruzione di corrente (predefinito 5 secondi) distingue i disturbi brevi dalle interruzioni reali: i supercondensatori coprono l’intervallo e, se l’alimentazione ritorna entro il tempo del timer, non accade altro.

### Sequenza di spegnimento in modalità Co-op

1. Il demone rileva la mancanza di alimentazione dalle misure di tensione del controller.
2. Il demone attende che trascorra il limite di tempo di interruzione (predefinito 5 secondi).
3. Il demone esegue il comando di spegnimento configurato (predefinito `/sbin/poweroff`).
4. Il sistema operativo si spegne in modo controllato alimentato dai supercondensatori.
5. Il controller rileva che il Compute Module si è spento e disattiva la linea da 5 V.
6. Se lo spegnimento non si completa entro 60 secondi, il controller forza lo spegnimento.
7. Il sistema resta spento finché l’alimentazione di ingresso non ritorna, quindi si riavvia automaticamente.

### Sequenza di spegnimento in modalità Solo

1. Il controller rileva la mancanza di alimentazione e avvia il timer di interruzione di corrente (predefinito 5 secondi).
2. Allo scadere del timer, il controller simula una doppia pressione del pulsante di accensione.
3. Il sistema operativo risponde e avvia uno spegnimento controllato alimentato dai supercondensatori.
4. Se lo spegnimento non si completa entro 60 secondi, il controller forza lo spegnimento.
5. Il sistema resta spento finché l’alimentazione di ingresso non ritorna, quindi si riavvia automaticamente.

### Comportamento di riavvio dopo uno spegnimento da software

Uno spegnimento avviato da software mentre l’alimentazione di ingresso resta disponibile (ad esempio con il comando `shutdown` o dal menu del desktop) termina nello stato *powered down* (spento). Ciò che accade dopo dipende dall’impostazione di configurazione `auto_restart`:

- `auto_restart` disabilitato (impostazione di fabbrica sulle unità prodotte dall’inizio del 2026): il sistema resta spento finché l’alimentazione di ingresso non viene tolta e ridata o finché non viene premuto un pulsante di accensione.
- `auto_restart` abilitato (valore di ripiego del firmware e impostazione di fabbrica sulle unità precedenti): il controller riavvia il sistema dopo 5 secondi, in modo che un sistema non presidiato non resti spento a causa di uno spegnimento accidentale.

L’impostazione si modifica con `halpi config set auto_restart <true|false>`.

La pressione di un pulsante di accensione, o lo spegnere e riaccendere l’alimentazione di ingresso, riavvia sempre il sistema, indipendentemente dall’impostazione `auto_restart`.

## Protezione tramite watchdog

In modalità Co-op un timer watchdog protegge dai blocchi del sistema operativo:

- Il demone deve inviare al controller un segnale di feed del watchdog a intervalli regolari.
- Se nessun feed arriva entro il timeout del watchdog (predefinito 10 secondi), il controller considera l’host non rispondente, mostra la sequenza dei LED di allarme (tutti i LED rossi fissi) e spegne e riaccende il Compute Module per ripristinare il funzionamento.
- Il timeout è configurabile con `halpi config set watchdog_timeout <seconds>`.

## Standby

Lo standby spegne il Compute Module mentre il controller resta attivo, in attesa di una riattivazione programmata:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Durante la transizione tutti i LED sono blu fissi; in standby sono rossi attenuati. Il controller riavvia il sistema all’orario programmato, alla pressione di un pulsante di accensione o dopo che l’alimentazione di ingresso è stata tolta e ridata.

## Riferimento dei LED di stato

I cinque LED RGB del pannello frontale riflettono lo stato del controller. Questa tabella è la mappatura di riferimento dagli stati del controller alle sequenze dei LED; la pagina [Uso quotidiano](../user-guide/operation.md#indicatori-led-di-stato) ne presenta una versione semplificata.

| Stato del controller | Sequenza dei LED |
|:---------------------|:-----------------|
| PowerOff (nessuna alimentazione di ingresso utilizzabile; controller alimentato dalla carica residua) | LED 5 rosso fisso |
| OffCharging | Barra rossa che si riempie durante la carica dei supercondensatori |
| SystemStartup | Scorrimento arcobaleno, quindi un ciclo di colori fissi |
| OperationalSolo | Barra gialla del livello di carica |
| OperationalCoOp | Barra verde del livello di carica |
| BlackoutSolo | Barra arancione del livello di carica |
| BlackoutCoOp | Barra verde scuro del livello di carica |
| BlackoutShutdown, ManualShutdown | Barra viola del livello di carica |
| PoweredDownBlackout, PoweredDownManual | Tutti spenti |
| HostUnresponsive (timeout del watchdog) | Tutti rossi fissi |
| EnteringStandby | Tutti blu fissi |
| Standby | Tutti rossi attenuati |
| Allarme di sovratensione dei supercondensatori | Tutti i LED lampeggianti in rosso |

Nelle sequenze a barra del livello di carica, ogni LED acceso rappresenta un volt di tensione dei supercondensatori:

| LED | Intervallo di tensione |
|:----|:-----------------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Parametri di configurazione

La configurazione è memorizzata nella memoria flash del controller e viene conservata anche spegnendo e riaccendendo il sistema. Si legge e si modifica con `halpi config` — vedere la [Guida al software](../user-guide/software.md#gestione-della-configurazione).

| Parametro | Valore predefinito | Descrizione |
|:----------|:-------------------|:------------|
| `auto_restart` | `false` sulle unità attuali (impostato al collaudo di produzione); valore di ripiego del firmware `true` | Riavvio automatico 5 s dopo uno spegnimento da software in presenza di alimentazione di ingresso |
| `watchdog_timeout` | 10 s | Timeout del watchdog in modalità Co-op |
| `power_on_threshold` | 8,0 V | Tensione dei supercondensatori richiesta prima dell’accensione del Compute Module |
| `solo_power_off_threshold` | 5,5 V | Tensione dei supercondensatori alla quale il controller forza lo spegnimento in modalità Solo |
| `solo_depleting_timeout` | 5 s | Timer di interruzione di corrente in modalità Solo |
| `led_brightness` | 48 | Luminosità dei LED del pannello frontale (0–255) |

Il timer di interruzione di corrente della modalità Co-op e il comando di spegnimento sono impostazioni del demone, configurate in `/etc/halpid/halpid.conf` (`blackout-time-limit`, predefinito 5 s; `poweroff`, predefinito `/sbin/poweroff`).

!!! quote "Informazioni correlate"
    - **Uso di tutti i giorni:** vedere [Uso quotidiano](../user-guide/operation.md)
    - **Dettagli sul sistema di alimentazione:** vedere [Alimentazione in dettaglio](./power-supply.md)
    - **Aggiornamenti del firmware:** vedere [Guida al software](../user-guide/software.md#aggiornamenti-del-firmware)
    - **Sorgenti del firmware e protocollo I2C:** vedere il repository [`HALPI2-firmware`](https://github.com/hatlabs/HALPI2-firmware)

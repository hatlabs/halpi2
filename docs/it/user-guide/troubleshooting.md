# Risoluzione dei problemi

Questa pagina descrive i problemi più comuni che possono presentarsi durante il funzionamento dell’HALPI2 e il modo di risolverli.

## Problemi di alimentazione e di avvio

### Il sistema non si accende

**Sintomi:** nessuna attività dei LED, nessun segno di funzionamento dopo il collegamento dell’alimentazione.

1. Verificare con un multimetro, sul connettore E7T, che la tensione di ingresso rientri nell’intervallo previsto (11–32 V CC).
2. Controllare i collegamenti del cavo di alimentazione: accertarsi che il connettore E7T sia inserito a fondo.
3. Se si utilizza l’alimentazione dal bus NMEA 2000, verificare che il limitatore di corrente sia impostato su 0,9 A e che la rete sia in grado di fornire corrente sufficiente.
4. Aprire la custodia e verificare l’assenza di danni visibili o di collegamenti interni allentati.

### LED con sequenza arcobaleno

**Sintomi:** i LED percorrono ciclicamente una sequenza arcobaleno senza raggiungere mai uno stato stabile.

La sequenza arcobaleno indica che il controller si è acceso ma il CM5 non viene rilevato. Ciò può accadere se:

- Il Compute Module non è installato oppure non è inserito correttamente.
- Il Compute Module è difettoso.
- Un dispositivo collegato immette tensioni parassite che impediscono l’avvio del CM5: provare a scollegare il cavo HDMI.

1. Scollegare eventuali display HDMI e riavviare, per escludere interferenze dovute a tensioni parassite.
2. Se il problema persiste, aprire la custodia e verificare che il modulo CM5 sia inserito a fondo nel proprio connettore: questa operazione richiede la rimozione della scheda portante (carrier board).

### I LED restano gialli

**Sintomi:** i LED passano dal rosso (carica in corso) al giallo (sistema alimentato), ma non raggiungono mai il verde.

Lo stato giallo indica che il controller ha alimentato il CM5 e attende la risposta del demone. Se i LED restano gialli, il sistema operativo non si sta avviando oppure il demone HALPI non è installato.

1. Verificare che il selettore della modalità di avvio sia in posizione “Normal”: il LED indicatore giallo accanto al selettore si accende quando la modalità di avvio è impostata su “Abnormal” (avvio da USB).
2. Collegare un display tramite HDMI per individuare errori di avvio o la presenza del prompt di accesso.
3. Verificare che l’unità SSD NVMe sia inserita correttamente nel proprio slot M.2.
4. Se il sistema operativo si avvia correttamente, verificare che il demone sia installato: `systemctl status halpid`
5. Se il demone è installato ma non è in esecuzione, consultarne i log: `journalctl -u halpid -e`

### Il sistema si spegne in modo imprevisto

**Sintomi:** il sistema si spegne senza alcun intervento dell’utente, anche se l’alimentazione esterna è collegata.

1. Verificare la stabilità della tensione di ingresso: brevi cali al di sotto della soglia attivano il timer di interruzione di corrente. Utilizzare `halpi status` per monitorare `V_in` in tempo reale.
2. Ispezionare il cavo di alimentazione alla ricerca di collegamenti allentati o conduttori danneggiati che possano causare contatti intermittenti.
3. Se si utilizza l’alimentazione dal bus NMEA 2000, verificare che la tensione di rete rimanga stabile sotto carico. Altri dispositivi ad assorbimento elevato presenti sulla rete possono provocare cadute di tensione.

## Aggiornamento del firmware non riuscito o ripristinato

Dopo un aggiornamento del firmware, se il sistema si riavvia entro 30 secondi il firmware ripristina automaticamente la versione precedente come misura di sicurezza.

1. Verificare la versione corrente del firmware: `halpi get firmware_version`
2. Ripetere l’aggiornamento: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Al termine dell’installazione dell’aggiornamento, eseguire uno spegnimento controllato: `sudo shutdown -h now`
4. Attendere che il sistema si sia spento completamente prima di ricollegare l’alimentazione: lasciare trascorrere almeno 30 secondi prima del riavvio successivo, per evitare che si attivi il meccanismo di ripristino.

## Problemi di rete e di interfaccia

### Nessun dato NMEA 2000

**Sintomi:** `candump can0` non produce alcun output, oppure Signal K non riceve dati.

1. Verificare lo stato dell’interfaccia CAN:
    ```bash
    ip link show can0
    ```
    L’interfaccia dovrebbe risultare `UP`. Se risulta `DOWN`, attivarla:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Controllare il LED RX sulla scheda portante: deve lampeggiare quando sulla rete sono presenti dati. Se il LED RX resta spento:
    - Verificare il collegamento del cavo Micro-C e la posizione del connettore a T.
    - Verificare che la rete NMEA 2000 sia alimentata e che gli altri dispositivi stiano trasmettendo.
    - Accertarsi che il jumper di terminazione da 120 Ω **non** sia inserito sulle reti NMEA 2000.

3. Se il LED RX lampeggia ma `candump` non mostra nulla, il problema è nel software. Verificare la configurazione dell’interfaccia CAN:
    ```bash
    ip -details link show can0
    ```

4. Verificare la presenza di errori sul bus CAN:
    ```bash
    ip -statistics link show can0
    ```
    Conteggi di errore elevati indicano problemi di cablaggio, velocità di trasmissione errata o contesa sul bus.

### Nessun dato NMEA 0183 su RS-485

**Sintomi:** nessun dato su `/dev/ttyAMA4`, oppure il dispositivo collegato non risponde.

1. Aprire la custodia e controllare i LED dell’interfaccia RS-485: il LED RX deve lampeggiare durante la ricezione dei dati.
2. Verificare che la porta seriale esista e sia accessibile:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Verificare la polarità del cablaggio: RS-485 utilizza una segnalazione differenziale con linee A/B. Se i collegamenti A e B sono invertiti, la comunicazione non avviene.

### Collegamento Ethernet non stabilito

1. Controllare il cavo Ethernet e il connettore RJ45. Provare con un altro cavo.
2. Aprire la custodia e controllare i LED Ethernet per verificare lo stato del collegamento.
3. Verificare lo stato del collegamento: `ip link show eth0`
4. Se il collegamento è attivo ma non è presente alcun indirizzo IP, controllare il DHCP: `sudo dhclient eth0`
5. Per le configurazioni con IP statico, verificare le impostazioni in `/etc/network/interfaces` oppure in NetworkManager.

## Problemi del sistema operativo

### Impossibile accedere al dispositivo via SSH

1. Verificare che SSH sia abilitato: `sudo systemctl status ssh`
2. Verificare la connettività di rete: il dispositivo risponde al ping?
3. SSH è abilitato per impostazione predefinita nelle immagini HaLOS senza monitor (headless) e in OpenPlotter. Nelle varianti HaLOS Desktop e in Raspberry Pi OS, SSH può essere abilitato tramite `raspi-config`.

### Il sistema è lento o si blocca

1. Controllare la temperatura della CPU: temperature ambiente estreme possono provocare la limitazione termica delle prestazioni. Utilizzare:
    ```bash
    vcgencmd measure_temp
    ```
    Temperature superiori a 80 °C indicano un problema termico. Ridurre la temperatura ambiente oppure migliorare la circolazione dell’aria attorno alla custodia.

2. Controllare l’utilizzo della memoria: `free -h`
3. Controllare l’utilizzo del disco: `df -h`. Un’unità SSD NVMe piena causa gravi problemi di prestazioni.
4. Verificare la presenza di processi fuori controllo: `top` oppure `htop`

### L’orologio è errato dopo una mancanza di alimentazione

HALPI2 dispone di un orologio in tempo reale (RTC) con batteria tampone, che mantiene l’ora durante le interruzioni di corrente. Se l’orologio si azzera:

1. Controllare la batteria dell’RTC: potrebbe essere necessario sostituirla se il sistema è rimasto a lungo senza alimentazione.
2. Verificare la sincronizzazione NTP quando la rete è disponibile: `timedatectl status`
3. Se necessario, impostare manualmente l’ora: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Diagnostica tramite LED

Le sequenze dei LED consentono di individuare rapidamente lo stato del sistema:

| Sintomo | Sequenza dei LED | Causa probabile |
|:--------|:------------|:-------------|
| Il sistema non si avvia | Nessun LED acceso | Assenza di alimentazione di ingresso o guasto hardware |
| Blocco durante l’avvio | Riempimento progressivo rosso | Supercondensatori ancora in carica: attendere |
| Blocco durante l’avvio | Sequenza arcobaleno | CM5 non rilevato: verificare l’inserimento del modulo e scollegare i display |
| Restano gialli | Giallo fisso | Il sistema operativo non si avvia oppure il demone non è installato |
| Spegnimento imprevisto | Scorrimento verde/giallo | Rilevata mancanza di alimentazione: verificare l’alimentazione di ingresso |
| Sovratensione | LED 1 rosso lampeggiante | Tensione di ingresso troppo elevata (> 32 V) |
| Guasto | Tutti i LED lampeggianti in rosso | Guasto hardware: contattare il produttore |

!!! quote "Informazioni correlate"
    - **Sequenze dei LED:** vedere [Indicatori LED di stato](./operation.md#status-led-indicators)
    - **Gestione dell’alimentazione:** vedere [Gestione dell’alimentazione e procedure di spegnimento](./operation.md#power-management-and-shutdown-procedures)
    - **Gestione del demone:** vedere [Guida al software](./software.md#halpi-daemon-halpid)
    - **Dettagli sull’interfaccia CAN:** vedere [Interfacce e connettività](./interfaces.md#can-fd-nmea-2000)
    - **Dettagli sull’interfaccia RS-485:** vedere [Interfacce e connettività](./interfaces.md#rs-485-nmea-0183)

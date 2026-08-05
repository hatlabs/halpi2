---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Guida al software

## Immagini del sistema operativo

Hat Labs fornisce immagini precompilate per HALPI2. Tutte le immagini includono la configurazione e le personalizzazioni necessarie per l’hardware HALPI2, tra cui CAN (NMEA 2000) come dispositivo di rete `can0`, RS-485 (NMEA 0183) come `/dev/ttyAMA4` e il pacchetto `halpi2-firmware`.

### HaLOS (predefinito)

[HaLOS](https://docs.halos.fi) è una distribuzione Linux basata su container progettata per applicazioni nautiche e industriali. Offre un’interfaccia di gestione web per l’amministrazione del sistema, la gestione delle applicazioni e il monitoraggio: non sono necessari display, tastiera o VNC.

**Varianti dell’immagine:**

| Immagine | Descrizione |
|:------|:------------|
| Halos-HALPI2 | Immagine base senza monitor (headless) con Cockpit e gestione dei container |
| Halos-HALPI2-Desktop | Immagine base con Raspberry Pi Desktop |
| Halos-HALPI2-Marine | Senza monitor, con applicazioni nautiche (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Desktop con applicazioni nautiche |

Scaricare le immagini HaLOS dalla [pagina delle release di HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest). Per la documentazione dettagliata, vedere [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter è un’immagine basata su Raspberry Pi OS con aggiunte per le applicazioni nautiche. Offre un ambiente desktop tradizionale con accesso remoto VNC e include Signal K e OpenCPN preinstallati.

Se non si utilizzano display, tastiera e mouse con l’HALPI2, è possibile collegarsi al computer tramite un cavo Ethernet oppure tramite l’access point WiFi (`OpenPlotter`, password `12345678`).

In entrambi i casi è possibile accedere al computer HALPI2 tramite VNC o SSH. Per utilizzare VNC è necessario scaricare [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) di RealVNC.

Poiché sia l’access point sia l’utente predefinito hanno password predefinite, è indispensabile modificarle immediatamente dopo il primo avvio. La procedura è descritta nella [documentazione di OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Scaricare le immagini OpenPlotter da [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS e Raspberry Pi OS Lite

Se si preferisce utilizzare il Raspberry Pi OS standard, è possibile scaricare
l’immagine più recente con supporto per HALPI2 dal [repository GitHub](https://github.com/hatlabs/openplotter-halpi/releases).
Scrivere l’immagine sull’unità SSD utilizzando Raspberry Pi Imager. Durante la
scrittura è possibile applicare personalizzazioni come l’impostazione
dell’hostname, l’abilitazione di SSH e la configurazione del WiFi.

Se si decide di non applicare personalizzazioni, per completare la
configurazione iniziale è necessario collegare all’HALPI2 un display e una
tastiera. Al primo avvio verranno richiesti un nome utente e una password.


## Scrittura di un’immagine del sistema operativo sull’unità SSD

Sono disponibili due metodi per scrivere un’immagine del sistema operativo sull’unità SSD NVMe dell’HALPI2: rimuovere l’unità SSD e utilizzare un adattatore USB NVMe, oppure scrivere l’immagine direttamente sull’HALPI2. Il metodo con adattatore USB NVMe è consigliato per praticità e semplicità d’uso, poiché questi adattatori si trovano online a basso costo e offrono una procedura di scrittura lineare.

### Scrittura tramite un adattatore USB NVMe

Per scrivere l’immagine con il metodo dell’adattatore USB NVMe, iniziare rimuovendo l’unità SSD NVMe dall’HALPI2 seguendo la procedura descritta nella [Guida all’hardware](./hardware.md#sostituzione-dellunita-ssd-nvme). Quindi scaricare un’immagine compatibile con HALPI2 — un’[immagine HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest) oppure un’[immagine OpenPlotter/Raspberry Pi OS](https://github.com/hatlabs/openplotter-halpi/releases) — assicurandosi di selezionare l’immagine adatta all’uso previsto.

Inserire l’unità SSD nell’adattatore USB NVMe e collegarlo al computer. Utilizzare Raspberry Pi Imager per scrivere l’immagine scaricata sull’unità SSD NVMe. Se si scrive un’immagine Raspberry Pi OS, durante la procedura è possibile modificare e applicare le impostazioni di personalizzazione del sistema operativo secondo necessità. Se però non vengono applicate impostazioni personalizzate, per la configurazione iniziale successiva all’installazione occorrerà collegare all’HALPI2 una tastiera e un mouse USB.

Con le immagini HaLOS, le impostazioni di personalizzazione del sistema operativo **non** devono essere applicate durante la scrittura. HaLOS si configura dopo l’avvio tramite la sua interfaccia web.

Analogamente, con l’immagine OpenPlotter le impostazioni di personalizzazione del sistema operativo **non** devono essere applicate durante la scrittura. La configurazione avviene invece dopo il primo avvio, utilizzando gli strumenti di configurazione di Raspberry Pi e di OpenPlotter.

Al termine della scrittura, scollegare l’adattatore e rimuovere l’unità SSD. Reinserire l’unità SSD nell’HALPI2 seguendo la procedura di installazione descritta nella Guida all’hardware, quindi rimontare la custodia secondo la stessa guida.

### Scrittura direttamente sull’HALPI2

In alternativa, è possibile scrivere l’immagine del sistema operativo direttamente sull’HALPI2 senza rimuovere l’unità SSD. Questo metodo segue la procedura standard prevista per il Compute Module, documentata nella [documentazione Raspberry Pi](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Le istruzioni di configurazione della scheda riportate in quella pagina sono scritte per la CM5 IO Board, ma la procedura è analoga per HALPI2.

**Prerequisiti.** Installare lo strumento `rpiboot` dal [repository `usbboot`](https://github.com/raspberrypi/usbboot) di Raspberry Pi. Su Linux e macOS, compilarlo e installarlo dai sorgenti come descritto nel README del repository; su Windows, installare Raspberry Pi Imager oppure il programma di installazione autonomo di `rpiboot` collegato nella stessa pagina.

Per predisporre l’HALPI2 alla scrittura via USB:

1. Spegnere completamente il sistema e aprire il coperchio della custodia seguendo la procedura descritta nella [Guida all’hardware](./hardware.md#accesso-alla-custodia).
2. Individuare il connettore USB-C con l’etichetta “USB Boot” a destra del profilo dell’HAT sulla scheda portante (carrier board) e portare il selettore della modalità di avvio adiacente in posizione “Abnormal”. (Non è ancora disponibile alcuna indicazione tramite LED: il dispositivo non è alimentato.)
3. Collegare un cavo USB tra il computer e il connettore USB Boot dell’HALPI2, quindi riaccendere il dispositivo. Un LED ambra accanto al selettore della modalità di avvio si accende, a conferma che l’HALPI2 è in modalità USB boot.
4. Sul computer, eseguire `rpiboot`. Lo strumento rileva l’HALPI2 e carica il firmware del gadget di archiviazione di massa; l’HALPI2 compare quindi come dispositivo di archiviazione di massa USB.
5. Una volta che `rpiboot` è andato a buon fine e il dispositivo di archiviazione di massa è comparso, riportare il selettore della modalità di avvio in posizione “Normal”. Ciò non interrompe la sessione di scrittura e garantisce che l’HALPI2 si avvii normalmente dall’immagine appena scritta dopo il successivo ciclo di spegnimento e riaccensione. Lasciandolo in posizione “Abnormal”, al successivo avvio il dispositivo rientra in modalità USB boot invece di avviare il nuovo sistema operativo.
6. Scrivere l’immagine del sistema operativo con Raspberry Pi Imager (o con qualsiasi altro strumento in grado di scrivere su un dispositivo a blocchi), scegliendo come destinazione il nuovo dispositivo di archiviazione di massa.
7. Al termine della scrittura, scollegare il cavo USB, spegnere e riaccendere l’HALPI2 e chiudere la custodia.

!!! tip "Spegnere e riaccendere senza scollegare i cavi"
    Con la custodia già aperta, il modo più rapido per riavviare l’HALPI2 consiste nel cortocircuitare brevemente i due pin inferiori dei Button Headers accanto alla presa USB-C. Toccare entrambi i pin contemporaneamente con il guscio metallico del connettore di un cavo USB-C funziona bene ed è sicuro.

## Configurazione iniziale del sistema

Dopo aver scritto correttamente l’immagine e avviato l’HALPI2 per la prima volta, sono necessari alcuni passaggi di configurazione per garantire un funzionamento sicuro e corretto del sistema.

### Configurazione di HaLOS

HaLOS si configura interamente tramite la sua interfaccia web. Dopo il primo avvio, accedere a Cockpit all’indirizzo `https://halos.local:9090/` e alla dashboard all’indirizzo `https://halos.local/`. Modificare immediatamente le password predefinite: per i dettagli vedere la [Guida introduttiva](../getting-started/getting-started.md#configurazione-al-primo-avvio) e la [documentazione di HaLOS](https://docs.halos.fi/getting-started/first-boot/).

### Configurazione di OpenPlotter

Con l’immagine OpenPlotter, il sistema si avvia con password predefinite sia per l’access point WiFi sia per l’account utente predefinito. Per motivi di sicurezza è indispensabile modificare queste password immediatamente dopo il primo avvio.

La procedura di modifica delle password e la configurazione iniziale sono descritte nella [Guida introduttiva](../getting-started/getting-started.md#configurazione-al-primo-avvio) e nella [documentazione di OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Configurazione di Raspberry Pi OS

Se si è scelto di utilizzare il Raspberry Pi OS standard invece di OpenPlotter, seguire la procedura di configurazione standard di Raspberry Pi che viene presentata al primo avvio. Questa procedura guidata accompagna nella creazione degli account utente, nell’impostazione delle password, nella configurazione delle connessioni WiFi e nell’abilitazione dei servizi essenziali, come SSH per l’accesso remoto.

Durante la configurazione iniziale può essere utile impostare anche il fuso orario, il layout della tastiera e altre preferenze regionali corrispondenti all’ambiente di utilizzo. Lo strumento di configurazione di Raspberry Pi (`raspi-config`) consente di accedere a ulteriori impostazioni di sistema, modificabili al termine della configurazione iniziale.

## Accesso remoto

HALPI2 supporta diversi metodi di accesso remoto, che consentono di monitorare e controllare il sistema senza doverlo raggiungere fisicamente. Ciò risulta particolarmente utile nelle installazioni in cui l’HALPI2 è montato senza display in punti difficili da raggiungere.

### Accesso via web (HaLOS)

HaLOS offre un’interfaccia di gestione web completa, senza bisogno di software aggiuntivo:

- **Dashboard** (`https://halos.local/`): la dashboard Homarr dà accesso a tutte le applicazioni installate, tra cui Signal K, Grafana e altre applicazioni nautiche.
- **Cockpit** (`https://halos.local:9090/`): amministrazione del sistema, con accesso al terminale, aggiornamenti software, configurazione di rete e gestione delle applicazioni in container.

### SSH (Secure Shell)

SSH offre un accesso sicuro da riga di comando al sistema HALPI2 e consente di eseguire comandi, trasferire file e svolgere da remoto le attività di amministrazione del sistema. SSH è abilitato per impostazione predefinita nelle immagini HaLOS senza monitor e in OpenPlotter. Nelle varianti HaLOS Desktop e in Raspberry Pi OS, SSH può essere abilitato con `raspi-config`.

Per connettersi tramite SSH, utilizzare un client SSH come il terminale integrato nei sistemi macOS e Linux oppure applicazioni come PuTTY su Windows. Il comando di connessione di base è:

```bash
ssh username@halpi2-ip-address
```

Le connessioni SSH sono cifrate e sicure, il che le rende adatte all’uso su reti pubbliche se configurate con un’autenticazione robusta. Richiedono inoltre pochissima banda, risultando ideali per l’accesso remoto su connessioni lente e ad alta latenza.

### VNC (Virtual Network Computing)

!!! note
    VNC è applicabile solo alle immagini OpenPlotter e Raspberry Pi OS Desktop. HaLOS utilizza invece l’accesso via web: vedere sopra.

VNC offre l’accesso remoto all’interfaccia grafica dell’HALPI2 e consente di interagire con l’ambiente desktop come se ci si trovasse fisicamente davanti al dispositivo. VNC è preinstallato e preconfigurato nelle immagini OpenPlotter. Nelle installazioni Raspberry Pi OS, VNC può essere abilitato con lo strumento di configurazione `raspi-config`.

Per collegarsi da remoto al desktop dell’HALPI2, utilizzare l’applicazione [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) di RealVNC, disponibile per dispositivi Windows, macOS, Linux, iOS e Android. VNC funziona bene sulle reti locali e negli ambienti offline, risultando ideale per le installazioni su imbarcazioni, dove la connettività internet può essere limitata o assente.

Per l’accesso remoto tramite internet, VNC richiede configurazioni di rete aggiuntive, come il port forwarding o una VPN, poiché il protocollo di per sé non attraversa i firewall e i dispositivi NAT.

### Raspberry Pi Connect

Raspberry Pi Connect propone un approccio moderno e basato su web all’accesso remoto al desktop e consente di collegarsi al desktop dell’HALPI2 utilizzando semplicemente un browser web standard, senza installare alcun software aggiuntivo. Questo servizio funziona automaticamente attraverso firewall e configurazioni NAT, risultando particolarmente adatto all’accesso remoto tramite internet senza configurazioni di rete complesse.

A differenza di VNC, Raspberry Pi Connect gestisce automaticamente le complessità di rete e offre un accesso immediato da qualsiasi luogo dotato di connessione a internet. Richiede però che anche l’HALPI2 mantenga attiva una connessione a internet per poter funzionare.

## Aggiornamenti del software

Si consiglia di eseguire aggiornamenti regolari per mantenere prestazioni e sicurezza ottimali del sistema.

### Aggiornamenti di HaLOS

In HaLOS i pacchetti di sistema (compreso il firmware HALPI2) si aggiornano tramite Cockpit oppure da riga di comando con `apt`. Le applicazioni basate su container (Signal K, Grafana e altre) si aggiornano tramite l’interfaccia Container Apps di Cockpit, che verifica la disponibilità di nuove versioni delle immagini del container.

### Aggiornamenti da riga di comando (tutte le immagini)

Il metodo più affidabile per aggiornare il sistema è l’interfaccia da riga di comando. Aprire una finestra di terminale ed eseguire i comandi seguenti per aggiornare il sistema:

```bash
sudo apt update
sudo apt upgrade
```

Il primo comando (`apt update`) aggiorna il database dei pacchetti con le versioni più recenti disponibili, mentre il secondo (`apt upgrade`) scarica e installa tutti gli aggiornamenti disponibili. Questa procedura aggiorna tutti i pacchetti installati, compresi il Raspberry Pi OS di base, i componenti OpenPlotter e il software specifico di HALPI2.

Durante l’aggiornamento può essere richiesta la conferma dell’installazione di alcuni pacchetti o del riavvio di determinati servizi. In genere è sicuro accettare queste richieste, salvo motivi specifici per rifiutarle.

### Aggiornamenti grafici

Per chi preferisce un’interfaccia grafica, l’ambiente desktop segnala visivamente la disponibilità di aggiornamenti. Quando gli aggiornamenti sono pronti per l’installazione, nell’angolo in alto a destra della barra delle applicazioni del desktop compare un’icona di download. Facendo clic su questa icona si apre il gestore degli aggiornamenti, che offre un’interfaccia semplice per esaminare e installare gli aggiornamenti disponibili.

## Aggiornamenti del firmware

Il firmware del controller HALPI2 può essere aggiornato con la procedura di aggiornamento standard di Raspberry Pi OS, che offre un approccio integrato e senza interruzioni per mantenere aggiornate le versioni del firmware. Aggiornamenti regolari del firmware sono importanti per garantire prestazioni ottimali, accedere a nuove funzionalità e mantenere la compatibilità con i componenti software in evoluzione.

### Aggiornamenti automatici del firmware

Gli aggiornamenti del firmware vengono distribuiti tramite il normale meccanismo di aggiornamento del sistema, ovvero pacchetti Debian in un repository APT. Per verificare la disponibilità di aggiornamenti del firmware e installarli, aprire una finestra di terminale ed eseguire i comandi seguenti:

```bash
sudo apt update
sudo apt upgrade
```

Quando è disponibile un nuovo firmware HALPI2, viene scaricato e installato automaticamente nell’ambito della procedura di aggiornamento. Il sistema segnala se tra i pacchetti disponibili sono inclusi aggiornamenti del firmware.

Al termine dell’aggiornamento del pacchetto del firmware, è indispensabile riavviare correttamente il sistema per applicare le modifiche al firmware. Utilizzare il comando di spegnimento per garantire un ciclo di spegnimento e riaccensione completo:

```bash
sudo shutdown -h now
```

**Importante:** il semplice riavvio del sistema non è sufficiente per gli aggiornamenti del firmware. È necessario uno spegnimento completo seguito da una riaccensione, poiché solo così il controller può riavviarsi e applicare il nuovo firmware. Il firmware del controller viene aggiornato esclusivamente durante la sequenza di accensione.

### Funzioni di sicurezza del firmware

HALPI2 integra meccanismi di sicurezza che proteggono da un firmware corrotto. Se il dispositivo viene riavviato di nuovo entro 30 secondi dall’applicazione di un aggiornamento del firmware, il sistema ripristina automaticamente la versione precedente del firmware. Questa funzione offre protezione contro aggiornamenti del firmware problematici, che potrebbero impedire il normale funzionamento.

### Installazione manuale del firmware

Per utenti esperti o in scenari specifici di risoluzione dei problemi, il firmware può essere installato manualmente con lo strumento da riga di comando HALPI. I file del firmware sono memorizzati nella directory `/usr/share/halpi2-firmware/` e possono essere flashati direttamente con:

```bash
halpi flash <firmware_file>.bin
```

### Disabilitazione degli aggiornamenti automatici del firmware

Alcuni utenti possono voler disabilitare gli aggiornamenti automatici del firmware per mantenere una versione specifica del firmware. È possibile farlo modificando il file di configurazione di HALPI2:

```bash
sudo nano /etc/halpid/firmware.conf
```

Individuare l’impostazione `AUTO_FLASH_ON_INSTALL` e modificarla in `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Salvare il file e uscire dall’editor. Questa modifica della configurazione impedisce all’HALPI2 di flashare automaticamente il nuovo firmware durante la normale procedura di aggiornamento, lasciando il pieno controllo sul momento in cui applicare gli aggiornamenti del firmware. Resta comunque possibile installare manualmente gli aggiornamenti del firmware con il comando `halpi flash` quando lo si desidera.


## Strumento da riga di comando HALPI

L’interfaccia software di HALPI2 è costituita dal servizio demone `halpid` e dallo strumento da riga di comando `halpi`. Insieme offrono funzioni di monitoraggio, configurazione e controllo del sistema.

### Demone HALPI (`halpid`)

Il demone HALPI viene eseguito come servizio di sistema e assicura la comunicazione tra il sistema operativo e il controller HALPI2. Consente il funzionamento in modalità Co-op con tutte le funzioni di monitoraggio e di gestione dell’alimentazione.

#### Gestione del servizio

Il demone è gestito tramite systemd:

```bash
# Check daemon status
systemctl status halpid

# Start the daemon
sudo systemctl start halpid

# Stop the daemon
sudo systemctl stop halpid

# Enable auto-start at boot
sudo systemctl enable halpid

# Disable auto-start
sudo systemctl disable halpid

# View daemon logs
journalctl -u halpid -f
```

#### Configurazione

La configurazione del demone è memorizzata in `/etc/halpid/halpid.conf`. Per modificarla, utilizzare:

```bash
sudo nano /etc/halpid/halpid.conf
```

Le modifiche alla configurazione richiedono il riavvio del demone:

```bash
sudo systemctl restart halpid
```

### Strumento da riga di comando HALPI (`halpi`)

Il comando `halpi` offre accesso diretto alle funzioni del controller e allo stato del sistema. Comunica con il demone per eseguire i comandi e recuperare informazioni sullo stato operativo, sulla configurazione e sui parametri hardware dell’HALPI2.

#### Stato e monitoraggio del sistema

La funzione principale dello strumento da riga di comando HALPI è fornire informazioni complete sullo stato del sistema, tra cui i parametri hardware, lo stato operativo e i dati di monitoraggio in tempo reale.

Visualizzazione dello stato del sistema:
```bash
# Display comprehensive system status
halpi status
```

Questo comando offre una panoramica completa dello stato operativo attuale dell’HALPI2, compresi i livelli di tensione, l’assorbimento di corrente, le letture di temperatura e lo stato del controller:

```
$ halpi status
 hardware_version               N/A
 firmware_version             3.1.0
 state              OperationalCoOp
 5v_output_enabled             True
 watchdog_enabled              True
 watchdog_timeout              10.0  s
 watchdog_elapsed               0.0  s
 V_in                          12.2  V
 I_in                          0.38  A
 V_supercap                   10.27  V
 T_mcu                         43.3  °C
 T_pcb                         35.2  °C
```

Per monitorare un solo valore specifico, è possibile recuperarlo come segue:

```bash
# Show controller firmware version
halpi get firmware_version
```

Per scopi di scripting è preferibile utilizzare l’API REST, come descritto nella sezione [Accesso all’API REST](#accesso-allapi-rest).

#### Gestione della configurazione

Lo strumento da riga di comando HALPI offre funzioni complete di gestione della configurazione, che consentono di visualizzare le impostazioni attuali e di modificare i parametri operativi.

Visualizzazione della configurazione attuale:
```bash
# Show current configuration
halpi config
```

Vengono così mostrati tutti i parametri configurabili con i rispettivi valori attuali:

```
$ halpi config
 Key                       Value
 watchdog_timeout           10.0
 power_on_threshold          8.0
 solo_power_off_threshold    5.5
 led_brightness               40
 auto_restart               True
 solo_depleting_timeout      5.0
```

#### Controllo dei LED

Una delle impostazioni modificate più di frequente è la luminosità dei LED, che può essere adattata ai diversi ambienti di utilizzo e alle preferenze personali.

Esempi di comandi per la gestione della luminosità dei LED:
```bash
# Get current LED brightness (0-255)
halpi config get led_brightness

# Set LED brightness to low level for night operation
halpi config set led_brightness 40

# Set moderate brightness
halpi config set led_brightness 64

# Turn LEDs off completely
halpi config set led_brightness 0

# Maximum brightness for daylight operation
halpi config set led_brightness 255
```

La luminosità dei LED accetta valori da 0 (completamente spenti) a 255 (luminosità massima), consentendo un controllo preciso degli indicatori LED del pannello frontale.

#### Gestione dell’alimentazione

Lo strumento da riga di comando HALPI offre le funzioni essenziali di gestione dell’alimentazione per un funzionamento sicuro del sistema.

Esempi di comandi per la gestione dell’alimentazione:
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

Il comando di spegnimento garantisce che il sistema si spenga in sicurezza, consentendo al sistema operativo di chiudere le applicazioni e di smontare correttamente i file system prima che il controller interrompa l’alimentazione.

#### Accesso all’API REST

Per utenti esperti e applicazioni personalizzate, il demone HALPI mette a disposizione anche un’interfaccia API REST accessibile tramite socket di dominio Unix. Ciò consente un accesso programmatico più rapido ai dati di sistema:

Di seguito alcuni esempi d’uso:
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

L’API REST è particolarmente utile per le applicazioni di monitoraggio, i sistemi di registrazione dei dati o l’integrazione con altro software che necessita di accesso in tempo reale alle informazioni di stato di HALPI2.

La documentazione completa dell’API REST è disponibile nel capitolo [Sviluppo software: demone](../software-development/daemon.md).

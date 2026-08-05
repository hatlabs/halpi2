---
translated_from: e4d4a4c5108676be9c19bdd2a82a321b24b14191
---

# Introduzione

HALPI2 è un computer di bordo pronto all’uso basato sul Raspberry Pi Compute Module 5 (CM5). Offre un insieme completo di funzionalità adatte ad applicazioni nautiche, automobilistiche e a molte applicazioni industriali.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Link al negozio"
    Acquistare HALPI2 dal [negozio online Hatlabs](https://shop.hatlabs.fi/products/halpi2-computer).

## Che cos’è HALPI2?

HALPI2 rappresenta l’ultima evoluzione dell’informatica embedded robusta e unisce la potenza e l’ecosistema di Raspberry Pi a funzionalità specifiche per ambienti gravosi. A differenza dei normali computer a scheda singola, HALPI2 è progettato fin dall’origine per il funzionamento 24 ore su 24 e 7 giorni su 7 in condizioni difficili, dove l’affidabilità è essenziale.

Il sistema integra un Raspberry Pi Compute Module 5 con una scheda portante (carrier board) dedicata, il tutto alloggiato in una custodia in alluminio impermeabile che funge anche da dissipatore di calore. Questa soluzione offre la potenza di calcolo necessaria alle applicazioni moderne, mantenendo al tempo stesso la robustezza richiesta dall’uso nautico e industriale.

## Caratteristiche e funzionalità principali

### Caratteristiche della custodia

- **Custodia in alluminio impermeabile (IP65)**, dimensioni 200 × 130 × 60 mm
- **Connettori standard** per alimentazione, NMEA 2000, ethernet gigabit, HDMI, 2× USB 3.0 e antenna WiFi/Bluetooth
- **Connettività flessibile** con possibilità di scelta tra 3× pressacavi PG7 e connettori impermeabili SP13
- **Supporto per antenne esterne** tramite aperture per 2 connettori SMA aggiuntivi
- **Progettazione per montaggio a parete** con connettori posizionati per un’installazione semplice

![Disposizione dei connettori dell’HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Caratteristiche hardware

- **Ampio intervallo di tensione di ingresso** da 10 a 32 V CC, con protezione fino a 100 V CC
- **Limitazione di corrente intelligente**: corrente di ingresso massima di 0,9 o 2,5 A, selezionabile dall’utente
- **Doppia opzione di alimentazione**: collegamento diretto a 12 V/24 V oppure alimentazione dal bus NMEA 2000 a 12 V
- **Backup a supercondensatori** per l’immunità ai disturbi e per lo spegnimento controllato in caso di mancanza di alimentazione
- **Gestione avanzata dell’alimentazione** con rilevamento automatico della mancanza di alimentazione
- **Raffreddamento passivo** con il CM5 a contatto diretto con la custodia
- **Archiviazione ad alta velocità** tramite interfaccia standard M.2 per unità SSD NVMe
- **Possibilità di espansione** tramite il connettore GPIO a 40 pin standard Raspberry Pi
- **Ampia dotazione di I/O**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, ethernet gigabit
- **Interfacce specifiche per la nautica**: CAN FD (NMEA 2000) e RS-485 (NMEA 0183)
- **Orologio in tempo reale (RTC)** con batteria tampone per una misura precisa del tempo
- **Indicazione visiva dello stato** tramite cinque LED RGB
- **Interazione con l’utente** tramite connettori a pettine per pulsanti configurabili

![Vista interna dell’HALPI2](./halpi2-interior.jpg)
*Vista interna dell’HALPI2, con la scheda portante e i vari connettori.*

### Caratteristiche software

- **Immagini di sistema operativo preconfigurate**, pronte per l’uso immediato: [HaLOS](https://docs.halos.fi) (predefinita), OpenPlotter, Raspberry Pi OS e Raspberry Pi OS Lite
- **Monitoraggio completo** di tensione, corrente e temperatura
- **Aggiornamenti del firmware trasparenti** tramite interfaccia I2C

## Applicazioni tipiche

### Applicazioni nautiche

- **Sistemi di navigazione** con plotter cartografici (chartplotter) e integrazione GPS
- **Registrazione dei dati** di parametri motore, sensori ambientali e prestazioni dell’imbarcazione
- **Server Signal K** per la gestione unificata dei dati di bordo
- **Elaborazione di bordo generica** per l’accesso a internet e la comunicazione
- **Diagnostica della rete NMEA 2000** per una maggiore affidabilità del sistema

### Applicazioni industriali

- **Monitoraggio di processo** e sistemi di controllo
- **Rilevamento ambientale** e acquisizione dati
- **Stazioni di monitoraggio remoto**
- **Automazione e controllo** delle apparecchiature
- **Sistemi di manutenzione predittiva**

### Applicazioni automobilistiche

- **Sistemi di gestione della flotta**
- **Telematica** e tracciamento dei veicoli
- **Sistemi di infotainment** a bordo veicolo
- **Piattaforme di diagnostica e monitoraggio**

## Contenuto della confezione

La confezione dell’HALPI2 comprende:

- **Unità HALPI2** con Compute Module 5 e unità SSD NVMe preinstallati (salvo ordine senza)
- **Cavo di alimentazione** con connettore E7T (compatibile Amphenol LTW Ceres Mini), lunghezza 2 m
- **Spina volante E7T** per installazioni personalizzate
- **Coppia di connettori cilindrici (barrel) CC** da 5,5 × 2,1 mm, per l’uso con alimentatori standard da 12 V/24 V
- **Antenna Raspberry Pi** per la connettività WiFi e Bluetooth
- **3 pressacavi PG7** per interfacce aggiuntive
- **Guida rapida e documentazione di garanzia** per iniziare

![Contenuto della busta accessori dell’HALPI2](./goodie-bag-contents.jpg)

Accessori aggiuntivi disponibili separatamente:

- **Cavo di derivazione NMEA 2000** per applicazioni alimentate dal bus
- **Vari kit di connettori** per installazioni personalizzate

## Come utilizzare questa documentazione

Questa documentazione è strutturata per rispondere sia alle esigenze degli utenti finali che cercano indicazioni pratiche, sia a quelle degli sviluppatori professionisti che necessitano di informazioni tecniche dettagliate.

### Per gli utenti finali

- Iniziare dalla **Guida introduttiva** per la configurazione e l’installazione
- Consultare i **Casi d’uso comuni** per indicazioni specifiche per applicazione
- Fare riferimento alla **Risoluzione dei problemi** in caso di anomalie

### Per gli sviluppatori

- Esaminare il **Riferimento tecnico** per le specifiche dettagliate
- Studiare le sezioni **Sviluppo software** per le applicazioni personalizzate
- Consultare i **File di progetto** per la pianificazione dell’integrazione
- Fare riferimento alla **Configurazione avanzata** per l’ottimizzazione delle prestazioni

### Suggerimenti per la lettura

- 💡 I riquadri **Suggerimento rapido** offrono scorciatoie per le operazioni più comuni
- ⚠️ I riquadri **Avvertenza** e **Attenzione** evidenziano informazioni importanti per la sicurezza
- 🔧 Le sezioni **Dettagli tecnici** offrono approfondimenti sull’implementazione
- 📖 I **riferimenti incrociati** collegano fra loro gli argomenti correlati in tutta la documentazione

Sia che si tratti di configurare il primo computer di bordo, sia di sviluppare una soluzione industriale personalizzata, questa documentazione accompagna passo dopo passo lungo tutta l’esperienza con HALPI2.

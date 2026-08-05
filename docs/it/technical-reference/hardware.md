---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Riferimento hardware

Questa pagina riporta le specifiche elettriche, meccaniche e ambientali dell’HALPI2. Per le informazioni procedurali (installazione, manutenzione, sostituzione), consultare la [Guida all’hardware](../user-guide/hardware.md). Per i dettagli sui protocolli delle interfacce, consultare [Interfacce e connettività](./interfaces.md).

## Riepilogo delle specifiche

| Parametro | Valore |
|:----------|:------|
| Modulo di calcolo | Raspberry Pi CM5 (compatibile con CM4) |
| Controller della scheda portante (carrier board) | RP2040 (Arm Cortex-M0+, dual core, 133 MHz) |
| Tensione di ingresso | 9–36 V CC (massimo assoluto 38,6 V, protezione dai transitori fino a 100 V) |
| Consumo di potenza | da 250 mA a riposo a 590 mA sotto carico (ingresso da 12 V, HaLOS senza monitor) |
| Impostazioni del limite di corrente | 0,9 A o 2,5 A (selezionabili) |
| Riserva a supercondensatori | 4× 25 F / 2,7 V in serie (6,25 F effettivi a 10,8 V max) |
| Temperatura di esercizio | −20 °C … +60 °C |
| Dimensioni della custodia | 200 × 130 × 60 mm (connettori esclusi) |
| Peso della custodia | TODO |
| Materiale della custodia | Alluminio pressofuso verniciato a polvere |
| Grado di protezione | IP65 |
| Licenza | CERN-OHL-S v2 (hardware) |

## Specifiche elettriche

### Alimentazione

L’alimentazione accetta un ampio intervallo di tensione di ingresso in corrente continua e fornisce le linee regolate da 5 V e 3,3 V per il CM5 e le periferiche. La protezione in ingresso comprende la protezione contro l’inversione di polarità (LM74800), la disconnessione per sovratensione a 38,6 V, il clamping TVS e il filtraggio EMI di modo comune e differenziale.

| Parametro | Valore |
|:----------|:------|
| Tensione di ingresso consigliata | 9–36 V CC |
| Tensione di ingresso massima assoluta | 38,6 V (continua), 100 V (transitoria, limitata dal TVS) |
| Corrente di ingresso massima | 0,9 A o 2,5 A (limitatore di corrente selezionabile) |
| Fusibile di ingresso | 7 A (solo protezione da guasto) |
| Linea intermedia da 10 V | 10,25 V nominali (convertitore buck SiC463ED) |
| Linea da 5 V | 5,1 V / 4 A (TPS566238, alimenta il CM5 e le porte USB) |
| Linea da 3,3 V | 3,33 V / 3 A (TPS566238, commutata dal controller sulla v0.6.0+) |
| Soglia UVLO della linea da 3,3 V | 4,5 V sul supercondensatore |
| LDO iniziale da 3,3 V | SE8633K2 (per l’avvio del controller e del bilanciatore dei supercondensatori) |

### Riserva a supercondensatori

Il banco di supercondensatori fornisce l’alimentazione di riserva per uno spegnimento controllato in caso di mancanza di alimentazione.

| Parametro | Valore |
|:----------|:------|
| Configurazione | 4× celle da 25 F / 2,7 V in serie |
| Capacità effettiva | 6,25 F a 10,8 V massimi |
| Bilanciamento | Bilanciamento attivo |
| Intervallo di tensione di carica | 0–10,8 V (monitorato dall’ADC del controller) |
| Soglia di accensione | 8,0 V (configurabile via firmware) |
| Soglia di spegnimento | 5,5 V (configurabile via firmware) |

### Consumo di corrente

Misurato con ingresso da 12 V e un Raspberry Pi CM5 che esegue l’immagine HaLOS senza monitor (headless).

| Condizione | Corrente assorbita |
|:----------|:-------------|
| Sistema a riposo | ~250 mA |
| Carico tipico | ~400 mA |
| Carico di picco | ~590 mA |

!!! note
    Queste misure escludono il consumo dei dispositivi USB esterni. Ogni porta USB 3.0 può erogare fino a 0,93 A, quindi l’assorbimento totale del sistema dipende in larga misura dalle periferiche collegate.

## Piedinature dei connettori

### Connettore di alimentazione in ingresso

Tipo Phoenix MC, passo 3,81 mm, 2 pin. Sul pannello frontale, il connettore cilindrico (barrel) E7T si collega a questo connettore a pettine.

| Pin | Funzione |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 V CC) |

### Connettore CAN FD

Tipo Phoenix MC, passo 3,81 mm, 4 pin. Isolato galvanicamente.

| Pin | Funzione |
|:----|:---------|
| 1 | GND_CAN (massa isolata) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

Il jumper di terminazione (etichetta “120R”) attiva una resistenza di terminazione da 120 Ω tra CAN_H e CAN_L.

### Connettore RS-485

Tipo Phoenix MC, passo 3,81 mm, 5 pin. Isolato galvanicamente.

| Pin | Funzione |
|:----|:---------|
| 1 | GND_RS485 (massa isolata) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Connettore a pettine dei pulsanti

Connettore a pettine 2×3 pin, passo 2,54 mm. Ogni coppia di pin per pulsante è composta da GND + segnale.

| Coppia di pin | Funzione |
|:---------|:---------|
| Power | Pulsante di accensione del CM5 (doppio clic = spegnimento, pressione prolungata = spegnimento forzato) |
| Reset | Reset hardware dell’RP2040 (pin RUN) |
| User | Configurabile dall’utente (in attesa di implementazione nel firmware) |

### Connettori HDMI (HDMI0, HDMI1)

Connettori FPC orizzontali a 20 pin, passo 0,5 mm (FPC0.5-SMT-20P). Ogni canale dispone di protezione ESD (RCLAMP0524P) e di alimentazione da 5 V a corrente limitata (AP2553W6-7).

### Connettori MIPI CSI/DSI (MIPI0, MIPI1)

Connettori FPC orizzontali a 22 pin, passo 0,5 mm. Ogni canale dispone di protezione ESD (RCLAMP0524P). Compatibili con i moduli fotocamera e display Raspberry Pi.

### Slot M.2 NVMe (PCIe M.2 M-key)

Socket M.2 di tipo M per unità SSD NVMe, con supporto dei formati da 2230 a 2280. Collegato tramite PCIe Gen 2 x1. Include un oscillatore SUSCLK dedicato per la compatibilità con la sospensione e la ripresa NVMe (aggiunto nella v0.6.1).

### Connettori per ventola (CM5 Fan)

Connettori per ventola PWM a 4 pin (HC-1.0-4PLT) presenti sia sul lato superiore sia su quello inferiore della scheda portante. Sono collegati in parallelo: utilizzarne uno solo alla volta.

| Pin | Funzione |
|:----|:---------|
| 1 | +5V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### Porte USB 3.0

| Connettore | Collegamento | Limite di corrente |
|:----------|:-----------|:-------------|
| USB3-0 | Diretto all’USB 3.0 del CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | Porta 1 dell’hub USB3 (UPD720210) | 0,93 A |
| USB3-1-1 | Porta 2 dell’hub USB3 | 0,93 A |
| USB3-1-2 | Porta 3 dell’hub USB3 | 0,93 A |

Tutte le porte dispongono di protezione ESD (RCLAMP0524P) e di filtraggio con perline di ferrite.

### Porta USB del controller (MCU USB)

Presa Micro-USB, solo in modalità periferica USB 2.0. Utilizzata per aggiornare il firmware dell’RP2040 (flashare un’immagine UF2). Protetta da ESD (RCLAMP0524P).

### Porta di avvio USB (USB Boot)

Presa USB Type-C, modalità periferica USB 2.0. Collegata alla porta USB 2.0 OTG del CM5 per l’avvio da memoria di massa USB. Protetta da ESD (RCLAMP0524P).

## Connettore GPIO a 40 pin (Raspberry Pi GPIO Header)

Il connettore GPIO a pettine segue il layout standard Raspberry Pi a 40 pin. I pin seguenti sono utilizzati dalle periferiche integrate dell’HALPI2:

| GPIO | Pin | Funzione | Interfaccia | Condiviso? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | I2C di sistema | Sì (indirizzo 0x6d riservato) |
| 3 | 5 | I2C1 SCL | I2C di sistema | Sì (indirizzo 0x6d riservato) |
| 6 | 31 | SPI0 CS | Controller CAN FD | CS personalizzato: può coesistere con i pin CS standard |
| 9 | 21 | SPI0 MISO | Controller CAN FD | Bus SPI0 condiviso |
| 10 | 19 | SPI0 MOSI | Controller CAN FD | Bus SPI0 condiviso |
| 11 | 23 | SPI0 SCLK | Controller CAN FD | Bus SPI0 condiviso |
| 12 | 32 | UART4 TX | RS-485 | Libero se RS-485 è disattivato |
| 13 | 33 | UART4 RX | RS-485 | Libero se RS-485 è disattivato |
| 24 | 18 | RS-485 EN | RS-485 (modalità manuale) | Libero in modalità automatica |
| 26 | 37 | CAN INT | Controller CAN FD | No |

Tutti i restanti pin GPIO sono disponibili per gli HAT e per le applicazioni dell’utente. Consultare la [Guida all’hardware](../user-guide/hardware.md#uso-degli-hat) per i dettagli sulla compatibilità degli HAT e per le istruzioni su come disattivare le interfacce integrate.

## Dispositivi I2C

Il bus I2C di sistema (I2C1, GPIO 2/3) ospita i dispositivi seguenti:

| Indirizzo | Dispositivo | Funzione |
|:--------|:-------|:---------|
| 0x4b | TMP112A | Sensore di temperatura della scheda |
| 0x6d | RP2040 | Controller della scheda portante (modalità secondaria) |

Il bus I2C del controller (I2C0, interno alla scheda portante) è utilizzato per la comunicazione DDC HDMI e con i display MIPI, con pull-up da 2,2 kΩ.

## Architettura di isolamento

Le interfacce CAN FD e RS-485 sono isolate galvanicamente dal resto del sistema. Ogni interfaccia dispone di alimentazione isolata indipendente (convertitore CC-CC B0505S-1WR3) e di isolamento dei segnali.

| Interfaccia | Isolamento dei segnali | Isolamento dell’alimentazione | Massa isolata |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Ciò significa che guasti del bus, anelli di massa e disturbi sulle reti CAN o RS-485 non possono danneggiare il sistema principale né interferire con esso.

## Specifiche meccaniche

### Custodia

| Parametro | Valore |
|:----------|:------|
| Materiale | Alluminio pressofuso verniciato a polvere |
| Dimensioni | 200 × 130 × 60 mm (connettori esclusi) |
| Peso | TODO |
| Grado di protezione IP | IP65 |
| Spazio interno sopra la scheda portante | 45 mm (consente fino a 2 HAT sovrapposti) |
| Viti del coperchio | 4× M4×10 svasate, testa PH2 |
| Guarnizione | Guarnizione del coperchio per la tenuta agli agenti atmosferici |
| Compensazione della pressione | Tappo di compensazione (non deve essere rimosso) |

### Posizioni sul pannello

Il pannello frontale comprende posizioni predisposte per:

- 1× connettore di alimentazione E7T
- 1× connettore NMEA 2000 Micro-C
- 1× Ethernet RJ45
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× connettore per antenna RP-SMA (per Wi-Fi/Bluetooth)
- 2× posizioni per antenna SMA (fornite con tappi ciechi)
- 1× tappo di compensazione
- 3× posizioni per pressacavo PG7 (fornite con tappi ciechi)

### Montaggio

- Montaggio della scheda portante: 4× viti M4×6 fissate alla base della custodia
- Montaggio degli HAT: 4× inserti filettati M2,5 (v0.5.0+; la v0.4.0 richiede l’installazione manuale dei dadi)
- Montaggio del CM5: 4× dadi da saldare M2,5

## Gestione termica

Il CM5 è montato sul lato inferiore della scheda portante. Il calore viene trasferito dal SoC e dal chipset RP1 del CM5 attraverso pad termici alla base in alluminio della custodia, che funge da dissipatore di calore.

| Componente | Spessore del pad termico |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Componenti dell’alimentazione | 2 mm |

La custodia standard offre un raffreddamento passivo senza ventola. È disponibile un connettore per ventola PWM a 4 pin per custodie personalizzate o per applicazioni con temperatura ambiente elevata.


!!! quote "Informazioni correlate"
    - **Schemi elettrici e file di progetto:** consultare [File di progetto e schemi elettrici](../appendices/design-files.md)
    - **Comportamento della gestione dell’alimentazione:** consultare [Approfondimento sull’alimentazione](./power-supply.md)
    - **Protocolli delle interfacce:** consultare [Interfacce e connettività](./interfaces.md)
    - **Controller e protocollo I2C:** consultare [Controller della scheda portante](./controller.md)
    - **Installazione fisica:** consultare [Guida all’hardware](../user-guide/hardware.md)

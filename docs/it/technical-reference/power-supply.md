---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# Alimentazione in dettaglio

L’alimentazione dell’HALPI2 è progettata per gli ambienti elettrici instabili di imbarcazioni e veicoli: tollera picchi e disturbi di tensione, limita la corrente di spunto e immagazzina energia sufficiente a spegnere il sistema in sicurezza quando l’alimentazione di ingresso viene a mancare.

Per le specifiche elettriche, vedere il [Riferimento hardware](./hardware.md). Per la macchina a stati che agisce sulle misure qui descritte, vedere il riferimento [Controller della scheda portante](./controller.md).

## Stadio di ingresso

L’intervallo di ingresso nominale è 10–32 V CC e copre sia gli impianti a 12 V sia quelli a 24 V. Lo stadio di ingresso è protetto contro l’inversione di polarità e contro i transitori di sovratensione fino a 100 V, come i load dump dell’alternatore.

### Limitazione di corrente

Un limitatore di corrente in ingresso controlla la corrente massima assorbita dalla sorgente, selezionabile tra 0,9 A e 2,5 A direttamente sulla scheda portante (carrier board). Il limite ha due scopi:

- Contiene la corrente di spunto quando i supercondensatori scarichi iniziano a caricarsi all’accensione.
- Mantiene l’assorbimento totale entro il bilancio di potenza della sorgente — con l’impostazione da 0,9 A (LEN 18) l’HALPI2 può essere alimentato in sicurezza dal bus NMEA 2000.

L’impostazione predefinita è 0,9 A. Selezionare 2,5 A quando il sistema alimenta periferiche ad alto assorbimento o quando si desidera un avvio più rapido. La posizione del limitatore e la procedura per modificare l’impostazione sono descritte nella [Guida all’hardware](../user-guide/hardware.md#configurazione-della-limitazione-di-corrente).

## Riserva a supercondensatori

Un banco di supercondensatori fornisce l’energia di riserva per gli spegnimenti controllati. A differenza di un UPS a batteria, i supercondensatori non si usurano, funzionano nell’intero intervallo di temperatura e si caricano in pochi secondi — al prezzo di una riserva di energia molto più piccola.

### Carica

I supercondensatori si caricano ogni volta che l’alimentazione di ingresso è presente. Partendo da scarichi, la carica richiede circa:

- 25 secondi con il limite di corrente da 0,9 A
- 9 secondi con il limite di corrente da 2,5 A

I LED del pannello frontale mostrano l’avanzamento della carica come una barra rossa che si riempie. Il Compute Module viene acceso quando la tensione dei supercondensatori raggiunge la soglia di accensione (predefinita 8,0 V).

### Durata della riserva

Quando l’alimentazione di ingresso viene a mancare, i supercondensatori sostengono l’intero carico del sistema. Forniscono 30–60 secondi di autonomia, a seconda del carico del sistema e delle periferiche collegate — un tempo sufficiente, con margine, per uno spegnimento controllato del sistema operativo.

!!! warning "Non è un UPS"
    Il sistema a supercondensatori è progettato per coprire i disturbi brevi e per alimentare uno spegnimento sicuro. Non è progettato per continuare a funzionare durante interruzioni prolungate.

## Rilevamento della mancanza di alimentazione

Il controller misura continuamente la tensione di ingresso e considera assente l’alimentazione di ingresso quando la tensione scende sotto 9,0 V. Un timer di interruzione di corrente (predefinito 5 secondi) evita lo spegnimento per le interruzioni brevi: i supercondensatori coprono l’intervallo e il funzionamento prosegue senza interruzioni se l’alimentazione ritorna in tempo. Le interruzioni più lunghe attivano le sequenze di spegnimento automatico descritte nel riferimento [Controller della scheda portante](./controller.md#mancanza-di-alimentazione-e-sequenze-di-spegnimento).

## Monitoraggio

Il controller misura la tensione di ingresso, la corrente di ingresso e la tensione dei supercondensatori, e le espone tramite il demone HALPI:

```bash
halpi status
```

I valori sono disponibili anche in modo programmatico tramite l’API REST del demone — vedere la [Guida al software](../user-guide/software.md#accesso-allapi-rest).

!!! quote "Informazioni correlate"
    - **Specifiche elettriche:** vedere [Riferimento hardware](./hardware.md)
    - **Macchina a stati e sequenze di spegnimento:** vedere [Controller della scheda portante](./controller.md)
    - **Comportamento dell’alimentazione nell’uso quotidiano:** vedere [Uso quotidiano](../user-guide/operation.md)

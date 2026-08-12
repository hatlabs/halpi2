---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Uso quotidiano

L’HALPI2 è progettato per il funzionamento non presidiato. Con l’immagine HaLOS preinstallata — o con qualsiasi sistema operativo in cui sia installato il [demone HALPI](./software.md#strumento-da-riga-di-comando-halpi) — la gestione dell’alimentazione è automatica: il dispositivo carica i supercondensatori di riserva, supera senza interruzioni i disturbi di tensione, spegne in sicurezza il sistema operativo quando l’alimentazione viene a mancare e si riavvia quando l’alimentazione ritorna. Nulla di tutto ciò richiede l’intervento dell’utente.

## Accensione

L’HALPI2 non ha un pulsante di accensione sulla custodia: si avvia non appena viene collegata l’alimentazione di ingresso. (È possibile collegare un pulsante di accensione esterno alla scheda portante — vedere [Pulsanti esterni](./interfaces.md#pulsanti-esterni).) La barra dei LED si riempie dapprima di rosso mentre i supercondensatori si caricano (da alcuni secondi a mezzo minuto, a seconda dell’[impostazione del limite di corrente](./hardware.md#configurazione-della-limitazione-di-corrente)). I LED riproducono quindi una breve animazione arcobaleno con ciclo di colori mentre il Compute Module si avvia, mostrano una barra gialla durante l’avvio del sistema operativo e diventano verdi quando il sistema operativo è in esecuzione e il demone HALPI si è connesso.

## Spegnimento

Per spegnere l’HALPI2, togliere l’alimentazione di ingresso — ad esempio con un interruttore del quadro elettrico. Il sistema rileva la mancanza di alimentazione, spegne il sistema operativo in modo controllato alimentandosi dai supercondensatori e resta spento. I LED mostrano una barra viola durante lo spegnimento e si spengono al termine.

È anche possibile spegnere il sistema da software — tramite il menu del desktop, il comando `shutdown` o `halpi shutdown`. Il sistema si spegne e resta spento finché l’alimentazione di ingresso non viene tolta e ridata (oppure finché non viene premuto un [pulsante di accensione esterno](./interfaces.md#pulsanti-esterni), se presente).

In via opzionale, il controller può riavviare automaticamente il sistema circa 5 secondi dopo uno spegnimento da software se l’alimentazione di ingresso resta collegata, in modo che un comando di spegnimento accidentale non lasci mai fuori uso un’installazione difficile da raggiungere fisicamente. La funzione si abilita con `halpi config set auto_restart true`; l’impostazione viene conservata nel controller. Le unità prodotte prima dell’inizio del 2026 venivano fornite con questo comportamento abilitato — per verificare la propria unità, eseguire `halpi config get auto_restart`.

Il sistema può anche essere messo in standby, in cui si spegne e si riattiva a un orario programmato — vedere il riferimento [Controller della scheda portante](../technical-reference/controller.md#standby).

## Indicatori LED di stato

I cinque LED del pannello frontale mostrano che cosa sta facendo il sistema:

| Sequenza dei LED | Significato |
|:-----------------|:------------|
| Barra rossa che si riempie | Supercondensatori in carica prima dell’avvio — attendere |
| Arcobaleno e ciclo di colori | Compute Module in avvio. Se la sequenza si ripete senza progressi, l’avvio del modulo non è riuscito — vedere [Risoluzione dei problemi](./troubleshooting.md#led-con-sequenza-arcobaleno) |
| Barra gialla | Sistema in esecuzione, demone HALPI non connesso — normale per un breve periodo durante l’avvio. Se persiste, vedere [Risoluzione dei problemi](./troubleshooting.md#i-led-restano-gialli) |
| Barra verde | Funzionamento normale |
| Barra arancione o verde scuro | Alimentazione di ingresso assente, funzionamento con l’alimentazione di riserva — segue lo spegnimento, a meno che l’alimentazione non ritorni entro pochi secondi |
| Barra viola | Spegnimento in corso |
| Tutti rossi fissi | Sistema operativo che non risponde — il controller lo riavvierà automaticamente |
| Tutti rossi lampeggianti | Guasto dei supercondensatori — contattare l’assistenza |
| Tutti blu fissi | Passaggio allo standby in corso |
| Tutti rossi attenuati | Standby |
| Tutti spenti | Sistema spento |

Nelle sequenze a barra, il numero di LED accesi indica il livello di carica dei supercondensatori. Le finestre di tensione esatte e la mappatura completa degli stati si trovano nel riferimento [Controller della scheda portante](../technical-reference/controller.md#riferimento-dei-led-di-stato).

La luminosità dei LED è regolabile — vedere [Controllo dei LED](./software.md#controllo-dei-led). Con il componente aggiuntivo [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights) i LED possono anche essere riutilizzati come display per metriche di sistema e dati nautici (attività di rete, livelli dei serbatoi, valori NMEA 2000 e Signal K).

## In caso di mancanza di alimentazione

Non occorre fare nulla. I cali e i disturbi brevi — fino a 5 secondi per impostazione predefinita — vengono coperti dai supercondensatori e il funzionamento prosegue senza interruzioni. In caso di interruzione più lunga, il sistema si spegne da solo in modo controllato sfruttando i 30–60 secondi di alimentazione di riserva immagazzinata nei supercondensatori. Quando l’alimentazione di ingresso ritorna, il sistema si riavvia automaticamente.

!!! warning "Non è un UPS"
    I supercondensatori servono a coprire i disturbi brevi e ad alimentare uno spegnimento sicuro. Per continuare a funzionare durante interruzioni prolungate è necessario un gruppo di continuità (UPS) esterno.

## Verifica dello stato del sistema

Una barra LED verde indica che il sistema è in buono stato. Per i dettagli, il comando `halpi` mostra lo stato del controller, le tensioni, la corrente e le temperature:

```bash
halpi status
```

Se qualcosa non sembra corretto, vedere [Risoluzione dei problemi](./troubleshooting.md) e la [Guida al software](./software.md#strumento-da-riga-di-comando-halpi).

## Funzionamento senza il demone

Sui sistemi operativi privi del demone HALPI, il controller ricorre a una modalità di protezione di base: rileva comunque la mancanza di alimentazione e richiede lo spegnimento, ma simulando pressioni del pulsante di accensione — il che non funziona se il sistema è bloccato — e il monitoraggio e la configurazione non sono disponibili. Se si utilizza un sistema operativo personalizzato, installare il demone; vedere [Altre distribuzioni Debian](../software-development/ubuntu-installation.md). Il funzionamento delle due modalità è descritto nel riferimento [Controller della scheda portante](../technical-reference/controller.md#modalita-di-funzionamento).

!!! quote "Informazioni correlate"
    - **Funzionamento interno della gestione dell’alimentazione:** vedere [Controller della scheda portante](../technical-reference/controller.md)
    - **Dettagli sul sistema di alimentazione:** vedere [Alimentazione in dettaglio](../technical-reference/power-supply.md)
    - **Il comando `halpi` e il demone:** vedere [Guida al software](./software.md)
    - **Problemi:** vedere [Risoluzione dei problemi](./troubleshooting.md)

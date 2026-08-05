# File di progetto e schemi elettrici

Questa pagina mette a disposizione gli schemi elettrici e i file di progetto meccanico dell’HALPI2.

Il progetto elettrico dell’HALPI2 è realizzato in KiCad. I file di progetto sono disponibili nel [repository GitHub](https://github.com/hatlabs/HALPI2-hardware). A ogni versione rilasciata corrisponde un tag nel repository.

Gli schemi elettrici sono forniti per comodità come file PDF qui di seguito. I progetti di layout del PCB sono disponibili solo nel repository GitHub.

I file di progetto meccanico sono inizialmente forniti solo per la custodia. Il progetto è stato realizzato con Autocad Fusion, ma i file esportati in formato STEP sono leggibili dalla maggior parte dei software CAD.

## Versione 0.6.1

Una release correttiva che introduce miglioramenti di integrità del segnale e di messa a terra individuati durante i collaudi di produzione.

Modifiche:

- Aggiunta di un oscillatore di clock per NVMe SUSCLK, per risolvere problemi di compatibilità con alcune unità SSD NVMe
- Aggiunta dei condensatori mancanti alle coppie differenziali RX dell’hub USB3
- Messa a terra in corrispondenza di ogni punto di fissaggio

### File di progetto

- File di progetto KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- Schema elettrico in PDF: [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Versione 0.6.0

La terza release di produzione dell’HALPI2, con ulteriori correzioni minori alla scheda portante (carrier board). Le caratteristiche della scheda restano invariate rispetto alla versione 0.5.0.

Modifiche:

- L’uscita della linea da 3,3 V è ora commutata dal controller anziché essere sempre attiva
- Aggiunta di punti di test per migliorare i collaudi di produzione
- Nuovo instradamento delle interfacce HDMI, MIPI e USB3 per una migliore integrità del segnale
- I connettori FFC a bordo scheda sono ora orizzontali
- Migliorata la stabilità del convertitore buck da 10 V: non emette più fischi in nessuna condizione
- Riprogettazione del circuito di bilanciamento dei supercondensatori con un unico amplificatore operazionale a 4 unità
- Alcune impronte dei componenti sono state modificate per migliorarne la reperibilità

### File di progetto

- File di progetto KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Schema elettrico in PDF: [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Versione 0.5.0

La seconda release di produzione dell’HALPI2, con correzioni minori alla scheda portante. Le funzionalità della scheda restano invariate rispetto alla versione 0.4.0.

Modifiche:

- Corretti piccoli errori nella serigrafia
- Rimossi i riempimenti di rame a 3,3 V dallo strato inferiore, in prossimità delle strutture di fissaggio
- Aggiunti dadi da saldare per facilitare il montaggio degli HAT
- Aggiunti dadi da saldare per un fissaggio più sicuro del Compute Module
- Ripristinati i connettori a pettine dei jumper in tecnologia THT, per una maggiore resistenza meccanica
- Aggiunto un LED di alimentazione dedicato per +5 V
- Bilanciamento dei supercondensatori reso meno stringente
- Riorganizzati i connettori a pettine dei jumper per una migliore usabilità

### File di progetto

- File di progetto KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Schema elettrico in PDF: [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- Modello 3D della custodia: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (identico a quello della versione 0.4.0)

## Versione 0.4.0

La prima release pubblica dell’HALPI2.

### File di progetto

- File di progetto KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Schema elettrico in PDF: [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- Modello 3D della custodia: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

# Interfacce e connettività

Questa pagina documenta come le interfacce del CM5 vengono rese disponibili sulla
scheda portante (carrier board) di HALPI2. Per l’uso quotidiano delle porte CAN FD
e RS-485 integrate, vedere la guida utente [Interfacce e connettività](../user-guide/interfaces.md).

## Porte seriali (UART)

Il Compute Module 5 raggiunge il connettore a pettine a 40 pin tramite il proprio
controllore di I/O RP1, che espone cinque UART (`uart0`–`uart4`). Ogni UART è
cablata a una coppia fissa di GPIO: a differenza dei modelli Pi precedenti, i pin
non possono essere rimappati. La console di accesso è una UART di debug dedicata
e separata (`/dev/ttyAMA10`) e non rientra tra queste.

| UART | TX / RX | Pin del connettore | Dispositivo Linux | Disponibilità su HALPI2 |
|:-----|:--------|:------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Libera. Porta seriale HAT convenzionale; utilizzata dagli HAT GNSS. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Libera. Sono i pin della EEPROM di identificazione degli HAT (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Libera. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Utilizzata dal controllore CAN FD (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Utilizzata da RS-485. |

### Abilitare una UART

Aggiungere l’overlay `-pi5` corrispondente a `/boot/firmware/config.txt` e riavviare:

```
dtoverlay=uart2-pi5
```

`uart0` si abilita invece con `dtparam=uart0=on`. (Su un CM5 il firmware
reindirizza i normali overlay `uartN` ai rispettivi equivalenti `uartN-pi5`,
quindi funzionano entrambi i nomi; qui si utilizza la forma `-pi5` per chiarezza.)

Il controllo di flusso hardware va abilitato esplicitamente con il parametro
`ctsrts`; gli overlay possono inoltre pilotare direttamente la linea di
abilitazione di un transceiver RS-485 con il parametro `rs485`:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS occupano la coppia di GPIO successiva, che su HALPI2 è spesso già in uso:

| UART | CTS / RTS | In conflitto con |
|:-----|:----------|:---------------|
| `uart1` | GPIO2 / 3 | Bus I2C di sistema (I2C1) |
| `uart2` | GPIO6 / 7 | Chip select del CAN FD |
| `uart3` | GPIO10 / 11 | Bus SPI del CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

`uart1` è quindi utilizzabile in pratica solo come porta con soli TX/RX.

### Liberare una UART occupata

`uart3` e `uart4` si sovrappongono alle interfacce CAN FD e RS-485 integrate:

- **`uart3`** condivide il bus SPI0 con il controllore CAN FD: il pin GPIO9 è
  l’uscita dati del controllore (SDO). L’utilizzo di `uart3` richiede la
  disabilitazione dell’interfaccia CAN e una modifica hardware, e non è
  supportato sulla scheda standard.
- **`uart4`** è la porta RS-485. Rimuovendo il jumper di abilitazione della
  ricezione presente sulla scheda si scollega il ricevitore RS-485 dal pin
  GPIO13, liberando `uart4` per un uso generico. RS-485 non risulta più
  disponibile.

Vedere [Disabilitazione delle interfacce integrate](../user-guide/hardware.md#using-hats)
per i passaggi hardware.

### Verifica

Dopo il riavvio, verificare che il nodo di dispositivo esista e che i pin
svolgano la funzione prevista:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

I pin selezionati devono riportare la propria funzione UART (`a2` per
`uart1`–`uart4`, `a4` per `uart0`).

## Altri argomenti

- Dettagli di implementazione di NMEA 2000
- Specifiche USB 3.0 e gestione dell’alimentazione
- Ethernet e rete
- Requisiti di archiviazione M.2 NVMe

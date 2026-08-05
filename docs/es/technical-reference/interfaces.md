---
translated_from: 9497de10027831b20a1e2278a32df0c12d9a4a39
---

# Interfaces y conectividad

En esta página se documenta cómo se exponen las interfaces del CM5 en la placa
portadora del HALPI2. Para el uso cotidiano de los puertos CAN FD y RS-485
integrados, véase la guía de usuario [Interfaces y conectividad](../user-guide/interfaces.md).

## Puertos serie (UART)

El Compute Module 5 llega al conector GPIO de 40 pines a través de su controlador
de E/S RP1, que expone cinco UART (`uart0`–`uart4`). Cada UART está cableada a un
par fijo de GPIO — a diferencia de los modelos anteriores de Pi, los pines no se
pueden reasignar. La consola de inicio de sesión es una UART de depuración
dedicada e independiente (`/dev/ttyAMA10`) y no es ninguna de estas.

| UART | TX / RX | Pines del conector | Dispositivo Linux | Disponibilidad en el HALPI2 |
|:-----|:--------|:------------|:-------------|:-----------------------|
| `uart0` | GPIO14 / 15 | 8 / 10 | `/dev/ttyAMA0` | Libre. Puerto serie convencional de los HAT; se usa en los HAT de GNSS. |
| `uart1` | GPIO0 / 1 | 27 / 28 | `/dev/ttyAMA1` | Libre. Son los pines de la EEPROM de identificación del HAT (ID_SD / ID_SC). |
| `uart2` | GPIO4 / 5 | 7 / 29 | `/dev/ttyAMA2` | Libre. |
| `uart3` | GPIO8 / 9 | 24 / 21 | `/dev/ttyAMA3` | Ocupada por el controlador CAN FD (SPI0). |
| `uart4` | GPIO12 / 13 | 32 / 33 | `/dev/ttyAMA4` | Ocupada por RS-485. |

### Activación de una UART

Añadir el overlay `-pi5` correspondiente a `/boot/firmware/config.txt` y reiniciar:

```
dtoverlay=uart2-pi5
```

`uart0` se activa en cambio con `dtparam=uart0=on`. (En un CM5, el firmware
redirige los overlays `uartN` simples a sus equivalentes `uartN-pi5`, por lo que
sirve cualquiera de los dos nombres; aquí se emplea la forma `-pi5` por claridad.)

El control de flujo por hardware es opcional y se activa con el parámetro
`ctsrts`; además, los overlays pueden gobernar directamente la línea de
habilitación de un transceptor RS-485 con el parámetro `rs485`:

```
dtoverlay=uart2-pi5,ctsrts
```

CTS/RTS ocupan el siguiente par de GPIO, que en el HALPI2 suele estar ya en uso:

| UART | CTS / RTS | Conflicto con |
|:-----|:----------|:---------------|
| `uart1` | GPIO2 / 3 | Bus I2C del sistema (I2C1) |
| `uart2` | GPIO6 / 7 | Chip-select del CAN FD |
| `uart3` | GPIO10 / 11 | Bus SPI del CAN FD |
| `uart4` | GPIO14 / 15 | `uart0` |

Por tanto, `uart1` solo resulta práctica como puerto de solo TX/RX.

### Liberación de una UART ocupada

`uart3` y `uart4` se solapan con las interfaces CAN FD y RS-485 integradas:

- **`uart3`** comparte el bus SPI0 con el controlador CAN FD — GPIO9 es la
  salida de datos (SDO) del controlador. Usar `uart3` exige desactivar la
  interfaz CAN y una modificación de hardware, y no está admitido en la placa
  estándar.
- **`uart4`** es el puerto RS-485. Retirar el puente (jumper) de habilitación de
  recepción de la placa desconecta el receptor RS-485 del GPIO13 y libera
  `uart4` para uso general. RS-485 queda entonces no disponible.

Los pasos de hardware figuran en [Desactivación de las interfaces integradas](../user-guide/hardware.md#uso-de-hat).

### Comprobación

Tras reiniciar, comprobar que el nodo de dispositivo existe y que los pines
tienen la función esperada:

```
ls /dev/ttyAMA*
pinctrl funcs | grep -iE 'txd|rxd'
pinctrl 4 5
```

Los pines seleccionados deben indicar su función UART (`a2` para `uart1`–`uart4`,
`a4` para `uart0`).

## Otros temas

- Detalles de implementación de NMEA 2000
- Especificaciones de USB 3.0 y gestión de la alimentación
- Ethernet y redes
- Requisitos de almacenamiento M.2 NVMe

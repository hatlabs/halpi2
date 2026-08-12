---
translated_from: 0dea1c6b57ea6c3cf1af4e1d138e07ce80dacefa
---

# Controlador de la placa portadora

La placa portadora del HALPI2 incluye un microcontrolador RP2040 que gestiona la alimentación, supervisa el sistema y controla los LED del panel frontal. El controlador funciona con independencia del Compute Module: opera desde el momento en que se conecta la alimentación de entrada, antes de que arranque el sistema operativo y después de que se apague. El Compute Module se comunica con él por I2C (bus 1, dirección `0x6d`) a través del [demonio HALPI](../user-guide/software.md#herramienta-de-linea-de-comandos-halpi).

Esta página describe los modos de funcionamiento, las transiciones de estado y la configuración del controlador. Documenta la versión de firmware 3.3.x. Para el uso cotidiano no es necesario leer nada de esto; véase en su lugar [Uso diario](../user-guide/operation.md).

## Modos de funcionamiento

El controlador funciona en uno de dos modos, según si el demonio HALPI se está comunicando con él.

### Modo cooperativo

El modo cooperativo (co-op) es el modo de funcionamiento normal. Está activo cuando el demonio HALPI (`halpid`) está en ejecución y se comunica con el controlador. La imagen HaLOS preinstalada y todas las imágenes de sistema operativo de Hat Labs incluyen el demonio.

En modo cooperativo:

- El controlador y el demonio intercambian datos en tiempo real: tensiones, corriente, temperaturas y estado.
- Los eventos de pérdida de alimentación se comunican al demonio, que inicia un apagado controlado del sistema operativo.
- El temporizador watchdog (temporizador de vigilancia) protege frente a los bloqueos del sistema operativo (véase [Protección mediante watchdog](#proteccion-mediante-watchdog)).
- La configuración puede leerse y modificarse con la herramienta de línea de comandos `halpi`.

### Modo solo

El modo solo es el modo de respaldo. El controlador entra en él cuando no hay comunicación con el demonio:

- durante el arranque, antes de que se inicie el demonio
- si el demonio no está instalado, se ha desactivado o se ha bloqueado
- en sistemas operativos sin compatibilidad con HALPI2

En modo solo, el controlador sigue protegiendo frente a la pérdida de alimentación, pero con un mecanismo más rudimentario: solicita el apagado simulando pulsaciones del botón de encendido y no puede saber si el sistema operativo ha completado realmente el apagado de forma controlada.

!!! tip "Fiabilidad del modo solo"
    El modo solo ofrece una protección esencial, pero es menos fiable que el modo cooperativo. Las pulsaciones simuladas de botón no funcionan si el sistema operativo está bloqueado. Si se utiliza un sistema operativo personalizado, conviene instalar el demonio HALPI; véase [Otras distribuciones Debian](../software-development/ubuntu-installation.md).

## Pérdida de alimentación y secuencias de apagado

El controlador supervisa la tensión de entrada de forma continua. La alimentación de entrada se considera perdida cuando la tensión de entrada cae por debajo de 9,0 V. Un temporizador de corte de corriente (5 segundos de forma predeterminada) distingue los microcortes breves de los cortes reales: los supercondensadores cubren el intervalo y, si la alimentación vuelve dentro del periodo del temporizador, no ocurre nada más.

### Secuencia de apagado en modo cooperativo

1. El demonio detecta la pérdida de alimentación a partir de las medidas de tensión del controlador.
2. El demonio espera a que transcurra el límite de tiempo de corte de corriente (5 segundos de forma predeterminada).
3. El demonio ejecuta el comando de apagado configurado (predeterminado: `/sbin/poweroff`).
4. El sistema operativo se apaga de forma controlada con la energía de los supercondensadores.
5. El controlador detecta que el Compute Module se ha apagado y desactiva la línea de 5 V.
6. Si el apagado no se completa en 60 segundos, el controlador fuerza el corte de la alimentación.
7. El sistema permanece apagado hasta que vuelve la alimentación de entrada y entonces se reinicia automáticamente.

### Secuencia de apagado en modo solo

1. El controlador detecta la pérdida de alimentación e inicia el temporizador de corte de corriente (5 segundos de forma predeterminada).
2. Cuando el temporizador expira, el controlador simula una doble pulsación del botón de encendido.
3. El sistema operativo responde e inicia un apagado controlado con la energía de los supercondensadores.
4. Si el apagado no se completa en 60 segundos, el controlador fuerza el corte de la alimentación.
5. El sistema permanece apagado hasta que vuelve la alimentación de entrada y entonces se reinicia automáticamente.

### Comportamiento del reinicio tras un apagado por software

Un apagado iniciado desde el software mientras la alimentación de entrada sigue disponible (por ejemplo, con el comando `shutdown` o desde el menú del escritorio) termina en el estado de *apagado*. Lo que ocurre a continuación depende del parámetro de configuración `auto_restart`:

- `auto_restart` desactivado (el ajuste de fábrica en las unidades producidas desde principios de 2026): el sistema permanece apagado hasta que se realiza un ciclo de la alimentación de entrada o se pulsa un botón de encendido.
- `auto_restart` activado (el valor por defecto del firmware y el ajuste de fábrica en las unidades anteriores): el controlador reinicia el sistema al cabo de 5 segundos, de modo que un sistema desatendido no se quede apagado por un apagado accidental.

El ajuste se cambia con `halpi config set auto_restart <true|false>`.

Una pulsación del botón de encendido o un ciclo de la alimentación de entrada reinician siempre el sistema, con independencia del ajuste de `auto_restart`.

## Protección mediante watchdog

En modo cooperativo, un temporizador watchdog protege frente a los bloqueos del sistema operativo:

- El demonio debe enviar al controlador una señal de alimentación del watchdog a intervalos regulares.
- Si no llega ninguna señal dentro del tiempo de espera del watchdog (10 segundos de forma predeterminada), el controlador considera que el host no responde, muestra el patrón de LED de alerta (todos los LED en rojo fijo) y realiza un ciclo de alimentación del Compute Module para recuperarlo.
- El tiempo de espera se configura con `halpi config set watchdog_timeout <seconds>`.

## Modo de reposo

El modo de reposo apaga el Compute Module mientras el controlador permanece activo, a la espera de una reactivación programada:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

Durante la transición, todos los LED se muestran en azul fijo; en el modo de reposo, en rojo tenue. El controlador reinicia el sistema a la hora programada, al pulsarse un botón de encendido o tras un ciclo de la alimentación de entrada.

## Referencia de los LED de estado

Los cinco LED RGB del panel frontal reflejan el estado del controlador. Esta tabla es la correspondencia de referencia entre los estados del controlador y los patrones de LED; la página [Uso diario](../user-guide/operation.md#indicadores-led-de-estado) presenta una versión simplificada.

| Estado del controlador | Patrón de LED |
|:-----------------------|:--------------|
| PowerOff (sin alimentación de entrada utilizable; el controlador funciona con la carga residual) | LED 5 en rojo fijo |
| OffCharging | Barra roja que se llena mientras se cargan los supercondensadores |
| SystemStartup | Barrido de arcoíris y, a continuación, un ciclo de colores fijos |
| OperationalSolo | Barra amarilla de nivel de carga |
| OperationalCoOp | Barra verde de nivel de carga |
| BlackoutSolo | Barra naranja de nivel de carga |
| BlackoutCoOp | Barra verde oscuro de nivel de carga |
| BlackoutShutdown, ManualShutdown | Barra morada de nivel de carga |
| PoweredDownBlackout, PoweredDownManual | Todos apagados |
| HostUnresponsive (tiempo de espera del watchdog agotado) | Todos en rojo fijo |
| EnteringStandby | Todos en azul fijo |
| Standby | Todos en rojo tenue |
| Alarma de sobretensión de los supercondensadores | Todos los LED parpadeando en rojo |

En los patrones de barra de nivel de carga, cada LED encendido representa un voltio de tensión de los supercondensadores:

| LED | Rango de tensión |
|:----|:-----------------|
| LED 1 | 5,0–6,0 V |
| LED 2 | 6,0–7,0 V |
| LED 3 | 7,0–8,0 V |
| LED 4 | 8,0–9,0 V |
| LED 5 | 9,0–10,0 V |

## Parámetros de configuración

La configuración se almacena en la memoria flash del controlador y se conserva entre ciclos de alimentación. Se lee y se modifica con `halpi config`; véase la [Guía del software](../user-guide/software.md#gestion-de-la-configuracion).

| Parámetro | Valor predeterminado | Descripción |
|:----------|:---------------------|:------------|
| `auto_restart` | `false` en las unidades actuales (se fija en la prueba de producción); valor por defecto del firmware: `true` | Reiniciar automáticamente 5 s después de un apagado por software mientras hay alimentación de entrada |
| `watchdog_timeout` | 10 s | Tiempo de espera del watchdog en modo cooperativo |
| `power_on_threshold` | 8,0 V | Tensión de los supercondensadores necesaria antes de encender el Compute Module |
| `solo_power_off_threshold` | 5,5 V | Tensión de los supercondensadores a la que el controlador fuerza el apagado en modo solo |
| `solo_depleting_timeout` | 5 s | Temporizador de corte de corriente del modo solo |
| `led_brightness` | 48 | Brillo de los LED del panel frontal (0–255) |

El temporizador de corte de corriente del modo cooperativo y el comando de apagado son ajustes del demonio, configurados en `/etc/halpid/halpid.conf` (`blackout-time-limit`, predeterminado 5 s; `poweroff`, predeterminado `/sbin/poweroff`).

!!! quote "Información relacionada"
    - **Uso cotidiano:** véase [Uso diario](../user-guide/operation.md)
    - **Detalles del sistema de alimentación:** véase [La alimentación en detalle](./power-supply.md)
    - **Actualizaciones de firmware:** véase la [Guía del software](../user-guide/software.md#actualizaciones-de-firmware)
    - **Código fuente del firmware y protocolo I2C:** véase el repositorio [`HALPI2-firmware`](https://github.com/hatlabs/HALPI2-firmware)

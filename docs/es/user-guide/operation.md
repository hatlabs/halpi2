# Funcionamiento del sistema

## Indicadores LED de estado

HALPI2 incorpora cinco LED RGB que ofrecen información visual sobre el estado del sistema y las condiciones de alimentación.

### Referencia rápida de los estados de los LED

| Patrón de LED | Color | Significado |
|-------------|-------|---------|
| LED 5 fijo | Rojo | Alimentación conectada, esperando la carga |
| Llenado progresivo | Rojo | Carga de los supercondensadores |
| Arcoíris + ciclo de colores | Varios | El CM5 no ha arrancado |
| Barra de tensión | Amarillo | Funcionamiento en modo solo |
| Barra de tensión | Verde | Funcionamiento en modo cooperativo |
| Barra de tensión | Naranja | Alimentación de respaldo activa (modo solo) |
| Barra de tensión | Verde oscuro | Alimentación de respaldo activa (modo cooperativo) |
| Todos parpadeando | Rojo | Sobretensión en los supercondensadores |
| Todos fijos | Rojo | Tiempo de espera del watchdog agotado |
| Barra de tensión | Morado | Apagado en curso |
| Todos fijos | Azul | Apagado al modo de reposo en curso |
| Todos fijos | Rojo tenue | Modo de reposo |
| Todos apagados | — | Sistema apagado |

### Indicación de la tensión de los supercondensadores

Durante el funcionamiento, los LED actúan como indicador de tensión y muestran el nivel de carga de los supercondensadores:

- **LED 1**: 5,0–6,0 V
- **LED 2**: 6,0–7,0 V
- **LED 3**: 7,0–8,0 V
- **LED 4**: 8,0–9,0 V
- **LED 5**: 9,0–10,0 V

## Gestión de la alimentación y procedimientos de apagado

HALPI2 incorpora una fuente de alimentación diseñada para soportar picos de tensión, microcortes e interrupciones breves.

### Descripción general del sistema de alimentación

El sistema de gestión de la alimentación de HALPI2 consta de:

- **Fuente de alimentación de rango amplio** (entrada de 11–32 V CC con protección hasta 100 V CC)
- **Sistema de respaldo con supercondensadores** para apagados controlados durante una pérdida de alimentación
- **Limitación de corriente** (0,9 A o 2,5 A seleccionables)
- **Detección de la pérdida de alimentación** e inicio automático del apagado
- **Supervisión de la tensión y la corriente de entrada**

El sistema funciona en dos modos: modo solo y modo cooperativo (co-op).

### Funcionamiento en modo solo

El modo solo ofrece un funcionamiento autónomo básico cuando el demonio HALPI no está en ejecución. El controlador funciona de forma independiente, sin comunicación con el software.

#### Características del modo solo

- **No requiere comunicación con el software**
- **Protección básica ante la pérdida de alimentación**: supervisa la tensión de entrada y reacciona ante la pérdida de alimentación
- **Apagado automático mediante pulsaciones simuladas del botón de encendido**
- **Opciones limitadas de supervisión y configuración**

#### Pérdida de alimentación y apagado en modo solo

**Detección de la pérdida de alimentación:**
El controlador supervisa la tensión de entrada y detecta la pérdida de alimentación. Un temporizador de corte de corriente (5 segundos de forma predeterminada) evita apagados durante interrupciones breves.

**Secuencia de apagado automático:**

1. **El controlador detecta la pérdida de alimentación**
2. **Se activa el temporizador de corte de corriente** para distinguir los microcortes de una pérdida real de alimentación
3. **Pulsaciones simuladas del botón de encendido**: el controlador envía una doble pulsación del botón de encendido al Compute Module
4. **El sistema operativo responde** e inicia un apagado controlado
5. **Los supercondensadores mantienen la alimentación** (normalmente 30–60 segundos disponibles)
6. **Protección con tiempo de espera de 60 segundos**: apagado forzado si el apagado controlado falla
7. **El sistema permanece apagado** hasta que vuelve la alimentación
8. **Reinicio automático** cuando se restablece la alimentación

**Apagado manual en modo solo:**

- Se produce un apagado normal del sistema operativo
- El sistema se reinicia automáticamente después de 5 segundos si sigue disponible la alimentación de entrada
- Para un apagado permanente, desconectar la alimentación de entrada tras iniciar el apagado controlado

#### Cuándo está activo el modo solo

El modo solo se activa:

- Durante el arranque inicial, antes de que se inicie el demonio HALPI
- Si el demonio HALPI no consigue iniciarse o está desactivado
- En sistemas operativos no compatibles que carecen del demonio
- Cuando el demonio se ha bloqueado o ha dejado de responder

!!! tip "Fiabilidad del modo solo"
    El modo solo ofrece una protección esencial, pero es menos fiable que el modo cooperativo. El controlador depende de pulsaciones simuladas de botón para solicitar el apagado, lo que puede no funcionar si el sistema está bloqueado.

### Funcionamiento en modo cooperativo

El modo cooperativo ofrece la funcionalidad completa de gestión de la alimentación cuando el demonio HALPI está en ejecución y se comunica con el controlador.

#### Características del modo cooperativo

- **Comunicación directa con el software**: intercambio de datos en tiempo real entre el controlador y el demonio
- **Protección mediante temporizador watchdog** (temporizador de vigilancia): un tiempo de espera de 30 segundos garantiza la estabilidad del sistema
- **Comportamiento de apagado configurable**: tiempos y comandos personalizables
- **Supervisión en tiempo real**: supervisión completa de los parámetros de alimentación
- **Opciones de configuración avanzadas**

#### Pérdida de alimentación y apagado en modo cooperativo

**Detección de la pérdida de alimentación:**
El controlador supervisa la alimentación de entrada y comunica los eventos directamente al demonio HALPI. El temporizador de corte de corriente configurable (5 segundos de forma predeterminada) permite interrupciones breves de la alimentación sin iniciar el apagado.

**Secuencia de apagado automático:**

1. **El controlador detecta la pérdida de alimentación** y lo comunica al demonio HALPI
2. **Evaluación del temporizador de corte de corriente**: el demonio determina si la pérdida de alimentación supera el umbral
3. **Ejecución del comando de apagado**: el demonio ejecuta el comando de apagado (predeterminado: `/sbin/poweroff`)
4. **Apagado controlado del sistema operativo**: las aplicaciones se cierran y los sistemas de archivos se desmontan de forma segura
5. **La alimentación de respaldo de los supercondensadores** aporta energía durante todo el apagado
6. **El controlador supervisa la finalización**: detecta cuándo se apaga el Compute Module
7. **La línea de 5 V se desactiva** cuando el apagado ha terminado
8. **El sistema permanece apagado** hasta que vuelve la alimentación de entrada
9. **Gestión del reinicio**: según la configuración, el sistema se reinicia automáticamente o permanece apagado

**Apagado manual en modo cooperativo:**

- Se produce un apagado controlado estándar cuando se inicia desde el software
- El sistema se reinicia automáticamente después de 5 segundos si sigue disponible la alimentación de entrada
- Para impedir el reinicio automático, desconectar la alimentación o configurar `auto_restart` como `false`

#### Protección mediante watchdog

El modo cooperativo incluye protección mediante temporizador watchdog:

- **Tiempo de espera de comunicación de 30 segundos**: el demonio debe comunicarse con el controlador con regularidad
- **Recuperación automática**: el sistema se reinicia si la comunicación se interrumpe
- **Protección ante fallos del software**: garantiza la recuperación tras bloqueos del demonio o del sistema
- **«Alimentar el watchdog»**: el demonio envía actualizaciones de estado periódicas para reiniciar el temporizador

#### Cuándo está activo el modo cooperativo

El modo cooperativo se activa cuando:

- El demonio HALPI está en ejecución y funciona correctamente
- Se ha establecido la comunicación entre el demonio y el controlador
- El sistema funciona sobre un sistema operativo compatible
- Están disponibles todas las funciones de supervisión y control del sistema

!!! info "Comprobación del modo cooperativo"
    Consultar el estado del demonio: `systemctl status halpid`

    Ver el estado del controlador: `halpi status`

    Para más información sobre el comando `halpi`, consultar la [Guía del software](./software.md#halpi-daemon-halpid).

### Alimentación de respaldo y sistema de condensadores

Ambos modos dependen del sistema de respaldo con supercondensadores para la protección mediante apagado controlado:

**Duración de la alimentación de respaldo:**

- Los supercondensadores proporcionan 30–60 segundos de alimentación de respaldo
- La duración depende de la carga del sistema y de los periféricos conectados
- Tiempo suficiente para cerrar de forma segura el sistema de archivos y terminar los procesos
- No está diseñado para mantener el funcionamiento durante cortes prolongados

**Características de la carga:**

- Tiempo de carga: 25 segundos con el límite de corriente de 0,9 A
- Tiempo de carga: 9 segundos con el límite de corriente de 2,5 A
- El progreso de la carga se muestra visualmente mediante la progresión de los LED (patrón de llenado en rojo)

!!! warning "Limitación de la protección ante la pérdida de alimentación"
    El sistema de supercondensadores está diseñado para el apagado controlado, no para mantener el funcionamiento. No se debe confiar en él para cortes de corriente prolongados.

### Consideraciones sobre el apagado manual

HALPI2 da prioridad al funcionamiento y la recuperación automáticos, lo que afecta al comportamiento del apagado manual.

#### Comportamiento del reinicio automático

De forma predeterminada, HALPI2 se reinicia tras un apagado manual si la alimentación de entrada sigue disponible:

- Los apagados manuales producen un apagado normal del sistema operativo
- Tras completarse el apagado transcurre un periodo de gracia de 5 segundos
- El sistema se reinicia automáticamente para mantener la disponibilidad operativa
- Así se garantiza la recuperación ante apagados accidentales

#### Métodos de apagado intencionado

Para un apagado permanente, se puede seguir uno de estos métodos:

**Método de desconexión de la alimentación:**

1. Iniciar el apagado controlado desde el software
2. Esperar a que finalice el apagado (los LED se apagan)
3. Desconectar la alimentación de entrada para impedir el reinicio automático

**Método de configuración:**

1. Desactivar el reinicio automático: `halpi config set auto_restart false`
2. Iniciar el apagado desde el software
3. El sistema permanece apagado una vez completado el apagado

**Modo de reposo (futuro):**
!!! info "Estado de la función"
    La funcionalidad del modo de reposo está prevista para futuras versiones del firmware. Permitirá apagar el Compute Module mientras el controlador de HALPI2 permanece activo, a la espera de eventos de reactivación.

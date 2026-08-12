---
translated_from: 288cabc5149b6610fd3f280bfce455d945b6a356
---

# Interfaces y conectividad

## CAN FD / NMEA 2000

El HALPI2 incorpora una interfaz [CAN FD](https://en.wikipedia.org/wiki/CAN_FD) completamente aislada que admite tanto redes náuticas [NMEA 2000](https://en.wikipedia.org/wiki/NMEA_2000) como aplicaciones de automoción o industriales. La interfaz proporciona comunicación de datos a alta velocidad con aislamiento eléctrico total para lograr inmunidad al ruido.

### Especificaciones de la interfaz

La interfaz CAN FD admite tanto el protocolo CAN estándar como CAN FD. En aplicaciones NMEA 2000, la interfaz funciona en modo CAN normal a la velocidad de datos estándar de 250 kbps. Cuando se emplea en aplicaciones de automoción o industriales, la interfaz puede aprovechar todas las capacidades de CAN FD, con velocidades de datos de hasta 8 Mbps.

El panel frontal incorpora un conector Micro-C compatible con el cableado y los componentes estándar de NMEA 2000. Esto permite la integración directa con redes náuticas existentes mediante conectores en T y cables de derivación estándar.

### Configuración de alimentación y carga de la red

El impacto del HALPI2 sobre la alimentación de la red NMEA 2000 depende de la configuración de alimentación elegida. En la configuración estándar, con alimentación externa a través del conector E7T, el dispositivo no necesita energía de la red NMEA 2000, lo que da un número de equivalencia de carga (LEN) de 0.

Cuando se configura para alimentarse del bus NMEA 2000, el consumo de corriente del dispositivo debe limitarse a 0,9 A mediante el limitador de corriente interno. Esto corresponde a un valor LEN de 18. Al alimentar el HALPI2 a través de NMEA 2000, el dispositivo debe conectarse al cable troncal de la red cerca del cable de alimentación para minimizar la caída de tensión y garantizar un funcionamiento fiable.

### Configuración del hardware

La placa portadora incluye una resistencia de terminación de 120 Ω que puede habilitarse mediante un puente (jumper). En aplicaciones NMEA 2000 debe evitarse la terminación en el dispositivo, ya que la norma no la permite. No obstante, en aplicaciones de automoción o industriales con comunicación punto a punto, el puente puede colocarse para habilitar la resistencia de terminación.

Para el diagnóstico y la resolución de problemas de red, la placa portadora dispone de LED RX y TX dedicados que indican la actividad de la red. Estos LED ofrecen una indicación visual inmediata sobre la transmisión y la recepción de datos, lo que facilita el diagnóstico de los problemas de conectividad.

### Instalación en la red

La conexión a las redes NMEA 2000 se realiza mediante un conector en T estándar (no suministrado) instalado en el cable troncal de la red y un cable de derivación que une el conector en T con el conector Micro-C del HALPI2.

### Integración con el software

La interfaz CAN se integra de forma transparente con Linux a través del marco SocketCAN y aparece como el dispositivo de red `can0`. Esta interfaz estándar permite utilizar las herramientas CAN habituales de Linux para la supervisión y el diagnóstico. La interfaz de red viene preconfigurada en todas las imágenes del sistema operativo del HALPI2 (HaLOS, OpenPlotter y Raspberry Pi OS).

La integración con el servidor Signal K está disponible en las variantes de imagen HaLOS Marine y en OpenPlotter, que detectan y utilizan automáticamente la interfaz CAN para procesar los datos NMEA 2000. En las imágenes HaLOS no náuticas, Signal K puede instalarse desde la tienda Container Apps de Cockpit. El servidor Signal K se encarga de la descodificación de los PGN y proporciona acceso web a los datos de la red en tiempo real.

### Resolución de problemas

La resolución de problemas de red comienza por los LED RX/TX de la placa portadora. En funcionamiento normal, los LED muestran una actividad intermitente que se corresponde con el tráfico de la red. La ausencia de actividad en RX puede indicar problemas de cableado o una terminación incorrecta, mientras que la ausencia de actividad en TX puede apuntar a conflictos de red o al cableado.

El comando `candump` de Linux permite supervisar el bus CAN directamente desde la línea de comandos. Esta herramienta ofrece información detallada sobre todos los mensajes del bus y permite un diagnóstico en profundidad. En su forma más sencilla se ejecuta así:

```bash
candump can0
```

Esto muestra en tiempo real todos los mensajes CAN entrantes sin procesar.

El panel de control del servidor Signal K aporta funciones adicionales de supervisión de la red. Muestra en tiempo real las velocidades de datos NMEA 2000 procedentes de la interfaz CAN. La herramienta de exploración de datos permite ver los datos NMEA 2000 descodificados.

!!! quote "Información relacionada"
    - **Configuración de la alimentación:** véase [Primeros pasos](../getting-started/getting-started.md#instalacion-permanente-de-la-alimentacion)
    - **Configuración del software:** véase [Guía del software](./software.md)
    - **Resolución de problemas de red:** véase [Guía de resolución de problemas](./troubleshooting.md)


## RS-485 (NMEA 0183)

El HALPI2 incluye una interfaz [RS-485](https://en.wikipedia.org/wiki/RS-485) aislada que proporciona comunicación serie para redes náuticas [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183)[^rs422] y aplicaciones industriales.

[^rs422]: Técnicamente, NMEA 0183 utiliza la norma RS-422, pero RS-485 es compatible con versiones anteriores, lo que permite al HALPI2 comunicarse tanto con dispositivos RS-422 como RS-485.

### Especificaciones de la interfaz

El transceptor RS-485 funciona a velocidades de hasta 10 Mbps, aunque las aplicaciones NMEA 0183 típicas utilizan las velocidades estándar de 4800 o 38400 bps. La interfaz cuenta con aislamiento galvánico y cumple la especificación NMEA 0183, lo que protege al HALPI2 frente a los bucles de masa y el ruido eléctrico habituales en los entornos náuticos.

La interfaz está conectada internamente al UART 4 del Raspberry Pi y aparece como `/dev/ttyAMA4` en el sistema operativo Linux. A este dispositivo serie estándar puede acceder cualquier aplicación compatible con la comunicación serie, incluidos el servidor Signal K, OpenCPN y aplicaciones propias.

### Configuración del hardware

La placa portadora incluye LED RX y TX dedicados que indican la actividad de comunicación en la interfaz RS-485. Estos LED ofrecen una indicación visual inmediata durante la instalación y la resolución de problemas, lo que permite comprobar fácilmente que los datos se transmiten y se reciben correctamente.

Cuando funciona como interfaz RS-485 genérica, el dispositivo puede configurarse en modo de habilitación de transmisión automático o manual. En el modo manual se utiliza un pin GPIO para controlar la señal de habilitación de transmisión, de modo que el software gestiona cuándo la interfaz está en modo de transmisión o de recepción. Esto es necesario en aplicaciones multiemisor, en las que la interfaz debe permanecer en estado recesivo mientras no transmite. El modo automático permite que el hardware active la señal de habilitación de transmisión al enviar datos, lo que simplifica la configuración en aplicaciones de un solo emisor.

Además, la interfaz RS-485 admite un modo semidúplex, que le permite transmitir y recibir por el mismo par de hilos.

La interfaz también puede deshabilitarse por completo mediante la configuración del hardware si se necesita el UART 4 para otros fines.

### Cableado y conexión

La interfaz RS-485 requiere un prensaestopas o un conector de panel que debe aportar el usuario. Una buena opción es [un conector de panel SP13 con latiguillo](https://shop.hatlabs.fi/products/sp13-pigtail-connector-pair-5-pin-female-cable-plug). La interfaz es compatible con la señalización RS-422 utilizada en NMEA 0183 y admite tanto redes RS-485 multiemisor como redes RS-422 de un emisor y varios receptores. Utiliza pares diferenciales equilibrados, etiquetados TX+/TX- y RX+/RX-.

### Integración con el software

Todas las imágenes del HALPI2 vienen preconfiguradas con la interfaz RS-485 lista para usar. En las imágenes HaLOS Marine y en OpenPlotter, el servidor Signal K detecta automáticamente la interfaz y recibe los datos NMEA 0183 transmitidos.

En aplicaciones propias, la interfaz se comporta como un puerto serie estándar de Linux. Las aplicaciones pueden abrir `/dev/ttyAMA4` y configurar la velocidad en baudios, los bits de datos, los bits de parada y la paridad según lo requiera el equipo conectado. Las aplicaciones en Python, Node.js y C/C++ pueden acceder fácilmente a la interfaz mediante las bibliotecas estándar de comunicación serie.

### Aplicaciones habituales

En entornos náuticos, la interfaz RS-485 se conecta normalmente a receptores GPS, sondas de profundidad, instrumentos de viento, transpondedores AIS u otros dispositivos que utilizan el protocolo NMEA 0183. Entre las aplicaciones industriales puede estar la conexión a PLC, sensores y otros equipos de automatización que utilizan Modbus RTU u otros protocolos RS-485.

La capacidad de alta velocidad de la interfaz también admite aplicaciones no estándar, como la captura de datos de sensores a alta cadencia o protocolos de comunicación propios, lo que hace al HALPI2 adecuado para embarcaciones de investigación y aplicaciones de supervisión especializadas.

!!! quote "Información relacionada"
    - **Configuración del software:** véase [Guía del software](./software.md)
    - **Resolución de problemas:** véase [Guía de resolución de problemas](./troubleshooting.md)


## GNSS (GPS)

El HALPI2 admite HAT receptores GNSS conectados al UART0 (`/dev/ttyAMA0`). Cualquier receptor GNSS en este puerto funciona con gpsd sin configuración adicional.

Para los receptores u-blox (como el Max-M8Q), las imágenes HaLOS Marine ofrecen además una configuración automática optimizada para el uso náutico.

### Configuración automática (receptores u-blox)

En las imágenes HaLOS Marine, un servicio de systemd (`configure-ublox-marine`) detecta y configura automáticamente los receptores u-blox en cada arranque:

| Parámetro | Valor |
|:----------|:------|
| Velocidad en baudios | 115200 bps (valor de fábrica: 9600) |
| Frecuencia de actualización | 10 Hz (100 ms) |
| Modelo dinámico | Sea (optimizado para el uso náutico) |

La configuración se ejecuta en cada arranque porque los módulos u-blox basados en ROM (como el MAX-M8Q) no tienen memoria flash. Los ajustes se guardan en la RAM respaldada por pila (BBR), que puede perderse si se interrumpe la alimentación de la pila de respaldo, por ejemplo cuando el dispositivo permanece sin alimentación durante un periodo prolongado. La reconfiguración es transparente y añade aproximadamente 2 segundos al arranque de gpsd.

Si no se detecta ningún receptor, el servicio finaliza de forma silenciosa. Un HAT GNSS recién instalado se configura automáticamente en el siguiente reinicio.

### Acceso a los datos

Los datos de GPS los proporciona [gpsd](https://gpsd.io/) en el puerto TCP 2947. En las imágenes HaLOS Marine, Signal K se conecta a gpsd automáticamente: no hace falta ninguna configuración adicional.

Para el diagnóstico se utilizan las herramientas de línea de comandos estándar de gpsd:

```bash
# Monitor GPS data in real-time
gpsmon

# Output raw NMEA 0183 sentences
gpspipe -r
```

### Imágenes distintas de HaLOS

En Raspberry Pi OS u otros sistemas operativos, instalar y configurar gpsd manualmente:

```bash
sudo apt install gpsd gpsd-clients
```

Editar `/etc/default/gpsd` para establecer `DEVICES="/dev/ttyAMA0"` y reiniciar el servicio. El receptor funciona con sus valores de fábrica (9600 baudios, 1 Hz) salvo que se configure con `ubxtool`, del paquete `gpsd-clients`.

!!! quote "Información relacionada"
    - **gpsd en HaLOS:** véase [documentación de GPS de HaLOS](https://docs.halos.fi/user-guide/gps/)
    - **Configuración del software:** véase [Guía del software](./software.md)


## Ethernet

El HALPI2 incluye una interfaz Gigabit Ethernet que proporciona conectividad de red de alta velocidad para la transferencia de datos, el acceso remoto y la integración con las redes de a bordo. El puerto Ethernet de la placa portadora es un conector RJ45 estándar. Se lleva a un conector de panel al que puede conectarse un cable Ethernet externo.

## USB

El HALPI2 dispone de cuatro puertos USB 3.0 Type A integrados en total, que ofrecen conectividad de alta velocidad para todo tipo de periféricos y dispositivos. Un puerto se conecta directamente a la interfaz USB 3.0 del CM5, mientras que los otros tres pasan por un concentrador USB 3 integrado. En la configuración estándar, dos de los puertos se llevan al panel frontal y otros dos quedan disponibles en la placa portadora para conexiones internas.

## HDMI

El HALPI2 incluye dos puertos HDMI 2.0 (HDMI0 y HDMI1) para salida de vídeo. La placa portadora ofrece conectores de cable plano flexible (FFC) para ambos puertos HDMI. Estos se llevan al panel frontal mediante cables FFC personalizados. Los conectores del panel frontal son conectores HDMI Type A convencionales.

La salida HDMI del HALPI2 admite de forma fiable dos flujos de vídeo Full HD (1080p) simultáneos. La salida de vídeo 4K puede funcionar, pero no está garantizada.

## MIPI (CSI/DSI)

La placa portadora incluye dos conectores MIPI CSI/DSI para interfaces de cámara y de pantalla. Son conectores FFC (cable plano flexible) de 22 pines con paso de 0,5 mm. Deberían funcionar tal cual con las cámaras y pantallas más recientes compatibles con Raspberry Pi.

Por motivos de estanqueidad, el uso de cables FFC debe limitarse únicamente a conexiones internas.

## Botones externos

El HALPI2 dispone de un conector de 2×3 pines en la placa portadora para conectar botones externos. La carcasa no incluye botones integrados, lo que permite al usuario personalizar la ubicación y el tipo de los botones según sus necesidades concretas.

### Asignación de pines del conector de los botones

La placa portadora incluye un conector de 6 pines con tres funciones de botón etiquetadas:

| Etiqueta | Función | Descripción |
|:------|:---------|:------------|
| Reset | Reinicio del controlador | Reinicio por hardware (pin RUN del RP2040) |
| Power | Alimentación del Raspberry Pi | Botón de encendido del CM5 (entrada PWR_BUT) |
| User | Configurable por el usuario | Evento definido por el usuario (aún no implementado) |

Cada conexión de botón utiliza dos pines: uno para la señal del botón y otro para masa. Utilizar pulsadores momentáneos normalmente abiertos (NA) que conecten el pin de señal a masa al pulsarlos.

### Funciones de los botones

**Botón «Reset»:**
El botón de reinicio provoca un reinicio del sistema a nivel de hardware forzando a nivel bajo el pin RUN del RP2040. Esta acción realiza un reinicio completo del sistema que afecta al controlador, al CM5 y a todos los periféricos conectados. El botón de reinicio resulta especialmente útil en situaciones de recuperación de emergencia, cuando los procedimientos de apagado por software han fallado y el sistema ha dejado de responder.

**Botón «Power»:**
El botón de encendido se conecta directamente a la entrada del botón de encendido del CM5 y funciona igual que el botón de encendido del Raspberry Pi 5. Un doble clic del botón de encendido solicita un apagado controlado del sistema, lo que permite al sistema operativo cerrar correctamente las aplicaciones y desmontar los sistemas de archivos antes de apagarse. Una pulsación larga del botón de encendido fuerza un apagado inmediato, que solo debe emplearse cuando el sistema no responde.

**Botón «User»:**
La funcionalidad del botón de usuario está pendiente de implementación en el software y ofrecerá funciones configurables por el usuario en futuras versiones del firmware. Una vez implementada, este botón estará destinado a acciones personalizadas y a disparadores específicos de cada aplicación, de modo que el usuario podrá definir su propio comportamiento en función de sus requisitos operativos concretos.

### Instalación de los botones

#### Montaje directo en la carcasa

Para el montaje directo en la carcasa del HALPI2, utilizar los orificios pretaladrados de 6 mm o 13 mm que ya incorpora el diseño de la carcasa. Retirar primero los tapones ciegos correspondientes de esos orificios e instalar un conjunto de botón estanco cuyo diámetro coincida con el del orificio. Conectar el botón al conector de pines de la placa portadora con un cable adecuado, asegurando una descarga de tracción correcta y un sellado estanco en el paso por la carcasa.

#### Montaje en un panel externo

Al montar los botones en un panel de control remoto, elegir una ubicación adecuada que ofrezca un acceso cómodo sin comprometer la estanqueidad. Utilizar prensaestopas en los puntos de entrada de cable y conectar los botones con cable alargador de conductores de 22–26 AWG, manteniendo la longitud total del cable por debajo de 3 m para preservar la integridad de la señal. En instalaciones expuestas a la humedad o a entornos agresivos, emplear conectores estancos en los puntos de unión para garantizar un funcionamiento fiable a largo plazo.

#### Conexión

Todas las conexiones de los botones a la placa portadora deben emplear conectores hembra de paso de 2,54 mm. Comprobar la alineación correcta de los pines y la firmeza de la conexión para evitar problemas de contacto durante el funcionamiento.

!!! quote "Información relacionada"
    - **Gestión de la alimentación:** véase [Controlador de la placa portadora](../technical-reference/controller.md)
    - **Acceso al hardware:** véase [Mantenimiento del hardware](./hardware.md)

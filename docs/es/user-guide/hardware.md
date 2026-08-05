# Guía de hardware

## Acceso a la carcasa

HALPI2 incorpora una carcasa de aluminio inyectado con recubrimiento en polvo y orificios pretaladrados para los conectores del panel. Cuando se requieren modificaciones internas o tareas de mantenimiento, se puede acceder al interior de la carcasa siguiendo los procedimientos que se describen a continuación.

### Apertura de la carcasa

Para acceder a los componentes internos, se comienza comprobando que la unidad está completamente apagada y que los cables de alimentación están desconectados. La tapa se fija con cuatro tornillos avellanados M4×10 con cabeza PH2. Estos tornillos se retiran con un destornillador PH2 y a continuación se retira la tapa.

### Reensamblado

Antes de volver a montar la carcasa, conviene verificar que todas las conexiones internas están firmes y correctamente asentadas. Los cables se tienden con cuidado para evitar pinzamientos y curvas pronunciadas.

Es fácil conectar por error los cables planos flexibles (FFC) al revés. Las flechas «Contacts» de la serigrafía permiten verificar la orientación correcta.

Se debe prestar especial atención a la junta de la tapa, comprobando que no presenta daños, suciedad ni desplazamientos que puedan comprometer la estanqueidad de la carcasa.

Los cuatro tornillos M4×10 de la tapa se vuelven a instalar con el destornillador PH2. No apretar en exceso.


## Conectores del panel

### Configuración estándar

HALPI2 se suministra con una configuración de conectores estándar adecuada para la mayoría de las aplicaciones. La disposición predeterminada incluye:

- **Conector de alimentación E7T**
- **Conector NMEA 2000 micro**
- **Gigabit Ethernet RJ45**
- **Salida HDMI**
- **2× USB 3.0 Type-A**
- **3× posiciones de prensaestopas PG7** (con tapones ciegos)
- **2× posiciones de antena RP-SMA** (con tapones ciegos)
- **Tapón compensador de presión** para la igualación de presión

![Conectores del panel frontal y tapones ciegos](./front-panel-connectors-all.jpg)
*Conectores del panel frontal y tapones ciegos. Los conectores marcados en verde forman parte de la configuración estándar. Las posiciones amarillas son tapones ciegos que se pueden sustituir por conectores según sea necesario. La posición roja es el tapón compensador de presión, que no se debe retirar.*

### Opciones de conectores personalizados

Si se necesitan otros tipos de conectores, la configuración del panel se puede modificar:

#### Retirada de conectores

!!! warning "Importante"
    Los conectores solo se deben modificar con la unidad apagada y desconectada de todas las fuentes.

    Las roscas de plástico se pueden dañar por un par de apriete excesivo. Utilizar llaves de vaso estándar, pero apretar únicamente a mano.

1. **Utilizar el tamaño de llave de vaso adecuado:**
    - Conectores grandes: llave de vaso de 26 mm
    - Tornillos de nailon M6: llave de vaso de 10 mm
    - Conectores RP-SMA: llave de vaso de 8 mm
    - Posiciones PG7: destornillador plano grande, llave de vaso de 17 mm

2. **Retirar con cuidado**: las roscas de plástico se pueden dañar por un par de apriete excesivo

3. **Conservar las piezas retiradas** para un posible uso futuro

#### Instalación de conectores nuevos

1. **Utilizar únicamente conectores de calidad náutica** o con una clasificación ambiental adecuada
2. **Asegurar un sellado correcto**: se requiere un reborde ancho en el interior
3. **Apretar solo a mano**: no aplicar un par excesivo a las roscas de plástico
4. **Comprobar el ajuste** antes de la instalación definitiva

## Disposición interna

- La placa portadora de HALPI2 es la placa principal del ordenador: aloja el Compute Module 5 (CM5) en su cara inferior y proporciona la gestión de la alimentación, los indicadores y las conexiones de todas las interfaces.

### Áreas funcionales de la placa portadora

Las principales áreas funcionales de la placa portadora se ilustran en la imagen siguiente.

![Disposición de la placa portadora, cara superior](./carrier-board-top-layout.jpg)
*Disposición de la cara superior de la placa portadora, con las áreas funcionales principales.*

### Conectores de la placa portadora

Se accede a la funcionalidad a través de varios conectores integrados en la placa, que se muestran en la imagen siguiente.

![Conectores de la placa portadora, cara superior](./carrier-board-top-conx.jpg)
*Conectores de la placa portadora, cara superior.*

A continuación se ofrece la lista de los conectores de la cara superior.

| Etiqueta | Descripción |
|:------|:------------|
| **a1** | Conector de alimentación (tipo Phoenix MC, paso de 3,81 mm) |
| **a2** | Conmutador del límite de corriente de entrada (0,9 A o 2,5 A) |
| **a3** | Puente (jumper) de control de la alimentación. Cortocircuitar los pines «3.3V off» para forzar el apagado de la línea de 3,3 V. Cortocircuitar los pines «5V on» para forzar el encendido de la línea de 5 V. **NB:** en las placas de la versión 0.4.0, los conectores **a3** y **c2** están organizados de otra manera. |
| **b1** | Puerto Ethernet (RJ45) |
| **c1** | Puerto USB del controlador. Se utiliza para grabar el firmware del microcontrolador RP2040. |
| **c2** | Conector de pines del puente USB BOOT del MCU. Cortocircuitar los pines para poner el RP2040 en modo de arranque USB. |
| **c3** | Conector de depuración del controlador |
| **c4** | Conector GPIO del controlador sin montar |
| **c5** | Conectores de pines de los botones. Se utilizan para conectar los botones de encendido, reinicio y usuario. |
| **c6** | Botón de encendido. Se utiliza para encender y apagar el Compute Module 5. |
| **d1** | Conector GPIO de 40 pines de Raspberry Pi |
| **e1** | Conector MIPI0 para la interfaz de cámara o de pantalla |
| **e2** | Conector MIPI1 para la interfaz de cámara o de pantalla |
| **f1** | Conector HDMI0 |
| **f2** | Conector HDMI1 |
| **g1** | Conector M.2 para SSD NVMe |
| **h1** | Interfaz CAN FD (tipo Phoenix MC, paso de 3,81 mm) |
| **h2** | Puente del terminador CAN. Cortocircuitar los pines para habilitar el terminador del bus CAN FD. |
| **i1** | Interfaz RS-485 (tipo Phoenix MC, paso de 3,81 mm) |
| **i2** | Puente de habilitación automática/manual de RS-485. |
| **i4** | Puente XRS-485 RX Enable. Cortocircuitar los pines para habilitar la recepción de tráfico RS-485. |
| **j1** | Conector USB Boot del Compute Module. Se utiliza para grabar el firmware del Compute Module 5. |
| **j2** | Conmutador de selección del modo de arranque del Compute Module. Se ajusta a «Normal» para el funcionamiento normal y a «Abnormal» para el modo de arranque USB. Cuando el conmutador está en «Abnormal» se enciende un LED de advertencia. |
| **m1** | Conector USB3 0. Conectado directamente al CM5. |
| **m2** | Conector USB3 1-0. Conectado al concentrador USB3 integrado. |
| **m3** | Conector USB3 1-1. Conectado al concentrador USB3 integrado. |
| **m4** | Conector USB3 1-2. Conectado al concentrador USB3 integrado. |
| **n1** | Portapilas CR2032 para el RTC (reloj de tiempo real) |
| **q1** | Conector del ventilador del CM5. El ventilador se puede utilizar para mejorar la circulación de aire dentro de la carcasa. No es necesario cuando se usa la carcasa estándar. |

![Conectores de la placa portadora, cara inferior](./carrier-board-bottom-conx.jpg)
*Conectores de la placa portadora, cara inferior.*

A continuación se ofrece la lista de los conectores de la cara inferior.

| Etiqueta | Descripción |
|:------|:------------|
| **p1** | Conector del Compute Module 5. |
| **q1** | Conector del ventilador del CM5, ubicación alternativa. Este conector de pines permite conectar un ventilador de CPU sobre el módulo CM5 cuando se utiliza una carcasa personalizada. **NB:** los conectores **q1** y **q2** están conectados en paralelo y no se deben utilizar simultáneamente. |

Por último, el conector de la antena de WiFi y Bluetooth se encuentra en el propio Compute Module 5. Se muestra en la imagen siguiente.

![Conector de la antena WiFi](./cm5-top-conx.jpg)
*Conector de antena U.FL en el Compute Module 5.*

| Etiqueta | Descripción |
|:------|:------------|
| **r1** | Conector U.FL para la antena de WiFi y Bluetooth. |

### Blinkenlights

La placa portadora incorpora varios LED de estado para la supervisión del sistema.

![LED de estado de la placa portadora](./carrier-board-top-leds.jpg)
*LED de estado de la placa portadora y sus colores.*

Los LED de estado ofrecen información sobre los estados de alimentación y actividad del sistema. A continuación se ofrece la lista de los LED de estado.

| Etiqueta | Color | Descripción |
|-------|:-------|:------------|
| **1** | RGB   | Cinco LED RGB. Estos LED indican el estado y la actividad del sistema en el panel frontal. |
| **2** | Rojo   | LED de alimentación de las líneas de 3,3 V y 5 V. Estos LED indican el estado de alimentación de las líneas de tensión respectivas. |
| **3** | Amarillo| Indicador de velocidad de Ethernet. Encendido cuando el puerto Ethernet ha negociado una conexión de 100/1000 Mbps. |
| **4** | Verde | Indicador de actividad de Ethernet. Parpadea cuando hay tráfico de red en el puerto Ethernet. |
| **5** | Azul | Indicador de actividad del SSD. Parpadea cuando hay actividad de lectura/escritura en el SSD NVMe M.2. |
| **6** | Rojo | Indicador de estado de alimentación de la Pi. Encendido cuando el sistema tiene alimentación pero está apagado. |
| **7** | Verde | Indicador de actividad de la Pi. Parpadea cuando hay actividad en la Raspberry Pi. |
| **8** | Ámbar | Advertencia de modo de arranque «Abnormal». Encendido cuando el conmutador de modo de arranque USB está en «Abnormal». Indica que el dispositivo está configurado para grabarse a través del conector USB Boot y no arrancará con normalidad. |
| **9** | Verde | LED TX/RX de CAN. Estos LED parpadean cuando se reciben (RX) o se transmiten (TX) datos por la interfaz CAN. |
| **10** | Verde | LED TX/RX de RS-485. Estos LED parpadean cuando se reciben (RX) o se transmiten (TX) datos por la interfaz RS-485. |

Los patrones de los LED RGB se documentan en la [Guía de funcionamiento](./operation.md#status-led-indicators).

## Configuración de la limitación de corriente

La placa portadora incorpora un conmutador de limitación de corriente que permite configurar la corriente máxima suministrada a los periféricos. Para localizar el conmutador, consultar la ubicación del conmutador **a2** en la imagen de la sección [Conectores de la placa portadora](#carrier-board-connectors).

!!! info "Ajustes del límite de corriente"
    **Ajuste de 0,9 A (predeterminado):**

    - Obligatorio para la alimentación del bus NMEA 2000
    - Adecuado para el funcionamiento básico

    **Ajuste de 2,5 A:**

    - Para periféricos de alto consumo
    - Carga más rápida de los supercondensadores
    - Solo con una conexión de alimentación dedicada

Para cambiar el ajuste del límite de corriente, apagar primero HALPI2 por completo y retirar la tapa de la carcasa siguiendo el procedimiento descrito en la sección Acceso a la carcasa. Localizar el conmutador del límite de corriente en la placa portadora y moverlo a la posición deseada (0,9 A o 2,5 A). Una vez cambiado el ajuste, volver a montar la carcasa comprobando que todas las conexiones siguen firmes.

## Uso de HAT

### Compatibilidad con HAT

HALPI2 admite los HAT estándar de Raspberry Pi a través de su conector GPIO de 40 pines y mantiene plena compatibilidad eléctrica y mecánica con la especificación HAT de Raspberry Pi. La placa portadora ofrece la misma asignación de pines GPIO que una Raspberry Pi estándar, lo que permite que la mayoría de los HAT diseñados para Raspberry Pi 4 y 5 funcionen sin modificaciones. Esta compatibilidad abarca tanto los HAT oficiales de Raspberry Pi como las placas de expansión de terceros que siguen el estándar HAT.

### Restricciones físicas

La carcasa de HALPI2 ofrece 45 mm de espacio libre vertical por encima de la placa portadora, suficiente para alojar hasta dos HAT apilados. La zona situada a la izquierda del área de instalación de HAT marcada está ocupada por los supercondensadores, lo que limita el espacio disponible para los HAT que sobrepasan el contorno estándar de 65 × 56 mm. Se debe prestar especial atención a los HAT con conectores laterales. Los conectores orientados hacia el «sur» o el «este» no suelen presentar problemas, pero los orientados hacia el «oeste» pueden interferir con los supercondensadores.

### Conflictos de pines GPIO

Las interfaces integradas de HALPI2 utilizan varios pines GPIO, algo que se debe tener en cuenta al seleccionar HAT compatibles. La tabla siguiente detalla los pines GPIO reservados y sus funciones:

| Número de GPIO | Función | Interfaz | Notas |
|----------|----------|-----------|-------|
| GPIO 2 | I2C SDA | I2C del sistema | Se puede compartir; dirección 0x6d reservada |
| GPIO 3 | I2C SCL | I2C del sistema | Se puede compartir; dirección 0x6d reservada |
| GPIO 6 | SPI CS | CAN FD | Selección de chip (chip select) específica para el controlador CAN |
| GPIO 9 | SPI MISO | CAN FD | Bus SPI0 compartido |
| GPIO 10 | SPI MOSI | CAN FD | Bus SPI0 compartido |
| GPIO 11 | SPI SCK | CAN FD | Bus SPI0 compartido |
| GPIO 12 | UART TX | RS-485 | Transmisión de UART4 |
| GPIO 13 | UART RX | RS-485 | Recepción de UART4 |
| GPIO 24 | RS-485 EN | RS-485 | Señal de habilitación (solo en modo manual) |
| GPIO 26 | CAN INT | CAN FD | Línea de interrupción del controlador CAN |

### Uso compartido de interfaces y conflictos

El bus I2C de los GPIO 2 y 3 se puede compartir con dispositivos HAT, ya que I2C admite varios dispositivos en el mismo bus. Sin embargo, los HAT no deben utilizar la dirección I2C 0x6d, reservada para el controlador del sistema HALPI2. La mayoría de los HAT I2C funcionan sin problemas, pero conviene verificar las direcciones I2C utilizadas antes de la instalación.

El bus SPI0 empleado por la interfaz CAN FD se puede compartir con otros dispositivos SPI, ya que HALPI2 utiliza pines específicos de selección de chip (GPIO 6) e interrupción (GPIO 26). Los HAT que usan SPI0 con los pines de selección de chip estándar (GPIO 7 o GPIO 8) pueden coexistir con la interfaz CAN, aunque quizá requieran configuración adicional mediante overlays de árbol de dispositivos (device tree overlays).

### Desactivación de las interfaces integradas

Si un HAT requiere el uso exclusivo de pines ocupados por las interfaces integradas de HALPI2, dichas interfaces se pueden desactivar mediante modificaciones de hardware. La interfaz CAN FD se puede liberar por completo retirando el puente de soldadura GPIO6-CAN.CS situado en la cara inferior de la placa portadora. Esta modificación desconecta el controlador CAN del bus SPI y libera los GPIO 6, 9, 10, 11 y 26 para su uso por el HAT.

La interfaz RS-485 se puede desactivar retirando el puente RX Enable (i4) de la placa portadora. Esto impide que el transceptor RS-485 reciba datos y libera los GPIO 12 y 13 para otros usos. Si no se necesita el control manual de la habilitación de transmisión, el GPIO 24 también se puede reutilizar poniendo el puente de habilitación automática/manual de RS-485 (i2) en modo automático.

### Procedimiento de instalación

La instalación comienza apagando el sistema y desconectando todas las fuentes de alimentación. Retirar la tapa de la carcasa siguiendo el procedimiento descrito en la sección Acceso a la carcasa.

Las placas portadoras de la versión 0.5.0 y posteriores incluyen insertos roscados M2.5 preinstalados en las cuatro posiciones de montaje de HAT, lo que simplifica la instalación. Las placas v0.4.0 anteriores requieren instalar tuercas M2.5 manualmente. Para instalar las tuercas es necesario retirar temporalmente la placa portadora. Esto se puede hacer sin desconectar todos los cables.

Para muchos HAT habituales bastan separadores de 15 mm, pero conviene medir la altura del conector hembra del HAT para asegurar el espacio libre correcto. La base del conector macho tiene 2,5 mm de altura, por lo que se debe sumar este valor a la altura del conector hembra para determinar la longitud de separador necesaria.

Enroscar los separadores en los orificios de montaje o fijarlos con tuercas por debajo en las placas v0.4.0. Alinear el HAT con el conector GPIO de 40 pines y comprobar que todos los pines están bien colocados antes de aplicar una presión uniforme para asentar el conector. El HAT debe quedar paralelo a la placa portadora, sin holgura visible en la conexión GPIO.

Fijar el HAT con tornillos M2.5 o separadores adicionales a través de los orificios de montaje del HAT hasta los separadores. Estos tornillos no se incluyen con HALPI2 y se deben adquirir aparte. Apretar los tornillos lo justo para fijar el HAT sin flexionar el circuito impreso.

### Organización de los cables

Si el HAT incluye conectores externos que deben ser accesibles desde el exterior de la carcasa, conviene instalar conectores de panel adecuados en las posiciones de prensaestopas PG7 disponibles. De este modo se mantiene la protección ambiental de la carcasa y se facilita el acceso desde el exterior.

### Procedimiento de retirada

La retirada del HAT sigue el procedimiento de instalación en orden inverso. Apagar el sistema por completo y desconectar todas las fuentes de alimentación antes de abrir la carcasa. Retirar los tornillos de montaje M2.5 y levantar el HAT con cuidado, en línea recta desde el conector GPIO, evitando cualquier fuerza lateral que pudiera doblar los pines del conector.

Si el HAT parece atascado, comprobar si queda algún elemento de fijación o algún cable sin retirar antes de aplicar más fuerza. Algunos HAT con conectores muy ajustados pueden requerir un ligero balanceo mientras se tira hacia arriba. Balancear el HAT en la dirección norte-sur; hacerlo en la dirección este-oeste puede doblar los pines del conector cuando este se suelta de golpe.

### Configuración del software

Tras la instalación del hardware, el HAT puede requerir configuración de software para funcionar correctamente. Muchos HAT incluyen overlays de árbol de dispositivos que se deben habilitar en la configuración de Raspberry Pi. Editar `/boot/firmware/config.txt` y añadir las líneas `dtoverlay` adecuadas según indique la documentación del HAT.

!!! quote "Información relacionada"
    - **Referencia de la asignación de pines GPIO:** ver [Referencia de hardware](../technical-reference/hardware.md)
    - **Configuración del software:** ver [Configuración avanzada](../software-development/advanced-config.md)
    - **Modificaciones de la carcasa:** ver [Opciones de conectores personalizados](#custom-connector-options)

## Sustitución del SSD NVMe

### Compatibilidad de los SSD

HALPI2 admite SSD NVMe M.2 2230–2280 en la configuración estándar de una sola cara. Aunque las unidades 2230, más cortas, pueden ser de doble cara gracias al espacio libre adicional de esa posición de montaje, las unidades más largas deben ser de una sola cara para caber en la placa portadora.

La compatibilidad solo se puede garantizar con los SSD suministrados por Hat Labs y con los SSD oficiales de Raspberry Pi. Si se considera una unidad de terceros, conviene verificar su compatibilidad con Raspberry Pi 5 antes de la compra consultando los informes de usuarios y las listas de compatibilidad disponibles en internet. Entre los problemas habituales de las unidades incompatibles están el consumo excesivo, el sobrecalentamiento y los fallos de arranque o la inestabilidad del sistema.

### Preparación del SSD nuevo

Antes de instalar un SSD nuevo en HALPI2, conviene grabar el sistema operativo en la unidad. Aunque es posible grabar el SSD después de la instalación mediante el conector USB Boot del CM5 (j1), utilizar un adaptador externo de USB a NVMe resulta más fácil y rápido. El procedimiento de grabación se describe en la [Guía del software](./software.md).

### Desactivación de la tensión de 3,3 V del sistema

Los supercondensadores pueden mantener alimentada la línea de 3,3 V de la placa portadora durante bastante tiempo después de desconectar la alimentación principal. Como el SSD se alimenta desde la línea de 3,3 V, esta se debe desactivar para garantizar que el SSD queda completamente sin alimentación antes de retirarlo o instalarlo.

Comenzar apagando HALPI2 y desconectando la alimentación. Abrir la carcasa siguiendo el procedimiento descrito en la sección Acceso a la carcasa.

Localizar el puente «3.3V off» en la placa portadora. Su ubicación varía según la versión de la placa. En las placas v0.4.0, el puente está muy cerca de los supercondensadores, en su lado «sur». En las placas v0.5.0 y posteriores, localizar el conector «Pow.Ctrl» al «este» de los supercondensadores. Los pines «3.3V off» son los dos superiores del conector.

Mover el puente para cortocircuitar los pines «3.3V off». Esto desactiva la línea de 3,3 V, lo que se indica mediante el apagado de los LED.

### Procedimiento de retirada

La ranura M.2 se encuentra en el borde sur de la placa portadora. Consultar la imagen de la sección [Conectores de la placa portadora](#carrier-board-connectors) para localizar el conector M.2 etiquetado como **g1**.

Con un destornillador PH1, retirar el tornillo de montaje M2.5. Una vez retirado el tornillo, el SSD se levantará en ángulo. Levantar con suavidad la unidad por el extremo de montaje y extraerla del conector M.2 con un ligero movimiento de vaivén. Manipular el SSD por los bordes para no dañar los componentes ni los conectores.

### Procedimiento de instalación

Insertar el SSD preparado en el conector M.2 con un ángulo aproximado de 30 grados, comprobando que la muesca del SSD coincide con la guía del conector. La unidad debe deslizarse con suavidad, sin necesidad de forzarla. Una vez completamente asentada, presionar el extremo de montaje del SSD hasta que quede plano contra el separador.

Fijar el SSD con el tornillo de montaje M2.5 mediante un destornillador PH1. Apretar el tornillo lo justo para sujetar la unidad con firmeza. El SSD debe quedar perfectamente plano, sin curvatura ni flexión visibles.

Una vez colocado el SSD, retirar el puente de los pines «3.3V off» para volver a habilitar la línea de 3,3 V. Conservar el puente guardado en el conector para usos futuros.

Volver a montar la carcasa según se describe en la sección Acceso a la carcasa.
Para cualquier configuración de software o resolución de problemas, consultar la [Guía del software](./software.md).

!!! quote "Información relacionada"
    - **Imágenes del sistema:** ver [Guía del software](./software.md)
    - **Procedimientos de arranque:** ver [Funcionamiento del sistema](./operation.md)
    - **Acceso al hardware:** ver [Acceso a la carcasa](#enclosure-access)

## Sustitución del Compute Module 5

### Requisitos previos

La sustitución del Compute Module 5 exige una manipulación cuidadosa por la fragilidad de los conectores placa a placa. El CM5 utiliza dos conectores de alta densidad que se dañan con facilidad si se aplica una fuerza excesiva o una técnica inadecuada. Un módulo existente solo se debe retirar cuando sea absolutamente necesario, por ejemplo si está dañado o si se va a actualizar. Los daños en los conectores de montaje del módulo de cómputo, tanto en el CM5 como en la placa portadora, no están cubiertos por la garantía.

Antes de empezar, conviene disponer de almohadillas térmicas para la transferencia de calor. La configuración estándar utiliza una almohadilla de 1 mm de espesor sobre el SoC y almohadillas de 2 mm de espesor sobre el chip RP1 y los componentes de la fuente de alimentación interna. Las almohadillas térmicas existentes se pueden reutilizar si siguen intactas y limpias.

### Acceso al Compute Module

Apagar HALPI2 y desconectar la fuente de alimentación. Retirar la tapa de la carcasa siguiendo el procedimiento de la sección Acceso a la carcasa. Para acceder al CM5, que va montado en la cara inferior de la placa portadora, primero hay que retirar la placa portadora de la carcasa. Para no perder de vista los numerosos cables conectados a la placa portadora, se recomienda tomar algunas fotografías de las conexiones antes de continuar.

Desconectar los cables que impidan levantar la placa portadora. Retirar los tornillos de montaje de la placa portadora y levantar la placa de la carcasa.

### Retirada del módulo existente

!!! danger "Precaución"
    Si el módulo CM5 se desconecta un conector cada vez, las fuerzas de torsión pueden arrancar el conector del módulo CM5. Este daño no está cubierto por la garantía.

El CM5 está sujeto por dos conectores placa a placa que requieren una manipulación cuidadosa. No utilizar nunca herramientas metálicas en este procedimiento, ya que pueden dañar los conectores o los componentes de montaje superficial cercanos. Utilizar una espátula (spudger) de madera o de plástico, una púa de guitarra o una herramienta no conductora similar.

Colocar la herramienta en el centro del borde corto izquierdo del módulo CM5, entre el módulo y la placa portadora. Presionar con firmeza en las esquinas del lado derecho. Hacer palanca suavemente hacia arriba con una fuerza mínima: el módulo debe soltarse con un ligero clic y ambos conectores deben desprenderse a la vez.

![Retirada del módulo CM5](./unmount-cm5.jpg)
*Retirar el módulo CM5 presionando en las esquinas del borde derecho mientras se hace palanca hacia arriba en el centro del borde izquierdo. Ambos conectores deben desprenderse a la vez.*

### Instalación del módulo nuevo

Alinear el módulo CM5 nuevo con los conectores de la placa portadora, utilizando como guía el contorno serigrafiado en la placa portadora. El contorno del módulo impreso en la placa portadora debe coincidir exactamente con las dimensiones físicas del CM5 cuando la orientación es correcta.

Una vez alineado, aplicar una presión suave y uniforme en las posiciones de los conectores, en ambos bordes cortos del módulo. Se debe notar un leve clic al encajar los conectores. Presionar con firmeza, pero evitando flexionar la placa portadora: si es necesario, sujetarla por debajo. Ambos conectores deben quedar completamente asentados para un funcionamiento correcto.

A continuación, colocar las almohadillas térmicas sobre el módulo CM5. Las almohadillas térmicas se deben situar correctamente: una almohadilla de 1 mm sobre el SoC principal y almohadillas de 2 mm sobre el chip RP1 y los componentes de la fuente de alimentación. Si se reutilizan almohadillas existentes, comprobar que están limpias y bien colocadas.

![Colocación de las almohadillas térmicas en el CM5](./cm5-thermal-pads-annotated.jpg)
*Colocación de las almohadillas térmicas en el Compute Module 5. Utilizar una almohadilla de 1 mm de espesor sobre el SoC (centro) y almohadillas de 2 mm de espesor sobre el RP1 y los componentes de la fuente de alimentación. Las formas y los tamaños reales de las almohadillas térmicas pueden variar.*

### Conexión de la antena

Antes de volver a montar la placa portadora, conectar el cable de antena U.FL al conector de antena inalámbrica del CM5. Esta conexión resulta imposible de realizar una vez reinstalada la placa portadora. El conector U.FL requiere una alineación cuidadosa y una presión firme para asentarse correctamente. Se debe notar un chasquido claro cuando el conector queda completamente encajado. Hay que tener cuidado de no doblar el cuerpo del conector durante la instalación.

### Montaje final

Inspeccionar la instalación del módulo para comprobar que ambos conectores están completamente asentados y que el módulo queda plano contra la placa portadora, sin holguras. Las almohadillas térmicas deben hacer contacto con los componentes del módulo que generan calor.

Colocar de nuevo la placa portadora en la carcasa, comprobando que las almohadillas térmicas del CM5 quedan alineadas con las áreas de disipación correspondientes del fondo de la carcasa. Volver a instalar todos los tornillos de montaje de la placa portadora y reconectar los cables que se hayan desconectado durante la retirada.

Completar el montaje siguiendo el procedimiento estándar de cierre de la carcasa. En el primer arranque, el sistema debería reconocer automáticamente el CM5 nuevo.

!!! warning "Advertencia sobre los conectores"
    Los conectores placa a placa son los componentes más frágiles de este procedimiento. No utilizar nunca herramientas metálicas cerca de los conectores, aplicar únicamente fuerza vertical al retirarlos o instalarlos y comprobar que la alineación es perfecta antes de aplicar presión. Los conectores dañados suelen obligar a sustituir la placa portadora.

!!! quote "Información relacionada"
    - **Configuración del sistema tras la sustitución:** ver [Guía del software](./software.md)
    - **Resolución de problemas de arranque:** ver [Resolución de problemas](./troubleshooting.md)
    - **Gestión térmica:** ver [Referencia de hardware](../technical-reference/hardware.md)

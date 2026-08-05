---
translated_from: a51e1cfe53d070c073a563641f9301fd3383a418
---

# Primeros pasos

Esta guía permite poner el HALPI2 en funcionamiento en menos de 30 minutos y cubre además la instalación permanente. Conviene seguir estos pasos en orden para lograr una puesta en marcha sin contratiempos: primero una configuración de sobremesa para comprobar que todo funciona y, a continuación, la instalación permanente.

## Precauciones de seguridad y manipulación

!!! warning "Antes de empezar"
    - Asegurarse de que la alimentación del sistema eléctrico está desconectada antes de realizar las conexiones
    - Utilizar fusibles adecuados (3–5 A) para las conexiones de alimentación
    - Manipular la unidad con cuidado: aunque es robusta, una caída o un impacto pueden dañar los componentes internos
    - Comprobar que la polaridad es correcta al conectar los cables de alimentación
    - Evitar las descargas de electricidad estática: conviene descargarse a tierra y evitar frotar gatos y objetos de ámbar antes de tocar los componentes internos

## Material necesario

En el paquete del HALPI2:

- Unidad HALPI2 con CM5 y NVMe SSD preinstalados
- Cable de alimentación con conector E7T (2 m de longitud)

Elementos opcionales (incluidos en el paquete de venta):

- Par de conectores cilíndricos (barrel) de CC (5,5 × 2,1 mm), para el uso de una fuente de alimentación estándar de 12 V de tipo «wall wart» (transformador de enchufe)
- Antena WiFi/Bluetooth Raspberry Pi (necesaria si se utiliza WiFi para la configuración inicial)

Elementos adicionales (no incluidos):

- Fuente de alimentación de 12 V o 24 V
- Un ordenador aparte para la configuración sin pantalla (headless), si no se utiliza una pantalla conectada
- Cable de red (opcional, para la conexión por cable)
- Pantalla con entrada HDMI (opcional)
- Teclado y ratón USB (opcionales, para el acceso directo)

!!! tip "Consejo rápido"
    Cualquier dispositivo de red, como un router o un punto de acceso WiFi, suele utilizar una fuente de alimentación de 12 V que sirve para alimentar el HALPI2. ¡Merece la pena buscar una en el montón de hardware antiguo!

## Configuración de sobremesa

Se recomienda probar el HALPI2 en un escritorio o banco de trabajo antes de instalarlo de forma permanente. La configuración inicial puede realizarse sin pantalla, a través de una conexión de red, o con una pantalla, un teclado y un ratón conectados. La configuración sin pantalla puede hacerse mediante una conexión Ethernet por cable o mediante el punto de acceso WiFi del HALPI2.

### Paso 1: conectar los periféricos esenciales

#### Para la configuración inicial:

1. **Conexión de red (necesaria para la instalación sin pantalla):**
    - Conectar el cable Ethernet
    - Conectar la antena WiFi/Bluetooth

2. **Conexión de pantalla (opcional):**
    - Conectar una pantalla HDMI para el acceso directo
    - Teclado y ratón USB si se utiliza una pantalla

![Conectores del panel frontal](./front-panel-connectors.jpg)
*Conectores del panel frontal*

### Paso 2: conexión NMEA 2000 (opcional)

Si el HALPI2 se instala directamente en una embarcación o se dispone de una instalación NMEA 2000 de sobremesa, ya es posible conectarlo a la red NMEA 2000.

Una [red NMEA 2000](https://docs.hatlabs.fi/nmea2000/) consta de un cable troncal al que se conectan todos los dispositivos mediante conectores en T y cables de derivación. Añadir un conector en T al cable troncal de la red NMEA 2000. Conectar el conector micro NMEA 2000 del HALPI2 al conector en T mediante un cable de derivación NMEA 2000.

### Paso 3: conexión de la alimentación

!!! tip "Nota sobre la alimentación mediante NMEA 2000"
    El HALPI2 también puede alimentarse a través del bus NMEA 2000. Véase [Conexión de alimentación por el bus NMEA 2000](#conexion-de-alimentacion-por-el-bus-nmea-2000) en la sección Instalación permanente, más adelante.

Para la configuración de sobremesa se utiliza el cable de alimentación E7T suministrado. Conectar los extremos del cable de alimentación al conector cilíndrico hembra de la siguiente manera:

- **Cable rojo = positivo (+)**
- **Cable negro = negativo (−)**

![Conector E7T a conector cilíndrico](./e7t-barrel.jpg)
*Ejemplo del cableado del E7T al conector cilíndrico*

Conectar una fuente de alimentación estándar de 12 V o 24 V al conector cilíndrico. La fuente de alimentación debe estar dimensionada para al menos 1 A, a fin de cubrir las necesidades del HALPI2.

!!! warning "Advertencia"
    Al carecer de descarga de tracción, el conector cilíndrico de terminales de tornillo solo debe utilizarse en instalaciones temporales. Un tirón accidental del cable puede desconectarlo y dejar los conductores al descubierto.

## Primer arranque

El HALPI2 se entrega con [HaLOS](https://docs.halos.fi), una distribución de Linux basada en contenedores y con una interfaz web de gestión, diseñada para aplicaciones náuticas e industriales. Si se prefiere otro sistema operativo, como OpenPlotter o Raspberry Pi OS, véase la [Guía del software](../user-guide/software.md).

!!! info "Documentación de HaLOS"
    Esta guía cubre el hardware del HALPI2 y el primer encendido. Todo lo relativo al sistema operativo —configuración del primer arranque, red, aplicaciones, certificados y uso diario— se encuentra en la **[documentación de HaLOS](https://docs.halos.fi)**. Conviene tenerla a mano al seguir los pasos siguientes.

**Encender el HALPI2** conectando la fuente de alimentación, si no se ha hecho ya. Al cabo de unos segundos,
la barra de LED empieza a llenarse de luces rojas, lo que indica que los supercondensadores se están cargando. Los LED pasan a amarillo cuando el sistema arranca y, por último, a verde cuando el sistema operativo está en marcha y el demonio HALPI está conectado al controlador.

Si hay una pantalla conectada, aparece la pantalla de inicio de Raspberry Pi OS y, finalmente, el escritorio gráfico.

!!! tip "Consejo"
    Los patrones de los LED de estado están documentados en la [Guía de funcionamiento](../user-guide/operation.md).

### Acceso al HALPI2 sin pantalla

Si no hay ninguna pantalla conectada, se puede acceder al HALPI2 a través de su punto de acceso WiFi o de una conexión Ethernet. HaLOS ofrece una interfaz web: no hace falta ningún software adicional[^ssh].

[^ssh]: SSH también está disponible en las imágenes de HaLOS sin pantalla (activado de forma predeterminada). En las variantes Desktop, SSH se activa mediante `raspi-config`. Credenciales predeterminadas: nombre de usuario `pi`, contraseña `halos`.

En primer lugar, esperar a que los LED se pongan verdes, lo que indica que el sistema ha arrancado por completo. A continuación, seguir estos pasos:

**Opción 1 — Conexión mediante el punto de acceso WiFi:** HaLOS crea un punto de acceso WiFi llamado `Halos-XXXX` (único para cada dispositivo) con la contraseña `halos1234`. Conectar el ordenador a esta red.

El punto de acceso no dispone de internet propio, por lo que el paso siguiente consiste en dirigir el HALPI2 hacia una red WiFi que sí lo tenga (necesario para descargar las aplicaciones en contenedor en el primer arranque):

1. Abrir Cockpit en `https://halos.local:9090/` e iniciar sesión (nombre de usuario `pi`, contraseña `halos`).
2. Ir a **Networking** y hacer clic en **WiFi (wlan0)**.
3. Esperar a que aparezca la lista de redes disponibles y hacer clic en la red deseada.
4. Introducir la contraseña y hacer clic en **Add**.

El HALPI2 mantiene activo el punto de acceso `Halos-XXXX` mientras se une a la red, por lo que el ordenador puede desconectarse brevemente del punto de acceso y volver a conectarse por sí solo.

**Opción 2 — Conexión por Ethernet con cable:** si el HALPI2 se ha conectado a la red mediante Ethernet, obtiene automáticamente una dirección IP por DHCP.

Una vez establecida la conexión, abrir un navegador e ir a:

- **Panel de control:** `https://halos.local/` — el panel de control principal de Homarr, con enlaces a todas las aplicaciones instaladas
- **Administración del sistema:** `https://halos.local:9090/` — Cockpit para la gestión del sistema, las actualizaciones y las aplicaciones en contenedor

!!! note "Aviso de certificado SSL"
    La primera vez que se abre el panel de control o Cockpit, el navegador muestra un aviso de «No es seguro». HaLOS firma sus servicios web con una autoridad de certificación (CA) que genera en el propio dispositivo, y el navegador todavía no confía en esa CA. Por ahora, aceptar el aviso para continuar.

    Para eliminar el aviso de forma definitiva, basta con instalar una sola vez la CA del dispositivo en el ordenador; a partir de ese momento todos los servicios de HaLOS se validan correctamente en cualquier puerto. Abrir `https://halos.local/ca/` para acceder a un instalador guiado según la plataforma, o consultar [Confiar en el dispositivo](https://docs.halos.fi/user-guide/trust-the-device/) en la documentación de HaLOS.

!!! info "Se necesita internet en el primer arranque"
    La interfaz de Cockpit está disponible de inmediato, pero el panel de control principal y las demás aplicaciones basadas en contenedores necesitan una conexión a internet en el primer arranque para descargar sus imágenes de contenedor. Conectar el HALPI2 a internet mediante Ethernet o configurar el WiFi a través de Cockpit.

### Configuración del primer arranque

!!! warning "Advertencia"
    HaLOS incluye contraseñas predeterminadas que **deben** cambiarse durante el primer arranque para impedir el acceso no autorizado al dispositivo.

HaLOS tiene dos conjuntos de credenciales:

| Tipo de acceso | Nombre de usuario | Contraseña predeterminada | Uso |
|:---------------|:------------------|:--------------------------|:----|
| SSO (aplicaciones web) | `admin` | `halos` | Panel de control, Signal K, Grafana y otras aplicaciones web |
| Sistema (SSH/Cockpit) | `pi` | `halos` | Acceso SSH, administración del sistema con Cockpit |

#### Cambio de contraseñas

- **Contraseña SSO:** se cambia mediante Authelia (accesible desde el panel de control)
- **Contraseña del sistema:** se cambia mediante Cockpit (`https://halos.local:9090/`) en los ajustes de la cuenta de usuario, o por SSH con `passwd`

Para instrucciones detalladas sobre el primer arranque, véase la [guía de primeros pasos de HaLOS](https://docs.halos.fi/getting-started/first-boot/).

!!! info "¿Se utiliza OpenPlotter o Raspberry Pi OS?"
    Si se ha grabado un sistema operativo alternativo, véase la [Guía del software](../user-guide/software.md#configuracion-inicial-del-sistema) para conocer las instrucciones de configuración propias de cada sistema.

### Comprobación de la conexión NMEA 2000 (opcional)

La forma más sencilla de comprobar la conectividad NMEA 2000 es consultar el estado del servidor Signal K. En las variantes de imagen HaLOS Marine, Signal K viene preinstalado y es accesible desde el panel de control en `https://halos.local/`. En las imágenes de HaLOS no náuticas, Signal K puede instalarse desde la tienda de aplicaciones en contenedor de Cockpit.

Abrir la interfaz web de Signal K y observar la actividad de la conexión `can0`: debería verse la recepción de algo de tráfico.

![Actividad de las conexiones del servidor Signal K](./sk-n2k-deltas.jpg)

## Apagado del dispositivo

El HALPI2 está diseñado para apagarse automáticamente al desconectarse de la alimentación. Para apagar el dispositivo basta con cortar la corriente, ya sea con un interruptor del cuadro eléctrico o desconectando el conector de alimentación. El sistema inicia automáticamente una secuencia de apagado por software, de modo que todas las aplicaciones se cierran correctamente y el sistema de archivos se desmonta de forma segura.

Si el sistema se apaga desde la interfaz de escritorio o con herramientas de línea de comandos (como el comando `shutdown`), el dispositivo se reinicia automáticamente al cabo de unos 5 segundos. Este comportamiento se debe a que el sistema de gestión de la alimentación detecta que la alimentación externa sigue disponible.

Durante el proceso de apagado, el estado del sistema puede supervisarse mediante los indicadores LED del panel frontal. Al cortarse la corriente, los LED verdes se atenúan para señalar una situación de corte de corriente. Transcurridos 5 segundos, los LED cambian a violeta, lo que indica con claridad que el dispositivo se está apagando. Una vez completado el proceso de apagado, todos los LED se apagan.

En condiciones normales, el proceso de apagado suele durar solo unos segundos. Sin embargo, en algunos casos ciertos servicios necesitan más tiempo para detenerse correctamente. Cuando esto ocurre, el dispositivo puede agotar casi por completo los supercondensadores antes de apagarse. Esta prolongación del apagado es un comportamiento normal y no indica ningún fallo del sistema.

## Resolución de problemas en la puesta en marcha

### Problemas frecuentes y poco frecuentes:

❌ **No hay alimentación ni LED:**

- Comprobar las conexiones de alimentación y la polaridad
- Comprobar el estado del fusible
- Asegurarse de que la tensión está dentro del rango de 11–32 V

❌ **El punto de acceso WiFi no aparece:**

- Asegurarse de que la antena está bien conectada
- Probar a conectarse con otro dispositivo
- Comprobar si el HALPI2 ha arrancado por completo (los LED deben estar verdes)
- Probar primero la conexión por Ethernet

❌ **No se puede acceder al dispositivo mediante `halos.local`:**

- Probar con la dirección IP asignada (consultar la lista de clientes DHCP del router)

❌ **Hay una pantalla conectada, pero no muestra nada:**

- Asegurarse de que el cable HDMI está bien conectado
- Asegurarse de que la pantalla está encendida y con la entrada correcta seleccionada
- Probar con otro cable HDMI u otro puerto de la pantalla
- Asegurarse de que el HALPI2 está encendido (los LED deben estar amarillos o verdes)
- Si los LED parpadean con un patrón de arcoíris, el Compute Module 5 no está bien asentado. Puede deberse a daños durante el transporte. Seguir las instrucciones de la [Guía del usuario](../user-guide/operation.md) para volver a asentar el CM5, o contactar con el servicio de soporte.

❌ **La pantalla conectada muestra un mensaje de error sobre «nvme»:**

- Esto indica que el NVMe SSD no se detecta o no se ha inicializado correctamente. Puede deberse a daños durante el transporte. Seguir las instrucciones de la [Guía del usuario](../user-guide/operation.md) para volver a asentar el NVMe SSD, o contactar con el servicio de soporte.

### Cómo obtener ayuda:

- **Documentación:** consultar las secciones específicas para una resolución de problemas detallada
- **Comunidad:** participar en los foros de la comunidad de Hat Labs
- **Soporte:** contactar con el soporte técnico para los problemas de hardware

---

## Instalación permanente

Una vez comprobado que todo funciona sobre la mesa, seguir estos pasos para el montaje y el cableado definitivos.

### Planificación de la instalación

!!! tip "Consejo rápido"
    Conviene fotografiar el cableado existente antes de modificarlo: resulta útil para resolver problemas más adelante.

Conviene dedicar tiempo a planificar la instalación. Aspectos a tener en cuenta:

- **Ubicación de montaje**: accesibilidad, protección, ventilación
- **Tendido de cables**: recorridos más cortos, protección frente a daños
- **Fuente de alimentación**: circuito dedicado o compartido, requisitos de fusibles
- **Integración en la red**: NMEA 2000, Ethernet, cobertura WiFi
- **Factores ambientales**: temperatura, humedad, vibraciones

#### Herramientas y materiales necesarios

**Herramientas:**

- Taladro con brocas
- Juego de destornilladores (PH2 Phillips, plano grande)
- Pelacables y tenazas de crimpar para las conexiones de alimentación
- Multímetro para las comprobaciones
- Pistola de aire caliente o mechero (para el tubo termorretráctil)

**Materiales (no incluidos):**

- Tornillos de montaje (4 mm o M4, según la superficie de montaje)
- Fusibles adecuados (3–5 A) o interruptores automáticos del cuadro eléctrico con el valor nominal correspondiente
- Cable de calidad náutica (1,5 mm² o 16 AWG para la alimentación, si el cable suministrado es demasiado corto)
- Tubo termorretráctil y terminales
- Bridas y clips de sujeción

### Montaje

#### Elección de la ubicación

Elegir una ubicación de montaje que ofrezca:

!!! tip "Condiciones de montaje óptimas"
    - **Rango de temperatura:** −20 °C … +60 °C de temperatura ambiente
    - **Ventilación:** espacio libre suficiente alrededor de la carcasa
    - **Protección:** alejada de las salpicaduras directas de agua y de los daños mecánicos
    - **Acceso:** acceso fácil a los conectores y a los LED de estado
    - **Soporte:** superficie de montaje sólida, capaz de soportar 2 kg más los cables
    - **Espacio:** dejar al menos 100 mm de espacio libre delante de los conectores del panel para el tendido de cables.

Aunque esta guía se centra en las instalaciones fijas, en la práctica suele bastar con colocar el dispositivo en un estante o sobre una mesa, siempre que quede estable y protegido de la humedad y los impactos.

#### Recomendaciones ambientales

**Instalaciones náuticas:**

- Montar por encima del nivel previsto del agua de sentina
- Evitar las zonas con salpicaduras directas o agua estancada
- Tener en cuenta el movimiento y las vibraciones de la embarcación, y fijar bien todas las conexiones
- Utilizar herrajes de montaje resistentes a la corrosión

**Instalaciones en vehículos:**

- Proteger del calor y las vibraciones del motor
- Asegurar una ventilación adecuada en espacios cerrados
- Tener en cuenta la accesibilidad para el mantenimiento
- Utilizar un montaje resistente a las vibraciones

**Instalaciones industriales:**

- Proteger de los productos químicos del proceso y de las temperaturas extremas
- Tener en cuenta las fuentes de interferencias electromagnéticas
- Asegurar la conformidad con la normativa eléctrica local
- Prever el acceso para el mantenimiento rutinario

#### Orientación de montaje

!!! info "Orientación recomendada"
    **Preferible:** conectores orientados hacia abajo

    - Reduce el riesgo de entrada de agua
    - Mejora el tendido de cables
    - Facilita el acceso para el mantenimiento

    **Aceptable:** conectores orientados hacia un lado

    - Asegurar un drenaje adecuado
    - Utilizar juntas en las entradas de cables

    **Evitar:** conectores orientados hacia arriba

    - Aumenta el riesgo de entrada de agua
    - Dificulta el tendido de cables

#### Pasos de montaje

##### Paso 0: descargar e imprimir la plantilla de taladrado

Descargar la [plantilla de taladrado del HALPI2](./HALPI2_enclosure_1B_Drill_Template_v2.pdf) e imprimirla a escala 100 %. Esta plantilla permite marcar con precisión los agujeros de montaje. Si no se dispone de impresora, también pueden utilizarse las cotas indicadas en la plantilla para marcar los agujeros a mano, o emplear la propia carcasa para marcarlos directamente sobre la superficie de montaje.

[![Plantilla de taladrado](./HALPI2_enclosure_1B_Drill_Template_v2.png)](./HALPI2_enclosure_1B_Drill_Template_v2.pdf)

##### Paso 1: preparar la superficie de montaje

1. **Limpiar la superficie de montaje**
2. **Marcar los agujeros de montaje** con la plantilla impresa
3. **Probar el ajuste** de la carcasa antes de la instalación
4. **Taladrar los agujeros guía** para los tornillos de montaje

##### Paso 2: instalar el HALPI2

1. **Colocar la carcasa** con los conectores en la orientación preferible
2. **Apretar los tornillos de montaje**: firmes, pero sin excederse en el par

### Instalación permanente de la alimentación

#### Elección de la fuente de alimentación

**Opción 1: conector de alimentación dedicado**

- La opción más fiable y flexible
- Admite toda la capacidad de potencia
- Facilita el mantenimiento y la resolución de problemas

**Opción 2: alimentación por el bus NMEA 2000**

- Simplifica el cableado en las instalaciones náuticas
- Limitada a un consumo de 0,9 A
- Exige prestar especial atención a la caída de tensión

#### Configuración de la limitación de corriente

El HALPI2 incorpora un limitador de corriente de entrada que gestiona la carga inicial de los supercondensadores y protege la instalación frente a situaciones de sobrecorriente. El límite de corriente puede fijarse en 0,9 A o en 2,5 A, según la fuente de alimentación y los requisitos de la aplicación. El valor predeterminado de 0,9 A es adecuado para la mayoría de las aplicaciones.

Para acelerar el arranque inicial o alimentar periféricos de alto consumo, puede pasarse al ajuste de 2,5 A. Seguir los pasos descritos en la [Guía del usuario](../user-guide/operation.md) para modificar el límite de corriente.

#### Conexión de alimentación dedicada

##### Preparación del cable

1. **Tender el cable de alimentación** desde el HALPI2 hasta la fuente de alimentación
2. **Dejar bucles de servicio** en ambos extremos
3. **Proteger el cable** del roce y de posibles daños
4. **Cortar a medida** dejando margen de trabajo suficiente

##### Conexión en la fuente de alimentación

1. **Garantizar la protección del cable** asignando un interruptor automático de 3–5 A o instalando un fusible en línea
2. **Pelar los extremos del cable** con la longitud adecuada
3. **Instalar los terminales** con una técnica de crimpado correcta
4. **Conectar a la fuente de alimentación:**
    - **Cable rojo:** terminal positivo (+)
    - **Cable negro:** terminal negativo (−)
5. **Comprobar la polaridad** con el multímetro antes de aplicar tensión

##### Conexión en el HALPI2

El conector E7T viene precableado y no requiere ninguna terminación en campo. Basta con enchufarlo a la toma de alimentación del HALPI2.

#### Conexión de alimentación por el bus NMEA 2000

!!! info "Requisitos previos"
    - El conmutador del límite de corriente **debe** estar fijado en 0,9 A
    - La red NMEA 2000 debe disponer de capacidad de alimentación suficiente
    - El cable de derivación debe quedar cerca de la alimentación de la red para minimizar la caída de tensión

##### Componentes necesarios

- Cable de derivación NMEA 2000 (no incluido)
- Conector en T para la integración en el cable troncal (no incluido)

##### Pasos de instalación

1. **Apagar** todos los dispositivos NMEA 2000
2. **Abrir la carcasa del HALPI2** (véanse las instrucciones en la [Guía del usuario](../user-guide/operation.md))
3. **Localizar el conector de alimentación de la placa portadora**
4. **Desconectar el bloque de terminales existente**
5. **Conectar el bloque de terminales interno de alimentación NMEA 2000** al conector de alimentación de la placa portadora
6. **Comprobar el límite de corriente**: debe estar fijado en 0,9 A
7. **Conectar al cable troncal** con el cable de derivación y el conector en T adecuados
8. **Probar la instalación** antes del cierre definitivo
9. **Volver a montar la carcasa**

![Cableado de alimentación NMEA 2000](./n2k-power-conx.jpg)
*Para alimentar el HALPI2 por NMEA 2000, desconectar el bloque de terminales 1 y sustituirlo por el bloque de terminales 2.*

### Conexiones de red y de datos

#### Conexión de datos NMEA 2000

Incluso con una conexión de alimentación dedicada, puede interesar disponer de conectividad de datos NMEA 2000:

1. **Instalar el conector en T** en el cable troncal NMEA 2000
2. **Conectar el cable de derivación** entre el conector en T y el HALPI2
3. **Comprobar la terminación correcta** de la red NMEA 2000
4. **Probar la conectividad** después de la instalación

#### Conexión Ethernet

Para la conectividad de red:

1. **Utilizar cable de calidad náutica** o adecuado para el entorno
2. **Instalar prensaestopas o pasacables** si el tendido atraviesa mamparos
3. **Dejar bucles de servicio** en ambos extremos
4. **Probar la conectividad** antes de la instalación definitiva

#### Antena WiFi/Bluetooth

1. **Instalar la antena** en el conector RP-SMA
2. **Orientarla para una cobertura óptima**: alejada de obstáculos metálicos. En armarios metálicos puede ser necesario un cable alargador RP-SMA de macho a hembra.
3. **Comprobar la intensidad de la señal** en la posición definitiva

### Resolución de problemas de instalación

#### Problemas de alimentación

❌ **No hay indicación de alimentación:**

- Comprobar el estado y el valor nominal del fusible
- Comprobar la tensión de la fuente de alimentación (11–32 V)
- Confirmar que la polaridad es correcta
- Comprobar la continuidad de los cables de alimentación

❌ **Alimentación intermitente:**

- Comprobar el apriete de todas las conexiones
- Inspeccionar los terminales en busca de corrosión
- Comprobar que la sección del conductor es adecuada para la corriente

#### Conectividad de red

❌ **No hay comunicación NMEA 2000:**

- Comprobar la terminación de la red (120 Ω en ambos extremos)
- Comprobar la instalación del conector en T
- Confirmar la integridad del cable de derivación
- Probar con un dispositivo que se sepa que funciona

❌ **No hay conectividad Ethernet:**

- Probar el cable con un comprobador de cables
- Comprobar la configuración del switch o del router
- Comprobar si hay conflictos de direcciones IP
- Confirmar la categoría del cable (Cat5e como mínimo)

#### Problemas ambientales

❌ **Entrada de humedad:**

- Inspeccionar el estado de todas las juntas
- Comprobar la orientación de los conectores
- Revisar los puntos de entrada de cables
- Valorar una protección adicional

❌ **Sobrecalentamiento:**

- Alejar el dispositivo de las fuentes de calor
- Comprobar que el flujo de aire alrededor de la carcasa no está obstruido

### Seguridad y conformidad

#### Seguridad eléctrica

- **Utilizar fusibles adecuados** para la protección contra sobrecorriente
- **Asegurar una puesta a tierra correcta** conforme a la normativa local
- **Proteger frente a cortocircuitos** con un tendido adecuado

#### Instalaciones náuticas

- **Seguir las normas locales o las ABYC** para las instalaciones eléctricas
- **Utilizar componentes de calidad náutica** en toda la instalación

#### Instalaciones industriales

- **Cumplir la normativa eléctrica local**
- **Asegurar una protección adecuada frente a EMI/RFI**
- **Documentar la instalación** conforme a los requisitos de la planta

## Pasos siguientes

Una vez que el HALPI2 está en funcionamiento:

1. **Explorar la [Guía del usuario](../user-guide/operation.md)** para conocer las instrucciones de funcionamiento detalladas
2. **Revisar los casos de uso habituales** para la configuración específica de cada aplicación
3. **Consultar la referencia técnica** para conocer las opciones de configuración avanzadas
4. **Unirse a la comunidad** para obtener consejos, trucos y soporte

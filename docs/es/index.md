# Introducción

HALPI2 es un ordenador de a bordo listo para usar basado en el Raspberry Pi Compute Module 5 (CM5). Ofrece un conjunto completo de prestaciones muy adecuado para aplicaciones náuticas, de automoción y para numerosas aplicaciones industriales.

![HALPI2](./halpi2_front_view.jpg)

!!! note "Enlace a la tienda"
    HALPI2 puede adquirirse en la [tienda web de Hatlabs](https://shop.hatlabs.fi/products/halpi2-computer).

## ¿Qué es HALPI2?

HALPI2 representa la última evolución de la informática embebida robusta, y combina la potencia y el ecosistema de Raspberry Pi con prestaciones especializadas para entornos exigentes. A diferencia de los ordenadores de placa única convencionales, HALPI2 está diseñado desde cero para el funcionamiento 24/7 en condiciones adversas, donde la fiabilidad es primordial.

El sistema integra un Raspberry Pi Compute Module 5 con una placa portadora propia, todo ello alojado en una carcasa estanca de aluminio que hace a la vez de disipador térmico. Este diseño aporta la potencia de cálculo que exigen las aplicaciones modernas y mantiene al mismo tiempo la robustez necesaria para el uso náutico e industrial.

## Características y prestaciones principales

### Características de la carcasa

- **Carcasa estanca (IP65) de aluminio**, de 200×130×60 mm
- **Conectores estándar** para alimentación, NMEA 2000, ethernet gigabit, HDMI, 2× USB 3.0 y antena WiFi/Bluetooth
- **Conectividad flexible**, con opción de 3× prensaestopas PG7 o conectores estancos SP13
- **Compatibilidad con antenas externas** mediante troqueles para 2 conectores SMA adicionales
- **Diseño para montaje en pared**, con los conectores situados para facilitar la instalación

![Disposición de los conectores del HALPI2](./user-guide/front-panel-connectors-all.jpg)

### Características del hardware

- **Amplio rango de tensión de entrada**, de 10 a 32 V CC, con protección hasta 100 V CC
- **Limitación de corriente inteligente**: corriente máxima de entrada de 0,9 o 2,5 A, seleccionable por el usuario
- **Doble opción de alimentación**: conexión directa a 12 V/24 V o alimentación de 12 V desde el bus NMEA 2000
- **Respaldo por supercondensadores** para la inmunidad a microcortes y el apagado controlado ante una pérdida de alimentación
- **Gestión avanzada de la alimentación**, con detección automática de la pérdida de alimentación
- **Diseño de refrigeración pasiva**, con el CM5 en contacto directo con la carcasa
- **Almacenamiento de alta velocidad** mediante una interfaz estándar M.2 NVMe SSD
- **Capacidad de ampliación** a través del conector GPIO de 40 pines estándar de Raspberry Pi
- **Amplias opciones de E/S**: 2× HDMI, 2× MIPI (DSI/CSI), 4× USB 3.0, ethernet gigabit
- **Interfaces específicas para náutica**: CAN FD (NMEA 2000) y RS-485 (NMEA 0183)
- **Reloj de tiempo real** con pila de respaldo para mantener la hora con precisión
- **Indicación visual del estado** mediante cinco LED RGB
- **Interacción con el usuario** a través de conectores de pines de botón configurables

![Vista interior del HALPI2](./halpi2-interior.jpg)
*Vista interior del HALPI2, con la placa portadora y los distintos conectores.*

### Características del software

- **Imágenes del sistema operativo preconfiguradas**, listas para su puesta en marcha inmediata: [HaLOS](https://docs.halos.fi) (predeterminada), OpenPlotter, Raspberry Pi OS y Raspberry Pi OS Lite
- **Supervisión completa** de tensión, corriente y temperatura
- **Actualizaciones de firmware transparentes** a través de la interfaz I2C

## Aplicaciones previstas

### Aplicaciones náuticas

- **Sistemas de navegación** con plóteres cartográficos e integración de GPS
- **Registro de datos** de parámetros del motor, sensores ambientales y rendimiento de la embarcación
- **Servidores Signal K** para la gestión unificada de los datos de la embarcación
- **Informática de a bordo de propósito general** para el acceso a internet y las comunicaciones
- **Depuración de redes NMEA 2000** para mejorar la fiabilidad del sistema

### Aplicaciones industriales

- **Supervisión de procesos** y sistemas de control
- **Detección ambiental** y adquisición de datos
- Estaciones de **supervisión remota**
- **Automatización de equipos** y control
- Sistemas de **mantenimiento predictivo**

### Aplicaciones de automoción

- Sistemas de **gestión de flotas**
- **Telemática** y seguimiento de vehículos
- Sistemas de **infoentretenimiento a bordo**
- Plataformas de **diagnóstico y supervisión**

## Contenido de la caja

El paquete de HALPI2 incluye:

- **Unidad HALPI2** con Compute Module 5 y NVMe SSD preinstalados (salvo que se haya pedido sin ellos)
- **Cable de alimentación** con conector E7T (compatible con Amphenol LTW Ceres Mini), de 2 m de longitud
- **Clavija de cable E7T** para instalaciones personalizadas
- **Par de conectores cilíndricos (barrel) de CC** (5,5 × 2,1 mm) para su uso con fuentes de alimentación estándar de 12 V/24 V
- **Antena Raspberry Pi** para la conectividad WiFi y Bluetooth
- **3 prensaestopas PG7** para interfaces adicionales
- **Guía de inicio rápido y documentación de garantía** para empezar

![Contenido de la bolsa de accesorios del HALPI2](./goodie-bag-contents.jpg)

Accesorios adicionales disponibles por separado:

- **Cable de derivación NMEA 2000** para aplicaciones alimentadas desde el bus
- **Diversos kits de conectores** para instalaciones personalizadas

## Cómo usar esta documentación

Esta documentación está estructurada para atender tanto a los usuarios finales que buscan orientación práctica como a los desarrolladores profesionales que necesitan información técnica detallada.

### Para usuarios finales

- Empezar por la guía **Primeros pasos** para la puesta en marcha y la instalación
- Consultar **Casos de uso habituales** para obtener orientación específica de cada aplicación
- Recurrir a **Resolución de problemas** cuando surja alguna incidencia

### Para desarrolladores

- Revisar la **Referencia técnica** para conocer las especificaciones detalladas
- Estudiar las secciones de **Desarrollo de software** para las aplicaciones personalizadas
- Examinar los **Archivos de diseño** para planificar la integración
- Consultar la **Configuración avanzada** para optimizar el rendimiento

### Sugerencias sobre la documentación

- 💡 Los cuadros de **consejos rápidos** ofrecen atajos para las tareas habituales
- ⚠️ Los avisos de **advertencia** y **precaución** destacan información de seguridad importante
- 🔧 Las secciones de **detalles técnicos** ofrecen información pormenorizada sobre la implementación
- 📖 Las **referencias cruzadas** enlazan temas relacionados a lo largo de la documentación

Tanto si se trata de poner en marcha un primer ordenador náutico como de desarrollar una solución industrial a medida, esta documentación guía paso a paso a lo largo de toda la experiencia con HALPI2.

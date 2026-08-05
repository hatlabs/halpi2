---
translated_from: a428b6a7e1ca303e0571592a86d0cc6a3db97a83
---

# Guía del software

## Imágenes del sistema operativo

Hat Labs ofrece imágenes precompiladas para el HALPI2. Todas las imágenes incluyen la configuración y las personalizaciones necesarias para el hardware del HALPI2, entre ellas CAN (NMEA 2000) como dispositivo de red `can0`, RS-485 (NMEA 0183) como `/dev/ttyAMA4` y el paquete `halpi2-firmware`.

### HaLOS (predeterminado)

[HaLOS](https://docs.halos.fi) es una distribución de Linux basada en contenedores, diseñada para aplicaciones náuticas e industriales. Proporciona una interfaz web para la administración del sistema, la gestión de aplicaciones y la supervisión, sin necesidad de pantalla, teclado ni VNC.

**Variantes de imagen:**

| Imagen | Descripción |
|:------|:------------|
| Halos-HALPI2 | Imagen base sin pantalla (headless) con Cockpit y gestión de contenedores |
| Halos-HALPI2-Desktop | Imagen base con el escritorio de Raspberry Pi |
| Halos-HALPI2-Marine | Sin pantalla, con aplicaciones náuticas (Signal K, Grafana, InfluxDB, AvNav) |
| Halos-HALPI2-Desktop-Marine | Escritorio con aplicaciones náuticas |

Las imágenes de HaLOS se descargan desde la [página de versiones de HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest). La documentación detallada está en [docs.halos.fi](https://docs.halos.fi).

### OpenPlotter

OpenPlotter es una imagen basada en Raspberry Pi OS con añadidos para aplicaciones náuticas. Ofrece un entorno de escritorio tradicional con acceso remoto por VNC, e incluye Signal K y OpenCPN preinstalados.

Si no se utilizan pantalla, teclado y ratón con el HALPI2, es posible conectarse al ordenador mediante un cable Ethernet o a través del punto de acceso WiFi (`OpenPlotter`, contraseña `12345678`).

Con cualquiera de las dos vías se puede acceder al ordenador HALPI2 mediante VNC o SSH. Para usar VNC es necesario descargar el [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) de RealVNC.

Dado que tanto el punto de acceso como el usuario predeterminado vienen con contraseñas predeterminadas, es imprescindible cambiarlas inmediatamente después del primer arranque. El procedimiento se describe en la [documentación de OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

Las imágenes de OpenPlotter se descargan desde [GitHub](https://github.com/hatlabs/openplotter-halpi/releases).

### Raspberry Pi OS y Raspberry Pi OS Lite

Si se prefiere utilizar el Raspberry Pi OS estándar, se puede descargar la última
imagen compatible con el HALPI2 desde [el repositorio de GitHub](https://github.com/hatlabs/openplotter-halpi/releases).
Grabar la imagen en el disco SSD con Raspberry Pi Imager. Durante la grabación
se pueden aplicar personalizaciones como el nombre de host, la activación de SSH
o la configuración del WiFi.

Si se decide no aplicar personalizaciones, hace falta tener una pantalla y un
teclado conectados al HALPI2 para completar la configuración inicial. En el
primer arranque se solicitarán un nombre de usuario y una contraseña.


## Grabación de una imagen del sistema operativo en el SSD

Hay dos métodos disponibles para grabar una imagen del sistema operativo en el SSD NVMe del HALPI2: extraer el SSD y usar un adaptador USB NVMe, o grabar directamente en la unidad HALPI2. Se recomienda el método del adaptador USB NVMe por comodidad y facilidad de uso, ya que estos adaptadores se encuentran en internet a bajo precio y ofrecen un proceso de grabación sencillo.

### Grabación mediante un adaptador USB NVMe

Para grabar la imagen con el método del adaptador USB NVMe, empezar por extraer el SSD NVMe de la unidad HALPI2 siguiendo el procedimiento descrito en la [Guía del hardware](./hardware.md#sustitucion-del-ssd-nvme). A continuación, descargar una imagen compatible con el HALPI2 — una [imagen de HaLOS](https://github.com/halos-org/halos-pi-gen/releases/latest) o una [imagen de OpenPlotter/Raspberry Pi OS](https://github.com/hatlabs/openplotter-halpi/releases) —, asegurándose de elegir la imagen adecuada para el uso previsto.

Insertar el SSD en el adaptador USB NVMe y conectarlo al ordenador. Utilizar Raspberry Pi Imager para grabar la imagen descargada en el SSD NVMe. Si se graba una imagen de Raspberry Pi OS, se pueden editar y aplicar los ajustes de personalización del sistema operativo durante el proceso de grabación. Sin embargo, si no se aplican ajustes personalizados, harán falta un teclado y un ratón USB conectados al HALPI2 para la configuración inicial posterior a la instalación.

Con las imágenes de HaLOS **no** deben aplicarse ajustes de personalización del sistema operativo durante el proceso de grabación. HaLOS se configura después del arranque a través de su interfaz web.

De forma similar, con la imagen de OpenPlotter **no** deben aplicarse ajustes de personalización del sistema operativo durante el proceso de grabación. La configuración se realiza después del primer arranque con las herramientas de configuración de Raspberry Pi y de OpenPlotter.

Una vez completado el proceso de grabación, desconectar el adaptador y extraer el SSD. Volver a insertar el SSD en la unidad HALPI2 siguiendo el procedimiento de instalación descrito en la Guía del hardware y montar de nuevo la carcasa según esa misma guía.

### Grabación directa en el HALPI2

Como alternativa, es posible grabar la imagen del sistema operativo directamente en el HALPI2 sin extraer el SSD. Este método sigue el procedimiento estándar de grabación del Compute Module documentado en la [documentación de Raspberry Pi](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Las instrucciones de preparación de la placa que allí figuran están escritas para la CM5 IO Board, pero el proceso es similar en el HALPI2.

**Requisitos previos.** Instalar la herramienta `rpiboot` del [repositorio `usbboot`](https://github.com/raspberrypi/usbboot) de Raspberry Pi. En Linux y macOS, compilarla e instalarla desde el código fuente como se describe en el README del repositorio; en Windows, instalar Raspberry Pi Imager o el instalador independiente de `rpiboot` enlazado en esa misma página.

Para preparar el HALPI2 para la grabación por USB:

1. Apagar el sistema por completo y abrir la tapa de la carcasa siguiendo el procedimiento descrito en la [Guía del hardware](./hardware.md#acceso-a-la-carcasa).
2. Localizar el conector USB-C etiquetado «USB Boot» a la derecha del contorno del HAT en la placa portadora y pasar el interruptor de modo de arranque adyacente a la posición «Abnormal». (Todavía no hay indicación por LED — el dispositivo está sin alimentación.)
3. Conectar un cable USB entre el ordenador y el conector «USB Boot» del HALPI2 y volver a alimentar el dispositivo. Se encenderá un LED ámbar junto al interruptor de modo de arranque, lo que confirma que el HALPI2 está en modo de arranque USB.
4. Ejecutar `rpiboot` en el ordenador. Detectará el HALPI2 y cargará el firmware de dispositivo de almacenamiento masivo; el HALPI2 aparece entonces como un dispositivo de almacenamiento masivo USB.
5. Devolver el interruptor de modo de arranque a la posición «Normal» en cuanto `rpiboot` termine correctamente y aparezca el dispositivo de almacenamiento masivo. Esto no interrumpe la sesión de grabación y garantiza que el HALPI2 arranque con normalidad desde la imagen recién grabada tras el siguiente ciclo de alimentación. Dejarlo en «Abnormal» hace que el dispositivo vuelva a entrar en modo de arranque USB en el siguiente arranque en lugar de iniciar el nuevo sistema operativo.
6. Grabar la imagen del sistema operativo con Raspberry Pi Imager (o cualquier otra herramienta capaz de escribir en un dispositivo de bloques), tomando como destino el nuevo dispositivo de almacenamiento masivo.
7. Desconectar el cable USB al terminar la grabación, realizar un ciclo de alimentación del HALPI2 y cerrar la carcasa.

!!! tip "Ciclo de alimentación sin desconectar nada"
    Con la carcasa ya abierta, la forma más rápida de reiniciar el HALPI2 es cortocircuitar brevemente los dos pines inferiores de los conectores de pines «Button Headers» situados junto al conector USB-C. Tocar ambos pines a la vez con la carcasa metálica de un conector de cable USB-C funciona bien y es seguro.

## Configuración inicial del sistema

Tras grabar y arrancar el HALPI2 por primera vez, son necesarios varios pasos de configuración para garantizar un funcionamiento seguro y correcto del sistema.

### Configuración de HaLOS

HaLOS se configura íntegramente a través de su interfaz web. Después del primer arranque, se accede a Cockpit en `https://halos.local:9090/` y al panel de control en `https://halos.local/`. Las contraseñas predeterminadas deben cambiarse de inmediato — véanse la guía [Primeros pasos](../getting-started/getting-started.md#configuracion-del-primer-arranque) y la [documentación de HaLOS](https://docs.halos.fi/getting-started/first-boot/) para más detalles.

### Configuración de OpenPlotter

Con la imagen de OpenPlotter, el sistema arranca con contraseñas predeterminadas tanto para el punto de acceso WiFi como para la cuenta de usuario predeterminada. Por motivos de seguridad, es imprescindible cambiar estas contraseñas inmediatamente después del primer arranque.

El procedimiento de cambio de contraseña y la configuración inicial se describen en la guía [Primeros pasos](../getting-started/getting-started.md#configuracion-del-primer-arranque) y en la [documentación de OpenPlotter](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Configuración de Raspberry Pi OS

Si se ha optado por el Raspberry Pi OS estándar en lugar de OpenPlotter, hay que seguir el proceso de configuración estándar de Raspberry Pi que se presenta en el primer arranque. Este asistente guía por la creación de cuentas de usuario, el establecimiento de contraseñas, la configuración de las conexiones WiFi y la activación de servicios esenciales como SSH para el acceso remoto.

Durante la configuración inicial puede convenir además ajustar la zona horaria, la distribución del teclado y otras preferencias regionales acordes con el entorno de uso. La herramienta de configuración de Raspberry Pi (`raspi-config`) da acceso a ajustes adicionales del sistema que pueden modificarse una vez completada la configuración inicial.

## Acceso remoto

El HALPI2 admite varios métodos de acceso remoto, que permiten supervisar y controlar el sistema sin necesidad de acceder físicamente al dispositivo. Esto resulta especialmente valioso en instalaciones donde el HALPI2 se monta sin pantalla en lugares de difícil acceso.

### Acceso web (HaLOS)

HaLOS ofrece una interfaz de gestión web completa que no requiere software adicional:

- **Panel de control** (`https://halos.local/`): el panel de control de Homarr da acceso a todas las aplicaciones instaladas, entre ellas Signal K, Grafana y otras aplicaciones náuticas.
- **Cockpit** (`https://halos.local:9090/`): administración del sistema, con acceso a terminal, actualizaciones de software, configuración de red y gestión de aplicaciones en contenedor.

### SSH (Secure Shell)

SSH proporciona acceso seguro por línea de comandos al sistema HALPI2, lo que permite ejecutar comandos, transferir archivos y realizar tareas de administración del sistema de forma remota. SSH está activado de forma predeterminada en las imágenes sin pantalla de HaLOS y en OpenPlotter. En las variantes HaLOS Desktop y en Raspberry Pi OS, SSH se puede activar con `raspi-config`.

Para conectarse por SSH se utiliza un cliente SSH, como el terminal integrado en macOS y Linux o aplicaciones como PuTTY en Windows. El comando básico de conexión es:

```bash
ssh username@halpi2-ip-address
```

Las conexiones SSH están cifradas y son seguras, lo que las hace adecuadas para su uso en redes públicas siempre que se configuren con una autenticación robusta. Además, requieren muy poco ancho de banda, por lo que son idóneas para el acceso remoto por conexiones lentas y de alta latencia.

### VNC (Virtual Network Computing)

!!! note
    VNC solo es aplicable a las imágenes de OpenPlotter y de Raspberry Pi OS Desktop. HaLOS utiliza en su lugar el acceso web — véase más arriba.

VNC proporciona acceso remoto al escritorio de la interfaz gráfica del HALPI2, lo que permite interactuar con el entorno de escritorio como si se estuviera físicamente ante el dispositivo. VNC viene preinstalado y preconfigurado en las imágenes de OpenPlotter. En las instalaciones de Raspberry Pi OS, VNC se puede activar con la herramienta de configuración `raspi-config`.

Para conectarse remotamente al escritorio del HALPI2 se utiliza la aplicación [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) de RealVNC, disponible para dispositivos Windows, macOS, Linux, iOS y Android. VNC funciona bien en redes locales y en entornos sin conexión, por lo que resulta idóneo para instalaciones en embarcaciones donde la conectividad a internet puede ser limitada o inexistente.

Para el acceso remoto a través de internet, VNC exige configuración de red adicional, como redirección de puertos o una VPN, ya que el protocolo no atraviesa por sí mismo cortafuegos ni dispositivos NAT.

### Raspberry Pi Connect

Raspberry Pi Connect ofrece un enfoque web moderno para el acceso remoto al escritorio: permite conectarse al escritorio del HALPI2 con un simple navegador estándar, sin instalar ningún software adicional. Este servicio funciona automáticamente a través de cortafuegos y configuraciones NAT, por lo que resulta especialmente adecuado para el acceso remoto por internet sin necesidad de una configuración de red compleja.

A diferencia de VNC, Raspberry Pi Connect gestiona automáticamente la complejidad de la red y ofrece un acceso fluido desde cualquier lugar con conexión a internet. Ahora bien, también exige que el propio HALPI2 mantenga una conexión a internet activa para funcionar.

## Actualizaciones de software

Se recomiendan actualizaciones periódicas para mantener el rendimiento y la seguridad óptimos del sistema.

### Actualizaciones de HaLOS

En HaLOS, los paquetes del sistema (incluido el firmware del HALPI2) se actualizan mediante Cockpit o desde la línea de comandos con `apt`. Las aplicaciones basadas en contenedores (Signal K, Grafana, etc.) se actualizan desde la interfaz Container Apps de Cockpit, que comprueba si hay nuevas versiones de las imágenes de contenedor.

### Actualizaciones por línea de comandos (todas las imágenes)

El método más fiable para actualizar el sistema es la interfaz de línea de comandos. Abrir una ventana de terminal y ejecutar los comandos siguientes para actualizar el sistema:

```bash
sudo apt update
sudo apt upgrade
```

El primer comando (`apt update`) actualiza la base de datos de paquetes con las últimas versiones disponibles, mientras que el segundo (`apt upgrade`) descarga e instala todas las actualizaciones disponibles. Este proceso actualiza todos los paquetes instalados, incluidos el Raspberry Pi OS base, los componentes de OpenPlotter y el software específico del HALPI2.

Durante el proceso de actualización puede solicitarse confirmación para instalar ciertos paquetes o para reiniciar servicios. Por lo general es seguro aceptar estas peticiones, salvo que haya motivos concretos para rechazarlas.

### Actualizaciones gráficas

Para quien prefiera una interfaz gráfica, el entorno de escritorio avisa visualmente cuando hay actualizaciones disponibles. Aparece un icono de descarga en la esquina superior derecha de la barra de tareas del escritorio cuando las actualizaciones están listas para instalarse. Al pulsar ese icono se abre el gestor de actualizaciones, que ofrece una interfaz sencilla para revisar e instalar las actualizaciones disponibles.

## Actualizaciones de firmware

El firmware del controlador del HALPI2 se puede actualizar mediante el proceso estándar de actualización de Raspberry Pi OS, lo que ofrece una forma integrada y sin fricciones de mantener las últimas versiones de firmware. Las actualizaciones periódicas de firmware son importantes para asegurar un rendimiento óptimo, acceder a nuevas funciones y mantener la compatibilidad con los componentes de software en evolución.

### Actualizaciones automáticas de firmware

Las actualizaciones de firmware se distribuyen mediante el mecanismo estándar de actualización del sistema, con paquetes Debian en un repositorio APT. Para buscar e instalar actualizaciones de firmware, abrir una ventana de terminal y ejecutar los comandos siguientes:

```bash
sudo apt update
sudo apt upgrade
```

Cuando hay firmware nuevo disponible para el HALPI2, se descarga e instala automáticamente como parte del proceso de actualización. El sistema avisa si entre los paquetes disponibles se incluyen actualizaciones de firmware.

Una vez completada la actualización del paquete de firmware, es esencial reiniciar el sistema correctamente para aplicar los cambios del firmware. Utilizar el comando de apagado para garantizar un ciclo de alimentación completo:

```bash
sudo shutdown -h now
```

**Importante:** un simple reinicio del sistema no basta para las actualizaciones de firmware. Es necesario un apagado completo seguido de un nuevo arranque, porque así el controlador se reinicia y aplica el nuevo firmware. El firmware del controlador solo se actualiza durante la secuencia de encendido.

### Mecanismos de seguridad del firmware

El HALPI2 incorpora mecanismos de seguridad integrados que protegen frente a la corrupción del firmware. Si el dispositivo se reinicia de nuevo antes de 30 segundos tras aplicar una actualización de firmware, el sistema vuelve automáticamente a la versión anterior. Esta función protege frente a actualizaciones de firmware problemáticas que podrían impedir el funcionamiento normal.

### Instalación manual del firmware

Para usuarios avanzados o para escenarios concretos de diagnóstico, el firmware se puede instalar manualmente con la herramienta de línea de comandos HALPI. Los archivos de firmware se guardan en el directorio `/usr/share/halpi2-firmware/` y se pueden grabar directamente con:

```bash
halpi flash <firmware_file>.bin
```

### Desactivación de las actualizaciones automáticas de firmware

Puede interesar desactivar las actualizaciones automáticas de firmware para mantener una versión concreta. Esto se consigue editando el archivo de configuración del HALPI2:

```bash
sudo nano /etc/halpid/firmware.conf
```

Localizar el ajuste `AUTO_FLASH_ON_INSTALL` y cambiarlo a `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Guardar el archivo y salir del editor. Este cambio de configuración impide que el HALPI2 grabe automáticamente firmware nuevo durante el proceso de actualización estándar, con lo que se obtiene control total sobre cuándo se aplican las actualizaciones de firmware. Las actualizaciones de firmware se pueden seguir instalando manualmente con el comando `halpi flash` cuando se desee.


## Herramienta de línea de comandos HALPI

La interfaz de software del HALPI2 se compone del servicio demonio `halpid` y de la herramienta de línea de comandos `halpi`. Juntos ofrecen capacidades de supervisión, configuración y control del sistema.

### Demonio HALPI (`halpid`)

El demonio HALPI se ejecuta como servicio del sistema y proporciona la comunicación entre el sistema operativo y el controlador del HALPI2. Permite el funcionamiento en modo Co-op con todas las funciones de supervisión y gestión de la alimentación.

#### Gestión del servicio

El demonio se gestiona mediante systemd:

```bash
# Check daemon status
systemctl status halpid

# Start the daemon
sudo systemctl start halpid

# Stop the daemon
sudo systemctl stop halpid

# Enable auto-start at boot
sudo systemctl enable halpid

# Disable auto-start
sudo systemctl disable halpid

# View daemon logs
journalctl -u halpid -f
```

#### Configuración

La configuración del demonio se guarda en `/etc/halpid/halpid.conf`. Para editarla:

```bash
sudo nano /etc/halpid/halpid.conf
```

Los cambios de configuración requieren reiniciar el demonio:

```bash
sudo systemctl restart halpid
```

### Herramienta de línea de comandos HALPI (`halpi`)

El comando `halpi` da acceso directo a las funciones del controlador y al estado del sistema. Se comunica con el demonio para ejecutar comandos y obtener información sobre el estado operativo, la configuración y los parámetros de hardware del HALPI2.

#### Estado del sistema y supervisión

La función principal de la herramienta de línea de comandos HALPI es ofrecer información completa sobre el estado del sistema. Incluye los parámetros de hardware, el estado operativo y los datos de supervisión en tiempo real.

Visualización del estado del sistema:
```bash
# Display comprehensive system status
halpi status
```

Este comando ofrece una visión completa del estado operativo actual del HALPI2, con los niveles de tensión, el consumo de corriente, las lecturas de temperatura y el estado del controlador:

```
$ halpi status
 hardware_version               N/A
 firmware_version             3.1.0
 state              OperationalCoOp
 5v_output_enabled             True
 watchdog_enabled              True
 watchdog_timeout              10.0  s
 watchdog_elapsed               0.0  s
 V_in                          12.2  V
 I_in                          0.38  A
 V_supercap                   10.27  V
 T_mcu                         43.3  °C
 T_pcb                         35.2  °C
```

Si solo se desea supervisar un valor concreto, se puede obtener así:

```bash
# Show controller firmware version
halpi get firmware_version
```

Para el uso en scripts es preferible recurrir a la API REST, tal como se describe en la sección [Acceso a la API REST](#acceso-a-la-api-rest).

#### Gestión de la configuración

La herramienta de línea de comandos HALPI ofrece amplias capacidades de gestión de la configuración, que permiten consultar los ajustes actuales y modificar los parámetros de funcionamiento.

Consulta de la configuración actual:
```bash
# Show current configuration
halpi config
```

Esto muestra todos los parámetros configurables y sus valores actuales:

```
$ halpi config
 Key                       Value
 watchdog_timeout           10.0
 power_on_threshold          8.0
 solo_power_off_threshold    5.5
 led_brightness               40
 auto_restart               True
 solo_depleting_timeout      5.0
```

#### Control de los LED

Uno de los ajustes que se modifican con más frecuencia es el brillo de los LED, que se puede adaptar a distintos entornos de uso y preferencias.

Ejemplos de comandos para gestionar el brillo de los LED:
```bash
# Get current LED brightness (0-255)
halpi config get led_brightness

# Set LED brightness to low level for night operation
halpi config set led_brightness 40

# Set moderate brightness
halpi config set led_brightness 64

# Turn LEDs off completely
halpi config set led_brightness 0

# Maximum brightness for daylight operation
halpi config set led_brightness 255
```

El brillo de los LED admite valores de 0 (completamente apagado) a 255 (brillo máximo), lo que permite un control preciso de los indicadores LED del panel frontal.

#### Gestión de la alimentación

La herramienta de línea de comandos HALPI ofrece funciones esenciales de gestión de la alimentación para un funcionamiento seguro del sistema.

Ejemplos de comandos de gestión de la alimentación:
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

El comando de apagado garantiza que el sistema se apague de forma segura, permitiendo que el sistema operativo cierre las aplicaciones y desmonte correctamente los sistemas de archivos antes de que el controlador corte la alimentación.

#### Acceso a la API REST

Para usuarios avanzados y aplicaciones a medida, el demonio HALPI ofrece además una interfaz de API REST accesible mediante un socket de dominio Unix. Esto permite un acceso programático más rápido a los datos del sistema:

A continuación se muestran algunos ejemplos de uso:
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

La API REST resulta especialmente útil para aplicaciones de supervisión, sistemas de registro de datos o la integración con otro software que necesite acceso en tiempo real a la información de estado del HALPI2.

La documentación completa de la API REST está en el capítulo [Desarrollo de software: demonio](../software-development/daemon.md).

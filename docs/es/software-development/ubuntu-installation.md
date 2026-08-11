---
translated_from: e096c9a0b090c6f3ced22a4d369daab4ad1fcadb
---

# Uso de otras distribuciones basadas en Debian

!!! warning "Nota"
    Hat Labs no puede prestar soporte para la instalación y el uso de sistemas operativos de terceros. Las instrucciones siguientes se ofrecen como cortesía a los usuarios que deseen utilizar HALPI2 con una configuración de software personalizada.

HALPI2 funciona sin problemas con cualquier sistema operativo compatible con el Raspberry Pi Compute Module 5. Para aprovechar toda la funcionalidad del hardware de HALPI2, incluidas las prestaciones de gestión de la alimentación y de supervisión, el sistema operativo debe ser compatible con el demonio HALPI2 (`halpid`) y requiere cierta configuración. Estos pasos son bastante sencillos en las distribuciones de Linux basadas en Debian. Esta sección ofrece instrucciones paso a paso para instalar Ubuntu en HALPI2. Puede que las instrucciones necesiten pequeños ajustes en otras distribuciones basadas en Debian.

La distribución Ubuntu cuenta con una [imagen oficial de Ubuntu para el Raspberry Pi](https://ubuntu.com/download/raspberry-pi) Compute Module 5, que puede utilizarse con HALPI2.

## Requisitos previos

Una vez instalada en la Pi la imagen elegida de Ubuntu (o de otra distribución basada en Debian), conviene asegurarse de disponer de las últimas actualizaciones de software:

```bash
sudo bash
apt update
apt full-upgrade
apt auto-remove
exit
```

A continuación deben instalarse los siguientes paquetes, necesarios para el proceso de instalación:

```bash
sudo apt install curl openssh-server dpkg-dev i2c-tools npm net-tools iw git
```

## Repositorio de Hat Labs

Los paquetes precompilados para el HALPI2 los proporciona Hat Labs y están disponibles a través de un repositorio apt.
Para añadir este repositorio hay que ejecutar los siguientes comandos con privilegios de root (desde `sudo bash`):

```bash
sudo bash
curl -fsSL https://apt.hatlabs.fi/hat-labs-apt-key.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/hatlabs.gpg
cat > /etc/apt/sources.list.d/hatlabs.sources << EOF
Types: deb
URIs: https://apt.hatlabs.fi/
Suites: stable
Components: main
Signed-By: /etc/apt/trusted.gpg.d/hatlabs.gpg
EOF
apt update
exit
```

## Firmware común de HALPI2

El firmware de los dispositivos comunes de la placa HALPI2 se configura editando `/boot/firmware/config.txt` y añadiendo las siguientes líneas a la sección `[all]`:

```text
# --- HALPI2 / Raspberry Pi 5 IO setup ---

# Use antenna path #2 for Wi-Fi/BT
dtparam=ant2

# Enable SPI0 and relocate CS1 to GPIO6 (BCM6) for the CAN controller.
dtoverlay=spi0-2cs,cs1_pin=6

# Attach a Microchip MCP2517FD/2518FD CAN-FD controller to SPI0 Chip-Select 1.
#  - spi0-1        : controller is on SPI0, CS1 (wired to GPIO6 by the overlay above)
#  - interrupt=26  : MCP251xFD INT pin wired to GPIO26
#  - oscillator=40000000 : external crystal is 40 MHz
# Produces a SocketCAN interface (e.g. can0).
dtoverlay=mcp251xfd,spi0-1,interrupt=26,oscillator=40000000

# Enable PL011 UART4.  Creates /dev/ttyAMA4 for NMEA 0183 communication.
dtoverlay=uart4-pi5

# Enable the ARM I2C bus.  The halpid daemon reaches the power management
# controller over /dev/i2c-1.
dtparam=i2c_arm=on

# Disable the unused SD card interface.  It causes a long delay at shutdown.
# See: https://github.com/raspberrypi/linux/issues/7014
dtparam=sd=off
```

!!! warning "El I2C debe estar habilitado"
    En Raspberry Pi OS, `dtparam=i2c_arm=on` está comentado, y otras distribuciones pueden hacer lo mismo. Sin esa línea no existe `/dev/i2c-1` y `halpid` no alcanza el hardware de gestión de la alimentación.

Además, el módulo del kernel `i2c-dev` debe cargarse en el arranque para que el demonio `halpid`, que se ejecuta en espacio de usuario, pueda usar el bus.
Para ello se crea el archivo `/etc/modules-load.d/i2c-dev.conf` con:

```bash
echo i2c-dev | sudo tee /etc/modules-load.d/i2c-dev.conf
```

## Configuración del bus CAN (NMEA 2000)

El siguiente comando habilita el bus CAN para la comunicación NMEA 2000 en el HALPI2:

```bash
sudo bash
apt install can-utils
cat > /etc/systemd/network/80-can.network << EOF
[Match]
Name=can*

[CAN]
BitRate=250000
RestartSec=100ms
EOF
chmod 644 /etc/systemd/network/80-can.network
echo 'SUBSYSTEM=="net", KERNEL=="can*", ACTION=="add|change", ATTR{tx_queue_len}="1000"' > /etc/udev/rules.d/80-can.rules
chmod 644 /etc/udev/rules.d/80-can.rules
systemctl enable systemd-networkd
reboot
```

Una vez reiniciado el sistema, puede comprobarse que la interfaz CAN está disponible con cualquiera de estos comandos:

```bash
ip link show can0
ifconfig can0
```

## Demonio HALPI2

El demonio HALPI2 sirve para supervisar y controlar la placa portadora del HALPI2 y proporciona la herramienta de línea de comandos `halpi`.
Instalar el paquete `halpid` desde el repositorio de Hat Labs:

```bash
sudo apt install halpid
```

El demonio HALPI2 debería estar ya en ejecución y el comando `halpi` disponible. El estado del demonio se comprueba con:
```bash
halpi status
```

## Instalación del firmware de HALPI2

Ahora que el comando `halpi` está disponible, puede instalarse el paquete `halpi2-firmware`, que graba el firmware más reciente en la placa del HALPI2:
```bash
sudo apt install halpi2-firmware
```

El firmware se graba automáticamente al instalar o actualizar el paquete. Para desactivarlo, establecer `AUTO_FLASH_ON_INSTALL=no` en `/etc/halpid/firmware.conf`.

El paquete instala los binarios del firmware en `/usr/share/halpi2-firmware/`. Para grabar manualmente una versión concreta, indicar a `halpi flash` la ruta del binario:
```bash
halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_3.3.1.bin
```

## Configuración del servidor Signal K

El servidor Signal K es una opción muy extendida para la gestión de datos náuticos y puede conectarse con fuentes de datos tanto NMEA 2000 como NMEA 0183.
El servidor Signal K se instala con npm. Los siguientes comandos instalan el servidor Signal K y ejecutan la configuración inicial:

```bash
npm i -g signalk-server
signalk-server-setup
```

Después se puede acceder al servidor Signal K desde un navegador, en el puerto configurado.

### Conexión NMEA 2000 en Signal K

Para configurar una conexión NMEA 2000 con la interfaz CAN del HALPI hay que utilizar una cuenta de administrador de Signal K e ir a la sección `Server > Data Connections` del menú.
Allí se puede pulsar el botón `+Add` y crear un conector con las siguientes propiedades:

```text
          Data Type: NMEA2000
            Enabled: Yes
                 ID: "HALPI2N2K"
   NMEA 2000 Source: Canbus (canboatjs)
          Interface: can0
```

Reiniciar y comprobar en el panel de control si se están recibiendo datos.

### Conexión NMEA 0183 en Signal K

Para configurar una conexión NMEA 0183 con la interfaz CAN del HALPI hay que utilizar una cuenta de administrador de Signal K e ir a la sección `Server > Data Connections` del menú.
Allí se puede pulsar el botón `+Add` y crear un conector con al menos las siguientes propiedades:

```text
          Data Type: NMEA0183
            Enabled: Yes
                 ID: "HALPI2N0183"
   NMEA 0183 Source: Serial
        Serial Port: /dev/ttyAMA4
          Baud Rate: 4800 | 38400
```

Reiniciar y comprobar en el panel de control si se están recibiendo datos.

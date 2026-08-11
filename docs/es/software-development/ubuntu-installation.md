---
translated_from: 9b2819d37e8c666f7908c658418aa61209985b55
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

!!! danger "Comprobar el dispositivo de arranque antes de pegar esto"
    El bloque siguiente termina con `dtparam=sd=off`. En un Compute Module 5 esa línea desactiva la ranura microSD integrada y, en un módulo con eMMC, también la eMMC. Conviene mantenerla si el arranque se hace desde NVMe, que es la configuración estándar del HALPI2. Hay que quitarla si el arranque se hace desde microSD o eMMC; de lo contrario el equipo no arrancará tras el siguiente reinicio.

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

# Disable the SD interface.  Without this, shutdown stalls long enough that the
# supercapacitors can run out before the controller powers the board down.
# This also disables the onboard microSD slot and the eMMC on a CM5 that has
# one, so omit the line if you boot from either.
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

Reiniciar para aplicar los cambios y comprobar después que el bus I2C está presente:

```bash
sudo reboot
```

```bash
ls /dev/i2c-1
```

Si `/dev/i2c-1` no existe, revisar los cambios en `config.txt` antes de continuar. El demonio `halpid` no puede arrancar sin él.

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

El socket del demonio solo es legible para el grupo `halpid`. El paquete añade el usuario a ese grupo, pero la pertenencia se aplica solo en las nuevas sesiones de inicio. Si el comando no logra conectar, cerrar la sesión y volver a entrar, o usar `sudo halpi status`.

## Instalación del firmware de HALPI2

Ahora que el comando `halpi` está disponible, instalar el paquete `halpi2-firmware`, que incluye los archivos de firmware en `/usr/share/halpi2-firmware/`:
```bash
sudo apt install halpi2-firmware
```


!!! warning "Grabar el firmware manualmente"
    El paquete intenta grabar durante la instalación, pero el intento falla de forma silenciosa en las versiones actuales ([`HALPI2-firmware` #40](https://github.com/hatlabs/HALPI2-firmware/issues/40)). Apt informa igualmente de éxito, así que conviene grabar a mano y comprobar el resultado.

Grabar el firmware y apagar después el equipo. Un reinicio no aplica el firmware nuevo:
```bash
sudo halpi flash /usr/share/halpi2-firmware/halpi2-rs-firmware_*.bin
sudo shutdown -h now
```

Volver a encender el equipo y confirmar la versión con `halpi status`. En una instalación sin pantalla, hay que poder alcanzar el interruptor de alimentación antes de ejecutar el apagado.

La [guía del software](../user-guide/software.md#instalacion-manual-del-firmware) describe el mecanismo de actualización automática y cómo desactivarlo.

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

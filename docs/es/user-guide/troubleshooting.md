---
translated_from: 232aac811fb62f4cc46a1955e832ea282dc92332
---

# Resolución de problemas

Esta página recoge los problemas más habituales que pueden surgir durante el funcionamiento de HALPI2 y la forma de resolverlos.

## Problemas de alimentación y de arranque

### El sistema no se enciende

**Síntomas:** ninguna actividad de los LED, ninguna señal de vida tras conectar la alimentación.

1. Comprobar con un multímetro en el conector E7T que la tensión de entrada está dentro del rango (10–32 V CC).
2. Revisar las conexiones del cable de alimentación: el conector E7T debe estar completamente insertado.
3. Verificar el limitador de corriente si se utiliza la alimentación desde el bus NMEA 2000: debe estar ajustado a 0,9 A y la red debe poder suministrar corriente suficiente.
4. Abrir la carcasa y buscar daños visibles o conexiones internas sueltas.

### LED en arcoíris

**Síntomas:** los LED recorren un patrón de arcoíris y nunca llegan a un estado estable.

El patrón de arcoíris significa que el controlador se ha encendido pero no se detecta el CM5. Esto puede ocurrir si:

- El Compute Module no está instalado o no está bien asentado.
- El Compute Module está defectuoso.
- Un dispositivo conectado inyecta tensiones parásitas que impiden el arranque del CM5; en ese caso conviene probar a desconectar el cable HDMI.

1. Desconectar cualquier pantalla HDMI y reiniciar para descartar interferencias por tensiones parásitas.
2. Abrir la carcasa si el problema persiste y comprobar que el módulo CM5 está completamente asentado en su conector; para ello hay que retirar la placa portadora.

### Los LED se quedan en amarillo

**Síntomas:** los LED pasan de rojo (carga) a amarillo (encendido) pero nunca llegan a verde.

El estado amarillo significa que el controlador ha alimentado el CM5 y espera la respuesta del demonio. Si los LED se quedan en amarillo, o bien el sistema operativo no arranca, o bien el demonio HALPI no está instalado.

1. Comprobar que el conmutador de modo de arranque está en la posición «Normal»: el LED indicador amarillo situado junto al conmutador se enciende cuando el modo de arranque está en «Abnormal» (arranque por USB).
2. Conectar una pantalla por HDMI para detectar errores de arranque o un aviso de inicio de sesión.
3. Comprobar que el NVMe SSD está bien asentado en su ranura M.2.
4. Comprobar que el demonio está instalado si el sistema operativo arranca correctamente: `systemctl status halpid`
5. Revisar los registros del demonio si está instalado pero no se está ejecutando: `journalctl -u halpid -e`

### El sistema se apaga de forma inesperada

**Síntomas:** el sistema se apaga sin intervención del usuario, aunque la alimentación externa esté conectada.

1. Comprobar la estabilidad de la tensión de entrada: las caídas breves por debajo del umbral activan el temporizador de corte de corriente. Con `halpi status` se puede supervisar `V_in` en tiempo real.
2. Inspeccionar el cable de alimentación en busca de conexiones sueltas o conductores dañados que puedan provocar contactos intermitentes.
3. Verificar la estabilidad de la tensión de la red bajo carga si se utiliza la alimentación desde el bus NMEA 2000. Otros dispositivos de alto consumo de la red pueden provocar caídas de tensión.

## Actualización de firmware fallida o revertida

Después de una actualización de firmware, si el sistema se reinicia antes de 30 segundos, el firmware vuelve automáticamente a la versión anterior como medida de seguridad.

1. Comprobar la versión de firmware actual: `halpi get firmware_version`
2. Reintentar la actualización: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. Realizar un apagado controlado una vez instalada la actualización: `sudo shutdown -h now`
4. Esperar a que el sistema se apague por completo antes de volver a conectarlo: deben transcurrir al menos 30 segundos antes del siguiente reinicio para evitar que se active el mecanismo de reversión.

## Problemas de red y de interfaces

### No hay datos NMEA 2000

**Síntomas:** `candump can0` no muestra nada, o Signal K no recibe datos.

1. Comprobar el estado de la interfaz CAN:
    ```bash
    ip link show can0
    ```
    La interfaz debería aparecer como `UP`. Si aparece como `DOWN`, hay que activarla:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Comprobar el LED RX de la placa portadora: debería parpadear cuando hay datos en la red. Si el LED RX está inactivo:
    - Verificar la conexión del cable Micro-C y la colocación del conector en T.
    - Comprobar que la red NMEA 2000 tiene alimentación y que otros dispositivos están transmitiendo.
    - Asegurarse de que el puente de terminación de 120 Ω **no** está activado en las redes NMEA 2000.

3. Verificar la configuración de la interfaz CAN cuando el LED RX parpadea pero `candump` no muestra nada, ya que entonces el problema está en el software:
    ```bash
    ip -details link show can0
    ```

4. Comprobar si hay errores en el bus CAN:
    ```bash
    ip -statistics link show can0
    ```
    Un recuento alto de errores apunta a problemas de cableado, a una velocidad de transmisión incorrecta o a contención en el bus.

### No hay datos NMEA 0183 en RS-485

**Síntomas:** no hay datos en `/dev/ttyAMA4`, o el dispositivo conectado no responde.

1. Abrir la carcasa y comprobar los LED de la interfaz RS-485: el LED RX debería parpadear cuando se reciben datos.
2. Verificar que el puerto serie existe y es accesible:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Comprobar la polaridad del cableado: RS-485 utiliza señalización diferencial con líneas A/B. Si las conexiones A y B están intercambiadas, no hay comunicación posible.

### No se establece el enlace Ethernet

1. Revisar el cable Ethernet y el conector RJ45. Probar con otro cable.
2. Abrir la carcasa y comprobar los LED de Ethernet para conocer el estado del enlace.
3. Verificar el estado del enlace: `ip link show eth0`
4. Comprobar el DHCP si el enlace está activo pero no hay dirección IP: `sudo dhclient eth0`
5. Verificar los ajustes en `/etc/network/interfaces` o en NetworkManager en las configuraciones de IP estática.

## Problemas del sistema operativo

### No se puede acceder al dispositivo por SSH

1. Verificar que SSH está habilitado: `sudo systemctl status ssh`
2. Comprobar la conectividad de red: ¿responde el dispositivo a un ping?
3. Tener en cuenta que SSH está habilitado de forma predeterminada en las imágenes de HaLOS sin pantalla (headless) y en OpenPlotter. En las variantes HaLOS Desktop y en Raspberry Pi OS, SSH puede habilitarse con `raspi-config`.

### El sistema va lento o se bloquea

1. Comprobar la temperatura de la CPU: una temperatura ambiente extrema puede provocar limitación térmica. Para ello:
    ```bash
    vcgencmd measure_temp
    ```
    Una temperatura superior a 80 °C indica un problema térmico. Conviene reducir la temperatura ambiente o mejorar la circulación de aire alrededor de la carcasa.

2. Comprobar el uso de memoria: `free -h`
3. Comprobar el uso del disco: `df -h`; un NVMe SSD lleno provoca problemas graves de rendimiento.
4. Buscar procesos desbocados: `top` o `htop`

### La hora es incorrecta tras una pérdida de alimentación

HALPI2 dispone de un reloj de tiempo real (RTC) con pila de respaldo que mantiene la hora durante los cortes de corriente. Si el reloj se pone a cero:

1. Comprobar la pila del RTC: puede que haya que sustituirla si el sistema ha estado mucho tiempo sin alimentación.
2. Verificar la sincronización NTP cuando haya red disponible: `timedatectl status`
3. Ajustar la hora manualmente si es necesario: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## Diagnóstico mediante los LED

Los patrones de los LED permiten diagnosticar rápidamente el estado del sistema:

| Síntoma | Patrón de LED | Causa probable |
|:--------|:--------------|:---------------|
| El sistema no arranca | Sin LED | Sin alimentación de entrada o fallo de hardware |
| Bloqueo durante el arranque | Relleno progresivo en rojo | Los supercondensadores aún se están cargando: esperar |
| Bloqueo durante el arranque | Patrón de arcoíris | CM5 no detectado: comprobar el asentamiento del módulo y desconectar las pantallas |
| Se queda en amarillo | Barra amarilla | El sistema operativo no arranca o el demonio no está instalado |
| Apagado inesperado | Barra naranja o verde oscuro y, después, morada | Alimentación de entrada perdida, apagado con la energía de respaldo: comprobar la alimentación de entrada |
| El sistema se reinicia por sí solo | Todos los LED en rojo fijo antes del reinicio | Tiempo de espera del watchdog agotado: el sistema operativo dejó de responder y el controlador lo reinició |
| Fallo | Todos los LED parpadeando en rojo | Sobretensión en los supercondensadores: contactar con el soporte |

!!! quote "Información relacionada"
    - **Patrones de LED:** véase [Indicadores LED de estado](./operation.md#indicadores-led-de-estado)
    - **Comportamiento ante la pérdida de alimentación:** véase [Cuando se pierde la alimentación](./operation.md#cuando-se-pierde-la-alimentacion)
    - **Gestión del demonio:** véase [Guía del software](./software.md#demonio-halpi-halpid)
    - **Detalles de la interfaz CAN:** véase [Interfaces y conectividad](./interfaces.md#can-fd-nmea-2000)
    - **Detalles de la interfaz RS-485:** véase [Interfaces y conectividad](./interfaces.md#rs-485-nmea-0183)

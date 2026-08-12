---
translated_from: a79f6f20e3cbe488309469e1f6730f929d29c362
---

# Uso diario

El HALPI2 está diseñado para el funcionamiento desatendido. Con la imagen HaLOS preinstalada —o con cualquier sistema operativo que tenga instalado el [demonio HALPI](./software.md#herramienta-de-linea-de-comandos-halpi)—, la gestión de la alimentación es automática: el dispositivo carga sus supercondensadores de respaldo, supera los microcortes de tensión, apaga el sistema operativo de forma segura cuando se pierde la alimentación y vuelve a arrancar cuando esta se restablece. Nada de esto requiere la intervención del usuario.

## Encendido

El HALPI2 no tiene botón de encendido en la carcasa: arranca en cuanto se conecta la alimentación de entrada. (Puede cablearse un botón de encendido externo a la placa portadora; véase [Botones externos](./interfaces.md#botones-externos).) La barra de LED se llena primero de rojo mientras se cargan los supercondensadores (entre unos segundos y medio minuto, según el [ajuste del límite de corriente](./hardware.md#configuracion-de-la-limitacion-de-corriente)). A continuación, los LED muestran una breve animación de arcoíris y ciclo de colores mientras arranca el Compute Module, presentan una barra amarilla mientras arranca el sistema operativo y se ponen verdes cuando el sistema operativo está en marcha y el demonio HALPI se ha conectado.

## Apagado

Para apagar el HALPI2, cortar la alimentación de entrada, por ejemplo con un interruptor del cuadro eléctrico. El sistema detecta la pérdida de alimentación, apaga el sistema operativo de forma controlada con la energía de los supercondensadores y permanece apagado. Los LED muestran una barra morada mientras se ejecuta el apagado y se apagan cuando este termina.

También puede apagarse el sistema desde el software: el menú del escritorio, el comando `shutdown` o `halpi shutdown`. El sistema se apaga entonces y permanece apagado hasta que se realiza un ciclo de la alimentación de entrada (o se pulsa un [botón de encendido externo](./interfaces.md#botones-externos), si está instalado).

De forma opcional, el controlador puede reiniciar el sistema automáticamente unos 5 segundos después de un apagado por software mientras la alimentación de entrada siga conectada, de modo que un comando de apagado accidental nunca deje fuera de servicio una instalación de difícil acceso físico. Se activa con `halpi config set auto_restart true`; el ajuste se conserva en el controlador. Las unidades producidas antes de principios de 2026 se entregaron con este comportamiento activado; puede comprobarse con `halpi config get auto_restart`.

El sistema también puede ponerse en modo de reposo, en el que se apaga y vuelve a activarse a una hora programada; véase la referencia del [Controlador de la placa portadora](../technical-reference/controller.md#modo-de-reposo).

## Indicadores LED de estado

Los cinco LED del panel frontal muestran lo que está haciendo el sistema:

| Patrón de LED | Significado |
|:--------------|:------------|
| Barra roja llenándose | Los supercondensadores se cargan antes del arranque: esperar |
| Arcoíris y ciclo de colores | El Compute Module está arrancando. Si el patrón se repite sin avanzar, el módulo no ha conseguido arrancar; véase [Resolución de problemas](./troubleshooting.md#led-en-arcoiris) |
| Barra amarilla | En funcionamiento, demonio HALPI no conectado: normal durante unos instantes en el arranque. Si persiste, véase [Resolución de problemas](./troubleshooting.md#los-led-se-quedan-en-amarillo) |
| Barra verde | Funcionamiento normal |
| Barra naranja o verde oscuro | Alimentación de entrada perdida, funcionamiento con la energía de respaldo: sigue un apagado salvo que la alimentación vuelva en unos segundos |
| Barra morada | Apagado en curso |
| Todos en rojo fijo | El sistema operativo no responde: el controlador lo reiniciará automáticamente |
| Todos parpadeando en rojo | Fallo de los supercondensadores: contactar con el soporte |
| Todos en azul fijo | Entrando en modo de reposo |
| Todos en rojo tenue | Modo de reposo |
| Todos apagados | Sistema apagado |

En los patrones de barra, el número de LED encendidos indica el nivel de carga de los supercondensadores. Los rangos de tensión exactos y la correspondencia completa de estados figuran en la referencia del [Controlador de la placa portadora](../technical-reference/controller.md#referencia-de-los-led-de-estado).

El brillo de los LED puede ajustarse; véase [Control de los LED](./software.md#control-de-los-led). Los LED también pueden reutilizarse como pantalla de métricas del sistema y datos náuticos (actividad de red, niveles de los tanques, valores NMEA 2000 y Signal K) con el complemento [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights).

## Cuando se pierde la alimentación

No es necesario hacer nada. Las caídas breves y los microcortes —de hasta 5 segundos de forma predeterminada— los cubren los supercondensadores, y el funcionamiento continúa sin alteraciones. En un corte más largo, el sistema se apaga por sí mismo de forma controlada con los 30–60 segundos de alimentación de respaldo que almacenan los supercondensadores. Cuando vuelve la alimentación de entrada, el sistema arranca de nuevo automáticamente.

!!! warning "No es un SAI"
    Los supercondensadores existen para cubrir los microcortes y alimentar un apagado seguro. Para mantener el funcionamiento durante cortes de corriente prolongados se necesita un sistema de alimentación ininterrumpida (SAI) externo.

## Comprobación del estado del sistema

Una barra de LED verde significa que el sistema funciona correctamente. Para más detalles, el comando `halpi` muestra el estado del controlador, las tensiones, la corriente y las temperaturas:

```bash
halpi status
```

Si algo no parece correcto, véanse [Resolución de problemas](./troubleshooting.md) y la [Guía del software](./software.md#herramienta-de-linea-de-comandos-halpi).

## Funcionamiento sin el demonio

En los sistemas operativos sin el demonio HALPI, el controlador recurre a un modo de protección básico: sigue detectando la pérdida de alimentación y solicita el apagado, pero mediante pulsaciones simuladas del botón de encendido —lo que falla si el sistema está bloqueado—, y la supervisión y la configuración no están disponibles. Si se utiliza un sistema operativo personalizado, conviene instalar el demonio; véase [Otras distribuciones Debian](../software-development/ubuntu-installation.md). El funcionamiento de los dos modos se describe en la referencia del [Controlador de la placa portadora](../technical-reference/controller.md#modos-de-funcionamiento).

!!! quote "Información relacionada"
    - **Funcionamiento interno de la gestión de la alimentación:** véase [Controlador de la placa portadora](../technical-reference/controller.md)
    - **Detalles del sistema de alimentación:** véase [La alimentación en detalle](../technical-reference/power-supply.md)
    - **El comando `halpi` y el demonio:** véase la [Guía del software](./software.md)
    - **Problemas:** véase [Resolución de problemas](./troubleshooting.md)

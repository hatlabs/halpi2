---
translated_from: 9e11a0dc9c72a6805946f415590859708bf324c8
---

# Preguntas frecuentes

## ¿Por qué el HALPI2 se reinicia después de apagarlo?

El dispositivo tiene activado el reinicio automático: con `auto_restart` en `true`, el controlador reinicia el sistema unos 5 segundos después de un apagado por software mientras la alimentación de entrada está conectada. Las unidades producidas antes de principios de 2026 se entregaron así; las unidades actuales se entregan con esta función desactivada. Se desactiva con `halpi config set auto_restart false`, aunque también puede conservarse, ya que garantiza que un sistema desatendido no se quede apagado tras un comando de apagado accidental. Con la función activada, el apagado permanente se consigue cortando la alimentación de entrada. Véase [Apagado](user-guide/operation.md#apagado).

## ¿Cómo se apaga el HALPI2?

Cortando la alimentación de entrada. El sistema detecta la pérdida de alimentación y se apaga de forma controlada con la energía de los supercondensadores: así es como está previsto apagarlo. Véase [Apagado](user-guide/operation.md#apagado).

## ¿Hay que hacer algo cuando se va la corriente?

No. Los supercondensadores cubren los microcortes breves, los cortes más largos activan un apagado seguro automático y el sistema se reinicia por sí solo cuando vuelve la corriente. Véase [Cuando se pierde la alimentación](user-guide/operation.md#cuando-se-pierde-la-alimentacion).

## ¿Cuánto dura la alimentación de respaldo?

Los supercondensadores proporcionan 30–60 segundos, según la carga del sistema. Es tiempo suficiente para un apagado seguro con margen, pero el HALPI2 no es un SAI: no sigue funcionando durante cortes de corriente prolongados. Véase [La alimentación en detalle](technical-reference/power-supply.md).

## ¿Puede el HALPI2 estar encendido de forma ininterrumpida?

Sí. El HALPI2 está diseñado para el funcionamiento desatendido continuo, y su gestión de la alimentación lo da por supuesto: el sistema se recupera de las pérdidas de alimentación y de los bloqueos del sistema operativo sin intervención del usuario.

## ¿Qué significa que los LED se queden en amarillo?

Una barra amarilla significa que el sistema está en marcha pero el demonio HALPI no se ha conectado, algo normal durante unos instantes en el arranque. Una barra amarilla persistente significa que el sistema operativo no arranca o que el demonio no está instalado. Véase [Resolución de problemas](user-guide/troubleshooting.md#los-led-se-quedan-en-amarillo).

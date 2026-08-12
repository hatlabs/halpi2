---
translated_from: f27483ba16d09d9291ae72cabdffe7aa35755096
---

# La alimentación en detalle

La alimentación del HALPI2 está diseñada para los entornos eléctricos inestables de embarcaciones y vehículos: tolera picos de tensión y microcortes, limita la corriente de irrupción y proporciona energía almacenada suficiente para apagar el sistema de forma segura cuando se pierde la alimentación de entrada.

Para las especificaciones eléctricas, véase la [Referencia del hardware](./hardware.md). Para la máquina de estados que actúa sobre las medidas aquí descritas, véase la referencia del [Controlador de la placa portadora](./controller.md).

## Etapa de entrada

El rango de entrada nominal es de 10–32 V CC, lo que cubre tanto los sistemas de 12 V como los de 24 V. La etapa de entrada está protegida contra la inversión de polaridad y contra sobretensiones transitorias de hasta 100 V, como las desconexiones bruscas de carga del alternador (load dump).

### Limitación de corriente

Un limitador de corriente de entrada controla la corriente máxima extraída de la fuente, seleccionable entre 0,9 A y 2,5 A mediante un conmutador de la placa portadora. El límite cumple dos funciones:

- Limita la corriente de irrupción cuando los supercondensadores descargados comienzan a cargarse al conectar la alimentación.
- Mantiene el consumo total dentro del presupuesto de potencia de la fuente: el ajuste de 0,9 A (LEN 18) permite alimentar el HALPI2 con seguridad desde un bus NMEA 2000.

El ajuste predeterminado es 0,9 A. Seleccionar 2,5 A cuando el sistema alimente periféricos de alto consumo o cuando se desee un arranque más rápido. La ubicación del conmutador y el procedimiento para cambiarlo se describen en la [Guía del hardware](../user-guide/hardware.md#configuracion-de-la-limitacion-de-corriente).

## Respaldo por supercondensadores

Un banco de supercondensadores proporciona la energía de respaldo para los apagados controlados. A diferencia de un SAI basado en baterías, los supercondensadores no se desgastan, funcionan en todo el rango de temperatura y se cargan en segundos, a costa de una reserva de energía mucho menor.

### Carga

Los supercondensadores se cargan siempre que hay alimentación de entrada. Desde la descarga completa, la carga tarda aproximadamente:

- 25 segundos con el límite de corriente de 0,9 A
- 9 segundos con el límite de corriente de 2,5 A

Los LED del panel frontal muestran el progreso de la carga como una barra roja que se llena. El Compute Module se enciende cuando la tensión de los supercondensadores alcanza el umbral de encendido (8,0 V de forma predeterminada).

### Duración del respaldo

Cuando se pierde la alimentación de entrada, los supercondensadores asumen toda la carga del sistema. Proporcionan 30–60 segundos de funcionamiento, según la carga del sistema y los periféricos conectados: tiempo suficiente para un apagado controlado del sistema operativo con margen.

!!! warning "No es un SAI"
    El sistema de supercondensadores está diseñado para cubrir los microcortes y alimentar un apagado seguro. No está diseñado para mantener el funcionamiento durante cortes de corriente prolongados.

## Detección de la pérdida de alimentación

El controlador mide la tensión de entrada de forma continua y considera perdida la alimentación de entrada cuando la tensión cae por debajo de 9,0 V. Un temporizador de corte de corriente (5 segundos de forma predeterminada) evita el apagado en las interrupciones breves: los supercondensadores cubren el intervalo y el funcionamiento continúa sin alteraciones si la alimentación vuelve a tiempo. Los cortes más largos activan las secuencias de apagado automático descritas en la referencia del [Controlador de la placa portadora](./controller.md#perdida-de-alimentacion-y-secuencias-de-apagado).

## Supervisión

El controlador mide la tensión de entrada, la corriente de entrada y la tensión de los supercondensadores, y las expone a través del demonio HALPI:

```bash
halpi status
```

Los valores también están disponibles de forma programática a través de la API REST del demonio; véase la [Guía del software](../user-guide/software.md#acceso-a-la-api-rest).

!!! quote "Información relacionada"
    - **Especificaciones eléctricas:** véase la [Referencia del hardware](./hardware.md)
    - **Máquina de estados y secuencias de apagado:** véase [Controlador de la placa portadora](./controller.md)
    - **Comportamiento cotidiano de la alimentación:** véase [Uso diario](../user-guide/operation.md)

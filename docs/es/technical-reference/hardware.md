---
translated_from: c237d8b6a74b99528445a8bb38aa5473b824b52e
---

# Referencia de hardware

Esta página recoge las especificaciones eléctricas, mecánicas y ambientales del HALPI2. Para la información de procedimiento (instalación, mantenimiento, sustitución), véase la [Guía de hardware](../user-guide/hardware.md). Para los detalles de los protocolos de interfaz, véase [Interfaces y conectividad](./interfaces.md).

## Resumen de especificaciones

| Parámetro | Valor |
|:----------|:------|
| Módulo de cómputo | Raspberry Pi CM5 (compatible con CM4) |
| Controlador de la placa portadora | RP2040 (Arm Cortex-M0+, doble núcleo, 133 MHz) |
| Tensión de entrada | 9–36 V CC (máximo absoluto 38,6 V, protección contra transitorios hasta 100 V) |
| Consumo | de 250 mA en reposo a 590 mA con carga (entrada de 12 V, HaLOS sin pantalla) |
| Ajustes del límite de corriente | 0,9 A o 2,5 A (seleccionable) |
| Respaldo por supercondensadores | 4× 25 F / 2,7 V en serie (6,25 F efectivos a 10,8 V máx.) |
| Temperatura de funcionamiento | −20 °C … +60 °C |
| Dimensiones de la carcasa | 200 × 130 × 60 mm (sin conectores) |
| Peso de la carcasa | TODO |
| Material de la carcasa | Aluminio inyectado con recubrimiento en polvo |
| Grado de protección | IP65 |
| Licencia | CERN-OHL-S v2 (hardware) |

## Especificaciones eléctricas

### Alimentación

La alimentación admite un amplio rango de entrada en corriente continua y proporciona líneas reguladas de 5 V y 3,3 V para el CM5 y los periféricos. La protección de entrada incluye protección contra inversión de polaridad (LM74800), desconexión por sobretensión a 38,6 V, recorte mediante TVS y filtrado EMI en modo común y diferencial.

| Parámetro | Valor |
|:----------|:------|
| Tensión de entrada recomendada | 9–36 V CC |
| Tensión de entrada máxima absoluta | 38,6 V (continua), 100 V (transitoria, limitada por TVS) |
| Corriente de entrada máxima | 0,9 A o 2,5 A (limitador de corriente seleccionable) |
| Fusible de entrada | 7 A (solo protección frente a fallos) |
| Línea intermedia de 10 V | 10,25 V nominales (convertidor reductor SiC463ED) |
| Línea de 5 V | 5,1 V / 4 A (TPS566238, alimenta el CM5 y los puertos USB) |
| Línea de 3,3 V | 3,33 V / 3 A (TPS566238, conmutada por el controlador en la v0.6.0 y posteriores) |
| Umbral UVLO de 3,3 V | 4,5 V en el supercondensador |
| LDO inicial de 3,3 V | SE8633K2 (para el arranque del controlador y del balanceador de supercondensadores) |

### Respaldo por supercondensadores

El banco de supercondensadores proporciona energía de respaldo para realizar un apagado controlado en caso de pérdida de alimentación.

| Parámetro | Valor |
|:----------|:------|
| Configuración | 4 celdas de 25 F / 2,7 V en serie |
| Capacidad efectiva | 6,25 F a 10,8 V máximo |
| Balanceo | Balanceo activo |
| Rango de tensión de carga | 0–10,8 V (supervisado por el ADC del controlador) |
| Umbral de encendido | 8,0 V (configurable por firmware) |
| Umbral de apagado | 5,5 V (configurable por firmware) |

### Consumo de corriente

Medido con entrada de 12 V y un Raspberry Pi CM5 ejecutando la imagen sin pantalla (headless) de HaLOS.

| Condición | Corriente consumida |
|:----------|:-------------|
| Sistema en reposo | ~250 mA |
| Carga típica | ~400 mA |
| Carga máxima | ~590 mA |

!!! note
    Estas mediciones excluyen el consumo de los dispositivos USB externos. Cada puerto USB 3.0 puede suministrar hasta 0,93 A, por lo que el consumo total del sistema depende en gran medida de los periféricos conectados.

## Asignación de pines de los conectores

### Conector de entrada de alimentación

Tipo Phoenix MC, paso de 3,81 mm, 2 pines. En el panel frontal, el conector cilíndrico (barrel) E7T se conecta a este conector de pines.

| Pin | Función |
|:----|:---------|
| 1 | GND |
| 2 | VIN (9–36 V CC) |

### Conector CAN FD

Tipo Phoenix MC, paso de 3,81 mm, 4 pines. Aislado galvánicamente.

| Pin | Función |
|:----|:---------|
| 1 | GND_CAN (masa aislada) |
| 2 | — |
| 3 | CAN_H |
| 4 | CAN_L |

El puente (jumper) de terminación (etiqueta «120R») habilita una resistencia de terminación de 120 Ω entre CAN_H y CAN_L.

### Conector RS-485

Tipo Phoenix MC, paso de 3,81 mm, 5 pines. Aislado galvánicamente.

| Pin | Función |
|:----|:---------|
| 1 | GND_RS485 (masa aislada) |
| 2 | RX_A_C |
| 3 | RX_B_C |
| 4 | TX_A_C |
| 5 | TX_B_C |

### Conector de pines de los botones

Conector de 2×3 pines, paso de 2,54 mm. Cada par de botones es GND + señal.

| Par de pines | Función |
|:---------|:---------|
| Power | Botón de encendido del CM5 (doble clic = apagado, pulsación larga = apagado forzado) |
| Reset | Reinicio por hardware del RP2040 (pin RUN) |
| User | Configurable por el usuario (pendiente de implementación en el firmware) |

### Conectores HDMI (HDMI0, HDMI1)

Conectores FPC horizontales de 20 pines, paso de 0,5 mm (FPC0.5-SMT-20P). Cada canal dispone de protección ESD (RCLAMP0524P) y de alimentación de 5 V con limitación de corriente (AP2553W6-7).

### Conectores MIPI CSI/DSI (MIPI0, MIPI1)

Conectores FPC horizontales de 22 pines, paso de 0,5 mm. Cada canal dispone de protección ESD (RCLAMP0524P). Compatibles con los módulos de cámara y de pantalla de Raspberry Pi.

### Ranura M.2 NVMe (PCIe M.2 M-key)

Zócalo M.2 tipo M para SSD NVMe, compatible con los formatos de 2230 a 2280. Conectado mediante PCIe Gen 2 x1. Incluye un oscilador SUSCLK dedicado para la compatibilidad con la suspensión y reanudación de NVMe (añadido en la v0.6.1).

### Conectores de ventilador (CM5 Fan)

Conectores de ventilador PWM de 4 pines (HC-1.0-4PLT) disponibles tanto en la cara superior como en la inferior de la placa portadora. Están conectados en paralelo: solo debe utilizarse uno a la vez.

| Pin | Función |
|:----|:---------|
| 1 | +5 V |
| 2 | FAN_PWM |
| 3 | FAN_TACHO |
| 4 | GND |

### Puertos USB 3.0

| Conector | Conexión | Límite de corriente |
|:----------|:-----------|:-------------|
| USB3-0 | Directo al USB 3.0 del CM5 | 0,93 A (AP22652W6-7) |
| USB3-1-0 | Puerto 1 del concentrador USB3 (UPD720210) | 0,93 A |
| USB3-1-1 | Puerto 2 del concentrador USB3 | 0,93 A |
| USB3-1-2 | Puerto 3 del concentrador USB3 | 0,93 A |

Todos los puertos disponen de protección ESD (RCLAMP0524P) y de filtrado mediante ferrita.

### Puerto USB del controlador (MCU USB)

Conector hembra micro-USB, únicamente en modo periférico USB 2.0. Se utiliza para actualizar el firmware del RP2040 (grabación de archivos UF2). Con protección ESD (RCLAMP0524P).

### Puerto de arranque USB (USB Boot)

Conector hembra USB Type-C, modo periférico USB 2.0. Conectado al puerto USB 2.0 OTG del CM5 para el arranque desde almacenamiento masivo USB. Con protección ESD (RCLAMP0524P).

## Conector GPIO de 40 pines (Raspberry Pi GPIO Header)

El conector GPIO sigue la disposición estándar de 40 pines de Raspberry Pi. Los periféricos integrados del HALPI2 utilizan los siguientes pines:

| GPIO | Pin | Función | Interfaz | ¿Compartido? |
|:-----|:----|:---------|:----------|:--------|
| 2 | 3 | I2C1 SDA | I2C del sistema | Sí (dirección 0x6d reservada) |
| 3 | 5 | I2C1 SCL | I2C del sistema | Sí (dirección 0x6d reservada) |
| 6 | 31 | SPI0 CS | Controlador CAN FD | CS personalizado; puede coexistir con los pines CS estándar |
| 9 | 21 | SPI0 MISO | Controlador CAN FD | Bus SPI0 compartido |
| 10 | 19 | SPI0 MOSI | Controlador CAN FD | Bus SPI0 compartido |
| 11 | 23 | SPI0 SCLK | Controlador CAN FD | Bus SPI0 compartido |
| 12 | 32 | UART4 TX | RS-485 | Libre si RS-485 está deshabilitado |
| 13 | 33 | UART4 RX | RS-485 | Libre si RS-485 está deshabilitado |
| 24 | 18 | RS-485 EN | RS-485 (modo manual) | Libre en modo automático |
| 26 | 37 | CAN INT | Controlador CAN FD | No |

El resto de los pines GPIO quedan disponibles para HAT y aplicaciones de usuario. En la [Guía de hardware](../user-guide/hardware.md#uso-de-hat) se detallan la compatibilidad de los HAT y las instrucciones para deshabilitar las interfaces integradas.

## Dispositivos I2C

El bus I2C del sistema (I2C1, GPIO 2/3) aloja los siguientes dispositivos:

| Dirección | Dispositivo | Función |
|:--------|:-------|:---------|
| 0x4b | TMP112A | Sensor de temperatura de la placa |
| 0x6d | RP2040 | Controlador de la placa portadora (modo secundario) |

El bus I2C del controlador (I2C0, interno a la placa portadora) se utiliza para la comunicación DDC de HDMI y con las pantallas MIPI, con resistencias de pull-up de 2,2 kΩ.

## Arquitectura de aislamiento

Las interfaces CAN FD y RS-485 están aisladas galvánicamente del resto del sistema. Cada interfaz dispone de alimentación aislada independiente (convertidor CC-CC B0505S-1WR3) y de aislamiento de señal.

| Interfaz | Aislamiento de señal | Aislamiento de alimentación | Masa aislada |
|:----------|:-----------------|:---------------|:----------------|
| CAN FD | ISO7721DR | B0505S-1WR3 | GND_CAN |
| RS-485 | TI41M31 | B0505S-1WR3 | GND_RS485 |

Esto significa que los fallos de bus, los bucles de masa y el ruido presentes en las redes CAN o RS-485 no pueden dañar el sistema principal ni interferir en él.

## Especificaciones mecánicas

### Carcasa

| Parámetro | Valor |
|:----------|:------|
| Material | Aluminio inyectado con recubrimiento en polvo |
| Dimensiones | 200 × 130 × 60 mm (sin conectores) |
| Peso | TODO |
| Grado IP | IP65 |
| Espacio libre interno sobre la placa portadora | 45 mm (admite hasta 2 HAT apilados) |
| Tornillos de la tapa | 4× M4×10 avellanados, cabeza PH2 |
| Junta | Junta de la tapa para el sellado frente a la intemperie |
| Compensación de presión | Tapón compensador de presión (no debe retirarse) |

### Posiciones del panel

El panel frontal incluye posiciones pretaladradas para:

- 1× conector de alimentación E7T
- 1× conector Micro-C NMEA 2000
- 1× Ethernet RJ45
- 2× HDMI Type-A
- 2× USB 3.0 Type-A
- 1× conector de antena RP-SMA (para Wi-Fi/Bluetooth)
- 2× posiciones de antena SMA (suministradas con tapones ciegos)
- 1× tapón compensador de presión
- 3× posiciones de prensaestopas PG7 (suministradas con tapones ciegos)

### Montaje

- Montaje de la placa portadora: 4× tornillos M4×6 a la base de la carcasa
- Montaje de los HAT: 4× insertos roscados M2.5 (v0.5.0 y posteriores; la v0.4.0 requiere instalar las tuercas manualmente)
- Montaje del CM5: 4× tuercas soldadas M2.5

## Gestión térmica

El CM5 se monta en la cara inferior de la placa portadora. El calor se transfiere desde el SoC y el chipset RP1 del CM5 a través de almohadillas térmicas hasta la base de aluminio de la carcasa, que actúa como disipador térmico.

| Componente | Espesor de la almohadilla térmica |
|:----------|:---------------------|
| SoC (BCM2712) | 1 mm |
| RP1 | 2 mm |
| Componentes de la alimentación | 2 mm |

La carcasa estándar proporciona refrigeración pasiva sin ventilador. Se dispone de un conector de ventilador PWM de 4 pines para carcasas personalizadas o aplicaciones con temperatura ambiente elevada.


!!! quote "Información relacionada"
    - **Esquemas y archivos de diseño:** véase [Archivos de diseño y esquemas](../appendices/design-files.md)
    - **Comportamiento de la gestión de la alimentación:** véase [Análisis detallado de la alimentación](./power-supply.md)
    - **Protocolos de interfaz:** véase [Interfaces y conectividad](./interfaces.md)
    - **Controlador y protocolo I2C:** véase [Controlador de la placa portadora](./controller.md)
    - **Instalación física:** véase [Guía de hardware](../user-guide/hardware.md)

# Archivos de diseño y esquemas

Esta página recoge los esquemas y los archivos de diseño mecánico del HALPI2.

El diseño eléctrico del HALPI2 se realiza en KiCad. Los archivos de diseño están disponibles en el [repositorio de GitHub](https://github.com/hatlabs/HALPI2-hardware). Cada versión publicada tiene su etiqueta correspondiente en el repositorio.

Los esquemas se ofrecen a continuación como archivos PDF para mayor comodidad. Los diseños de trazado del PCB solo están disponibles en el repositorio de GitHub.

Los archivos de diseño mecánico se ofrecen inicialmente solo para la carcasa. El diseño se ha realizado con Autocad Fusion, pero los archivos exportados en formato STEP pueden leerse con la mayoría del software CAD.

## Versión 0.6.1

Versión de corrección que incorpora mejoras de integridad de señal y de puesta a tierra detectadas durante las pruebas de producción.

Cambios:

- Se añade un oscilador de reloj para el SUSCLK de NVMe, con el fin de corregir problemas de compatibilidad con determinados NVMe SSD
- Se añaden los condensadores que faltaban en los pares diferenciales RX del concentrador USB3
- Se proporciona puesta a tierra en todos los puntos de montaje

### Archivos de diseño

- Archivos de diseño de KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.1.zip)
- PDF del esquema: [HALPI2-schematic_v0.6.1.pdf](./HALPI2-schematic_v0.6.1.pdf)

## Versión 0.6.0

Tercera versión de producción del HALPI2, con más correcciones menores en la placa portadora. Las prestaciones de la placa son las mismas que en la versión 0.5.0.

Cambios:

- La salida de la línea de 3,3 V ahora la conmuta el controlador en lugar de estar siempre activa
- Se añaden puntos de prueba para mejorar las pruebas de producción
- Se vuelven a trazar las interfaces HDMI, MIPI y USB3 para mejorar la integridad de la señal
- Los conectores FFC de la placa son ahora horizontales
- Se mejora la estabilidad del convertidor reductor de 10 V: ya no zumba en ninguna circunstancia
- Se reimplementa el circuito de equilibrado de los supercondensadores con un único amplificador operacional de 4 unidades
- Se han cambiado las huellas de algunos componentes para mejorar la disponibilidad

### Archivos de diseño

- Archivos de diseño de KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- PDF del esquema: [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)

## Versión 0.5.0

Segunda versión de producción del HALPI2, con correcciones menores en la placa portadora. La funcionalidad de la placa es la misma que en la versión 0.4.0.

Cambios:

- Se corrigen errores menores de la serigrafía
- Se eliminan los vertidos de cobre de 3,3 V de la capa inferior junto a las estructuras de montaje
- Se añaden tuercas soldables para facilitar el montaje de las HAT
- Se añaden tuercas soldables para fijar con mayor seguridad el Compute Module
- Se vuelve a montar los conectores de pines de puente en THT para mejorar la resistencia mecánica
- Se añade un LED de alimentación dedicado de +5 V
- Se relaja el equilibrado de los supercondensadores
- Se reorganizan los conectores de pines de puente para mejorar la usabilidad

### Archivos de diseño

- Archivos de diseño de KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- PDF del esquema: [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- Modelo 3D de la carcasa: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (igual que en la versión 0.4.0)

## Versión 0.4.0

Primera versión pública del HALPI2.

### Archivos de diseño

- Archivos de diseño de KiCad: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- PDF del esquema: [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- Modelo 3D de la carcasa: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

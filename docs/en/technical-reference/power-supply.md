# Power Supply Deep Dive

The HALPI2 power supply is designed for the unstable electrical environments of boats and vehicles: it tolerates voltage spikes and glitches, limits inrush current, and provides enough stored energy to shut the system down safely when input power is lost.

For the electrical specifications, see the [Hardware Reference](./hardware.md). For the state machine that acts on the measurements described here, see the [Carrier Board Controller](./controller.md) reference.

## Input Stage

The nominal input range is 10–32 VDC, covering both 12 V and 24 V systems. The input stage is protected against reverse polarity and against transient overvoltage events of up to 100 V, such as alternator load dumps.

### Current Limiting

An input current limiter controls the maximum current drawn from the supply, selectable between 0.9 A and 2.5 A with a switch on the carrier board. The limit serves two purposes:

- It caps the inrush current when the discharged super-capacitors begin charging at power-on.
- It keeps the total draw within the power budget of the source — the 0.9 A setting (LEN 18) makes HALPI2 safe to power from an NMEA 2000 bus.

The default setting is 0.9 A. Select 2.5 A when the system powers high-current peripherals or when faster startup is desired. The switch location and the procedure for changing it are described in the [Hardware Guide](../user-guide/hardware.md#current-limiting-configuration).

## Super-Capacitor Backup

A bank of super-capacitors provides backup energy for graceful shutdowns. Unlike a battery-based UPS, super-capacitors do not wear out, work across the full temperature range, and charge in seconds — at the cost of a much smaller energy reserve.

### Charging

The super-capacitors charge whenever input power is present. From empty, charging takes approximately:

- 25 seconds at the 0.9 A current limit
- 9 seconds at the 2.5 A current limit

The front-panel LEDs show charging progress as a red bar filling up. The Compute Module is powered on once the super-capacitor voltage reaches the power-on threshold (default 8.0 V).

### Backup Duration

When input power is lost, the super-capacitors carry the full system load. They provide 30–60 seconds of runtime, depending on system load and connected peripherals — sufficient for a graceful operating-system shutdown with margin.

!!! warning "Not a UPS"
    The super-capacitor system is designed to bridge glitches and to power a safe shutdown. It is not designed for continued operation through extended outages.

## Power Loss Detection

The controller measures the input voltage continuously and considers input power lost when the voltage drops below 9.0 V. A blackout timer (default 5 seconds) suppresses shutdown for brief interruptions: the super-capacitors bridge the gap, and operation continues undisturbed if power returns in time. Longer outages trigger the automatic shutdown sequences described in the [Carrier Board Controller](./controller.md#power-loss-and-shutdown-sequences) reference.

## Monitoring

The controller measures input voltage, input current, and super-capacitor voltage, and exposes them through the HALPI daemon:

```bash
halpi status
```

The values are also available programmatically through the daemon's REST API — see the [Software Guide](../user-guide/software.md#rest-api-access).

!!! quote "Related Information"
    - **Electrical specifications:** See [Hardware Reference](./hardware.md)
    - **State machine and shutdown sequences:** See [Carrier Board Controller](./controller.md)
    - **Everyday power behavior:** See [Daily Operation](../user-guide/operation.md)

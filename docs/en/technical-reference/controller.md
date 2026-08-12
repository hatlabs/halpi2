# Carrier Board Controller

The HALPI2 carrier board includes an RP2040 microcontroller that manages power, monitors the system, and controls the front-panel LEDs. The controller runs independently of the Compute Module: it operates from the moment input power is connected, before the operating system boots and after it shuts down. The Compute Module communicates with it over I2C (bus 1, address `0x6d`) through the [HALPI daemon](../user-guide/software.md#halpi-command-line-tool).

This page describes the controller's operating modes, state transitions, and configuration. It documents firmware version 3.3.x. For everyday use, none of this is required reading — see [Daily Operation](../user-guide/operation.md) instead.

## Operating Modes

The controller operates in one of two modes, depending on whether the HALPI daemon is communicating with it.

### Co-op Mode

Co-op mode is the normal operating mode. It is active when the HALPI daemon (`halpid`) is running and communicating with the controller. The preinstalled HaLOS image and all Hat Labs OS images include the daemon.

In Co-op mode:

- The controller and the daemon exchange real-time data: voltages, current, temperatures, and state.
- Power loss events are communicated to the daemon, which initiates a graceful operating-system shutdown.
- The watchdog timer protects against operating-system hangs (see [Watchdog Protection](#watchdog-protection)).
- Configuration can be read and changed with the `halpi` command line tool.

### Solo Mode

Solo mode is the fallback mode. The controller enters it when there is no daemon communication:

- during boot, before the daemon starts
- if the daemon is not installed, has been disabled, or has crashed
- on operating systems without HALPI2 support

In Solo mode the controller still protects against power loss, but with a blunter mechanism: it requests shutdown by simulating power-button presses, and it cannot tell whether the operating system actually completed the shutdown gracefully.

!!! tip "Solo Mode Reliability"
    Solo mode provides essential protection but is less reliable than Co-op mode. Simulated button presses do not work if the operating system is frozen. If you run a custom operating system, install the HALPI daemon — see [Other Debian Distributions](../software-development/ubuntu-installation.md).

## Power Loss and Shutdown Sequences

The controller monitors the input voltage continuously. Input power is considered lost when the input voltage falls below 9.0 V. A blackout timer (default 5 seconds) distinguishes brief glitches from real outages: the super-capacitors bridge the gap, and if power returns within the timer period, nothing else happens.

### Shutdown Sequence in Co-op Mode

1. The daemon detects the power loss from the controller's voltage measurements.
2. The daemon waits for the blackout time limit (default 5 seconds) to pass.
3. The daemon executes the configured shutdown command (default `/sbin/poweroff`).
4. The operating system shuts down gracefully on super-capacitor power.
5. The controller detects that the Compute Module has powered off and disables the 5 V rail.
6. If the shutdown does not complete within 60 seconds, the controller forces power off.
7. The system remains off until input power returns, then restarts automatically.

### Shutdown Sequence in Solo Mode

1. The controller detects power loss and starts the blackout timer (default 5 seconds).
2. When the timer expires, the controller simulates a double power-button press.
3. The operating system responds and begins a graceful shutdown on super-capacitor power.
4. If the shutdown does not complete within 60 seconds, the controller forces power off.
5. The system remains off until input power returns, then restarts automatically.

### Restart Behavior After a Software Shutdown

A shutdown initiated through software while input power remains available (for example, the `shutdown` command or the desktop menu) ends in the *powered down* state. What happens next depends on the `auto_restart` configuration setting:

- `auto_restart` disabled (the factory setting on units produced since early 2026): the system stays off until input power is cycled or a power button is pressed.
- `auto_restart` enabled (the firmware fallback, and the factory setting on earlier units): the controller restarts the system after 5 seconds, so that an unattended system does not stay off because of an accidental shutdown.

Change the setting with `halpi config set auto_restart <true|false>`.

A power-button press or an input power cycle always restarts the system, regardless of the `auto_restart` setting.

## Watchdog Protection

In Co-op mode, a watchdog timer protects against operating-system hangs:

- The daemon must send a watchdog feed to the controller at regular intervals.
- If no feed arrives within the watchdog timeout (default 10 seconds), the controller considers the host unresponsive, shows the alert LED pattern (all LEDs solid red), and power-cycles the Compute Module to recover.
- The timeout is configurable with `halpi config set watchdog_timeout <seconds>`.

## Standby

Standby powers down the Compute Module while the controller remains active, waiting for a scheduled wake-up:

```bash
# Enter standby, wake up after a delay (seconds)
halpi shutdown --standby --time 3600

# Enter standby, wake up at a given time (local time; append Z or an offset for UTC)
halpi shutdown --standby --time "2026-08-13 06:00:00"
```

During the transition, all LEDs show solid blue; in standby, they show dim red. The controller restarts the system at the scheduled time, on a power-button press, or after an input power cycle.

## Status LED Reference

The five front-panel RGB LEDs reflect the controller state. This table is the authoritative mapping from controller states to LED patterns; the [Daily Operation](../user-guide/operation.md#status-led-indicators) page presents a simplified version.

| Controller state | LED pattern |
|:-----------------|:------------|
| PowerOff (no usable input power; controller running on residual charge) | LED 5 solid red |
| OffCharging | Red bar filling as super-capacitors charge |
| SystemStartup | Rainbow sweep, then a cycle of solid colors |
| OperationalSolo | Yellow charge-level bar |
| OperationalCoOp | Green charge-level bar |
| BlackoutSolo | Orange charge-level bar |
| BlackoutCoOp | Dark green charge-level bar |
| BlackoutShutdown, ManualShutdown | Purple charge-level bar |
| PoweredDownBlackout, PoweredDownManual | All off |
| HostUnresponsive (watchdog timeout) | All solid red |
| EnteringStandby | All solid blue |
| Standby | All dim red |
| Super-capacitor overvoltage alarm | All LEDs flashing red |

In the charge-level bar patterns, each lit LED represents one volt of super-capacitor voltage:

| LED | Voltage range |
|:----|:--------------|
| LED 1 | 5.0–6.0 V |
| LED 2 | 6.0–7.0 V |
| LED 3 | 7.0–8.0 V |
| LED 4 | 8.0–9.0 V |
| LED 5 | 9.0–10.0 V |

## Configuration Parameters

Configuration is stored in the controller's flash memory and survives power cycles. Read and change it with `halpi config` — see the [Software Guide](../user-guide/software.md#configuration-management).

| Parameter | Default | Description |
|:----------|:--------|:------------|
| `auto_restart` | `false` on current units (set at production test); firmware fallback `true` | Restart automatically 5 s after a software shutdown while input power is present |
| `watchdog_timeout` | 10 s | Co-op mode watchdog timeout |
| `power_on_threshold` | 8.0 V | Super-capacitor voltage required before the Compute Module is powered on |
| `solo_power_off_threshold` | 5.5 V | Super-capacitor voltage at which the controller forces power off in Solo mode |
| `solo_depleting_timeout` | 5 s | Solo mode blackout timer |
| `led_brightness` | 48 | Front-panel LED brightness (0–255) |

The Co-op mode blackout timer and shutdown command are daemon settings, configured in `/etc/halpid/halpid.conf` (`blackout-time-limit`, default 5 s; `poweroff`, default `/sbin/poweroff`).

!!! quote "Related Information"
    - **Everyday use:** See [Daily Operation](../user-guide/operation.md)
    - **Power system details:** See [Power Supply Deep Dive](./power-supply.md)
    - **Firmware updates:** See [Software Guide](../user-guide/software.md#firmware-updates)
    - **Firmware source and I2C protocol:** See the [HALPI2-firmware repository](https://github.com/hatlabs/HALPI2-firmware)

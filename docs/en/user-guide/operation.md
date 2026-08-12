# Daily Operation

HALPI2 is designed for unattended operation. On the preinstalled HaLOS image — or any operating system with the [HALPI daemon](./software.md#halpi-command-line-tool) installed — power management is automatic: the device charges its backup super-capacitors, rides out voltage glitches, shuts the operating system down safely when power is lost, and starts up again when power returns. None of this requires user action.

## Powering On

HALPI2 has no power button on the enclosure: it starts whenever input power is connected. (An external power button can be wired to the carrier board — see [External Buttons](./interfaces.md#external-buttons).) The LED bar first fills up with red while the super-capacitors charge (seconds to half a minute, depending on the [current limit setting](./hardware.md#current-limiting-configuration)). The LEDs then play a short rainbow and color-cycle animation while the compute module starts, show a yellow bar while the operating system boots, and turn green once the operating system is running and the HALPI daemon has connected.

## Shutting Down

To shut down HALPI2, cut the input power — for example with a switch on the electrical panel. The system detects the power loss, shuts the operating system down gracefully on super-capacitor power, and stays off. The LEDs show a purple bar while the shutdown runs and turn off when it completes.

You can also shut down through software — the desktop menu, the `shutdown` command, or `halpi shutdown`. The system then powers off and stays off until the input power is cycled (or an [external power button](./interfaces.md#external-buttons), if fitted, is pressed).

Optionally, the controller can restart the system automatically about 5 seconds after a software shutdown while input power remains connected, so that an accidental shutdown command never strands an installation that is hard to reach physically. Enable it with `halpi config set auto_restart true`; the setting persists in the controller. Units produced before early 2026 shipped with this behavior enabled — check yours with `halpi config get auto_restart`.

The system can also be put into standby, where it powers off and wakes up again at a scheduled time — see the [Carrier Board Controller](../technical-reference/controller.md#standby) reference.

## Status LED Indicators

The five front-panel LEDs show what the system is doing:

| LED pattern | Meaning |
|:------------|:--------|
| Red bar filling up | Super-capacitors charging before startup — wait |
| Rainbow and cycling colors | Compute module starting up. If the pattern repeats without progress, the module failed to start — see [Troubleshooting](./troubleshooting.md#rainbow-leds) |
| Yellow bar | Running, HALPI daemon not connected — normal for a short time during boot. If it persists, see [Troubleshooting](./troubleshooting.md#leds-stay-yellow) |
| Green bar | Normal operation |
| Orange or dark green bar | Input power lost, running on backup — shutdown follows unless power returns within seconds |
| Purple bar | Shutting down |
| All solid red | Operating system unresponsive — the controller will restart it automatically |
| All flashing red | Super-capacitor fault — contact support |
| All solid blue | Entering standby |
| All dim red | Standby |
| All off | Powered off |

In the bar patterns, the number of lit LEDs shows the super-capacitor charge level. The exact voltage windows and the full state mapping are in the [Carrier Board Controller](../technical-reference/controller.md#status-led-reference) reference.

The LED brightness can be adjusted — see [LED Control](./software.md#led-control). The LEDs can also be repurposed as a display for system metrics and marine data (network activity, tank levels, NMEA 2000 and Signal K values) with the [HALPI2 blinkenlights](https://github.com/hatlabs/HALPI2-blinkenlights) add-on.

## When Power Is Lost

Nothing needs to be done. Brief dips and glitches — up to 5 seconds by default — are bridged by the super-capacitors, and operation continues undisturbed. In a longer outage, the system shuts itself down gracefully on the 30–60 seconds of backup power the super-capacitors hold. When input power returns, the system starts up again automatically.

!!! warning "Not a UPS"
    The super-capacitors exist to bridge glitches and to power a safe shutdown. For continued operation through extended outages, an external uninterruptible power supply is required.

## Checking System Health

A green LED bar means the system is healthy. For details, the `halpi` command shows the controller state, voltages, current, and temperatures:

```bash
halpi status
```

If something looks wrong, see [Troubleshooting](./troubleshooting.md) and the [Software Guide](./software.md#halpi-command-line-tool).

## Running Without the Daemon

On operating systems without the HALPI daemon, the controller falls back to a basic protection mode: it still detects power loss and requests a shutdown, but by simulating power-button presses — which fails if the system is frozen — and monitoring and configuration are unavailable. If you run a custom operating system, install the daemon; see [Other Debian Distributions](../software-development/ubuntu-installation.md). How the two modes work is described in the [Carrier Board Controller](../technical-reference/controller.md#operating-modes) reference.

!!! quote "Related Information"
    - **How power management works internally:** See [Carrier Board Controller](../technical-reference/controller.md)
    - **Power system details:** See [Power Supply Deep Dive](../technical-reference/power-supply.md)
    - **The `halpi` command and daemon:** See [Software Guide](./software.md)
    - **Problems:** See [Troubleshooting](./troubleshooting.md)

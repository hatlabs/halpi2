# FAQ

## Why does HALPI2 restart after I shut it down?

Your device has automatic restart enabled: with `auto_restart` set to `true`, the controller restarts the system about 5 seconds after a software shutdown while input power is connected. Units produced before early 2026 shipped this way; current units ship with it disabled. Turn it off with `halpi config set auto_restart false` — or keep it, since it ensures an unattended system does not stay off after an accidental shutdown command. With it enabled, shut down permanently by cutting the input power. See [Shutting Down](user-guide/operation.md#shutting-down).

## How do I turn HALPI2 off?

Cut the input power. The system detects the power loss and shuts down gracefully on super-capacitor power — this is the designed way to turn it off. See [Shutting Down](user-guide/operation.md#shutting-down).

## Do I need to do anything when the power goes out?

No. Brief glitches are bridged by the super-capacitors, longer outages trigger an automatic safe shutdown, and the system restarts by itself when power returns. See [When Power Is Lost](user-guide/operation.md#when-power-is-lost).

## How long does the backup power last?

The super-capacitors provide 30–60 seconds, depending on system load. That is enough for a safe shutdown with margin, but HALPI2 is not a UPS — it does not keep running through extended outages. See [Power Supply Deep Dive](technical-reference/power-supply.md).

## Can HALPI2 stay powered around the clock?

Yes. HALPI2 is designed for continuous unattended operation, and its power management assumes it: the system recovers from power loss and operating-system hangs without user intervention.

## What does it mean when the LEDs stay yellow?

A yellow bar means the system is running but the HALPI daemon has not connected — normal for a short time during boot. A persistent yellow bar means the operating system is not booting or the daemon is not installed. See [Troubleshooting](user-guide/troubleshooting.md#leds-stay-yellow).

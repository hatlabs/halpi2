# System Operation

## Power Management and Shutdown Procedures

HALPI2 features a power supply designed to withstand voltage spikes, glitches and short-term outages. This section helps you understand its operation and how to configure it for your needs.

### Power System Overview

HALPI2's power management system consists of several integrated components:

- **Wide-range power supply** (11-32 VDC input with protection up to 100 VDC)
- **Super-capacitor backup system** for graceful shutdowns during power loss
- **Current limiting** (0.9A or 2.5A selectable)
- **Power loss detection** and automatic shutdown initiation
- **Input voltage and current monitoring**

The system operates in two distinct modes depending on software configuration:

**Solo Mode:** HALPI2 operates independently, monitoring input voltage and managing shutdowns autonomously without software coordination.

**Co-op Mode:** The HALPI daemon manages the power system, providing enhanced monitoring, configuration options, and coordinated shutdown procedures.

### Operational Modes

#### Solo Mode

Solo mode provides basic autonomous operation when the HALPI daemon is not running or has failed to start. The controller operates independently to protect the system:

**Characteristics:**
- No software communication required
- Basic power loss protection active
- Automatic shutdown via simulated power button presses
- Limited monitoring and configuration options

**Automatic Behavior:**
- Monitors input voltage continuously
- Triggers shutdown sequence on power loss detection
- Uses internal blackout timer (default 5 seconds) before initiating shutdown
- Simulates double power-button presses to request system shutdown
- Forces power-off after 60 seconds if shutdown doesn't complete
- System will restart automatically when stable power returns

**When Active:**
- During initial boot before daemon starts
- If HALPI daemon fails or is disabled
- On unsupported operating systems without daemon

> 💡 **Solo Mode Reliability**
>
> While Solo mode provides basic protection, it's less reliable than Co-op mode because there's no direct communication with the operating system. The controller must rely on simulated button presses to request shutdown.

#### Co-op Mode

Co-op mode provides full power management functionality when the HALPI daemon is running and communicating with the controller:

**Co-op Mode Features:**
- Direct communication between controller and daemon software
- Watchdog timer ensures system stability (30-second timeout)
- Configurable shutdown behavior and timing
- Real-time monitoring of power parameters

**Automatic Behavior:**
- Monitoring of input power status
- Configurable blackout timer (default 5 seconds) allows for brief power interruptions
- Shutdown command execution (default: `/sbin/poweroff`)
- Super-capacitor backup provides time for safe file system closure
- System restart management based on configuration

**Watchdog Protection:**
The daemon must "feed the watchdog" by communicating with the controller regularly. If communication stops for 30 seconds, the system automatically reboots to recover from software failures.

**When Active:**
- Normal operation with supported operating systems
- HALPI daemon running and healthy
- Full system monitoring and control available

> 🔧 **Daemon Status Check**
>
> Verify Co-op mode operation: `systemctl status halpid`
>
> View controller state: `halpi status`
>
> Green LEDs indicate active Co-op mode operation.

### Shutdown Procedures

#### Automatic Shutdown

HALPI2 automatically protects your system during power loss events through its super-capacitor backup system and shutdown logic.

**Power Loss Detection:**
1. **Monitoring** of input voltage and power availability
2. **Blackout detection** when input power is lost or falls below threshold
3. **Blackout timer activation** to distinguish brief glitches from actual power loss

**Shutdown Sequence:**
When power loss exceeds the blackout timer period:

**Co-op Mode Sequence:**
1. HALPI daemon detects power loss condition
2. Daemon initiates shutdown command
3. Operating system closes all applications and file systems
4. Super-capacitors provide backup power throughout the process
5. Controller monitors for shutdown completion
6. 5V rail disabled when Compute Module 5 powers off
7. System remains powered off until power returns

**Solo Mode Sequence:**
1. Controller detects power loss internally
2. Simulated power button double-presses sent to Compute Module
3. Operating system responds to button press shutdown request
4. Super-capacitors maintain power during shutdown process
5. 60-second timeout ensures power-off if shutdown hangs
6. Forced power-off if graceful shutdown doesn't complete

**Backup Power Duration:**
- Super-capacitors typically provide 30-60 seconds of backup power
- Duration depends on system load and connected peripherals
- Sufficient time for safe file system closure and process termination
- Charging time: ~25 seconds (0.9A limit) or ~9 seconds (2.5A limit)

> ⚠️ **Power Loss Protection**
>
> The super-capacitor system is designed for graceful shutdown, not continued operation. Do not rely on it to maintain system operation during extended power outages.

#### Manual Shutdown Considerations

HALPI2's design prioritizes automated operation and recovery, which affects manual shutdown behavior:

**Automatic Restart Behavior:**
- Manual shutdowns (via command line, desktop menu, or SSH) result in normal system shutdown
- However, if input power remains available, the system will automatically restart after a 5-second grace period
- This ensures recovery from accidental shutdowns and maintains unattended operation reliability

**Intentional Shutdown Methods:**

**For Temporary Shutdown:**
1. Use the standby mode functionality (when available) to power off the Compute Module while keeping the controller active
2. Standby mode allows wake-up from external events without full power cycling

**For Permanent Shutdown:**
1. **Disconnect input power** after initiating graceful shutdown
2. **Use daemon configuration** to disable automatic restart: `halpi config set auto_restart false`. After this, the system will not restart automatically after a manual shutdown.
3. **Physical power switch** at the power source for complete shutdown

**Standby Mode Operation:**
> 🔧 **Feature Status**
>
> Standby mode functionality is planned for future firmware releases. This will allow the Raspberry Pi to be powered off while the HALPI2 controller remains active, waiting for wake-up events.

> 📖 **Related Information**
>
> - **LED status indicators:** See [Status LED Meanings](./operation.md#status-led-meanings)
> - **Manual power button:** See [User Button Configuration](./operation.md#user-button-configuration)
> - **System monitoring:** See [Monitoring System Health](./operation.md#monitoring-system-health)
> - **Technical specifications:** See [Power Supply Deep Dive](../technical-reference/power-supply.md)
> - **Troubleshooting:** See [Troubleshooting Guide](./troubleshooting.md)


## Status LED Indicators

HALPI2 features five RGB LEDs that provide visual feedback about system status and power conditions.

### LED Status Quick Reference

| LED Pattern | Color | Meaning |
|-------------|-------|---------|
| Progressive fill | Red | Super-capacitor charging |
| Rainbow | Multi | System booting |
| All solid | Yellow | Solo mode operation |
| All solid | Green | Co-op mode operation |
| LED 1 flashing | Red | Input overvoltage warning |
| LED 5 flashing | Red | Super-capacitor overvoltage warning |
| All solid | Red | Watchdog timeout |
| Scrolling | Green/Yellow | Backup power active |
| All solid | Purple | Shutdown in progress |
| All solid | Blue | Shutdown to Standby in progress |
| All solid | Dim Red | Standby |
| All off | None | System off |
| All blinking rapidly | Red | Fault condition - contact manufacturer |

### Super-Capacitor Voltage Indication

During operation, the LEDs function as a voltage indicator showing super-capacitor charge level:

- **LED 1**: 5.0-6.0V
- **LED 2**: 6.0-7.0V
- **LED 3**: 7.0-8.0V
- **LED 4**: 8.0-9.0V
- **LED 5**: 9.0-10.0V

> 📖 **Related Information**
>
> - **Power management:** See [Power Management and Shutdown Procedures](#power-management-and-shutdown-procedures)
> - **System monitoring:** See [Monitoring System Health](#monitoring-system-health)

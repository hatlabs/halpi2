# System Operation

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

## Power Management and Shutdown Procedures

HALPI2 features a power supply designed to withstand voltage spikes, glitches and short-term outages.

### Power System Overview

HALPI2's power management system consists of:

- **Wide-range power supply** (11-32 VDC input with protection up to 100 VDC)
- **Super-capacitor backup system** for graceful shutdowns during power loss
- **Current limiting** (0.9A or 2.5A selectable)
- **Power loss detection** and automatic shutdown initiation
- **Input voltage and current monitoring**

The system operates in two modes: Solo Mode and Co-op Mode.

### Solo Mode Operation

Solo mode provides basic autonomous operation when the HALPI daemon is not running. The controller operates independently without software communication.

#### Solo Mode Characteristics

- **No software communication required**
- **Basic power loss protection** - monitors input voltage and responds to power loss
- **Automatic shutdown via simulated power button presses**
- **Limited monitoring and configuration options**

#### Solo Mode Power Loss and Shutdown

**Power Loss Detection:**
The controller monitors input voltage and detects power loss. A blackout timer (default 5 seconds) prevents shutdowns during brief interruptions.

**Automatic Shutdown Sequence:**
1. **Controller detects power loss**
2. **Blackout timer activates** to distinguish glitches from actual power loss
3. **Simulated power button presses** - controller sends double power-button presses to Compute Module
4. **Operating system responds** and begins graceful shutdown
5. **Super-capacitors maintain power** (typically 30-60 seconds available)
6. **60-second timeout protection** - forced power-off if graceful shutdown fails
7. **System remains off** until power returns
8. **Automatic restart** when power is restored

**Manual Shutdown in Solo Mode:**
- Normal operating system shutdown occurs
- System automatically restarts after 5 seconds if input power remains available
- For permanent shutdown, disconnect input power after initiating graceful shutdown

#### When Solo Mode is Active

Solo mode occurs:
- During initial boot before HALPI daemon starts
- If HALPI daemon fails to start or is disabled
- On unsupported operating systems without the daemon
- When the daemon has crashed or become unresponsive

> 💡 **Solo Mode Reliability**
>
> Solo mode provides essential protection but is less reliable than Co-op mode. The controller relies on simulated button presses to request shutdown, which may not work if the system is frozen.

### Co-op Mode Operation

Co-op mode provides full power management functionality when the HALPI daemon is running and communicating with the controller.

#### Co-op Mode Features

- **Direct software communication** - real-time data exchange between controller and daemon
- **Watchdog timer protection** - 30-second timeout ensures system stability
- **Configurable shutdown behavior** - customizable timing and commands
- **Real-time monitoring** - comprehensive power parameter monitoring
- **Advanced configuration options**

#### Co-op Mode Power Loss and Shutdown

**Power Loss Detection:**
The controller monitors input power and communicates events directly to the HALPI daemon. The configurable blackout timer (default 5 seconds) allows brief power interruptions without initiating shutdown.

**Automatic Shutdown Sequence:**
1. **Controller detects power loss** and communicates to HALPI daemon
2. **Blackout timer assessment** - daemon evaluates if power loss exceeds threshold
3. **Shutdown command execution** - daemon executes shutdown command (default: `/sbin/poweroff`)
4. **Operating system graceful shutdown** - applications close and filesystems unmount safely
5. **Super-capacitor backup power** provides energy throughout shutdown
6. **Controller monitors completion** - tracks when Compute Module powers off
7. **5V rail disabled** when shutdown is complete
8. **System remains off** until input power returns
9. **Restart management** - based on configuration, system restarts automatically or remains off

**Manual Shutdown in Co-op Mode:**
- Standard graceful shutdown occurs when initiated through software
- System automatically restarts after 5 seconds if input power remains available
- To prevent automatic restart, disconnect power or configure `auto_restart` to `false`

#### Watchdog Protection

Co-op mode includes watchdog timer protection:

- **30-second communication timeout** - daemon must communicate with controller regularly
- **Automatic recovery** - system reboots if communication stops
- **Software failure protection** - ensures recovery from daemon crashes or system hangs
- **"Feeding the watchdog"** - daemon sends regular status updates to reset timer

#### When Co-op Mode is Active

Co-op mode occurs when:
- HALPI daemon is running and healthy
- Communication between daemon and controller is established
- System operates on a supported operating system
- Full system monitoring and control features are available

> 🔧 **Verifying Co-op Mode**
>
> Check daemon status: `systemctl status halpid`
>
> View controller state: `halpi status`
>
> For further information on the `halpi` command, see the [Software Guide](./software.md#halpi-daemon-halpid).

### Backup Power and Capacitor System

Both modes rely on the super-capacitor backup system for graceful shutdown protection:

**Backup Power Duration:**
- Super-capacitors provide 30-60 seconds of backup power
- Duration depends on system load and connected peripherals
- Sufficient time for safe file system closure and process termination
- Not designed for continued operation during extended outages

**Charging Characteristics:**
- Charging time: 25 seconds with 0.9A current limit
- Charging time: 9 seconds with 2.5A current limit
- Visual charging progress shown through LED progression (red fill pattern)

> ⚠️ **Power Loss Protection Limitation**
>
> The super-capacitor system is designed for graceful shutdown, not continued operation. Do not rely on it for extended power outages.

### Manual Shutdown Considerations

HALPI2 prioritizes automated operation and recovery, affecting manual shutdown behavior.

#### Automatic Restart Behavior

By default, HALPI2 restarts after manual shutdowns when input power remains available:

- Manual shutdowns result in normal operating system shutdown
- 5-second grace period follows shutdown completion
- System automatically restarts to maintain operational availability
- Ensures recovery from accidental shutdowns

#### Intentional Shutdown Methods

For permanent shutdown, use one of these approaches:

**Power Disconnection Method:**
1. Initiate graceful shutdown through software
2. Wait for shutdown completion (LEDs turn off)
3. Disconnect input power to prevent automatic restart

**Configuration Method:**
1. Disable automatic restart: `halpi config set auto_restart false`
2. Initiate shutdown through software
3. System remains off after shutdown completion

**Standby Mode (Future):**
> 🔧 **Feature Status**
>
> Standby mode functionality is planned for future firmware releases. This will allow the Compute Module to be powered off while the HALPI2 controller remains active, waiting for wake-up events.

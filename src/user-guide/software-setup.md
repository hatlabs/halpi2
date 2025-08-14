# Software Setup

- Pre-built image options (OpenPlotter, Raspberry Pi OS)
- Flashing images to NVMe storage
- Initial system configuration
- Software updates
- Network setup (WiFi, Ethernet)
- Remote access (SSH, VNC)
- Firmware updates

## Software Setup

Hat Labs provides pre-built images for HALPI2, which can be downloaded from
[GitHub](https://github.com/hatlabs/openplotter-halpi/releases). The pre-built
images include the necessary configuration and customizations for the HALPI2
hardware.

All pre-built images have the CAN (NMEA 2000) interface enabled by default, as
network device `can0`. RS-485 (NMEA 0183) is available as `/dev/ttyAMA0`.

### OpenPlotter

OpenPlotter is a Raspberry Pi OS operating system image with useful
additions for marine applications. The pre-installed image is based on the
OpenPlotter Headless edition that enables a WiFi Access Point for easy
configuration and access to the HALPI2.

If you are not using a display, keyboard and a mouse with the HALPI2, you can
connect to the computer either using an Ethernet cable or via the WiFi Access Point.

With either, you can access the HALPI2 computer using VNC or SSH. VNC provides
a remote desktop interface to access the HALPI2 desktop, while SSH
allows you to access the command line interface. You need to download RealVNC's
[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) to use VNC.

Since both the access point and the
default user come with default passwords, it is imperative that the passwords
are changed immediately after the first boot. The process is described in
the [OpenPlotter documentation](https://openplotter.readthedocs.io/latest/getting_started/first_steps.html).

### Raspberry Pi OS and Raspberry Pi OS Lite

If you prefer to use the standard Raspberry Pi OS, you can download the latest
image with HALPI2 support from [the GitHub repository](https://github.com/hatlabs/openplotter-halpi/releases).
Flash the image to the SSD disk using Raspberry Pi Imager. When flashing, you
can apply customizations such as setting the hostname, enabling SSH, and
configuring WiFi.

If you decide to not apply customizations, you need to have a display and
keyboard connected to the HALPI2 to complete the initial setup. You will be asked
to provide a username and password at the first boot.





## HALPI Command Line Tool

HALPI2's software interface consists of the `halpid` daemon service and the `halpi` command line tool. Together, they provide system monitoring, configuration, and control capabilities.

### HALPI Daemon (`halpid`)

The HALPI daemon runs as a system service, providing communication between the operating system and the HALPI2 controller. It enables Co-op mode operation with full monitoring and power management features.

#### Service Management

The daemon is managed through systemd:

```bash
# Check daemon status
systemctl status halpid

# Start the daemon
sudo systemctl start halpid

# Stop the daemon
sudo systemctl stop halpid

# Enable auto-start at boot
sudo systemctl enable halpid

# Disable auto-start
sudo systemctl disable halpid

# View daemon logs
journalctl -u halpid -f
```

#### Configuration

The daemon configuration is stored in `/etc/halpid.conf`. Key settings include:

- **Watchdog timeout** - How often to communicate with controller
- **Power loss response** - Actions to take during power loss
- **Monitoring intervals** - Frequency of health checks
- **LED brightness** - Default LED brightness setting

Configuration changes require daemon restart:

```bash
sudo systemctl restart halpid
```

### HALPI Command Line Tool (`halpi`)

The `halpi` command provides direct access to controller functions and system status. It communicates with the daemon to execute commands and retrieve information.

#### Basic System Information

**System Status:**
```bash
# Display comprehensive system status
halpi print

# Show controller firmware version
halpi version

# Display power and voltage information
halpi power
```

**Example Output:**
```
$ halpi print
Controller Status: Co-op Mode
Input Voltage: 12.3V
Input Current: 0.8A
Super-cap Voltage: 9.1V
Temperature: 42°C
Watchdog: Active (30s timeout)
LEDs: Green (brightness 128)
```

#### LED Control

**Brightness Management:**
```bash
# Get current LED brightness (0-255)
halpi get led-brightness

# Set LED brightness
halpi set led-brightness 64

# Minimum brightness for dark environments
halpi set led-brightness 16

# Maximum brightness
halpi set led-brightness 255
```

#### Power Management

**System Control:**
```bash
# Initiate graceful shutdown
halpi shutdown

# Request system restart
halpi restart

# Enter standby mode (when available)
halpi standby
```

**Power Monitoring:**
```bash
# Display power parameters
halpi power

# Monitor super-capacitor status
halpi supercap

# Show power history (if logging enabled)
halpi power-log
```

#### Configuration Commands

**System Settings:**
```bash
# View current configuration
halpi config show

# Set watchdog timeout (seconds)
halpi config watchdog-timeout 30

# Configure power loss delay
halpi config power-loss-delay 5

# Reset to default settings
halpi config reset
```

#### Hardware Control

**Component Management:**
```bash
# USB port control (when supported)
halpi usb disable 1
halpi usb enable 1

# PCIe power management
halpi pcie sleep
halpi pcie wake
```

#### Status and Monitoring

**Real-time Monitoring:**
```bash
# Continuous status display
halpi monitor

# Temperature monitoring
halpi temperature

# Event log display
halpi events

# Hardware diagnostic information
halpi diagnostic
```

### Common Usage Patterns

#### Daily Operations

**System Health Check:**
```bash
# Quick system overview
halpi print

# Check for any alerts or issues
halpi events | tail -10
```

**LED Adjustment:**
```bash
# Dim LEDs for nighttime operation
halpi set led-brightness 32

# Restore normal brightness
halpi set led-brightness 128
```

#### Troubleshooting

**Daemon Communication:**
```bash
# Verify daemon is running
systemctl status halpid

# Check communication with controller
halpi print

# Review recent events
halpi events
```

**Power Issues:**
```bash
# Check power parameters
halpi power

# Monitor super-capacitor status
halpi supercap

# Review power-related events
halpi events | grep power
```

#### Configuration Changes

**Watchdog Settings:**
```bash
# Check current watchdog timeout
halpi config show | grep watchdog

# Adjust timeout for specific application
halpi config watchdog-timeout 60

# Restart daemon to apply changes
sudo systemctl restart halpid
```

### Integration with System Scripts

The `halpi` command can be integrated into system scripts for automation:

```bash
#!/bin/bash
# Example: Check system health in a cron job

STATUS=$(halpi print | grep "Controller Status")
if [[ $STATUS != *"Co-op Mode"* ]]; then
    echo "HALPI2 not in Co-op mode" | logger
    # Send alert or take corrective action
fi
```

### Error Handling

**Common Issues:**

❌ **"Cannot connect to daemon":**
- Check if `halpid` service is running: `systemctl status halpid`
- Restart the daemon: `sudo systemctl restart halpid`

❌ **"Controller not responding":**
- Hardware communication issue
- Try controller reset (physical reset button)
- Check hardware connections

❌ **"Permission denied":**
- Some commands require sudo privileges
- Add user to appropriate group if available
- Use `sudo halpi` for system-level commands

### Command Reference Summary

| Command | Purpose |
|---------|---------|
| `halpi print` | Complete system status |
| `halpi power` | Power and voltage information |
| `halpi get/set led-brightness` | LED brightness control |
| `halpi config show` | Display current configuration |
| `halpi monitor` | Real-time status monitoring |
| `halpi events` | System event log |
| `halpi shutdown` | Graceful system shutdown |

> 📖 **Related Information**
>
> - **Power management:** See [Power Management and Shutdown Procedures](#power-management-and-shutdown-procedures)
> - **LED indicators:** See [Status LED Indicators](#status-led-indicators)
> - **Troubleshooting:** See [Troubleshooting Guide](./troubleshooting.md)
> - **Advanced configuration:** See [Advanced Configuration](../software-development/advanced-config.md)





### Option 2: Flash Customized Raspberry Pi OS

- 💡 **Quick Tip:** These instructions can also be used for reinstalling OpenPlotter if you want to reset your device to factory settings.

You'll need a USB NVMe adapter and a computer with Raspberry Pi Imager or similar software to flash the image to the NVMe SSD. USB NVMe adapters are available at low cost from various online retailers.

![NVMe Adapter](./nvme-adapter.jpg)

Follow the steps below to flash the image:

1. **Remove the NVMe SSD** from the HALPI2 unit. Follow the instructions provided in the [User Guide](../user-guide/operation.md) for safely removing the SSD.
2. **Download a HALPI2-compatible image** from [GitHub openplotter-halpi releases](https://github.com/hatlabs/openplotter-halpi/releases)
3. **Insert the SSD into the USB NVMe adapter** and connect it to your computer.
4. **Flash to NVMe SSD** using Raspberry Pi Imager. If you are flashing a Raspberry Pi OS image, edit and apply OS customization settings as needed. If custom settings are not applied, you will need a USB keyboard and mouse for the initial setup. ⚠️ **Warning**: When using the OpenPlotter image or 3rd party images, OS customization settings should **not** be applied.

### Option 3: Manual Configuration

When using a custom image or OS, you will need to manually configure the HALPI2 features. This includes:
- Configuring device tree overlays for HALPI2 hardware
- Setting up the HALPI2 daemon for hardware control
- Configuring interfaces (CAN, RS-485, etc.)

The detailed steps are described in the [Software Setup section](../user-guide/software-setup.md) of the User Guide.

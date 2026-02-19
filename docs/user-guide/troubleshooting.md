# Troubleshooting

This page covers common issues you may encounter when operating HALPI2 and how to resolve them.

## Power and Boot Issues

### System does not power on

**Symptoms:** No LED activity, no signs of life after connecting power.

1. Verify input voltage is within range (11–32 VDC) using a multimeter at the E7T connector.
2. Check the power cable connections — ensure the E7T connector is fully seated.
3. If using NMEA 2000 bus power, verify that the current limiter is set to 0.9A and that the network can supply sufficient current.
4. Open the enclosure and check for any visible damage or loose internal connections.

### LEDs light up but the system does not boot

**Symptoms:** LEDs show the red charging pattern or rainbow boot pattern, but the system never reaches the operational state (solid yellow or green LEDs).

1. Wait for the super-capacitor to charge — the red progressive fill must complete before the system starts. This takes 9–25 seconds depending on the current limit setting.
2. If the LEDs remain in the rainbow pattern for more than 60 seconds, the Compute Module may not be booting. Connect a display via HDMI to check for boot errors.
3. Verify the NVMe SSD is properly seated in its M.2 slot.
4. Check that the boot mode switch is in the "Normal" position (not "Abnormal"/USB boot mode).

### System keeps restarting

**Symptoms:** The system boots, runs for a short time, then restarts in a loop.

This is most commonly caused by the watchdog timer in Co-op mode. When the HALPI daemon (`halpid`) is not running or cannot communicate with the controller, the 30-second watchdog timeout triggers a restart.

1. Check if the daemon is running: `systemctl status halpid`
2. Check daemon logs for errors: `journalctl -u halpid -e`
3. If the daemon is failing to start, check the configuration: `cat /etc/halpid/halpid.conf`
4. As a temporary measure, you can disable the daemon to fall back to Solo mode: `sudo systemctl stop halpid`

!!! tip "Distinguishing watchdog restarts from other issues"
    If LEDs show solid red before the restart, the watchdog has timed out. If the system restarts without the red LED warning, the issue is likely at the operating system level (kernel panic, out-of-memory, etc.).

### System shuts down unexpectedly

**Symptoms:** System powers off without user intervention, even though external power is connected.

1. Check input voltage stability — brief voltage dips below the threshold trigger the blackout timer. Use `halpi status` to monitor `V_in` in real time.
2. Check the blackout timer setting: `halpi config get solo_depleting_timeout` (default: 5 seconds). If your power source has frequent short interruptions, you may need to increase this value.
3. Inspect the power cable for loose connections or damaged conductors that could cause intermittent contact.
4. If using NMEA 2000 bus power, verify that the network voltage remains stable under load. Other high-draw devices on the network can cause voltage drops.

## Daemon and Controller Communication

### `halpi status` shows "Solo" mode instead of "Co-op"

The system is running without full daemon-controller coordination. This means the daemon is not communicating with the controller.

1. Verify the daemon is running: `systemctl status halpid`
2. Start the daemon if it's stopped: `sudo systemctl start halpid`
3. Check for I2C communication errors in the logs: `journalctl -u halpid -e | grep -i error`
4. Verify I2C bus access: `i2cdetect -y 1` — address `0x6d` should appear. If it doesn't, the controller may not be responding.

### `halpi` command returns errors

**"Connection refused" or "socket not found":**
The daemon is not running. Start it with `sudo systemctl start halpid`.

**"Permission denied":**
The `halpi` command requires the user to be in the appropriate group or use `sudo`.

**"Timeout" errors:**
The daemon is running but cannot communicate with the controller over I2C. Check physical connections and I2C bus integrity:

```bash
# Check if the I2C device is accessible
ls -l /dev/i2c-1

# Scan for devices on the I2C bus
i2cdetect -y 1
```

### Firmware update failed or rolled back

After a firmware update, if the system restarts within 30 seconds, the firmware automatically rolls back to the previous version as a safety measure.

1. Check current firmware version: `halpi get firmware_version`
2. Retry the update: `sudo apt update && sudo apt install --reinstall halpi2-firmware`
3. After the update installs, perform a clean shutdown: `sudo shutdown -h now`
4. Wait for the system to fully power off before reconnecting — allow at least 30 seconds before the next restart to prevent the rollback mechanism from triggering.

## Network and Interface Issues

### No NMEA 2000 data

**Symptoms:** `candump can0` shows no output, or Signal K is not receiving data.

1. Check the CAN interface status:
    ```bash
    ip link show can0
    ```
    The interface should show `UP`. If it shows `DOWN`, bring it up:
    ```bash
    sudo ip link set can0 up type can bitrate 250000
    ```

2. Check the RX LED on the carrier board — it should flash when data is present on the network. If the RX LED is inactive:
    - Verify the Micro-C cable connection and T-connector placement.
    - Check that the NMEA 2000 network has power and other devices are transmitting.
    - Ensure the 120Ω termination jumper is **not** enabled for NMEA 2000 networks.

3. If the RX LED flashes but `candump` shows nothing, the issue is in software. Verify the CAN interface configuration:
    ```bash
    ip -details link show can0
    ```

4. Check for CAN bus errors:
    ```bash
    ip -statistics link show can0
    ```
    High error counts suggest wiring problems, incorrect baud rate, or bus contention.

### No NMEA 0183 data on RS-485

**Symptoms:** No data on `/dev/ttyAMA4`, or the connected device is not responding.

1. Check the RX/TX LEDs on the carrier board for the RS-485 interface.
2. Verify the serial port exists and is accessible:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Test with a simple serial monitor:
    ```bash
    # For standard NMEA 0183 at 4800 baud
    stty -F /dev/ttyAMA4 4800
    cat /dev/ttyAMA4
    ```
4. Check wiring polarity — RS-485 uses differential signaling (TX+/TX−, RX+/RX−). Swapped polarity will prevent communication.
5. For multi-talker RS-485 networks, ensure the transmit enable mode is configured correctly (automatic vs. manual).

### Ethernet link not established

1. Check the Ethernet cable and RJ45 connector. Try a different cable.
2. Verify link status: `ip link show eth0`
3. If the link is up but there's no IP address, check DHCP: `sudo dhclient eth0`
4. For static IP configurations, verify the settings in `/etc/network/interfaces` or NetworkManager.

## Operating System Issues

### Cannot SSH into the device

1. Verify SSH is enabled: `sudo systemctl status ssh`
2. Check network connectivity — can you ping the device?
3. On OpenPlotter images, SSH is enabled by default. On Raspberry Pi OS, SSH may need to be enabled via `raspi-config` or by placing an empty `ssh` file in the boot partition.
4. Check the firewall rules: `sudo iptables -L`

### System runs slowly or freezes

1. Check CPU temperature — passive cooling depends on good thermal contact with the enclosure:
    ```bash
    vcgencmd measure_temp
    ```
    Temperatures above 80°C indicate a thermal issue. Verify the thermal pad between the CM5 and enclosure lid is properly positioned.

2. Check memory usage: `free -h`
3. Check disk usage: `df -h` — a full NVMe SSD will cause severe performance issues.
4. Check for runaway processes: `top` or `htop`

### Clock is wrong after power loss

HALPI2 has a real-time clock (RTC) with a backup battery that maintains time during power outages. If the clock resets:

1. Check the RTC battery — it may need replacement if the system has been unpowered for an extended period.
2. Verify NTP synchronization when network is available: `timedatectl status`
3. Manually set the time if needed: `sudo timedatectl set-time "2025-01-15 14:30:00"`

## LED Diagnostics

Use the LED patterns to quickly diagnose system state:

| Symptom | LED Pattern | Likely Cause |
|:--------|:------------|:-------------|
| System won't start | No LEDs | No input power or hardware fault |
| Stuck during startup | Red progressive fill | Super-capacitor still charging — wait |
| Stuck during startup | Rainbow pattern | CM5 not booting — check SSD and boot switch |
| Unexpected shutdown | Scrolling green/yellow | Power loss detected — check input power |
| Reboot loop | Solid red before restart | Watchdog timeout — check `halpid` status |
| Overvoltage | LED 1 flashing red | Input voltage too high (>32V) |
| Fault | All LEDs blinking red | Hardware fault — contact manufacturer |

!!! quote "Related Information"
    - **LED patterns:** See [Status LED Indicators](./operation.md#status-led-indicators)
    - **Power management:** See [Power Management and Shutdown Procedures](./operation.md#power-management-and-shutdown-procedures)
    - **Daemon management:** See [Software Guide](./software.md#halpi-daemon-halpid)
    - **CAN interface details:** See [Interfaces and Connectivity](./interfaces.md#can-fd-nmea-2000)
    - **RS-485 interface details:** See [Interfaces and Connectivity](./interfaces.md#rs-485-nmea-0183)

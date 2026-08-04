# Troubleshooting

This page covers common issues you may encounter when operating HALPI2 and how to resolve them.

## Power and Boot Issues

### System does not power on

**Symptoms:** No LED activity, no signs of life after connecting power.

1. Verify input voltage is within range (11–32 VDC) using a multimeter at the E7T connector.
2. Check the power cable connections — ensure the E7T connector is fully seated.
3. If using NMEA 2000 bus power, verify that the current limiter is set to 0.9A and that the network can supply sufficient current.
4. Open the enclosure and check for any visible damage or loose internal connections.

### Rainbow LEDs

**Symptoms:** LEDs cycle through a rainbow pattern and never progress to a steady state.

The rainbow pattern means the controller has powered on but the CM5 is not detected. This can happen if:

- The Compute Module is not installed or not properly seated.
- The Compute Module is defective.
- A connected device is injecting stray voltages that prevent the CM5 from starting — try disconnecting the HDMI cable.

1. Disconnect any HDMI displays and restart to rule out stray voltage interference.
2. If the issue persists, open the enclosure and verify the CM5 module is fully seated in its connector — this requires removing the carrier board.

### LEDs stay yellow

**Symptoms:** LEDs progress from red (charging) to yellow (powered on) but never reach green.

The yellow state means the controller has powered the CM5 and is waiting for the daemon to respond. If LEDs stay yellow, either the operating system is not booting or the HALPI daemon is not installed.

1. Check that the boot mode switch is in the "Normal" position — the yellow indicator LED next to the switch lights up when boot mode is set to "Abnormal" (USB boot).
2. Connect a display via HDMI to check for boot errors or a login prompt.
3. Verify the NVMe SSD is properly seated in its M.2 slot.
4. If the OS boots successfully, check that the daemon is installed: `systemctl status halpid`
5. If the daemon is installed but not running, check its logs: `journalctl -u halpid -e`

### System shuts down unexpectedly

**Symptoms:** System powers off without user intervention, even though external power is connected.

1. Check input voltage stability — brief voltage dips below the threshold trigger the blackout timer. Use `halpi status` to monitor `V_in` in real time.
2. Inspect the power cable for loose connections or damaged conductors that could cause intermittent contact.
3. If using NMEA 2000 bus power, verify that the network voltage remains stable under load. Other high-draw devices on the network can cause voltage drops.

## Firmware Update Failed or Rolled Back

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

1. Open the enclosure and check the RS-485 interface LEDs — the RX LED should flash when data is being received.
2. Verify the serial port exists and is accessible:
    ```bash
    ls -l /dev/ttyAMA4
    ```
3. Check wiring polarity — RS-485 uses differential signaling with A/B lines. Swapped A and B connections will prevent communication.

### Ethernet link not established

1. Check the Ethernet cable and RJ45 connector. Try a different cable.
2. Open the enclosure and check the Ethernet LEDs for link status.
3. Verify link status: `ip link show eth0`
4. If the link is up but there's no IP address, check DHCP: `sudo dhclient eth0`
5. For static IP configurations, verify the settings in `/etc/network/interfaces` or NetworkManager.

## Operating System Issues

### Cannot SSH into the device

1. Verify SSH is enabled: `sudo systemctl status ssh`
2. Check network connectivity — can you ping the device?
3. SSH is enabled by default on HaLOS headless images and OpenPlotter. On HaLOS Desktop variants and Raspberry Pi OS, SSH can be enabled via `raspi-config`.

### System runs slowly or freezes

1. Check CPU temperature — extreme ambient temperatures can cause thermal throttling. Use:
    ```bash
    vcgencmd measure_temp
    ```
    Temperatures above 80°C indicate a thermal issue. Try to reduce ambient temperature or improve airflow around the enclosure.

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
| Stuck during startup | Rainbow pattern | CM5 not detected — check module seating and disconnect displays |
| Stays yellow | Solid yellow | OS not booting or daemon not installed |
| Unexpected shutdown | Scrolling green/yellow | Power loss detected — check input power |
| Overvoltage | LED 1 flashing red | Input voltage too high (>32V) |
| Fault | All LEDs blinking red | Hardware fault — contact manufacturer |

!!! quote "Related Information"
    - **LED patterns:** See [Status LED Indicators](./operation.md#status-led-indicators)
    - **Power management:** See [Power Management and Shutdown Procedures](./operation.md#power-management-and-shutdown-procedures)
    - **Daemon management:** See [Software Guide](./software.md#halpi-daemon-halpid)
    - **CAN interface details:** See [Interfaces and Connectivity](./interfaces.md#can-fd-nmea-2000)
    - **RS-485 interface details:** See [Interfaces and Connectivity](./interfaces.md#rs-485-nmea-0183)

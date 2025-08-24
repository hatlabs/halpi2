# Software Guide

## Operating System Images

Hat Labs provides pre-built images for HALPI2, which can be downloaded from
[GitHub](https://github.com/hatlabs/openplotter-halpi/releases). The pre-built
images include the necessary configuration and customizations for the HALPI2
hardware.

All pre-built images have the CAN (NMEA 2000) interface enabled by default, as
network device `can0`. RS-485 (NMEA 0183) is available as `/dev/ttyAMA4`.

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


## Flashing an Operating System Image to SSD

There are two methods available for flashing an operating system image to the HALPI2's NVMe SSD: removing the SSD and using a USB NVMe adapter, or flashing directly on the HALPI2 unit. The USB NVMe adapter method is recommended for convenience and ease of use, as these adapters can be found online at low cost and provide a straightforward flashing process.

### Flashing Using a USB NVMe Adapter

To flash the image using the USB NVMe adapter method, begin by removing the NVMe SSD from the HALPI2 unit following the procedure described in the [Hardware Guide](./hardware.md#replacing-the-nvme-ssd). Next, download a HALPI2-compatible image from the [GitHub openplotter-halpi releases](https://github.com/hatlabs/openplotter-halpi/releases) page, ensuring you select the appropriate image for your intended use.

Insert the SSD into the USB NVMe adapter and connect it to your computer. Use the Raspberry Pi Imager to flash the downloaded image to the NVMe SSD. If you are flashing a Raspberry Pi OS image, you can edit and apply OS customization settings as needed during the flashing process. However, if custom settings are not applied, you will need a USB keyboard and mouse connected to the HALPI2 for the initial setup after installation.

When using the OpenPlotter image, OS customization settings should **not** be applied during the flashing process. Instead, configuration is done after the first boot using the Raspberry Pi and OpenPlotter configuration tools, which provide the appropriate setup interface for the marine-focused environment.

Once the flashing process is complete, unplug the adapter and remove the SSD. Insert the SSD back into the HALPI2 unit following the installation procedure described in the Hardware Guide, then reassemble the enclosure according to the same guide.

### Flashing Directly on the HALPI2

Alternatively, you can flash the operating system image directly on the HALPI2 without removing the SSD. This method follows the standard Compute Module flashing procedure as documented in the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/compute-module.html#flash-compute-module-emmc). Note that the board setup instructions in the Raspberry Pi documentation are for the CM5 IO Board, but the process is similar for the HALPI2.

To set up the HALPI2 for USB flashing, begin by powering off the system completely and opening the enclosure lid following the procedure described in the [Hardware Guide](./hardware.md#enclosure-access). Locate the USB-C connector labeled "USB Boot" to the right of the HAT outline on the carrier board, and switch the adjacent boot mode switch to the "Abnormal" position. An amber LED will light up to indicate that the HALPI2 is in USB boot mode.

Connect a USB cable between your computer and the USB Boot connector on the HALPI2. Power the device back up - it is now ready to receive a custom boot image using the `usbboot` command. Run the `usbboot` command as described in the Raspberry Pi documentation to prepare the device for flashing.

Flash the operating system image using the Raspberry Pi Imager or other compatible flashing software. The HALPI2 will appear as a mass storage device during this process, allowing standard image flashing tools to write directly to the internal NVMe SSD.

After the flashing process is complete, it is essential to toggle the Boot Mode switch back to the "Normal" position to ensure the device will boot normally from the newly flashed image. Disconnect the USB cable and close the enclosure.

## Initial System Configuration

After successfully flashing and booting your HALPI2 for the first time, several configuration steps are required to ensure secure and proper operation of the system.

### OpenPlotter Configuration

When using the OpenPlotter image, the system will boot with default passwords for both the WiFi access point and the default user account. For security reasons, it is imperative that these passwords are changed immediately after the first boot.

The password change process and initial configuration are described in the [Quick Start Guide](../getting-started/quick-start.md#first-boot-configuration).

### Raspberry Pi OS Configuration

If you have chosen to use the standard Raspberry Pi OS instead of OpenPlotter, follow the standard Raspberry Pi setup process that will be presented on first boot. This setup wizard will guide you through creating user accounts, setting passwords, configuring WiFi connections, and enabling essential services like SSH for remote access.

During the initial setup, you may also want to configure timezone settings, keyboard layout, and other regional preferences to match your operating environment. The Raspberry Pi configuration tool (`raspi-config`) provides access to additional system settings that can be adjusted after the initial setup is complete.

## Software Updates

The HALPI2 software and firmware can be updated using the standard Raspberry Pi OS update process, which ensures that all system components remain current with the latest features and security patches. Regular updates are recommended to maintain optimal system performance and security.

### Command Line Updates

The most reliable method for updating the system is through the command line interface. Open a terminal window and execute the following commands to update the system:

```bash
sudo apt update
sudo apt upgrade
```

The first command (`apt update`) refreshes the package database with the latest available versions, while the second command (`apt upgrade`) downloads and installs all available updates. This process will update all installed packages, including the base Raspberry Pi OS, OpenPlotter components, and HALPI2-specific software.

During the update process, you may be prompted to confirm the installation of certain packages or to restart services. It is generally safe to accept these prompts unless you have specific reasons to decline.

### Graphical Updates

For users who prefer a graphical interface, the desktop environment provides visual notification when updates are available. A download icon will appear in the top right corner of the desktop taskbar when updates are ready to be installed. Clicking this icon opens the update manager, which provides a user-friendly interface for reviewing and installing available updates.

## Remote Access

The HALPI2 supports multiple methods for remote access, allowing you to monitor and control the system without requiring physical access to the device. This is particularly valuable for installations where the HALPI2 may be mounted without a display in difficult-to-reach locations.

### SSH (Secure Shell)

SSH provides secure command line access to the HALPI2 system, allowing you to execute commands, transfer files, and perform system administration tasks remotely. SSH is enabled by default on OpenPlotter images and can be enabled during the image flashing process for Raspberry Pi OS. For existing installations, SSH can be activated using the `raspi-config` utility.

To connect via SSH, use an SSH client such as the built-in terminal on macOS and Linux systems, or applications like PuTTY on Windows. The basic connection command is:

```bash
ssh username@halpi2-ip-address
```

SSH connections are encrypted and secure, making them suitable for use over public networks when properly configured with strong authentication. It also requires very little bandwidth, making it ideal for remote access over low-speed and high-latency connections.

### VNC (Virtual Network Computing)

VNC provides remote desktop access to the HALPI2's graphical interface, allowing you to interact with the desktop environment as if you were physically present at the device. VNC comes preinstalled and preconfigured on OpenPlotter images. For Raspberry Pi OS installations, VNC can be enabled using the `raspi-config` configuration tool.

To connect to the HALPI2 desktop remotely, use RealVNC's [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) application, which is available for Windows, macOS, Linux, iOS, and Android devices. VNC works effectively on local networks and offline environments, making it ideal for boat installations where internet connectivity may be limited or unavailable.

For remote access over the internet, VNC requires additional network configuration such as port forwarding or VPN setup, as the protocol does not inherently traverse firewalls and NAT devices.

### Raspberry Pi Connect

Raspberry Pi Connect offers a modern web-based approach to remote desktop access, allowing you to connect to the HALPI2 desktop using just a standard web browser without requiring any additional software installation. This service works through firewall and NAT configurations automatically, making it particularly suitable for remote access over the internet without complex network setup.

Unlike VNC, Raspberry Pi Connect handles the networking complexities automatically, providing seamless access from anywhere with an internet connection. However, it also requires that the HALPI2 itself maintains an active internet connection to function.

## Firmware Updates

The HALPI2 controller firmware can be updated using the standard Raspberry Pi OS update process, which provides a seamless and integrated approach to maintaining the latest firmware versions. Regular firmware updates are important for ensuring optimal performance, accessing new features, and maintaining compatibility with evolving software components.

### Automatic Firmware Updates

Firmware updates are delivered through the standard system update mechanism, Debian packages in an APT repository. To check for and install firmware updates, open a terminal window and execute the following commands:

```bash
sudo apt update
sudo apt upgrade
```

When new HALPI2 firmware is available, it will be automatically downloaded and installed as part of the upgrade process. The system will notify you if firmware updates are included in the available packages.

After completing the firmware package update process, it is essential to properly restart the system to apply the firmware changes. Use the shutdown command to ensure a complete power cycle:

```bash
sudo shutdown -h now
```

**Important:** Simply rebooting the system is not sufficient for firmware updates. A complete shutdown and restart is required because this allows the controller to restart and apply the new firmware. The controller firmware is only updated during the power-on sequence.

### Firmware Safety Features

The HALPI2 includes built-in safety mechanisms to protect against firmware corruption. If the device is restarted again within 30 seconds of applying a firmware update, the system will automatically roll back to the previous firmware version. This feature provides protection against problematic firmware updates that might prevent normal operation.

### Manual Firmware Installation

For advanced users or specific troubleshooting scenarios, firmware can be manually installed using the HALPI command line tool. Firmware files are stored in the `/usr/share/halpi2-firmware/` directory and can be flashed directly using:

```bash
halpi flash <firmware_file>.bin
```

### Disabling Automatic Firmware Updates

Some users may want to disable automatic firmware updates to maintain a specific firmware version. This can be accomplished by editing the HALPI2 configuration file:

```bash
sudo nano /etc/halpid/firmware.conf
```

Locate the `AUTO_FLASH_ON_INSTALL` setting and change it to `no`:

```bash
AUTO_FLASH_ON_INSTALL=no
```

Save the file and exit the editor. This configuration change will prevent the HALPI2 from automatically flashing new firmware during the standard update process, giving you complete control over when firmware updates are applied. You can still manually install firmware updates using the `halpi flash` command when desired.


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

The daemon configuration is stored in `/etc/halpid/halpid.conf`. To edit the configuration, use:

```bash
sudo nano /etc/halpid/halpid.conf
```

Configuration changes require daemon restart:

```bash
sudo systemctl restart halpid
```

### HALPI Command Line Tool (`halpi`)

The `halpi` command provides direct access to controller functions and system status. It communicates with the daemon to execute commands and retrieve information about the HALPI2's operational state, configuration, and hardware parameters.

#### System Status and Monitoring

The primary function of the HALPI command line tool is to provide comprehensive system status information. This includes hardware parameters, operational state, and real-time monitoring data.

**Display System Status:**
```bash
# Display comprehensive system status
halpi status
```

This command provides a complete overview of the HALPI2's current operational state, including voltage levels, current consumption, temperature readings, and controller status:

```
$ halpi status
 hardware_version               N/A
 firmware_version             3.1.0
 state              OperationalCoOp
 5v_output_enabled             True
 watchdog_enabled              True
 watchdog_timeout              10.0  s
 watchdog_elapsed               0.0  s
 V_in                          12.2  V
 I_in                          0.38  A
 V_supercap                   10.27  V
 T_mcu                         43.3  °C
 T_pcb                         35.2  °C
```

If you only want to monitor a specific value, it can be retrieved as follows:

```bash
# Show controller firmware version
halpi get firmware_version
```

For scripting purposes, it is better to use the REST API instead, as described in the [REST API Access](#rest-api-access) section.

#### Configuration Management

The HALPI command line tool provides comprehensive configuration management capabilities, allowing you to view current settings and modify operational parameters.

**View Current Configuration:**
```bash
# Show current configuration
halpi config
```

This displays all configurable parameters and their current values:

```
$ halpi config
 Key                       Value
 watchdog_timeout           10.0
 power_on_threshold          8.0
 solo_power_off_threshold    5.5
 led_brightness               40
 auto_restart               True
 solo_depleting_timeout      5.0
```

#### LED Control

One of the most commonly adjusted settings is the LED brightness, which can be customized for different operating environments and user preferences.

**LED Brightness Management:**
```bash
# Get current LED brightness (0-255)
halpi config get led_brightness

# Set LED brightness to low level for night operation
halpi config set led_brightness 40

# Set moderate brightness
halpi config set led_brightness 64

# Turn LEDs off completely
halpi config set led_brightness 0

# Maximum brightness for daylight operation
halpi config set led_brightness 255
```

The LED brightness accepts values from 0 (completely off) to 255 (maximum brightness), allowing fine-tuned control over the front panel LED indicators.

#### Power Management

The HALPI command line tool provides essential power management functions for safe system operation.

**System Control Commands:**
```bash
# Initiate graceful shutdown
halpi shutdown

# Enter standby mode (when available)
halpi standby
```

The shutdown command ensures that the system powers down safely, allowing the operating system to close applications and unmount filesystems properly before the controller cuts power.

#### REST API Access

For advanced users and custom applications, the HALPI daemon also provides a REST API interface accessible via Unix domain socket. This allows for faster programmatic access to system data:

**REST API Examples:**
```bash
# Get all system values
curl --unix-socket /var/run/halpid.sock http://localhost/values

# Get all configuration parameters
curl --unix-socket /var/run/halpid.sock http://localhost/config

# Get individual parameter values
curl --unix-socket /var/run/halpid.sock http://localhost/values/V_supercap
```

The REST API is particularly useful for monitoring applications, data logging systems, or integration with other software that needs real-time access to HALPI2 status information.

Full REST API documentation is available in the [Software Development: Daemon](../software-development/daemon.md) chapter.

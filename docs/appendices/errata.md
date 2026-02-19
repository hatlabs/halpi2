# Errata

Known hardware issues for different HALPI2 versions are listed on this page.

## Version 0.4.0 Devices

#### Initial Current Spike on Power-Up

When the device is powered up with completely depleted super-capacitors, the initial inrush current can reach 1.1A for a short moment. This makes the device nominally non-compliant with the NMEA 2000 requirement of maximum 1A input current.

The higher than specified initial current is due to an obscure interaction between the RP2040 microcontroller analog inputs and the current limiting circuitry.

#### Copper Fill Under Mounting Ledges

A 3.3V power plane on the bottom layer of the PCB extends above the mounting ledges. In some enclosures, the mounting ledges have remnants of sharp "flashes" (leftover bits of aluminium from the casting process). If the flash edges penetrate the PCB solder mask, they can create a short circuit to the 3.3V plane, preventing the device from being powered up.

The issue can be fixed by applying electrical PVC tape on top of the mounting ledges.

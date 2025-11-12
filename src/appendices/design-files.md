# Design Files and Schematics

This page provides the schematics and mechanical design files for HALPI2.

The electrical design of HALPI2 is done in KiCad. The design files are available in the [GitHub repository](https://github.com/hatlabs/HALPI2-hardware). Each released version has a corresponding tag in the repository.

The schematics are provided for convenience as PDF files below. The PCB layout designs are only available in the GitHub repository.

Mechanical design files are initially provided for the enclosure only. The design has been done with Autocad Fusion but the STEP format export files are readable by most CAD software.

### Version 0.6.0

The third production release of HALPI2 with more minor fixes to the carrier board. The board features remain the same as in version 0.5.0.

Changes include:
- 3.3V rail output is now toggled by the controller instead of being always on
- Add test points for improved production testing
- Re-route HDMI, MIPI and USB3 interfaces for better signal integrity
- Onboard FFC connectors are now horizontal
- Improve 10V buck converter stability - no longer whines on any circumstances
- Reimplement supercap balancing circuit with a single 4-unit opamp
- Some component footprints have been changed to improve availability

#### Design files

- KiCad design files: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.6.0.zip)
- Schematic PDF: [HALPI2-schematic_v0.6.0.pdf](./HALPI2-schematic_v0.6.0.pdf)


### Version 0.5.0

The second production release of HALPI2 with minor fixes to the carrier board. The board functionality remains the same as in version 0.4.0.

Changes include:
- Fixed minor silkscreen bugs
- Removed 3.3V copper pours from bottom layer next to mounting structures
- Add solder nuts for easier mounting of HATs
- Add solder nuts for more secure mounting of the Compute Module
- Revert jumper headers back to THT for better mechanical strength
- Add a dedicated +5V power LED
- Relax supercap balancing
- Reorganize jumper headers for better usability

#### Design Files

- KiCad design files: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.5.0.zip)
- Schematic PDF: [HALPI2-schematic_v0.5.0.pdf](./HALPI2-schematic_v0.5.0.pdf)
- Enclosure 3D model: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step) (same as in version 0.4.0)

### Version 0.4.0

This is the first public release of HALPI2.

#### Design Files

- KiCad design files: [https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip](https://github.com/hatlabs/HALPI2-hardware/archive/refs/tags/v0.4.0.zip)
- Schematic PDF: [HALPI2-schematic_v0.4.0.pdf](./HALPI2-schematic_v0.4.0.pdf)
- Enclosure 3D model: [HALPI2-enclosure_v0.4.0.step](./HALPI2-enclosure_v0.4.0.step)

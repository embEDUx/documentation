# Bootloader Design
**(work in progress)**

## Bootloader Choice
As some platforms at the HTWG already run **Das U-Boot** as bootloader, a soft
requirement is **U-Boot**. However the software solution must not be restricted
to a specific **U-Boot** version. **U-Boot** also has TFTP/BootP support in
general, but it has to be evaluated if it's supported for all required
platforms.

## Build Process
To retrieve the **U-Boot** sources, the following possibilities exist

* User has to provide sources within the **U-Boot** repository
* Download sources from official website during build process

## BUild Steps
The build process must include the following steps.

1. Retrieve the build specifications from the **U-Boot**-repository
1. Retrieve the **U-Boot** sources
1. (Cross-)Compile **U-Boot** for target architecture with config provided by
   the specifications
1. Create an archive from the necessary files.

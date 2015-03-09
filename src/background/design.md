# Design
**(work in progress)**

The design for the **embEDUx** system can now be derived from the given
[requirements](requirements.md). 

Without specifying any details, the following software must be handled by the
system.:

* **Linux** Kernel
* Bootloader
* RootFS containing the system and user-space application

These parts will be referred as ***products*** within this documentation. 

# Product specification

## Bootloader
As some platforms at the HTWG are already running with **Das U-Boot** as
bootloader, a soft requirement is **U-Boot**. However the software solution must
not be restricted to a specific **U-Boot** version.

## Kernel
No specific **Linux** kernel version is required and the software solution must
not be restricted to a specific kernel version.

## RootFS 
The software solution must not restrict the user in his choice of available
applications or libraries, although the common distribution restrictions (eg.
Application is not available/updated in package manager) can still apply.

## Portability 
Software solutions must be easy to setup on various architectures. 

## Extensibility 
Adding support for additional hardware platforms must be simple. 

## Other 
Platform specific source code must be avoided as far as possible. 


# Evaluate Suggestion: Yocto Project
- evaluate: => not for our purpose

# DIY

## Products

### U-Boot
- realize we need files which better not be assigned to the product
### Kernel
- realize we need files which better not be assigned to the product

### Miscellaneous Files
=> directly derived from U-Boot/Kernel 

### Toolchain

### RootFS

## How can we configure and build the products automatically (different platforms/architectures)
=> Design Continuous Integration
=> call user build script within a repository
=> cross compilation for kernel/uboot
=> find solution for rootfs

## How can we setup the CI?
=> ansible

## What does the build script need to do for the different products

### U-Boot
- download sources
- apply config
- build
- prepare output for boot partition 

### Linux
- download sources
- apply gentoo patches
- apply user patches
- apply config
- build
- prepare output for boot partition
- prepare output for root partition

### Misc
- contains files for root / boot
- prepare output for boot partition
- prepare output for root partition

### Toolchain
- apply config
- build
- prepare output

### RootFS
- config 
- prepare output for root partition

---



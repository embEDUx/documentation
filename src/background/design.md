# Design
From the given [Requirements](requirements.md) the key elements of the software
solution can already be defined.

The solution has to provide a **Linux** kernel, a **U-Boot** and a RootFS, which
will be referred as *products* within this documentation. 


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



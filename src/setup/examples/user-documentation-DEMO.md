# User Documentation Demo
This is the User Documentation demonstration for the **Github** Repositories.
Others may use it as an orientation and overview of the contents they have to
put in their User Documentation.

## Repositories
Product | Repository URL
--- | ---
U-Boot | [https://github.com/embEDUx/uboot-specs.git](https://github.com/embEDUx/uboot-specs.git)
Linux | [https://github.com/embEDUx/linux-specs.git](https://github.com/embEDUx/linux-specs.git)
RootFS | [https://github.com/embEDUx/rootfs-specs.git](https://github.com/embEDUx/rootfs-specs.git)
Miscellaneous files | [https://github.com/embEDUx/misc-specs.git](https://github.com/embEDUx/misc-specs.git)
Toolchains | [https://github.com/embEDUx/toolchain-specs.git](https://github.com/embEDUx/toolchain-specs.git)

#### Permissions
If you need permissions to these repositories, please contact your
Administrator.


## Web-Interfaces
Server-Name | URL
--- | ---
moe | http://moe.in.htwg-konstanz.de:8010

## Product Download URLs
Product | URL
--- | ---
U-Boot | [http://moe.in.htwg-konstanz.de:8010/uboot/](http://moe.in.htwg-konstanz.de:8010/uboot/)
Linux | [http://moe.in.htwg-konstanz.de:8010/linux/](http://moe.in.htwg-konstanz.de:8010/linux/)
RootFS | [http://moe.in.htwg-konstanz.de:8010/rootfs/](http://moe.in.htwg-konstanz.de:8010/rootfs/)
Miscellaneous files | [http://moe.in.htwg-konstanz.de:8010/misc/](http://moe.in.htwg-konstanz.de:8010/misc/)
Toolchains | [http://moe.in.htwg-konstanz.de:8010/toolchains/](http://moe.in.htwg-konstanz.de:8010/toolchains/)

## Platform Strings
Platform | Platform-String | RootFS-String | Toolchain-String (target\_arch)
--- | --- | --- | ---
Raspberry Pi | raspberry-pi | armv6j\_hardfp | armv6j
Banana Pi | banana-pi | armv7a\_hardfp | armv7a
Utilite Pro | utilite-pro | armv7a\_hardfp | armv7a
Qemu ARM | qemu-virt-arm | armv7a\_hardfp | armv7a
Beaglebone Black | beaglebone-black | armv7a\_hardfp | armv7a

## Build Commands
Product | Buildcommands
--- | --- 
Linux | './build'
Uboot | './build'
Misc | './build'
Toolchain | './build'
RootFS | *special ansible buildroutine: TODO LINK*

## Output Directories
Product | Output Folder
--- | --- 
Linux | output
Uboot | output 
Misc | output
Toolchain | output
RootFS | *special ansible buildroutine: TODO LINK*

## Output File-Scheme
Product / Description | Nr of Files / File-Scheme
--- | ---
**Linux** | 3
Linux Blob | < branch-name \>\_< date&time \>\_< commit-hash \>\_boot.tar.bz2
Modules+Sources | < branch-name \>\_< date&time \>\_< commit-hash \>\_root.tar.bz2
Linux config | < branch-name \>\_< date&time \>\_< commit-hash \>\_config.tar.bz2
**Uboot** | 1
Uboot Blob | < branch-name \>\_< date&time \>\_< commit-hash \>\_uboot.tar.bz2
**Misc** | 2
Additional Boot Files | < branch-name \>\_< date&time \>\_< commit-hash \>\_boot.tar.bz2
Additonal Root Files| < branch-name \>\_< date&time \>\_< commit-hash \>\_root.tar.bz2
**Toolchain** | 1
Toolchain | < branch-name \>\_< date&time \>\_< commit-hash \>\_toolchain.tar.bz2
**RootFS** | 2
Rootfs Archive | < branch-name \>\_< date&time \>\_< commit-hash \>\_rootfs.tar.bz2
Portage Snapshot | < branch-name \>\_< date&time \>\_< commit-hash \>\_portage.tar.bz2

#### Variable Descriptions
Variable | Note
--- | ---
branch-name | The branch that triggered the build
date&time | YYYYMMDDhhmmss
commit-hash | Short version of the hash for the commit which triggered the build

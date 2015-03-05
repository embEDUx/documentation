
## Repositories
Component | Repository URL
--- | ---
U-Boot | https://apu.in.htwg-konstanz.de/labworks-embEDUx/uboot.git
Linux | https://apu.in.htwg-konstanz.de/labworks-embEDUx/linux.git
RootFS | https://apu.in.htwg-konstanz.de/labworks-embEDUx/rootfs.git
Miscellaneous files | https://apu.in.htwg-konstanz.de/labworks-embEDUx/misc.git

### Permissions
If you need permissions to these repositories, please contact your
Administrator.

## Buildmaster

### Web-Interfaces
Server-Name | URL
--- | ---
moe | http://moe.in.htwg-konstanz.de:8010

### Component Download URLs
Component | URL
--- | ---
U-Boot | http://moe.in.htwg-konstanz.de:8010/uboot/
Linux | http://moe.in.htwg-konstanz.de:8010/linux/
RootFS | http://moe.in.htwg-konstanz.de:8010/rootfs/
Miscellaneous files | http://moe.in.htwg-konstanz.de:8010/misc/

### Platform Strings
Platform | Platform-String | RootFS-String | Toolchain-Strings (target\_arch)
--- | --- | --- | ---
Raspberry Pi | raspberry-pi | armv6j\_hardfp | armv6j
Banana Pi | banana-pi | armv7a\_hardfp | armv7a
Utilite Pro | utilite-pro | armv7a\_hardfp | armv7a
Qemu ARM | qemu-virt-arm | armv7a\_hardfp | armv7a
Beaglebone Black | beaglebone-black | armv7a\_hardfp | armv7a

### Build Commands
Builders | Buildcommands
--- | --- 
Linux | './build'
Uboot | './build'
Misc | './build'
Toolchain | './build'
RootFS | *special ansible buildroutine: TODO LINK*

### Output Directories
Builders | Buildcommands
--- | --- 
Linux | output
Uboot | output 
Misc | output
Toolchain | output
RootFS | *special ansible buildroutine: TODO LINK*

### Output File-Scheme
Builder | File-Scheme
--- | --- 
Linux | < branch-name \>\_< date&time \>\_< commit-hash \>\_< destination \>.tar.bz2
Linux | < branch-name \>\_< date&time \>\_< commit-hash \>\_config.tar.bz2
Uboot | < branch-name \>\_< date&time \>\_< commit-hash \>\_uboot.tar.bz2
Misc | < branch-name \>\_< date&time \>\_< commit-hash \>\_< destination \>.tar.bz2
Toolchain | < branch-name \>\_< date&time \>\_< commit-hash \>\_toolchain.tar.bz2
Rootfs | < branch-name \>\_< date&time \>\_< commit-hash \>\_rootfs.tar.bz2

Variable | Note
--- | ---
branch-name | The branch that triggered the build
date&time | YYYYMMDDhhmmss
commit-hash | Short version of the hash for the commit which triggered the build
destination | 'boot' or 'root' partition

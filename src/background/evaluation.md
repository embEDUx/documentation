# Evaluation

## Comparison With Similar Projects
- | Buildroot | Yocto
--- | --- | ---
Setup | `git clone git://git.buildroot.net/buildroot` | `git clone -b dizzy git://git.yoctoproject.org/poky.git`
Configuration | `make menuconfig` | Configuration is happening in conf files, although there is also a GUI 
Output | Bootloader, Kernel, RootFS, Toolchain | SD Card Image
Platform Support | - | Common platforms are supported or available through so called *Board Support Packages (BSP)*, otherwise manual configuration can be done
Software Support | - | Common software is available, otherwise can be added by creating own recipes

### Conclusion:
As we want to have a highly dynamic system, where we still offer up-to date
products, non of the aforementioned projects offer a satisfying solution.
Therefore developing our own projects is necessary.


## Toolchain
Toolchains built with buildroot have absolute symbolic links compiled within the
binaries.  As we want to have a portable toolchain, this fact disqualifies
buildroot for our needs. Fortunately, Crosstool-NG offers the possibility to
build static toolchains. Even toolchains, that are built on host with
architecture X, compiled for architecture Y, which cross-compile for
architecture Z are possible with Crosstool-NG. These kind of toolchains are
called *canadian* toolchain.

## RootFS

## Buildserver

## How can we configure and build the products automatically (different platforms/architectures)
* Design Continuous Integration
* call user build script within a repository
* cross compilation for kernel/uboot
* find solution for rootfs

## How can we setup the CI?
* ansible

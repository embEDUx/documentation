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

## Bootloader
Different platforms use the same source code, when the same version of
**U-Boot** should be build. This also means storing the source code within the
**U-Boot** repository within each *branch* will lead to a huge overhead of
source code file within the repository.

Another option would be to download the source code during build by specifying
the whole build process within a build script, which will be executed by the
build server. With this solution only the required build script will be
redundant within the **U-Boot** repository.

The final solution is to not just add *branches* for each platform and
**U-Boot** version, but also add a source code branch for each **U-Boot**
version. This branch contains a script for downloading the source code of that
certain **U-Boot** version. All the other platform branches can execute that
script and retrieve the source code at runtime.

## Linux Kernel
Due to keeping the possibility to build the kernel locally, emerging the kernel
sources with OS dependent tools (e.g. emerge) is not viable. Also keeping the
sources within the **Linux** repository, will as already mentioned in the
bootloader chapter, lead to a lot of redundancy when different platforms use the
same sources. Therefore a promising solution is to add for each **Linux** kernel
version, which should be build, a branch that contains a script to download the
sources at runtime. The other branches for each platform can then execute that
script and retrieve the sources at runtime.

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

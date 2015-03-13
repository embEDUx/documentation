# Implementation for building Linux 


## Repository
For each platform the **Linux** repository will have at least two branches,
however the version\_generic branches will only exist one time per version.

![Repository](usage/linux/img/example_linux_repository.png)

### version\_generic
This branch exists exactly one time per **Linux** version. It contains the
script, that downloads the sources for the version it is designed for. For
obliterating the redundancy throughout the different platforms, it also
implements the whole build process.

1. Download sources
1. Download **Gentoo** patches
1. Apply **Gentoo** patches
1. Apply User patches
1. Copy config into source directory 
1. Build linux
1. Build modules
1. Provide two output archives
    * Kernel and DTB for boot partition
    * Modules and sources for root partition

### version\_platform
This branch exists for each platform as many times as different version of
**Linux** should be built. It contains a build script, which will do the
following: 

1. Checkout the version\_generic branch for the version it is defined for
1. Set necessary parameter e.g. configration
1. Execute the script from the version\_generic branch

## Build Script
For simplicity bash is used for the script language. As an example the two
scripts, which were implemented and uses throughout the whole development and
test process are provided:

* [version\_generic](usage/linux/default/generic_build)
* [version\_platform](usage/linux/default/platform_build)

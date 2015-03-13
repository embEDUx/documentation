# Implementation for building U-Boot


## Repository
For each platform the **U-Boot** repository will have at least two branches,
however the verion\_generic branches will only exist one time per version.

![Repository](usage/uboot/img/example_uboot_repository.png)

### version\_generic
This branch exists exactly one time per **U-Boot** version. It contains the
script, that downloads the sources for the version it is designed for. For
obliterating the redundancy throughout the different platforms, it also
implements the whole build process.

1. Download sources
1. Apply configuration
1. Build images
1. Provide Output in archive

### version\_platform
This branch exists for each platform as many times as different version of
**U-Boot** should be built. It contains a build script, which will do the
following: 

1. Checkout the version\_generic branch for the version it is defined for
1. Set necessary parameter e.g. configuration
1. Execute the script from the version\_generic branch

## Build Script
For simplicity bash is used for the script language. As an example the two
scripts, which were implemented and uses throughout the whole development and
test process are provided:

* [version\_generic](usage/uboot/default/generic_build)
* [version\_platform](usage/uboot/default/platform_build)

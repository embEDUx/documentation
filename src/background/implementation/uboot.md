# Implementation for building U-Boot
The [design](../design/bootloader.md) and the
[evaluation](../evaluation/uboot.md) result in the following implementation.

## Repository
The repository is called *uboot-specs*. Each platform/version combination gets
its own branch, which will be referred as *version\_platform* branch. Each
version has also one branch, which will be referred as *version\_generic*
branch. 

[![Repository](usage/uboot/img/example_uboot_repository.png)](usage/uboot/img/example_uboot_repository.png)

**Important**: Each *version\_platform* branch depends on a *version\_generic*
branch.

### version\_generic
This branch exists exactly one time per **U-Boot** version. It contains the
script, that downloads the sources for the version it is designed for. For
obliterating the redundancy throughout the different platforms, it also
implements the whole build process.

#### Build steps
1. Download sources
1. Build image
1. Provide Output in archive

#### Build script
The following build script reflects the build steps.

* [version\_generic](usage/uboot/default/generic_build)

### version\_platform
This branch exists for each platform as many times as different version of
**U-Boot** should be built. It contains a build script, which will do the
following: 

#### Build steps
1. Checkout the *version\_generic* branch for the version which should be build
1. Set necessary parameter e.g. configuration
1. Execute the script from the *version\_generic branch*

#### Build script
The following build script reflects the build steps.

* [version\_platform](usage/uboot/default/platform_build)


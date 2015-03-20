# Bootloader Design
With having to support a wide variety of [platforms](../requirements.md), there
is no other option, then using **Das U-Boot** as bootloader. A positive
side-effect of this choice is the fact, that most of the platforms at the HTWG
Konstanz already run **Das U-Boot** as bootloader and therefore the
configuration for those platforms exist.
 
## Sources 
As directly derived from the [requirements](../requirements.md) the mainline
sources of **U-Boot** must be used. However there can't be any restriction to a
specific version. To be able to run any platform with the mainline sources of
**U-Boot** the possibility of applying user patches during build has to be
considered.
 
## Repository
The user specification, such as configuration of **U-Boot** and user patches for
the mainline sources should be stored within a repository. Therefore each platform /
version combination needs to get its own branch. E.g. two branches have to
exist if **U-Boot** version 1.0 and 1.2 should be build for platform A.

## Cross Target Support
As **U-Boot** has to be build for different architectures [cross
target support](../design.md#cross-target-support) needs to be considered. 

## Build Process
As mainline sources have to be used, those sources need to be retrieved somehow
before the build process. Two possible options to retrieve the sources are:

* Yocto Project
* Buildroot
* The User has to provide sources within the repository
* The sources have to be downloaded before each build process at runtime

## Build Steps
Building **U-Boot** has to include the following steps:

1. Retrieve the build specifications from the **U-Boot**-repository
1. Retrieve the **U-Boot** sources
1. Apply required patches
1. (Cross-)Compile **U-Boot** for target architecture with config provided by
   the specifications
2. Create an archive from the necessary files.


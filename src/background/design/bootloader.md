# Bootloader Design
With having to support a wide variety of [platforms](../requirements.md), there
is no other option, then using **Das U-Boot** as bootloader. A positive
side-effect of this choice is the fact, that most of the platforms at the HTWG
Konstanz already run **Das U-Boot** as bootloader and therefore the
configuration for those platforms exist.
 
## Sources 
As directly derived from the [requirements](../requirements.md) the mainline
sources of **U-Boot** must be used. However there can't be any restriction to a
specify version. To be able to run any platform with the mainline sources of
**U-Boot** the possibility of applying user patches during build has to be
considered.
 
## Repository
A repository for each platform is needed. It might also be necessary to build
different **U-Boot** versions for the same platform. Therefore one repository
has to exist for each platform for the desired **U-Boot** version. That means
two repositories have to exist **U-Boot** version 1.0 and 1.2 should be build
for platform A. A possible solution might be abusing the branch system of
  **Git**.

## Build Process
As mainline sources have to be used, those sources need to be retrieved somehow
before the build process. Also the user has to provide the configuration or at
least define the config, that should be applied for the build process. Two
possible options to retrieve the sources are:

* The User has to provide sources within the repository
* The sources are downloaded before each build process

## Build Steps
Building **U-Boot** has to include the following steps:

1. Retrieve the build specifications from the **U-Boot**-repository
1. Retrieve the **U-Boot** sources
1. Apply required patches
1. (Cross-)Compile **U-Boot** for target architecture with config provided by
   the specifications
1. Create an archive from the necessary files.



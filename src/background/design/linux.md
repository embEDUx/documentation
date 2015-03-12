# Linux Design
From the [requirements](../requirements.md) we can derive the following design
criteria. 

## Sources 
The mainline sources of **Linux** must be used. However there can't be any
restriction to a specify version. To be able to run any platform with the
mainline sources of **Linux** the possibility of applying user patches during
build has to be considered.

## Repository
A repository for each platform is needed. It might also be necessary to build
different **Linux** versions for the same platform. Therefore one repository
has to exist for each platform for the desired **Linux** version. That means
two repositories have to exist if **Linux** version 1.0 and 1.2 should be build
for platform A. A possible solution might be abusing the branch system of
  **Git**.

## Build Process
As mainline sources have to be used, those sources need to be retrieved somehow
before the build process. Also the user has to provide the configuration or at
least define the config, that should be applied for the build process. Two
possible options to retrieve the sources are:

* The User has to provide sources within the repository
* The sources are downloaded before each build process
* Gentoo sources ebuild from with **Gentoo** is used

## Build Steps
The build process must include the following steps.

1. Retrieve the build specifications from the **Linux**-repository
1. Retrieve **Linux** kernel sources
1. Apply required patches provided from the **Linux**-repository
1. (Cross-)Compile kernel for target architecture with kernel config provided by
   the specifications
1. Create two archives from the necessary files.
    * destination boot partition (kernel image, device tree blob)
    * destination root partition (e.g. modules)


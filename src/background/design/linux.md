# Linux Design
From the [requirements](../requirements.md) we can derive the following design
criteria. 

## Sources 
As directly derived from the [requirements](../requirements.md) the mainline
sources of **Linux** must be used. However there can't be any restriction to a
specify version. To be able to run any platform with the mainline sources of
**Linux** the possibility of applying user patches during build has to be
considered.

## Repository
The user specification, such as configuration of **Linux** and potential user
patches for the mainline sources should be stored together in a repository.
Therefore each platform / version combination needs to have its own branch. E.g.
if **Linux** version 1.0 and 1.2 should be build for platform A, two branches
  have to exist.

## Cross Target Support
As **Linux** has to be build for different architectures [cross target
support](../design.md#cross-target-support) needs to be considered. 

## Build Process
As mainline sources have to be used, those sources need to be retrieved somehow
before the build process. Two possible options to retrieve the sources are:

* The User has to provide sources within the repository
* The sources have to be downloaded before each build process
* Gentoo sources ebuild together with **Gentoo** has to be used

## Build Steps
The build process must include the following steps.

1. Retrieve the build specifications from the repository
1. Retrieve kernel sources
1. Apply provided patches
1. (Cross-)Compile kernel for target architecture with kernel config provided by
   the specifications
1. Create two archives from the necessary files.
    * Files for the boot partition (kernel image, device tree blob)
    * Files for the root partition (e.g. modules)


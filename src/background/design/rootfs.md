# RootFS Design
**(work in progress)**

According to the requirements it needs to be possible to install various
packages in the RootFS. Combined with the requirement for simple extension, the
only sane design choice is to include a package management system. Basically,
the following two types of package management systems exist.

## Package Management System
* Binary Based Package Installation

    Binary packages are built and hosted by a distributor. The distributor
    choses which packages are built, for which platform these packages are
    built and naturally the configuration and compiler flags that are chosen.
    Binary packages install fast, and are only limitted by the download and disk
    speed.

* Source Based Package Installation

    Building packages from source gives the highest possibility of being able to
    install the package on a specific platforms. Source files are downloaded to
    the local computer and are then compiled to binary files, which are
    installed into the local system. Configuration and compiler flags can be
    adjusted locally. Source packages install slowly, since they are compiled
    locally which might be very slow depending on the available CPU and RAM
    resources.

For the **embEDUx** use-case, availability and compatibility are preferred over
installation speed. This leads to the choice of a source based package
installation based on the above comparison.

The choice of the source package management system should be evaluated
carefully. Candidates shall be

* Yocto Project
* Buildroot
* Gentoo crossdev
* Gentoo catalyst

## List of Packages
For each build, a list of desired packages must be provided.

## Configuration and compiler flags
The fact that a source based package
management system will be chosen, should allow specification on configuration
and compiler flags during the build process. These options shall be provided
together with the package lists.

## Cross Target Support
Even though the number of ARM-systems is growing, most Desktops and Servers are
still running on x86-based architectures. In order to build the products for the
platforms used within the lab-courses, it is necessary to either use
cross-toolchains or emulators. The following candidates for the different
techniques need to be evaluated for every of the embEDUx products.

* Cross-Compilation
    * Gentoo crossdev
    * YOCTO
* Emulation
    * Qemu user emulation
    * Qemu system emulation


## Build Steps
The build process must include the following steps.

1. Retrieve the build specifications from the RootFS-repository
1. Parse the package list provided by the user
1. Translate the package list into a format that is accepted by the package
   manager
1. Cleanup the build files
1. Create an archive from the RootFS

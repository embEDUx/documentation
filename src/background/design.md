# Design
**(work in progress)**

The design for the **embEDUx** system can now be derived from the given
[requirements](requirements.md). The requirements include a wide variety of
configuration options, which in turn requires a configurable build system.
The build system must be able to build the following software according to a
provided configuration:

* Linux Kernel
* Bootloader
* RootFS containing the system and user-space application

These parts will be referred as ***products*** within the further documentation.

# Comparison With Similar Projects
At the time of designing **embEDUx**, there are several open source projects
that need to be considered as a base for **embEDUx**.
These projects will be examined throughout the design in the different
sections.

* Embedian - unfortunately, the project was officially retired as of July 2014 
* Buildroot
* YOCTO Project

# Product-Specification Storage Units
It must be possible to build the products independently from each other.
Therefore, each product should be managed in a separate storage unit which will be
referred as a *repository* from this point on.

## Repository Format
Configuration files and specification files are most certainly provided by the
user as text files. For this purpose, a version control system should be used in
order to have a history of build changes and allow easier handling of the
repositories.

# Product Requirement Analysis

## Bootloader
As some platforms at the HTWG already run **Das U-Boot** as bootloader, a soft
requirement is **U-Boot**. However the software solution must not be restricted
to a specific **U-Boot** version. **U-Boot** also has TFTP/BootP support in
general, but it has to be evaluated if it's supported for all required
platforms.

### Build process
The build process must include the following steps.

1. Retrieve the build specifications from the RootFS-repository
TODO Lars

## Linux-Kernel
No specific **Linux** kernel version is required and the software solution must
not be restricted to a specific kernel version. It would be reasonable to have
the same kernel sources for all of the platforms, and only provide platform
specific patches to the common base where necessary. In addition to these
patches, it should be able to provide a specific configuration for a build.

## Toolchains for Building Kernel and Bootloader
The Linux-Kernel and the Bootloader must be compiled from their sources,
otherwise the user is not able to provide the configuration for these.
In oder to build these products for the different platforms it will require a
Toolchain with the respective build targets. The toolchain should also be user
configurable, which leaves the following projects for the evaluation of
toolchain creation.

* Crosstool-NG
* Buildroot

### Build process
The build process must include the following steps.

1. Retrieve the build specifications from the RootFS-repository
TODO Lars

## RootFS 
The requirements include the need for various packages. Combined with the
requirement for simple extension, the only sane design choice is to include a
package management system. 
There are basically two types of package management
systems.
### Package Management System
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
* Gentoo Portage
* Buildroot
* YOCTO

### Package Lists
The list and configuration of the desired packages
must be configurable for each build.

### Build process
The software that is used to assemble the RootFS according to the provided
package list must be chosen wisely. There are many projects to consider for this
part. The following of them will be evaluated:
- YOCTO
- Buildroot
- Gentoo crossdev
- cross-boss
- Gentoo catalyst

The main evaluation criteria is cross-platform support.

#### Steps
The build process must include the following steps.

1. Retrieve the build specifications from the RootFS-repository
1. Parse the package list provided by the user
1. Translate the package list into a format that is accepted by the package
   manager
1. Cleanup the build files
1. Create an archive from the RootFS

# Design Decisions


## Portability 
In order to have a portable build system, all components should live and run in
systems that are separated from the buildserver's host system. Possible
technologies for this are either Virtual Machines or Linux Containers.

### Virtualization and Container Technologies
* Virtual Machines are completely abstracted from the host system's hardware.
  They run on a so-called Hypervisor, which simulates a complete machine for the
  target system. The target system runs it's own kernel, and needs to boot and
  initialize an Operating System from scratch. Security is considered very high,
  since the Hypervisor has full control over soft- and hardware-resources that
  are passed to the guest system.   The architecture of an operating system
  inside a virtual machine can be completely different to the host architecture,
  and thus is highly portable.  Depending on available acceleration
  technologies, the performance of the virtual CPU, RAM and disk can suffer
  significantly.

* Linux Containers utilize a feature in recent Linux Kernels which allow
  separating processes from each other. This includes the separation of host and
  contained processes, as well as different contained processes from each other.
  These contained processes can be an initialization processes to boot a
  different Linux System on the running host Linux kernel, or simply any other
  application available. Recently there has been a lot of development and
  activity on Linux Containers in the community, namely because of a software
  called Docker.  Security is highly dependent on the implementation of the
  process separating that happens in the host kernel.   The host kernel must
  obviously be able to run the contained application.  Therefore, the
  application must either be in the host's native or compatible executable
  format, or the system needs an emulator to run the foreign architecture. The
  performance for contained processes does not differ significantly compared to
  a regular running process. This is not entirely true for executables that
  require emulation because the CPU instructions must be translated before they
  can be run.

In favor of speed (see [Comparison of VM and Linux
Containers](http://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf),)
container technologies should be chosen as the base for the buildsystem. In
environments where security is a high requirement, the containers can live
inside a virtual machine, but that is beyond the design for the buildsystem
itself.

### Split Functionality Into Containers
Containers are relatively cheap entities for the system. This allows the
buildsystem to be split into several containers for the different parts of the
buildsystem.

### Container Management Software
The choice of the container management software still needs to be evaluated, but in favor
of popularity Docker should be the main candidate.


## Setup
The buildserver will undoubtedly be a complex structure of software components.
To make the setup as easy as possible it should be automated as far as possible.

### Setup Parameters
Setup parameters are essential to the configuration of the buildserver.

* Buildserver Target Machine

    The target machine shall by default run all containers that belong to the
    buildsystem

* Target Platform and Architectures
    
    The platform names and their corresponding architecture.
    The architectures will be supported as build targets. 

### Automation
Any scripting language can be used and there's no chosen preference as of this
point.


## Maintenance

### Extensibility 
Adding support for additional hardware platforms must be simple. 

## Other 
Platform specific source code must be avoided as far as possible. 


# Evaluate Suggestion: Yocto Project
- evaluate: => not for our purpose

# DIY

## Products

### U-Boot
- realize we need files which better not be assigned to the product
### Kernel
- realize we need files which better not be assigned to the product

### Miscellaneous Files
=> directly derived from U-Boot/Kernel 

### Toolchain 
### RootFS

## How can we configure and build the products automatically (different platforms/architectures)
=> Design Continuous Integration
=> call user build script within a repository
=> cross compilation for kernel/uboot
=> find solution for rootfs

## How can we setup the CI?
=> ansible

## What does the build script need to do for the different products

### U-Boot
- download sources
- apply config
- build
- prepare output for boot partition 

### Linux
- download sources
- apply gentoo patches
- apply user patches
- apply config
- build
- prepare output for boot partition
- prepare output for root partition

### Misc
- contains files for root / boot
- prepare output for boot partition
- prepare output for root partition

### Toolchain
- apply config
- build
- prepare output

### RootFS
- config 
- prepare output for root partition

---



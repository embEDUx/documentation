# Design
**(work in progress)**

The design for the **embEDUx** system must be created by carefully analyzing the
[project requirements](requirements.md). These include a wide variety of
necessary configuration options, which in turn requires a configurable build
system. The build system must be able to build the following software

* Linux Kernel
* Bootloader
* RootFS containing the system and user-space application, while the

while build configuration must be user providable for each build.  These
software that is built by the build system will be referred as ***products***
within the further documentation.


# Comparison With Similar Projects
The idea of building a complete Linux-based system for a specific platform is
not new. Therefore it is of no surprise, that by the time of designing
**embEDUx**, there are several open source projects that need to be considered
as a base for **embEDUx**. The following projects have feature specifications
could possibly fulfill the requirements that were previously defined. The
projects will be evaluated in order to find out if they suitable as base
projects.

* Embedian - unfortunately, the project was officially retired as of July 2014 

    A debian based distribution targetted for embedded systems

* Buildroot

    A collection of bash scripts in order to build toolchains, Linux-kernels,
    bootloaders and root filesystems. It can be configured via an ncurses-based
    menu.

* OpenEmbedded

* Yocto Project
    TODO lars
    

# Product-Specification Storage Units
It must be possible to build the products independently from each other.
Therefore, each product should be managed in a separate storage unit which will
be referred as a *repository* from this point on. Additionally each platform
needs to have its own identifiable storage unit within the *respository*. This
storage unit will be referred as *branch* from this point on.

## Repository Format
Configuration files and specification files are most certainly provided by the
user as text files. For this purpose, a version control system should be used in
order to have a history of build changes and allow easier handling of the
repositories.

# Product Requirement Analysis
The build process and the configuration options of each product must fulfill the
requirements of the corresponding product. The requirements chapter lists
different requirements for each product, which must therefore be analyzed
separately.



# Portability 
In order to have a portable build system, all components should live and run in
systems that are separated from the buildserver's host system. Possible
technologies for this are either Virtual Machines or Linux Containers.

## Virtualization and Container Technologies
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

## Split Functionality Into Containers
Containers are relatively cheap entities for the system. This allows the
buildsystem to be split into several containers for the different parts of the
buildsystem.

## Container Management Software
The choice of the container management software still needs to be evaluated, but in favor
of popularity Docker should be the main candidate.

# Setup Process
The buildserver will undoubtedly be a complex structure of software components.
To make the setup as easy as possible it should be automated as far as possible.

## Setup Parameters
Setup parameters are essential to the configuration of the buildserver.

* Buildserver Target Machine

    The target machine shall by default run all containers that belong to the
    buildsystem

* Target Platform and Architectures
    
    The platform names and their corresponding architecture.
    The architectures will be supported as build targets. 

## Automation
Any scripting language can be used and there's no chosen preference as of this
point.


# Maintenance
The way we handle the maintenance scenarios is a key factor in how well users
will accept the **embEDUx** build system.

# Extensibility 
Adding support for additional hardware platforms must be simple. The user should
not be forced to have a complete understanding of the **embEDUx** build system
to be able to add his platform. However the complexity of the system, requires
the user to have a fair overview of the **embEDUx** components and how these
work together in order to build the products.

### Workflow 
Platform specific source code must be avoided as far as possible. This results
in using mainline sources, wherever it is possible. Differences in the platform
architecture are adapted by patches, which are applied during the build process.
As the base sources, for each product and platform are the same, this will lead to
the same workflow for each platform and each product.

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
=> Design Continuous Integration
=> call user build script within a repository
=> cross compilation for kernel/uboot
=> find solution for rootfs

## How can we setup the CI?
=> ansible

## Visualization
The following graphic shows the aforementioned design decisions.

[![](background/design/img/design.png)](background/design/img/design.png)


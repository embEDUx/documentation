# Design
**(work in progress)**

The design for the **embEDUx** system must be created by carefully analyzing the
[project requirements](requirements.md). These include a wide variety of
necessary configuration options, which in turn requires a configurable build
system. The build system must be able to build the following software

* Linux Kernel
* Bootloader
* RootFS containing the system and user-space application

while build configuration must be user providable for each build.

The software that is built by the build system will be referred as
***products*** within the further documentation.

## Comparison With Similar Projects
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
    

## Product-Specification Storage Units
It must be possible to build the products independently from each other.
Therefore, each product should be managed in a separate storage unit which will
be referred as a *repository* from this point on. Additionally each platform
needs to have its own identifiable storage unit within the *respository*. This
storage unit will be referred as *branch* from this point on.

### Repository Format
Configuration files and specification files are most certainly provided by the
user as text files. For this purpose, a version control system should be used in
order to have a history of build changes and allow easier handling of the
repositories.

## Product Requirement Analysis
The build process and the configuration options of each product must fulfill the
requirements of the corresponding product. The requirements chapter lists
different requirements for each product, which must therefore be analyzed
separately.



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

## Extensibility 
Adding support for additional hardware platforms must be simple. The user should
not be forced to have a complete understanding of the **embEDUx** build system
to be able to add his platform. One way to look at extensibility is to already
take the initial setup into account, where the hardware platforms are
practically added too, just to a zero-base. Designing this step to be as easy as
possible, will allow to extend the system as easy as possible. Therefore, this
criteria is moved over to the [setup process](setup-process).

## Overall System Design
[![](background/design/img/design.png)](background/design/img/design.png)

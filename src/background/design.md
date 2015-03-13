# Design
**(work in progress)**

The design for the **embEDUx** system must be created by carefully analyzing the
[project requirements](requirements.md). These include a wide variety of
necessary configuration options, which in turn requires a configurable build
system. The build system must be able to build the following software

* Linux Kernel
* Bootloader
* RootFS containing the system and user-space application

while the build configuration must be user providable for each build.

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

* Yocto Project

    "Provides open source, high quality infrastructure and tools to help
    developers create their own **Linux** distribution for any hardware
    architecture, across muiltiple market segments. It is intended to provide a
    helpful starting point for developers."
    ([Source](https://wiki.yoctoproject.org/wiki/FAQ#What_is_the_Yocto_Project.3F))
    
## Repositories - Product-Specification Storage Units
It must be possible to build the products independently from each other.
Therefore, each product specification should be managed in a separate storage
unit which will be referred as a *repository* from this point on. Additionally
each platform needs to have its own identifiable storage subunit within the
*respository*. The storage subunits will be referred as *branches* from this
point on.

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


## Platform Support Extensibility 
Adding support for additional hardware platforms must be simple. The user should
not be forced to have a complete understanding of the **embEDUx** build system
to be able to add his platform. One way to look at extensibility is to already
take the initial setup into account, where the hardware platforms are
practically added too, just to a zero-base. Designing this step to be as easy as
possible, will allow to extend the system as easy as possible. Therefore, this
criteria is moved over to the [setup process](setup-process).

## Overall System Design
[![](background/design/img/design.png)](background/design/img/design.png)

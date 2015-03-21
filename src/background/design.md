# Design
**(work in progress)**
This page is the entry point of the design chapter and it includes many links to
more detailed explanations of the mentioned topics. In order to understand the
complete system design, please read the following page and all linked pages.

## Products Built By **embEDUx** 
The software that is built by the buildserver will be
referred as ***products*** within the further documentation. This helps to
distinguish between software that is used throughout the build system, and
software that is being built uses the build system.

The design for the **embEDUx** system must be created carefully by analyzing the
[project requirements](requirements.md) that have been determined by the
underlying circumstances at the HTWG and it's lab-courses. 

The requirements include a wide variety of necessary configuration options which
need to be considered for the design of the different products.  This in turn
requires a configurable build system, which must be able to build the following
software

* [Linux Kernel](design/linux.md)
* [Bootloader](design/bootloader.md)
* [RootFS](design/rootfs.md)

## Buildserver
While the build configuration must be user providable for each individual build.
Each individual build represents a configuration change that has been made by
the user. The buildserver must react to these changes and start the build
process.

* [Buildserver](design/buildserver.md)

## Hardware Deployment Tool
Deploying the built products to the platforms includes several steps.
**embEDUx** provides a deployment tool to make this process easier for the user.

* [Flashtool](design/flashtool.md)

## Specification Storage
To store the product specifications corresponding storage units must be
implemented. 

* [Repositories](design/repositories.md)

## Cross-Target Support
Even though the number of ARM-systems is growing, most Desktops and Servers are
still running on x86-based hardware-architectures. The platforms that are used
within the lab-courses are all based on the ARM architecture. Since the purpose
of the **embEDUx** buildsystem is to build and deploy complete Linux-based
systems for these hardware platforms, cross-target support is absolutely
necessary for the project to work.

## Comparison With Similar Projects
The idea of building a complete Linux-based system for a specific platform is
not new. Therefore it is of no surprise that by the time of designing
**embEDUx** there are several open source projects that have similar project
goals. These projects need to be considered as a base for the **embEDUx**
project. The following projects have feature specifications, that could possibly
fulfill the requirements that have been analyzed and collected on the
[requirements page](requirements.md).  The projects will be evaluated in order
to find out if they suitable as base projects.

* [Buildroot](evaluation/buildroot.md)
* [Yocto Project](evaluation/yocto-project.md)


## Overall System Design
[![](background/design/img/design.png)](background/design/img/design.png)

This is how the system has been designed in the beginning. Take a look at [post-evaluation system
design](evaluation.md#post-evaluation-system-overall-design) how the design
evolved throughout the evaluation phase.

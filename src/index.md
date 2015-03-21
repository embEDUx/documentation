# The **embEDUx** Project
The *embEDUx* project aims to deliver a **complete solution for building and
deploying customized linux distributions for educational purposes**.

The origin lays at a university of applied sciences called
[HTWG Konstanz](http://www.htwg-konstanz.de/English.20.0.html) located in Constance,
Germany.  For the complete story have a look at the [the
beginning](background/background.md#The Beginning).

We are working on making the current state publicly available.  We will also
upload the build specification files that allow you to reproduce our builds!

#### Terminology
Before continuing, please make sure that you are familiar with the
[terminology](background/terminology.md). If you keep an open eye for
crudities, you are encouraged to inform us by either opening an issue or putting
up a pull-request.

## Focus on Hardware
A variety from low up to high end ARM-boards were available during the design
and development of the project. Successful builds have been produced for

* Raspberry Pi
* Banana Pi
* Beaglebone Black
* Utilite Pro

## What Is It And What Can It Do?
* Automated build system for complete customized Linux distributions
* Easy to setup via the configurable setup routine
* Centralized build configurations for all your platforms
* Individual configuration and builds with specified targets, organized by
    * Platform: for Linux-Kernel, U-Boot
    * Architecture: RootFS
    * Hybrid: Toolchain, Misc-Files
* Working examples for the aforementioned hardware platforms


## What Is It Not? 
* Magic system for guessing all your platforms configuration automatically
* While we were able build, deploy to and run systems on these platforms, this
project is not meant to provide the builds them self. Instead, you will find
instructions how to setup or use an existing instance of the build system in
order to produce your own customized builds.

## Design and Implementation Choices
**embEDUx** is completely based on Open Source software. The biggest projects that
were chosen for the core of the solution are
### The Core

* GNU Toolchain
* Crosstool-NG
* Gentoo Linux
* Buildbot
* Ansible
* Qemu
* Das U-Boot Bootloader
* Git

If you are interested in why these components have been chosen, or how the system
was designed and implemented using these components, please head over to the
[***background section***](background/background.md).

## Building Customized Linux Distributions
The embEDUx build system been designed to build customized Linux distributions.
These systems consist of distinct products, namely

* Linux-Kernel
* Das U-Boot Bootloader
* Root Filesystem

and finally some miscellaneous files and a toolchain to support the build
process and later application development.

If you are not familiar with any of these terms, please consider reading through
the [terminology](background/terminology.md), and if necessary study other
subject related literature.


## Getting Started with ***your*** Distribution
The task of building a customized Linux distribution is rather complex, and the
**embEDUx** tries to not take away flexibility with the provided solution.
Therefore, a good understanding of the matter is needed and it is not possible
to provide you with a static instruction list. Like every software system, the
very basic topics are about its setup and its usage, here we go!

### Setup
If you already have access to a fully setup instance of the build system, you
can skip this chapter. 

* [Setup Instructions](setup/setup.md)

### Usage
The customized Linux distribution will consist of the aforementioned products,
of which you will have to build ***all*** in order to achieve ultimate glory
with a complete system for your target platform!

* [Usage Overview](usage/usage.md)

### Deploy
**embEDUx** ships a CLI-style [Flashtool](usage/flashtool.md) for
easy deployment to your hardware! 

* [Hardware Deployment](usage/usage.md#hardware-deployment)


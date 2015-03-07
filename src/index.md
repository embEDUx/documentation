# The **embEDUx** Project
The *embEDUx* project aims to deliver a **solution for building and deploying customimized
linux distributions for educational purposes**.

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

## The Core
embEDUx is completely based on Open Source software. The biggest projects that
were chosen for the core of the solution are

* GNU Toolchain
* Gentoo Linux
* Buildbot
* Ansible
* Qemu
* Das U-Boot Bootloader
* Git.

If you are interested in why these choice were made, please head over to the
[background section](background/background.md)

## Focus on Hardware
A variety from low up to high end ARM-boards were available during the design
and development of the project. Successful builds have been produced for

* Raspberry Pi
* Banana Pi
* Beaglebone Black
* Utilite Pro

While we were able build, deploy to and run systems on these platforms, this
project is not meant to provide the builds them self. Instead, you will find
instructions how to setup or use an existing instance of the build system in
order to produce you own customized builds.

## Customized Linux Distributions
The embEDUx build system been designed to build customized Linux distributions.
These systems consist of distinct products, which can and must be
built separately. The content of the build, or even the build process, is
specified by the user.

The distribution you'll build consists of these three products.

* [U-Boot](background/specs/uboot.md) images
* [Linux](background/specs/linux.md)-Kernel images and modules
* [RootFS](background/specs/rootfs.md)-archives based on Gentoo

Click on the links to learn more about how we specified the products.

In addition there is a [Flashtool](background/specs/flashtool.md) for easy deployment to hardware!

## Roles
The **embEDUx** build system consists of many components and there is a very big
difference in setting up the system or just using it. The different roles

Role | Responsibilities
--- | ---
Administrator | [Setup](setup/setup.md), [Create User Documentation](setup/user-documentation.md)
Distribution Architect | Building [U-Boot](usage/uboot.md), [Linux-Kernel](usage/linux.md), [RootFS](usage/rootfs.md)


## Getting Started with **your** Distribution
The following is a checklist and guideline how you can get started with building
your own distribution

1. [setup embEDUx](setup/setup.md)
    If you already have access to a fully setup instance of the build system,
    you can skip this step. Otherwise, please follow the link!

1. [User Documentation](setup/user-documentation.md)
    If you already have your user documentation, you can skip this step.
    Otherwise 

## Principal/Administrator
You are probably that tough guy, that needs to setup his servers for this
awesome **EmbEDUx** build system.

blablablabla

**Don't forget to provide your users with the [User
Documentation](setup/user-documentation.md)** for your setup.

## Student/Board Owner
You are the guy with the hardware. The guy that wants to run his really own configured
**Linux** distribution on his nice and shine hardware.

As you probably already know, for running your hardware you need a bootloader, a
**Linux** kernel and a RootFS. Luckily thats exactly what **EmbEDUx** will build
for you, as long as you provide the rules for the build process.

First start with the bootloader, **U-Boot**. Blablabla

When you done with your bootloader, continue with the **Linux** kernel. 

Once those two components are done, finally configure your fully personalized
RootFS.


## [Architectural Design](background/design/architecture.md)
[![](background/common/img/architectural_overview.png)](background/common/img/architectural_overview.png)

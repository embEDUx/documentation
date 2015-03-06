# The **embEDUx** Project
The *embEDUx* project aims to deliver a **solution for building and deploying customimized
linux distrubitions for educational purposes**.

The origin lays at a university of applied sciences called
[HTWG](http://www.htwg-konstanz.de/English.20.0.html) located in Constance,
Germany.  For the complete story have a look at the [the
beginning](background/background.md#The Beginning).

We are working on making the current state publicly available.  We will also
upload the build specification files that allow you to reproduce our builds!

#### Terminology
Before continuing, please make sure that you are familiar with the
[Terminology](background/common/terminology.md). If you keep an open eye for
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

## Delivered Components
The embEDUx build system has been designed to build the following components
according to user-provided specifications. 


* [U-Boot](background/uboot.md) images
* [Linux](background/linux.md)-Kernel images and modules
* [RootFS](background/rootfs.md)-archives based on Gentoo

In addition there is a [Flashtool](background/flashtool.md) for easy hardware deployment!

*(links goto background information pages)*

## Focus on Hardware
A variety from low up to high end ARM-boards were available during the design
and development of the project. Successful builds have been produced for

* Raspberry Pi
* Banana Pi
* Beaglebone Black
* Utilite Pro

## Architectural Overview
[![](background/common/img/architectural_overview.png)](background/common/img/architectural_overview.png)

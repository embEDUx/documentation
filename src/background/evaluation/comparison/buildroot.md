# Buildroot
A collection of Makefiles and bash scripts in order to build toolchains, Linux-kernels,
bootloaders and root filesystems through cross-compilation. It can be 
configured via an **ncurses**-based menu.

## Workflow
To start working with **buildroot** the user simply downloads the latest
stable **buildroot** version as tarball or retrieves the development state via
git. The [package requirements](http://buildroot.org/downloads/
manual/manual.html#requirement) for **buildroot** must be installed before the user
is able to use **buildroot**.


### Configuration
To start working with **buildroot** the user simply types `make menuconfig` to
create a configuration via a **ncurses**-based configuration menu similar to the
**Linux** configuration menu.

![**Buildroot** configuration via **ncurses**](background/evaluation/comparison/img/buildroot_configuration.png)

This configuration will manage the following steps:

#### Target options
Options which depend on the target architecture, like:

* Select the target architecture
* Application Binary Interface


#### Build options
Several options for the build procedure, e.g.:

* Selecting the download locations and mirrors
* Selecting a directory for patches
* gcc flags


#### Toolchain
The user can decide whether **buildroot** should build its own toolchain or 
should use an external toolchain. For the a own builded toolchain there are
several options, e.g.:

* C library: glibc, musl, uclibc
* Kernel header version
* Binutil options
* GCC options


#### System configuration
The user can configure several options for the built system, e.g.:

* System hostname
* Password encoding and root password
* Selecting a RootFS skeleton


#### Kernel
All kernel related configurations, e.g.:

* Kernel version
* Kernel patches
* Kernel configuration file
* Kernel binary format


#### Target packages
Selecting packages which will be installed with 
[busybox](http://www.busybox.net/) on the target **RootFS**. **Busybox** combines
many common unix utilities into a single executable. The provided packages for 
**BusyBox** are divided into several groups, e.g.:

* Audio and video applications
* Development tools
* Hardware handling


#### Filesystem images
Filesystem related configurations for the **RootFS** image, e.g.:

* Filesystem type (ext2/3/4, jffs2, etc.)
* Building a cpio archive of the **RootFS**
* Building a tarball of the **RootFS**


#### Bootloaders
User can select the bootloader which should be build for the target system,
the **buildroot** configuration provides several bootloaders, e.g.:

* Uboot and configuration (e.g. version, patches, binary format)
* Barebox
* Atmel related bootloaders


#### Host utilities
User can select various utilities for the host building system, e.g.:

* Uboot tools
* Tools for different filesystems


#### Legacy config options
Shows the user which packages were removed or renamed from the buildroot
configuration. The list is divided in subsections for each **buildroot**
version.


After going through the **buildroot** configuration a `.config` file will be
saved. With this config file the user can build the configured system with the
`make` command. **Buildroot** will download all required software components and
compile them for the target system. If no **cross-toolchain** was given, the tool 
will build the toolchain first, and compile the other software with it.

The user can also configure several package by itself after configuring
**buildroot**. The following packages can be configured via the **ncurses**
configuration procedure:

#### Configuring BusyBox

`make busybox-menuconfig`

This allows the user to configure **BusyBox** in more detail.

#### Configuring Linux kernel

`make linux-menuconfig`

This allows the user to make subsequent changes on the configuration of the 
downloaded kernel with the standard configuration procedure of the **Linux**
kernel.

#### Configuring uClibc

`make uclibc-menuconfig`

This allows the user to configure uclibc in the same way as for **BusyBox**.
    

## Summary
**Buildroot** is a nice tool to build an own distribution for different target
platforms. The way of configuring the distribution is well known and intuitive
for people who previously configured and built a **Linux** kernel, and are
familiar with the principle of cross compilation. People who are new to these
topics need to read documentation that goes beyond the F1-help-text that is
provided by the **Buildroot** configuration menu.

The **Buildroot** tool is able to provide a lot of packages for the target
system. It is also possible to build **BusyBox**-only RootFS. Every package is
built on the host system, using a cross-toolchain, that can either be
downloaded or also compiled configured and compiled within the
**Buildroot**-context. It is possible to add own packages, and a short instruction
how to add a new package (called applet) can be found [on the busybox
website](http://www.busybox.net/FAQ.html#adding). Adding new software can be a
cumbersome process, because it has to be cross-compilable and package
dependencies need to be maintained manually.

## Overview
Criteria | Result | Notes
--- | --- | ---
Cross-target support | YES | Manual configuration necessary
Package management | LIMITED | Difficult to extend
Buildroutine Automation | YES | Includes Kernel, Toolchain, RootFS
Deployment | NO | System must be installed by hand on the embedded device

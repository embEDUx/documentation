# Buildroot
*Buildroot is a set of Makefiles and patches that makes it easy to generate a
complete embedded Linux system. Buildroot can generate any or all of a
cross-compilation toolchain, a root filesystem, a kernel image and a bootloader
image.* ([source](http://buildroot.uclibc.org/about.html))
The evaluation process was done with the **buildroot** version *2014.02*.

## Workflow
To start working with **buildroot** the user simply downloads the latest
stable **buildroot** version as tarball or retrieves the development state via
git. The [package requirements](http://buildroot.org/downloads/
manual/manual.html#requirement) for **buildroot** must be installed before the user
is able to use **buildroot**.


### Configuration and Building
To start working with **buildroot** the user simply types `make menuconfig` to
create a configuration via a **ncurses**-based configuration menu similar to the
**Linux** configuration menu.

![**Buildroot** configuration via **ncurses**](background/evaluation/comparison/img/buildroot_configuration.png)

#### Linux Kernel an Uboot

**Buildroot** supplies a mechanism to build any **Linux** kernel or **Uboot** version
the user want to. It provides an interface to add additional configuration
files and patches. The configuration of **Uboot** and **Linux** can be done
separately.


#### Toolchain
The user can decide whether **buildroot** should build its own toolchain or 
should use an external toolchain. This built toolchain is designed to work 
in the **Buildroot** context. Unfortunately the built toolchains from
**Buildroot** have absolute symbolic links compiled within the binaries. As a
result the toolchains are not portable.



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

# Buildroot
*Buildroot is a set of Makefiles and patches that makes it easy to generate a
complete embedded Linux system. Buildroot can generate any or all of a
cross-compilation toolchain, a root filesystem, a kernel image and a bootloader
image.* ([source](http://buildroot.uclibc.org/about.html))

This evaluation was done with the **buildroot** version *2014.02*.

**Buildroot** uses a **ncurses**-based configuration menu similar to the
**Linux** configuration menu. 

![**Buildroot** configuration via **ncurses**](background/evaluation/comparison/img/buildroot_configuration.png)

## Products
This part of the document evaluates the support for the defined
[required](../../requirements.md).

### Linux Kernel and U-Boot
**Buildroot** supplies a mechanism to build any **Linux** kernel or **Uboot**
version is provided by the user. It provides an interface to add additional
configuration files and patches. The configuration of **Uboot** and **Linux**
can be done separately.

### Toolchain
The user can decide whether **buildroot** should build its own toolchain or use
an external toolchain. This resulting toolchain is designed to work within the
**Buildroot** context. Unfortunately these toolchains have absolute symbolic
links compiled within the binaries. As a result the toolchains are not portable
which is a [requirement](../../requirements.md#lab-course-specific-requirements)
for the **embEDUx** system.

### RootFS
The **Buildroot** tool is able to provide a lot of packages for the target
system. It is also possible to build **BusyBox**-only RootFS. Every package is
built on the host system, using a cross-toolchain.

It is possible to add own packages, and a short instruction how to add a new
package (called applet) can be found [on the busybox
website](http://www.busybox.net/FAQ.html#adding).  But adding new software can
be a cumbersome process, because it has to be cross-compilable and package
dependencies need to be maintained manually.

The user is dependent on the...


## Summary
**Buildroot** is a nice tool to build an own distribution for
different target platforms. The way of configuring the distribution is well
known and intuitive for people who previously configured and built a **Linux**
kernel, and are familiar with the principle of cross compilation. People who are
new to these topics need to read documentation that goes beyond the F1-help-text
that is provided by the **Buildroot** configuration menu.

## Overview Criteria | Result | Notes 
--- | --- | --- 
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Difficult to extend 
Buildroutine Automation | YES | Includes Kernel, Toolchain, RootFS 
Deployment | NO | System must be installed by hand on the embedded device


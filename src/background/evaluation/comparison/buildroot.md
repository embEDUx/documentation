# Buildroot
*Buildroot is a set of Makefiles and patches that makes it easy to generate a
complete embedded Linux system. Buildroot can generate any or all of a
cross-compilation toolchain, a root filesystem, a kernel image and a bootloader
image.* ([source](http://Buildroot.uclibc.org/about.html))

This evaluation was done with the **Buildroot** version *2014.02*.

**Buildroot** uses a **ncurses**-based configuration menu similar to the
**Linux** configuration menu. 

![**Buildroot** configuration via **ncurses**](background/evaluation/comparison/img/Buildroot_configuration.png)

## Products
This part of the document evaluates the support for the defined
[requirements](../../requirements.md).

### Linux Kernel and U-Boot
**Buildroot** supplies a mechanism to build any **Linux** kernel or **Uboot**
version is provided by the user. It provides an interface to add additional
configuration files and patches. The configuration of **Uboot** and **Linux**
can be done separately.

### Toolchain
The user can decide whether **Buildroot** should build its own toolchain or use
an external toolchain. This resulting toolchain is designed to work within the
**Buildroot** context. Unfortunately these toolchains have absolute symbolic
links compiled within the binaries. As a result the toolchains are not portable
which is a [requirement](../../requirements.md#lab-course-specific-requirements)
for the **embEDUx** system.

### RootFS
The **Buildroot** tool is able to provide a lot of packages for the target
system. It is also possible to build **BusyBox**-only RootFS. Every package is
built on the host system, using a cross-toolchain.

Due to the fact, that **Buildroot** does only provide a small set of the
standard **Linux** userspace applications and libraries, it can be reasonably
assumed that the required software packages for the different lab-courses must
be added to the **Buildroot** 

**Buildroot** allows the user to [add own packages](http://Buildroot.uclibc.org/downloads/manual/manual.html#adding-packages).
But adding new software can be a cumbersome process, because it has to be 
cross-compilable and package dependencies need to be maintained manually.


## Summary
**Buildroot** is a nice tool to build an own distribution for
different target platforms. The way of configuring the distribution is well
known and intuitive for people who previously configured and built a **Linux**
kernel, and are familiar with the principle of cross compilation. People who are
new to these topics need to read documentation that goes beyond the F1-help-text
that is provided by the **Buildroot** configuration menu.

On the other hand **Buildroot** can't satisfy all requirements of the
**embEDUx** project. One important requirement is, that the system should
provide a portable toolchain. This is not possible with **Buildroot** as
mentioned before. Another unsatisfied requirement is the provision of userspace
applications for the **RootFS**. 

Criteria | Result | Notes 
--- | --- | --- 
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Difficult to extend 
Buildroutine Automation | YES | Includes Uboot, Kernel, Toolchain, RootFS 
Deployment | NO | System must be installed by hand on the embedded device


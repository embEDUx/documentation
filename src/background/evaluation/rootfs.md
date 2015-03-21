# Evaluation RootFS
The evaluation for the RootFS needs to find a suitable solution that combines
the designed features:

* Cross-target support
* Package management
* Build routine Automation

## Gentoo Portage
**Gentoo Portage** is a full-fledged source-based package management system that
can install, uninstall and update a huge variety of software package on a Linux
System. The so called *portage tree* holds the package specification files
*(ebuilds)* that allows the `emerge`-utility to build and install the packages
into the system.

* `emerge`-utility

    The `emerge`-utility written in python for accessing the features of
    **Portage** from the command line. The program calculates dependencies and
    arranges the package installation order accordingly. The build process
    itself happens inside a sandbox environment. This protects the system from
    possibly dangerous commands inside  ebuilds. The compilation and
    installation into the system will only succeed of no sandbox violation
    occurred during the proccess.

* USE-flags - package customization

    USE-flags are one of **Porage**'s excellent features that allows the user to
    custmize the packages that are available for installation. Most USE-flags
    translate directly to options that are passed to the `./configure`-step int
    he compilation process.

* Binary package support
    
    Successfull package builds can be stored in a binary package format. They
    can be resued for further installations without the need to compile the same
    package more than once.

* portage-tree overlay support

    It is possible to define additional portage trees in order to extend the
    available ebuils and therefore extend the available software packages.


### Result Gentoo Portage
Criteria | Result | Notes
--- | --- | ---
Cross-target support | NO / native-only | uses installed system buildtools for
compilation


## Gentoo Catalyst

## Gentoo Crossdev and Cross-Emerge
Gentoo's crossdev is a utility that can create cross-toolchains and setup
wrappers for the emerge utility to use the cross-toolchain on the target RootFS that is
laying in the host system's filesystem. 

The following script shows the furthest point of evaluation with these tools. It
is annotated with comments that describe what's done and why.

```
#! /bin/bash

export TARGET_CHOST=arm-hardfloat-linux-gnueabi

# Building cross toolchain and minimal rootfs
crossdev -t ${TARGET_CHOST} --portage "-bg" --b 2.24-r2 --g 4.8.2 --k 3.14 --l
2.19

# Initializing emerge wrapper
crossdev --init-target ${TARGET_CHOST} --b 2.24-r2 --g 4.8.2 --k 3.14 --l 2.19

# Switch to default arm profile
rm /usr/${TARGET_CHOST}/etc/portage/make.profile
ln -s /usr/portage/profiles/default/linux/arm/13.0
/usr/${TARGET_CHOST}/etc/portage/make.profile

# Crosscompiling Python has problems with the readline and ncurses library.
mkdir /usr/${TARGET_CHOST}/etc/portage/package.use
echo 'dev-lang/python -readline -ncurses' >
/usr/${TARGET_CHOST}/etc/portage/package.use/python

# We use python 2.7 and 3.3.
echo 'PYTHON_TARGETS="python2_7 python3_3"' >>
/usr/${TARGET_CHOST}/etc/portage/make.conf 
mkdir /usr/${TARGET_CHOST}/etc/portage/package.mask
echo '=dev-lang/python-3.4*' >
/usr/${TARGET_CHOST}/etc/portage/package.mask/python

# Set USE flags and maximum load level according to the num of CPUs
cat <<EOF >> /usr/${TARGET_CHOST}/etc/portage/make.conf
USE="\${USE} minimal -acl -nls -ipv6 -man -doc -fortran -openmp -static
-static-libs -spell -berkdb -gdbm"
NUMCPUS=$(cat /proc/cpuinfo  | grep processor | wc -l)
MAKEOPTS="-l\${NUMCPUS} -j\${NUMCPUS}"
EMERGE_DEFAULT_OPTS="--jobs 3 --load-average=\${NUMCPUS} -b"
EOF

# Create basic directory structure
mkdir /usr/${TARGET_CHOST}/{dev,sys,proc,usr,usr/portage}

# Fix for python cross-compile
cat <<EOF > /tmp/config.site
ac_cv_file__dev_ptmx=yes
ac_cv_file__dev_ptc=yes
EOF
ARCH=arm CONFIG_SITE=/tmp/config.site emerge-${TARGET_CHOST} -av python:2.7
python:3.3
rm /tmp/config.site

# emerge internal arm glibc and gcc. make sure future links happen against these
libraries and not the toolchains ones.
ARCH=arm emerge-${TARGET_CHOST} -av glibc gcc binutils

# emerge a minimal base system which can install packages on its own. this will
depend on python and many other wanted packages
ARCH=arm emerge-${TARGET_CHOST} -av gzip app-arch/tar portage baselayout openrc

# emerge default arm system set as far as possible
ARCH=arm emerge-${TARGET_CHOST} -DNauv --keep-going=y --with-bdeps=y @system
```

The last line tells the cross-emerge to emerge all packages that are enlisted in
the *@system* set. The system-set contains an init-manager, python and the base
system utilities that are needed to work with a Linux-system. This process
**failed every time**. As you can see in the comments of the previous steps, the
script mentions a fix and a needed workaround which involved recompiling the
cross-toolchain with the initial cross-toolchain in order to function not
properly, but better. **Inconsistent results** were achieved and build failures
during the system installation could not be fixed nor completely explained.
Experimentation with different versions for glibc, binutils, kernel headers and
gcc version did hot help. either.

### Results Crossdev and Emerge-Crossdev
Criteria | Result | Notes
--- | --- | ---
Cross-target support | NO | not reliable
Package management | YES | portage package manager included
Build routine Automation | NO | needs wrapper


## Qemu User Emulation
Qemu user emulation makes uses of the BINFMT\_SUPPORT to execute binaries of
foreign binary formats by executing them with a binary simulator for the
corresponding architecture. 

The following example shows how a statically compiled qemu-user emulator for ARM is copied from
the host system into the target RootFS, which has been setup by crossdev. It
then prepares a conventional `chroot`-workflow and executes the steps. As a
result, the shell inside the target RootFS is run by the qemu-user emulator for
ARM, and one can continue working inside the target RootFS as if it was a native
system.

```
cp /usr/bin/qemu-arm /usr/${TARGET_CHOST}/usr/bin/
cat <<EOF > /usr/${TARGET_CHOST}/enter-me.sh
#! /bin/sh
ROOTFS=/usr/${TARGET_CHOST}
cp /etc/resolv.conf \${ROOTFS}/etc/resolv.conf
mount --rbind /dev \${ROOTFS}/dev
mount --bind /proc \${ROOTFS}/proc
mount --bind /sys \${ROOTFS}/sys
mount --bind /usr/portage \${ROOTFS}/usr/portage
chroot \${ROOTFS}/
umount \${ROOTFS}/*/* \${ROOTFS}/* 2>/dev/null
EOF
chmod +x /usr/${TARGET_CHOST}/enter-me.sh
/usr/${TARGET_CHOST}/enter-me.sh
```

In the process of building various packages that are required in the further
procedure of creating the  build-system, we encountered many situations were the
qemu-user emulation was not reliable. Here is one example were the compilation
of the Golang-compiler fails with an error from the tcg ([Tiny Code Generator](http://wiki.qemu.org/Documentation/TCG). 

```
cmd/go
 (null)*(null) Unable to trace static ELF: /var/tmp/portage/dev-lang/go-1.3.3/work/go/pkg/tool/linux_arm/go_bootstrap: /var/tmp/portage/dev-lang/go-1.3.3/work/go/pkg/tool/linux_arm/go_bootstrap clean -i std 
/var/tmp/portage/app-emulation/qemu-2.1.2-r1/work/qemu-2.1.2/tcg/tcg.c:1683: tcg fatal error
./make.bash: line 161:  1136 Aborted                 "$GOTOOLDIR"/go_bootstrap clean -i std
 * ERROR: dev-lang/go-1.3.3::gentoo failed (compile phase):
 *   build failed
 * 
 * Call stack:
 *     ebuild.sh, line  93:  Called src_compile
 *   environment, line 2076:  Called die
 * The specific snippet of code:
 *       ./make.bash || die "build failed";
```
Errors like these make qemu-user an unreliable solution for the **embEDUx** project.

### Result Qemu user emulation
Criteria | Result | Notes
--- | --- | ---
Cross-target support | NO | not reliable

## Qemu System Emulation
System Emulation was already a considered as an abstraction technique in the
[Buildserver Design - Virtual Machines](virtual-machines). In comparison to
[Qemu user emulation](Qemu-user-emulation), a complete system is emulated
instead of translating the foreign machine code into the machine code executable
by the running host machine. 
### Filesystem Passthrough via 9p-fs
The first approach is to store a target RootFS directly on the filesystem of
the build machine, and pass it to the virtual machine via the **9p-fs**.

```
QEMU_AUDIO_DRV=none qemu-system-arm \
  -M virt \
  -m 4095 \
  -nographic \
  -kernel output/zImage \
  -append "root=root rw rootflags=rw,trans=virtio,version=9p2000.L rootfstype=9p console=ttyAMA0" \
  -net user \
  -netdev user,id=vnet0 \
  -device virtio-net-device,netdev=vnet0 \
  -device virtio-serial-device \
  -chardev socket,path=/tmp/foo,server,nowait,id=vconsole \
  -device virtserialport,chardev=vconsole,name=vconsole \
  -fsdev local,id=root,path=rootfs/,security_model=passthrough \
  -device virtio-9p-device,fsdev=root,mount_tag=/dev/root
```


### Limitations
In comparison, this method has significant limitations of different nature, due
to the following reasons:

* Target Linux-Kernel required for the virtual machine

    In order to run a virtual machine, a kernel that supports executing in the
    target system must be configured and compiled using a cross-toolchain. The
    preperation of the kernel for the virtual machine shall not be covered in
    the RootFS evaluation.

* No multi-core support for ARM architectures

    While **Qemu** supports the simulation of multiple ARM-CPU-cores inside the
    virtual machine, it does not use more than one processor on the host.
    Multicore build machines can therefore not be fully utilized by single
    virtual ARM machines.


* [Bugs in the 9p-fs filesystem](https://bugs.launchpad.net/qemu/+bug/1336794)
  that make it impossible to use the virtual machine like in a chroot-manner

    The bug in the 9p-fs makes it necessary to create and maintain a disk image for
    the virtual machine, which introduces additional overhead in the disk I/O that
    happens within the virtual machine. This topic will not be evaluated further
    since it is not new to the team members, and will be considered for the
    implementation if *Qemu system emulation* will make it into the next round.


### Result Qemu system emulation
Besides the performance overhead, the virtual machine performs reliable during
the evaluation phase.

While a virtual machine itself would add extra complexity to the build process,
it would allow to run arbitrary

Criteria | Result | Notes
--- | --- | ---
Cross-target support | YES | slow through complete system emulation

## Overview
From the aforementioned evaluation and the evaluation of
[buildroot](buildroot.md) and the [Yocto Project](yocto-project.md) the results
are as shown.

Candidate | Cross-target support | Package management | RootFS Build routine Automation
--- | --- | --- | ---
Gentoo Portage | NO | YES | -
Gentoo catalyst | NO | - | YES
YOCTO | YES | LIMITED / difficult to extend | YES 
Buildroot | YES | LIMITED / difficult to extend | YES
Gentoo crossdev and cross-emerge | NOT RELIABLE | YES / portage | -
Qemu user emulation | LIMITED / not fully reliable | - | -
Qemu system emulation | YES / slow | - | -

## Conclusion
It seems like there is no completely ready solution for building RootFS. As a
result, the choice is to pick the components that **offer reliability in
cross-target support, and package management qualities** and incorporate the
them into a custom automated build routine. The components chosen for the task
are **Gentoo Portage** paired with **Qemu system emulation** in case of
Cross-Target buildjobs.

# Evaluation RootFS Build routine
As described in the design chapter [Buildserver - Build Automation
Routines](../design/buildserver.md#build-automation-routines), the automated RootFS build routine will be triggered by the continuous integration master component.

## RootFS Build routine Steps
Based on recent evaluation results and the described steps that were designed
under [Design - RootFS Build Automation
Routine](../design/rootfs.md#rootfs-build-automation-routine), the RootFS
build routine can be specified in greater detail.

1. If running on a Cross-Target Container
    1. Ensure that the disk image for the virtual machine is prepared
    1. Ensure that the Cross-Target Virtual Machine has been setup
    1. Ensure the virtual machine is running and reachable
1. If running on a native container
    1. Ensure that the RootFS for the chroot is prepared
    1. Esnure  that the SSHd
1. Retrieve the build specifications from the RootFS-repository
1. Parse the package list provided by the user
1. Translate the package list into a format that is accepted by the package
   manager
   1. Cleanup the build files
   1. Create an archive from the RootFS
1. Pack the RootFS contents

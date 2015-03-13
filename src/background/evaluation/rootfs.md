# Evaluation RootFS
The evaluation for the RootFS needs to find a suitable solution that combines
the designed features:

* Cross-target support
* Package management
* Buildroutien Automation

## YOCTO 
## Buildroot

## Gentoo Crossdev and Cross-emerge
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

### Results crossdev and emerge-crossdev
Criteria | Result | Nots
--- | --- | ---
Cross-target support | NO | not reliable
Package management | YES | portage package manager included
Buildroutien Automation | NO | needs wrapper


## Qemu user emulation
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

Criteria | Result | Nots
--- | --- | ---
Cross-target support | NO | not reliable

## Qemu system emulation
System Emulation was already a considered as an abstraction technique in the
[Buildserver Design - Virtual Machines](virtual-machines)

Throughout the RootFS buildprocess, a virtual machine could be used to run a
native compiler for the target architecture.

Criteria | Result | Nots
--- | --- | ---
Cross-target support | YES | slow through complete system emulation


## Gentoo Portage

## Gentoo catalyst


### Evaluation Result Overview

Candiate | Cross-target support | Package management | Buildroutine Automation
--- | --- | --- | ---
YOCTO | LIMITED | LIMITED | YES
Buildroot | YES | LIMITED | YES
Gentoo Crossdev and Cross-emerge | NOT RELIABLE | YES | -
Qemu user emulation | NOT RELIABLE | NO | NO
Qemu system emulation | YES/SLOW | - | -
Gentoo Portage | - | YES | -
Gentoo catalyst | NO | YES | YES


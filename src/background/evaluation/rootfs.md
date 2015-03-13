# Evaluation RootFS
The evaluation for the RootFS needs to find a suitable solution that combines
the designed features:

* Cross-target support
* Package management
* Buildroutine Automation

## Yocto Project
The **Yocto Project** is divided in multiple sub-projects. After the build
process an entire **Linux** distribution is created, including the toolchain.

* Bitbake (build tool)

    **Bitbake** is the sub-project that builds the output system image, and is
    based on **Gentoo Portage**. The buildprocess uses meta data to calculcate 
    the installation instructions. 

* Openembedded-Core - Meta data (available software)

    The meta data is provided by the **openembedded-core** and is stored as
    recipes which are used by **Bitbake** to build the packages. As the **Yocto
    Project** is mainly targetted on creating images for the embedded
    domain, it seems that the meta data, and therefore the available software
    packgaes, is updated less frequently when compared to other package
    management systems.

* Hob (Human Oriented Builder)

    **Hob** is a graphical user interface which allows the user to select a
    platform (machine) and an image recip. The image recipe contains the
    information of which packages should be build. This configuration can be
    modified with **Hob**. **Hob** is a nice tool, once all the required meta
    data exist to select and start the generation process.

The **Yocto Project** offers a great set of tools and possibilities, but needs a
lot of configuration. Everything is capsulated within the recipes, so an easy
editing of kernel version or user-space software is not possible.

### Result Yocto Project
Criteria | Result | Nots
--- | --- | ---
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Package manager can be configured with own repository
Buildroutine Automation | YES | -

## Buildroot


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

In the vast number of provided packages are many dependencies between this packages. Some dependencies are required and must be resolved by the package manger,  some are optional depending on the scope of features a user want to have (e.g. vim can be installed with a graphical  or just with a textual interface). 

The portage system offers users a mechanism to indicate which software features they would like to include or exclude while building packages. This mechanism is called ___USE flags___. 

_USE flags_ are managed in Gentoo systems at several areas. There are profile flags, default flags, package or atom flags and temporary flags. This flags are evaluated due installation in this order. This means a _Use flag_ defined in a higher instance will be overwritten by an _USE flag_ in a lower instance.

### Let's make a recipe: ebuild

As mentioned before an _ebuild_ is not more as a recipe (precisely a script) which defines how to build a certain package. The used language is _bash_.

To retain the overview in the _portage tree_ every _ebuild_ is dedicated to a specific category. It is also possible that several package have the same name but are dedicated in different categories.

The next example will explain how to create an own _ebuild_. The basic requirement for a new software package is a valid _makefile_ with an "install" target. The following example will be an _ebuild_ for the [car2car library](https://apu.in.htwg-konstanz.de/armrider/car2car/raw/master/doc/thesis_final.pdf) package.

The basic _Gentoo ebuilds_ are stored in the normal _portage tree_ at _"/usr/portage". Own _ebuilds_ can't be stored at this location since a _portage_ update would delete all inofficial _ebuilds_ from this _portage tree_. So it's advisable to create an so called ___overlay___ (read more about ovelrays in chapter [Expanding portage: Creating a portage overlay](Gentoo-Portage#expanding-portage-creating-a-portage-overlay)). This overlay is located at ```/usr/local/portage-car2car```. Next the car2car package must dedicated to a _portage-category_. There's a list with all available _portage-categories_ at ```/usr/portage/profiles/categories```. In this case we use the category __"net-libs"__, so ther must be created a new directory in the overlay.

``` mkdir -p /usr/local/portage-car2car/net-libs/libcar2car```

Next a ebuild will be defined at this location. It must contain the version of the program as suffix. The complete path of the ebuild is ```/usr/local/portage-car2car/net-libs/libcar2car/libcar2car-1.0.ebuild```:

```bash
EAPI=4

DESCRIPTION="C2C Library which is needed to communicate with other ARMrider"
HOMEPAGE="http://armrider.in.htwg-konstanz.de"
SRC_URI="${P}.tar.bz2"
RESTRICT="fetch"

LICENSE=""
SLOT="0"
KEYWORDS="amd64 i386 arm"
IUSE=""

DEPEND="dev-libs/boost
        >=sys-devel/gcc-4.7.3"
RDEPEND="${DEPEND}"

src_install() {
    # Install lib.
    dolib.so libcar2car.so || die

    # Install headerfiles from ./libcar2car
    insinto /usr/include/libcar2car
    cd include
    doins -r * || die
}
```

### Binary Pakage support


TODO: Use this text:
http://armrider.in.htwg-konstanz.de/index.php/Gentoo_-_Einf%C3%BChrung


### Expanding portage: Creating a portage overlay * **README**
http://dev.gentoo.org/~ulm/pms/head/pms.html#x1-350004.4

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
Criteria | Result | Nots
--- | --- | ---
Cross-target support | NO | not reliable
Package management | YES | portage package manager included
Buildroutien Automation | NO | needs wrapper


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
Criteria | Result | Nots
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

### Performance Loss
In comparison, this method has siginificant
performance limitations and overhead, due to the following reasons:

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

Criteria | Result | Nots
--- | --- | ---
Cross-target support | YES | slow through complete system emulation


## Evaluation Result 

### Feature Overview
Candiate | Cross-target support | Package management | Buildroutine Automation
--- | --- | --- | ---
Gentoo Portage | - | YES | -
Gentoo catalyst | NO | - | YES
YOCTO | LIMITED | LIMITED / difficult to extend | YES 
Buildroot | YES | LIMITED / difficult to extend | YES
Gentoo crossdev and cross-emerge | NOT RELIABLE | YES | -
Qemu user emulation | LIMITED / not fully reliable | - | -
Qemu system emulation | YES / slow | - | -

### Conclusion
It seems like there is no solution that is ready to be integrated into the
designed continuous integration system without further modifications or
automation processes wrapped around. As a result, **the choice will favor
reliability in cross-target support, and package management qualities** and
incorporate the winners into a custom automated buildroutine.

# Evaluation RootFS Buildroutine Automation
As described in the design chapter [Buildserver - Build Automation
Routines](../design/buildserver.md#build-automation-routines), the automated RootFS buildroutine will be triggered by the continuous integration master component.

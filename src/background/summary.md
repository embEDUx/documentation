# Summary
This page gives a summary of what has been achieved with the **embEDUx**
project.

## Features and used Core Components
* cross target support (Qemu, Crosstool-NG)
* automated yet configurable setup (Ansible, configuration templates)
    * low initial entry barrier
    * flexibility for advanced users
* continuous integration (Buildbot)
    * automated builds
    * build monitoring
    * version control and collaboration (Git)
* user providable download/build scripts for kernel/uboot/toolchain/misc
    * highly flexible and locally testable
    * working example build scripts for a quick start
    * freedom of choice for sources and patches
* plenty of recent software packages for the RootFS (Gentoo/Portage)
* possibility of manual or semi-automatic deployment

## Main Advantages over existing Projects
* Designed for continuous integration
* [Yocto Project](evaluation/yocto-project.md#summary)
    * less platform integration overhead
    * better package availability
* [Buildroot](evaluation/buildroot.md#summary)
    * less platform integration overhead
    * better package availability
    * portable toolchain

## Main Disadvantages over existing Projects
* Slow cross RootFS builds due to Qemu System Emulation

## Successful Integrated Platforms
* Raspberry Pi
* Beaglebone Black
* Banana Pi
* Utilite Pro

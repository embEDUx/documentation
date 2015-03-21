# Summary
This page gives a summary of what has been achieved with the **embEDUx**
project.

## Features And Used Core Components
* cross target support (**Qemu**, **Crosstool-NG**)
* automated yet configurable setup (**Ansible**, configuration templates)
    * low initial entry barrier
    * flexibility for advanced users
* continuous integration (**Buildbot**)
    * automated builds
    * build monitoring
    * version control and collaboration (**Git**)
* user providable download/build scripts for kernel/uboot/toolchain/misc
    * highly flexible and locally testable
    * working example build scripts for a quick start
    * freedom of choice for sources and patches
* plenty of recent software packages for the RootFS (**Gentoo**/**Portage**)
* possibility of manual or semi-automatic deployment

## Main Advantages Over Comparable Projects
* Designed for continuous integration
* [Yocto Project](evaluation/yocto-project.md#summary)
    * less platform integration overhead
    * better package availability
* [Buildroot](evaluation/buildroot.md#summary)
    * less platform integration overhead
    * better package availability
    * portable toolchain

## Main Disadvantages Over Comparable Projects
* Slow cross RootFS builds due to Qemu System Emulation

## Future Development
The initial project authors transferred the **embEDUx** project to GitHub in
order to make it available for public use and to attract further developers.

## Critics
Starting off as a study project, many of the early decisions were heavily biased
by the university environment. These decisions were later reviewed and efforts
were made to make the project portable. However, there are still issues that
need to be resolved in order to improve the build system make it viable for more
generic scenarios.

As the project lives on GitHub now, the publicly available issue trackers will
be used. A list of all issue trackers can be found on the [FAQ
page](../troubleshooting/faq.md).

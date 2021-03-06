# Evaluation Linux 
The considerations from the [design](../design/linux.md) will be evaluated
within this chapter. As the decision against the **Yocto Project** and
**Buildroot** was already made, those two are no longer evaluated and a solution
to build the **Linux** kernel with low configuration effort has to be found.

## Cross Target Support
**Linux** supports cross compilation and can therefore be compiled with a
cross toolchain.

## Build Process 
Due to keeping the possibility to build the kernel locally, emerging the kernel
sources with OS dependent tools (e.g. emerge with **Gentoo**) is not a viable
solution. As already mentioned in the [u-boot evaluation](uboot.md), keeping the
sources within the **Linux** repository will lead to a lot of overhead when the
same **Linux** versions should be build for different platforms. The same
solution as already described in the [u-boot evaluation](uboot.md) will be used.

Each **Linux** version has a branch, which contains a script that downloads the
specific sources. Each platform has a branch for each **Linux** version that
should be build. This branch contains a script which executes the download
script from the **Linux** version branch.

[![Structure](background/evaluation/img/eval_linux.png)](background/evaluation/img/eval_linux.png)

## Build Steps
With the now evaluated build process, the build steps can be redefined.

1. Checkout platform branch for **Linux** version X
1. Checkout **Linux** version X branch
1. Call build script ***build*** from platform branch
    * set necessary build parameters
1. Call build script ***build*** from **Linux** version X branch
    * download sources
    * if provided apply patches
    * build **Linux**
    * create archive

## Build Tools
These tools are needed to successfully iterate through the build steps.

* bash
* make 
* gcc
* git
* wget
* patch
* tar
* bzip2
* awk
* sed


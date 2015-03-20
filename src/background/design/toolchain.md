# Design Toolchain
The Linux-Kernel and the Bootloader must be able to be compiled from their
sources, otherwise the user is not able to provide the configuration. In order
to build these products for the different platforms a Toolchain for the
respective build targets is required. The toolchain should also be configurable
by the user, which leaves the following projects for the evaluation of the
toolchain creation.

* [Yocto Project](https://www.yoctoproject.org/)
* [Crosstool-NG](http://crosstool-ng.org/)
* [Buildroot](http://buildroot.uclibc.org/)

Another derivation from the [requirements](../requirements.md) is the need for a
portable toolchain.

## Build process
1. Retrieve the build specifications from the repository
1. Build toolchain with provided configuration
1. Create an archive with the toolchain


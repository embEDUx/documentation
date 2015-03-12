**(work in progress)**

## Toolchains for Building Kernel and Bootloader
The Linux-Kernel and the Bootloader must be compiled from their sources,
otherwise the user is not able to provide the configuration for these.  In oder
to build these products for the different platforms a Toolchain wit the
respective build targets is required. The toolchain should also be user
configurable, which leaves the following projects for the evaluation of
toolchain creation.

* Crosstool-NG
* Buildroot

### Build process
1. Retrieve the build specifications from the **Toolchains**-repository
1. Translate the toolchain specifications
1. Build toolchain
1. Create an archive with the toolchain
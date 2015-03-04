# Repositories and branches

The following image shows the structure how the **Git** repositories should be
setup by your system administrator. The image should help you to understand the
importance of the different repositories and branches for the **embEDUx**
project. 

As you can see, there are 5 repositories. Each repository holds the data for the
five products that **embEDUx** can build. 

Those are:

* linux: Kernel image and device tree blob
* uboot: **U-Boot** image
* toolchain: Toolchain
* rootfs: RootFS
* misc: Miscellaneous files, that are needed on the boot or root partition

[![Repository structure](usage/common/img/repositories.png)](usage/common/img/repositories.png)

### Legend

1. Source branch
Each version of the **Linux** kernel needs to have exactly one *kernel* branch in
the *linux* repository. Also for each version of **U-Boot**, exactly one *uboot*
branch is needed in the *uboot* repository.

1. Platform branch
For each platform there needs to be one *platform* branch in the *linux*,
*uboot* and *misc* repository.

1. RootFS repository
As multiple Platforms have the same architecture, there is only one RootFS
needed for each architecture. But as there are multiple courses offered, which
need different RootFS, each RootFS is build for each architecture.

1. Toolchain repository
For each architecture, there needs to be a toolchain branch in the *toolchains*
repository. These toolchains are statically linked, so that everyone can use
them on their own development system. Theoretically also a
[canadian](http://crosstool-ng.org/#canadian_build) toolchain can be possible.

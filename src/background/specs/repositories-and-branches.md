# Specification - Repositories and Branches

**(work in progress)**

This is the specification that has been worked out according to the [design on
repositories and branches](../design/repositories-and-branches.md).

## Textual Specification
The five repositories form the base structure which allows an independent
management for the different products. Each repository holds the content
necessary for building the product. The content will be processed by a central
buildserver. 

Repository Name | Desired build output
--- | ---
linux |  Linux-Kernel images, DeviceTreeBlobs, module archives
uboot |  U-Boot image blobs
toolchain |  Toolchain archives
rootfs |  RootFS content archives
misc |  Miscellaneous files archives (needed on boot and root partitions)

## Visualization
This is a visualization of the relations between the different products and
their corresponding repositories. It shall be used by Administrators and Users
to understand the structure. The Administrator can learn how the repositories
should be setup, and the User should be able to understand the importance of the
different repositories and branches for the **embEDUx** project. 

[![Repository structure](usage/common/img/repositories.png)](usage/common/img/repositories.png)


### Footnotes
1. Source branch

    Each version of the **Linux** kernel needs to have exactly one
    *version\_generic* branch in the *linux* repository. Also for each version
    of **U-Boot**, exactly one *version\_generic* branch is needed in the
    *uboot* repository.

1. Platform branch

    For each platform there needs to be one *version\_platform* branch in the *linux*,
    *uboot* and *misc* repository.

1. RootFS repository

    For each RootFS -> architekture dependency (which can be directly inherited
    from the platform) there needs to be one branch.

1. Toolchain repository

    For each architecture, there needs to be a toolchain branch in the
    *toolchains* repository. These toolchains are statically linked, so that
    everyone can use them on their own development system. Theoretically also a
    [canadian](http://crosstool-ng.org/#canadian_build) toolchain can be
    possible.

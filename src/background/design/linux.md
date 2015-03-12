# Linux Buildprocess Design
**(work in progress)**

## Linux-Version 
No specific **Linux** kernel version is required and the software solution must
not be restricted to a specific kernel version. It would be reasonable to have
the same kernel sources for all of the platforms, and only provide platform
specific patches to the common base where necessary. In addition to these
patches, it should be able to provide a specific configuration for a build.

## Build Process
To retrieve the **Linux** kernel sources, there are the following possibilities.

* User has to provide the sources within the **Linux** repository
* Emerge **Gentoo** kernel sources ebuild during build process
* Download and patch kernel sources manually from
  [www.kernel.org](https://kernel.org) during build process

## Build Steps
The build process must include the following steps.

1. Retrieve the build specifications from the **Linux**-repository
1. Retrieve **Linux** kernel sources
1. Apply required patches provided from the **Linux**-repository
1. (Cross-)Compile kernel for target architecture with kernel config provided by
   the specifications
1. Create two archives from the necessary files.
    * destination boot partition (kernel image, device tree blob)
    * destination root partition (e.g. modules)

# Build Process Generalization
Platform specific source code must be avoided as far as possible. This leads to
to using the mainline sources whenever it is possible. Differences in the
platform architecture are represented and stored differentially. As the base sources, for each product and platform are the same, this
will lead to the same workflow for each platform and each product.

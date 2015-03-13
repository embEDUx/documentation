# Implementation for building Toolchain 
The [design](../design/toolchain.md) and the
[evaluation](../evaluation/toolchain.md) result in the following implementation.

## Repository
The repository is called *toolchain-specs*. Each host architecture / target
architecture combination gets its own branch. The branch contains the build
script and the toolchain configuration required for **Crosstool-NG**.

## Build steps
1. Call `ct-ng build`
1. Compress output in archive.

## Build script
The following build script reflects the build steps.

* [build](setup/post-install/toolchains/default/toolchain_build)

# Implementation for building Toolchain 

For each toolchain, the *toolchain-specs* repository contains exactly one
branch. The branch contains the *.config* file for **Crosstool-NG** and the
build script, that will do the following steps:

1. Call `ct-ng build`
1. Compress output in archive.

## Build Script
For simplicity bash is used for the script language. As an example the two
scripts, which were implemented and uses throughout the whole development and
test process are provided:

* [build](setup/post-install/toolchains/default/toolchain_build)

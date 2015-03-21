# Evaluation Toolchain
As written in the [design](../design/toolchain.md) there are two possible
solutions, but with the evaluation of the [Yocto Project](yocto-project.md) and
[buildroot](buildroot.md) already done, there is only one solution left.

## Crosstool-NG
**Crosstoo-NG** offers the possibility to build static, and therefore portable
toolchains. With **Crosstool-NG** even toolchains , that are built on host with
architecture X, compiled for architecture Y, cross-compiling for architecture Z
are possible. These kind of toolchains are called *canadian* toolchain.
**Crosstool-NG** also has an **ncurses** based configuration menu similar to the
**Linux** kernel *menuconfig*, which results in an intuitive usage. The
configuration is stored in a .config file and can be stored within the
specification storage unit.

## Repository
Each toolchain gets its own branch. That means one branch contains a toolchain
for a specified host and target architecture.

## Build Steps
Following build steps are necessary to retrieve the toolchain.

1. Checkout toolchain branch
1. Call the build script ***build***.
1. Provide the output in an archive

## Build Tools
These tools are needed to successfully iterate through the build steps.

* ct-ng 
* bash > 3.0
* date
* git
* tar
* bzip2
* sed


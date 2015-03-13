## Evaluation Toolchain

As written in the [design](../design/toolchain.md) there are two possible
solutions. Unfortunately toolchains built with **Buildroot** have absolute
symbolic links compiled within the binaries and are therefore the result is not
portable. As we want to have a portable toolchain, this fact disqualifies
buildroot for our needs. Fortunately, **Crosstool-NG** offers the possibility to
build static toolchains. With **Crosstool-NG** even toolchains are possible, that
are built on host with architecture X, compiled to be ran on architecture Y,
cross-compiling for architecture Z. These kind of toolchains are called
*canadian* toolchain.  Crosstool-NG has also an *ncurses* based configuration
menu similar to the **Linux** kernel *menuconfig*. The configuration is stored
in a .config file.

## Repository
Each toolchain gets its own branch. That means one branch contains a toolchain
for a specified host and target architecture.

## Build steps
Following build steps are necessary to retrieve the toolchain.

1. Checkout toolchain branch
1. Build toolchain with **Crosstool-NG** and the given configuration
1. Provide the output in an archive

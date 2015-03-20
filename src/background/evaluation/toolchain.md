## Evaluation Toolchain

As written in the [design](../design/toolchain.md) there are two possible
solutions, but with the [evaluation of buildroot](comparison/buildroot.md) in
mind, there is only one solution left. 

### Crosstool-NG
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

## Build steps
Following build steps are necessary to retrieve the toolchain.

1. Checkout toolchain branch
1. Build toolchain with **Crosstool-NG** and the given configuration
1. Provide the output in an archive


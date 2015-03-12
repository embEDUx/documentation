## Evaluation Toolchain

As written in the [design](../design/toolchain.md) there are two possible
solutions. Unfortunately toolchains built with buildroot have absolute symbolic
links compiled within the binaries and are therefore not portable. As we want to
have a portable toolchain, this fact disqualifies buildroot for our needs.
Fortunately, Crosstool-NG offers the possibility to build static toolchains.
Wit Crosstool-NG even toolchains are possible, that are built on host with
architecture X, compiled to be ran on architecture Y, cross-compiling for
architecture Z. These kind of toolchains are called *canadian* toolchain.
Crosstool-NG has also an *ncurses* based configuration menu similar to the
**Linux** kernel *menuconfig*.

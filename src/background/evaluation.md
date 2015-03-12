# Evaluation
The considerations from the [design](design.md) will be evaluated within this
chapter.

## Comparison With Similar Projects
- | Buildroot | Yocto
--- | --- | ---
Setup | `git clone git://git.buildroot.net/buildroot` | `git clone -b dizzy git://git.yoctoproject.org/poky.git`
Configuration | `make menuconfig` | Configuration is happening in conf files, although there is also a GUI 
Output | Bootloader, Kernel, RootFS, Toolchain | SD Card Image
Platform Support | - | Common platforms are supported or available through so called *Board Support Packages (BSP)*, otherwise manual configuration can be done
Software Support | - | Common software is available, otherwise can be added by creating own recipes

### Conclusion
As we want to have a highly dynamic system, where we still offer up-to date
products, non of the aforementioned projects offer a satisfying solution.
Therefore developing our own projects is necessary.


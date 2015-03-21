# Building Qemu Kernels
The first build jobs for your instance of **embEDUx** build system will probably
be the Linux-Kernels for the Qemu Emulators that will run in the cross RootFS
containers. 


## Default Setup
Every supported target architecture that has no native RootFS container needs
one kernel.

## Default Example - 3.18.1\_qemu-virt-arm
The current default setup requires just one Kernel for all
ARM-RootFS-buildslaves.  For an example Linux-Specification, please have a look
at the following branches:

* Version Generic: <https://github.com/embEDUx/linux-specs/tree/3.18.1>
* Version Platform: <https://github.com/embEDUx/linux-specs/tree/3.18.1_qemu-virt-arm>

Please follow the [Linux-Kenrel Usage Instructions](../../usage/linux.md) along
with the above example branches and you should have your first Linux-Build in no
time.

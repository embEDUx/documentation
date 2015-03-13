# Implementation building miscellaneous files
During the implementation of the **Linux** and **U-Boot** build process,
scenarios occurred, where files needed to be provided to the boot or root
partition. Unfortunately these files couldn't be assigned to any of the existing
repositories.

Therefore the *misc-spec* repository was added. The solely purpose of this
repository is to store files for the platform. Each platform has one branch
within the repository. Each branch contains the build script and two folder,
which represent the destination partition.

* src\_boot
* src\_root

The files are stored in the respective folder within their folder structure,
which means that e.g. the *inittab* file is stored in *src\_root/etc/inittab*.
Another example would be the firmware blobs for the raspberry pi or the
**U-Boot** script, which need to be stored within root directory of the boot
partition. These files would be stored in *src\_boot/*.

## Build steps & script
The build scripts only purpose is to provide the archives for each destination
partition. Therefore is only archives the two folders *src\_boot* and
*scr\_root*.

* [build](usage/misc/default/platform_build)


# Linux
This guide will help you through the steps to generate a **Linux** kernel for
your desired platform.

## Prerequisites
All of the [...]() apply also to this guide.

### Requirements
* Git Repository *linux*
* **Buildbot** setup for desired platform architecture

### Suggestions
* Toolchain (Host architecture -> target architecture)

    A toolchain will allow you to test your platforms' kernel configuration
    locally.

## Naming schema
**Buildbot** can only build your images, if you follow this naming schema

* Kernel branch: <kernel\_version\> (eg. 3.17.2)
* Platform branch: <kernel\_version\>\_<platform\_name\> (eg. 3.17.2_raspberry-pi)

**Importan: The platform\_name must not contain any underscores, use dashes
instead!**

## Add new upstream kernel
Before you can add [a new platfom](#add-new-platform-for-a-linux-kernel), for
which you want to build a **Linux** kernel, you first need to add an *kernel*
branch to the *linux* repository.

1. Clone the *linux* repository. The URL should have been provided to you by
   your system administrator.
   ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git 
   ```

1. Add a *kernel* branch named *<Major\>.<Minor\>.<Subminor\>* to the *linux*
   repository. 
   ```
$ git checkout master
$ git branch 3.18.7
$ git checkout 3.18.7
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 3.18.7
   ```

1. Add the [template](usage/linux/template/kernel_build) as ***build*** to the repository
   and make it executable.
   ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 20:52 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
   ```

1. Modify *KERNEL\_URL*, *KERNEL\_FILE* and *PATCH\_VERSION* in the ***build***
   script, to match the desired kernel version. Be careful with the **Gentoo**
   patch version, as the version number not necessarily needs to fit to the
   resulting **Linux** kernel. In this case **Gentoo** patches 3.18-9 result in
   **Linux** kernel 3.18.7.
   ```
...
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-3.18.tar.xz"
...
PATCH_VERSION="3.18-9"
...
   ```

1. Add the files, commit and push. 
   ```
$ git add build
$ git commit -m "new kernel"
$ git push 
   ```

1. Now you have a *kernel* branch for your desired **Linux** kernel version
   within your *linux* repository. The next step is to add *platform* branches
   to the repository.

## Add new platform for a **Linux** kernel
This step requires an existing [*kernel* branch](#add-new-upstream-kernel) for
which you want to add a platform.

1. If not already done, clone the *linux* repository. The URL should have been
   provided to you by your system administrator. 
   ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git
   ```

1. Add a *platform* branch following the naming schema
   *<Major\>.<Minor\>.<Subminor\>\_<platform\>* to the *linux* repository.
   It is necessary for that the **Buildbot** is able to detect the just created
   branch, therefore this branch needs to be pushed to the remote repository
   ```
$ git checkout master
$ git branch 3.18.7_raspberry-pi
$ git checkout 3.18.7_raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 3.18.7_raspberry-pi
   ```

1. Add the [template](usage/linux/template/platform_build) as ***build*** to the
   repository and make it executable. 
   ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 21:20 build
-rw-r--r-- 1 user user    0 Mar  1 21:19 README
   ```

1. Modify *KERNEL\_VERSION* in ***build*** to the desired version, which also
   has to be the name of the *kernel* branch. Finally modify *KERNEL\_DTB* to
   the desired device tree blobs name. Make sure the device tree sources exist
   in the **Linux** sources, which will be downloaded by the *kernel* branch. If
   not, you need to add them by adding a patch to the *platform* branch. In this
   case the desired device tree sources do exist, so nothing is left to do.
   ```
...
KERNEL_VERSION="3.18.7"
...
KERNEL_DTB="bcm2835-rpi-b.dtb"
KERNEL_CONFIG=".config"
KERNEL_IMG="zImage"
...
   ```

1. Add a working kernel configuration ***.config*** to the repository. If you
   aren't sure if your kernel configuration is working, you can test it locally
   by executing ***build*** with the fitting [toolchain](toolchains.md).
   ```
$ ls -hla
total 76K
drwxr-xr-x 1 user user  44 Mar  1 21:29 .
drwxr-xr-x 1 user user 650 Mar  1 15:04 ..
-rwxr-xr-x 1 user user 562 Mar  1 21:25 build
-rw-r--r-- 1 user user 69K Mar  1 21:29 .config
drwxr-xr-x 1 user user 188 Mar  1 21:29 .git
-rw-r--r-- 1 user user   0 Mar  1 20:51 README 
   ```

1. Optional: Add needed patches to the repository.
   ```
$ ls -hl
total 8.0K
-rw-r--r-- 1 user user 2.8K Mar  1 21:38 9000-Smsc95xx_allow_mac_to_be_set.patch
-rwxr-xr-x 1 user user  562 Mar  1 21:25 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
   ```

1. Add all files, commit  and push branch upstream.
   ```
$ git add build
$ git add .config
$ git add *.patch
$ git commit -m "added raspberry-pi 3.18.7 kernel build"
$ git push
   ```

1. The **Buildbot** should start building your kernel now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first kernel for your first platform. If
   you have a [uboot](uboot.md), a [rootfs](rootfs.md) and the
   necessary [misc](misc.md) files, you can flash everything with the
   [flashtool](flashtool.md).


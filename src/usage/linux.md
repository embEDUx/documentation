# Linux
This guide will help you through the steps to build a **Linux** kernel for
your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/user-documentation.md).

* Git Repository
* **Buildserver** setup for desired platform architecture

### Suggestions
* Build/download a toolchain. This will allow you to test your build
  configuration before you push it upstream.

* Have a look at the default build scripts. As the **Buildserver** just executes
  these scripts, you have no limits on what you want to do before, during and
  after the build process.

## Name scheme
The **Builserver** can only build your images, if you follow this name scheme
for any of the branches:

* Kernel branch: <Major\>.<Minor\>.<Subminor\> (eg. 3.17.2)
* Platform branch: <kernel-branch-name\>\_<platform-string\> (eg. 3.17.2_raspberry-pi)

Please look up the Platform string in the [User
Documentation](../setup/user-documentation) provided by your administrator. If
your platform doesn't exist yet, please contact your administrator.

## Add new upstream kernel
Before you can add [a new platfom](#add-new-platform-for-a-linux-kernel), for
which you want to build a **Linux** kernel, you first need to add a *kernel*
branch to the *linux* repository. 

In this case we will add a branch for 3.18.7 **Linux** kernel.

1. Clone the *linux* repository with the URL provided in the user documentation.
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git 
    ```

1. Add a *kernel* branch *<Major\>.<Minor\>.<Subminor\>* to the *linux*
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

1. Add the [default script](usage/linux/template/kernel_build) as ***build*** to the
   repository and make it executable.

    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 20:52 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
    ```

1. Modify *KERNEL\_URL*, *KERNEL\_FILE* in the ***build*** script, to match the
   desired kernel version. You also need to modify *PATCH\_VERSION*, which is
   the version of the **Gentoo** specific patches. Be careful with the version
   number, as it doesn't necessarily fit to the resulting **Linux** kernel
   version. In this case **Gentoo** patches 3.18-9 result in **Linux** kernel
   3.18.7.
   
    ```
...
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-3.18.tar.xz"
...
PATCH_VERSION="3.18-9"
...
    ```

1. Add the files, commit and push them upstream. 
   
    ```
$ git add build
$ git commit -m "new kernel"
$ git push 
    ```

1. Now that you have a *kernel* branch for your desired **Linux** kernel version
   within your *linux* repository, the next step is to add *platform* branches
   to the repository.

## Add new platform for a **Linux** kernel
This step requires an existing [*kernel* branch](#add-new-upstream-kernel) for
which you want to add a platform.

1. If not already done, clone the *linux* repository with the URL provided in
   the user documentation.
   
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git
    ```

1. Add a *platform* branch following the name schema
   *<kernel-branch\>\_<platform-string\>* to the *linux* repository. It is
   necessary that you push this initial branch upstream, so the **Buildserver**
   can find the new *platform* branch.

    ```
$ git checkout master
$ git branch 3.18.7_raspberry-pi
$ git checkout 3.18.7_raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 3.18.7_raspberry-pi
    ```

1. Add the [default script](usage/linux/template/platform_build) as ***build***
   to the repository and make it executable. 
   
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 21:20 build
-rw-r--r-- 1 user user    0 Mar  1 21:19 README
    ```

1. Modify *KERNEL\_VERSION* in ***build*** to the desired *kernel* branch. Then
   modify *KERNEL\_DTB* to the desired device tree blob. If your platforms
   device tree sources aren't in the **Linux** kernel sources yet, you have to
   add them with a patch, as described in a later step.
   
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
   by executing ***build*** with the fitting [toolchain](toolchains.md#Usage).
   
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

1. Optional: Add needed patches to the root of your *platform* branch. The patch
   needs to be in the standard patch format, as created wit `diff -Naur`.
   
    ```
$ diff -Naur linux/.../smsc95xx.c.old linux/.../smsc95xxx.c > 9000-Smsc95xx_allow_mac_to_be_set.patch
$ ls -hl
total 8.0K
-rw-r--r-- 1 user user 2.8K Mar  1 21:38 9000-Smsc95xx_allow_mac_to_be_set.patch
-rwxr-xr-x 1 user user  562 Mar  1 21:25 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
    ```

1. Add all files, commit and push the  branch upstream.
   
    ```
$ git add build
$ git add .config
$ git add *.patch
$ git commit -m "added raspberry-pi 3.18.7 kernel build"
$ git push
    ```

1. The **Buildserver** should start building your kernel image now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first kernel for your first platform. If
   you have a [uboot](uboot.md), a [rootfs](rootfs.md) and the necessary
   [misc](misc.md) files, you can flash everything with the **Flashtool** or
   deploy your files manually (see [Hardware
   Deployment](usage.md#hardware-deployment)).


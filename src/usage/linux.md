# Linux
This guide will help you through the steps to build a **Linux** kernel for
your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/user-documentation.md).

* Git Repository *linux*
* **buildserver** setup for desired platform architecture

### Suggestions
* Build/download a toolchain. This will allow you to test your build
  configuration locally before you push it upstream.

* Have a look at the default build scripts
  ([generic](usage/linux/default/generic_build),
  [platform](usage/linux/default/platform_build)). As the **buildserver**
  just executes these scripts, you have no limits on what you want to do before,
  during and after the build process.

## Branch Name-Scheme
The **builserver** can only build your images, if you follow the correct
name-scheme for the branches.

The variables that are needed for your platform can be found in the [User
Documentation](../setup/user-documentation.md).

### Variables

Variable | Notes
--- | ---
Platform-String | Specified and mapped to the target architecture by the Administrator. Found in the [User Documentation](../setup/user-documentation.md)
Major | Kernel major version number (**X**.2.3)
Minor | Kernel minor version number (1.**X**.3)
Subminor | Kernel subminor version number (1.2.**X**)

### Branches
To avoid unnecessary redundancy, which will naturally occur if you build
multiple platforms for the same kernel version, following branch structure is
necessary. The default build scripts
([generic](usage/linux/default/generic_build),
[platform](usage/linux/default/platform_build)) follow exactly this idea.

Branch | Dependency | Task
--- | --- | ---
version\_generic | platform independent | Provide **Linux** sources with **Gentoo** patches
version\_platform | platform dependent | Store .config, user patches, call build script in version\_generic branch

For each kernel version, there will be exactly one *version\_generic* branch,
where for each platform there will be one *version\_platform* branch. Following
name-scheme has to be followed.

Branch | Scheme | Example
--- | --- | ---
version\_generic | < major \>.< minor \>.< subminor \> | 3.17.2
version\_platform | < major \>.< minor \>.< subminor \>\_< platform-string \> |  3.17.2\_raspberry-pi

## Step-by-Step Example
The following example will give you a detailed overview of the necessary steps
to build kernel 3.18.7 for the raspberry pi. We assume that at this point the
*linux* repository is empty.

### Add new upstream kernel
Before you can add [a new platfom](#add-new-platform), for which you want to
build a **Linux** kernel, you first need to add a *version\_generic* branch to
the *linux* repository. 

1. Clone the *linux* repository with the URL provided in the user documentation.

    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git 
    ```

1. Add a *version\_generic* branch to the *linux* repository. 

    ```
$ git checkout master
$ git branch 3.18.7
$ git checkout 3.18.7
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 3.18.7
    ```

1. Add the [default script](usage/linux/default/generic_build) as ***build*** to the
   branch and make it executable.

    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 20:52 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
    ```

1. Modify *< kernel-url \>*, *< kernel-file \>* in the ***build*** script, to
   match the desired [kernel version](https://www.kernel.org/pub/linux/kernel/).
   You also need to modify *< patch-version \>*, which is the version of the
   **Gentoo** specific
   [patches](http://dev.gentoo.org/~mpagano/genpatches/tarballs). Be careful as
   the version number of the **Gentoo** patches doesn't follow the version
   number of the **Linux** kernel. In this case **Gentoo** patches 3.18-9 result
   in **Linux** kernel 3.18.7.
   
    ```
...
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-3.18.tar.xz"
...
PATCH_VERSION="3.18-9"
...
    ```

1. Add your changes, commit and push them upstream.
   
    ```
$ git add build
$ git commit -m "new kernel"
$ git push 
    ```

1. Now that you have a *version\_generic* branch for your desired **Linux** kernel
   version within your *linux* repository, the next step is to add a *version\_platform*
   branch.

### Add new platform
This step requires an existing [*version\_genereric*](#add-new-upstream-kernel)
branch for the **Linux** kernel version you want to add a platform.

1. If not already done, clone the *linux* repository with the URL provided in
   the user documentation.
   
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git
    ```

1. Add a *version\_platform* branch to the *linux* repository. It is necessary that you
   push the branch at this point upstream, so the **buildserver** can find the
   new *version\_platform* branch.

    ```
$ git checkout master
$ git branch 3.18.7_raspberry-pi
$ git checkout 3.18.7_raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 3.18.7_raspberry-pi
    ```

1. Add the [default build script](usage/linux/default/platform_build) as ***build***
   to the branch and make it executable. 
   
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 2.9K Mar  1 21:20 build
-rw-r--r-- 1 user user    0 Mar  1 21:19 README
    ```

1. Modify *< kernel-version \>* in ***build*** to the desired *version\_generic*
   branch. Then modify *< kernel-dtb \>* to the desired device tree blob. If
   your platforms device tree sources aren't in the **Linux** kernel sources
   yet, you have to add them with a patch, as described in a later step.
   
    ```
...
KERNEL_VERSION="3.18.7"
...
KERNEL_DTB="bcm2835-rpi-b.dtb"
KERNEL_CONFIG=".config"
...
    ```

1. Add a working kernel configuration ***.config*** to the branch. If you aren't
   sure weather your kernel configuration is working or not, you can run the build
   script locally with a proper [toolchain](toolchains.md#Usage).
   
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

1. Optional: Add needed patches to the root directory of your branch. The patch
   needs to be in the standard patch format, eg. created with `diff -Naur`.
   
    ```
$ diff -Naur linux/.../smsc95xx.c.old linux/.../smsc95xxx.c > 9000-Smsc95xx_allow_mac_to_be_set.patch
$ ls -hl
total 8.0K
-rw-r--r-- 1 user user 2.8K Mar  1 21:38 9000-Smsc95xx_allow_mac_to_be_set.patch
-rwxr-xr-x 1 user user  562 Mar  1 21:25 build
-rw-r--r-- 1 user user    0 Mar  1 20:51 README
    ```

1. Add all changes, commit and push them upstream.
   
    ```
$ git add build
$ git add .config
$ git add *.patch
$ git commit -m "added raspberry-pi 3.18.7 kernel build"
$ git push
    ```

1. The **buildserver** should start building your kernel image now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first kernel for your first platform. If
   you have a [uboot](uboot.md), a [rootfs](rootfs.md) and the necessary
   [misc](misc.md) files, you can flash everything with the **Flashtool** or
   deploy your files manually (see [Hardware
   Deployment](usage.md#hardware-deployment)).


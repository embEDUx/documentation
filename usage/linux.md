# Linux

1. [Naming schema](#naming-schema)
1. [Kernel branch](#kernel-branch)
1. [Platform branch](#platform-branch)
1. [Usage example](#usage-example)

The *linux* repository contains the scripts to build a *Linux* kernel.

## Naming schema
To create a Linux kernel **embEDUx** needs at least one *kernel* branch and a
*platform* branch. The branches need to follow a certain name schema:

* Kernel branch: \<kernel\_version> (eg. 3.17.2)
* Platform branch: \<kernel\_version>\_\<platform\_name\> (eg. 3.17.2_raspberry-pi)

**Importan: The platform\_name must not contain any underscores, use dashes
instead!**

## Kernel branch
The *kernel* branch will provide all the platform independent files, which are
the kernel sources, the **Gentoo** patches and the build script to patch and
build the kernel. Multiple platforms use for the same kernel version the same
*kernel* branch and therefore the same kernel sources.

Use this [template](linux/template/kernel_build) when adding a new kernel
version to the *linux* repository. Only change the variables  *KERNEL_URL*,
*KERNEL_FILE* and *PATCH_VERSION* to fit to the desired kernel version. The
*KERNEL_URL* and the *KERNEL_FILE* can be obtained from
[www.kernel.org](https://www.kernel.org/).  The *PATCH_VERSION* for the desired
kernel version can be obtained from
[dev.gentoo.org](https://dev.gentoo.org/~mpagano/genpatches/tarballs/).

Because Gentoo patches are applied during build process, make sure that the
kernel version and the Gentoo patch version match to each other.  The
*\<Major\>.\<Minor\>* version (eg. 3.17, 3.18, 3.19) is a common base version
for the Gentoo patches. The version of the  Gentoo patches doesn't strictly
  follow the kernel version, which can lead to the situation, that Gentoo
  patches 3.18-8 result in the linux kernel version 3.18.7.

**Important: Gentoo patch version does NOT need to reflect resulting linux
kernel version**

These are the, that need to be modified for each kernel version.
```bash
...
### Sources
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-<Major>.<Minor>.tar.gz"
...
PATCH_VERSION="<Major>.<Minor>-<Subminor>"
...
```

## Platform branch
The *platform* branch has to contain all platform dependent informations, which
are a valid kernel configuration and optional user patches. Furthermore it needs
to contain the build script named ***build***. Use this
[template](linux/template/platform_build) to add a new platform, or a new
kernel version for the platform to the *linux* repository.

With this template, the only variables that have to be changed are
*KERNEL\_VERSION*, which should be the name of the *kernel* branch and the
*KERNEL\_DTB*, which should be the name of the desired device tree file.

**Important: The sources for the device tree file have to be present in the
kernel sources, or otherwise added by a user patch.**

These are the lines that need to be modified.
```
KERNEL_VERSION="<kernel_version>"
...
KERNEL_DTB="<platform_dtb>"
KERNEL_CONFIG=".config"
KERNEL_IMG="zImage"
...
```

### User patches
Sometime the user wants to add new drivers, device tree source code, or a bug
fix before the build process is started. In this case those files need to be
present as a patch in the root folder of the *platform* branch.

### Environment variables
With a local installed cross toolchain and valid  *kernel* branch in the *linux*
repository it is possible to test the *platform* build script locally. In order
to be able to execute the ***build*** script, the following environment
variables need to be set.
* Target architecture:
  ARCH= (eg. 'arm')
* Path to the cross toolchain:
  CROSS_COMPILE= (eg.'armv6j-ctng-linux-gnueabi/bin/armv6j-ctng-linux-gnueabi-')
* Path where **embEDUx** should store its files:
  EMBEDUX_TMP= (eg. '/var/tmp/embedux/download/'

## Usage example 
In the following example a new 3.18.7 kernel and the raspberry-pi platform for
that kernel will be added to the *linux* repository. 

### Add new kernel
The following steps are necessary before you can [add](#add-new-platform) a
*plaform* for the desired kernel version to the repository.

1. Clone the *linux* repository. The URL for that repository should have been
   provided to you by your system administrator.
   ```
   $ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git 
   ```

1. Add a *kernel* branch named *\<Major\>.\<Minor\>.\<Subminor\>* to the *linux*
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

1. Add the [template](template/kernel_build) as ***build*** to the repository
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
   resulting **Linux** kernel.
   ```
   ...
   KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
   KERNEL_FILE="linux-3.18.tar.xz"
   ...
   PATCH_VERSION="3.18-9"
   ...
   ```

1. Add the changed files, commit and push. 
   ```
   $ git add build
   $ git commit -m "new kernel"
   $ git push 
   ```

1. Thats it. Now you have a *kernel* branch for your desired **Linux** kernel
   version within your *linux* repository. The next step is to add *platform*
   branches to the repository.

### Add new platform
This step requires an [existing](#add-new-kernel) *kernel* branch.

1. If not already done, clone the *linux* repository. The URL should have been
   provided to you by your system administrator. 
   ```
   $ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git
   ```

1. Add a *platform* branch named
   *\<Major\>.\<Minor\>.\<Subminor\>\_\<platform\>* to the *linux* repository.
   It is necessary that you push this initial branch, so **embEDUx** can start
   building your kernel after the last step.
   ```
   $ git checkout master
   $ git branch 3.18.7_raspberry-pi
   $ git checkout 3.18.7_raspberry-pi
   $ touch README.md
   $ git add README.md
   $ git commit -m "inital commit"
   $ git push --set-upstream origin 3.18.7_raspberry-pi
   ```

1. Add the [template](template/platform_build) as ***build*** to the repository
   and make it executable. 
   ```
   $ ls -hl
   total 4.0K
   -rwxr-xr-x 1 user user 2.9K Mar  1 21:20 build
   -rw-r--r-- 1 user user    0 Mar  1 21:19 README
   ```

1. Modify *KERNEL\_VERSION* in ***build*** to the desired version, which also
   has to be the name of the *kernel* branch. Finally modify *KERNEL\_DTB* to
   the desired device tree blobs name and make sure the device tree sources do
   exist in the kernel sources.
   ```
   KERNEL_VERSION="3.18.7"
   ...
   KERNEL_DTB="bcm2835-rpi-b.dtb"
   KERNEL_CONFIG=".config"
   KERNEL_IMG="zImage"
   ...
   ```

1. Add a working kernel configuration ***.config*** to the repository.
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
   $ git add \*.patch
   $ git commit -m "new platform"
   $ git push
   ```

1. The **buildbot** should start building your kernel now. You can follow the
   build process on the **buildbot** website.
   ![Buildbot done](img/buildbot_done.png)

1. Congratulations, you just built your first kernel for your first platform.
   You can either use the [flashtool](flashtool.md) to flash the
   kernel image to your platform device or simple do the flash process manually
   with the archives from the **Buildbot** website.


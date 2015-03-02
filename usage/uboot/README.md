# U-boot

1. [Naming schema](#naming-schema)
1. [Kernel branch](#kernel-branch)
1. [Platform branch](#platform-branch)
1. [Usage example](#usage-example)

## Naming schema
To create **u-boot** **embEDUx** needs at least a *uboot* branch and a
*platform* branch. The branches need to follow a certain name schema:

* Uboot branch: \<uboot\_version> (eg. 2015.01-rc1)
* Platform branch: \<uboot\_version>\_\<platform\_name\> (eg. 2015.01-rc1_raspberry-pi)

**Importan: The platform\_name must not contain any underscores, use dashes
instead!**

## uboot branch
The uboot branch will contain the platform independent files, which in this case
are the uboot sources and the build script to build the uboot image.

**embEDUx** provides a [template](usage/uboot/template/uboot_build) that only
needs to be modified for the desired uboot version.

These are the important lines, in general editing *UBOOT\_FILE* to the desired
uboot version archive (eg. u-boot-2015.01-rc1.tar.bz2) should be enough. The
archive name can be obtained from [ftp.denx.de](http://ftp.denx.de/pub/u-boot/).

```bash
...
UBOOT_URL="http://ftp.denx.de/pub/u-boot"
UBOOT_FILE="<uboot_filename>"
...
```

## Platform branch 
The *platform* branch only contains the build script ***build***. This build
script needs to be modified to build the desired uboot version. A good start is
this [template](usage/uboot/template/platform_build).

Only *UBOOT\_VERSION*, *UBOOT\_CONFIG* and eventually *FIRMWARE\_IMG* need to be
modified. 

```
...

...
```

There are also some rare cases, where the user might want to proceed
certain steps before or after the output is created. In this case the user can
define the function pre_output() or post_putput().

* pre_output(): Will be executed before the output is packed.
* post_output(): Will be executed after the output was packed.

### Environment variables
With a local installed cross toolchain and an exising *kernel* branch in the
repository it is possible to test the *platform* build script locally. In order
to work, following environment variables need to be set.
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

1. Add a *kernel* branch named *\<Major\>.\<Minor\>.\<Subminor\>* to the *linux*
   repository. It is necessary that you push this initial branch, so **embEDUx**
   can start building your kernel after the last step.
   ```
   $ git checkout master
   $ git branch 3.18.7
   $ git checkout 3.18.7
   $ git touch README.md
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
   script, to match the desired kernel version.
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

The build script in the corresponding *platform* branch can now use the just
created *kernel* branch.

### Add new platform
This step requires an [existing](#add-new-kernel) *kernel* branch.

1. Add a *platform* branch named
   *\<Major\>.\<Minor\>.\<Subminor\>\_\<platform\>* to the *linux* repository.
   It is necessary that you push this initial branch, so **embEDUx** can start
   building your kernel after the last step.
   ```
   $ git checkout master
   $ git branch 3.18.7_raspberry-pi
   $ git checkout 3.18.7_raspberry-pi
   $ git touch README.md
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

1. Modify *KERNEL\_VERSION* in ***build*** to the desired version, which is also
   the name of the *kernel* branch. Finally modify *KERNEL\_DTB* to the desired
   device tree blobs name and make sure the device tree sources do exist in the
   kernel sources.
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
   You can use the [flashtool](usage/flashtool/README.md) to flash the kernel image
   to your platform device.


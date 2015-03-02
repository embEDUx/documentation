# U-Boot

1. [Naming schema](#naming-schema)
1. [Kernel branch](#kernel-branch)
1. [Platform branch](#platform-branch)
1. [Usage example](#usage-example)

The *uboot* repository contains the scripts to build a **U-Boot** image for your
desired platform.

## Naming schema
To create **U-Boot** **embEDUx** needs at least one *uboot* branch and a
*platform* branch. The branches need to follow a certain name schema:

* U-Boot branch: \<uboot\_version> (eg. 2015.01-rc1)
* Platform branch: \<uboot\_version>\_\<platform\_name\> (eg. 2015.01-rc1_raspberry-pi)

**Importan: The platform\_name must not contain any underscores, use dashes
instead!**

## uboot branch
The uboot branch will contain the platform independent files, which in this case
are the uboot sources and the build script to build the uboot image.

Use this [template](usage/uboot/template/uboot_build) to add a new **U-Boot**
version to the *uboot* repository. Modify *UBOOT\_FILE* to the desired uboot
version archive (eg. u-boot-2015.01-rc1.tar.bz2). The archive name can be
obtained from [ftp.denx.de](http://ftp.denx.de/pub/u-boot/).

```bash
...
UBOOT_URL="http://ftp.denx.de/pub/u-boot"
UBOOT_FILE="<uboot_filename>"
...
```

## Platform branch 
The *platform* branch only contains the build script ***build***. This build
script needs to be modified to build the desired uboot version. Use this
[template](usage/uboot/template/platform_build) to add a new platform to the
*uboot* repository.

Only *UBOOT\_VERSION*, *UBOOT\_CONFIG* and eventually *FIRMWARE\_IMG* need to be
modified. 

```
...
UBOOT_VERSION="<uboot_version>"
UBOOT_CONFIG="<def_config>"
...
FIRMWARE_IMG="u-boot.bin"
...
```

There are also some rare cases, where the user might want to proceed
certain steps before or after the output is created. In this case the user can
define the function pre\_output() or post\_output().

* pre\_output(): Will be executed before the output is packed.
* post\_output(): Will be executed after the output was packed.

### Environment variables
With a local installed cross toolchain and an exising *uboot* branch in the
repository it is possible to test the *platform* build script locally. In order
to work, following environment variables need to be set.
* Target architecture:
  ARCH= (eg. 'arm')
* Path to the cross toolchain:
  CROSS_COMPILE= (eg.'armv6j-ctng-linux-gnueabi/bin/armv6j-ctng-linux-gnueabi-')
* Path where **embEDUx** should store its files:
  EMBEDUX_TMP= (eg. '/var/tmp/embedux/download/'

## Usage example 
In the following example a new 2015.01 **U-Boot** and the raspberry-pi platform
for that **U-Boot** will be added to the *uboot* repository. 

### Add new U-Boot
The following steps are necessary before you can [add](#add-new-platform) a
*plaform* for the desired **U-Boot** version to the repository.

1. Clone the *uboot* repository with the URL provided by your system
   administrator.
   ```
   $ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
   ```

1. Add a *uboot* branch named like the **U-Boot** version to the *uboot*
   repository.
   ```
   $ git checkout master
   $ git branch 2015.01
   $ git checkout 2015.01
   $ touch README.md
   $ git add README.md
   $ git commit -m "inital commit"
   $ git push --set-upstream origin 2015.01
   ```

1. Add the [template](usage/uboot/template/uboot_build) as ***build*** to the
   repository and make it executable.
   ```
   $ ls -hl
   total 4.0K
   -rwxr-xr-x 1 user user 1.1K Mar  2 18:49 build
   -rw-r--r-- 1 user user    0 Mar  2 18:48 README
   ```

1. Modify *UBOOT\_FILE* in the ***build*** script, to match the desired
   **U-Boot** version.
   ```
   ...
   UBOOT_FILE="u-boot-2015.01.tar.bz2"
   ...
   ```

1. Add the changed files, commit and push. 
   ```
   $ git add build
   $ git commit -m "new uboot"
   $ git push 
   ```

The build script in the corresponding *platform* branch can now use the just
created *uboot* branch.

### Add new platform
This step requires an [existing](#add-new-kernel) *uboot* branch.

1. If not already done, clone the *uboot* repository with the URL provided by
   your system administrator.
   ```
   $ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
   ```

1. Add a *platform* branch named *\<uboot-version\>\_\<platform\>* to the
   *uboot* repository.  It is necessary that you push this initial branch, so
   **embEDUx** can start building your **U-Boot** image after the last step of
   this example.
   ```
   $ git checkout master
   $ git branch 2015.01_raspberry-pi
   $ git checkout 2015.01_raspberry-pi
   $ touch README.md
   $ git add README.md
   $ git commit -m "inital commit"
   $ git push --set-upstream origin 2015.01_raspberry-pi
   ```

1. Add the [template](usage/uboot/template/platform_build) as ***build*** to the
   repository and make it executable. 
   ```
   $ ls -hl
   total 4.0K
   -rwxr-xr-x 1 user user 431 Mar  2 18:59 build
   -rw-r--r-- 1 user user   0 Mar  2 18:57 README
   ```

1. Modify *UBOOT\_VERSION* in ***build*** to the desired version, which is also
   the name of the *uboot* branch. Also modify *UBOOT\_CONFIG* to the platform
   configuration for **U-Boot**. If needed also modify the *FIRMWARE\_IMG*.
   ```
   UBOOT_VERSION="2015.01"
   UBOOT_CONFIG="rpi_config"
   ...
   FIRMWARE_IMG="u-boot.bin"
   ```

1. Optional: Add pre_output or post_output functions to the ***build*** script.

1. Add all files, commit  and push branch upstream.
   ```
   $ git add build
   $ git commit -m "new platform"
   $ git push
   ```

1. The **buildbot** should start building your **U-Boot** now. You can follow the
   build process on the **buildbot** website.
   ![Buildbot done](img/buildbot_done.png)

1. Congratulations, you just built your first **U-Boot** for your first
   platform.  You can use the [flashtool](usage/flashtool/README.md) to flash
   the **U-Boot** image to your platform device.


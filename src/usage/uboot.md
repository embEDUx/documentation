# U-Boot
This guide will help you through the steps to build a **U-Boot** image for
your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/user-documentation.md).

* Git Repository *uboot*
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

* U-Boot branch: <uboot-version\> (eg. 2015.01-rc1)
* Platform branch: <uboot-version\>\_<platform-name\> (eg. 2015.01-rc1_raspberry-pi)

Please look up the Platform string in the [User
Documentation](../setup/user-documentation.md) provided by your administrator. If
your platform doesn't exist yet, please contact your administrator.

### Add new upstream U-Boot
The following steps are necessary before you can add [a new
platform](#add-new-platform-for-u-boot-version) to the repository. The following
example will add the **U-Boot** 2015.01 for the raspberry pi. The source code
archive can be found at the [U-Boot website](http://ftp.denx.de/pub/u-boot/).

1. Clone the *linux* repository with the URL provided in the user documentation.
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

1. Add the [default script](usage/uboot/template/uboot_build) as ***build*** to the
   repository and make it executable.
   
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 1.1K Mar  2 18:49 build
-rw-r--r-- 1 user user    0 Mar  2 18:48 README
    ```

1. Modify *UBOOT\_FILE* in the ***build*** script, to match the **U-Boot**
   archive for the desired version. If you use the default build script, make
   sure the file exists on the [webserver](http://ftp.denx.de/pub/u-boot/).
   
    ```
...
UBOOT_FILE="u-boot-2015.01.tar.bz2"
...
    ```

1. Add the changed files, commit and push upstream.
   
    ```
$ git add build
$ git commit -m "new uboot 2015.01"
$ git push 
    ```

Now you can continue and add *platform* branches to the *uboot* repository.

### Add new platform for U-Boot version
This step requires an [existing](#add-new-upstream-u-boot) *uboot* branch for
the desired **U-Boot** version.

1. If not already done, clone the *linux* repository with the URL provided in
   the user documentation.
   
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
    ```

1. Add a *platform* branch named *<uboot-version\>\_<platform-string\>* to the *uboot*
   repository.  It is necessary that you push this initial branch, so the
   **Buildbot** can start building your **U-Boot** image after last step of this
   example.
   
    ```
$ git checkout master
$ git branch 2015.01_raspberry-pi
$ git checkout 2015.01_raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 2015.01_raspberry-pi
    ```

1. Add the [default build script](usage/uboot/template/platform_build) as
   ***build*** to the branch and make it executable. 
    
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 431 Mar  2 18:59 build
-rw-r--r-- 1 user user   0 Mar  2 18:57 README
    ```

1. Modify *UBOOT\_VERSION* in ***build*** to the desired version, which is also
   the name of the *uboot* branch you created in the previous chapter. Also
   modify *UBOOT\_CONFIG* to the platform configuration for **U-Boot**. In this
   case we expect a default configuration for you platform within the **U-Boot**
   source. If this isn't the case, please read furhter informations at
   [background/uboot](../background/uboot.md). If needed also modify the
   *FIRMWARE\_IMG* to the format that your platform expects, or add more files
   if for example your platform needs also the second stage bootloader binary.
   
    ```
...
UBOOT_VERSION="2015.01"
UBOOT_CONFIG="rpi_config"
...
FIRMWARE_IMG="u-boot.bin"
...
    ```

1. Optional: Add pre\_output or post\_output functions to the ***build***
   script. They will be called before and after the output is packed. For
   further information check [background/uboot](../background/uboot.md) or have
   a look at the [default build script](template/platform_build).

1. Add all files, commit and push the changes upstream.
   
    ```
$ git add build
$ git commit -m "new platform"
$ git push
    ```

1. The **Buildserver** should start building your **U-Boot** image now. For
   further informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first **U-Boot** for your first
   platform.
  
   ** Be aware that you might still need some necessary files on your boot and
   root partition to boot your system successfully. See [misc](misc.md) for the
   necessary steps.**
   
   If you have a [linux](linux.md), a [rootfs](rootfs.md) and the
   necessary [misc](misc.md) files, you can flash everything with the
   **Flashtool** or deploy your files manually (see [Hardware
   Deployment](usage.md#hardware-deployment)).

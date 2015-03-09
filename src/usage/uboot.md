# U-Boot
This guide will help you through the steps to build a **U-Boot** image for
your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.
    * At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/post-install/user-documentation.md).
    * Your platform needs to be included in the [User
      Documentation](../setup/post-install/user-documentation.md), if that isn't
      the case, please contact an Administrator to add your platform to the
      **embEDUx** build system.
* Git Repository *uboot*
* **Buildserver** setup for desired platform architecture

### Suggestions
* Build/download a toolchain. This will allow you to test your build
  configuration locally before you push it upstream. For further information
  have a look at [Local Testing](../troubleshooting/local-testing.md).

* Have a look at the default build scripts
  ([generic](usage/uboot/default/generic_build),
  [platform](usage/uboot/default/platform_build)). As the **buildserver** just
  executes these scripts, you have no limits on what you want to do before,
  during and after the build process.

## Branch Name-Scheme
The **builserver** can only build your images, if you follow the correct
name-scheme for the branches.

The variables that are needed for your platform can be found in the [User
Documentation](../setup/post-install/user-documentation.md).

### Variables

Variable | Notes
--- | ---
Platform-String | Specified and mapped to the target architecture by the Administrator. Found in the [User Documentation](../setup/post-install/user-documentation.md)
Uboot-Version | The **U-Boot** version

### Branches
To avoid unnecessary redundancy, which will naturally occur if you build
multiple platforms for the same kernel version, following branch structure is
necessary. The default build scripts
([generic](usage/uboot/default/generic_build),
[platform](usage/uboot/default/platform_build)) follow exactly this idea.

Branch | Dependency | Task
--- | --- | ---
version\_generic | platform independent | Provide **U-Boot** sources
version\_platform | platform dependent | Call build script in version\_generic branch

For each **U-Boot** version, there will be exactly one *version\_generic* branch,
where for each platform there will be one *version\_platform* branch. Following
name-scheme has to be followed.

Branch | Scheme | Example
--- | --- | ---
version\_generic | < uboot-version \> | 2015.01
version\_platform | < uboot-version \>\_< platform-string \> |  2015.01\_raspberry-pi

[![Example U-Boot
Repository](usage/uboot/img/example_uboot_repository.png)](usage/uboot/img/example_uboot_repository.png)

## Step-by-Step Example
The following example will give you a detailed overview of the necessary steps
to build **U-Boot** 2015.01 for the raspberry pi. We assume that at this point the
*uboot* repository is empty.

## Add new upstream U-Boot
Before you can add [a new platform](#add-new-platform), for which you want to
build a **U-Boot** image, you first need to add a *version\_generic* branch to
the *uboot* repository.

1. Clone the *uboot* repository with the URL provided in the user documentation.

    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
    ```

1. Add a *version\_platform* branch to the *uboot* repository.
  
    ```
$ git checkout master
$ git branch 2015.01
$ git checkout 2015.01
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 2015.01
    ```

1. Add the [default script](usage/uboot/default/generic_build) as ***build*** to the
   branch and make it executable.
   
    ```
$ ls -hl
    ```

        total 4.0K
        -rwxr-xr-x 1 user user 1.1K Mar  2 18:49 build
        -rw-r--r-- 1 user user    0 Mar  2 18:48 README

1. Modify *<uboot-file \>* in the ***build*** script, to match the **U-Boot**
   archive for the desired version. If you use the default build script, make
   sure the file exists on the [ftp server](http://ftp.denx.de/pub/u-boot/).
   
        ...
        UBOOT_FILE="u-boot-2015.01.tar.bz2"
        ...

1. Before you push your changes upstream, make sure the build script is running
   without any errors. If you need help, have a look at
   [Local Testing](../troubleshooting/local-testing.md)

1. Add your changes, commit and push them upstream.
   
    ```
$ git add build
$ git commit -m "new uboot 2015.01"
$ git push 
    ```

Now that you have a *version\_generic* branch for your desired **U-Boot**
version within your *uboot* repository, the next step is to add a
*version\_platform* branch.

## Add new platform
This step requires an existing [*version\_generic*](#add-new-upstream-u-boot) branch for
the desired **U-Boot** version, you want to add a platform.

1. If not already done, clone the *uboot* repository with the URL provided in
   the user documentation.
   
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
    ```

1. Add a *version\_platform* branch to the *uboot* repository.  It is necessary
   that you push the branch at this point upstream, so the **buildserver** can
   find this new *version\_platform* branch.
   
    ```
$ git checkout master
$ git branch 2015.01_raspberry-pi
$ git checkout 2015.01_raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin 2015.01_raspberry-pi
    ```

1. Add the [default build script](usage/uboot/default/platform_build) as
   ***build*** to the branch and make it executable. 
    
    ```
$ ls -hl
    ```

        total 4.0K
        -rwxr-xr-x 1 user user 431 Mar  2 18:59 build
        -rw-r--r-- 1 user user   0 Mar  2 18:57 README

1. Modify *< uboot-version \>* to thhe desired *version\_generic* branch. Then
   modify *< def-config \>* to the platform configuration for **U-Boot**. In
   this case we expect a default configuration for you platform within the
   **U-Boot** source. If this isn't the case, please read further informations
   at [background/uboot](../background/specs/uboot.md).    

        ...
        UBOOT_VERSION="2015.01"
        UBOOT_CONFIG="rpi_config"
        ...
        FIRMWARE_IMG="u-boot.bin"
        ...

1. Optional: Add pre\_output or post\_output functions to the ***build***
   script. They will be called before and after the output is packed. For
   further information check [background/specs/uboot](../background/specs/uboot.md) or have
   a look at the [default build script](usage/uboot/default/platform_build).

1. Before you push your changes upstream, make sure the build script is running
   without any errors. If you need help, have a look at
   [Local Testing](../troubleshooting/local-testing.md)

1. Add all changes, commit and push them upstream.
   
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
  
   **Be aware that you might still need some necessary files on your boot and
   root partition to boot your system successfully. See [misc](misc.md) for the
   necessary steps.**
   
   If you have a [linux](linux.md), a [rootfs](rootfs.md) and the
   necessary [misc](misc.md) files, you can flash everything with the
   **Flashtool** or deploy your files manually (see [Hardware
   Deployment](usage.md#hardware-deployment)).

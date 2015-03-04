# Miscellaneous files
This guide will help you through the steps to build archives, containing the
files for your boot and root partition of your desired platform.

The misc repository is necessary because in platforms require some files that
need to be present in the root or boot partition. However these file cant be
strictly assigned logically  to the *rootfs*,*linux* or *uboot* repository.

Two mandatory files are, which are always needed are:

* boot.scr: This boot script is required for **U-Boot** and needs to go on the
  boot partition.
* inittab: This file is required by the operating system and needs to go on the
  root partition.

The files have to be stored within the folder ***src_boot*** and ***src_root***
and **within their folder structure**, so that the [default build
script](usage/misc/files/build) can pack them in the required structure within
an archive.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/user-documentation.md).

* Git Repository *misc*
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

* <platform-string\>

Please look up the platform string in the [User
Documentation](../setup/user-documentation) provided by your administrator. If
your platform doesn't exist yet, please contact your administrator.

## Add new platform
To add a new platform following steps are required. As an example we will add
the raspberry pi platform to the *misc* repository.

1. Clone the *linux* repository with the URL provided in the user documentation.

    ```
$ git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
    ```

1. Add a new *platform* branch to the *misc* repository and push it upstream.
   This last step is required, so the **Buildbot** can start the build process
   at the end of this example.
   
    ```
$ git checkout master
$ git branch raspberry-pi
$ git checkout raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin raspberry-pi 
    ```

1. Add the [default build script](usage/misc/files/build) to your *platform* branch and
   make it executable.
   
    ```
$ ls -hl
total 8.0K
-rwxr-xr-x 1 user user 939 Mar  2 19:35 build
-rw-r--r-- 1 user user   1 Mar  2 19:33 README.md
    ```

1. Add at least these two files and modify them to fit to to your platform.
   
    ```
$ mkdir src_boot
$ touch src_boot/boot.scr.txt
$ mkdir src_root
$ mkdir src_root/etc/
$ touch src_root/etc/inittab
    ```

1. The raspberry pi also needs some
   [firmware](https://github.com/raspberrypi/firmware) blobs, present at boot,
   so we simply add these files to the *platform* branch in the *misc*
   repository.
    
    ```
$ ls -hl src_boot/
total 6.6M
-rw-r--r-- 1 user user  18K Mar  2 19:53 bootcode.bin
-rw-r--r-- 1 user user  307 Mar  2 19:53 boot.scr.txt
-rw-r--r-- 1 user user   18 Mar  2 19:53 config.txt
-rw-r--r-- 1 user user  19K Mar  2 19:53 COPYING.linux
-rw-r--r-- 1 user user 2.3K Mar  2 19:53 fixup_cd.dat
-rw-r--r-- 1 user user 6.0K Mar  2 19:53 fixup.dat
-rw-r--r-- 1 user user 9.0K Mar  2 19:53 fixup_x.dat
-rw-r--r-- 1 user user 1.5K Mar  2 19:53 LICENCE.broadcom
-rw-r--r-- 1 user user 525K Mar  2 19:53 start_cd.elf
-rw-r--r-- 1 user user 2.5M Mar  2 19:53 start.elf
-rw-r--r-- 1 user user 3.5M Mar  2 19:53 start_x.elf
    ```

1. Add all files to the repository, commit and push upstream.
   
    ```
$ git add build
$ git add src_boot
$ git add src_root
$ git commit -m "new platform"
$ git push
    ```

1. The **Buildserver** should start building your misc image now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first kernel for your first platform. If
   you have a [linux](linux.md), a [uboot](uboot.md) and a [rootfs](rootfs.md)
   you can flash everything with the **Flashtool** or deploy your files manually
   (see [Hardware Deployment](usage.md#hardware-deployment)).


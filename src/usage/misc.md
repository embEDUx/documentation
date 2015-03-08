# Miscellaneous files
This guide will help you through the steps to build archives, containing the
files for your boot and root partition of your desired platform.

If you wonder why you would even need this repository, please consider having a
look at [background/misc](../background/specs/misc.md).

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/post-install/user-documentation.md).

* Git Repository *misc*
* **buildserver** setup for desired platform architecture
* Required Software
    * wget
    * tar

### Suggestions
* Have a look at the default [build script](usage/misc/default/platform_build). As the
  **buildserver** just executes this script, you have no limits on what you want
  to do before, during and after the build process.

## Branch Name-Scheme
The **builserver** can only build your images, if you follow the correct
name-scheme for the branches.

The variables that are needed for your platform can be found in the [User
Documentation](../setup/post-install/user-documentation.md).

### Variables

Variable | Notes
--- | ---
Platform-String | Specified and mapped to the target architecture by the Administrator. Found in the [User Documentation](../setup/post-install/user-documentation.md)

### Branches

Branch | Scheme | Example
--- | --- | ---
platform | < platform-string \> |  raspberry-pi

### Side note
Two mandatory files, which are always needed are:

File | Folder | Notes
--- | --- | ---
boot.scr.txt | src\_boot | Script for **U-Boot** boot sequence ([source](http://www.denx.de/wiki/view/DULG/UBootScripts))
inittab | src\_root/etc | Describes which processes are started at boot ([source](http://unixhelp.ed.ac.uk/CGI/man-cgi?inittab+5))

**Store the files within their desired folder structure. Eg. *inittab* has to be
in */etc* at the root partition**

For deeper insight have a look at the [default build
script](usage/misc/default/platform_build).

### Step-by-Step Example
The following example will give you a detailed overview of the necessary steps
to build the misc files for the raspberry pi. We assume that at this point the
*misc* repository is empty.

## Add new platform

1. Clone the *misc* repository with the URL provided in the user documentation.

    ```
$ git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
    ```

1. Add a *platform* branch to the *misc* repository. It is necessary that you
   push the branch at this point upstream, so the **buildserver** can find the
   new *platform* branch.
   
    ```
$ git checkout master
$ git branch raspberry-pi
$ git checkout raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin raspberry-pi 
    ```

1. Add the [default build script](usage/misc/default/platform_build) as
   ***build*** to the branch and make it executable.
   
    ```
$ ls -hl
total 8.0K
-rwxr-xr-x 1 user user 939 Mar  2 19:35 build
-rw-r--r-- 1 user user   1 Mar  2 19:33 README.md
    ```

1. As described in [background/misc](../background/specs/misc.md) we need at least
   *boot.scr.txt* and *inittab* in this repository. So we prepare these files
   for the raspberry pi (example:
     [boot.scr.txt](usage/misc/default/boot.scr.txt),
     [inittab](usage/misc/default/inittab) and add them to the branch. 
   
    ```
$ mkdir src_boot
$ touch src_boot/boot.scr.txt
$ vim src_boot/boot.scr.txt
$ mkdir src_root
$ mkdir src_root/etc/
$ touch src_root/etc/inittab
$ vim src_root/inittab
    ```

1. The raspberry pi also needs some
   [firmware](https://github.com/raspberrypi/firmware/tree/master/boot) files present at boot,
   so we simply add these files to the *src_boot* folder.
    
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

1. Before you push your changes upstream, make sure your build script is running
   without any errors!

1. Add the changes, commit and push them upstream. 
   
    ```
$ git add build
$ git add src_boot
$ git add src_root
$ git commit -m "new platform"
$ git push
    ```

1. The **buildserver** should start building your misc files now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first misc files for your first
   platform. If you have a [linux](linux.md), a [uboot](uboot.md) and a
   [rootfs](rootfs.md), you can flash everything with the **Flashtool** or
   deploy your files manually (see [Hardware
   Deployment](usage.md#hardware-deployment)).


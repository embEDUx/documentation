# Miscellaneous files
The misc repository was needed because in some situations we need some files
present in the root or boot partition, that don't belong in the *rootfs*,
*linux* or *uboot* repository.

Two mandatory files are:
* boot.scr: This boot script is required for **U-Boot** and needs to go on the
  boot partition.
* inittab: This file is required by the operating system and needs to go on the
  root partition.

The files have to be stored in the folder ***src_boot*** and ***src_root*** and
**within their folder structure**, so that the [build](usage/misc/files/build)
script can pack them in the required archives.

## Name schema
The branches have to be named for the platform they are meant for.

* <platform\_name\>

**Important: The <platform\_name\> can not contain any underscores, use dashes
instead.**

## Add new platform
To add a new platform following steps are required. Don't forget the mandatory
files!

1. Clone the *misc* repository with the URL that was provided by your system
   administrator.
   ```
$ git@apu.in.htwg-konstanz.de:labworks-embEDUx/uboot.git
   ```

1. Add new *platform* branch to the *misc* repository and push it upstream.
This last step is required, so the **Buildbot** can pack and deploy the misc
files at the end of this example.
   ```
$ git checkout master
$ git branch raspberry-pi
$ git checkout raspberry-pi
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin raspberry-pi 
   ```

1. Add the [build](usage/misc/files/build) script to your *platform* repository
and make it executable.
   ```
$ ls -hl
total 8.0K
-rwxr-xr-x 1 user user 939 Mar  2 19:35 build
-rw-r--r-- 1 user user   1 Mar  2 19:33 README.md
   ```

1. Add at least these two files and modify them to fit to the platform.
   ```
$ mkdir src_boot
$ touch src_boot/boot.scr.txt
$ mkdir src_root
$ mkdir src_root/etc/
$ touch src_root/etc/inittab
   ```

1. The raspberry pi also needs some firmware blobs to boot, which need to be
   placed in the boot partition, so we simply add these files to the *misc*
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

1. Add all files to the repository, commit and push.
   ```
$ git add build
$ git add src_boot
$ git add src_root
$ git commit -m "new platform"
$ git push
   ```

1. The **Buildbot** will now execute the build script and provide the output on
   the website. You can flash the output with the [flashtool](flashtool.md).

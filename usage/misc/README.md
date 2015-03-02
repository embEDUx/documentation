# Misc

The misc repository was needed because in some situations we need some files
present in the root or boot partition, that don't belong in the *rootfs*,
*linux* or *uboot* repository.

Each branch contains the files needed for the boot and root partition. Those can
be for example the ***boot.scr*** for **U-Boot**, or the ***inittab*** for the rootfs. To pack these files in a smart way, this branch also has to contain this [build](usage/misc/files/build) script.

## Name schema
The branches have to be named for the platform they are meant for.
* \<platform\_name\>

**Important: The \<platform\_name\> can not contain any underscores, use dashes
instead.**

## Add new platform

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
   -rwxr-xr-x 1 lars lars 939 Mar  2 19:35 build
   -rw-r--r-- 1 lars lars   1 Mar  2 19:33 README.md
   ```

1. Add at least these two files and modify them to fit to the platform.
   ```
   $ mkdir src_boot
   $ mkdir src_root
   $ touch src_boot/boot.scr.txt
   $ touch src_root/inittab
   # Edit files
   ```

1. Add all files to the repository, commit and push.
   ```
   $ git add build
   $ git add src_boot
   $ git add src_root
   $ git commit -m "new platform"
   $ git push
   ```

1. The **Buildbot** will now execute the build script and provide the output on the website. You can flash the output with the [flashtool](usage/flashtool/README.md).

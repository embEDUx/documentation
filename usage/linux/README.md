# Linux
To create a Linux kernel **embEDUx** needs at least a *kernel* branch and a
*platform* branch. The branches need to have the following name scheme:

* Kernel branch: \<kernel\_version> (eg. 3.17.2)
* Platform branch: \<kernel\_version>\_\<platform\_name\> (eg. 3.17.2_raspberry-pi)

**Importan: The platform\_name must not contain an underscore, use a dash
instead!**


## Kernel branch
The *kernel* branch will provide all the platform independent files, which are
the kernel sources, the Gentoo patches and the build script to patch and build
the kernel. Multiple platforms use the same *kernel* branch for the same kernel
version. 

Following [template](template/kernel-build) should be used as a build script:

```bash
...
### Sources
KERNEL_URL="http://www.kernel.org/pub/linux/kernel/v3.x"
KERNEL_FILE="linux-<Major>.<Minor>.tar.gz"
...
PATCH_VERSION="<Major>.<Minor>-<Subminor>"
...
```

The user only needs to change *KERNEL_URL*, *KERNEL_FILE* and *PATCH_VERSION* to
fit to the desired kernel version. The *KERNEL_URL* and the *KERNEL_FILE* can be
obtained from [www.kernel.org](https://www.kernel.org/). The *PATCH_VERSION* for
the desired kernel version can be obtained from
[dev.gentoo.org](https://dev.gentoo.org/~mpagano/genpatches/tarballs/).

**Important: Because Gentoo patches are needed, the user has to check which base
version of the kernel sources was used for patches. Most of the time it is the
*\<Major\>.\<Minor\>* version (eg. 3.17, 3.18, 3.19). The Gentoo patches don't
strictly follow the kernel version, which can lead to the situation, that Gentoo
patches 3.18.8 result in the linux kernel version 3.18.7.**

## Platform branch
The *platform* branch has to contain all platform dependent informations and a
build script. Those are a valid kernel configuration, the build script and any
needed user patches.

Following [template](template/platform-build) should be used as build script:

```
KERNEL_VERSION="<kernel_version>"
...
KERNEL_DTB="<platform_dtb>"
KERNEL_CONFIG=".config"
KERNEL_IMG="zImage"
...
```

The build script clones the *kernel* branch and executes the prepare and build
function. As long as the user sticks to the standard name scheme, the user only
needs to replace the *kernel_version*, which has to be the *kernel* branch name
and the *platform_dtb*, which is the device tree blob that should be created
for the platform during the build.

**Important: The sources for the *platform\_dtb* have to be present in the kernel
sources, or otherwise added by a user patch.**

### User patches
Any files that need to be added to the kernel sources need to be in the root
folder of the *platform* branch and follow the format and naming scheme of a
patch.

### Environment variables
With a local installed cross toolchain and an exising *kernel* branch in the
repository it is possible to test the *platform* build script locally. In order
to work, following environment variables need to be set.
* Target architecture:
  ARCH=
* Path to the cross toolchain:
  CROSS_COMPILE=
* Path where **embEDUx** should store its files:
  EMBEDUX_TMP=

## Usage example 
In the following example we will add a new 3.18.7 kernel to the *linux*
repository. Then we will add the platform raspberry-pi for the 3.18.7 kernel to
the repository.

### Add new kernel branch
Following steps are necessary to get *platform* build working.

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
   script.
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
This step requires an existing *kernel* branch.

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

1. Modify *KERNEL\_URL*, *KERNEL\_FILE*, and *PATCH\_VERSION* in the ***build***
   script.
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

Congratulations, you just built your first kernel for your first platform.


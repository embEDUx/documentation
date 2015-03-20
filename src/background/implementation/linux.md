# Implementation For Building Linux
The [design](../design/linux.md) and the
[evaluation](../evaluation/linux.md) result in the following implementation.

## Repository
* The repository is called *linux-specs*
* Each platform/version combination gets its own branch, which will be referred
  as *version\_platform* branch 
* Each version has also one branch, which will be referred as *version\_generic*
  branch. 

[![Repository](usage/linux/img/example_linux_repository.png)](usage/linux/img/example_linux_repository.png)

**Important**: Each *version\_platform* branch depends strongly on a
*version\_generic* branch.

### version\_generic
This branch exists exactly one time per **Linux** version. It contains the
script, that downloads the sources for the version it is designed for. For
obliterating the redundancy throughout the different platforms, it also
implements the whole build process.

With the decision to use **Gentoo** as RootFS, applying the **Gentoo** specific
patches to the **Linux** kernel is also necessary. Therefore these patches have
to be downloaded and applied during the build process.

#### Build Steps
1. Download sources
1. Extract sources
1. Download **Gentoo** patches
1. Extract **Gentoo** patches
1. Apply **Gentoo** patches
1. If provided in *version\_platform* branch, apply user patches
1. Build **Linux**
1. Provide Output in archives
    * Files for boot partition (kernel, dtb)
    * Files for root partition (modules, kernel sources)

#### Build Script
The following build script reflects the build steps.

* [version\_generic](usage/linux/default/generic_build)

### version\_platform
This branch exists for each platform as many times as different version of
**Linux** should be built. It contains a build script, which will do the
following: 

#### Build Steps
1. Checkout the needed *version\_generic* branch
1. Set necessary parameter e.g. configuration
1. Execute the script from the *version\_generic branch*

#### Build Script
The following build script reflects the build steps.

* [version\_platform](usage/linux/default/platform_build)


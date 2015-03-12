# Evaluation Linux 
The considerations from the [design](../design/linux.md) will be evaluated
within this chapter.

## Repository
The branch system of **Git** to fulfills our needs to keep distinct versions of
the specifications for each platform and **Linux** version within one
repository. 

### Content
The repository has to contain the kernel configuration, the build script, and
all the required patches. The build script has to apply the provided patches
during the build process.

## Build process 
Due to keeping the possibility to build the kernel locally, emerging the kernel
sources with OS dependent tools (e.g. emerge with **Gentoo**) is not a viable
solution. As already mentioned in the [u-boot evaluation](uboot.md), keeping the
sources within the **Linux** repository will lead to a lot of overhead when the
same **Linux** versions should be build for different platforms, as they use the
same kernel sources. The same solution as already described in the [u-boot
evaluation](uboot.md) will be used.

Together with abusing the branch structure of **Git** the following structure of
the repository can be achieved.

Each **Linux** version has a branch, which contains a script that downloads the
specific sources. Each platform has a branch for each **Linux** version that
should be build, containing a script, that executes the download script from the
**Linux** version branch.

![Structure](background/evaluation/img/eval_linux.png)



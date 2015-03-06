# Usage Documentation
This document will give you pointers at anything you need to know for building
and deploying the various products for a specific platform.

## Prerequisites
The following requirements are common to the build procedures of all products.
Please make sure that you and your systems fulfill the given requirements before
proceeding to the actual build instructions.

### Local Software
* Git is needed to download and submit build specifications.
* $EDITOR - to specify the builds you will need your favorite text editor.

### Successful Setup
A successful [setup of the buildserver](../setup/setup.md) is a definite
requirement, since it includes setting up the repositories that are used by
users to supply the build instructions to the *buildserver*.

### User Documentation
At the end of the setup, the Administrator is instructed to create the
[User Documentation](../setup/user-documentation.md). This information will be
needed to use the buildserver.


#### Git-Repositories
For every product you want to build, it's necessary to have a local copy of the
correspdonding Git-repository. The URLs are available in the aforementioned User
Documentation. The detailed product build instructions will guide you in finding
the needed repository.

## Suggestions
* Git practice! You will deal with and handful of repositories and their
  branches on the way of managing builds for your systems.
* Have a glimpse at the [background documentation](../background/background.md)
  to understand why your are instructed to do so. In case you don't, you  might
  miss potential functionality or the potential to help yourself in case of
  problems.


## Build Instructions
1. Open **your** User Documentation

1. Acquire the repository URL for the product you want to build.

1. Make sure you have the latest repository content. Run `git clone` for a fresh
   start or `git pull` for an existing repository

1. At this point you may re-use an existing branch, work on an existing branch,
   or create a new branch. Now, there are at least these two cases:
    * Creating a new **new branch**: Run `git checkout < template_branch >`,
      where < template_branch \>* is the branch you want yours to base on. Right
      away run `git checkout -b < new_branch >` and `git push --set-upstream
      origin < new_branch \>`. Afterwards, the buildserver will watch for
      changes on the new branch.
    * Modifying an **existing branch**:
        simply `git checkout < existing_branch >`
      
      When needed, you can find more detailed instructions in the product
      sections.

1. **Specify your build.** Since the build specifications are very different for
   each product, it's necessary to separate the instructions into distinct
   sections. Please follow the instructions given in the detailed sections:
    * [U-Boot](../usage/uboot.md)
    * [Toolchains](../usage/toolchains.md)
    * [Linux](../usage/linux.md)
    * [RootFS](../usage/rootfs.md)
    * [Miscellaneous files](../usage/misc.md)

       The work flow is basically the same for every product. One major
       difference in workflow occurs when building a RootFS. You will not be
       able to test the build locally before submitting your specification to
       the buildserver. The reason is the complex system that is needed to
       assemble a RootFS. More information will follow in the [detailed section
       for building the RootFS](../usage/rootfs.md).  For every other product,
       toolchains and instructions are provided to quickly setup and test the
       builds locally.


1. Run `git add` and `git commit` according to your changes. Please use **sane
   commit messages** to improve collaboration. The buildserver will pick up your
   changes, schedule a build and execute it as soon as it can.

1. Finally, run `git push` to upload your specification to the buildserver!

## Monitor your builds
In order to see the state of your running build, and also to check if it has
been scheduled correctly, you can [monitor the builds using the
web-interface](../usage/common/build-monitoring.md).

In case of a build failure please either

1. contact the Administrator and provide the Link to your failed build job if
you need support,

1. or fix the specification and commit them again


## Hardware Deployment
After the required build have successfully completed you can finally deploy the
products to your hardware.

### Flashtool 
You can [deploy your builds to hardware in a semi-automated manner using the
flashtool](../usage/flashtool.md). Please note that to deploy a complete system,
successful builds of all products need to be available.  This means, single
products can be built and deployed if there are previous successful builds for
the target platform.

### Manually
If for some reason the flashtool is not working for you, there is always the
possibility to deploy the products manually. Retrieve the *Product Download
URLs* from the [User Documentation](#User Documentation), or from the
*Buildmaster Web-Interface*, where they are listed at the last build step for
every successful job.  From there, you can download the files produced by the
builds. The rest depends strongly on your platform, and it is not possible to
provide a generic way that will possibly work for all platforms available on the
free market. 

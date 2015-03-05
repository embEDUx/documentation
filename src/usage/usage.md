# Usage Documentation
This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Prerequisites
The following requirements are common to the build procedures of all components.
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
You need to retrieve the Git-repository for every component you want to build.
The detailed component build instructions will guide you in finding the needed
repository.


## Suggestions
* Git practice! You will deal with and handful of repositories and their
  branches on the way of managing builds for your systems.
* Have a glimpse at the [background documentation](../background/background.md)
  to understand why your are instructed to do so. In case you don't, you  might
  miss potential functionality or the potential to help yourself in case of
  problems.


## Build Instructions
1. Open **your** User Documentation

1. Acquire the repository URL for the component you want to build. Therefore,
   see **your** user documentation.

1. Retrieve the latest repository content. Run `git clone` for a fresh start or
   `git pull` for an existing repository

1. At this point you may re-use an existing branch, work on an existing branch,
   or create a new branch. Further instructions are included on the detailed
   component sections.  Run `git checkout ` for the the branch of interest. This
   depends on the *component* and the *platform* you want to build for.  

1. **Specify your build.** Since the build specifications are very different for
   each component, it's necessary to separate the instructions into distinct
   sections. Please follow the instructions given in the detailed sections:
    * [U-Boot](../usage/uboot.md)
    * [Toolchains](../usage/toolchains.md)
    * [Linux](../usage/linux.md)
    * [RootFS](../usage/rootfs.md)
    * [Miscellaneous files](../usage/misc.md)

       The work flow is basically the same for every component. One major
       difference in workflow occurs when building a RootFS. You will not be
       able to test the build locally before submitting your specification to
       the buildserver. The reason is the complex system that is needed to
       assemble a RootFS. More information will follow in the detailed section
       for building the RootFS.  For every other component, toolchains and
       instructions are provided to quickly setup and test the builds locally.


1. Run `git add` and `git commit` according to your changes. Please use **sane
   commit messages** to improve collaboration. The buildserver will pick up your
   changes, schedule a build and execute it as soon as it can.

## Monitor your builds
In the meantime of your build, and also to check if it has been scheduled
correctly, you can [monitor the builds](../usage/common/build-monitoring.md).

In case of a build failure please either

1. contact the Administrator and provide the Link to your failed build job if
you need support,

1. or fix the specification and commit them again


## Hardware Deployment
### Flashtool
If your build succeeded you can continue to 
[deploy your builds to hardware using the flashtool](../usage/flashtool.md)

Please note that to deploy a complete system, successful builds of all
components need to be available.  This means, single components can be built and
deployed if there exists previous successful builds for the target platform.
After the required build have successfully completed you can finally 

### Manually
If for some reason the flashtool is not working for you, there is always the
possibility to deploy the components manually. Retrieve the *Component Download
URLs* from the [User Documentation](#User Documentation), or from the
*Buildmaster Web-Interface*, where they are listed at the last build step for
every successful job.  From there, you can download the files produced by the
builds. The rest depends strongly on your platform, and it is not possible to
provide a generic way that will possibly work for all platforms available on the
free market. 

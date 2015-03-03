# Usage Documentation
This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Prerequisites
The following requirements are common to the build procedures of all components.
Please make sure that you and your systems fulfill the given requirements before
proceeding to the actual build instructions.

#### Local Software
* Git is needed to download and submit build specifications

#### Successful Setup
A successful [setup of the buildserver](../setup/setup.md) is a definite
requirement, since it includes setting up the repositories that are used by
users to supply the build instructions to the *buildserver*.

#### User Documentation
At the end of the setup, the Administrator is instructed to create the
[User-Documentation](../setup/user-documentation.md#Repositories).

If you want to see an example, or you're a user at the HTWG please go to [User
Documentation at the HTWG](../setup/examples/user-documentation-HTWG.md) the
headline to obtain the information you need for the components you want to
build.

#### Git-Repositories
You need to retrieve the Git-repository for every component you want to build.
The detailed component build instructions will guide you in finding the needed
repository.


### Suggestions
* Git practice! You will deal with and handful of repositories and different
  on the way of managing builds for your systems.
* Have a glimpse at the [background documentation](../background/background.md)
  to understand why your are instructed to do so. In case you don't, you  might
  miss potential functionality or potential to help yourself in case of problems.


## Build Instructions

The work flow is basically all the same for every component. The only exception for
this is the RootFS, more information will follow in the detailed section.

1. Open the *User Documentation*  ([example HTWG-userdocs](../setup/examples/user-documentation-HTWG.md))

1. Acquire the repository URL for the component(s)

1. Run `git clone` for a fresh start or `git pull` for an existing repository

1. Run `git checkout` the branch of interest. This depends on the *component* and
   the *Platform* you want to build for

1. **Make changes. It is necessary to read the instructions for every
   component you want to build**
    * [U-Boot](../usage/uboot.md)
    * [Linux](../usage/linux.md)
    * [RootFS](../usage/rootfs.md)
    * [Miscellaneous files](../usage/misc.md)
    * [Toolchains](../usage/toolchains.md)

1. Run `git add` and `git commit` according to your changes. Please use **sane commit messages**
   to improve collaboration. The buildserver will pick up your changes, schedule
   a build and execute it as soon as it can.

## Monitor your builds
In the meantime of your build, and also to check if it has been scheduled
correctly, you can [monitor the builds](../usage/common/build-monitoring.md).

In case of a build failure please either

1. contact the Administrator and provide the Link to your failed build job if
you need support,

1. or fix the specification and commit them again


## Hardware Deployment
If your build succeeded you can continue to 
[deploy your builds to hardware using the flashtool](../usage/flashtool.md)

Please note that to deploy a complete system, successful builds of all
components need to be available.  This means, single components can be built and
deployed if there exists previous successful builds for the target platform.
After the required build have successfully completed you can finally 


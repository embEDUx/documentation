# Usage Documentation
This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Prerequisites
### Requirements

#### Local Software
* Git

#### Successful Setup
A successful [setup of the buildserver](../setup/setup.md) is a definite
requirement, since it includes setting up the repositories that are used by
users to supply the build instructions to the *buildserver*.

#### User Documentation
At the end of the setup, the Administrator is instructed to create the
[User-Documentation](../setup/user-documentation.md#Repositories).

#### [User Documentation at the HTWG](../setup/examples/user-documentation_htwg.md)
If you want to see an example, or you're a user at the HTWG, follow the link in
the headline to obtain the information you need for the component you want to build.

##### Git-Repositories
You need to retrieve the Git-repository for every component you want to build.


### Suggestions
* Git skills. You will deal with and handful of repositories and branching will
  be an important part of the work flow



## Build instructions
Triggering builds works by 

* [U-Boot](../usage/uboot.md)
* [Linux](../usage/linux.md)
* [RootFS](../usage/rootfs.md)
* [Miscellaneous files](../usage/misc.md)
* [Toolchains](../usage/toolchains.md)

## Monitoring instructions
While your builds are running, you might want to [monitor the build system on
the internal webserver](../usage/common/build-monitoring.md).

## Hardware Deployment
To deploy a complete system, successful builds of all components need to be
available.  This means, single components can be built and deployed if there
exists previous successful builds for the target platform. After the required
build have successfully completed you can finally [deploy to hardware using the
flashtool](../usage/flashtool.md)

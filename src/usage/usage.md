# Usage Documentation
This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Prerequisites
### Requirements
#### Successful Setup
A successful [Setup of the buildserver](../setup/setup.md) is a strong requirement, since
it includes setting up the repositories that are used by users to supply the
build instructions to the *buildserver*.

At the end of the setup, the Administrator is instructed to create the
[User-Documentation](../setup/user-documentation.md#Repositories).
For an example see ([user-documentation_htwg](../setup/examples/user-documentation_htwg.md))

* [Determine repositories](../usage/common/checkout-repositories.md)
* [Download repositories](../usage/common/checkout-repositories.md)

### Suggestions



## Build instructions
Triggering builds works by 

* [U-Boot](../usage/uboot.md)
* [Linux](../usage/linux.md)
* [RootFS](../usage/rootfs.md)
* [Miscellaneous files](../usage/misc.md)
* [Toolchains](../usage/toolchains.md)

## Monitoring instructions
While your builds are running, you might want to 
[monitor the build system on the internal
webserver](../usage/common/build-monitoring.md).

## Hardware Deployment
To deploy a complete system, successful of all components need to be available.
This means, single components can be built and deployed if there exists
previous successful builds for the target platform. After the required build
have successfully completed you can finally 
[deploy to hardware using the flashtool](../usage/flashtool.md)

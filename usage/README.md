This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Requirements
Before you can start heading over to the components sections, go through the
list of requirements and fulfill them if needed.

### Successful Setup
A successful [Setup of the buildserver](../setup) is a strong requirement, since
it includes setting up the repositories that are used by users to supply the
build instructions to the *buildserver*.

At the end of the setup, the Administrator is instructed to create the
[User-Documentation](setup/user-documentation.md/#Repositories). See the ([example setup @ HTWG](setup/examples/user-documentation.md))


* [Download repositories](common/checkout-repositories.md)
* [Determine repositories](common/checkout-repositories.md)

## Build instructions
Triggering builds works by 

* [U-Boot](uboot)
* [Linux](linux)
* [RootFS](roofs)
* [Miscellaneous files](misc)

## Monitoring instructions
While your builds are running, you might want to 
[monitor the build system on the internal
webserver](common/build-monitoring.md).

## Hardware Deployment
To deploy a complete system, successful of all components need to be available.
This means, single components can be built and deployed if there exists
previous successful builds for the target platform. After the required build
have successfully completed you can finally 
[deploy to hardware using the flashtool](flashtool)

### Change the root password

```bash
#!/bin/bash -ex
CHROOT_PATH=$(pwd)
sed -i '1d' ${CHROOT_PATH}/etc/shadow
echo root:$(python -c 'import crypt; print crypt.crypt("toor","$6$somesalt$")'):10770:0::::: >> ${CHROOT_PATH}/etc/shadow
```

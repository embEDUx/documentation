This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Requirements
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

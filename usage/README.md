This document will give you pointers at anything you need to know for building
and deploying the various components for specific platform.

## Build instructions
To deploy a complete system, successful of all components need to be available.
This means, single components can be updated and deployed if there exists
previous successful builds for you platform for the other components.

* [U-Boot](uboot)
* [Linux](linux)
* [RootFS](roofs)
* [Miscellaneous files](misc)

## Monitoring instructions
While your builds are running, you might want to 
[monitor the build system on the internal
webserver](common/build-monitoring.md).

## Hardware Deployment
After the build has successfully completed you can finally [deploy to hardware using the flashtool](flashtool)

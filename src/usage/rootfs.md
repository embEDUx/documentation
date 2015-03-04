# RootFS Specification
The RootFS will be assembled from a **Gentoo**-stage3 archive on the
buildserver. This page will guide you through the steps of providing your own
RootFS-specification to the buildserver.


## Prerequisites
Please review [the common usage prerequisites](usage.md#Prerequisites), which
are needed for the usage of every component.

### Requirements
* User Documentation.  At the end of the setup, the Administrator is instructed
  to create the [User Documentation](../setup/user-documentation.md).
* RootFS Git-Repository
  The RootFS-specification is supplied to the buildserver via git. Consult your
  User Documentation for the repository URLs. (See previous link)


### Suggestions
* Understand the [RootFS Background Information](../background/rootfs.md). The
  buldsystem itself and **Gentoo** as base distribution introduce a high level
  of customization options. These come with complexity and must be
  understood to be fully utilized.
* Get familiar with the [YAML-Syntax](http://yaml.org/)

### List Of Available Packages
The main reason why anyone would want a customized RootFS is the selection of
installed packages. For a categorized list of packages that are available, 
please visit the following sites:
* [Gentoo Portage category list](http://packages.gentoo.org/categories/)


## Repository content
### Branch Name-Scheme
The **buildserver** can only build your images, if you follow the correct name-scheme.

The variables that are needed for your platform can be found in the [User
Documentation](../setup/user-documentation.md).

* Kernel branch: <kernel\_version\> (eg. 3.17.2)
* Platform branch: <kernel\_version\>\_<platform\_name\> (eg. 3.17.2_raspberry-pi)

### The ***configuration.yml*** file
TODO link

### Pre/Post-Install File-Overlays
TODO

## Example Steps

## Advanced use cases
This section will provide some interesting use-cases for the output of the
RootFS-builds.

* [Running containers based on a generated RootFS](rootfs/advanced/run-containers.md)

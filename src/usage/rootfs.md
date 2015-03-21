# RootFS Specification
This page will guide you through the steps of providing your own
RootFS-specification to the buildserver.

## Prerequisites
Please review [the common usage prerequisites](usage.md#Prerequisites), which
are needed for the usage of every product.

### Requirements
* Access to an **embEDUx** buildserver system
* User Documentation.
    * At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/post-install/user-documentation.md).
    * Your platform needs to be included in the [User
      Documentation](../setup/post-install/user-documentation.md), if that isn't
      the case, please contact an Administrator to add your platform to the
      **embEDUx** build system.
* **rootfs-specs** Git-Repository

    The RootFS-specification is supplied to the buildserver via git. Consult
    your User Documentation for the repository URLs. (See previous link)

### Suggestions
* Understand the [RootFS Background Information](../background/implementation/rootfs.md). The
  buildsystem itself and **Gentoo** as base distribution introduce a high level
  of customization options. These come with complexity and must be
  understood to be fully utilized.
* Get familiar with the [YAML-Syntax](http://yaml.org/)


### List Of Available Packages
The main reason why anyone would want a customized RootFS is the selection of
installed packages. For a categorized list of packages that are available, 
please visit the following sites:

* [Gentoo Portage category list](http://packages.gentoo.org/categories/)


## Repository File-Structure

This is an example content of a branch in the RootFS-repository that makes use
of all the currently supported features.

```
.
├── configuration.yml
├── pre_install_overlay
│   └── etc
│       └── portage
│           ├── env
│           │   ├── no-distcc.conf
│           │   └── no-parallel.conf
│           └── package.env
└── pre_install_overlay
    └── pre_install_copied
```

## Quick Introduction
For all who skipped reading the background, here's a quick introduction
what happens during the build process on the buildserver. The **bold** words
indicate user provided content.

1. Reset the workspace to a clean state
1. Parse **configuration.yml**
1. Copy **pre_install_overlay** content to the target system
1. Execute the **pre_install_commands** on the target system
1. Install the specified packages
1. Copy **post_install_overlay** content to the target system
1. Execute the **post_install_commands** on the target system
1. Pack RootFS and upload archive to buildmaster

## Branch Name-Scheme

**< Platform-RootFS-String \>\_< RootFS-Name \>**

The **buildserver** can only build your images, if you follow the correct name-scheme.

### Variables
The variables that are needed for your platform can be found in the [User
Documentation](../setup/post-install/user-documentation.md). Please make sure to respect the
following criteria as well.

Variable | Notes
--- | ---
Platform-RootFS-String | Specified and mapped to the target platform by the Administrator. Found in the [User Documentation](../setup/post-install/user-documentation.md)
RootFS-Name | Chosen by the user. **Must not contain the '\_' character**

### Valid Examples
* armv7a_hardfp\_factory-systemd
* amd64\_factory-systemd

## The ***configuration.yml*** file
This file will specify packages to install and allows you to define commands
that will be run during the build routine. 

Please read through the [explained systemd configuration.yml
example](rootfs/configuration.yml.md)

## Pre/Post-Install File-Overlays
As seen in the [repository layout](#Repository-File-Structure) and described
outlined in [Quick Introduction](#Quick-Introduction), it is possible to provide
filesystem overlays that will be copied over the target RootFS at specified
times. 

Note that that file attributes cannot be preserved. If you need special
attributes or permissions on files, you have the following possibilities:
* set attributes in on the files of the install\_commands.
* `tar` your files in the overlay directories and `untar` them in one of the
  install\_commands 


## Advanced Use Cases
This section will provide some interesting use-cases for the output of the
RootFS-builds.

* [Running containers based on a generated RootFS](rootfs/advanced/run-containers.md)

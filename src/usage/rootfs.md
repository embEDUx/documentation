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

## Available Packages
The main reason why anyone would want a customized RootFS is the selection of
installed packages. For a categorized list of packages that are available, 
please visit the following sites:

* [Gentoo Portage category list](http://packages.gentoo.org/categories/)

## Branch Name-Scheme
The **buildserver** can only build your images, if you follow the correct name-scheme.

The variables that are needed for your platform can be found in the [User
Documentation](../setup/user-documentation.md).


* Kernel branch: <kernel\_version\> (eg. 3.17.2)
* Platform branch: <kernel\_version\>\_<platform\_name\> (eg. 3.17.2_raspberry-pi)

**Importan: The platform\_name must not contain any underscores, use dashes
instead!**



## The ***configuration.yml***-File
This file resides in the in the root directory of the 
*rootfs*-Repository. The file is written in [YAML-Syntax](http://yaml.org/). The
`---` in the first line of the file is necessary syntax which indicates
YAML-files, and must not be removed.

To demonstrate a **fully working example** this guide provides you with the
[systemd-rootfs specification](usage/rootfs/examples/systemd/configuration.yml)
taken from the actual setup at the HTWG.

### Global Flags Section
The *global*-Section configures the settings for global
[USE-Flags](../background/common/terminology.md#USE-flags) and 
[keywords](../background/common/terminology.md#keywords), which apply for every
installed package. If you find yourself putting the same keywords or USE-flags
for every package, this is the place to put them instead. 

```yaml
---
global:
    use:
        +: "python"
        -: "X doc"
```
This way, USE-flags **X** and **doc** are disabled system-wide, causing all affected
packages to build without X-support and without the installation of additional
documentation. The **python**-flag will be enabled for every package that supports
it. For example, this might cause packages to be built with bindings for
*Python* activated.


### Package-List and Package-Flags Section
The global section is followed by the package list. It is a YAML-dictionary
which defines the packages that are to be installed in the RootFS. The syntax
for every package is the same as for the global system.
```yaml
packages:
    sys-apps/util-linux:
        use:
            -: "systemd"
    virtual/udev:
        kw:
            +: "~amd64 ~x86"
    sys-apps/systemd:
        kw:
            +: "~amd64 ~x86"
        use: 
            +: "importd gcrypt curl lz4 lzma"
    app-editors/vim: {}
```

### Pre/Post-Install Commands Section
TODO
```
pre_install_commands:
    - "emerge-webrsync"
    - "chown -R portage:portage /usr/portage"

post_install_commands:
    - "echo Europe/Berlin > /etc/timezone"
    - "emerge --config timezone-data"
    - "mv /sbin/init /sbin/init-openrc"
    - "ln -sf /usr/lib/systemd/systemd /sbin/init"
```

### Pre/Post-Install File-Overlays
TODO

## Advanced use cases
This section will provide some interesting use-cases for the output of the
RootFS-builds.

* [Running containers based on a generated RootFS](rootfs/advanced/run-containers.md)

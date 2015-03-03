

## Prerequisites
Please review [the common usage prerequisites](usage.md#Prerequisites), which
are needed for the usage of every component.

### Requirements
#### RootFS Git-Repository

### Suggestions

### rootfs-Repository


## Branch name scheme


## RootFS specification
The RootFS specification is done in the ***configruation.yml*** in the root of
the *rootfs*-Repository. The file is written in [YAML-Syntax](http://yaml.org/).

The main reason why anyone would want a customized RootFs is the selection of
installed packages. For a categorized list of packages that are available, 
please visit the following sites:

* [Gentoo Portage package list](http://packages.gentoo.org/categories/)


### Example
To demonstrate a fully working example this guide provides you with a
[systemd-rootfs specification](rootfs/examples/systemd/configuration.yml)
taken from the actual setup at the HTWG.

The *global*-Section configures the settings for global
[USE-Flags](../background/common/terminology.md#USE-flags) and 
[keywords](../background/common/terminology.md#keywords), which apply for every
installed package. If you find yourself putting the same keywords or USE-flags
for every package, this is the place to put them instead. 


#### Global Section
```yaml
---
global:
    use:
        +: "python"
        -: "X doc"
```
This way, USE-flags **X** and **doc** are disabled system-wide, causing all affected
packages to build without X-support and without the installation of additional
documentation.


#### Package-List Section
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

#### Commands Section
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



### Global flags
### Packages and flags
### Available Packages
### Pre/Post-Install commands
### Pre/Post-Install overlays

## Advanced use cases
* [Running containers based on a generated RootFS](rootfs/advanced/run-containers.md)

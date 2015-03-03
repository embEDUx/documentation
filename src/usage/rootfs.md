## Requirements

## Suggested


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
The follow is is a fully working example, taken from 
[an example](rootfs/examples/systemd/configuration.yml)


The *global*-Section configures the settings for global
[use-Flags](../background/common/terminology.md#use-flags) and 
[keyywords](../background/common/terminology.md#keywords), which apply for every
installed package. If you find yourself putting the same keywords or use-flags
for every package, this is the place to put them instead. 
```
---
global:
    use:
        +: "python"
        -: "X doc"
```
In this example, the USE-flags **X** and **doc** are disabled system-wide, causing all affected
packages to build without X-support and without installed documentation.

The global section is followed by the package list. It is a YAML-dictionary that
defines the packages that are to be installed in the RootFS.


```
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

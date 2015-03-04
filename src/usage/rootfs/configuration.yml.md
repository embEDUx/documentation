# The RootFS ***configuration.yml*** file
This file resides in the in the root directory of the 
*rootfs*-Repository. The file is written in [YAML-Syntax](http://yaml.org/). The
`---` in the first line of the file is necessary syntax which indicates
YAML-files, and must not be removed.

To demonstrate a **fully working example** this guide provides you with the
[systemd-rootfs specification](examples/systemd/configuration.yml)
taken from the actual setup at the HTWG.

### Global Flags Section
The *global*-Section configures the settings for global
[USE-Flags](../../background/common/terminology.md#USE-flags) and 
[keywords](../../background/common/terminology.md#keywords), which apply for every
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

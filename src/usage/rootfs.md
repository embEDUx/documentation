## Requirements
### rootfs-Repository


## Branch name scheme


## RootFS specification
The RootFS specification is done in the ***configruation.yml*** in the root of
the *rootfs*-Repository. The file is written in YAML-Syntax and the following is
a fully working example, taken out of [the file from example]
(rootfs/examples/systemd/configuration.md)

The *global*-Section configures [use-Flags](rootfs/use-flags.md) and keywords

### Example
```yaml
---
global:
    use:
        +: "vim-syntax systemd"
        -: "X doc consolekit"

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
* [Running containers based on a generated RootFS](rootfs/run-as-container.md)

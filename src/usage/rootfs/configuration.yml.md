# The RootFS ***configuration.yml*** file
This file resides in the in the root directory of the 
*rootfs*-Repository. The file is written in [YAML-Syntax](http://yaml.org/). The
`---` in the first line of the file is necessary syntax which indicates
YAML-files, and must not be removed.

To demonstrate a **minima working example** this guide provides a slimmed down
version of the [systemd-rootfs
specification](examples/systemd/configuration.yml) taken from the actual setup
at the HTWG.

## Global Flags Section
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
The USE-flags **X** and **doc** are disabled system-wide, causing all affected
packages to build without X-support and without the installation of additional
documentation. The **python**-flag will be enabled for every package that
supports it. For example, this might cause packages to be built with bindings
for *Python* activated.


## Package-List and Package-Flags Section
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
The example shows the packages *sys-apps/util-linux*, *virtual/udev*,
*sys-apps/systemd* and *app-editors/vim* to be installed, with different
configuration. The brackets after the *vim*-line define an empty dictionary,
which cause the package to be installed with the default options. Remember, that
the default options are also influenced by the *global*-Section.

## Pre/Post-Install Commands Section
In order to not be limited to installing packages, or sometimes to work around
problems that occur during package installation, you can also **specifi
commands that are run** before and after the package installation. Both are
specified as a list of strings, which could look like in the following example.
```
pre_install_commands:
    - "emerge --sync"
    - "chown -R portage:portage /usr/portage"

post_install_commands:
    - "echo Europe/Berlin > /etc/timezone"
    - "emerge --config timezone-data"
    - "mv /sbin/init /sbin/init-openrc"
    - "ln -sf /usr/lib/systemd/systemd /sbin/init"
```
You can specify any command here. They will be **run as root** in sequential
order in the target RootFS. The changes you make with your commands are not
persistent to your next build job, but are only taking effect for the current
build.


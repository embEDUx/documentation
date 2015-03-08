# Flashtool

This guide will help you through the several commands you need to deploy builds
from the *buildserver* to hardware.

## Prerequisites

The Flashtool must be installed on your system. Please read the [setup
chapter](../setup/workstation/flashtool.md) of the **Flashtool**.

Also a successful [setup of the buildserver](../setup/setup.md) is required to
use the **Flashtool**.

### Requirements

* User Documentation

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/post-install/user-documentation.md).

* Git Repository with valid **recipe files**

## Getting started

After [installing](../setup/workstation/flashtool.md) the **Flashtool** on a linux system it
has to be configured first. To do so, type in the following command:

`$ flashtool init`

The tool needs a *working directory* which is set at the home directory
by default. (***${HOME}/.Flashtool***) It can be set by the user with the option
*-w | --working-dir*.

`$ flashtool -w /path/to/own/working_dir`

The tool will ask the user for some parameter to set, the next example shows
this procedure:

```bash
$ flashtool init
Type in a value for
    [Buildbot]->server
help:   Address or URL to a buildbot server. Optional Port must be set as next parameter.
: | 

...

Type in a value for
    [Buildbot]->port
help:   Port of the web frontend of the buildbot server
: |

...

Type in a value for
    [Recipes]->server
help:   Address or URL to a git server which contains yml recipes for different platforms
Must look like: git@{URL-to-server}:{path-to-git-repository}.git
: |

...

Type in a value for
   [Recipes]->user
help:   Directory where the user can save own recipe files.
: |

...

Type in a value for
    [Local]->products
help:   Local path where Flashtool should save downloaded products if option is selected.
: |
```

You can change these settings by calling the comand:

`$ flashtool config`

The tool will ask for each setting if you want to change the value or not.


## Get **recipes** from git server

**Recipes** are *yaml* configuration files, which declare how to deploy a
system on a platform (e.g. Raspberry Pi) and how to setup the platform. You 
find more information about **recipe** file in chapter 
[Recipe files](#recipe-files).

On the gitlab server **git@apu.in.htwg-konstanz.de:labworks-embEDUx/Flashtool_config.git**
there are provided some **recipe** files for different hardware.

To get the **recipe** files from the repository for the Flashtool run the following command:

`$ flashtool platform_recipes init`

The **recipe** files will be stored at the directory ***{working\_directory}/platforms***.
If there are new **recipes** on the repository you can get them with the command:

`$ flashtool platform_recipes update`

The given or created **recipe** files can be listed by the **Flashtool**.
To do so type in:

`$ flashtool list_platforms`

This command will list all **recipe** files grouped by their prefix.
### List finished builds from the configured **Buildbot** server

The **Buildbot** server provides all needed products for an **embEDUx** system.
All products for every configured platform can be listet by the **Flashtool** with
the following command:

`$ flashtool list_builds`

There are several options available for this command:

 option | Argument[s] | Description
 ------ | ----------- | ----------- 
 platform | -  |Specify a platform name. Only products for this platform will be listed. If none is selected, information for all platforms will be printed.
 --limit | N |Print top N entries for each selected product
 -l, --linux | - | List all linux kernel versions for the specified platform
 -u, --uboot | - | List all uboot versions for the specified platform
 -r, --rootfs | - | List all rootfs for the specified platform
 -m, --misc | - | List all misc files for the specified platform


## Setup Hardware and deploy system on Hardware

**Attention: the setup routine only allows to setup platforms which use a mmc
device as storage media. Support for other storage media must be implemented.**
If you want to implement new features to the **Flashtool**, please consider
reading the development section for the **Flashtool**. The new functionality
must be triggered by a recipe file an must be explained in the [recipe
files](#recipe-files) chapter.

This setup procedure requires an exisiting [recipe](#How_to_write_a_recipe_file) 
file. The basic command for this procedure is `Flashtool setup`.

**Important: You need access rights for reading and writing on a mmc device and
mounting a mmc device**

### Parameters

The setup command provides several optional and required parameter. The list
below will explain all parameters:

**Required parameter:**

 Parameter | Argument[s] | Description
 --------- | ----------- | -----------
 platform  |      -      | Specifies the platform which should be set up


**Optional parameter:**

* General options:

 Parameter | Argument[s] | Description
 --------- | ----------- | -----------
 -a, --auto |     -      | If an argument for a product matches for multiple files, the system, will fetch the latest file of a product in lexicographical order. Otherwise the user will be prompted to select a specific file.
 -L, --Local |    -      | If set, all downloaded files will be stored at the directory which is configured in the **Flashtool** configuration.


* Product Group 1 [linux, uboot, misc]:

The argument of an option will be interpreted as *Regex* string \*{string}.\*.
If this string matches for multiple files the **Flashtool** will handle this
situation dependent to the -a/--auto flag (see description above). The default
value for each option will match all files.

**Important: All three options must be stated or none of them.**

 Parameter | Argument[s] | Description
 --------- | ----------- | -----------
-l, --linux | version    | Select linux version.
-u, --uboot | version    | Select uboot version.
-m, --misc  | version    | Select misc files version.


* Product Group 2 [rootfs]

If no rootfs is specified the system will choose a factory rootfs for the
platform if exist. Otherwise the user will be prompted to choose a specific
rootfs.

 Parameter | Argument[s] | Description
 --------- | ----------- | -----------
-r, --rootfs | name      | Select rootfs


### setup procedure

The setup routine is triggered by the recipe file and will proceed different for
each recipe file. But in general there is a preparation step and a load step for
each recipe. These steps differ dependent on the type of recipe. The user will
be guided through the setup steps. If the "auto" flag is set all steps which do
not need an input from the user, will be selected with a default value.

To avoid user mistakes the **Flashtool** will prompt if the user want to proceed
with the setup procedure.


## Recipe files

Recipe files are important for the setup procedure. The user can configure, how
to setup a platform.

### Recipe files Name-Scheme

The name of a **recipe** file should follow this naming scheme:

{hardware-name}\_{identifier}.yml

**The name and identifier must not contain underscores, please use dashes instead.**
The *underscore* is used to divide the recipe file name in the two parts 
*hardware name* and *identifier*. It is important, that the platform name is also 
registered on the **buildserver**. You will find the valid platform-strings for
your **embEDUx** system in the [User Documentation](../setup/post-install/user-documentation.md).

The next example shows how to use this name scheme for a Raspberry Pi. This
name scheme is also used in the 
[HTWG setup](../setup/examples/user-documentation-HTWG.md#platform-strings) of **embEDUx**.

> raspberry-pi.yml
>
> raspberry-pi\_media_center.yml

The name for a Rapsberry Pi in this **embEDUx** configuration is *"raspberry-pi"*.
This name will be used in branches of the **git repositories** and on the
**buildbot** server to identify a Raspberry Pi.


### General structure of a recipe file

The recipe files for the **Flashtool** are written in 
[YAML-Syntax](http://yaml.org/). The next example shows the general structure
of a recipe file.

```yaml
---
type: # name of recipe type

recipe: 
    # specific configurations of the recipe
    # ...

---
type: # next recipe

recipe:
    # ...
```

The `---` is necessary to indicate a *YAML-document*. The example shows that a
recipe file can contain multiple *YAML-documents*. The must be at least one of
it.
Every *YAML-document* must contain a *type* keyword and a *recipe* keyword. The
content of the *recipe* section depends on the selected type. This is shown
in the next chapter.


### Recipe Types

For the extensibility of the **Flashtool**, we provide the possibility to define
different recipe types. Each type must have its counterpart implemented in the
python code of the **Flashtool**. By now we support the *mmc* recipe type. This
recipe type can handle the most deployment procedures for a wide range of
embedded hardware. If you need to implement a new recipe type, please read the 
development section for the **Flashtool**.

**MMC**:

This recipe type is used to configure platforms which use a mmc device as
storage media. The template below shows, how to state this recipe in a recipe file.


```yaml
---

type: mmc

recipe:
    partition_table: #partition table type
    partitions: # list with partition information
        -   name: # label
            size: # size of partition (allowed %/b/kb/mb/gb/)
            fs_type: # filesystem type (e.g. fat32, ext4)
            mount_point: # Mount point in System
            mount_opts:  # Mount options
            flags: # flags for partition
        -   #...
    load:
        Uboot:
            # device: or command:
        Linux_Boot:
            # device: or command:
        Linux_Root:
            # device: or command:
        Linux_Config:
            # device: or command:
        Rootfs:
            # device: or command:
        Misc_Boot:
            # device: or command:
        Misc_Root:
            # device: or command:
```

* ***partition\_table***:

      This section defines the partition table of the mmc device. The most embedded
      devices use *msods* or *gpt* for the partition table.

* ***partitions***:

      This section is used to define partitions on the mmc device. Each partition
      must be listed with a dash and must contain the subsections name, size,
      fs\_type, mount\_point, mount\_opts and flags. If one of these section is not
      needed, just leave the value after the colon blank.

      * ***name***:

        Name or label of the partition. The partition table type must support this
        feature.

      * ***size***:

        Size of the partition. The used units are b (byte), kb (kilobyte), mb
        (megabyte), gb (gigabyte) and \%. It is also possible to use the keyword
        *max* for the last stated partition. If you want to state the size of the
        partion in percentage, please use the percentage notation for each
        partition.

      * ***fs_type***:

        Filesystem type of the system. The **Flashtool** supports ext2, ext3, ext4,
        fat32 and btrfs.

      * ***mount_point***:

        Specifies the mount point which will be written in the **fstab** of the linux
        system.

      * ***mount_opts***:

        Specifies the mount options for the partition which will be written in the
        **fstab** of the linux system.

      * ***flags***:

        Flag for the partition. e.g. *boot*, *lba*. Multiple flags must be seperated 
        with a comma.

* ***load***:

      This section defines on which partition a software product should be loaded.
      The user can choose between the option *device* or *command* for every
      subsection. If a software product should be loaded on a partition of the mmc
      device, the user must use the option *device* and state the index of the
      partition which is defined in the section **partitions**. The index starts
      with zero.

      If a product should be loaded with an external command to the mmc device, you
      must use the option **command**. The value of the option is the external
      command. For a command you can use the to template variables *${file}* and
      *${device}*. The variable *${file}* will be replaced with the name of the
      specific software product. The variable *${device}* will be replaced with the
      */dev path* of the mmc device or the *dev path* of the mmc partition, if a
      number is written at the end of the variable (e.g. *${device0}*).

      The existing software products are Uboot, Linux\_Boot, Linux\_Root,
      Linux\_Config, Rootfs, Misc\_Boot, Misc\_Root.


**Example for a mmc recipe (utilite-pro.yml):**


```
---
type: mmc

recipe:
    partition_table: msdos
    partitions:
        -   name: boot
            size: 100mb
            fs_type: fat32
            mount_point: /boot
            mount_opts:
            flags: lba
        -   name: rootfs
            size: max
            fs_type: btrfs
            mount_point: /
            mount_opts:
            flags: 
    load:
        Uboot:
            command: dd if=${file} of=${device} bs=1K skip=1 seek=1 oflag=dsync
        Linux_Boot:
            device: 0
        Linux_Root:
            device: 1
        Linux_Config:
            device: 1
        Rootfs:
            device: 1
```



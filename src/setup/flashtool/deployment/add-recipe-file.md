# Add A New Recipe File

This chapter explains how to write a new recipe file for a platform. If you do
not know what a recipe file is and which role it plays in the deployment
procedure, please read the chapter [Deployment with the Flashtool](../deployment.md) 
first. It is also recommended to 

## Recipe Files Name-Scheme

The name of a **recipe** file must follow this naming scheme:

{hardware-name}\_{identifier}.yml

**The name and identifier must not contain underscores, please use dashes instead.**

The *underscore* is used to divide the recipe file name in the two parts 
*platform name* and *identifier*. It is important that the platform name is also 
registered on the buildserver. You will find the valid platform-strings for
your **embEDUx** system in the [User Documentation](../../post-install/user-documentation.md).

The next example shows how to use this name scheme for a Raspberry Pi. This
name scheme is also used in the 
[HTWG setup](../../examples/user-documentation-HTWG.md#platform-strings) of **embEDUx**.

> raspberry-pi.yml
>
> raspberry-pi\_media-center.yml

The name for a Raspberry Pi in this **embEDUx** configuration is *"raspberry-pi"*.
This name will be used in branches of the **git repositories** and on the
**buildbot** server to identify a Raspberry Pi.


## Recipe Skeletons

For the extensibility of the **Flashtool**, it provides the possibility to
define different recipe skeletons. Each skeleton must have its counterpart
implemented in the python code of the **Flashtool**. By now we support the *mmc*
recipe skeleton which is used in every recipe file on the **embEDUx**
[repository](https://github.com/embEDUx/flashtool-recipes).  

The recipe skeleton *mmc* can handle the most deployment procedures for a wide
range of embedded hardware. If you need to implement a new recipe skeleton, please
read the section [How to add a new deployment procedure](add-new-deployment.md).

### MMC:

This recipe skeleton is used to configure platforms which use a *MMC* device as
storage media. The template below shows, how to state this recipe skeleton in a 
recipe file.


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
      must be listed with a dash and must contain the subsections *name, size,
      fs\_type, mount\_point, mount\_opts and flags*. If one of these section is not
      needed, just leave the value after the colon blank.

      * ***name***:

        Name or label of the partition. The partition table type must support this
        feature.

      * ***size***:

        Size of the partition. The used units are b (byte), kb (kilobyte), mb
        (megabyte) and gb (gigabyte). It is also possible to use the keyword
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
      partition, which is defined in the section **partitions**. The index starts
      with zero.

      If a product should be loaded with an external command (e.g. dd) to the mmc
      device, you must use the option **command**. For a command you can use the 
      two template variables *${file}* and *${device}*. The variable *${file}* will
      be replaced with the name of the specific software product. The variable 
      *${device}* will be replaced with the *dev path* of the mmc device or the 
      *dev path* of the mmc partition, if a number is written at the end of the
      variable (e.g. *${device0}*).

      The existing software products are ***Uboot, Linux\_Boot, Linux\_Root,
      Linux\_Config, Rootfs\_Root, Rootfs\_Portage, Misc\_Boot, Misc\_Root***.
      Some products are divided into two parts. For example the product *Linux*
      provides packages for boot partition and packages for the root parition.


## Example for a recipe file with a mmc recipe (utilite-pro.yml):

This recipe is also available in the HTWG configuration.

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
        Rootfs_Root:
            device: 1
        Rootfs_Portage:
            device: 1
```

This recipe file will configure the deployment procedure for the utilite-pro as
follow:

* The MMC device will be partition into two partitions. The first partition will
    have the size of *100 mb*, its label is *"boot"* and the filesystem format is
    *fat32*. Also the *lba* flag set for the partition. The partition will be
    mounted at */boot* in the *RootFS*. The second partition will get the free
    space of the MMC device as size, its label is *"rootfs"* and the filesystem
    format is *btrfs*. The partition will be mounted at */*. 

* The uboot product and the 

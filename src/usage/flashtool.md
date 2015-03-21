# Flashtool

This guide will help you through the several commands you need to deploy builds
from the buildserver to hardware.

## Prerequisites

The Flashtool must be installed on your workstation. Please read the [setup
chapter](../setup/workstation.md) of the **Flashtool**.

Also a successful [setup of the buildserver](../setup/setup.md) is required to
use the **Flashtool**.

### Requirements

* User Documentation

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/post-install/user-documentation.md).

* Git Repository with valid ***recipe files***

## Getting started

After [installing](../setup/workstation.md) the **Flashtool** on a linux system it
has to be configured first. To do so, type in the following command:

`$ flashtool init`

The tool needs a *working directory* which is set at the home directory
by default. (***${HOME}/.Flashtool***) It can be set by the user with the option
*-w | --working-dir*.

`$ flashtool -w /path/to/own/working_dir init`

The tool will ask the user for some parameter to set. The next example shows this 
procedure. The given values are for the HTWG Environment:

```bash
[mahieke@hakunamatata test2]$ flashtool -w ./.flashtool init
Working directory does not exist at ./.flashtool
Do you want to setup working directory "./.flashtool" [(Y)|(y)|(N)|(n)]
Answer: y
Type in a value for
   [Recipes]->server
help:   Address or URL to a git server which contains yml recipes for different platforms
  Must look like: git@{URL-to-server}:{path-to-git-repository}.git
  or 
  https://{URL-to-server}/{path-to-git-repository}.git

: https://github.com/embEDUx/flashtool-recipes.git

Type in a value for
   [Recipes]->user
help:   Directory where the user can save own recipe files. Path must not include underscores!
: /home/mahieke/.flashtool/own-recipes

Type in a value for
   [Local]->products
help:   Local path where flashtool should save downloaded products if option is selected.
: /home/mahieke/.flashtool/downloaded-products 

Type in a value for
   [Buildbot]->server
help:   Address or URL to a buildbot server. Optional Port must be set as next parameter.
: http://moe.in.htwg-konstanz.de            

Type in a value for
   [Buildbot]->port
help:   Port of the web frontend of the buildbot server
: 8010
```

You can change these settings by calling the command:

`$ flashtool config`

The tool will ask for each setting if you want to change the value or not.


## Get Recipes From Git Server

**Recipes** are *yaml* configuration files, which declare how to deploy a
system on a platform (e.g. Raspberry Pi) and how to prepare the storage media of
a platform. You find more information about recipe files in chapter 
[Recipe files](../setup/flashtool/deployment.md).

On the **Gitlab** server **git@apu.in.htwg-konstanz.de:labworks-embEDUx/Flashtool\_config.git**
some recipe files for different hardware are provided.

To get the recipe files from the repository for the **Flashtool** run the following command:

`$ flashtool platform_recipes init`

The recipe files will be stored at the directory ***{working\_directory}/platforms***.
If there are new recipes on the repository you can get them with the command:

`$ flashtool platform_recipes update`

The given or created recipe files can be listed by the **Flashtool**.
To do so type in:

`$ flashtool list_platforms`

This command will list all recipe files grouped by their prefix.

### List Finished Builds From The Web Server

The **Buildbot** server provides all needed products for an **embEDUx** system.
All products for every configured platform can be listed by the **Flashtool** with
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


## Deploy Products On The Platform

The basic command for this procedure is `flashtool setup`. 

**Important: You need access rights for reading from and writing on the
storage device. The Flashtool will signal missing access rights.**

### Parameters

The setup command provides several optional and required parameter. The list
below will explain all parameters:

**Required parameter:**

 Parameter | Argument[s] | Description
 --------- | ----------- | -----------
 platform  |      -      | Specifies the platform which should be set up


*Example:* `flashtool setup`  **`raspberry-pi`**


**Optional parameter:**

* General options:

    Parameter | Argument[s] | Description
    --------- | ----------- | -----------
    -a, --auto |     -      | If an argument for a product matches for multiple files, the system, will fetch the latest file of a product in lexicographical order. Otherwise the user will be prompted to select a specific file.
    -L, --Local |    -      | If set, all downloaded files will be stored at the directory which is configured in the **Flashtool** configuration.


* Product Group 1 [linux, uboot, misc]:

    The argument of an option will be interpreted as *Regex* string \*{string}.\*.
    If this string matches for multiple files the **Flashtool** will handle this
    situation depending whether the -a/--auto flag is set or not(see description 
    above). The default value for each option will match all files.

    **Important: All three options must be stated or none of them.**

     Parameter | Argument[s] | Description
     --------- | ----------- | -----------
    -l, --linux | version    | Select linux version.
    -u, --uboot | version    | Select uboot version.
    -m, --misc  | version    | Select misc files version.

    *Example:* `flashtool setup raspberry-pi` **`-l 3.19.2 -u v2015.01`**

* Product Group 2 [rootfs]

    If no rootfs is specified the system will choose a factory rootfs for the
    platform if exist. Otherwise the user will be prompted to choose a specific
    rootfs.

     Parameter | Argument[s] | Description
     --------- | ----------- | -----------
     -r, --rootfs | name      | Select rootfs

     *Example:* `flashtool setup raspberry-pi -l 3.19.2` **`-r factory-systemd`**


### Setup Procedure

The deployment procedure is configured by the provided recipe file. As previous
mentioned the **embEDUx** system provides several recipe files for several
platforms. If you want learn more about configuring a deployment procedure for a
platform please read the chapter on [how to add a new recipe file](../setup/flashtool/deployment/add-recipe-file.md).

But in general there is a preparation step and a load step for
each recipe. These steps differ dependent on the type of recipe. The user will
be guided through the setup steps. If the "auto" flag is set all steps which do
not need an input from the user, will be selected with a default value.

To avoid overwriting a storage media of a platform by mistake the **Flashtool** 
will prompt if the user want to proceed with the setup procedure.

Congratulations you are now able to deploy a distribution build by the
**embEDUx** system with the **Flashtool**.

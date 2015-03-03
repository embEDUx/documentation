# Flashtool

1. Getting started

3. How to write a recipe file
4. Flashtool help page


## Getting started

After [installing](../setup/flashtool.md) the **flashtool** on a linux system it
has to be configured first. To do so, type in the following command:

> `flashtool init`

The tool needs a *working directory* which is set at the home directory
by default. (***${HOME}/.flashtool***) It can be set by the user with the option
*-w | --working-dir*.

> `flashtool -w /path/to/own/working_dir`

The tool will ask the user for some parameter to set, the next example shows
this procedure:

```bash
> flashtool init
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
help:   Local path where flashtool should save downloaded products if option is selected.
: |
```

You can change these settings by calling the comand:

> `flashtool config`

The tool will ask for each setting if you want to change the value or not.

### Get recipes from git server

**Recipes** are *yaml* configuration files, which declares how to deploy a
system on a hardware (e.g. Raspberry Pi) and how to setup the hardware. If
you want to write a new recipe for a hardware please read [How to write a recipe
file](#How_to_write_a_recipe_file). 

On the gitlab server **git@apu.in.htwg-konstanz.de:labworks-embEDUx/flashtool_config.git**
there are provided some recipe files for different hardware.

To get the recipe files from the repository for the flashtool run the following command:

> `flashtool platform_recipes init`

The recipe files will be stored at the directory ***{working\_directory}/platforms***.
If there are new recipes on the repository you can get them with the command:

> `flashtool platform_recipes update`

The given or created recipe files can be listed by flashtool. To do so type in:

> `flashtool list_platforms`

This command will list all recipe files grouped by their prefix. The name of a
recipe file should follow this naming scheme:

> {hardware-name}\_{identifier}.yml

The name and identifier must not contain underscores. The underscore is used to
divide the recipe file name in the two parts hardware name and identifier. It is
important, that the hardware name is also registered on the buildserver. The
next example shows how to use this naming scheme for a Raspberry Pi.

> raspberry-pi.yml

> raspberry-pi\_media_center.yml

The name for a Rapsberry Pi in this embEDUx configuration is *"raspberry-pi"*.
This name will be used in branches of the git repositories and on the buildbot
server to identify a Raspberry Pi.

### List finished builds from the configured **Buildbot** server

The **Buildbot** server provides all needed products for an embEDUx system.
These products can be 


### Setup Hardware and deploy system on Hardware


### How to write a recipefile
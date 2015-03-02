# Flashtool

1. Getting started

3. How to write a recipe file
4. Flashtool help page


## Getting started

After [installing](../setup/flashtool/README.md) the **flashtool** on a linux system it
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

### Get recipes from git server

**Recipes** are *yaml* configuration files, which declares how to deploy a
system on a hardware (e.g. Raspberry Pi). If you want to write a new recipe for
a hardware please read [How to write a recipe
file](#How_to_write_a_recipe_file). 

On the gitlab server **git@apu.in.htwg-konstanz.de:labworks-embEDUx/flashtool_config.git**
there are provided some recipe files for different hardware.

To get the recipe files from the repository for the flashtool run the following command:

> `flashtool platform_recipes init`

The recipe files will be stored at the directory ***{working_directory}/platforms***.
If there are new recipes on the repository you can get them with the command:

> `flashtool platform_recipes update`

### 

# Specification for a deployment tool

This is the specification that has been worked out according to the [design of
the Flashtool](../design/flashtool.md). 


## **Flashtool** configuration file and working directory

The configuration file for the **Flashtool** should be saved in a own working
directory for the **Flashtool**. This working directory can be set by the user
when the tool is initialized. When the user does not specify the working
directory it will be created in the *home* directory with the folder name
"*.flashtool*.

This working directory is used to save the configuration files for the
platforms and logging files of the **Flashtool**.


## Recipe file for platforms

The configuration file for the platform act as recipe for the setup procedure.
The user should be able to define how to partition the storage device of the
platform and where the software packages should be loaded. 

### Language

The language of the recipe file is *YAML*. A recipe file must contain at least
one *YAML document*. Each *YAML document* specifies a recipe. So a recipe file
contains one or more recipes. Each recipe must have a python counterpart, which
ensures if all required settings are given and checks the values of the
settings.

    ---
    type : ${recipe type}

    recipe:
        ${settings for recipe}

This example shows the basic structure of a recipe. Multiple recipes in a recipe
file must be divided by `---`.


### Name Scheme

The name scheme of a recipe file must be as follows:

`{platform name}.yml}`
or
`{platform name}_{identifier}.yml`

The *platform name* and the *identifier* must not contain underscores. The
platform name must also exist on the buildserver configuration for the specific
platform. With the *identifier* it is possible to set multiple recipe files for
a platform.


### Availability of predefined recipe files 

There must be a repository for recipe files which are set by the administrator.
This repository is a git repository and the URL to it must be configured in the
**Flashtool** configuration.


### User defined recipe files

It is also required to add a directory for the **Flashtool** where the user can
add own recipe files. This directory must be configured in the **Flashtool**
configuration.


## Retrieving software products 

The built software product must be retrieved from the **builbot** web server.
The web server provides a *JSON api* to get all information about every built
which was made. This *JSON* information must be parsed by the **Flashtool** to get
all valid builds. The next list shows the paths which provide different
information about the **buildbot master** and which data is useful for the
**Flashtool**.

* `/json`

    Get all supported platforms and which architecture the platform has. It also
    gets the name of the builder for a specific architecture.

    *useful values* in json string ([i]: for each entry):

    * builders[i]->basedir: builder name and architecture
    * builders[i]->schedulers: branch filter and platform name

* `/json/builders/{builder name}/builds/-1`

    Get the last build of the builder.

    *useful values* in json string:

    * number: build number

* `/json/builders/{builder name}/builds/{build id}`

    Get information about a specific build. Check if build was successful and
    save the following values for each successful build.

    *useful values* in json string:

    * text: check for value *build* and *successful*
    * properties->urls: path to the built files and product
    * properties->upload\_files: Created files of the build

    With this information it is possible to create a download link for each
    software product. The path is created by the following patterns:
    
        /{url}/{file name}


## List of feature
The table below shows a quick overview of the features of the **Flashtool**.
A detailed description of the command can be found in the [usage
section](../../usage/flashtool.md) of the **Flashtool**


 command | description
 ------- | -----------
 init / config | Configure needed options for the **Flashtool**. Must be done as first step (init) and can be changed any time (config)
 platform\_recipes | Get or update platform recipes from git repository
 list\_platforms   | Shows which platforms have a recipe file and can be set up
 list\_builds  | List all versions of software components on the platform, grouped by platform and product type
 setup  | runs a deployment procedure for the specified platform
 check\_mmc | Does a filesystem check on every partition on a mmc media


 



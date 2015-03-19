# Yocto Project
"Provides open source, high quality infrastructure and tools to help developers
create their own **Linux** distribution for any hardware architecture, across
muiltiple market segments. It is intended to provide a helpful starting point
for developers."
  ([Source](https://wiki.yoctoproject.org/wiki/FAQ#What_is_the_Yocto_Project.3F))

The introduction of the **Yocto Project** which greats you at the
[homepage](https://www.yoctoproject.org) for the project sounds like the **Yocto
Project** would the solution, that follows our defined
[requirements](../../requirements.md). Therefore we will analyze the
functionality and usability of the **Yocto Project**.

## Sub-Projects
The **Yocto Project** is just an umbrella project for a couple of self
organizing sub-projects. Each sub-project has its own purpose. The  


### Hob (Human Oriented Builder)

**Hob** is a graphical user interface, which helps the user through the building
process of **Yocto**. For a short manual have a look the
[homepage](https://www.yoctoproject.org/documentation/hob-manual-171).

With **Hob** you can select the machine for which the image should be build, and
which recipes should be contained in that image. With **Hob** you can't define
recipes or board support packages. Basically **Hob** only visualizes all the
board support packages and recipes in a nice way, so the user can choose
which ones are needed. The user then can trigger the build process. **Hob**
presents the necessary informations about success and error of building the
recipes.

### Bitbake
**Bitbake** is the sub-project that builds the output system image, and is
inspired by the **Portage** package management system from **Gentoo**. The build
process uses the meta data (recipes) from e.g. the **Openembedded-core** to
calculate the build instructions. With the recipe structure the output is highly
configurable by the user, as long as the recipes provided to **BitBake**. If a
recipe for a e.g. a user-space program is not available in the known sources
like **openembedded-core**, the user has to write an own recipe.

### Openembedded-Core - Meta data
The standard meta data is provided by the **openembedded-core** and is stored as
recipes which are used by **Bitbake** to build the packages. As the **Yocto
Project** is mainly targeted on creating images for the embedded domain, it
seems that the meta data, and therefore the available software packages, is
updated less frequently when compared to other package management systems. At
the time of evaluation there wasn't a **Python 3** version available through the
**Openembedded-core** project, which is violating the defined
[requirements](../../requirements.md).

## Workflow
In the next part of this document, for each of the required products a short
overview for the workflow is given.

### Bootloader

### Linux Kernel

### RootFS


## Result
The **Yocto Project** offers a great set of tools and possibilities, but needs a
lot of configuration. Everything is capsulated within the recipes, so an easy
editing of kernel version or user-space software is not possible.

* WebUI: Toaster
* GUI: HOB

Criteria | Result | Notes
--- | --- | ---
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Package manager can be configured with own repository
Buildroutine Automation | YES | -


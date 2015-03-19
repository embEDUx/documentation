# Yocto Project
*Provides open source, high quality infrastructure and tools to help developers
create their own **Linux** distribution for any hardware architecture, across
multiple market segments. It is intended to provide a helpful starting point
for developers.*
  ([Source](https://wiki.yoctoproject.org/wiki/FAQ#What_is_the_Yocto_Project.3F))

This is thee introduction of the **Yocto Project** which greats you at the
[homepage](https://www.yoctoproject.org) for the project. It makes the **Yocto
Project** one possible solution, which follows our defined
[requirements](../../requirements.md). Therefore we will analyze the
functionality and usability of the **Yocto Project**.

## Sub-Projects
The **Yocto Project** is an umbrella project for a couple of self organizing
sub-projects. Each sub-project has its own purpose. The  

### Hob (Human Oriented Builder)
**Hob** is a graphical user interface, which helps the user through the building
process of **Yocto**. For a short manual have a look the
[homepage](https://www.yoctoproject.org/documentation/hob-manual-171).

With **Hob** the machine for which the image should be build and also which
recipes should be contained within that image can be selected. But **Hob** can't
define recipes or board support packages. Basically **Hob** only visualizes all
the board support packages and recipes in a nice way, so the user can choose
which ones should be build. The user then can trigger the build process. **Hob**
presents the necessary informations about success and error of building the
recipes.

### Bitbake
**Bitbake** is the sub-project that builds the output system image, and is
inspired by the **Portage** package management system from **Gentoo**. The build
process uses the meta data (recipes) from e.g. the **openembedded-core** to
calculate the build instructions. With the recipe structure the output is highly
configurable by the user. If a recipe for e.g. a user-space program is not
available in the known sources like **openembedded-core**, the user has to write
an own recipe.

### Openembedded-Core - Meta data
The default meta data is provided by the **openembedded-core** and is stored as
recipes which are used by **Bitbake** to build the packages. As the **Yocto
Project** is mainly targeted on creating images for the embedded domain, it
seems that the meta data, and therefore the available software packages, is
updated less frequently when compared to other package management systems. At
the time of evaluation there wasn't a **Python 3** version available through the
**openembedded-core** project, which is violating the defined
[requirements](../../requirements.md#product-specific-requirements).

### Poky
*Poky is a reference system of the Yocto Project - a collection of Yocto Project
tools and metadata that serves as a set of working examples.*
([Source](https://www.yoctoproject.org/tools-resources/projects/poky))

## Products 
In this part of the document, the support for the
[required](../../requirements.md) is evaluated. 

### Bootloader
The default bootloader, which comes with **Poky** is **U-Boot**. The recipe in
**Poky** is for version 2013.07, which is compared to upstream 2015.01 pretty
old. Newer versions were added in the **openembedded-core** repository, however
they aren't part of the reference system **Poky**.

* 2014.07: 12.11.2014
* 2015.01: 14.02.2015

### Linux Kernel
**Poky** has the linux kernel versions 3.10, 3.14 and 3.17. In the
**openembedded-core** repository 3.19 can also be found.

TODO

### RootFS
TODO

## Result
Looking through the additional [board support
packages](http://git.yoctoproject.org/cgit/cgit.cgi/) and their pure amount of
additional recipes needed for the **Linux** kernel and **U-Boot**, it seems like
the **Yocto** Project is not the right choice to fulfill our
[requirements](../../requirements.md). From our point of view the **Yocto Project** is
a good choice, if you want to develop for a single platform. As soon as multi
platform development is needed, the amount of configuration and individual
modification needed for building with **Yocto** doesn't justify the results.
Another not negligible fact is also the sense able lack of up-to-date versions
for the different recipes. This would result in a scenario where anyone using
  the build system has to have knowledge about **Yocto** and **BitBake** to
  configure and write the required recipes.

Overall the **Yocto Project** is what it intends to be: *A helpful starting
point for developers.* But it is not, what we need to fulfill our
[requirements](../../requirements.md).


# Evaluation Yocto Project
*Provides open source, high quality infrastructure and tools to help developers
create their own **Linux** distribution for any hardware architecture, across
multiple market segments. It is intended to provide a helpful starting point
for developers.*
  ([Source](https://wiki.yoctoproject.org/wiki/FAQ#What_is_the_Yocto_Project.3F))

This is the introduction of the **Yocto Project** which greats you at the
[homepage](https://www.yoctoproject.org) for the project. It makes the **Yocto
Project** one possible solution, which follows our defined
[requirements](../requirements.md). Therefore we will analyze the
functionality and usability of the **Yocto Project**.

## Sub-Projects
The **Yocto Project** is an umbrella project for a couple of self organizing
sub-projects. Each sub-project has its own purpose.

### Hob (Human Oriented Builder)
**Hob** is a graphical user interface, which helps the user through the building
process of **Yocto**. For a quick start have a look the
[homepage](https://www.yoctoproject.org/documentation/hob-manual-171).

With **Hob** the machine for which the image should be build and also which
recipes should be used for that image can be selected. But **Hob** can't define
recipes or board support packages. Basically **Hob** only visualizes all the
board support packages and recipes in a nice way, so the user can choose which
ones should be build. The user then can trigger the build process and **Hob**
presents the necessary informations about success or failure for each recipe. 

### Bitbake
**Bitbake** is the sub-project that builds the image, and is inspired by the
**Portage** package management system from **Gentoo**. The build process uses
the meta data (recipes) from e.g. the **openembedded-core** to calculate the
build instructions. With the recipe structure the content of the output image is
highly configurable by the user. If a recipe for e.g. a user-space program is
not available in the known sources like **openembedded-core**, the user has to
write an own recipe.

### Openembedded-Core
The default meta data is provided by the **openembedded-core** and is stored as
recipes which are used by **Bitbake** for building the packages. As the **Yocto
Project** is mainly targeted on creating images for the embedded domain, it
seems that the meta data, and therefore the available software packages, are
updated less frequently when compared to other package management systems. E.g.
at the time of evaluation there wasn't a **Python 3** version available through
the **openembedded-core** project, which is violating the defined
[requirements](../requirements.md#product-specific-requirements).

### ADT (Application Development Toolkit)
From the
[documentation](http://www.yoctoproject.org/docs/1.6.1/adt-manual/adt-manual.html#adt-intro):


```
Fundamentally, the ADT consists of the following:

* An architecture-specific cross-toolchain and matching sysroot both built by
  the OpenEmbedded build system. The toolchain and sysroot are based on a
  Metadata configuration and extensions, which allows you to cross-develop on
  the host machine for the target hardware.

* The Eclipse IDE Yocto Plug-in.

* The Quick EMUlator (QEMU), which lets you simulate target hardware.

* Various user-space tools that greatly enhance your application
  development experience.
```

This description sounds like the swiss army knife we are looking for.
Unfortunately it also comes with quiet a lot of configuration costs. Using the
ADT as a development environment for the students wouldn't be a good solution,
as for this use case a solution with lower prerequisite knowledge is likely
preferable.

### Poky
*Poky is a reference system of the Yocto Project - a collection of Yocto Project
tools and metadata that serves as a set of working examples.*
([Source](https://www.yoctoproject.org/tools-resources/projects/poky))

## Products 
This part of the document evaluates the support for the defined
[requirements](../requirements.md).

### Bootloader
The default bootloader, which comes with **Poky** is **U-Boot**. The recipe in
**Poky** is for version 2013.07, which is compared to upstream 2015.01-rc1 pretty
old. Version 2014.07 is within in the **openembedded-core** repository since
12.11.2014, however they aren't part of the reference system **Poky**.

### Linux Kernel
**Poky** comes with the linux kernel versions 3.10, 3.14 and 3.17. These
versions are quited outdated. Also adding the support for each of the platforms
comes with modifying and adding multiple recipes for each of the desired kernel
version.

### RootFS
**Poky** contains by default a lot of user-space program recipes. As the effort
of comparing all the included recipes with the current available versions would
exceed this evaluation, only the important packages from the
[requirements](../requirements.md) are evaluated.

Software | Poky | Available
--- | --- | ---
gcc | 4.9.1 | 4.9.1
lighttpd | 1.4.35 | 1.4.35
ssh | 6.6.p1 | 6.8.p1 
Avahi | 0.6.31 | 0.6.31
iw-utility | n/a | 3.17
Python2 | 2.7.3 | 2.7.3
Python3 | n/a | 3.4

At the time of this evaluation and as aforementioned, **Yocto** doesn't provide
a **Python 3** recipe, which is violating the defined
[requirements](../requirements.md).

## Summary
By default the **Yocto Project** is missing the majority of the platforms that
would be used with the build system solution. Looking through the additional
[board support packages](http://git.yoctoproject.org/cgit/cgit.cgi/) and their
sheer amount of additional recipes needed for the **Linux** kernel and
**U-Boot**, it seems that the overhead to add a new platform is quite huge. The
**Yocto Project** is a good choice, if you want to develop for a single
platform. As soon as multi platform development is needed, the amount of
individual configuration and modification needed for building with **Yocto**
doesn't justify the results. Another not negligible fact is also the sensible
lack of up-to-date versions for the different recipes. This would result in a
scenario where anyone using the build system has to have knowledge about
**Yocto** and **BitBake** to configure and write the required recipes.

In the end the **Yocto Project** is what it intends to be: *A helpful starting
point for developers.* But it is not, what we need to fulfill the
[requirements](../requirements.md).

Criteria | Result | Notes 
--- | --- | --- 
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Extensible through recipes, although it needs a lot of configuration
Build routine Automation | YES | Includes U-Boot, Kernel, Toolchain, RootFS 
Deployment | LIMITED | Result of build process is an image, which can be deployed on a sd card with `dd`


"Provides open source, high quality infrastructure and tools to help developers
create their own **Linux** distribution for any hardware architecture, across
muiltiple market segments. It is intended to provide a helpful starting point
for developers."
  ([Source](https://wiki.yoctoproject.org/wiki/FAQ#What_is_the_Yocto_Project.3F))

The **Yocto Project** is divided in multiple sub-projects. After the build
process an entire **Linux** distribution is created, including the toolchain.

* Bitbake (build tool)

    **Bitbake** is the sub-project that builds the output system image, and is
    based on **Gentoo Portage**. The buildprocess uses meta data to calculcate 
    the installation instructions. 

* Openembedded-Core - Meta data (available software)

    The meta data is provided by the **openembedded-core** and is stored as
    recipes which are used by **Bitbake** to build the packages. As the **Yocto
    Project** is mainly targetted on creating images for the embedded
    domain, it seems that the meta data, and therefore the available software
    packgaes, is updated less frequently when compared to other package
    management systems.

* Hob (Human Oriented Builder)

    **Hob** is a graphical user interface which allows the user to select a
    platform (machine) and an image recip. The image recipe contains the
    information of which packages should be build. This configuration can be
    modified with **Hob**. **Hob** is a nice tool, once all the required meta
    data exist to select and start the generation process.

The **Yocto Project** offers a great set of tools and possibilities, but needs a
lot of configuration. Everything is capsulated within the recipes, so an easy
editing of kernel version or user-space software is not possible.

### Result Yocto Project
Criteria | Result | Notes
--- | --- | ---
Cross-target support | YES | Manual configuration necessary 
Package management | LIMITED | Package manager can be configured with own repository
Buildroutine Automation | YES | -


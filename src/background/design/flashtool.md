# Design Of A Deployment Tool - **Flashtool**

(work in progress)

This chapter describes the design of the **Flashtool** and its configuration
components.

## Automated And Configurable Deployment Tool

Deploying the software products built with the **embEDUx** system, should be done
as easy and as fast as possible the user. Therefore a tool should be developed
which automates the several steps of the deployment procedure. The deployment 
procedure will differ, dependent on the needs of the user but for all that there
are similarities in each deployment procedure. 

To find these similarities the deployment procedure must be abstracted into
several steps. 

### Storage device of the platform 

The first step is to recognize how the products can be deployed to the
platform. In every case this media will be a **storage device** which can be
accessed in different ways.

All platforms which are in use by the *HTWG Configuration* use MMC devices
as storage device for the products. But there might be other platforms which
use other storage devices (e.g. an internal NAND-Flash).

It must be assumed that the deployment tool must be able to
access these devices in different ways (e.g. via Linux block device or via
USB with an external tool). 

* The deployment tool must be open for new mechanisms and should
    provide an interface to access other storage devices.
        
### Recognize the storage device

It is also important for the deployment tool that it is able to recognize the
storage device when it is plugged in. This mechanism can also differ
dependent on the type of the storage device.

* The deployment tool must use a software or component of the host operating
    system (Linux) which allows to recognize different device types and makes 
    it possible to extend the deployment tool for this types.

### Partition the storage device

The next step is the possibility to partition the storage device in different
parts if needed. This depends on the configuration of the Linux kernel and
the Uboot. 

* The deployment tool must be able to let the user partition the storage
    device for its needs. Dependend on the storage device this might require
    different tools or mechanisms.


###


### Main goals for the implementation 

One of the main goals for the deployment tool is that it is open for new
features and mechanisms to form different deployment procedures. It is
impossible to implement an automation tool which fulfills the requirements for
all thinkable platforms. So there must be done constraints on the implementation
of features but the software must be open to add new features easily.

## Name Of The Deployment Tool

It seemed obvious to call this tool "**Flashtool**"
due to the fact that most of the embedded devices uses flash memories to store
their operating system and files.

## Programming language

One of the first decisions which were made for the tool was to choose *python*
as programming language. Python is a script language which is easy to learn,
highly productive, has a nice syntax and provides plenty of packages and 
libraries. It is also an often used language and will run on every Linux system.


## Design decisions

There are basic tasks which must be fulfilled by the **Flashtool**:

First of all the **Flashtool** must be usable for different *embEDUx*
environments. Therefore URLs to the *buildserver* or to repositories should not
be hard coded. 

- User must be able to configure several settings for the **Flashtool**, these
    settings should be saved in a configuration file.

The **Flashtool** should be able to setup several platforms. For the platforms
this includes partition a MMC device and load the software components to the
partitions. It must be possible to configure this setup process for the needs of
the user. And this configuration should be reusable, to setup several platforms
with the same configuration.

- User can create different configuration files for a platform to configure the
    setup/deploy process. (recipes)
- The configuration language should be easy to use.

Each software components will have several versions. These versions are
available on the *buildserver*.

- User should be able to list all available software components versions for a
    platform. 
- User should be able to select a specific version for a setup procedure.
- **Flashtool** must be able to reach all built software components on the
    *buildserver*

To make the setup process as easy as possible for the user, the **Flashtool**
should be able to recognize plugged in MMC media. 

- Automatic recognition of plugged in MMC devices.

The **Flashtool** should be extensible for future features.

- adding new setup routines for new platforms if needed.
- adding new commands for the **Flashtool**. 



# Design Of A Deployment Tool - **Flashtool**

This chapter describes the design of the **Flashtool** and its configuration
components.


## Name Of The Deployment Tool

It seemed obvious to call this tool "**Flashtool**"
due to the fact that most of the embedded devices uses flash memories to store
their operating system and files.


## Automated And Configurable Deployment Tool

Deploying the software products built with the **embEDUx** system, must be done
as easy and as fast as possible for the user. Therefore a tool must be developed
which automates the several steps of the deployment procedure. The deployment 
procedure will differ depending on the needs of the user, but for all that there
are similarities in each deployment procedure.

To find these similarities the deployment procedure must be abstracted into
several steps. 

### Access Storage Device Of The Platform 

The first step is to recognize how the products can be deployed to the
platform. In every case this media will be a **storage device** which can be
accessed in different ways.

All platforms which are in use by the *HTWG Configuration* use *MMC* devices
as storage device for the products. But there might be other platforms which
use other storage devices (e.g. an internal NAND-Flash).

It must be assumed that the **Flashtool** must be able to
access these devices in different ways (e.g. via Linux block device or via
USB with an external tool). 

* The **Flashtool** must be open for new mechanisms and should
    provide an interface to access storage devices.
        

### Recognize The Storage Device

It is also important for the deployment tool that it is able to recognize the
storage device when it is plugged in. This mechanism can also differ
depending on the type of the storage device.

* The deployment tool must use a software or component of the host operating
    system (Linux) which allows to recognize different device types and makes 
    it possible to extend the deployment tool for this types.


### Partition The Storage Device

The next step is the possibility to partition the storage device in different
parts if needed. This depends on the configuration of the Linux kernel and
the Uboot. 

* The **Flashtool** must provide a mechanism for the user to partition the 
    storage device for its needs. Dependend on the storage device this might
    require different tools or mechanisms.

* Since many platforms require partition flags, the **Flashtool** must be 
    able to set flags for the partitions.


### Getting Built Products

The **embEDUx** build system provides the built products with a web server.
These products must be downloaded from the web server. The following steps
are needed to manage this task:

* The **Flashtool** must retrieve information about all available products on
    the web server.

* The **Flashtool** must select a specific version of a product.

* The **Flashtool** must download the selected products from the web server.

The complexity of this tasks depends on the API of the web server and the 
ability of the used programming language.


### Getting The Files On The Storage Media

The downloaded products must be prepared for deploying on the partitions of the
storage device. Every product refers to a partition of the storage device or
refers to a specific address on the storage device (e.g. boot sector). To manage
this task the following steps must be available on the **Flashtool**:

* The **Flashtool** must contain a distinct mapping of a product to a partition
    or an address on the storage device for each platform and should be
    extensible for future mappings of other platforms.

* The **Flashtool** must copy the product to the storage device. The 

### Usable In Different Environments

The **Flashtool** must be usable for different *embEDUx*
environments. Therefore URLs to the *buildserver* or to repositories should not
be hard coded. 

- User must be able to configure several settings for the **Flashtool**, these
    settings should be saved in a configuration file.

### Main goals for the implementation 

The **Flashtool** must be open for new features and mechanisms to form different
deployment procedures. It is impossible to implement an automation tool which 
fulfills the requirements for all thinkable platforms. So there must be done 
constraints on the implementation of features but the software must be open to 
add new features easily.

- adding new deployment procedures for new platforms if needed.
- adding new commands for the **Flashtool**. 



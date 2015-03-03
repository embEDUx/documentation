## Repository Setup
TODO Lars
TODO Stefan

Setup one repository for each of the components. 

* [U-Boot](uboot)
* [Linux](linux)
* [RootFS](roofs)
* [Miscellaneous files](misc)

TODO
* Permisionss?
* 

## Prerequisites
### Requirements

### Admin-Machine Pre-Requisites
#### Git
* Initializing the aforementioned repositories
* Downloading the setup routine
#### Ansible
* Executing the setuproutinel

### Suggestions
### Authentication as root via SSH-key
* Allowing the setuproutine to access the target buildserver(s)

This is not a strict
  

### buildserver-Machine Pre-Requisites
#### Operating Systems
The buildserver machine must have a recent distribution of Linux installed.
Currently the setup routine supports
* Debian Wheezy and upwards
* Ubuntu 14.04 and upwards
* Gentoo

#### Installed Packages
* SSH Server
* Docker (in case of Gentoo)

### buildserver_setup Repository

### Setup parameters
* hosts inventory
* *buildmaster* configuration
* *buildslave* mapping

## Maintenance
### Adding packages to buildslaves workspace
* [Adding packages to buildslaves](customization/buildslaves-add-packages.md)


## Buildmaster configuration




## Create User-Documentation
The last step is to create the documentation that will be necessary for the
usage of the setup buildserver.

([example](examples/user-documentation_htwg.md)
* Buildbot Webinterface URL

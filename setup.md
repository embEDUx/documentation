## Repository Setup

* [U-Boot](uboot)
* [Linux](linux)
* [RootFS](roofs)
* [Miscellaneous files](misc)

## Installation

### Admin-Machine Pre-Requisites
#### Git
#### Ansible
#### Authentication via SSH-key

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
* [Adding packages to buildslaves](setup/buildslaves-add-packages.md)


## Buildmaster configuration




## Create User-Documentation
The last step is to 

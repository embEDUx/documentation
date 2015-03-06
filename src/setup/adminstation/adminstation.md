# Adminstation Setup
**(work in progress)**

## Prerequisites

### Repositories
* buildserver_setup repository

### Installed Packages
* Git
    * Initializing the aforementioned repositories
    * Downloading the setup routine
* Ansible
    * Executing the setup routine
    * **TODO: explain known bugs with docker-ansible and provide the fixed
      fork**

## Suggestions
### Authentication as root via SSH-key
* SSH root-access to the docker host running the buildslave(s) in question
    * Allows the setup routine to access the target buildserver(s) without
      password

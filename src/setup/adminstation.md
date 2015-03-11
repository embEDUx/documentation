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

## Installation of the Buildserver Setup Routine
**(work in progress)**

### Configure the buildserver IP

### Creating the password vault

1. Starting in the ansible-setup repository directory, the password file can be
   created using the ```ansible-vault``` utility.

        $ cd ${BULDSERVER-SETUP-REPO}
        $ ansible-vault create group_vars/vault.yml

1. Either $EDITOR or vim as fallback will open and present you with an empty
   file. Now create a simple YAML variable named *buildbot_psk* and assign it
   your desired password.

        ---
        buildbot_psk: your_secret_psk
        users:
            embedux: embedux

1. Save and exit the file. That's it!
1. Whenever you want to change something inside the vault file, use

        $ ansible-vault edit group_vars/vault.yml

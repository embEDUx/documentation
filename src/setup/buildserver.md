# Buildserver Setup
**(work in progress)**

## Hardware Requirements

HW-Component | Requirement
--- | ---
CPU | min. 1 Core per Container
RAM | **TODO: estimate**
Storage | **TODO: estimate**
Connectivity | **TODO: estimate**


## Software Requirements
### Operating Systems
The machines must have a recent distribution of Linux installed.
Currently the setup routine supports
* Debian Wheezy and upwards
* Ubuntu 14.04 and upwards
* Gentoo *(will be specified in more detail)*

### Installed Packages
* SSH Server
* Docker (in case of Gentoo)

### Suggestions
* Allow SSH root-access via key authentication
* Understand the [Background Information](../background/background.md)

## Setup parameters
* hosts inventory
* *buildmaster* configuration
* *buildslave* mapping


### Configure the buildserver IP
**(work in progress)**


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

### Install dependencies


```
ansible-playbook -i hosts dependencies.yml --ask-sudo-pass --tags all 
```

### Install the buildserver components

```
ansible-playbook -i hosts buildserver.yml --ask-sudo-pass --ask-vault-pass -e @group_vars/vault.yml --tags all
```


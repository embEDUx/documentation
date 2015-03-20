# Buildserver Setuproutine Evaluation
The buildserver design describes the [setup automation
routine](../design/buildserver.md#setup-automation-routine). It is designed to
install and initialize the different components of the **embEDUx** buildserver
on the buildserver target machine.

The two candidates for the implementation are Python and Ansible. In order to
chose the better alternative, functionality needs to be compared according to
the design specifications and previous evaluation results.

## Executing commands on the target machine
* SSH

* Python
* Ansible


## Configuration Templates
As specified under [configuration generation in the buildserver
design](../design/buildserver.md#required-setup-parameters), template generation
is required during the buildserver setup.


* Python
    
    Several python modules offer template rendering. Among them is the Jinja2
    templating engine which is a suitable candidate.

* Ansible

    A module for Jinja2 template rendering is included with the default Ansible
    setup.

## Package Installation
* apt
* portage


## Docker Container Management
* TODO: explain Docker as eval winner

As specified in the [RootFS evaluation](rootfs.md#conclusion), the
RootFS buildroutine needs Gentoo portage. Therefore, the Docker images for the 
buildserver components will be based on stage3 archives too.

* Download Gentoo stage3 archives for
    * buildmaster - native machine architecture
    * buildslaves - one per target architecture
* Build buildmaster container with the following packages
    * buildbot master component
* Build containers for the the buildslave component.
    * Default buildslaves containers. Build environment for 
        * Native and Cross-Target U-Boot, Linux, Misc, Toolchain
    * RootFS Buildslaves containers. Build environment for
        * Native- and Cross-Target RootFS

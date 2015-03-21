# Buildserver Setuproutine Evaluation
The buildserver design describes the [setup automation
routine](../design/buildserver.md#setup-automation-routine). It is designed to
install and initialize the different components of the **embEDUx** buildserver
on the buildserver target machine.

The two candidates for the implementation are Python and Ansible. In order to
chose the right one, the functionality needs to be compared to the
design specifications and previous evaluation results.

## Python
Python is a general purpose scripting language that offers a wide variety of standard and
additional modules. In theory, there should be no limitation to the complexity
of the setup process when Python is used. It is assumed that Python is already
known to the reader.

## Ansible
Ansible is an administration utility written in Python, with a focus on
automation of predefined actions. The actions that are available correspond to
modules, and can be customized according to the available module parameters.
Standard modules include things like installing packages, enabling system
services, manage user accounts, synchronize files to or from the target
machines, and many more. Ansible can be extended with custom modules, but the
builtin modules already provide great functionality. The connection to the
target machine uses SSH. 
### Quick Introduction
Ansible actions are organized and configured with different entities.  All
entities are defined in separate files, which are specified in the **YAML**
language.

#### Hosts
The first entity that needs to be defined is the hosts inventory. The hosts
inventory contains the address, SSH username and other host specific
information.

* Hosts
* Groups, can consist of several hosts

#### Tasks
Tasks use modules and module parameters to define actions that can be run on
target hosts. Tasks can be reused and grouped into several other entities.

* Tasks
* Roles, can consist of several tasks
* Plays, can include several roles
* Playbooks, can consist of several plays

#### Variables
Variable files can be specified to each element of the previous two entity
groups. There's also a special variable file that, unless overriden,  is valid
for all hosts at all times.


## Setup Steps Evaluation
### Executing commands on the target machine
* SSH

* Python

    Several modules are available, but none seems to make use of an already
    running SSH-agent.
    
* Ansible

    Ansible is based on SSH connections, and uses it as the default method for
    connecting to the target machine. It makes use of already running
    SSH-agents.


### Configuration Templates
As specified under [configuration generation in the buildserver
design](../design/buildserver.md#required-setup-parameters), template generation
is required during the buildserver setup.


* Python
    
    Several python modules offer template rendering. Among them is the Jinja2
    templating engine which is a suitable candidate.

* Ansible

    A module for Jinja2 template rendering is included with the default Ansible
    setup. It can be used for rendering templates to local or remote destination
    paths. Defined ansible variables will be used to replace
    template variables.

### Package Installation
**Docker** is the only non-default package that needs to be installed on the
remote host. 

* apt
* portage


### Docker Container Management
By the time of the design phase, it hasn't been clear yet which container
utility will be used to implement the abstraction. The [container utility
evaluation](container-utility.md) has chosen **Docker**. The necessary steps for
setting up the container infrastructure during the setup can now be listed, in
order to find the right tool for the setuproutine.

As specified in the [RootFS
evaluation](rootfs.md#conclusion), the RootFS buildroutine needs Gentoo portage.
Therefore, the Docker images for the buildserver components will be based on
stage3 archives too.

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


### Result Buildserver Setuproutine Steps Evaluation

Setup steps | Python | Ansible
--- | --- | ---
SSH | Difficult / manual key management | native method / uses SSH-agent
Template Rendering | addon jinja2 module / manual file handling | native jinja2 template module / easy
Package Installation | command module manual SSH commands | native apt module / easy
Docker Container Management | addon docker-py module / manual API calls | native docker module / easy

## Result Buildserver Setuproutine Evaluation
The original criteria can now be analyzed according to the results of the steps
evaluation.

Eval criteria | Python | Ansible
--- | --- | ---
Ready-for-use components availability | ok | ok
Extensibility effort | medium | easy
Templating features | uncomfortable | comfortable
Code readability | good | very good


Even though Python is a scripting programming language with many modules
available, **Ansible** is better for the purpose of automating the given tasks.
It has builtin modules for most of the required tasks.

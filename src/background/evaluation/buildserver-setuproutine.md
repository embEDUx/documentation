# Buildserver Setuproutine Evaluation
The buildserver design describes the [setup automation
routine](../design/buildserver.md#setup-automation-routine). It designed to
install the different components that form the **embEDUx** buildserver. The two
candidates for the implementation are Python and Ansible.

## Python
Python is a general purpose scripting language that offers a wide variety of standard and
additional modules. 

## Ansible
Ansible is an administration utility written in Python, with a focus on
automation of predefined actions. The actions that are available correspond to
modules, and can be customized according to the available module parameters.
Standard modules include things like installing packages, enabling system
services, manage user accounts, synchronize files to or from the target
machines, and many more. Ansible can be extended with custom modules, but the
builtin modules already provide great functionality. The connection to the
target machine uses SSH. 

### Entities
Ansible actions are organized and configured with different entities.  All
entities are defined in separate files, which are specified in the **YAML**
language.

#### Hosts Inventory
The first entity that needs to be defined is the hosts inventory, with optional
groups.

* Hosts
* Groups

#### Tasks
Tasks use modules and module parameters to define actions that can be run on
target hosts. Tasks can be reused and grouped into several other entities.

* Tasks
* Roles
* Plays
* Playbooks


#### Variables
Variables can be attached to each element of the previous two entity groups.

* Variables


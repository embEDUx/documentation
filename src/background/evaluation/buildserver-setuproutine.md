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
automation of predefined tasks,  The
actions that are available correspond to modules that are either

### Entities
All entities are defined in separate files, which are specified in the **YAML**
language.

The different entities can be assembled together.
Target hosts can be grouped together. 

* Hosts
* Groups

Tasks contain the instructions for the modules that takes actions on hosts or
host groups.
Tasks build roles, roles build
plays and plays build playbooks. 
Variables can be defined per entity, globally

* Tasks
* Roles
* Plays
* Playbooks

* Variables


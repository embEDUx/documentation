# Implementation Buildserver Setuproutine

## Ansible Quick Introduction
### Entities
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

## Modules Used

## Tasks Overview

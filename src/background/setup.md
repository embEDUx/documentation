# Setuproutine
The buildserver will undoubtedly be a complex structure of software components.
To make the setup as easy as possible it should be automated as far as possible.

## Required Setup Parameters
The administrator should only have to configure the parameters that can't
possibly be known upfront, or are not convenient to be predefined. At this
point, these parameters include

* Buildserver Machine Address

    The target machine shall by default run all containers that belong to the
    buildsystem

* Authentication credentials between system components

    While this could in general be generated randomly, it is chosen to let the
    user set the credentials for system internal communication.

* Authentication credentials between the system components and the users

    Default usernames and passwords are possible security holes, and should not
    be provided by the setuproutine.


## Default Setup Parameters
All other setup parameters should be provided as defaults by the setuproutine.

* Target Platform and Architectures
    
    The platform names and their corresponding architecture.  The architectures
    will be supported as build targets. By default, all tested platforms
    will be available as supported. The user is not forced to use them, but it
    is useful to already have working examples in the local installation.


## Configuration Generation From Templates
The user-provided and default setup parameters should be used to generate the
configuration files for the buildsystem. For commonly used changes, the
generator can be extended and can be utilized by beginners immediately.
Advanced users will still be able to modify the template if necessary.



## Language Choice
The setuproutine should be automated using an appropriate programming or
scripting language. The candidates for the task are:

* Shell
* Python
* Ansible

The criteria must include:

* Reusable components availability
* Code readability
* Extensibility
* Templating features

# Automated Builds and Setup

## Automated Setup Routine
The buildserver will undoubtedly be a complex structure of software components.
To make the setup as easy as possible it should be automated as far as possible.

### Required Setup Parameters
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

### Optional Setup Parameters These setup parameters are likely to be adjusted
by the administrator, but should be shipped with defaults from the HTWG setup.

* Target Platform and Architectures
    
    The platform names and their corresponding architecture.  The architectures
    will be supported as build targets. By default, all tested platforms will be
    available as supported. The user is not forced to use them, but it is useful
    to already have working examples in the local installation.

### Default Setup Parameters All other setup parameters should be provided as
defaults by the setuproutine.

### Configuration Generation From Templates The configured and default setup
parameters should be used to generate the configuration files for the
buildsystem. For commonly used changes, the generator can be extended and can be
utilized by beginners immediately.  Advanced users will still be able to modify
the template if necessary. 



### Language Choice
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

# Abstraction Layer For Automation
In order to have an automated build system, all components should be setup and
run abstracted from the buildserver's host system as far as possible.
Abstraction methods make it possible to deploy and run complex infrastructures
without having to care about the underlying hardware and system configuration.

Possible technologies for abstracting applications and whole operating systems
include Virtual Machines and Linux Containers.

## Virtualization Machines
Virtual Machines are completely abstracted from the host system's hardware.
They run on a so-called Hypervisor, which simulates a complete machine for the
target system. The target system runs it's own kernel, and needs to boot and
initialize an Operating System from scratch. Security is considered very high,
since the Hypervisor has full control over soft- and hardware-resources that are
passed to the guest system.   The architecture of an operating system inside a
virtual machine can be completely different to the host architecture, and thus
is highly portable.  Depending on available acceleration technologies, the
performance of the virtual CPU, RAM and disk can suffer significantly.

### Linux Containers
Linux Containers utilize a feature in recent Linux Kernels which allow
separating processes from each other. This includes the separation of host and
contained processes, as well as different contained processes from each other.
These contained processes can be an initialization processes to boot a
different Linux System on the running host Linux kernel, or simply any other
application available. Recently there has been a lot of development and
activity on Linux Containers in the community, namely because of a software
called Docker.  Security is highly dependent on the implementation of the
process separating that happens in the host kernel.   The host kernel must
obviously be able to run the contained application.  Therefore, the
application must either be in the host's native or compatible executable
format, or the system needs an emulator to run the foreign architecture. The
performance for contained processes does not differ significantly compared to
a regular running process. This is not entirely true for executables that
require emulation because the CPU instructions must be translated before they
can be run.

### Choosing Linux-Containers
In favor of speed (see [Comparison of VM and Linux
Containers](http://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf))
container technologies should be chosen as the base for the buildsystem
components. In environments where security is a high requirement, the containers
can live inside a virtual machine, but that is beyond the design for the
buildsystem itself.

## Splitting Functionality into Linux Containers
Performance wise, containers are relatively cheap entities for the system. This
allows the buildsystem to be split into several containers for the different
parts of the buildsystem, without losing performance over a flat installation on
the system. The container infrastructure could split the following
functionalities

* One Buildmaster

    Running with native buildserver host architecture, and has the following
    responsibilities

    * Watch all the product repositories for changes
    * Delegate build processes to buildslaves on changes
* Buildslaves with target architecture specific build tools

    Runs emulated or natively with the target architecture, and has the
    following target archtecture specific components:

    * Toolchain
    * Compiler flags
    * Base system archive

### Container Management Software
The choice of the container management software still needs to be evaluated, but in favor
of popularity Docker should be the main candidate. Candidates:

* Docker
* LXC
* OpenVZ

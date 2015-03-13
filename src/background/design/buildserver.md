# Buildserver
**(work in progress)**
This chapter describes the design of the buildserver components and the setup
routine which is used to install these components on the buildserver machine.

## Build Automation
The builds should run in an automated manner as soon as the build specifications
are updated by the user. As the build specifications are stored inside the product
repositories, the buildserver should watch them for changes and trigger a new
build on detected changes. The builds should only be triggered for the products
that received new build specifications in their repositories.

### Main Tasks
* Watch product repositories for changes
* Start build process for detected change

### Additional Tasks and Features
1. Split functionality
    * Repository Observer, Build Scheduler
    * Build Executor
1. Provide an overview of recent and running builds
1. View Log-files or recent and running builds
1. Allow to manually manage build jobs
    * (Re-)schedule builds
    * Cancel builds
1. Flexible build job specifications

All of the above matches exactly to what is generally referred as *continuous
integration*. This topic has received lots of attention from the open source
community and there are a couple of source projects available that could possibly
deliver the needed functionality. The following list of contiuous integration
systems shall be evaluated in order to find the best suiting system.

### Build Automation Candidates
* Gitlab-CI
* Buildbot
* Jenkins

## Setup Automation Routine
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

### Setup Automation Routine Candidates
The setuproutine should be automated using an appropriate programming or
scripting language. The chosen language needs to flexible in detecting
conditions, since every setup run will have different conditions.
The candidates are:

* Python
* Ansible

The criteria that will be evaluated include:

* Reusable components availability
* Task efficiency
* Extensibility effort
* Templating features
* Code readability

## Abstraction Layer For Automation
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

### Splitting Functionality Into Containers
Performance wise, containers are relatively cheap entities for the system. This
allows the buildsystem to be split into several containers for the different
parts of the buildsystem, without losing performance over a flat installation on
the system. The container infrastructure could split the different components of
the continuous integration system into containers.

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

## Linux-Containers Utility Candidates
There is still the choice to make which utility should be used in order to
utilize the Linux-Containers functionality.

* **Docker**
* **LXC**
* **OpenVZ**


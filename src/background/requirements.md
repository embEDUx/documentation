# Project Requirements (HTWG context)
The origin of **embEDUx** plays a big role in the requirements of the whole
project. In the [background introduction](background.md) it is briefly explained
that **embEDUx** aims to create **Linux** distributions for embedded systems in
educational environments. The specific educational environment at the HTWG
consists of several lab-courses, which have specific software requirements on
different hardware platforms.

In order to understand the requirements of **embEDUX**, these requirements need
to analyzed carefully.

## Products - The distribution pieces
The software that is built by the buildserver will be
referred as ***products*** within the further documentation. This helps to
distinguish between software that is used throughout the build system, and
software that is being built uses the build system.

The first action towards implementing the **embEDUx** project is to collect the
necessary requirements. While requirements were exchanged and discussed between
the team members and Prof. Dr. Mächtel, others were identified by analyzing the
lab-specific scenarios.

Hence the resulting set of requirements is a compound of generic requirements to
the nature of the resulting system and requirements that are necessary due to
technicalities.

## Generic Requirements
* Simple to setup and use
* Simple to extend with new hardware platforms
* Usage of mainline sources whenever possible
* User-provided configuration for builds
* Automated setup
* Automated build processes
* Automated deployment process


## Lab-Course Specific Requirements
In order to estimate the requirements list for all lab-courses we need to look
at the lab-courses in detail. 

Lab-Course | HW-Requirements | SW-Requirements
--- | --- | ---
System-Software | RPi | Linux w/ GPIO support, C-(Cross)-Compiler, Bootloader with Netboot support, Webserver, SSH-Daemon
Realtime-Systems | RPi | Linux w/ GPIO, C-(Cross)-Compiler, Bootloader with Netboot support, Various Dev. Applications
ARMrider Project | Iris Board | Linux w/ PWM, GPIO, 802.11s WiFi MESH, UART, Avahi Daemon, C++11-(Cross)-Compiler 
Software-Defined-Radio Project | Utilite Pro, Beaglebone Black, RPi, Banana Pi | Linux w/ USB-debugging and Tracing support, GNUradio Application, USB-Monitoring Userspace-Tools
Operating-Systems | RPi | Linux w/ GPIO, C-(Cross)-Compiler, Python 3.4, various Debugging Tools like valgrind, gdb, etc..: might vary

The students participating in the different courses will develop all kind of
software components on the laboratory computers. Furthermore as the laboratory
computers currently are based on x86_64 architecture a toolchain for
cross-compiling for the target hardware architecture is needed. This toolchain
has to be portable, as those computers are not part of the build system. 

## Hardware Platforms
The following hardware platforms will be used by the lab-courses

Platform | CPU | ARCH 
--- | --- | --- 
Raspberry Pi |  700 MHz ARM11 ARM1176JZF-S  | armv6j_hardfp
Iris Board w/ Colobri T20 | 1.0 GHz ARM Cortex-A9 | armv7a_hardfp 
Beaglebone Black | 1.0 GHz AM335X Cortex-A8 | armv7a_hardfp 
Banana Pi | 1.0  GHz ARM Cortex-A7 | armv7a_hardfp 
Utilite Pro | 1.2 GHz i.MX6 Cortex-A9 | armv7a_hardfp

## Product Specific Requirements
The lab-course specific requirements can now be summed up and ordered by
products. Afterwards, it will be possible to design the system to meet the
product requirements.

### Linux-Kernel
* Support for
    * Raspberry Pi
    * Iris Board (Tegra 2 w/ changed pins)
    * Beaglebone Black
    * Banana Pi
    * Utilite Pro
* GPIO
* UART
* 802.11s WiFi MESH
* USB Debugging
* Tracing

### User-Space applications
* C-(Cross)-Compiler
* C++11-(Cross)-Compiler
* Webserver
* SSH-Daemon
* Avahi Daemon
* iw-utility for configuring 802.11s MESH
* Generic Python Support
    * Python2 for a wide choice of modules
    * Python3 
* Support for arbitrary packages

### Bootloader
* TFTP/BootP Support

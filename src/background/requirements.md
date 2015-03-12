# Project Requirements (HTWG context)
The first action towards implementing the **embEDUx** project is to collect the
necessary requirements. While requirements were exchanged and discussed between
the team members and Prof. Dr. Mächtel, others were identified by analyzing the
lab-specific scenarios.

Hence the resulting set of requirements is a compound of generic requirements to
the nature of the resulting system and requirements that are necessary due to
technicalities.

## Generic Requirements
The generic and automated approach that needs to be found by this project must
meet the sum of the requirements for every single lab-course. The determination
for this set of requirements has to be done in two phases.

## Lab-Course Specific Requirements
In the first phase, lab-course specific requirements need to be collected.

#### Lab-Course Overview
Lab-Course | HW-Requirements | SW-Requirements
--- | --- | ---
System-Software | RPi | Linux w/ GPIO support, C-(Cross)-Compiler, Bootloader with Netboot support, Webserver, SSH-Daemon
Realtime-Systems | RPi | Linux w/ GPIO, C-(Cross)-Compiler, Bootloader with Netboot support, Various Dev. Applications
ARMrider Project | Iris Board | Linux w/ PWM, GPIO, 802.11s WiFi MESH, UART, Avahi Daemon, C++11-(Cross)-Compiler 
Software-Defined-Radio Project | Utilite Pro, Beaglebone Black, RPi, Banana Pi | Linux w/ USB-debugging and Tracing support, GNUradio Application, USB-Monitoring Userspace-Tools
Operating-Systems | RPi | Linux w/ GPIO, C-(Cross)-Compiler, Python 3.4, various Debugging Tools like valgrind, gdb, etc..: might vary

### Hardware Platforms
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
    * Raspberr Pi
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



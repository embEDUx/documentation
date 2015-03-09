# Project Requirements (HTWG context)
**(work in progress)**

The generic and automated approach that needs to be found by this project must
meet the sum of the requirements for every single lab-course. The determination
for this set of requirements has to be done in two phases.
  
In the first phase, lab-course specific requirements need to be expressed, while
the second phase consists of breaking them down to their elements to extract
similarities and form requirements that are generic enough to meet every
lab-course's requirements. An additional phase of finding requirements
will take place in an early phase of implementation, adding requirements by
analyzing the feature road-maps for the chosen technologies and by respecting
changes that will happen in the near future.

## Phase 1

### Lab-Course Overview
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

## Phase 2

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
    * Python2.7 for a wide choice of modules
    * Python3.4 
* Support for arbitrary packages

### Bootloader
* TFTP/BootP Support

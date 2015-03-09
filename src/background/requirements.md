# Project Requirements 
**(work in progress)**

The generic and automated approach that needs to be found by this project must
meet the sum of the requirements for every single lab-course. The determination
for this set of requirements has to be done in three phases.
  
In the first phase, lab-course specific requirements need to be expressed, while
the second phase consists of breaking them down to their elements. Phase three
is to extract similarities and form requirements that are generic enough to meet
every lab-course's requirements. An additional phase of finding requirements
will take place in an early phase of implementation, adding requirements by
analyzing the feature road-maps for the chosen technologies and by respecting
changes that will happen in the near future.

## Hardware Platforms
The hardware platforms that will be used by the lab-course. 

Platform | CPU | ARCH 
--- | --- | --- 
Raspberry Pi |  700 MHz ARM11 ARM1176JZF-S  | armv6j_hardfp
Iris Board w/ Colobri T20 | 1.0 GHz ARM Cortex-A9 | armv7a_hardfp 
Beaglebone Black | 1.0 GHz AM335X Cortex-A8 | armv7a_hardfp 
Banana Pi | 1.0  GHz ARM Cortex-A7 | armv7a_hardfp 
Utilite Pro | 1.2 GHz i.MX6 Cortex-A9 | armv7a_hardfp

## Bootloader
As some platforms at the HTWG are already running with **Das U-Boot** as
bootloader, a soft requirement is **U-Boot**. However the software solution must
not be restricted to a specific **U-Boot** version.

## Kernel
No specific **Linux** kernel version is required and the software solution must
not be restricted to a specific kernel version.

## RootFS 
The software solution must not restrict the user in his choice of available
applications or libraries, although the common distribution restrictions (eg.
Application is not available/updated in package manager) can still apply.

## Portability 
Software solutions must be easy to setup on various architectures. 

## Extensibility 
Adding support for additional hardware platforms must be simple. 

## Other 
Platform specific source code must be avoided as far as possible. 


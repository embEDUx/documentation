The generic and automated approach that needs to be found
by this project must meet the sum of the requirements for
every single lab-course. The determination for this set of
requirements has to be done in three phases.  In the first
phase, lab-course specific requirements need to be
expressed, while the second phase consists of breaking
them down to their elements. Phase three is to extract
similarities and form requirements that are generic enough
to meet every lab-course's requirements. An additional
phase of finding requirements will take place in an early
phase of implementation, adding requirements by analyzing
the feature road-maps for the chosen technologies and by
respecting changes that will happen in the near future.


## Criteria

Before any requirements can be acquired it is necessary to
determine which criteria matter. This section eventually
be updated during the process of requirements gathering.

The criteria will be collected per *lab-course*.

Criteria | Description (+ examples) 
--- | --- 
Hardware Platforms | The hardware platforms that will be used by the lab-course. 
Kernel | Kernel specific requirements like a minimum kernel-version, available drivers
User-Space | Available applications or libraries, applied configuration, package management, Debugging Symbols, ...
Portability | Software solution must be easy to setup on various architectures 
Extensibility | New hardware platforms can be added to the software solution with minimal effort 
Roles | There are different user roles which use the software solution. (e.g. Administrator, who sets up the software solution. User, who wants to set up a platform. etc. 
Other | Uncategorized requirements

## Platforms
### Hardware overview

Platform | CPU | STAGE3 ARCH | CHOST | CFLAGS | qemu-arm cpu model
--- | --- | --- | --- | --- | ---
Raspberry Pi |  700 MHz ARM11 ARM1176JZF-S core [[S]](http://elinux.org/RPi_Hardware)  | armv6j_hardfp |  armv6j-hardfloat-linux-gnueabi **TODO CHECK** | -O2 -march=armv6j -mfpu=vfp -mfloat-abi=hard [[S]](http://wiki.gentoo.org /wiki/Raspberry_Pi) | arm1176
IRIS Board | NVIDIA Tegra2: 1.0 GHz ARM Cortex-A9 | armv7a_hardfp | ??? [[S]](http://dev.gentoo.org/~armin76/arm/tegra2/install.xml) | **NO NEON SUPPORT** | ---
Beaglebone Black | 1.0 GHz AM335X Cortex-A8 | armv7a_hardfp |  --- | --- | ---
__Overview: Information for building software per platform__
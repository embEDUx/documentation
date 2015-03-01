# Introduction to embEDUx
*(stjunker)*

The name *embEDUx* includes hints for the words **embedded linux** and
**education**. The idea is to deliver an environment that eases the effort of
creating various embedded linux distributions depending on the educational
purpose that they are specifically aiming for.

The idea has its origin at IT-faculty at the HTWG Constance, where embEDUx will
have the use-case of preparing and maintaining linux distributions for the
different lab-courses taken by students. All of these lab-courses evolve around
the linux operating system, software applications for linux and hardware
components that are capable of running linux. Over time, the diversity in soft-
and hardware utilized in these lab-courses has increased and so has the
complexity and effort to prepare and maintain the systems in use.  

The embEDUx project has been created to find a generic and automated approach
for tasks concerning the preparation of soft- and hardware for these lab-courses
offered at the HTWG, which is the reason why the embEDUx requirements will have
a strong bias towards the requirements specific to the lab-courses.

## Terminology
Before you continue reading the different documentation snippets, please read 
through [Terminology](Terminology.md) for terms used within the documentation.


## Components
The embEDUx build system has been designed to build the following components
according to user-provided specifications:
- Das U-Boot Bootloader
- Linux Kernel images and modules
- RootFS-archives based on Gentoo


## Usage Information
If you have access to a setup instance of the embEDUx build system and want to 
start using it please goto [USAGE.md](USAGE.md). You will learn how to build the
components offered by the system.


## Setup Information
If you want to run the embEDUx build system on your own machine(s), please
consult [SETUP.md](SETUP.md)


## Background Information
For information on the development and the made decisions, please consult 
[BACKGROUND.md](BACKGROUND.md)

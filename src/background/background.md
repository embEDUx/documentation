# Background
## Overview
#### [1. Project Requirements](requirements.md)
#### [2. Design](design.md)
#### [3. Evaluation](evaluation.md)
#### [4. Implementation](implementation.md)

## The Beginning
The name **embEDUx** includes hints for the words *embedded* ***Linux*** and
*education*. The goal to deliver an environment that eases the effort of creating various
embedded **Linux** distributions depending on the educational purpose that they are
specifically aiming for. 

The project has its origin at the IT-faculty at the HTWG Constance, where
embEDUx will have the use-case of preparing and maintaining **Linux**
distributions for the different lab-courses taken by students. All of these
lab-courses evolve around the **Linux** operating system, software applications
for **Linux** and hardware components that are capable of running **Linux**. Over
time, the diversity in soft- and hardware utilized in these lab-courses has
increased and so has the complexity and effort to prepare and maintain the
systems in use.  

The embEDUx project has been created to find a generic and automated approach
for tasks concerning the preparation of soft- and hardware for the lab-courses
at the HTWG. Naturally, that's why the embEDUx requirements will have a strong
bias towards the requirements specific to the lab-courses.

## What is it, and what can it do?
* Automated build system for complete customized Linux distributions
* Easy to setup via the configurable setuproutine
* Centralized build configurations for all your platforms
* Individual configuration and builds with specified targets, organized by
    * Platform: for Linux-Kernel, U-Boot
    * Architecture: RootFS
    * Hybrid: Toolchain, Misc-Files
* Working examples for Raspberry Pi, Beaglebone Black, Banana Pi, Utilite Pro

## What is it not?
* Magic system for guessing all your platforms configuration automatically


## Initial contributors
The project started off with three master students of computer science who have
been working on this project in a team, supervised by a professor. Namely, these are

* Prof. Dr. Michael Mächtel
* Lars Eckervogt
* Manuel Hieke 
* Stefan Junker

Head over to the [contacts and support page](../support/contact-team.md) if you
want to contact any of these people.

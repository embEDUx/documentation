# Terminology
The introduction and the following sections contains terms that will be
explained or respectively defined in this chapter. For the scope of the embEDUx
project, these terms will be assumed as known by any reader or other participant
in the project. As a reminder this section includes explanations to important
terms and techniques used by Linux which are essential for this project.

## ABI (application binary interface)
In computer software, an application binary interface (ABI) is the interface
between two program modules, one of which is often a library or operating
system, at the level of machine code. An ABI determines such details as how
functions are called and in which binary format information should be passed
from one program component to the next, or to the operating system in the case
of a system call. ([Source](http://en.wikipedia.org/wiki/Application_binary_interface))

## Architecture
Architecture refers to a CPU's type of architecture. The CPU architecture
defines a set of CPU instructions that are known to the CPU. In the process of
software development and compilation, the supported CPU instructions are a very
important thing to keep in mind. Software that has been compiled specifically
for one architecture type is likely to misbehave or fail to work on other
architecture type, because the CPU will not be able to run the instructions
given by application's binary code. The linux kernel supports a wide range of
architectures and can therefore be run on many different systems.

## Bootloader
The boot loader is the first piece of software started by the BIOS or UEFI. It
is responsible for loading the kernel with the wanted kernel parameters, and
initial RAM disk before initiating the boot process.
([Source](https://wiki.archlinux.org/index.php/Boot_loaders))

## ELF
ELF (Executable and Linkable Format) is a format for binary application files.
If configured to, the linux kernel is able to execute these kind of files. It is
a very common file format for applications compiled for linux but is also found
and used by other operating systems. An important fact to know about the
ELF-format is that it contains a value to the key
[e_machine](http://www.sco.com/developers/gabi/2000-07-17/ch4.eheader.html) that
specifies the target instruction set architecture. Examining this section and
knowing the it's native architecture, an operating system is able to determine
if it is capable of executing a given binary application file. Exceptions to
this are situations where the system is running on a sub-architecture that is
not compatible with the sub-architecture that a binary has been compiled for. 
Unfortunately this is very likely to happen nowadays when dealing with different
sub-architectures of the ARM architecture.

## Kernel-Space
Kernel-Space refers to software that is executed by the linux kernel inside it's
own context This context is defined by memory space and provided permissions.
Kernel-Space software is either compiled into the kernel and shipped with it, or
it can be loaded at runtime from a kernel module file.

## (Linux) Kernel
Kernel refers to the linux kernel which is the core application providing linux'
main functionality. It is responsible for initializing and driving the system's
hardware resources. 

## Linux
Linux is the operating system of choice for the embEDUx project. In order to
work on or with embEDUx a fair knowledge about Linux is mandatory and assumed to
be present on users and developers involved in the project.

## Platform
The platform specification refers to a system's hardware configuration. It is
defined by the system's CPU architecture and peripherals that are connected to
the CPU. The term platform is often interchanged with the term board, but it
should be kept in mind that a system can consist of multiple boards that are
stacked upon each other.

## Root-Filesystem *(RootFS*)
The RootFS is a collection of software that is executable by a system running
the linux kernel. It can stored on many different types of storage, from which
it can be loaded by the linux kernel. The location and content of a RootFS is
heavily dependent on the purpose of the system it is designed for.

## Sub-Architecture
Architectures can be further specialized as sub-architectures. Sub-architectures
are not necessarily compatible to other sub-architectures within their common
architectures.

## (Cross-)Toolchain
A toolchain is a set of applications that are able to compile source code to
executable binary files. The toolchain produces binary files executable by a
specific architecture type, by translating the source code to CPU instructions
included in the architecture. The toolchain's own applications are, like any
other application, compiled for a specific architecture type. If this
architecture differs from the toolchain's target architecture it is considered a
cross-toolchain and the process is called cross-compilation.

## User-Space
The user-space context is defined by a memory space and provided permissions
strictly separated by the kernel-space. An application running in the a
user-space context is not able to access the kernel-space, or the user-space
context of other applications

# Links

[1] http://www.sco.com/developers/gabi/2000-07-17/ch4.eheader.html

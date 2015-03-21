# Creating the User Documentation
The user documentation is essential to the usage of the buildserver that has
been setup. You are encouraged to create the documentation carefully, and
double-check any information you put in. 

## Example User Documentation
If you want to see some examples, you can take a look at one of these:

* [Demo User Documentation](../examples/user-documentation-DEMO.md).  
* [HTWG User Documentation](../examples/user-documentation-HTWG.md).  

## Gather information from the **master.cfg configuration**
Most of the information that is provided to the user derives from the
buildserver setup. By default, the only information provided by the
Administrator were the credentials and the address of the buildserver. Therefore
it should be straight forward to put the user documentation together, and can in
most cases be very similar to the provided examples.

In general **nobody is asking you to include any passwords in here**.

## Product Repository URLs
The http(s) URLs for the Git-repositories of all products must be included.

* U-Boot
* Linux
* RootFS
* Miscellaneous files
* Toolchains

## Web-Interfaces
The Web-Interfaces for the buildserver(s) must be included.

## Product Download URLs
The download URLs for all products must be included. These are usually based on
the Web-Interface URL(s) from the previous chapter.

* U-Boot
* Linux
* RootFS
* Miscellaneous files
* Toolchains

## Platform Strings
For each of your platforms, you need to provide 
* Platform-String 
* RootFS-String 
* Toolchain-String

## Build Commands
For every product, the build command needs to be included. The command's will
be run in the spec-repositories.  These are the defaults if you haven't changed
any buildsteps in the **master.cfg**

Product | Buildcommands
--- | --- 
Linux | './build'
Uboot | './build'
Misc | './build'
Toolchain | './build'
RootFS | *does not apply*

## Output Directories
For every product, the output directory needs to be included.  The content of
this directory will be available for download on the buildserver's
web-interface.  These are the defaults if you haven't changed any buildsteps in
the **master.cfg**

Product | Output Folder
--- | --- 
Linux | output
Uboot | output 
Misc | output
Toolchain | output
RootFS | *does not apply*

## Output File-Scheme
For every product, the output file-scheme needs to be included.
These are the defaults if you haven't changed any buildsteps in the
**master.cfg**. **WARNING:** if your setup differs from these defaults, the
[Flashtool](../../background/design/flashtoolmd) will not work as expected.

Product / Description | Nr of Files / File-Scheme
--- | ---
**Linux** | 3
Linux Blob | < branch-name \>\_< date&time \>\_< commit-hash \>\_boot.tar.bz2
Modules+Sources | < branch-name \>\_< date&time \>\_< commit-hash \>\_root.tar.bz2
Linux config | < branch-name \>\_< date&time \>\_< commit-hash \>\_config.tar.bz2
**Uboot** | 1
Uboot Blob | < branch-name \>\_< date&time \>\_< commit-hash \>\_uboot.tar.bz2
**Misc** | 2
Additional Boot Files | < branch-name \>\_< date&time \>\_< commit-hash \>\_boot.tar.bz2
Additonal Root Files| < branch-name \>\_< date&time \>\_< commit-hash \>\_root.tar.bz2
**Toolchain** | 1
Toolchain | < branch-name \>\_< date&time \>\_< commit-hash \>\_toolchain.tar.bz2
**RootFS** | 2
Rootfs Archive | < branch-name \>\_< date&time \>\_< commit-hash \>\_rootfs.tar.bz2
Portage Snapshot | < branch-name \>\_< date&time \>\_< commit-hash \>\_portage.tar.bz2

### Variable Descriptions
Variable | Note
--- | ---
branch-name | The branch that triggered the build
date&time | YYYYMMDDhhmmss
commit-hash | Short version of the hash for the commit which triggered the build

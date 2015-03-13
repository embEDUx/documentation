# Implementation Misc
Throughout the development we realized, that some platforms need files present
at the boot partition. However these files couldn't be assigned logical to any
of the existing repositories. Therefore we added the *misc-spec* repository. It
basically contains the files that have to be provided either to the boot or the
root partition. 

* Each platform has one branch within the repository. 
* Each branch contains two folder *src_boot* and *src_root*.
* The files lay within this folder within their folder structure (e.g.
  src_root/etc/inittab). 
* The build script only packs content of the two folder into two archives.

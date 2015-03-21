# Summary
Starting into the **embEDUx** world with an almost fully automated setup routine
lowers the initial hurdles for interested users and administrators.

With using a continuous integration system as backend the users don't need to
gain the knowledge about the structure of the **embEDUx** build system. Another
benefit is the integrated frontend, which provides a nice web interface for
monitoring, triggering and canceling the build jobs.

Using **Git** repositories as storage units forces the user to use a version
control system, which also benefits the user in case of needed collaboration.

A great benefit of the **embEDUx** build system is the total freedom of choice
for each versions of **U-Boot** and the **Linux** kernel, while keeping the
  common and well known configuration steps. When using the provided example
  build scripts the chances of further needed modifications are left at a
  minimum. However if needed the build can be complete rewritten by the user,
  which leaves a high flexibility in structuring the build steps and therefore
  the build process. Using **Gentoo** respectively **Portage** as part of the
  RootFS gives the user a great choice for plenty of recent software packages.

## Keywords
* automated setup
  * low initial hurdles for administrator
  * still highly extensible, although requires more knowledge of the complex system
* continuous integration
  * build monitoring (buildbot, CI)
  * version control and collaboration through use of git
  * user needs only low knowledge of structure of the build system
* freedom of choice for sources (kernel/uboot)
* plenty of recent software packages (gentoo/portage)
* provided example build scripts cover common build processes
  * build process (kernel/uboot/toolchain/mics) through build scripts highly flexible
* possibility of manual or semi-automatic (flashtool) deployment
* cross target support


## 
As the **embEDUx** build system has the educational purpose in mind, this system
provides a great framework for students to configure **U-Boot**, **Linux** Kernel
and a RootFS in a more or less defined way. The overhead for the students using
the **embEDUx** build system is kept at a minimum.


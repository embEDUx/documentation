# Toolchains
This guide will help you through the steps to build a toolchain for the
architecture of your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](../setup/user-documentation.md).

* Git Repository *toolchains*
* **Buildserver** setup for desired platform architecture
* Crosstool NG [ct-ng](http://crosstool-ng.org/) locally installed.

### Suggestions
* Build/download a toolchain. This will allow you to test your build
  configuration before you push it upstream.

* Have a look at the default build scripts. As the **Buildserver** just executes
  these scripts, you have no limits on what you want to do before, during and
  after the build process.

## Name scheme
The **Builserver** can only build your images, if you follow this name scheme
for any of the branches:

* <host-arch\>\_<target-arch\>-ctng-linux-<abi\>

Please look up the target-arch  string in the [User
Documentation](../setup/user-documentation.md) provided by your administrator. If
your platform doesn't exist yet, please contact your administrator.

## Add a new toolchain
Following steps are necessary to add a toolchain to the *toolchains* repository.

1. Clone the *linux* repository with the URL provided in the user documentation.
  
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/toolchains.git
    ```
 
1. Add a *toolchain* branch to the *toolchains* repository. Follow the [name
   scheme](#name-scheme) carefully.
   
    ```
$ git checkout master
$ git branch amd64_armv6j-ctng-linux-gnueabi
$ git checkout amd64_armv6j-ctng-linux-gnueabi 
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin amd64_armv6j-ctng-linux-gnueabi
    ```

1. Add the [default build script](usage/toolchains/template/build) as ***build*** to the repository
   and make it executable.
   
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 470 Mar  3 20:52 build
-rw-r--r-- 1 user user   0 Mar  3 20:51 README
    ```

1. Configure your desired toolchain with *ct-ng* and add the ***.config*** to
   the branch. In this case we will just use a default configuration, with
   some mandatory modifications. For further information read
   [background/toolchains](../background/toolchains.md).

1. Test your toolchain configuration
  
    ```
   $ ct-ng build
    ```

1. Add the files, commit and push upstream.
   
    ```
$ git add build
$ git commit -m "new toolchain for amd64 -> armv6j"
$ git push 
    ```

1. The **Buildserver** should start building your kernel image now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).

1. Congratulations, you just built your first toolchain. You can now download
   the toolchain. Find the toolchain component URL in the [User
   Documentation](../setup/user-documentation.md) (see [Hardware
   Deployment](usage.md#hardware-deployment)).


# Toolchains
This guide will help you through the steps to build a toolchain for the
architecture of your desired platform.

## Prerequisites
All of [the common prerequisites apply](../../usage/usage.md#Prerequisites).

### Requirements
* User Documentation.

    At the end of the setup, the Administrator is instructed to create the [User
    Documentation](user-documentation.md).

* Git Repository *toolchains-specs*
* **buildserver** setup for desired platform architecture
* Crosstool NG [ct-ng](http://crosstool-ng.org/) locally installed.

### Suggestions
* Build/download a toolchain. This will allow you to test your build
  configuration before you push it upstream.

* Have a look at the default [build script](setup/post-install/toolchains/default/toolchain_build). As
  the **buildserver** just executes these scripts, you have no limits on what
  you want to do before, during and after the build process.

## Branch Name-Scheme
The **builserver** can only build your images, if you follow the correct
name-scheme for the branches.

The variables that are needed for your platform can be found in the [User
Documentation](user-documentation.md).

### Variables

Variable | Notes
--- | ---
host-arch | Architecture of the host system (where the toolchain is used)
taget-arch | Specified and mapped to the target architecture by the Administrator. Found in the [User Documentation](user-documentation.md)
abi | Application Binary Interface (selected by toolchain configuration)

### Branches

Branch | Scheme | Example
--- | --- | ---
toolchain | < host-arch \>\_< target-arch \>-ctng-linux-< abi \> | armv6j-ctng-linux-gnueabi 

## Step-by-Step Example
The following example will give you a detailed overview of the necessary steps
to build the toolchain for the raspberry pi (armv6j). We assume that at this point the
*toolchains-specs* repository is empty.

## Add a new toolchain

1. Clone the *toolchains-specs* repository with the URL provided in the user documentation.
  
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/toolchains.git
    ```
 
1. Add a *toolchain* branch to the *toolchains-specs* repository. It is necessary that you
   push the branch at this point upstream, so the **buildserver** can find the
   new *toolchain* branch.
   
    ```
$ git checkout master
$ git branch amd64_armv6j-ctng-linux-gnueabi
$ git checkout amd64_armv6j-ctng-linux-gnueabi 
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin amd64_armv6j-ctng-linux-gnueabi
    ```

1. Add the [default build script](setup/post-install/toolchains/default/toolchain_build) as
   ***build*** to the branch and make it executable.
   
    ```
$ ls -hl
    ```

        total 4.0K
        -rwxr-xr-x 1 user user 470 Mar  3 20:52 build
        -rw-r--r-- 1 user user   0 Mar  3 20:51 README

1. Configure your desired toolchain with **ct-ng** and add the ***.config*** to
   the branch. In this example we will just use a sample configuration (`ct-ng armv6-rpi-linux-gnueabi`)
   and modify the [configuration](usage/toolchains/default/.config), to build a
   static toolchain. For further information read
   [background/toolchains](../../background/specs/toolchains.md).

1. Test your toolchain configuration
  
    ```
   $ ct-ng build
    ```

1. Add changes, commit and push them upstream. 
   
    ```
$ git add build
$ git commit -m "new toolchain for amd64 -> armv6j"
$ git push 
    ```

1. The **buildserver** should start building your toolchain now. For further
   informations on how to monitor the build check [monitoring
   guide](../../usage/common/build-monitoring.md).

1. Congratulations, you just built your first toolchain for the platform
   architecture. Find the toolchain product download URL in the [User
   Documentation](user-documentation.md) (see [Hardware
   Deployment](../../usage/usage.md#hardware-deployment)).


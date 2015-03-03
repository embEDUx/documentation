# Toolchains
This guide will help you through the steps to build a toolchain for the
architecture of your desired platform.

## Prerequisites
All of [the common prerequisites apply](usage.md#Prerequisites).

### Requirements
* Git Repository *toolchains*
* **Buildbot** setup for your host architecture.
* Crosstool NG [ct-ng](http://crosstool-ng.org/) locally installed.

## Name scheme 
**Buildbot** can only build your toolchains, if you follow this naming schema

* <host\_arch\>\_<target\_arch\>-ctng-linux-<abi\>

## Add a new toolchain
Following steps are necessary to add a toolchain to the *toolchains* repository.

1. Clone the *toolchains* repository. The URL should have been provided to you
   by your system administrator.
  
    ```
$ git clone git@apu.in.htwg-konstanz.de:labworks-embEDUx/toolchains.git
    ```
 
1. Add a *toolchain* branch to the *toolchains* repository. Follow the [name
   schema](#name-schema) carefully.
   
    ```
$ git checkout master
$ git branch amd64_armv6j-ctng-linux-gnueabi
$ git checkout amd64_armv6j-ctng-linux-gnueabi 
$ touch README.md
$ git add README.md
$ git commit -m "inital commit"
$ git push --set-upstream origin amd64_armv6j-ctng-linux-gnueabi
    ```

1. Add the [build script](toolchains/template/build) as ***build*** to the repository
   and make it executable.
   
    ```
$ ls -hl
total 4.0K
-rwxr-xr-x 1 user user 470 Mar  3 20:52 build
-rw-r--r-- 1 user user   0 Mar  3 20:51 README
    ```

1. Configure your desired toolchain with *ct-ng* and add the ***.config*** to
   the repository. In this case we will just use a default configuration, with
   some mandatory modifications. For further information read
   [background/toolchains](../background/toolchains.md).

1. Test your toolchain configuration
  
    ```
   $ ct-ng build
    ```

1. Add the files, commit and push. 
   
    ```
$ git add build
$ git commit -m "new toolchain for amd64 -> armv6j"
$ git push 
    ```

1. The **Buildbot** should start building your toolchain now. For further
   informations on how to monitor the build check [monitoring
   guide](common/build-monitoring.md).


# Local Testing 
Sometimes it is necessary to test your build scripts locally on your machine. As
most of the time your target platform is a different platform than your host
machine, you need to use a cross toolchain. You will learn how to use the
toolchain in this chapter.

## Requirements
* Toolchain Download URL from User Documentation
* Necessary software to run the build script
    * Git
    * wget
    * diff
    * patch
    * tar

## Step-by-Step Example
The following example is based on modifying the ***build*** script for the
**Linux** kernel for the raspberry-pi. We assume that you already have your
files according to [Usage/Linux](../usage/linux.md).

1. Get the toolchain product download URL from your [User
Documentation](../setup/post-install/user-documentation.md) then download and
extract the toolchain archive *amd64_armv6j-ct-ng-linux-gnueabi* to
*/opt/toolchain/amd64_armv6j-ct-ng-linux-gnueabi/*

    ```
$ wget http://moe.in.htwg-konstanz.de:8010/toolchains/armv6j-ctng-linux-gnueabi/amd64_armv6j-ctng-linux-gnueabi_20150306112501_f5cb21e_toolchain.tar.bz2
    ```

        --2015-03-09 13:00:34--  http://moe.in.htwg-konstanz.de:8010/toolchains/armv6j-ctng-linux-gnueabi/amd64_armv6j-ctng-linux-gnueabi_20150306112501_f5cb21e_toolchain.tar.bz2
        Resolving moe.in.htwg-konstanz.de... 141.37.31.240
        Connecting to moe.in.htwg-konstanz.de|141.37.31.240|:8010... connected.
        HTTP request sent, awaiting response... 200 OK
        Length: 80099059 (76M) [application/x-tar]
        Saving to: ‘amd64_armv6j-ctng-linux-gnueabi_20150306112501_f5cb21e_toolchain.tar.bz2’
        
        amd64_armv6j-ctng-l 100%[=====================>]  76.39M  3.48MB/s   in 20s    
        
        2015-03-09 13:00:54 (3.88 MB/s) - ‘amd64_armv6j-ctng-linux-gnueabi_20150306112501_f5cb21e_toolchain.tar.bz2’ saved [80099059/80099059]

    ```
$ sudo mkdir /opt/toolchain
$ tar -xf amd64_armv6j-ctng-linux-gnueabi_20150306112501_f5cb21e_toolchain.tar.bz2 -C /opt/toolchain
    ```

1. Set the necessary environment variables

    ```
$ export ARCH=arm
$ export CROSS_COMPILE=/opt/toolchain/armv6j-ctng-linux-gnueabihf/bin/armv6j-ctng-linux-gnueabihf-
$ export EMBEDUX_TMP=/var/tmp
    ```

1. Now you can execute the build script.

    ```
$ ./build
    ```

        + KERNEL_VERSION=4.18.1
        + KERNEL_DTB=
        + KERNEL_CONFIG=.config
        + KERNEL_IMG=zImage
        + SRC_DIR=linux
        ++ git remote -v
        ++ sed -n '/.git/{p;q;}'
        ++ awk '{print $(NF-1)}'
        + git clone -b 3.18.1 --depth 1 --single-branch git@apu.in.htwg-konstanz.de:labworks-embEDUx/linux.git linux
        Cloning into 'linux'...
        ... 

Any errors that occur during the build process should be fixed before you push
the build script upstream! If you build script runs locally, it should also run
on the buildserver. Please test the script locally, and confirm it works, before
you contact an Administrator.


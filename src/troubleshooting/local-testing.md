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

## Run the build script

There are a couple of steps required to execute your script with the toolchain.

1. Download the proper toolchain for your platform with the URL provided in the
   [User Documentation](../setup/post-install/user-documentation.md)

1. Following environment variables are needed

    ```
    $ export ARCH=< architecture >
    $ export CROSS_COMPILE=< path to toolchain/bin/xxx- >
    $ export EMBEDUX_TMP=< tmp-path-to-store-files >
    ```

1. Execute the build script

    ```
    $ ./build
    ```

Any errors that occur during the build process should be fixed before you push
the build script upstream! If you build script runs locally, it should also run
on the buildserver. Please test the script locally, and confirm it works, before
you contact an Administrator.


# Entering Build Environment
If you run into trouble while building a product, you can SSH into the
build environment to analyze any possible root of the problem.

The following example shows entering the docker container that is used to build
the products for the amd64 Architecture. In this example, the host *buildserver*
is running the container that runs the respective buildslave.

## Requirements
* SSH-Access to the host on which the buildslave containers are running
* Permissions to run `docker` on the buildslave container host

## Step-By-Step Example
This example demonstrates how to enter a running instance of a build
environment of a amd64 buildslave running on an amd64 host.

1. SSH into the host

    ```
    $ ssh root@buildserver
    buildserver ~ # arch
    x86_64
    ```

1. Execute an interactive `bash`-shell inside the buildslave container

    ```
    buildserver ~ # docker exec -it buildslave_amd64.amd64 bash
    buildbot@52e612976b16 / $
    ```

1. Switch to the working directory, where the build slave is processing the
   ***build*** script.

    ```
    buildbot@52e612976b16 / $ cd /var/lib/buildslave/amd64/build
    ```


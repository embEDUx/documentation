# Entering RootFS Build Environment

If you run into trouble while building a RootFS, you can SSH into the
build environment. The following example shows entering the VM that is used to
build RootFS for the armv7a\_hardfp Architecture. In this example, the host *buildserver* is
running the container that runs the respective buildslave.

## Requirements
* SSH-Access to the host on which the buildslave containers are running
* Permissions to run `docker` on the buildslave container host

## Step-By-Step Example
This example demonstrates how to enter a running instance of a build
environment of a rootfs\_armv7a\_hardfp buildslave running on an amd64 host.

1. SSH into the host

    ```
    $ ssh root@buildserver
    buildserver ~ # arch
    x86_64
    ```

1. Execute an interactive `bash`-shell inside the buildslave container

    ```
    buildserver ~ # docker exec -it buildslave_rootfs_amd64.armv7a_hardfp bash
    buildbot@1355a15e64aa / $
    ```

1. SSH into the buildslave's instance of the build environment, using the
   SSH-key that has been generated during the build process
   
    ```
    buildbot@1355a15e64aa / $ ssh root@localhost -p 2222 -i /var/tmp/embedux/target_prepare/ssh_creds/target.id
    The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
    ED25519 key fingerprint is 11:b6:d6:73:40:ba:92:42:c9:d8:cc:a2:bb:b2:73:3a.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '[localhost]:2222' (ED25519) to the list of known hosts.
    root@localhost ~ # arch
    armv7l
    ```

1. If no other build happened in since your failed build, you are exactly
   where the failed build left off, good luck!

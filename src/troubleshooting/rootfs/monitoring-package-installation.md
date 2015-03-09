# Monitoring the Package Installation

If you're wondering what a step of the RootFS build routine is doing, you have
toe option of [entering the RootFS build
environment](entering-build-environment). The reason for this is mainly
to check if the build is still ongoing, or if it got stuck at one point without
committing a failure.

## Requirements
* SSH-Access to the host on which the buildslave containers are running
* Permissions to run `docker` on the buildslave container host
* Completed the steps of [entering the RootFS build
  environment](entering-build-environment).

## Step-By-Step Example
This example demonstrates how to check the system load and the logs of the
running package installation.

1. The example starts with already being logged into the SSHd inside the buildslave.

    ```
root@localhost ~ # arch
    ```

        armv7l

1. Use `top` to check the system load. Beforehand, you need to set the `TERM`
   environment variable, otherwise `top` will refuse to work.

    ```
root@localhost ~ # export TERM=vt200
root@localhost ~ # top
    ```

        top - 09:02:20 up 1 day, 18:11,  2 users,  load average: 1.80, 1.65, 1.61
        Tasks:  88 total,   2 running,  86 sleeping,   0 stopped,   0 zombie
        %Cpu(s): 97.8 us,  2.2 sy,  0.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
        KiB Mem:   1797116 total,  1453628 used,   343488 free,        8 buffers
        KiB Swap:        0 total,        0 used,        0 free.  1004672 cached Mem
          PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
          32287 portage   20   0  224688 209604  12852 R 94.4 11.7   1:43.17 cc1plus
          32302 root      20   0    3136   2116   1740 R  2.2  0.1   0:00.66 top
          32288 portage   20   0   10276   7676   2816 S  1.6  0.4   0:00.31 as

    As we can see, `cc1plus` is occupying the CPU, which means that the build
    process is very likely to be up and running!

1. We're interested in what package is being built.
   Therefore we have two options.
       - Checking the ***emerge.log*** for output of the package managers main
          process. Use `tail` with you preferred arguments, this example just
          retrieves the 5 last lines in the file.

        ```
root@localhost ~ # tail -n5 /var/log/emerge.log 
        ```

            1425868251:  === (113 of 122) Post-Build Cleaning
            (app-editors/vim-7.4.273::/mnt/pkgdir/app-editors/vim-7.4.273.tbz2)
            1425868251:  ::: completed emerge (113 of 122) app-editors/vim-7.4.273 to /
            1425868252:  >>> emerge (114 of 122) net-wireless/gnuradio-3.7.6.1-r2 to /
            1425868252:  === (114 of 122) Cleaning
            (net-wireless/gnuradio-3.7.6.1-r2::/usr/portage/net-wireless/gnuradio/gnuradio-
            3.7.6.1-r2.ebuild)
            1425868259:  === (114 of 122) Compiling/Packaging
            (net-wireless/gnuradio-3.7.6.1-r2::/usr/portage/net-wireless/gnuradi
            o/gnuradio-3.7.6.1-r2.ebuild)

        The ***emerge.log*** shows that the package *net-wireless/gnuradio* is being
        emerged.

       - Using the `genlop` utility. This also showas the runtime of the current
         build.

        ```
root@localhost ~ # genlop -ct
        ```

             Currently merging 114 out of 122
             * net-wireless/gnuradio-3.7.6.1-r2 
                   current merge time: 8 hours, 31 minutes and 7 seconds.
                   ETA: unknown.
    

1. The next step shows how to monitor the output of the package build log. Those
   who are familiar with the [portage package manager](TODO) already know what
   to do. The examples follows the ***build.log*** and initially displays the
   currently last line in the file.

    ```
root@localhost ~ # tail -n1 -f
    ```

        /var/tmp/portage/net-wireless/gnuradio-3.7.6.1-r2/temp/build.log 
        cd
        /var/tmp/portage/net-wireless/gnuradio-3.7.6.1-r2/work/gnuradio-3.7.6.1_build/gr-blocks/lib
        ... LOTS OF STUFF HERE
        [ 42%] Building CXX object
        ... LOGS OF STUFF THERE

    The important information is not the output itself, but that the output is
    changing after the command has been started. If the build process hung,
    there would be no more output after the first line. This is not
    the case in the example since there's a second line of output after a
    couple of seconds, which showactivity of the ongoing build process. 

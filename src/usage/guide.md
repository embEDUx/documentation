You came here, because you probably just want to start to use the **embEDUx**
build system. Unfortunately the system is so complex, we cannot provide you with
a simple *quick start* guide.

The following tree will guide you through all necessary steps. Once you reach
the end of this page, you will have full customized linux distribution. That
means you built your own **U-Boot**, **Linux** kernel and RootFS.

Before you can actually start configuring and building, you need to setup the
**embEDUx** build system.

## Setup embEDUx
... setup blablabla
... user docu

Congratulations, you or your Administrator did successfully setup the
**embEDUx** build system.

## Build customized Linux distribution

### Requirements
* Installed **embEDUx** build system
    * Did your Administrator provide you with the User Documentation?
        * Do you know the URL of your repositories
        * Do you know the URL of the web interface for the **Buildserver**

* User Documentation includes your platform
    * Contact Administrator if not!

Great, you are ready to configure your customized **Linux** distribution. The
first step is to configure and build a bootloader. We recommend and will for now
officially only support **U-Boot**.

### Add U-Boot for platform
There are two situations, that can ran into.

1. You are the first one building version 'abc' of **U-Boot** with **embEDUx**

    GOTO Add upstream **U-Boot** version 'abc' 

1. Someone already built version 'abc' of **U-Boot** with **embEDUx**, but for a different
  platform.

    GOTO Add platform for **U-Boot** version 'abc'


### Add Linux kernel for platform
There are two situations, that can ran into.

1. You are the first one building version 'abc' of **Linux** kernel with **embEDUx**

    GOTO Add upstream **Linux** kernel version 'abc' 

1. Someone already built version 'abc' of **Linux** kernel with **embEDUx**, but for a different
  platform.

    GOTO Add platform for **Linux** kernel version 'abc'

### Add RootFS for platform
As the RootFS is not dependent on the platforms hardware, but on the platforms
architecture, adding a RootFS is quiet different, than adding **U-Boot** or
**Linux** kernel.








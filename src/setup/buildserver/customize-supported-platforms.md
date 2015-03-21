# Add New Platforms To The Buildserver
If you have a hardware platform that is not yet supported by **embEDUx**, you
have to adjust a couple of parameters in the build system.

## Setup parameters in ***group_vars/all***
It is assumed that you are the Adminsitrator who has installed the build system
or you are still in the middle of that. Please file ***group_vars/all***,
relative the to the buildserver setup routine directory contains the variables
for the buildmaster configuration. Please read the [buildmaster configuration
generation](../../background/implementation/buildserver.md#buildmaster-configuration-generation)
to understand what you are about to do.

## Adding Your Platform
You need to know the *architecture* of your platform, and chose a name for it.
The next step is to check if that architecture is already used by another
platform.

### Existing Architecture
In this case, it should be as easy as adding the according platform regular
expression to the *arch_branchregex*-dicitonary. Assuming, the chosen name for
your platform is **octaboard** and it is based on ARMv7a with HardFloat-support,
your change would look like this:

```yaml
...
arch_branchregex:
...
    armv7a_hardfp: 
        ...
        - ".*octaboard"
...
```

Afterwards you need to continue with or rerun the **buildmaster.yml** Playbook
in order to make apply your changes.


### New Architecture
This case is far more complex than the above one and is currently not covered by
the documentation.

### No underscores in the platform names!
If you add a new platform by modifying the dictionary, it is *important* that it
must not contain any underscores, use dashes instead!

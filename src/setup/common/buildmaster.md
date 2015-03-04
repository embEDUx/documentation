# Buildmaster Setup

## Configuation File - **master.cfg** 
TODO: where is the ***master.cfg***?


The following is directly taken from the ***HTWG buildmaster master.cfg***. 

## ARCH <\> Platform-Mapping
The algorithm for choosing the correct buildslave for the specific platforms
uses this dictionary as the information source.
```
arch_branch_res_map = {
  "amd64": [".*-ctng-.*", ".*qemu-virt-amd64.*"],
  "armv6j_hardfp": [".*raspberry-pi"],
  "armv7a_hardfp": [".*beaglebone-black", ".*banana-pi", ".*irisboard", ".*utilite-pro", ".*qemu-virt-arm.*"]
}
```

### Adding a new platform to the HTWG configuration
If you add a new platform by modifying the dictionary, it is *important* that it
must not contain any underscores, use dashes instead!

## Scheduler
TODO

## Buildjobs
TODO

## Webinterface
TODO

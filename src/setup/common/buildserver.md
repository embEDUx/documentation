# Buildserver Setup

## Buildmaster
### Configuration file

#### ARCH <\> Platform-Mapping
The following is directly taken from the ***buildmaster master.cfg***. 
The algorithm for choosing the correct buildslave for the specific platforms
uses this dictionary as the information source.
```
arch_branch_res_map = {
  "amd64": [".*-ctng-.*", ".*qemu-virt-amd64.*"],
  "armv6j_hardfp": [".*raspberry-pi"],
  "armv7a_hardfp": [".*beaglebone-black", ".*banana-pi", ".*irisboard", ".*utilite-pro", ".*qemu-virt-arm.*"]
}
```

### Scheduler
TODO

### Buildjobs
TODO

### Webinterface
TODO

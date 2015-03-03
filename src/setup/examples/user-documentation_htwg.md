## Platform Strings

The following is directly taken from the *buildmaster*'s ***master.cfg***. It
shows the responsible settings for the ARCH <-> Platform mapping.
```
arch_branch_res_map = {
  "amd64": [".*-ctng-.*", ".*qemu-virt-amd64.*"],
  "armv6j_hardfp": [".*raspberry-pi"],
  "armv7a_hardfp": [".*beaglebone-black", ".*banana-pi", ".*irisboard", ".*utilite-pro", ".*qemu-virt-arm.*"]
}
```

Platform | Platform-String | RootFS-String | Toolchain-Strings (target\_arch)
--- | --- | ---
Raspberry Pi | raspberry-pi | armv6j\_hardfp | armv6j
Banana Pi | banana-pi | armv7a\_hardfp | armv7a
Utilite Pro | utilite-pro | armv7a\_hardfp | armv7a
Qemu ARM | qemu-virt-arm | armv7a\_hardfp | armv7a
Beaglebone Black | beaglebone-black | armv7a\_hardfp | armv7a



## Repositories

Component | Repository URL
--- | ---
U-Boot | https://apu.in.htwg-konstanz.de/labworks-embEDUx/uboot.git
Linux | https://apu.in.htwg-konstanz.de/labworks-embEDUx/linux.git
RootFS | https://apu.in.htwg-konstanz.de/labworks-embEDUx/rootfs.git
Miscellaneous files | https://apu.in.htwg-konstanz.de/labworks-embEDUx/misc.git

## Buildbot

### Buildmaster Webinterfaces
Servername | URL
--- | ---
moe | http://moe.in.htwg-konstanz.de:8010

# RootFS Build Routine
**(work in progress)**


### Occurred Problems

#### proot upgrade causes unexpected behavior with nested SSHd
The following structure gives an outline of the scenario and the direct result of
the mentioned bug after upgrading *sys-apps/proot* to version 5.0.0 inside the
container *buildslavei\_rootfs\_amd64*.

```
- Hardware Host @ OpenVZ Kernel 2.6.32.something
  - QEMU/KVM VM @ Gentoo Kernel 3.19
    - Docker container that contains another chroot_rootfs
      - running as user $ sudo proot chroot_inside_container sshd -p 2222
        - running as user $ ssh root@localhost -p 2222
          - running as chroot root # su some_user -s /bin/true 
            --> FAILS WITH 'Permission Denied'
```

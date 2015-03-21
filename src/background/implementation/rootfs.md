# RootFS Build Implementation
**(work in progress)**
The RootFS build process is triggered for every change in the RootFS product
specifications repository. Please have a look at the following picture,
especially how the build delegation to the RootFS containers is visualized. 

[![](background/img/post-eval_result_design_rootfs.png)](background/img/post-eval_result_design_rootfs.png)

According to the design and evaluation results, the RootFS build routine can
either be run in a RootFS container for the native or cross architecture. Both
scenarios must be handled by the build routine differently, since they requires a different setup
of preparing the target RootFS.

The build process involves setting up the build environment depending on whether
it is a cross container or not.



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

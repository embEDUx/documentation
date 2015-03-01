Once a RootFS has successfully been built and uploaded to the *buildmaster*, it
can be imported into and run by various container management systems. As there are many of
them and the number is growing, the examples cover the currently
most and least popular ones: *Docker* and *systemd*.

This page will include fully working examples, with the assumption that the
container management systems are installed and ready for usage.

The examples will use a RootFS called *amd64_factory_systemd*.

## Docker
TODO

## systemd
Starting with version 219 of *systemd*, the utility `machinectl` provides the
functionality of downloading and importing a RootFS to the local machine.

### Download/Import
This step is very easy, since `machinectl pull-tar` takes the URL as direct argument. For more information consult `man machinectl`.

```
# machinectl pull-tar http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150 228172018_faa83f5_rootfs.tbz2 --verify=no
Enqueued transfer job 2. Press C-c to continue download in background.
Pulling 'http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2', saving as 'amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2'.
Downloading 300.9M for http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2.
Got 1% of http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2.
 2min 18s left at 2.1M/s.
...
...
...
Got 99% of http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2. 680ms left at 2.9M/s.
Download of http://moe.in.htwg-konstanz.de:8010/rootfs/systemd/amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2 complete.
Created new local image 'amd64_factory_systemd_20150228172018_faa83f5_rootfs.tbz2'.
Operation completed successfully.
Exiting.
```
The RootFS is imported as a container image to the local system and can be listed with
`machinectl list-images`.


### Set a root password
By default the build system does not set a passwort for *root*, therefore it
needs to be set manually. It's possible to run the container's `passwd` command,
as on a normal Linux system.

```
# systemd-nspawn -M amd64_factory_systemd_20150228172018_faa83f5 passwd
Spawning container amd64_factory_systemd_20150228172018_faa83f5 on /var/lib/machines/amd64_factory_systemd_20150228172018_faa83f5.
Press ^] three times within 1s to kill container.
/etc/localtime is not a symlink, not updating container timezone.
New password: 
Retype new password: 
passwd: password updated successfully
Container amd64_factory_systemd_20150228172018_faa83f5 exited successfully.

```

### Allow login via machinectl
```
echo "pts/0" >> /var/lib/machines/amd64_factory_systemd_20150228172018_faa83f5/etc/securetty
```

### Start in background

Starting the container happens with the `macinectl start` command. It should not
take any longer than a couple of seconds.
```
# machinectl start amd64_factory_systemd_20150228172018_faa83f5
#
```

### Login
`machinectl login` will provide access to a running container.

```

This is amd64_factory_systemd_20150228172018_faa83f5.unknown_domain (Linux x86_64 4.0.0-rc1) 15:50:56

amd64_factory_systemd_20150228172018_faa83f5 login: root
Password:
Last login: Sun Mar  1 15:49:43  2015 on pts/0
root@amd64_factory_systemd_20150228172018_faa83f5 ~ # 
```

That's it! The default setup of a container is heavily based on the 
***[systemd-nspawn@.service.in](https://github.com/systemd/systemd/blob/master/units/systemd-nspawn@.service)***-Template installed in the system, which may
differ between Linux distributions.

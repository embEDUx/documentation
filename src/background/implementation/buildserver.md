**embEDUx** buildserver is a compound of several components. Together, these
components form a unit that is designed to build different products
automatically as soon as the user provides new build specifications via the
product repositories. All the components that run on the buildserver will be
contained by **Docker** containers.

# Setup routine With Ansible
The [evaluation chose Ansible](../evaluation/buildserver-setuproutine.md) for
the implementation of the setup routine. The tasks are be grouped into roles and
plays, with the target architectures being variable. This allows to reuse
tasks and roles for the different target architectures, but requires a high
flexibility in the tasks.

## Playbooks
The implementation includes one Playbook for every major setup task, and another
one that includes all of them.

### [buildserver.yml](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/buildserver.yml)

This playbook is the one that contains all major setup tasks. The Plays that are
executed in the default configuration are listed in the following table.

Play | Hosts | Actions
--- | --- | ---
#1 | all | Dependency Installation
#2 | buildmaster | Buildmaster Container Setup
#3 | all | Define groups for target architectures
#4 | buildslaves-amd64 | Setup and run amd64 buildslaves
#5 | buildslaves-armv6j_hardfp | Setup and run arm6j_hardfp buildslave containers
#6 | buildslaves-armv7a_hardfp | Setup armv7a_hardfp buildslave containers

    
### [dependencies.yml](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/dependencies.yml)
The dependencies Playbook takes care of installing and starting **Docker** on the target
machine. As required by design and evaluation, it can do this on **Ubuntu** and
**Gentoo** machines. It has been tested on Virtual Machines that were installed
with the mentioned Linux derivatives.

### [buildmaster.yml](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/buildmaster.yml)
The buildmaster Playbook builds and runs the buildmaster container on the target
machine. The architecture will be chosen according to the target machine
architecture. In theory, this should work on any target architecture that is
available as **Gentoo** stage3, but it has only been tested on x86\_64 target
machines so far.

### [buildslaves.yml](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/buildslaves.yml)
The buildslaves Playbook builds and runs the buildslaves containers on the
target machine. By default, the target machine is the buildmaster itself, thus
the buildslaves for all targets architectures will run on the buildmaster.  It
should be possible to distribute the buildslaves to several machines, including
foreign architectures, but that scenario has not been tested yet.


## Buildmaster Configuration Generation 
The buildmaster configuration is highly dependent on the configuration that is
provided by the setup variables. As designed and evaluated, a template engine is
used to generate the ***master.cfg*** during the setup procedure. A detailed
explanation of how the variables and template are connected will be given in
this chapter.

### Provided Information - [***group_vars/all***](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/group_vars/all)

The following file is the default configuration file for the setup routine. It
contains the setup that has been running at the HTWG, and it includes the
supported platforms used at the HTWG.

```yaml
---
# Variables listed here are applicable to all host groups
base_dir: /var/tmp/embedux
config_dir: "{{ base_dir }}/config"
embedux_tmp: /var/tmp/embedux
repos_url_base: "https://github.com/embEDUx"

arch_branchregex:
    amd64:
        - ".*-ctng-.*"
        - ".*qemu-virt-amd64.*"

    armv6j_hardfp: 
        - ".*raspberry-pi"

    armv7a_hardfp: 
        - ".*beaglebone-black"
        - ".*banana-pi"
        - ".*irisboard"
        - ".*utilite-pro"
        - ".*qemu-virt-arm.*"

arch_map:
    x86_64: amd64
    armv6l: armv6j_hardfp
    armv7l: armv7a_hardfp
arch_short_map:
    amd64: amd64
    armv6j_hardfp: arm
    armv7a_hardfp: arm

native_arch: "{{ arch_map[ansible_architecture] }}"
native_arch_short: "{{ arch_short_map[native_arch] }}"

docker_image_prefix: "embedux"
```

### Configuration Template - [***master.cfg.j2***](https://github.com/embEDUx/buildserver-setuproutine/blob/ansible/roles/docker_buildmaster/templates/master.cfg.j2)
This file will be rendered according to the information from the
*group_vars/all* file which contains the default configuration and can be edited
by the Administrator. Additionally, secrets that have been defined in the vault
are assigned to variables that are available in the buildmaster configuration.
If interested, the instructions how to create the vault file are demonstrated
within the [setup
documentation](../../setup/buildserver.md#creating-the-password-vault)


#### PSK (Pre-Shared-Key)
This variable is filled in by the buildsetup template renderer. 
```
psk = "{{ buildbot_psk }}"
```
The *buildbot_psk*-variable is special to the buildserver setup routine, because
it is stored in the password protected vault file.
#### Usernames and Passwords For Web-Interface
User permissions for the web-interface are also defined in the previously
mentioned *vault*-file.

```
users = [
    {% for user,pw in users.items() %}
    ("{{ user}}", "{{ pw }}"),
    {% endfor %}
]
```

#### Branch <-> Platform <-> Architecture Mapping / Repository URLs
The buildmaster configuration template implements the mapping between
repository branches and the corresponding platform or architecture. 

These data structures are filled in by the buildsetup template renderer.

```
arch_branch_res_map = {
    {% for arch, regex_list in arch_branchregex.items() %}
    "{{ arch }}": {{ regex_list }},
    {% endfor %}
}
git_repo_uris = {
    "default": ["{{ repos_url_base }}/linux-specs.git",
        "{{ repos_url_base }}/uboot-specs.git",
        "{{ repos_url_base }}/toolchain-specs.git",
        "{{ repos_url_base }}/misc-specs.git"],
    "rootfs": ["{{ repos_url_base }}/rootfs-specs.git"],
    "rootfs_buildroutine": "{{ repos_url_base }}/rootfs-buildroutine.git",
}
```

As seen, the *repo_url_base* variable that is provided by the setup routine
defines the URLs that are later being configured for change detection.

## Continuous Integration
While the above chapter gives an introduction of how the setup incorporates the
variables into the buildmaster configuration, this part will demonstrate how the
Continuous Integration-aspects have been implemented with **Buildbot**.

### Buildslaves
Every buildslave container needs an equivalent buildslave configuration. Each
architecture is configured with two buildslaves, one for default builds and one
for rootfs builds. All buildslaves use the previously explained PSK as a
password.

```
c["slaves"] = [BuildSlave(arch, psk) for arch in arch_branch_res_map.keys()]
c["slaves"].extend([BuildSlave("rootfs_"+arch, psk) for arch in
arch_branch_res_map.keys()])

from buildbot.changes.gitpoller import GitPoller
c['change_source'] = []
for git_repo_uri in git_repo_uris["default"]+git_repo_uris["rootfs"]:
    c['change_source'].append(GitPoller(
        repourl=git_repo_uri,
        branches=True,
        pollinterval=30))

```


### Repository Poller
Buildbot offers a poller for most repository formats. The
[GitPoller](http://docs.buildbot.net/current/manual/cfg-changesources.html?highlight=gitpoller#gitpoller)
allows polling the above repositories for changes.

```
from buildbot.changes.gitpoller import GitPoller
c['change_source'] = []
for git_repo_uri in git_repo_uris["default"]+git_repo_uris["rootfs"]:
  c['change_source'].append(GitPoller(
          repourl=git_repo_uri,
          branches=True,
          pollinterval=30))
```
The repositories are polled for changes every 30 seconds.

### Schedule Builds on Repository Changes
Schedulers are notified by the Repository Pollers on any change. The scheduler
can then decide if a build should be scheduled or not.  Buildbot offers several
schedulers. A suitable scheduler for our purpose is the
[AnyBranchScheduler](http://docs.buildbot.net/current/manual/cfg-schedulers.html#anybranchscheduler).
In the following snippet, they are used together with regex expressions to
accomplish the mapping shown in the previous code.

```
def default_repos(repository):
  return repository in git_repo_uris["default"]

def rootfs_repos(repository):
  return repository in git_repo_uris["rootfs"]

c['schedulers'] = []
for arch,branch_res in arch_branch_res_map.items():
  for branch_re in branch_res:
    c['schedulers'].append(AnyBranchScheduler(
      name="default / arch: %s / branch-filter: '%s'" % (arch, branch_re),
      change_filter=filter.ChangeFilter(branch_re=branch_re,
                                        repository_fn=default_repos),
      treeStableTimer=10,
      builderNames=[arch]))

for arch in arch_branch_res_map.keys():
  branch_re="%s.*" % arch
  c['schedulers'].append(AnyBranchScheduler(
    name="rootfs / arch: %s / branch-filter: '%s'" % (arch, branch_re),
    change_filter=filter.ChangeFilter(branch_re=branch_re,
                                      repository_fn=rootfs_repos),
    treeStableTimer=10,
    builderNames=["rootfs_"+arch]))
```

### Build Factories and Builders
The actual build jobs are defined as
[BuildFactories](http://docs.buildbot.net/current/developer/cls-buildfactory.html?highlight=buildfactory),
and are then assigned to the respective
[Builders](http://docs.buildbot.net/current/manual/cfg-builders.html?highlight=builder#builder-configuration)
These builders will receive build jobs by the scheduler accordingly.

#### Build Factories
The build factories for default and rootfs builds implement the buildjobs.
After checking out the changed repository branches

##### Default factory - runs the *./build* executable
The default factory expects the repository to have an executable named
**build**. It will be executed after the changed repository branch has been
checked out to the filesystem.

```
# default factory
factory_default = BuildFactory()
...
factory_default.addStep(ShellCommand(command=["./build"], haltOnFailure=True, usePTY=True))
...
```

##### RootFS factory - runs the [ansible-playbook from the RootFS-Buildroutine](rootfs.md)
The RootFS factory works completely different compared to the default factory.
It retrieves the [RootFS build routine](rootfs.md) from the previously defined
repository URL. Afterwards it runs the Playbook named **site.yml** which
processes the RootFS specifications from the changed RootFS repository branch.

```
# rootfs factory
factory_rootfs = BuildFactory()
...
factory_rootfs.addStep(ShellCommand(command="/usr/bin/git clone --single-branch --depth 1 %s .ansible" % git_repo_uris['rootfs_buildroutine']))
factory_rootfs.addStep(ShellCommand(command="ansible-playbook -i .ansible/hosts .ansible/site.yml -vvvvv",
                                    timeout=None, usePTY=True, haltOnFailure=True, 
                                    env={ "TERM": "vt100",
                                          "ANSIBLE_CONFIG": ".ansible/ansible.cfg",
                                          "ANSIBLE_FORCE_COLOR": "1",
                                          "BUILDMASTER_URL": buildaster_url,
                                    }))
```
##### Upload The Output 
Afterwards the factories successfully complete their build processes, the
content of directory called ***output*** is uploaded to the buildmaster webserver.

```
factory_rootfs.addStep(
  DirectoryUpload(
    slavesrc="output",
    masterdest=Interpolate("/var/lib/buildmaster/public_html/%(prop:product)s/%(prop:platform)s"),
    url=Interpolate("/%(prop:product)s/%(prop:platform)s")
  )
)
```

Many build steps have been skipped for this overview, please consult the
***master.cfg.j2*** file directly for more details.

#### Builders
The builder assignment implements the arch <-> branch <-> platform mapping.
Effectively, the builders are assigned per architecture, since the platform
mappings are already mapped to their according architecture.


```
c['builders'] = []

for arch in arch_branch_res_map.iterkeys():
  c['builders'].append(
      BuilderConfig(
        name=arch,
        slavenames=arch,
        factory=factory_default,
        ))
for arch in arch_branch_res_map.iterkeys():
  c['builders'].append(
      BuilderConfig(
        name="rootfs_"+arch,
        slavenames="rootfs_"+arch,
        factory=factory_rootfs,
        ))
```

### Authentication and Permissions
Last but not least, the permissions for the previously rendered userlist are
configured. This configuration only authenticated users to scheduler and abort
any builds manually. 

```
authz_cfg=authz.Authz(
    # change any of these to True to enable; see the manual for more
    # options
    auth=auth.BasicAuth(users),
    gracefulShutdown = 'auth',
    forceBuild = 'auth', # use this to test your slave once it is set up
    stopBuild = 'auth',
    stopAllBuilds = 'auth',
    cancelPendingBuild = 'auth',
    pingBuilder = True,
)
```
Please consult the official docs at
[Webstatus](http://docs.buildbot.net/current/developer/webstatus.html?highlight=authz#web-authorization-framework)
for more details on these options.

# Adding packages to buildslaves

## Prerequisites

### Requirements
* Ansible
* buildserver_setup repository
* SSH root-access to the docker host running the buildslave(s) in question

### Suggestions,
* SSH root-access via key authentication

## Example - Adding 'sys-apps/dtc'
1.  Gain access to the buildserver_setup repository
1.  Edit ***roles/docker_buildslave/templates/Dockerfile.j2***
1.  Add a RUN instruction per package that should be added
    ```
29 RUN \
30   {% set package="sys-apps/dtc" %}
31   emerge --autounmask-write=y {{ package }}; \
32   etc-update --automode -5 && \
33   emerge -u {{ package }} && \
34   rm -Rf /usr/portage/distfiles/*
    ```
1. Connect to the docker host running the buildslave
1. Identify and verify the buildslave containers that have to be rebuilt
    ```
$ docker ps -f name=".*buildslave_[^_]*\..*" -f status=running
    ```
1.  Stop the buildslave containers
    ```
$ docker ps -f name=".*buildslave_[^_]*\..*" -f status=running -q | xargs docker stop | xargs docker rm
    ```
1.  Delete the buildslaves images, without their history
    ```
$ docker images | grep -e ".*buildslave-[^-]*\..*" | grep -oE "[[:alnum:]]{12}" | xargs docker rmi --no-prune
    ```
1. Comment the rootfs roles in the *buildslaves.yml* playbook for every architecture
    ```
23   - role: docker_buildslave
24 #  - role: docker_buildslave_rootfs
    ```
1.  Run ansible-playbook
    ```
$ ansible-playbook -i hosts buildslaves.yml --tags all
    ```
1.  Uncomment the rootfs roles in the *buildslaves.yml* playbook for every architecture
    ```
23   - role: docker_buildslave
24   - role: docker_buildslave_rootfs
    ```

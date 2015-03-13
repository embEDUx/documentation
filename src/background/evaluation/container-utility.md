# Cointainer Utility Evaluation

## OpenVZ

* Seperate Fork of the Linux-Kernel
* Backport of critical bugfixes and important features, otherwise still on Linux
  version 2.6.*xx*
* Installation of custom kernel is not straight forward on recent Linux
  Distributions
* Emphasizes on security and encapsulation of the guest container

## LXC
Stable project that has recently hit version 1.0, which brought the feature of 

* Linux Mainline-Kernel support
    * Utilizes the Linux-Kernel Container capabilities
    * Supported by all current Linux distributions
* non-privileged containers configurable
* complex configuration possibilities

## Docker
* Initially shipped with LXC as backend engine
* Meanwhile shipped with an self-developed
* Docker Inc. offers an official registry with many ready-to-pull-and-deploy container images
* Emphasizes simplicity and encapsulation of the guest container

## Result Container Utility Evaluation
* Compatibility,
* simplicity and therefore
* publicity 
are all in favor of **Docker**. 
This has also been confirmed in a meeting with the leading Professor.

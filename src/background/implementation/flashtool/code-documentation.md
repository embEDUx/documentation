# Code Documentation

This page will explain the modules of the **Flashtool** which are important for
the developer.

# Utility

    flashtool
    ├── Utility
    │   ├── __init__.py 
    ...

The utility provides helper functions which used in the whole **Flashtool** code 
and which are not referable to other modules.

## check_permissions

***check_permissions(file)***

Function which checks if access permission are provided for the user.
If not the user will be informed which Groups have access writes to the file
and quits the program.

* :param file: file to check
* :return: None

## create_regex_allowed

***create_regex_allowed(chk)***

Creates a regex to check an input matching several keywords.

* :param chk: List with keywords which are allowed
* :return: string in regex notation

## get_size_block_dev

***get_size_block_dev(dev_name, partition=None)***

Function to determine the size of a partition or a whole block device.

* :param dev_name: Disk name of block setup
* :param partition:  Partition of disk
* :return: Size of disk/partition

## get_terminal_size

***get_terminal_size()***

Helper to get the current size of the terminal the Flashtool was
called.

* :return: list with width and height

## os_call

***os_call(command, timeout=None, allow_user_interrupt=True)***

Call shell-command with timeout. Can also block user interrupts
if wanted

* :param command: Command as list, suitable for the subprocess Popen call
* :param timeout: time in seconds
* :param allow_user_interrupt: flag if user interrupt is allowed
* :return: None

## untar

***untar(tar, target)***

Unpack a tarball to a target location using tarfile. The
progress of the unpack procedure will be shown.

* :param tar: tarball file
* :param target: target location
* :return: None

## user_prompt

***user_prompt(question, info, check=None)***

Function to handle user input with limited input possibilities.

* :param question: Output for user prompt
* :param info: short info for user
* :param check: List with valid user input
* :return: user input string

## user_select

***user_select(question, lower, upper)***

Helper function to ask the user for a selection in a numeric range.

* :param question: Output for user prompt
* :param info: short info for user
* :param check: List with valid user input
* :return: user input string



# udev/mmc.py

    flashtool
    ├── setup
    │   ├── udev
    │       └── mmc.py
    ...


This module recognizes mmc devices with the help of the pyudev module.


## get_active_mmc_info

***get_active_mmc_info()***

Tries to get information about a plugged in mmc device. The user
receives instructions to plug in the mmc device when the tool is ready
for recognition.

* :return: Information for Block devices

## get_mmc_device

***get_mmc_device(auto=False)***

Function which tries to get the device information of a mmc device.
If the system recognize multiple mmc devices the user is prompted to chose
a device.

* :param auto: decide if user should be asked for continuing the setup process
* :return: Returns a triple with device dev-paths, size of device and list with
         all dev-path of the partitions

## _get_real_block_devices

***_get_real_block_devices()***

Filters entries in the list with possible block devices
when they are not a block device.

* :param guessed_devices: list of possible block devices
* :return: list with valid block devices

## get_partition_information

***get_partition_information(devices)***

Retrieves important information about the partitions of
a block device.

Information:

    path: path to /dev device of the partition
    size: size of the partition
    fs_type: filesystem type of a partition
    fs_version: filesystem version
    name: partition label
    uuid: uuid of the partition

* param devices: list of block devices
* :return: List with information for a device

## ensure_unmounted

***ensure_unmounted(devs)***

Unmount the partitions which are given by in parameter devs.
The function will call the *umount* command as often as the device 
is listed in /proc/mounts.

* :param devs: list with /dev paths of partitions
* :return: None


## MMCProfiler

Class which is able to guess the right *mmc* device when plugged in.

### guess

***guess()***

Method which guesses the *mmc* device due to the recorded udev events.

* :return: a list with all possible *mmc* devices

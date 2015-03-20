# Setup of the Flashtool

## Requirements

__System:__

- python3
- python3-dev
- virtualenv
- libudev >= 151
- libparted
- gcc
- sed
- git

__Python packages:__

These package will be automatically installed when the [installation
instruction](#installation-python)
below is followed.

- setuptools
- colorama
- pyudev
- argcomplete
- PyYAML
- requests
- jinja2
- pyparted
- pycrypto


## Installation

### Required Packages

#### Installation Ubuntu/Debian:

```sh
$ apt-get install gcc python3 python3-dev python-virtualenvironment libudev-dev libparted sed git
```

#### Installation Arch Linux:

```sh
$ pacman -S gcc python3 python-virtualenv libsystemd parted sed git
```

#### Installation Fedora Linux:

```sh
$ yum install gcc python3 python3-devel python-virtualenv udev parted sed git
```

#### Installation Python:


**Virtualenv:**

Creating an virtual environment for python (python version must be >=3)

```sh
$ virtualenv -p python3  {path/for/virtualenv}  # python3 can also be python3.x
```

Go into the virtual environment. All packages installed via pip will only be
installed at the location of the virtual environment ({path/for/virtual-env})

```sh
$ source {path/for/virtualenv}/bin/activate
```

All python related packages will now be executed from virtual environment path 
The python installation of the system will be untouched.

After working with the virtual environment you can leave the virtual 
environment with the following command.

```sh
$ deactivate
```


**Installation of python packages via pip:**

```sh
$ source {path/to/virtualenv}/bin/activate  # go into virtualenv
```

Before you can install the package via *pip* you must ensure that the
*setuptools* package is installed.

```sh
$ pip install setuptools
```

Now you can install the required python packages and the **Flashtool** 
with the following command:

```sh
$ pip install -r https://raw.githubusercontent.com/embEDUx/flashtool/master/requirements.txt 
```

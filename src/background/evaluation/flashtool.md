# Evaluation of software components for the **Flashtool**

For several tasks of the **Flashtool** there are multiple python packages to do
the job.

## User interface

The **Flashtool** should be used in a command line interface and therefore it
has to provide several program parameter to trigger the different tasks. 

To implement command line options we considered using *getopt* or *argparse*.
The package [getopt](https://docs.python.org/3.3/library/getopt.html) is a 
C-style parser and is recommend for users of the C *getopt()* function. The
documentation for the *getopt* package recommend the package [argparse](https://docs.python.org/dev/library/argparse.html) 
for users who want to write less code (who doesn't?) and get better help and 
error messages. 

The decision to take the *argparse* package was easy, because a implementation
of the various command line parameter, which each of them will have own options,
will lead to a vast number of code with the *getopt* package. The *argparse*
package is easy to use and leads to clean code. Extending the parser with new
arguments is really easy.


## Partition a block device

For this purpose we had to choose between [blivet](https://github.com/rhinstaller/blivet) and [pyparted](https://github.com/rhinstaller/pyparted).
The *blivet* package is used by the fedora project and according to the
[documentation](http://blivet.readthedocs.org/en/latest/) it is easy to create
partitions. A big disadvantage of the *blivet* package is, that it has many
dependencies to other package, which must be installed by hand and are not
automatically installed by the *setup.py* script of the package. There were also
some difficulties to install some of the dependencies, because they only work
with python 2.7 and not python 3 or above. 
After failing to use the *blivet* package we decided to use the *pyparted*
package. This package uses the *libparted* package. *libparted* is the library 
of the GNU parted project. The *pyparted* is a good solution for the
**Flashtool** to partition block devices. It supports all features which are
given by the C library *libparted*. It took about 80 lines of code to implement
the functionality for the **Flashtool**.

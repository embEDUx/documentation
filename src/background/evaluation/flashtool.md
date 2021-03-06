# Evaluation of software components for the **Flashtool**

The **Flashtool** design describes the [automation of the deployment process]
(../design/flashtool.md). To implement the described design decisions there must
be evaluate several steps.

## Programming language

The decision for a programming language is very important step due to the
development procedure of a software. The **Flashtool** needs a programming 
language which is supported on a **Linux** distribution and runs on different
architectures. The script languages **Bash** and **Python** was considered to be
used as programming language. 

[Python](https://www.python.org/doc/) is a script language which is easy to 
learn, supports interfaces to other languages (like C), has a nice syntax and provides 
thousands of third-party modules. 

[Bash](https://www.gnu.org/software/bash/manual/bashref.html) is a command
language interpreter and provides an own script language. It is also the
GNU/Linux standard shell.


### Python vs Bash

Python and Bash are both script languages which run on likely every UNIX system.
Both languages must be compared on different disciplines, to decide which
language fits best for the **Flashtool**.

#### Development

**Python** is more productive than **Bash** for the development processes,
because it supports common programming paradigms like object-oriented
programming and functional programming. 

According to the design of the **Flashtool** the implementation will require a
lot of code. To accomplish the development of the **Flashtool**  with **Bash** 
would result in an confusing mass of **Bash**-scripts and would be hard to
maintain.


#### Community

**Bash** and **Python** is often used on **Linux** systems and supports both a
huge community and documentation. **Python** provides more third-party modules
for several task than **Bash** and is a good candidate for writing lesser code
to do the job. 


#### Calling other executables

Both languages provide a mechanism to call other executables easy.


#### Performance

**Python** is really fast in handling data structures (sorting, access) and
doing calculations [compared to Bash](http://opennomad.com/content/performance-different-scripting-languages-shell-v-perl-v-python-v-ruby).


#### Interfaces to other programming languages

**Python** provides a library which provides C compatible data types, and allows
calling functions in shared libraries. This makes it possible to wrap C
libraries in pure python. ((ctypes)[https://docs.python.org/2/library/ctypes.html?highlight=ctypes#module-ctypes])
There are other libraries like [swig](http://swig.org/Doc1.3/Python.html) and 
[cython](http://cython.org/) to connect C and C++ with Python.

Such mechanism are not known for **Bash**.

#### Summary

**Python** is more suitable as programming language for the **Flashtool** than
**Bash** because:

* Python is faster (organizing data structures, *http* requests, etc.)
* Large Python project are easier to maintain than with **Bash**
* Python provides a wide variety of standard and additional modules
* and can interact with C/C++ libraries.

## Python Version

After deciding to use python it is important to have in mind that there are
two python versions which have many differences in their API. At the beginning
of the development process, the goal was to implement the **Flashtool** 
compatible to python 2.x and python 3.x. This goal was not able to be achieved
for the following reasons:

* The module *tarfile* has issues with ***unicode*** file names when used with
    python 2.x. This issues did not appear in python 3.x.

* Providing python code compatible for both versions is sometimes cumbersome and 
    extends the implementation time.

For these reasons the decision was made to use python 3.x for the **Flashtool**.


## User interface

The **Flashtool** is used in a command line interface and therefore it
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
package is easy to use and leads to clean code. Extending the *argparse* code
with new arguments is really easy too.


## Partition a block device

To partition block devices with python we considered to use
[blivet](https://github.com/rhinstaller/blivet) or 
[pyparted](https://github.com/rhinstaller/pyparted).

### blivet

The *blivet* package is used by the fedora project and according to the
[documentation](http://blivet.readthedocs.org/en/latest/) it is easy to create
partitions. 

A big disadvantage of the *blivet* package is, that it has many
dependencies to other package, which must be installed. During the evaluation
process it turned out that most of the dependencies were not installed
automatically with the pip installation routine. The single dependencies had to
be installed by hand. There were also some difficulties to install some of the
dependencies, because they only work with python 2.7 and not python 3 or above.

After failing to use the *blivet* package we decided to use the *pyparted*
package.

### pyparted

This package uses the *libparted* package. *libparted* is the library 
of the GNU parted project. The *pyparted* module is a good solution for the
**Flashtool** to partition block devices. It supports all features which are
given by the C library *libparted*. 

It took about 80 lines of code to implement the functionality for the **Flashtool**.

# Design of a deployment tool - **Flashtool**

Deploying systems built with the **embEDUx** system should be done really easy for
the user. Therefore a tool should be developed which automates the several steps
of the deployment procedure. It seemed obvious to call this tool "**Flashtool**"
due to the fact that most of the embedded devices uses flash memories to store
their operating system and files.

## Programming language

One of the first decisions which were made for the tool was to choose *python*
as programming language. Python is a script language which is easy to learn,
highly productive, has a nice syntax and provides plenty of packages and 
libraries. It is also an often used language and will run on every Linux system.


## Design decision 

There are basic tasks which must be fulfilled by the **Flashtool**:

First of all the **Flashtool** must be usable for different *embEDUx*
environments. Therefore URLs to the *buildserver* or to repositories should not
be hard coded. 

- User must be able to configure several settings for the **Flashtool**, these
    settings should be saved in a configuration file.

The **Flashtool** should be able to setup several platforms. For the platforms
this includes partition a MMC device and load the software components to the
partitions. It must be possible to configure this setup process for the needs of
the user. And this configuration should be reusable, to setup several platforms
with the same configuration.

- User can create different configuration files for a platform to configure the
    setup/deploy process. (recipes)
- The configuration language should be easy to use.

Each software components will have several versions. These versions are
available on the *buildserver*.

- User should be able to list all available software components versions for a
    platform. 
- User should be able to select a specific version for a setup procedure.
- **Flashtool** must be able to reach all built software components on the
    *buildserver*

To make the setup process as easy as possible for the user, the **Flashtool**
should be able to recognize plugged in MMC media. 

- Automatic recognition of plugged in MMC devices.

The **Flashtool** should be extensible for future features.

- adding new setup routines for new platforms if needed.
- adding new commands for the **Flashtool**. 



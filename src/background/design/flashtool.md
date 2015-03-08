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


## Requirements of the **Flashtool**

There are basic tasks which must be fulfilled by the **Flashtool**:

1. set and change url to *buildserver* web interface
2. easy configuration setup for the *Flashtool*
3. provide easy configuration of a platform deployment routine (recipes)
4. retrieve software components form the *buildserver*

    * list software components for a platform
    * filter or select specific software versions

5. extensibility of the *Flashtool*
    
    * adding deployment routines
    * adding new configuration options

6. recognition of plugged in hardware
7. easy to use


## Features 

The table below shows a quick overview of the features of the **Flashtool**.
A detailed description of the command can be found in the [usage
section](../../usage/flashtool.md) of the **Flashtool**


 command | description
 ------- | -----------
 init / config | Configure needed options for the **Flashtool**. Must be done as first step (init) and can be changed any time (config)
 platform\_recipes | Get or update platform recipes from git repository
 list\_platforms   | Shows which platforms have a recipe file and can be set up
 list\_builds  | List all versions of software components on the platform, grouped by platform and product type
 setup  | runs a deployment procedure for the specified platform
 check\_mmc | Does a filesystem check on every partition on a mmc media


 


# Specification for a deployment tool

This is the specification that has been worked out according to the [design of
the Flashtool](../design/flashtool.md). 


## Flashtool configuration file



## Configuration file for platforms


### Language


### Name Scheme


### Availability 


### User defined recipe files


## Connection to buildserver **buildbot**


### JSON api of **buildbot**


## Recognition of MMC device


## User interface


## List of features
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


 



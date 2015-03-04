## Requirements
* A graphical Web-Browser :-)
* Buildserver Web-Interface URL. Find this in **your** [User
  Documentation](../../setup/user-documentation.md)

## Buildbot buildmaster Webinterface
The *buildmaster* provides a webinterface that can be used to control and
monitor the buildmaster's behavior. The two most important views are the
waterfall view and the builders view.

### Waterfall View
The **buildbot** waterfall-view gives an overview over all running and recent
builds in one place. Colors indicate the state of the builds and links to
detailed logs or general build information are provided.


### Builders View

#### Builders Status
The builders view let's you quickly see the status of all buildslaves.
On the following pictures, all are idle and have successfully finished their
last builds.

![buildmaster at HTWG - Builders - all Idle](usage/common/img/buildmaster_builders_view.png)

#### Force builds
Depending on the [buildmaster's scheduler
configuration](../../setup/common/buildmaster.md#Scheduler), it is also possible
to schedule forced builds via the builders view.

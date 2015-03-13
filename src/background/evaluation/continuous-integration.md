# Continuous Integration Evaluation
**(work in progress)**

The continuous integration system is responsible for scheduling the builds
according the changes in the product repositories. It delegates scheduled builds
to builders that are prepared with build environments specific to their mapped
platform or the platform's architecture.

## Repository Dependencies
Gitlab at thE HTWG

### Gitlab-CI
Here go the pros and cons of the Gitlab-CI

### buildbot
Here go the pros and cons of the buildbot

### Scheduler configuratoin
A suitable scheduler for our purpose could be the
[anybranchscheduler](http://docs.buildbot.net/current/manual/cfg-schedulers.html#anybranchscheduler).

# Continuous Integration Design
The design decisions made in [Automated Build
Triggering](buildserver.md#automated-build-triggering) and [Abstraction Layer
For Automation](buildserver.md#abstraction-layer-for-automation) must now be
merged in order to create a complete design for the continuous integration
system.

## Design Decisions
* Observation of Git-Repositories
* Trigger specific builds on changes
* Distributed Architecture of Scheduler and Executors


## Candidates
The topic *continous integration* has received a proper amount of attention from
the open source community, and there are a couple of source projects available
that could possibly deliver the needed functionality. The following list of
continuous integration systems shall be evaluated in order to find the best
suiting system. All of the candidates are open source projects:

* Buildbot
* Gitlab-CI
* Jenkins

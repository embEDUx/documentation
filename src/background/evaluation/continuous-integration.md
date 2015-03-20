# Continuous Integration Evaluation
The continuous integration system is responsible for scheduling the builds
according the changes in the product repositories. It delegates scheduled builds
to builders that are prepared with build environments specific to their mapped
platform or the platform's architecture.

## Gitlab-CI
Gitlab-CI aims to integrate with the Gitlab Collaboration Server. At the time of
the project evaluation the project is hosted at a **Gitlab**-Server at the HTWG, but
it is planned to be published on **GitHub**. Therefore, Gitlab-CI is not an
option.

## Buildbot
Buildbot is based on Python, and is also completely configurable through the
Python language. This brings both, complexity and flexibility. Judging by the
list of features and examining the documentation, all of the above design
decisions are possible to implement using **Buildbot**.

## Jenkins
Java based continuous integration tool, which is the first and last criteria
to analyze.

## Result Continuous Integration Evaluation
**Buildbot** will be chosen as the CI-system used within the **embEDUX**
build system. It was chosen, because

* it fulfills all of the design decisions
* it is Python based, which is very flexible and all team members are
  already familiar with Python
* there is no serious competition

## Master and Slave Terminologies
**Buildbot** uses the terms **Buildmaster** and **Buildslaves** as a referral to
the active scheduling component and the passive executors.

# Design - Continuous Integration (CI)
The continuous integration system is responsible for scheduling the builds
according the changes in the product repositories. It delegates scheduled builds
to builders that are prepared with build environments specific to their mapped
platform or the platform's architecture.

# Tasks
1.  provide an overview of recent and running builds
1.  View Log-files or recent and running builds
1.  Allow to manually manage build jobs
    * (re-) Schedule builds
    * Cancel builds
1.  Flexible build job specifications, not limited to specific commands or
  structures

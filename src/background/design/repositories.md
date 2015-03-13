# Design Repositories - Product-Specification Storage Units
It must be possible to build the products independently from each other.
Therefore, each product specification should be managed in a separate storage
unit which will be referred as a *repository* from this point on. Additionally
each platform needs to have its own identifiable storage subunit within the
*respository*. The storage subunits will be referred as *branches* from this
point on.

## Repository Format
Configuration files and specification files are most certainly provided by the
user as text files. For this purpose, a version control system should be used in
order to have a history of build changes and allow easier handling of the
repositories.

## Product Requirement Analysis
The build process and the configuration options of each product must fulfill the
requirements of the corresponding product. The requirements chapter lists
different requirements for each product, which must therefore be analyzed
separately.

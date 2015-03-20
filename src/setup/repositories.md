# Repository Setup
The storage units for the product specifications done by the user is realized in
the form of git repositories. In order for the build system to work properly
these repositories need to be set up. For further information have a look at the
[background](../background/background.md).

## Product Repositories
Setup an empty repository for each of the products. They will be used by the
users to provide their product specifications to the buildserver.

Product | Repository
--- | ---
U-Boot | uboot-specs
Linux | linux-specs
RootFS | rootfs-specs
Miscellaneous files | misc-specs
Toolchain | toolchain-specs

If you don't know how to setup empty repositories, have a look at [github hello
world](https://guides.github.com/activities/hello-world/#repository). Please
document the repositories URLs in the [User
Documentation](post-install/user-documentation.md) that you have to provide to
your users after the successful setup of the **embEDUx** build system. For the
**embEDUx** build system you need the *https* version of the URL, which can be
obtained on the lower right side on the [Github](https://github.com) website of
the repository.

![Repository URL](setup/img/github_url.png)

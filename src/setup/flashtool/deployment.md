# Deployment With The **Flashtool**

This page gives a quick overview about the deployment procedure as an
introduction for the topics [Writing a new recipe file](deployment/add-recipe-file.md) 
and [Adding a new deployment procedure](deployment/add-new-deployment.md).

## Quick Overview 

The deployment of products includes several steps:

1. prepare the storage media (layout of the storage media - e.g. partitions,
    adress ranges)
2. download and unpack products to the workstation
3. copy products to the storage device

The first and the third step can differ between the platforms. The second step
is the same for every platform. 

The preparation of a storage media (step 1) can differ in two ways:

1. differences in the layout for the same storage media of a platform or
    different platforms

2. different layout procedure for different storage medias

and the third step can differ depending on the storage media layout and the
selected products which are needed for a platform.

The mechanisms to layout a specific storage media type are the same but the
configuration how to layout a storage media can be different. 

As a result the deployment configuration is divided by the type of the storage
media and therefore there exist a ***recipe skeleton*** for each storage type.
With this recipe skeleton the user can configure a recipe for the first and 
the third step of the deployment. The configuration files which include the
recipes for a platform are called ***recipe files***.

## Further Reading

If you want to know how to write a recipe file for a platform with the given
recipe skeletons pleas read the chapter [Writing a new recipe file](deployment/add-recipe-file.md) 

If you are configuring a new platform for your **embEDUx** environment and need
to implement new recipe skeleton for a not supported storage device, pleas read
the chapter [Adding a new deployment procedure](deployment/add-new-deployment.md) 
first.

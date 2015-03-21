# Add A New Deployment Procedure

**(work in progress)**

This chapter describes how to implement new recipe types for the deployment
procedure. If you are unsure about the concept of recipe files for the
**Flashtool** please read the chapter [Deployment with the Flashtool](../deployment.md)
and [Writing a new recipe file](add-recipe-file.md) first.


## Common Procedure For A Developer

The following steps should be done, if you want to add a new deployment
procedure to the **Flashtool**

* Read the chapters below to understand where and how to add a new deployment
    procedure.
* Fork the [Flashtool]() sources and start to implement the new feature
* Create tests for the new feature in the directory tests. The Flashtool uses
    the module [pytest](http://pytest.org/latest/) for unit testing.
* You can create a pull request for your feature to get it integrated in the
  main **Flashtool** sources.

## General structure of a recipe file

The recipe files for the **Flashtool** are written in 
[YAML-Syntax](http://yaml.org/). The next example shows the general structure
of a recipe file.

    ---
    type: # name of recipe type

    recipe: 
        # specific configurations of the recipe
        # ...

    ---
    type: # next recipe

    recipe:
        # ...

The `---` is necessary to indicate a *YAML-document*. The *YAML-document*
represents a recipe. The example shows that a recipe file can contain 
multiple recipes. There must be at least one of it in a recipe file. 
Every recipe skeleton must contain a *type* keyword and a *recipe* keyword. 
For the value of the *type* keyword a name of a implemented recipe skeleton is
expected. The content of the *recipe* section depends on the selected recipe 
and is defined in the python code of the **Flashtool**. The proceeding for
adding a new .


## Recipe Skeletons And Their Python Representation

The recipe files can be parsed easily by python. To avoid errors from the author
of the recipe file, the given key value pairs in the recipe files, are parsed
and checked by the **Flashtool**. The **Flashtool** provides an interface for
new recipe skeletons.


## Structure Of The Setup Module Of The Flashtool

A new recipe skeleton for a deployment must be defined and implemented in 
python. The next figure will show where the python representation for a new 
recipe skeleton must be implemented in the **Flashtool** code structure.

    flashtool
    ├── setup
    │   ├── __init__.py 
    │   ├── deploy              # deployment procedures for a storage device
    │   │   ├── __init__.py
    │   │   ├── ...
    │   │   └── mmc.py
    │   │ 
    │   ├── recipe              # recipe skeleton implementation
    │   │   ├── __init__.py
    │   │   ├── ...
    │   │   └── mmc.py
    │   │
    │   └── devlayout           # modules to layout storage devices
    │       ├── __init__.py
    │       └── blockdev.py
    ...

The **Flashtool** will read in the recipe file from top to bottom. The type of
the recipe skeleton is given by the key `type` in the *YAML-document*. The
corresponding python files for the recipe skeleton must be mapped as python
file in the deploy and recipe directory. The name of these files must be the
recipe skeleton type name with a *py* extension.

According to the directory structure above the user can only state the recipe 
skeleton for *MMC* devices (`type: mmc`).


### Python Representation Of A Recipe Skeleton

The next example will show you how to implement a python representation for a 
recipe skeleton. Let's create recipe skeleton for a *HDD* device. 

#### 1. Specify an example *YAML document* 

The example shows all keywords which the recipe skeleton for *hdd* devices should
provide. The keywords for the recipe must be stated in the `recipe:` section. 
If you do not know how the *YAML* syntax look like, please have a closer look
[here](http://www.yaml.org/spec/1.2/spec.html#id2759963).


    ---
    type: hdd
    
    recipe:
        partition_type:
        partition:
            - name: 
              fs_type:
              size:
              flags:

The python representation must check the *YAML document* for the keywords 
*partition_type*, *paritition* and for every partition the keywords 
*name*, *fs_type*, *size* and *flags*.

The recipe file will be parsed with the [PyYaml](http://pyyaml.org/) module.
The *YAML document* above will be represented in python as the following
structure.

    {
        'type' : 'HDD',
        'recipe' : {
            partition_type : None,
            partitions : [
                {
                    name : None
                    fs_type : None,
                    size : None,
                    flags : None,
                }
            ],
        },
    }

You can see that the indentation level of the keywords have an impact on the 
structure of the python dictionary. 

The setup routine will read the value of *type* and search for a python
representation in the recipe directory (In this case the file *flashtool
/setup/recipe/hdd.py*). When found, it will pass the values of *recipe* into
the constructor of the python class (In this case *HDD*).


#### 2. Implement the python representation for the recipe skeleton. 

The python representation of the recipe skeleton is a python class and should
have its name written in *CAPITAL* letters and must inherit from the class
*YAML*.

    from flashtool.setup.recipe import YAML
    
    class HDD(YAML):
        ...

The valid keywords for the recipe must be added in a class attribute named
*attr*. The *attr* variable is only for keywords in one indentation level.
In this case a second class must be created for the *partition* keyword to
manage the nested keywords of the *partition* Node.

The constructor of the recipe representation must also provide a parameter.

    ...
    class HDD(YAML):
        attr = ['partition_type', 'partitions']

        def __init__(self, attributes):
            self.check_attributes(attributes)
            ... # DO SOME VALUE CHECKS HERE
            parts = []
            for part_attr in attributes['partitions']:
                part = Partition(part_attr)
                parts.append(part)
            attributes['partitions'] = parts
            YAML.__init__(self, attributes)


    class Partition(YAML):
        attr = ['name', 'fs_type', 'size', 'flags']
        
        def __init__(self, attributes):
            self.check_attributes(attributes, False)
            ... # DO SOME VALUE CHECKS HERE
            YAML.__init__(self, attributes)

    __entry__ = HDD

The classes inherits the method `check_attributes(self, attributes, subset=True)` 
from the super class *YAML*. Depending on the parameter `subset` it will check the
given parameter attributes in two ways:
    
* *`subset=True`*

    The dictionary attributes is only allowed to contain the keys which
    are specified in the class member `attr`. It allows that a key can
    be missing in the dictionary.

* *`subset=False`*

    The dictionary must contain exactly the keys which are specified in 
    the class attribute `attr`.
    

This method should be used to check the keys of the parsed *YAML document*.

The last statement of the constructor is a call of the constructor of the
super class *YAML*. It will save the given dictionary of the constructor parameter
as attributes of the created object. It is now possible to access the key
value pairs of dictionary with the dot `.` operator.

    hdd_obj.partition_type  # get partition types
    hdd_obj.partitions      # get list of partitions

The module variable __entry__ must be set with the class name of the
implemented recipe class. With this value the **Flashtool** can create an
instance of the new recipe class. 


#### 3. The load attribute:

The load structure can be used to map the software components to the defined
partitions. To add this structure to your recipe type you have to do the
following steps:

1. Add the keyword *load* to the *attr* class member of your python class
    first (In this example HDD).

        attr = ['paritions', 'partition_table', 'load']

2. Pass the value of the attribute *load* to the constructor of the class
   *Load* and save the *Load* object as new value of the *load* attribute.

        from flashtool.setup.recipe import Load
        ...
            attributes['load'] = Load(attributes['load'])
            YAML.__init__(self, attributes)

Now the user can use the *load* structure in the *hdd* recipe 

    ---
    type: hdd
    
    recipe:
        partition_type:
        partition:
            - name: 
              fs_type:
              size:
              flags:

        load: 
            Uboot:
                device: 
            Linux_Boot:
                device: 
            Linux_Root:
                device: 
                ...


#### 4. Deployment class
Now we can add a deploy class for the *hdd* recipe type. This class must be
stated in the file *hdd.py* and inherit from the super class Deploy. The 
following constructor and methods must be implemented for this class.

    `def __init__(self, recipe, actions, builds, platform, auto)`
    `def prepare(self)`
    `def load(self)`

The setup routine will search for a python file with the name *hdd.py* in
the directory *deploy*. The module variable `__entry__` must be set with the 
class name of the implemented deploy class. Let's call this class
`HddDeploy`. The following example will show the structure of the python
file.

    from flashtool.setup.deploy import Deploy
    # other imports

    class HddDeploy(Deploy):

        def __init__(self, recipe, actions, builds, platform, auto):
            # do initialization steps for the class ...

        def prepare(self):
            # code for preparation steps of the hardware, like partition
            # the device

        def load(self):
            # loading products to the device.

    __entry__ = HddDeploy


It is important that the constructor signature `__init__` provides the parameter
`recipe, actions, builds, platforms, auto`:

    * `recipe`: stores the python representation object for the recipe.

    * `actions`: dictionary with the key value pairs (keys: 
        `linux, uboot, misc, rootfs`). The values represent the version the user
        selected at the call of the **Flashtool**.

    * `builds`: *build server* object for downloading the products from the web
        server.

    * `platform`: the name of the platform

    * `auto`: flag for if the user wants to run the deployment procedure in
        automatic mode.

The setup routine will call first the `prepare()` method of all deployment
classes according to the recipe file which are specified in the *YAML* file
and then the `load()` methods. The 


## Useful Modules For The Deployment Class

Besides the limitations stated in chapter above, you are free in your way of
implementation of the deployment class.

The following link provides information about modules in the **Flashtool** sources
which can help to speed up your development process.

* [Code Documentation](../../../background/implementation/flashtool/code-documentation.md)

     

## Information to write in this chapter

**Attention: the setup routine only allows to deploy products on platforms
which use a mmc device as storage media. Support for other storage media must be implemented.**

If you want to implement new features to the **Flashtool**, please consider
reading the development section for the **Flashtool**. The new functionality
must be triggered by a recipe file an must be explained in the [recipe
files](#recipe-files) chapter.

The setup procedure requires an existing [recipe](#How_to_write_a_recipe_file) 
file.

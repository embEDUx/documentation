## Adding new recipe types

A recipe file is written in *YAML-Syntax* an can easily read in by python. To
avoid errors from the author of the recipe file, the given key value pairs in
the recipe files, are parsed and checked by the **Flashtool**. The **Flashtool**
provides an interface for new recipe types.

A new recipe type for the setup procedure of the **Flashtool** must be defined
and implemented in python. The next figure will show the structure of the 
setup part of the **Flashtool**.

```
./setup
├── init.py 
├── deploy
│   ├── __init__.py
│   ├── ...
│   └── mmc.py
│ 
├── recipe
│   ├── __init__.py
│   ├── ...
│   └── mmc.py
...
```

The **Flashtool** will read in the recipe file from top to bottom. Each *YAML 
document* in the recipe file represents a recipe. The type of the recipe 
is given by the key `type`. Only values are allowed which are mapped as python 
file in the deploy and recipe section. In this example the user can only state 
the recipe type `type: mmc`.


### Python representation of a recipe type

The next example will show you how to implement a python representation for a 
recipe type. Let's call the new recipe type *hdd*. 

1. Specify a *YAML document* with all keywords which the recipe type *hdd* should
    have. The keywords for the recipe must be stated in the `recipe:` section. 
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

    The setup routine will read the value of *type* and search for a python
    representation in the recipe directory (In this case the file *flashtool
    /setup/recipe/hdd.py*). When found it will pass the values of *recipe* into
    the constructor of the python class (In this case *HDD*). Of course there is
    no class defined at *flashtool/setup/recipe/hdd.py*, this brings us to step
    2.

2. Implement python representation for the recipe. The python representation of 
    the recipe type is a python class and must have the same name written in 
    *CAPITAL* letters and inherits from the class *YAML*. 

        from flashtool.setup.recipe import YAML
        
        class HDD(YAML):
            ...

    The valid keywords for the recipe must be added in a class attribute named
    *attr*. In this case we will provide a second class for the keyword
    *partition*. The constructor must also provide a parameter called
    *attributes*.

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
                self.check_attributes(attributes)
                ... # DO SOME VALUE CHECKS HERE
                YAML.__init__(self, attributes)

    The classes inherit the method `check_attributes(self, attributes)` from the
    super class *YAML*. It will check if the given attributes contains all
    keywords given in the class member *attr*. If not a exception will be
    raised.

    The last statement of the constructor is the call of the constructor of the
    super class *YAML*. It will save the attributes as attributes of the created
    object. It is now pssible to access the values of the attributes vith the
    dot `.` operator.

        hdd_obj.partition_type  # get partition types
        hdd_obj.partitions      # get list of partitions


3. Load attribute:
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
    

4. Now we can add a deploy class for the *hdd* recipe type. This class must be
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

            def __init__(self, recipe, actions, builds, platforms, auto):
                # do initialization steps for the class ...

            def prepare(self):
                # code for preparation steps of the hardware, like partition
                # the device

            def load(self):
                # loading products to the device.

        __entry__ = HddDeploy


    The setup routine will call first all `prepare()` methods of all objects
    which were specified in the *YAML* file and then all `load()` methods.
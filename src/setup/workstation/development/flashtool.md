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

The setup procedure reads in the recipe file first.

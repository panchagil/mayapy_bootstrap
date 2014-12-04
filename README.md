mayapy bootstrap
================

A base maya-python project with some useful tricks to help testing.
Some of the tricks I have gotten from the web and modify them for my purposes.
I will make and effort to search the original sources for this.

Features:
- reload of python module
- logger integrated with maya

Install
-----------------
The complete project is distributed as a maya module. To use the
project in maya,  copy the file 'myModule.mod' to
your MAYA_MODULE_PATH. Update the file to use the path to this
folder as MY_PATH


Examples
-----------------
* Run this code in maya to test how the reload works

``` python
import module

import mymodule
print mymodule.load_time()

import mymodule
print mymodule.load_time()

print 'reload module'
module.reload_module('mymodule')
import mymodule
print mymodule.load_time()
```

*  Run this code in maya to test the logger
``` python
import module
logger = module.get_logger(__name__)
logger.info('log level info')
```

MAYA_MODULE_PATH 
----------------
you can get the path using this mel command in maya:
```
getenv MAYA_MODULE_PATH
```



#mayapy bootstrap


A base maya-python project with some useful tricks to help testing.
Some of the tricks I have gotten from the web and modify them for my purposes.
I will make and effort to search the original sources for this.

Features:
- reload of python module
  - Maya has one instance of python running so the changes in your code don't get realoaded by maya. To reaload them you need to reload all your modules. 
  - I have added a small script that reloads all modules under a parent module. 

- logger integrated with maya
  - Maya has its own logger and you probably don't want to get them confused. 
  - I add a small setup to make it easier to use
  

##Install
The complete project is distributed as a maya module. To use the
project in maya,  copy the file 'myModule.mod' to
your MAYA_MODULE_PATH. Update the file to use the path to this
folder as MY_PATH

You can get the path using this mel command in maya:
```
getenv MAYA_MODULE_PATH
```

##Examples
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

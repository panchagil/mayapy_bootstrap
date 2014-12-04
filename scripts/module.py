import re
import sys
import logging

__author__ = 'pancha'


def reload_module(module):
    """
    Deletes all python modules under and including 'module'.
    Modules will be reloaded on demand when using include.

    :param module: the name of the parent module
    :return: None
    """
    reg = re.compile("%s$|%s\." % (module, module))
    for name in sys.modules.keys():
        if reg.match(name):
            del sys.modules[name]


# Set up logger for maya
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    # prevent logging from bubbling up to maya's logger
    logger.propagate = 0
    return logger


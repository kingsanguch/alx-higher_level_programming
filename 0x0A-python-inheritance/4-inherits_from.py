#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if obj inherits from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

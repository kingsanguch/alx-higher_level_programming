#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or a subclass"""
    return isinstance(obj, a_class)

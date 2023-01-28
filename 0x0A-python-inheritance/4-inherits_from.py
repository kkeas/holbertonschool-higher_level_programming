#!/usr/bin/python3
"""determines if an object directly or indirectly inherits from a class"""


def inherits_from(obj, a_class):
    """return true if obj is a subclass of a_class"""
    return issubclass(type(obj), a_class)

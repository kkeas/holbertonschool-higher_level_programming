#!/usr/bin/python3
"""determine if a_class is an instance of obj"""


def is_same_class(obj, a_class):
    """if instance true else false"""
    return a_class is type(obj)

#!/usr/bin/python3
"""base class"""


class BaseGeometry:
    """raise exception"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if value != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

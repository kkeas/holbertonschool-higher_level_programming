#!/usr/bin/python3
"""geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the rectangle subclass of base geometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        rect_string = "[Rectangle] "
        rect_string += str(self.__width) + "/" + str(self.__height)
        return rect_string

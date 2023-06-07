#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square subclass of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size property of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size property"""
        self.width = value
        self.height = value

    def __str__(self):
        """rets sqr info"""
        wht = "[Square] " + "({}) ".format(self.id)
        wht += "{}/{} - ".format(self.x, self.y)
        wht += "{}".format(self.width)
        return wht

    def update(self, *args, **kwargs):
        """update sqr args"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        else:
            for ky, vl in kwargs.items():
                setattr(self, ky, vl)

    def to_dictionary(self):
        """victor"""
        victor = {"id": self.id,
                   "size": self.width, "x": self.x, "y": self.y}
        return victor

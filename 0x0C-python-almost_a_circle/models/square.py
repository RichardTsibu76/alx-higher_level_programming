#!/usr/bin/python3
"""The Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that is inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor that initializes the Square class instances"""
        super().__init__(size, size, x, y, id)

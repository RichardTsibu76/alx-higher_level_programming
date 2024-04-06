#!/usr/bin/python3
"""This mod defines a function that adds new attributes"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

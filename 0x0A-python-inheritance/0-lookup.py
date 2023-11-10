#!/usr/bin/python3
"""This module contain function that looksup attributes and methods of classes"""

def lookup(obj):
    """Accepts an object and returns a list of attributes and methods

    Args:
        obj (class) - instance of a class
    """
    return dir(obj)

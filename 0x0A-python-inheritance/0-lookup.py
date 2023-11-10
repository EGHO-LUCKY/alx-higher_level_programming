#!/usr/bin/python3

def lookup(obj):
    """Accepts an object and returns a list of attributes and methods

    Args:
        obj (class) - instance of a class
    """
    return dir(obj)

#!/usr/bin/python3
"""This is a module on classes"""


class Square:
    """This class is used to define a square"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2

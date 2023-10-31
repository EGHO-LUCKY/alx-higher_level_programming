#!/usr/bin/python3
"""This is a module on classes"""


class Square:
    """This class is used to define a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #n stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
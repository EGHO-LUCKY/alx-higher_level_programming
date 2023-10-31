#!/usr/bin/python3
"""This is a module on classes"""


class Square:
    """This class is used to define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    """Sets the size of the square"""
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Specifies the position of a square
        Args: value is a tuple of two positive integers
        Raises: TypeError if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #n stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()

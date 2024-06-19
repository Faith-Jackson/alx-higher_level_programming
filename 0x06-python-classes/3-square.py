#!/usr/bin/python3
""" Defines a Square """


class Square:
    """ Representing a square """

    def __init__(self, size=0):
        """ Intializing the class attributes """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return (self.__size * self.__size)

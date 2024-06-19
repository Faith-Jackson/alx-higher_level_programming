#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ Represent a Square """

    def __init__(self, size=0):
        """ initialize the class attributes to be available
            to each instance of the class
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

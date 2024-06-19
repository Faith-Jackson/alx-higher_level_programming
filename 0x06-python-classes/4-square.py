#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Represent a Square """

    def __init__(self, size=0):
        """ Initializing the class attributes and making
            size a private attribute.
        """
        self.__size = size

    @property
    def size(self):
        """ Retrieve the private attribute size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size to value """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """ Returns the current square area """
        return self.size * self.size

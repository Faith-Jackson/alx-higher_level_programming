#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Represents a Square """

    def __init__(self, size=0):
        """ Initialize the class attribute """

        self.__size = size

    @property
    def size(self):
        """ To retrieve the private size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ To set the private size attribute to value """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

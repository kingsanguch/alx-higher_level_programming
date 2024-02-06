#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes a Square instance"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of a Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of a Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

#!/usr/bin/python3
"""
module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class
    """
    def __init__(self, width, height):
        """
        functio def
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        def func
        """
        return self.__width * self.__height

    def __str__(self):
        """
        func def
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

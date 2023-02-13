#!/usr/bin/python3
"""
class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class def
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        def of func
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

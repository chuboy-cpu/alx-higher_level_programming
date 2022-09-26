#!/usr/bin/python3

""" Defines a class that inherits from BaseGemetry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Represents a rectangle """
    def __init__(self, width, height):
        """ Initialise a new rectangle """
        self.integer_validator('width, width')
        self.__width = width
        self.integer_validator('heigt, height')
        self.__height = height
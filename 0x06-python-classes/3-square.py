#!/usr/bin/python3
'''The module that defines the class Square'''


class Square:
    '''The class defines a Square'''
    def __init__(self, size=0):
        '''The initialization method assigns value to an instance
        Args:
            size(int): The size of the Square of type int
        Attributes:
            self.__size: A private attribute
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size

    def area(self):
        '''The area of an object instantiated'''
        return self.__size ** 2

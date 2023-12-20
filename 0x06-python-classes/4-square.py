#!/usr/bin/python3
'''defines a class Square'''


class Square:
    '''The class defines a square'''
    def __init__(self, size=0):
        '''The initialization method assigns value to an object created
        Args:
            size(int): An integer passed as size of an instance
        Attributes:
            self.size = The setter for the self.__size
        '''
        self.size = size

    def area(self):
        '''Returns the area of the object'''
        return self.__size ** 2

    @property
    def size(self):
        '''The getter for an object of class Square'''
        return self.__size

    @size.setter
    def size(self, size):
        '''The setter for the object of class Square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size

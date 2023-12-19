#!/usr/bin/python3
'''a defined class Square which takes an int or nothing as input'''


class Square:
    '''The class defines a Square'''
    def __init__(self, size=0):
        '''The initilization method takes an integer or nothing
        Args:
            size(int): An integer
        Attributes:
            self.__size: A private attibute named size
        '''
        self.set_size(size)

    def set_size(self, size):
        '''The setter for self.__size
        Args:
            size(int): An integer or nothing
        Attributes:
            self.__size: A private attribute named size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size

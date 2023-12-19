#!/usr/bin/python3
'''The module defines a class Square of private attribute size'''


class Square:
    '''The class Square of private attribute size'''
    def __init__(self, size):
        '''initialization method of argument size
        Args:
            size: No type or value verification
        Attributes:
            size: Private instance attribute
        '''
        self.__size = size

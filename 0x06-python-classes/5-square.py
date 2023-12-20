#!/usr/bin/python3
'''defines a class Square'''


class Square:
    '''The class defines a Square'''
    def __init__(self, size=0):
        '''assigning size to an object through the initializing method
        Args:
            size(int): The size of the square
        Attributes:
            self.__size: A private instance/object attribute
        '''
        self.size = size

    @property
    def size(self):
        '''The getter for the object instantiated'''
        return self.__size

    @size.setter
    def size(self, size):
        '''The setter for the object'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return
        self.__size = size

    def area(self):
        '''Returns the area of the Square object created'''
        return self.__size ** 2

    def my_print(self):
        '''it Prints the square using # representation'''
        for c in range(self.__size):
            for d in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()

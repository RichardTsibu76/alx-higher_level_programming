#!/usr/bin/python3
# This module that enhances the operation of argv

from sys import argv

if __name__ == "__main__":

    number = len(argv)

    sum = 0

# The for loop

    for integer in range(1, number):

        sum += int(argv[integer])

    print("{}".format(sum))

#!/usr/bin/python3

from sys import argv, exit
if __name__ == "__main__":
    number_check = len(argv)
    if number_check == 1:
        print("{} arguments.".format(number_check - 1))
        exit(0)
    elif number_check == 2:
        print("{} argument:".format(number_check - 1))
    else:
        print("{} arguments:".format(number_check - 1))

    for i in range(1, number_check):
        print("{}: {}".format(i, argv[i]))

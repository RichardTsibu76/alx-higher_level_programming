#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        stor_len = len(my_list)
        my_list.reverse()
        for looper in my_list:
            print("{:d}".format(looper))

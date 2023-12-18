#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    record_from_list = 0

    try:

        for i in my_list:

            if record_from_list < x:

                print("{}".format(i), end="")

                record_from_list += 1
        print()

    except IndexError:

        print("Out of range")

    return record_from_list

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    count = 0
    try:
        for i in my_list:
            if count < x:
                try:
                    print("{:d}".format(i), end="")
                    count += 1
                    num += 1
                except (ValueError, TypeError):
                    count += 1
        print()
        return num
    except Exception:
        print()
        return num

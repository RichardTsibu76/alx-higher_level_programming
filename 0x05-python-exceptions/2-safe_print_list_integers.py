#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    figure = 0
    read_count = 0
    try:
        for i in my_list:
            if read_count < x:
                try:
                    print("{:d}".format(i), end="")
                    read_count += 1
                    figure += 1
                except (ValueError, TypeError):
                    read_count += 1
        print()
        return figure
    except Exception:
        print()
        return figure

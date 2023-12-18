#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    figure = 0
    check_count = 0
    try:
        for i in my_list:
            if check_count < x:
                try:
                    print("{:d}".format(i), end="")
                    check_count += 1
                    figure += 1
                except (ValueError, TypeError):
                    check_count += 1
        print()
        return figure
    except Exception:
        print()
        return figure

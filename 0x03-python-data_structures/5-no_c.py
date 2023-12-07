#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return ""
    num = len(my_string)
    idx = 0
    while idx < num:
        if idx == 0 and my_string[idx] != 'c' and my_string[idx] != 'C':
            new_str = my_string[idx]
        elif idx == 0 and (my_string[idx] == 'c' or my_string[idx] == 'C'):
            new_str = ""
        elif my_string[idx] == 'c' or my_string[idx] == 'C':
            pass
        # new_str += new_str[len(new_str):] + ""
        else:
            # new_str += new_str[len(new_str):] + my_string[idx]
            new_str += my_string[idx]
        idx = idx + 1
    return new_str

#!/usr/bin/python3
""" Module to print status code """
import sys


class Magic:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines != 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_of_a = len(tuple_a)
    len_of_b = len(tuple_b)
    if len_of_a < 2:
        if len_of_a == 0:
            tuple_a = (0, 0)
        else:
            tuple_a += 0,
    if len_of_b < 2:
        if len_of_b == 0:
            tuple_b = (0, 0)
        else:
            tuple_b += 0,
    c = tuple()
    for idx in range(2):
        c += (tuple_a[idx] + tuple_b[idx]),
    return c

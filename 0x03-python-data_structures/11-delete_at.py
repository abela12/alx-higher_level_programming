#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx > n - 1:
        return my_list
    else:
        del my_list[idx]
        return

#!/usr/bin/python3
def safe_print_integer(value):

    try:
        print('{:d}'.format(value))
    except Exception as error:
        return False
    else:
        return True

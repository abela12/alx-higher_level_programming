#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        return fct(*args)
    except Exception as exception:
        print('Exception: {}'.format(exception), file=sys.stderr)

#!/usr/bin/python3
def no_c(my_string):
    result = []
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            result.append(letter)
    return ''.join(result)

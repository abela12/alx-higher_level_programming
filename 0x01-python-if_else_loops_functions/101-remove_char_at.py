#!/usr/bin/python3
def remove_char_at(str, n):
    part = str[:n]
    parts = str[n+1:]
    return part + parts

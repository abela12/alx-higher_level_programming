#!/usr/bin/python3
""" add_attribute module """


def add_attribute(prmObject, prmName, prmValue):
    """ add_attribute function """
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)

#!/usr/bin/python3
def roman_value(prmCharacter):
    roman_list = [('I', 1), ('V', 5), ('X', 10),
                  ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    for item in roman_list:
        character, value = item
        if (prmCharacter is character):
            return value
    return None


def next_value(prmString, prmIndex):
    if prmIndex + 1 < len(prmString):
        return roman_value(prmString[prmIndex + 1])
    else:
        return None


def roman_to_int(roman_string):
    result = 0

    if (roman_string is None or isinstance(roman_string, str) is False):
        return result

    enum = enumerate(roman_string)
    for index, character in enum:
        currentValue = roman_value(character)
        nextValue = next_value(roman_string, index)
        if nextValue is None or currentValue >= nextValue:
            result += currentValue
        else:
            result += (nextValue - currentValue)
            next(enum)
    return result

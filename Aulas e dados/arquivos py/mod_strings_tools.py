

from re import split

def RemoveSpaces(my_string):
    strings = split(r'[;,\s]\s*', my_string)
    return strings
    
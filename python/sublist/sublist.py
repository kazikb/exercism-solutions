# Więcej informacji jak można sprawdzić czy lista A zawiera się w liście B
# https://www.geeksforgeeks.org/python-check-if-a-list-is-contained-in-another-list/

"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):

    if list_one == list_two: return EQUAL

    list_one_string = ','.join(map(str, list_one))
    list_two_string = ','.join(map(str, list_two))

    if list_one_string in list_two_string and len(list_one) < len(list_two): return SUBLIST
    if list_two_string in list_one_string and len(list_one) > len(list_two): return SUPERLIST
    return UNEQUAL

import re

def is_valid(isbn):

    if re.match("^\\d-?\\d{3}-?\\d{5}-?[\\d|X]$", isbn):

        if isbn[-1] == "X": value = 10
        else:  value = int(isbn[-1])

        multiplier = 2

        for item in isbn[-2::-1]:
            if not item.isdigit(): continue

            value += int(item) * multiplier
            multiplier += 1

        if value % 11 == 0: return True
    return False

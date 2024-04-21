# Czy dany znak jest literą sprawdzam za pomocą wbudowanej metody dla stringa
# https://docs.python.org/3/library/stdtypes.html

def is_isogram(string):
    string_list = list(string.lower())

    for letter in string_list:
        if letter.isalpha() and string_list.count(letter) > 1:
            return False
    return True

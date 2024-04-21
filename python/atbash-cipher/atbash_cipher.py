# Do rozwiązania tego problemu yykorzystuje maketrans - jest to dużo szybsze rozwiązania
# które dodatkowo sprawi że kod będzie bardziej czytelny.
# https://docs.python.org/3/library/stdtypes.html#str.translate
# https://docs.python.org/3/library/stdtypes.html#str.maketrans
#
# Poniższy zapis to tz. "ternary operator":
# Czyli zapisu warunku w jednej linii:
# >>> x=5
# >>> x if x >=0 else 0
# 5
# >>> x=-4
# >>> x if x >=0 else 0
# 0
#
# W złączeniu " ".join wykorzystuje "generator expression"
# który jest szybszy od porównania dwóch list.
# (expression for item in iterable)
#
# >>> l = ["a","b","c","f"]
# >>> " ".join(x.upper() for x in l)
# 'A B C F'
# >>> " ".join(x.upper() for x in l if x != "b")
# 'A C F'

import string

TRANSLATION = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

def encode(plain_text):

    cipher_text = ""

    cipher_text = "".join(letter.lower() for letter in plain_text if letter.isalnum()).translate(TRANSLATION)
    return " ".join(cipher_text[index:index+5] for index in range(0,len(cipher_text),5))

def decode(ciphered_text):
    return "".join(letter.lower() for letter in ciphered_text if letter.isalnum()).translate(TRANSLATION)

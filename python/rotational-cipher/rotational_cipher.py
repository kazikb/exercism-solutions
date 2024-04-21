# Tabela znaków ascii jako ściągawka
# https://www.asciitable.com/
# https://docs.python.org/3/library/functions.html
#
# Korzystam z wbudowanej funkcji "ord" która zwraca kod unicode znaku.
# Duże litery są w zakresie (A -> 65 Z -> 90)
# Małe litery są w zakresie (a -> 97 Z -> 122)
#
# Ponieważ szyfr Cezara zakłada że do każdej litery przypisana jest wartość 1 do 26
# dlatego najpierw odejmuje minimalną wartość dla dużej bądź małej litery, następnie
# wykonuje przesunięcie zgodnie ze wzorem: cypher_letter = (letter + key) % 26
# Ostatnim krokiem jest dodanie wartości pierwszego znaku (odpowiednio duże bądź małe litery)
# żeby uzyskać prawidłowy kod unicode.
#
# https://en.wikipedia.org/wiki/Caesar_cipher

def rotate(text, key):
    rotate_text = ""
    for item in text:
        if item.isalpha():
            if item.isupper(): rotate_text += chr((ord(item) - 65 + key) % 26 + 65)
            else: rotate_text +=  chr((ord(item) - 97 + key) % 26 + 97)
        else: rotate_text += item
    return rotate_text

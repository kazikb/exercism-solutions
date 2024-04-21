# Wzorowałem się na podejściu 2 opisanym pod tym linkiem:
# https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
# W pętli ustalam na jakiej pozycji z systemu 10 jest dana liczba względem systemy rzymskiego.
#
# Jako przykład weźmy liczbę 27 -> XXVII
# 1 przebieg:
# Liczba 2 (podstawa 10) odpowiada podstawie decimal_base = X * 2
# 2 przebieg
# Liczba 7 (podstawa 1) odpowiada 2 członowej cyfrze decimal_base = 1 * 10 / 2 -> V + decimal_base = I * 2
#
# Na koniec trzeba zmniejszyć podstawę od 10

ROMAN_NUMERAL = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

def roman(number):

    roman_number = ""
    decimal_base = 1000

    while number:
        number_position = number // decimal_base

        if number_position <= 3: roman_number += ROMAN_NUMERAL[decimal_base] * number_position
        elif number_position == 4:
            roman_number += ROMAN_NUMERAL[decimal_base] + ROMAN_NUMERAL[(decimal_base * 10) // 2]
        elif 5 <= number_position < 9:
            roman_number += ROMAN_NUMERAL[(decimal_base * 10) // 2] + ROMAN_NUMERAL[decimal_base] * (number_position - 5)
        else: roman_number += ROMAN_NUMERAL[decimal_base] + ROMAN_NUMERAL[decimal_base * 10]

        number = number % decimal_base
        decimal_base //= 10

    return roman_number

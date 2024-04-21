# Przeliczanie systemów liczbowych teoria:
# https://www-users.mat.umk.pl/~leii/PP/systemyLiczbowe.pdf
# https://mattomatti.com/pl/a40
#
# W pierwszej kolejności przeliczamy liczbę na system 10
# Następnie z systemu dziesiętnego na docelowy.
#
# Przeliczanie z systemu dziesiętnego na binarny:
# 1. Liczbę, którą chcesz zamienić podziel przez 2.
# 2. Reszta z dzielenia (0 lub 1) jest ostatnią cyfrą zapisy binarnego.
# 3. Weź część całkowitą z tego dzielenia i uczyń ją nową liczbą.
# 4. Podziel nową liczbę przez 2 i zapisz resztę jako kolejną (od końca) cyfrę zapisu binarnego.
# 5. Powtarzaj kroki 3-4 aż część całkowita z dzielenia nie będzie 0.
# 6. (Odwróć otrzymany zapis binarny)

def rebase(input_base, digits, output_base):

    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")

    decimal = 0
    digits_len = len(digits) - 1
    for index, digit in enumerate(digits):
        if 0 <= digit < input_base:
            decimal += input_base ** (digits_len - index) * digit
        else: raise ValueError("all digits must satisfy 0 <= d < input base")

    if decimal == 0: return [0]

    output = []
    while decimal > 0:
        output.insert(0, decimal % output_base)
        decimal = decimal // output_base

    return output

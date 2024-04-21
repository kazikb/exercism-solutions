# Aby przedstawić liczbę w formacie binarnym można skorzystać z funkcji "format" dla stringa
# https://docs.python.org/3/library/string.html#format-string-syntax
#
# >>> format(27%128, "07b")
# '0011011'
# 0: - numer pola
# 07 - rozwiń liczbę do 10 znaków i dodaj 0 na początku żeby wyrównać.
# b  - zmień na binarny
# >>> "{0:07b}".format(27)
# '0011011'
# >>> format(27%128, "010b")
# '0000011011'
# 0   - numer pola
# 010 - rozwiń liczbę do 10 znaków i dodaj 0 na początku żeby wyrównać.
# b   - zmień na binarny
# >>> "{0:010b}".format(27)
# '0000011011'

#region Example Solution
# https://en.wikipedia.org/wiki/Variable-length_quantity
# Zgodnie z opisem na wiki alternatywnej metody
#
# Another way to look at this is to represent the value in base-128 and then set the MSB of all but the last base-128 digit to 1.
#
# Funkcja encode
#
# 127 - 0x7F - '0b1111111'
# 128 - 0x80 - '0b10000000'
#   7 - 0x7  - '0b111'
#
# Przejdziemy konwersje liczby 0xFFFFFFFF
#
# >>> bin(int("0xFFFFFFFF", 16))
# '0b11111111111111111111111111111111'
#
# vlq = [number & 127]
# >>> bin(0b11111111111111111111111111111111 & 0b1111111)
# '0b1111111' # taka wartość jest zapisywana do tablicy vlq (zaczynamy konwersje od tyłu)
# number >>= 7
# >>> bin(0b11111111111111111111111111111111 >> 0b111)
# '0b1111111111111111111111111' # przesunięcie bitowe w prawo zmniejsza liczbę o 7 najniższych bitów czyli ostatni zakodowany fragment (za którym nie ma już kolejnych)
#
# Operacje w pętli while rozbite krok po kroku
# vlq.append(number & 127 | 128)
# number & 127 -> bierzemy 7 bitów danej liczby
# >>> bin(0b1111111111111111111111111 & 0b1111111)
# '0b1111111'
# number & 127 | 128 -> ustawiamy 8 MSb który mówi że za tym fragmentem znajduje się kolejny zakodowany fragment danej liczby
# >>> bin(0b1111111 | 0b10000000)
# '0b11111111'
# >>> bin(0b1111111111111111111111111 >> 0b111)
# '0b111111111111111111' # Taka wartość trafia do kolejnej iteracji pętli while

# def encode(numbers):
#     vlqs = []
#     for number in numbers:
#         vlq = [number & 127]
#         number >>= 7
#         while number > 0:
#             vlq.append(number & 127 | 128)
#             number >>= 7
#         vlqs.extend(reversed(vlq))
#     return vlqs

# Dekodowanie przejdziemy na przykładzie ciągu [0xC8, 0xE8, 0x56]
# Ponieważ number zaczyna od 0 to pierwsze przesunięcie nic nie robi
# >>> bin(0 << 0b111) -> number << 7
# '0b0'
# >>> int("0xC8",16)
# 200 -> wartość pierwszego byte
# >>> bin(0b11001000 & 0b1111111) -> (byte & 127)
# '0b1001000'
# >>> bin(0b0 | 0b1001000) -> (number << 7) | (byte & 127)
# '0b1001000'
#
# Sprawdzamy czy to był ostatni byte w liczbie i jeśli nie to przechodzimy do kolejnego byta
# >>> bin(0b11001000 & 0b10000000)
# '0b10000000'
# >>> if not 0b11001000 & 0b10000000: 'ok' -> if not byte & 128: sprawdza czy jest ustawiony MSb (8 bit)
# ...
#
# Drugi przebieg
# >>> bin(0b1001000 << 0b111) -> number << 7
# '0b10010000000000'
# >>> int("0xE8", 16)
# 232
# >>> bin(0b11101000 & 0b1111111) -> (byte & 127)
# '0b1101000'
# >>> bin(0b10010000000000 | 0b1101000) -> (number << 7) | (byte & 127)
# '0b10010001101000'
#
# Sprawdzamy czy to był ostatni byte w liczbie i jeśli nie to przechodzimy do kolejnego byta
# >>> bin(0b11101000 & 0b10000000)
# '0b10000000'
# >>> if not 0b11101000 & 0b10000000: 'ok'
# ...
#
# Trzeci przebieg (i ostatni)
# >>> bin(0b10010001101000 << 0b111 ) -> number << 7
# '0b100100011010000000000'
# >>> int("0x56", 16)
# 86
# >>> bin(0b1010110 & 0b1111111) -> (byte & 127)
# '0b1010110'
# >>> bin(0b100100011010000000000 | 0b1010110) -> (number << 7) | (byte & 127)
# '0b100100011010001010110'
#
# Sprawdzamy czy to był ostatni byte w liczbie i jeśli nie to przechodzimy do kolejnego byta
# >>> bin(0b1010110 & 0b10000000)
# '0b0'
# >>> if not 0b1010110 & 0b10000000: 'ok'
# ...
# 'ok'
#
# Dostajemy prawidłowy wynik
# >>> int("0b100100011010001010110", 2)
# 1193046
# >>> int("0x123456", 16)
# 1193046

# def decode(bytes_):
#     numbers = []
#     number = 0
#     unended = True
#     for byte in bytes_:
#         number = (number << 7) | (byte & 127)
#         if not byte & 128:
#             unended = False
#             numbers.append(number)
#             number = 0
#     if unended:
#         raise ValueError("incomplete sequence")
#     return numbers
#endregion Example Solution

# 127 - 0x7F - '0b1111111'
# 128 - 0x80 - '0b10000000'
#   7 - 0x7  - '0b111'
def encode(numbers):
    encode_numbers = []

    for number in numbers:
        number_vlq = []
        number_vlq.insert(0, (number & 0x7F))
        number = number >> 0x7

        while number > 0:
            number_vlq.insert(0, ((number & 0x7F) | 0x80))
            number = number >> 0x7

        encode_numbers.extend(number_vlq)

    return encode_numbers

def decode(bytes_):
    decode_numbers = []
    number = 0

    while len(bytes_) > 0:

        byte = bytes_.pop(0)

        number = ((number << 0x7) | (byte & 0x7F))
        if not byte & 0x80:
            decode_numbers.append(number)
            number = 0
            end_stream = True
        else:
            end_stream = False

    if not end_stream:
        raise ValueError("incomplete sequence")

    return decode_numbers

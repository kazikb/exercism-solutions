# Komentarz z jednego z zadań https://exercism.org/tracks/python/exercises/secret-handshake/solutions/IsaacG
# na którym się wzorowałem.
#
# I feel like I should share what I learned trying to understand this solution. The string number is converted to a number in binary form.
# number & 1 << x is interpreted as number & (1 << x) which means
# 1 << x : adds x zeros bits on the right of the starting 1 (1 << 2 is 100 in binary, i.e. 4, etc)
# then compute a "bitwise and" with number : for each bit of number and 1 << x, only output 1 if both bits are 1.
# As the 1 << x is just a one at the xth position, this is equivalent to selecting the xth bit of number.
#
# Mój przykład na podstawie liczby 5 -> b'101'
# if 5 & 1 << 0: print("ok") -> if b'101' & b'001'
# output: ok
# if 5 & 1 << 1: print("ok") -> if b'101' & b'010'
# output: ...
# if 5 & 1 << 2: print("ok") -> if b'101' & b'100'
# output: ok
#
# Zapis "int(binary_str, base=2)" mówi żeby string reprezentujący liczbę został skonwertowany na liczbę o podstawie n (tutaj 2).
# Czyli int("101", base=10) -> 101 a int("101", base=2) -> 5

def commands(binary_str):
    commands_list = ["wink", "double blink", "close your eyes", "jump"]
    binary = int(binary_str, base=2)
    return_handshake = []

    for index, item in enumerate(commands_list):
        if binary & 1 << index: return_handshake.append(item)
    if binary & 1 << 4: return_handshake.reverse()
    return return_handshake

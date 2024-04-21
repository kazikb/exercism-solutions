# Bardzo eleganckie rozwiązanie tego problemu dlatego je zapisałem żeby mi nie uciekło:
# https://exercism.org/tracks/python/exercises/pythagorean-triplet/solutions/knkua
#
# a**2 + b**2 = c**2
# a + b + c = N <->
# a**2 + b**2 = c**2
# a + b = N - c
# Solving system of equations for a and b
# D = sqrt(c**2 - N**2 + 2*N*c)
# a = (N - c - D)/2
# b = (N - c + D)/2
# D is real for c > N * (sqrt(2) - 1)
# And c < N/2 from the problem statement

from math import sqrt

def triplets_with_sum(number):
    triplets_list = []
    for c in range(int(number/2) - 1, int((sqrt(2) - 1) * number), -1):
        x = sqrt(c**2 - number**2 + 2 * number * c)
        if x == int(x):
            triplets_list.append([int((number - c -x) / 2), int((number - c + x) / 2), c])
    return triplets_list

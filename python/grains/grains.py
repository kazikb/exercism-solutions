# Ponieważ obliczenia liczby nasion to podnoszenie 2 do potęgi n można to zrobić na dwa sposoby:
#
# 2**64 - 1 -> standardowe podnoszenie liczby do potęgi za pomocą operatorów arytmetycznych.
# (1 << 64) - 1 -> przesunięcie bitowe które jest dużo szybsze i daje ten sam efekt.
#
# Informacje o obsłudze wyjątków
# https://docs.python.org/3/tutorial/errors.html#raising-exceptions
# https://docs.python.org/3/library/exceptions.html#base-classes
# https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement

"""
Calculate number of grains.
"""

def square(number):
    """ Function to calculate number of grains on a given square.

    :param number: int - square number.
    """
    #
    # Warunek może być zapisany na dwa sposoby:
    #
    # if number not in range(1,65):
    #
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    # return 2**(number - 1)
    return 1 << (number - 1)

def total():
    """

    Function to calculate total number of grains.
    """
    # return 2**64 - 1
    return (1 << 64) -1
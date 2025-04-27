def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    palindrom = None
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor -1, -1):
            candidate = i * j
            if palindrom is not None and candidate < palindrom:
                break
            if str(candidate) == str(candidate)[::-1]:
                if palindrom is None or candidate > palindrom:
                    palindrom = candidate
                    factors = [[i, j]]
                else:
                    factors.append([i, j])
    return (palindrom, factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    palindrom = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            candidate = i * j
            if palindrom is not None and candidate > palindrom:
                break
            if str(candidate) == str(candidate)[::-1]:
                if palindrom is None or candidate < palindrom:
                    palindrom = candidate
                    factors = [[i, j]]
                else:
                    factors.append([i, j])
    return (palindrom, factors)

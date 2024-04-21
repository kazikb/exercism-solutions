def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    sum = 0
    division = 1
    while division < number:
        if number % division == 0:
            sum += division
        division += 1

    if sum == number:
        return 'perfect'
    if sum > number:
        return 'abundant'
    return 'deficient'

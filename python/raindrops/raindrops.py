def convert(number):
    """
    Function to generate raindrop sound base on modulo operation.

    param: number: int - number to calculate.
    return: str - raindrop sound or number.
    """
    result = ''

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if result:
        return result
    else:
        return str(number)

COLOR_CODE_LIST = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]

def value(colors):
    """
    Function to return resistor value.

    :param colors: list - Two element list with colors of resistor.
    :return: int - Numeric value.
    """
    return COLOR_CODE_LIST.index(colors[0]) * 10 + COLOR_CODE_LIST.index(colors[1])

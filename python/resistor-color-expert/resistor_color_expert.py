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

TOLERANCE_LIST = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

UNITS_LIST = [
    "ohms",
    "kiloohms",
    "megaohms",
    "gigaohms"
]

def resistor_label(colors):

    # Przeglądam przekazaną listę i w zależności od jej wielkości
    # ustalam wartości dla parametrów tolerance i power które są
    # opcjonalne
    if len(colors) > 3:
        tolerance = TOLERANCE_LIST[colors.pop()]
        power = COLOR_CODE_LIST.index(colors.pop())
    elif len(colors) == 3:
        tolerance = None
        power = COLOR_CODE_LIST.index(colors.pop())
    else:
        tolerance = None
        power = 1

    # Tutaj wyliczam wartość rezystora na podstawie wartości 2 pierwszych pasków.
    ohms = 0
    for index, value in enumerate(colors):
        ohms += COLOR_CODE_LIST.index(value) * 10 ** (len(colors) - 1 - index)

    ohms *= 10 ** power

    if ohms > 10 ** 9:
        ohms = ohms / 10 ** 9
        unit = UNITS_LIST[3]
    elif ohms > 10 ** 6:
        ohms = ohms / 10 ** 6
        unit = UNITS_LIST[2]
    elif ohms > 10 ** 3:
        ohms = ohms / 10 ** 3
        unit = UNITS_LIST[1]
    else:
        unit = UNITS_LIST[0]

    # Zadanie wymagało dla liczb bez reszty zwracać tylko część całkowitą.
    if ohms % 1 == 0: ohms = int(ohms)

    if tolerance: return f"{ohms} {unit} \u00b1{tolerance}%"
    return f"{ohms} {unit}"
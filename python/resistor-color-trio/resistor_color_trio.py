# Wykorzystanie operacji "//" (dzielenie całkowite) pozwala na zastosowanie prefixów
# Brana jest część całkowita z dzielenia.
#
# Wiki odnośnie prefixów:
# https://en.wikipedia.org/wiki/Metric_prefix

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

def label(colors):
    ohms = (COLOR_CODE_LIST.index(colors[0]) * 10 + COLOR_CODE_LIST.index(colors[1])) * 10 ** COLOR_CODE_LIST.index(colors[2])

    if ohms > 10**9:
        return f"{ohms // 10**9} gigaohms"
    if ohms > 10**6:
        return f"{ohms // 10**6} megaohms"
    if ohms > 10**3:
        return f"{ohms // 10**3} kiloohms"
    return f"{ohms} ohms"

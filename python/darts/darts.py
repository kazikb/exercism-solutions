# Do rozwiązania tego problemu należy skorzystać z obliczenia promienia okręgu
# którego długość wyznacza iloczyn kartezjański. Wzór wygląda tak:
# x**2 + y**2 = r**2
#
# Dlatego należy wyciągnąć pierwiastek kwadratowy:
# (x**2 + y**2)**0.5
#
# Alternatywnie można to obliczyć z wykorzystaniem funkcji pierwiastka kwadratowego
# https://docs.python.org/3/library/math.html
#
# distance = math.sqrt(x ** 2 + y ** 2)

def score(x, y):
    """
    Function to calculate earned points for a single toss.

    param: x: float - x dimension
    param: y: float - y dimension
    return: int - number of points
    """

    distance = (x ** 2 + y ** 2) ** 0.5
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0

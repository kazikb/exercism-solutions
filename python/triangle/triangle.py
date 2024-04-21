def istriangle(sides):
    a, b, c = sides
    if (
        (a > 0 and b > 0 and c > 0) and
        (a + b >= c) and
        (a + c >= b) and
        (c + b >= a)
    ):
        return True
    else:
        return False

def equilateral(sides):
    return istriangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return istriangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return istriangle(sides) and len(set(sides)) == 3
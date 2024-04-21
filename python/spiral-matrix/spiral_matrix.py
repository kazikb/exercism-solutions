# Wzorcowe rozwiązanie tego problemu:
# https://exercism.org/tracks/python/exercises/spiral-matrix/solutions/glennj
#
# Funkcja next() https://docs.python.org/3/library/functions.html#next
# Bierze następny element z obiektu typu iterables
#
# https://docs.python.org/3/library/itertools.html#itertools.cycle
# cycle('ABCD') → A B C D A B C D A B C D ...
# W nieskończoność zwraca elementy w pętli z obiektu typu iterables

from itertools import cycle

def spiral_matrix(size):
    matrix = [[0] * size for i in range(size)]

    # Ten fragment mówi że poruszamy się zgodnie z ruchem wskazówek zegara.
    # Dzięki wykorzystaniu funkcji next() bierzemy kolejny element tuple(x, y)
    # a następnie przypisujemy wartości to zmiennych mr i mc za pomocą których
    # zmieniam wskaźnik w macierzy matrix.
    matrix_pointer = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    mr, mc = next(matrix_pointer)
    r, c = 0, 0

    for i in range(size**2):
        matrix[r][c] = i + 1
        r1 = r + mr
        c1 = c + mc

        # W warunku sprawdzam czy wartość r lub c nie jest mniejsza od 0 lub większa-równe od size
        # oraz czy dana wartość pod matrix[r][c] nie jest równa 0 (co by oznaczało że już to pole
        # wypełniłem). Jeżeli któryś z warunków zostanie spełniony zmieniam wartości mr i mc
        # poprzez rozpakowanie kolejnego tuple(x, y) zwróconego przez funkcję next().
        if (
           r1 < 0 or r1 >= size or
           c1 < 0 or c1 >= size or
           matrix[r1][c1] != 0
        ):
            mr, mc = next(matrix_pointer)

        r += mr
        c += mc

    return matrix

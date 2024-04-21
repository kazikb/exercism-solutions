# Można to rozwiązać z wykorzystaniem funkcji zip_longest
# https://docs.python.org/3/library/itertools.html#itertools.zip_longest
#
# Najpierw rozpakowujemy podany tekst i za pomocą funkcji zip_longest wyrównujemy
# linie do najdłuższej dostępnej za pomocą znaku wskazanego w `fillvalue`.
#
# lines = ["T", "EE", "AAA", "SSSS", "EEEEE", "RRRRRR"]
# matrix -> ['TEASER', '$EASER', '$$ASER', '$$$SER', '$$$$ER', '$$$$$R']

from itertools import zip_longest

def transpose(lines):
    matrix = zip_longest(*lines.splitlines(), fillvalue="$")
    matrix = ["".join(word) for word in matrix]
    return "\n".join(line.rstrip("$").replace("$", " ") for line in matrix)

# Alternatywnie można ten problem rozwiązać w poniższy sposób:
#
# def transpose(lines):
#     matrix = []
#     for i, line in enumerate(lines.splitlines()):
#         for j, char in enumerate(line):
#             if len(matrix) <= j:
#                 matrix.append([])
#             while len(matrix[j]) < i:
#                 matrix[j].append(" ")
#             matrix[j].append(char)

#     matrix = ["".join(item) for item in matrix]
#     return "\n".join(line for line in matrix)

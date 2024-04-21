BINARY_FONT_TO_STRING = (
    [" _ ", "| |", "|_|", "   "], # 0
    ["   ", "  |", "  |", "   "], # 1
    [" _ ", " _|", "|_ ", "   "], # 2
    [" _ ", " _|", " _|", "   "], # 3
    ["   ", "|_|", "  |", "   "], # 4
    [" _ ", "|_ ", " _|", "   "], # 5
    [" _ ", "|_ ", "|_|", "   "], # 6
    [" _ ", "  |", "  |", "   "], # 7
    [" _ ", "|_|", "|_|", "   "], # 8
    [" _ ", "|_|", " _|", "   "], # 9
)

def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for item in input_grid:
        if len(item) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    line_numbers = len(input_grid) // 4
    string_number = []

    for line in range(0,line_numbers):

        for column in range(0, (len(input_grid[line * 4]) // 3)):

            binary_number = []

            for x in range(line * 4,(line + 1) * 4):
                binary_number.append(input_grid[x][column * 3:(column + 1) * 3])

            string_number.append(
                    str(BINARY_FONT_TO_STRING.index(binary_number)) if binary_number in BINARY_FONT_TO_STRING else '?'
                )

        if line + 1 < line_numbers: string_number.append(",")

    return "".join(string_number)

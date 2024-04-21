# Porównanie czy dwa sety są równe
# https://docs.python.org/3/library/stdtypes.html?highlight=set#set
# len(set(minefield[y]).difference({" ","*"})) != 0
#
# Zapis `def annotate(minefield) -> []:` mówi jaki obiekt będzie zwracać funkcja.
# https://docs.python.org/3/library/typing.html

def annotate(minefield):

    if not minefield: return minefield

    x_len = len(minefield[0])
    y_len = len(minefield)
    out_minfield = minefield.copy()

    for x in range(x_len):

        # check x position and is there something before or after
        if x + 1 < x_len: x_after = True
        else: x_after = False
        if x - 1 >= 0: x_before = True
        else: x_before = False

        for y in range(y_len):

            print(set(minefield[y]))
            if len(minefield[y]) != x_len or len(set(minefield[y]).difference({" ","*"})) != 0:
                raise ValueError("The board is invalid with current input.")

            mine_counter = 0

            # check y position and is there something before or after
            if y + 1 < y_len: y_after = True
            else: y_after = False
            if y - 1 >= 0: y_before = True
            else: y_before = False

            # start checking fields
            if minefield[y][x] == "*": continue
            else:
                if y_before and x_before and minefield[y-1][x-1] == "*": mine_counter += 1
                if y_before and minefield[y-1][x] == "*": mine_counter += 1
                if y_before and x_after and minefield[y-1][x+1] == "*": mine_counter += 1
                if x_before and minefield[y][x-1] == "*": mine_counter += 1
                if x_after and minefield[y][x+1] == "*": mine_counter += 1
                if y_after and x_before and minefield[y+1][x-1] == "*": mine_counter += 1
                if y_after and minefield[y+1][x] == "*": mine_counter += 1
                if y_after and x_after and minefield[y+1][x+1] == "*": mine_counter += 1

                # modify row
                if mine_counter > 0:
                    row = list(out_minfield[y])
                    row[x] = str(mine_counter)
                    out_minfield[y] = "".join(row)

    return out_minfield
